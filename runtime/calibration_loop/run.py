#!/usr/bin/env python3
"""Execute Calibration Loop v0.2 with deterministic routing and measurable resource deltas."""

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


DELTA_DIMENSIONS = (
    "decision",
    "action",
    "reversal",
    "evidence",
    "allocation",
    "distinction",
)


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


def _nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_expected_delta(value: object, context: str) -> None:
    if not isinstance(value, dict) or set(value) != set(DELTA_DIMENSIONS):
        raise RuntimeErrorBounded(f"{context} must contain exactly delta dimensions {list(DELTA_DIMENSIONS)}")
    if not all(isinstance(value[key], bool) for key in DELTA_DIMENSIONS):
        raise RuntimeErrorBounded(f"{context} delta dimensions must be booleans")


def validate_observed_delta(value: object, context: str) -> None:
    if not isinstance(value, dict) or set(value) != set(DELTA_DIMENSIONS):
        raise RuntimeErrorBounded(f"{context} must contain exactly delta dimensions {list(DELTA_DIMENSIONS)}")
    for key in DELTA_DIMENSIONS:
        item = value[key]
        if item is not None and not _nonempty(item):
            raise RuntimeErrorBounded(f"{context}.{key} must be null or a non-empty string")


def delta_is_material(observed_delta: dict) -> bool:
    return any(observed_delta[key] is not None for key in DELTA_DIMENSIONS)


def validate_diagnosis(payload: dict) -> None:
    required = {
        "material_question",
        "bottleneck",
        "resource_assessment",
        "candidate_moves",
        "needs",
        "rationale",
    }
    if set(payload) != required:
        raise RuntimeErrorBounded(f"R&D diagnosis fields drift: {sorted(set(payload) ^ required)}")
    for key in ("material_question", "bottleneck", "rationale"):
        if not _nonempty(payload[key]):
            raise RuntimeErrorBounded(f"R&D diagnosis {key} must be non-empty")

    assessments = payload["resource_assessment"]
    if not isinstance(assessments, list) or not assessments:
        raise RuntimeErrorBounded("resource_assessment must be a non-empty array")
    assessment_fields = {"resource", "expected_contribution", "authority_ceiling", "uncertainty", "expected_delta"}
    seen_resources: set[str] = set()
    for i, item in enumerate(assessments):
        if not isinstance(item, dict) or set(item) != assessment_fields:
            raise RuntimeErrorBounded(f"resource_assessment[{i}] fields drift")
        for key in ("resource", "expected_contribution", "authority_ceiling", "uncertainty"):
            if not _nonempty(item[key]):
                raise RuntimeErrorBounded(f"resource_assessment[{i}].{key} must be a non-empty string")
        if item["resource"] in seen_resources:
            raise RuntimeErrorBounded(f"resource_assessment contains duplicate resource: {item['resource']}")
        seen_resources.add(item["resource"])
        validate_expected_delta(item["expected_delta"], f"resource_assessment[{i}].expected_delta")

    moves = payload["candidate_moves"]
    if not isinstance(moves, list) or not moves:
        raise RuntimeErrorBounded("candidate_moves must be a non-empty array")
    move_fields = {"move", "resource", "expected_decision_value", "reversibility"}
    for i, item in enumerate(moves):
        if not isinstance(item, dict) or set(item) != move_fields:
            raise RuntimeErrorBounded(f"candidate_moves[{i}] fields drift")
        if not all(_nonempty(item[k]) for k in move_fields):
            raise RuntimeErrorBounded(f"candidate_moves[{i}] values must be non-empty strings")

    needs = payload["needs"]
    if not isinstance(needs, dict) or set(needs) != ALL_NEED_KEYS:
        missing = ALL_NEED_KEYS - set(needs) if isinstance(needs, dict) else ALL_NEED_KEYS
        extra = set(needs) - ALL_NEED_KEYS if isinstance(needs, dict) else set()
        raise RuntimeErrorBounded(f"R&D diagnosis needs drift: missing={sorted(missing)} extra={sorted(extra)}")
    if not all(isinstance(v, bool) for v in needs.values()):
        raise RuntimeErrorBounded("all R&D diagnosis needs must be booleans")


def expected_delta_for_resource(diagnosis: dict, resource: str) -> dict:
    matches = [
        item["expected_delta"]
        for item in diagnosis["resource_assessment"]
        if item["resource"] == resource
    ]
    if len(matches) != 1:
        raise RuntimeErrorBounded(
            f"routed resource {resource} must have exactly one ex-ante expected_delta in resource_assessment"
        )
    return dict(matches[0])


def validate_synthesis(payload: dict, routed_resources: tuple[str, ...] | list[str]) -> None:
    required = {
        "decision_before",
        "decision_after",
        "next_move",
        "resource_deltas",
        "learning_records",
        "stop_or_continue",
        "routing_amendment_proposed",
    }
    if not isinstance(payload, dict):
        raise RuntimeErrorBounded("R&D synthesis must be object")
    missing = required - set(payload)
    extra = set(payload) - required - {"_adapter_meta"}
    if missing or extra:
        raise RuntimeErrorBounded(f"R&D synthesis fields drift: missing={sorted(missing)} extra={sorted(extra)}")
    for key in ("decision_before", "decision_after", "next_move"):
        if not _nonempty(payload[key]):
            raise RuntimeErrorBounded(f"R&D synthesis {key} must be non-empty")
    if payload["stop_or_continue"] not in {"STOP", "CONTINUE"}:
        raise RuntimeErrorBounded("R&D synthesis stop_or_continue must be STOP or CONTINUE")
    if not isinstance(payload["learning_records"], list):
        raise RuntimeErrorBounded("R&D synthesis learning_records must be an array")

    deltas = payload["resource_deltas"]
    if not isinstance(deltas, list):
        raise RuntimeErrorBounded("R&D synthesis resource_deltas must be an array")
    expected_resources = list(routed_resources)
    seen: list[str] = []
    delta_fields = {"resource", "material", "unique_delta", "observed_delta"}
    for i, item in enumerate(deltas):
        if not isinstance(item, dict) or set(item) != delta_fields:
            raise RuntimeErrorBounded(f"resource_deltas[{i}] fields drift")
        resource = item["resource"]
        if not _nonempty(resource):
            raise RuntimeErrorBounded(f"resource_deltas[{i}].resource must be non-empty")
        if resource in seen:
            raise RuntimeErrorBounded(f"duplicate resource delta: {resource}")
        seen.append(resource)
        if not isinstance(item["material"], bool):
            raise RuntimeErrorBounded(f"resource_deltas[{i}].material must be boolean")
        if not _nonempty(item["unique_delta"]):
            raise RuntimeErrorBounded(f"resource_deltas[{i}].unique_delta must be non-empty")
        validate_observed_delta(item["observed_delta"], f"resource_deltas[{i}].observed_delta")
        derived = delta_is_material(item["observed_delta"])
        if item["material"] != derived:
            raise RuntimeErrorBounded(
                f"resource_deltas[{i}].material={item['material']} conflicts with observed_delta-derived material={derived}"
            )
    if seen != expected_resources:
        raise RuntimeErrorBounded(
            f"resource_deltas must preserve routed resource order exactly: expected={expected_resources} got={seen}"
        )


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
        "prompt_ref": "prompts/RND_AGENT_V0_2_CANDIDATE.md",
        "telos_ref": "research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md",
        "task": task,
        "instruction": "Diagnose resource↔telos miscalibration, map candidate resource moves, commit ex ante to which decision-state dimensions each assessed resource could change, and return exactly the Calibration Loop v0.2 diagnosis shape.",
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
        "prompt_ref": "prompts/RND_AGENT_V0_2_CANDIDATE.md",
        "telos_ref": "research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md",
        "task": task,
        "diagnosis": diagnosis,
        "routing": route_payload,
        "resource_results": results,
        "instruction": "Compare resource deltas against the ex-ante expected_delta commitments, update the blocked decision, choose the cheapest next calibration move, and record what the system learned about future resource allocation. For each invoked resource, report observed_delta by decision/action/reversal/evidence/allocation/distinction. Do not average disagreements away.",
    }
    if mock:
        return mock_rnd_synthesis(task, diagnosis, results, route_payload), request
    adapter = adapters.get("RND")
    if adapter is None:
        return None, request
    synthesis = adapter.invoke(request)
    return synthesis, request


def annotate_peer_invocations(trace: dict, synthesis: dict) -> None:
    by_resource = {item["resource"]: item for item in synthesis["resource_deltas"]}
    for invocation in trace["resource_invocations"]:
        if invocation.get("phase") != "ANALYZE" or invocation.get("resource") not in by_resource:
            continue
        delta = by_resource[invocation["resource"]]
        invocation["observed_delta"] = delta["observed_delta"]
        invocation["material"] = delta["material"]


def run(task: dict, config: dict, mock: bool, strict: bool) -> dict:
    validate_task(task)
    adapters = adapter_map(config)
    trace: dict = {
        "runtime_version": "0.2",
        "rnd_telos_version": "0.2-candidate",
        "task": task,
        "diagnosis": None,
        "routing": None,
        "resource_invocations": [],
        "synthesis": None,
        "final_state": None,
        "failure": None,
    }
    try:
        return _run(task, trace, adapters, mock, strict)
    except Exception as exc:
        # A FAILED RUN KEPT WHAT IT ALREADY PAID FOR.
        #
        # `main` used to build a fresh two-line trace on any exception, so a run that reached the
        # R&D synthesis and failed its shape check discarded the diagnosis, the routing decision and
        # every peer result underneath it -- the expensive part, thrown away at the cheapest step.
        # The failure is still a failure and the exit code is unchanged; what is preserved is the
        # evidence of how far the loop got, which is what makes the next attempt cheaper than the
        # last. The exception type is not swallowed: it is re-raised carrying the partial trace.
        exc.partial_trace = trace  # type: ignore[attr-defined]
        raise


def _run(task: dict, trace: dict, adapters: dict, mock: bool, strict: bool) -> dict:
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

    expected_deltas = {
        resource: expected_delta_for_resource(diagnosis, resource)
        for resource in decision.resources
    }
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
                "expected_delta": expected_deltas[resource],
                "observed_delta": None,
                "material": None,
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
                    "expected_delta": expected_deltas[resource],
                    "observed_delta": None,
                    "material": None,
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

    validate_synthesis(synthesis, decision.resources)
    trace["synthesis"] = synthesis
    annotate_peer_invocations(trace, synthesis)
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
        # Whatever the run reached before it failed, when it reached anything at all. A task that
        # could not be read or a config that would not parse has no partial trace and falls back to
        # the two-line shape this always wrote.
        partial = getattr(exc, "partial_trace", None)
        trace = dict(partial) if isinstance(partial, dict) else {
            "runtime_version": "0.2",
            "rnd_telos_version": "0.2-candidate",
        }
        trace["task_ref"] = str(args.task)
        trace["final_state"] = "FAILED_EXECUTION"
        trace["failure"] = str(exc)
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
