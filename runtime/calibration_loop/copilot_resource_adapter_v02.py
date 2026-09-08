#!/usr/bin/env python3
"""Best-effort GitHub Copilot CLI adapter for Calibration Loop v0.2.

This is an execution adapter only. Canonical prompts, routing, authority ceilings,
and the v0.2 delta-accounting contract remain owned by the main runtime.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys

from openai_resource_adapter import prompt_for, validate_semantic_shape


class AdapterError(RuntimeError):
    pass


def extract_json(text: str) -> dict:
    raw = text.strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", raw, flags=re.DOTALL | re.IGNORECASE)
    if fenced:
        raw = fenced.group(1).strip()
    try:
        value = json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        if start < 0:
            raise AdapterError(f"Copilot returned no JSON object: {raw[:1000]}")
        try:
            value, _ = json.JSONDecoder().raw_decode(raw[start:])
        except json.JSONDecodeError as exc:
            raise AdapterError(f"Copilot returned invalid JSON: {raw[:1000]}") from exc
    if not isinstance(value, dict):
        raise AdapterError("semantic output must be one JSON object")
    return value


def exact_runtime_bridge(resource: str, phase: object, request: dict) -> str:
    if resource == "RND" and phase == "SYNTHESIZE":
        routed = ((request.get("routing") or {}).get("resources") or [])
        return (
            "\n\n# Exact runner invariant\n"
            f"routing.resources is exactly {json.dumps(routed, ensure_ascii=False)}. "
            "resource_deltas MUST contain exactly those routed peer resources, in exactly that order. "
            "Never include RND DIAGNOSE or RND SYNTHESIZE in resource_deltas. "
            "If routing.resources is empty, resource_deltas MUST be []. "
            "For each routed peer, material must equal whether at least one observed_delta dimension is non-null."
        )
    return ""


def main() -> int:
    try:
        request = json.load(sys.stdin)
        if not isinstance(request, dict):
            raise AdapterError("stdin must contain one JSON object")
        resource = request.get("resource")
        phase = request.get("phase")
        if resource not in {"RND", "NETA", "SCAFFOLD"}:
            raise AdapterError(f"unsupported resource: {resource}")

        canonical_prompt = prompt_for(resource, request)
        runtime_request = json.dumps(request, ensure_ascii=False, sort_keys=True, indent=2)
        instruction = (
            canonical_prompt
            + exact_runtime_bridge(resource, phase, request)
            + "\n\n# Runtime request\n"
            + runtime_request
            + "\n\nDo the current runtime task only. Return the exact JSON shape required above."
        )
        command = [
            "copilot",
            "-p",
            instruction,
            "-s",
            "--no-ask-user",
            "--no-custom-instructions",
        ]
        proc = subprocess.run(command, text=True, capture_output=True, check=False)
        if proc.returncode != 0:
            detail = proc.stderr.strip() or proc.stdout.strip() or f"exit={proc.returncode}"
            raise AdapterError(f"Copilot CLI failed: {detail[:3000]}")

        semantic = extract_json(proc.stdout)
        validate_semantic_shape(resource, phase, semantic)
        print(json.dumps(semantic, ensure_ascii=False))
        return 0
    except (AdapterError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"adapter_error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
