#!/usr/bin/env python3
"""Local command adapter that drives Calibration Loop resources through the Claude CLI.

Transport only. Every semantic element is reused from the canonical live adapter:
prompt loading (`prompt_for`), the return-shape bridge contract, JSON extraction
(`parse_json_object`) and shape validation (`validate_semantic_shape`).

Provenance deviation, stated on purpose: this adapter reaches an Anthropic model,
not the `gpt-5.6-sol` configured in `openai-config.example.json`. Every resource it
serves therefore shares one model lineage, so agreement between R&D, Neta and
Scaffold is role-conditioned execution and is NOT independent triangulation.

Reads one JSON request on stdin, writes one semantic JSON object on stdout, exits
non-zero on execution failure. No key is stored in the repository.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from openai_resource_adapter import (  # noqa: E402
    LiveAdapterError,
    parse_json_object,
    prompt_for,
    validate_semantic_shape,
)

# The subprocess must reason from the request alone. No repository tool access, no
# MCP servers, no inherited project context.
DISABLED_TOOLS = [
    "Bash", "Edit", "Write", "Read", "Glob", "Grep", "NotebookEdit",
    "WebSearch", "WebFetch", "Task", "Agent", "TodoWrite", "SlashCommand", "Skill",
]

RESOURCE_META_FORBIDDEN = {"RND"}


def cli_binary() -> str:
    return os.environ.get("CALIBRATION_CLAUDE_BIN", "claude")


def model_for(resource: str) -> str:
    return (
        os.environ.get(f"CALIBRATION_{resource}_CLAUDE_MODEL")
        or os.environ.get("CALIBRATION_CLAUDE_MODEL")
        or "opus"
    )


def timeout_seconds() -> int:
    return int(os.environ.get("CALIBRATION_CLAUDE_TIMEOUT_SECONDS", "1500"))


def invoke_cli(system_prompt: str, user_input: str, model: str) -> dict:
    command = [
        cli_binary(),
        "-p",
        "--system-prompt", system_prompt,
        "--model", model,
        "--output-format", "json",
        "--restricted",
        "--strict-mcp-config",
        "--disallowed-tools", *DISABLED_TOOLS,
    ]
    # A neutral working directory keeps repository CLAUDE.md and any user-level
    # project context out of the invocation.
    with tempfile.TemporaryDirectory(prefix="calibration-adapter-") as workdir:
        try:
            completed = subprocess.run(
                command,
                input=user_input,
                capture_output=True,
                text=True,
                cwd=workdir,
                timeout=timeout_seconds(),
            )
        except FileNotFoundError as exc:
            raise LiveAdapterError(f"claude CLI not found: {exc}") from exc
        except subprocess.TimeoutExpired as exc:
            raise LiveAdapterError(f"claude CLI timed out after {timeout_seconds()}s") from exc

    if completed.returncode != 0:
        raise LiveAdapterError(
            f"claude CLI exited {completed.returncode}: {(completed.stderr or completed.stdout)[:2000]}"
        )
    try:
        envelope = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise LiveAdapterError(f"claude CLI returned non-JSON envelope: {completed.stdout[:1000]}") from exc
    if not isinstance(envelope, dict):
        raise LiveAdapterError("claude CLI envelope must be one JSON object")
    if envelope.get("is_error"):
        raise LiveAdapterError(f"claude CLI reported an error: {str(envelope)[:2000]}")
    return envelope


def extract_result_text(envelope: dict) -> str:
    text = envelope.get("result")
    if not isinstance(text, str) or not text.strip():
        raise LiveAdapterError("claude CLI envelope contained no result text")
    return text.strip()


def served_model(envelope: dict) -> str | None:
    usage = envelope.get("modelUsage")
    if isinstance(usage, dict) and usage:
        return sorted(usage)[0]
    return None


def provenance(resource: str, requested_model: str, envelope: dict) -> dict:
    return {
        "adapter": "claude_cli_adapter",
        "resource": resource,
        "transport": "claude CLI --print",
        "provider": "anthropic",
        "requested_model": requested_model,
        "served_model": served_model(envelope),
        "session_id": envelope.get("session_id"),
        "uuid": envelope.get("uuid"),
        "num_turns": envelope.get("num_turns"),
        "stop_reason": envelope.get("stop_reason"),
        "total_cost_usd": envelope.get("total_cost_usd"),
        "independence_caveat": (
            "Same model lineage as the other resources in this run. Agreement between "
            "resources is role-conditioned execution, not independent triangulation."
        ),
    }


def record_sidecar(record: dict) -> None:
    """Persist provenance the strict RND semantic shape cannot legally carry."""
    target = os.environ.get("CALIBRATION_ADAPTER_PROVENANCE")
    if not target:
        return
    path = Path(target)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--resource", choices=["RND", "NETA", "SCAFFOLD"], required=True)
    parser.add_argument("--print-request", action="store_true", help="Print the built invocation without calling the model")
    args = parser.parse_args()
    try:
        try:
            request = json.load(sys.stdin)
        except json.JSONDecodeError as exc:
            raise LiveAdapterError(f"stdin must contain one JSON object: {exc}") from exc
        if not isinstance(request, dict):
            raise LiveAdapterError("stdin must contain one JSON object")
        if request.get("resource") != args.resource:
            raise LiveAdapterError(f"request resource must be {args.resource}")

        system_prompt = prompt_for(args.resource, request)
        user_input = json.dumps(request, ensure_ascii=False, sort_keys=True)
        model = model_for(args.resource)

        if args.print_request:
            print(json.dumps({
                "resource": args.resource,
                "model": model,
                "system_prompt_chars": len(system_prompt),
                "input_chars": len(user_input),
                "disallowed_tools": DISABLED_TOOLS,
            }, ensure_ascii=False, indent=2))
            return 0

        envelope = invoke_cli(system_prompt, user_input, model)
        semantic = parse_json_object(extract_result_text(envelope))
        validate_semantic_shape(args.resource, request.get("phase"), semantic)

        meta = provenance(args.resource, model, envelope)
        meta["phase"] = request.get("phase")
        record_sidecar(meta)

        # RND control-flow shapes are validated for exact keys by the runner, so
        # provenance for RND lives only in the sidecar. Neta/Scaffold retain it inline.
        if args.resource not in RESOURCE_META_FORBIDDEN:
            semantic["_adapter_meta"] = meta

        print(json.dumps(semantic, ensure_ascii=False))
        return 0
    except (LiveAdapterError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"adapter_error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
