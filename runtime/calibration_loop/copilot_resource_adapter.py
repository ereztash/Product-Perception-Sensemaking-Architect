#!/usr/bin/env python3
"""Best-effort GitHub Copilot CLI adapter for the canonical Calibration Loop.

This is an execution adapter only. It does not change R&D or Neta prompts, routing,
authority, or promotion rules. It reads one JSON request on stdin and writes one
semantic JSON object on stdout, matching the existing CommandAdapter contract.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MODEL = os.environ.get("COPILOT_MODEL", "gpt-5.4")
EFFORT = os.environ.get("COPILOT_REASONING_EFFORT", "high")

DEFAULT_PROMPTS = {
    "RND": "prompts/RND_AGENT_V0_2_CANDIDATE.md",
    "NETA": "prompts/SYSTEM.md",
}

NEED_KEYS = {
    "signal_interpretation_ambiguity",
    "multiple_plausible_mechanisms",
    "proxy_substitution_risk",
    "research_to_intervention_transition",
    "broad_reasoning_needed",
    "architecture_alternatives_needed",
    "novel_synthesis_needed",
    "external_research_needed",
    "owner_authority_needed",
    "repo_authority_needed",
    "environment_authority_needed",
    "field_authority_needed",
}


class AdapterError(RuntimeError):
    pass


def safe_text(ref: str) -> str:
    path = (ROOT / ref).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise AdapterError(f"reference escapes repository: {ref}") from exc
    if not path.is_file():
        raise AdapterError(f"reference not found: {ref}")
    return path.read_text(encoding="utf-8")


def bridge(resource: str, phase: object) -> str:
    if resource == "RND" and phase == "DIAGNOSE":
        return """# Runtime bridge contract
Return exactly ONE JSON object and no Markdown, with exactly these fields:
- material_question: non-empty string
- bottleneck: non-empty string
- resource_assessment: non-empty array; each item has exactly resource, expected_contribution, authority_ceiling, uncertainty (non-empty strings)
- candidate_moves: non-empty array; each item has exactly move, resource, expected_decision_value, reversibility (non-empty strings)
- needs: object containing exactly these boolean keys: signal_interpretation_ambiguity, multiple_plausible_mechanisms, proxy_substitution_risk, research_to_intervention_transition, broad_reasoning_needed, architecture_alternatives_needed, novel_synthesis_needed, external_research_needed, owner_authority_needed, repo_authority_needed, environment_authority_needed, field_authority_needed
- rationale: non-empty string
Do not add fields. Diagnose this specific task, not an example from the prompt."""
    if resource == "RND" and phase == "SYNTHESIZE":
        return """# Runtime bridge contract
Return exactly ONE JSON object and no Markdown, with exactly these fields:
- decision_before: string
- decision_after: string
- next_move: string
- resource_deltas: array; each item has resource, material (boolean), unique_delta
- learning_records: array of objects describing what future routing/allocation learned
- stop_or_continue: STOP or CONTINUE
- routing_amendment_proposed: null unless repeated evidence justifies an amendment
Preserve disagreements and authority ceilings. Same-model peer agreement is not independent triangulation. Synthesize this specific task, not an example from the prompt."""
    if resource == "NETA" and phase == "ANALYZE":
        return """# Runtime bridge contract
Return exactly ONE JSON object and no Markdown, with exactly these fields:
- resource: "NETA"
- summary: non-empty string
- unique_delta: non-empty string
- evidence_refs: array of strings; only references actually present in the runtime request
- limitations: array of strings
For this case discriminate the plausible mechanisms behind pre-move self-questions versus declarative insight/instruction. Do not infer FIELD behavior or outcome. Explicitly inspect ownership, attention allocation, metacognitive monitoring, transfer, cognitive load, and ritual/proxy risk without assuming any one is the mechanism."""
    raise AdapterError(f"unsupported resource/phase: {resource}/{phase}")


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


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(resource: str, phase: object, payload: dict) -> None:
    if resource == "RND" and phase == "DIAGNOSE":
        required = {"material_question", "bottleneck", "resource_assessment", "candidate_moves", "needs", "rationale"}
        if set(payload) != required:
            raise AdapterError(f"RND diagnosis fields drift: {sorted(set(payload) ^ required)}")
        if not all(nonempty(payload[k]) for k in ("material_question", "bottleneck", "rationale")):
            raise AdapterError("RND diagnosis strings must be non-empty")
        if not isinstance(payload["needs"], dict) or set(payload["needs"]) != NEED_KEYS or not all(isinstance(v, bool) for v in payload["needs"].values()):
            raise AdapterError("RND diagnosis needs shape drift")
        return
    if resource == "RND" and phase == "SYNTHESIZE":
        required = {"decision_before", "decision_after", "next_move", "resource_deltas", "learning_records", "stop_or_continue", "routing_amendment_proposed"}
        if set(payload) != required:
            raise AdapterError(f"RND synthesis fields drift: {sorted(set(payload) ^ required)}")
        if payload.get("stop_or_continue") not in {"STOP", "CONTINUE"}:
            raise AdapterError("RND synthesis stop_or_continue must be STOP or CONTINUE")
        return
    if resource == "NETA" and phase == "ANALYZE":
        required = {"resource", "summary", "unique_delta", "evidence_refs", "limitations"}
        if set(payload) != required or payload.get("resource") != "NETA":
            raise AdapterError("NETA semantic shape drift")
        if not nonempty(payload.get("summary")) or not nonempty(payload.get("unique_delta")):
            raise AdapterError("NETA summary/unique_delta must be non-empty")
        return
    raise AdapterError(f"unsupported validation target: {resource}/{phase}")


def main() -> int:
    try:
        request = json.load(sys.stdin)
        if not isinstance(request, dict):
            raise AdapterError("stdin must contain one JSON object")
        resource = request.get("resource")
        phase = request.get("phase")
        if resource not in DEFAULT_PROMPTS:
            raise AdapterError(f"unsupported resource: {resource}")

        prompt_ref = request.get("prompt_ref") or DEFAULT_PROMPTS[resource]
        parts = [safe_text(prompt_ref)]
        telos_ref = request.get("telos_ref")
        if telos_ref:
            parts.append("# Referenced telos document\n" + safe_text(telos_ref))
        parts.append(bridge(resource, phase))
        parts.append("# Runtime request\n" + json.dumps(request, ensure_ascii=False, sort_keys=True, indent=2))
        prompt = "\n\n".join(parts)

        command = [
            "copilot",
            "-p", prompt,
            "-s",
            "--no-ask-user",
            "--no-custom-instructions",
            "--model", MODEL,
            "--effort", EFFORT,
        ]
        proc = subprocess.run(command, text=True, capture_output=True, check=False)
        if proc.returncode != 0:
            detail = proc.stderr.strip() or proc.stdout.strip() or f"exit={proc.returncode}"
            raise AdapterError(f"Copilot CLI failed: {detail[:3000]}")

        semantic = extract_json(proc.stdout)
        validate(resource, phase, semantic)
        print(json.dumps(semantic, ensure_ascii=False))
        print(json.dumps({"adapter_provider": "github-copilot-cli", "model": MODEL, "effort": EFFORT, "resource": resource, "phase": phase}), file=sys.stderr)
        return 0
    except (AdapterError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"adapter_error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
