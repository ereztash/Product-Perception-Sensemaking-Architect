#!/usr/bin/env python3
"""Execute Calibration Loop v0.1 with deterministic routing and pluggable resource adapters."""

from __future__ import annotations

import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from validate_calibration_task import ContractError, validate as validate_task  # noqa: E402
from adapters import (  # noqa: E402
    AdapterError,
    CommandAdapter,
    mock_neta_result,
    mock_rnd_diagnosis,
    mock_rnd_synthesis,
    mock_scaffold_result,
)
from routing import ALL_NEED_KEYS, route  # noqa: E402


class RuntimeErrorBounded(RuntimeError):
    pass


def load_json(path: Path) -> dict:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeErrorBounded(f"{path} must contain one JSON object")
    return payload


def load_config(path: Path | None) -> dict:
    if path is None:
        return {"adapters": {}}
    payload = load_json(path)
    adapters = payload.get("adapters", {})
    if not isinstance(adapters, dict):
        raise RuntimeErrorBounded("config.adapters must be an object")
    for resource, cfg in adapters.items():
        if resource not in {"RND", "NETA", "SCAFFOLD"}:
            raise RuntimeErrorBounded(f"unsupported command adapter resource: {resource}")
        if not isinstance(cfg, dict) or set(cfg) != {"command"}:
            raise RuntimeErrorBounded(f"adapter {resource} must contain only command")
        command = cfg["command"]
        if not isinstance(command, list) or not command or not all(isinstance(x, str) and x for x in command):
            raise RuntimeErrorBounded(f"adapter {resource}.command must be a non-empty string array")
    return payload


def validate_diagnosis(payload: dict) -> None:
    required = {"material_question", "bottleneck", "needs", "rationale"}
    if set(payload) != required:
        raise RuntimeErrorBounded(f"R&D diagnosis fields drift: {sorted(set(payload) ^ required)}")
    for key in ("material_question", "bottleneck", "rationale"):
        if not isinstance(payload[key], str) or not payload[key].strip():
            raise RuntimeErrorBounded(f"R&D diagnosis {key} must be non-empty")
    needs = payload["needs"]
    if not isinstance(needs, dict) or set(needs) != ALL_NEED_KEYS:
        missing = ALL_NEED_KEYS - set(needs) if isinstance(needs, dict) else ALL_NEED_KEYS
        extra = set(needs) - ALL_NEED_KEYS if isinstance(needs, dict) else set()
        raise RuntimeErrorBounded(f"R&D diagnosis needs drift: missing={sorted(missing)} extra={sorted(extra)}")
    if not all(isinstance(v, bool) for v in needs.values()):
        raise RuntimeErrorBounded("all R&D diagnosis needs must be booleans")


def adapter_map(config: dict) -> dict[str, CommandAdapter]:
    return {
        resource: CommandAdapter(resource=resource, command=cfg["command"])
        for resource, cfg in config.get("adapters", {}).items()
    }


def resource_request(resource: str, task: dict, fired: list[str]) -> dict:
    base = {
        "resource": resource,
        "phase": "ANALYZE",
        "task": task,
        "requested_focus": fired,
        "independence_rule": "Analyze the task independently. Do not infer another resource's conclusion and do not turn agreement into independent evidence.",
    }
    if resource == "NETA":
        base["prompt_ref"] = "prompts/SYSTEM.md"
        base["role_boundary"] = "Challenge framing, proxy substitution, mechanism collapse and premature intervention. Do not decide external research validity or architecture doctrine."
    elif resource == "SCAFFOLD":
        base["role_boundary"] = "Provide broad expert reasoning and candidate alternatives. Treat your output as a scaffold/candidate source, not ground truth."
    return base


def invoke_resource(resource: str, request: dict, adapters: dict[str, CommandAdapter], mock: bool) -> dict:
    if mock:
        if resource == "NETA":
            return mock_neta_result(request)
        if resource == "SCAFFOLD":
            return mock_scaffold_result(request)
        raise RuntimeErrorBounded(f"no mock for resource {resource}")
    adapter = adapters.get(resource)
    if adapter is None:
        raise RuntimeErrorBounded(f"adapter not configured: {resource}")
    result = adapter.invoke(request)
    result.setdefault("resource", resource)
    if result.get("resource") != resource:
        raise RuntimeErrorBounded(f"{resource} adapter returned mismatched resource identity")
    return result


def rnd_diagnose(task: dict, adapters: dict[str, CommandAdapter], mock: bool) -> tuple[dict | None, dict]:
    request = {
        "resource": "RND",
        "phase": "DIAGNOSE",
        "prompt_ref": "prompts/RND_AGENT_V0_1.md",
        "task": task,
        "instruction": "Identify the live calibration bottleneck and return the exact v0.1 diagnosis shape expected by the runner.",
    }
    if mock:
        diagnosis = mock_rnd_diagnosis(task)
        validate_diagnosis(diagnosis)
        return diagnosis, request
    adapter = adapters.get("RND")
    if adapter is None:
        return None, request
    diagnosis = adapter.invoke(request)
    validate_diagnosis(diagnosis)
    return diagnosis, request


def rnd_synthesize(task: dict, diagnosis: dict, route_payload: dict, results: list[dict], adapters: dict[str, CommandAdapter], mock: bool) -> tuple[dict | None, dict]:
    request = {
        "resource": "RND",
        "phase": "SYNTHESIZE",
        "prompt_ref": "prompts/RND_AGENT_V0_1.md",
        "task": task,
        "diagnosis": diagnosis,
        "routing": route_payload,
        "resource_results": results,
        "instruction": "Compare resource deltas, update the blocked decision, choose the cheapest next move, and record what the system learned about resource usefulness. Do not average disagreements away.",
    }
    if mock:
        return mock_rnd_synthesis(task, diagnosis, results, route_payload), request
    adapter = adapters.get("RND")
    if adapter is None:
        return None, request
    synthesis = adapter.invoke(request)
    if not isinstance(synthesis, dict):
        raise RuntimeErrorBounded("R&D synthesis must be object")
    return synthesis, request


def run(task: dict, config: dict, mock: bool, strict: bool) -> dict:
    validate_task(task)
    adapters = adapter_map(config)
    trace: dict = {
        "runtime_version": "0.1",
        "task": task,
        "diagnosis": None,
        "routing": None,
        "resource_invocations": [],
        "synthesis": None,
        "final_state": None,
        "failure": None,
    }

    diagnosis, diag_request = rnd_diagnose(task, adapters, mock)
    trace["resource_invocations"].append({
        "resource": "RND",
        "phase": "DIAGNOSE",
        "request": diag_request,
        "state": "COMPLETE" if diagnosis is not None else "PENDING_RESOURCE",
    })
    if diagnosis is None:
        if strict:
            raise RuntimeErrorBounded("RND adapter is required in --strict mode")
        trace["final_state"] = "PENDING_RESOURCE"
        return trace

    trace["diagnosis"] = diagnosis
    decision = route(diagnosis, task["allowed_resources"])
    route_payload = decision.as_dict()
    trace["routing"] = route_payload

    max_calls = (task.get("budget") or {}).get("max_resource_calls")
    required_calls = 2 + len(decision.resources)
    if max_calls is not None and required_calls > max_calls:
        raise RuntimeErrorBounded(f"routing requires {required_calls} resource calls but budget allows {max_calls}")

    requests = {
        resource: resource_request(resource, task, route_payload["fired"].get(resource, []))
        for resource in decision.resources
    }

    missing = [r for r in decision.resources if not mock and r not in adapters]
    if missing:
        for resource in decision.resources:
            trace["resource_invocations"].append({
                "resource": resource,
                "phase": "ANALYZE",
                "request": requests[resource],
                "state": "PENDING_RESOURCE" if resource in missing else "READY",
            })
        if strict:
            raise RuntimeErrorBounded(f"required adapters not configured: {missing}")
        trace["final_state"] = "PENDING_RESOURCE"
        return trace

    results: list[dict] = []
    max_parallel = (task.get("budget") or {}).get("max_parallel_calls", 1)
    if requests:
        with ThreadPoolExecutor(max_workers=min(max_parallel, len(requests))) as pool:
            future_map = {
                pool.submit(invoke_resource, resource, request, adapters, mock): resource
                for resource, request in requests.items()
            }
            by_resource: dict[str, dict] = {}
            for future in as_completed(future_map):
                resource = future_map[future]
                by_resource[resource] = future.result()
            for resource in decision.resources:
                result = by_resource[resource]
                results.append(result)
                trace["resource_invocations"].append({
                    "resource": resource,
                    "phase": "ANALYZE",
                    "request": requests[resource],
                    "result": result,
                    "state": "COMPLETE",
                })

    synthesis, synth_request = rnd_synthesize(task, diagnosis, route_payload, results, adapters, mock)
    trace["resource_invocations"].append({
        "resource": "RND",
        "phase": "SYNTHESIZE",
        "request": synth_request,
        "state": "COMPLETE" if synthesis is not None else "PENDING_RESOURCE",
    })
    if synthesis is None:
        if strict:
            raise RuntimeErrorBounded("RND synthesis adapter unavailable")
        trace["final_state"] = "PENDING_RESOURCE"
        return trace

    trace["synthesis"] = synthesis
    trace["final_state"] = "AUTHORITY_STOP" if decision.authority_handoffs and not decision.resources else "COMPLETE"
    return trace


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", type=Path)
    parser.add_argument("--config", type=Path)
    parser.add_argument("--mock", action="store_true", help="Use deterministic built-in mock resources for CI/development only")
    parser.add_argument("--strict", action="store_true", help="Fail when a required adapter is not configured")
    parser.add_argument("--output", type=Path, help="Persist the full trace JSON")
    args = parser.parse_args()

    try:
        task = load_json(args.task)
        config = load_config(args.config)
        trace = run(task, config=config, mock=args.mock, strict=args.strict)
    except (OSError, json.JSONDecodeError, ContractError, AdapterError, RuntimeErrorBounded, ValueError) as exc:
        trace = {
            "runtime_version": "0.1",
            "task_ref": str(args.task),
            "final_state": "FAILED_EXECUTION",
            "failure": str(exc),
        }
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(trace, ensure_ascii=False, indent=2))
        return 1

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(trace, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(trace, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
