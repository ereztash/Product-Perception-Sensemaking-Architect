#!/usr/bin/env python3
"""Live OpenAI Responses API adapter for Calibration Loop resources.

Reads one JSON request from stdin and writes one semantic JSON result to stdout.
No API key is stored in the repository.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
API_URL = os.environ.get("OPENAI_RESPONSES_URL", "https://api.openai.com/v1/responses")
DEFAULT_MODEL = os.environ.get("OPENAI_MODEL", "gpt-5.6-sol")
DEFAULT_EFFORT = os.environ.get("OPENAI_REASONING_EFFORT", "high")

RESOURCE_DEFAULT_PROMPTS = {
    "RND": "prompts/RND_AGENT_V0_2_CANDIDATE.md",
    "NETA": "prompts/SYSTEM.md",
    "SCAFFOLD": "prompts/SCAFFOLD_RESOURCE_V0_1.md",
}


class LiveAdapterError(RuntimeError):
    pass


def env_for(resource: str, suffix: str, default: str | None = None) -> str | None:
    return os.environ.get(f"CALIBRATION_{resource}_{suffix}", os.environ.get(f"OPENAI_{suffix}", default))


def load_request() -> dict:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        raise LiveAdapterError(f"stdin must contain one JSON object: {exc}") from exc
    if not isinstance(payload, dict):
        raise LiveAdapterError("stdin must contain one JSON object")
    return payload


def safe_repo_path(ref: str) -> Path:
    candidate = (ROOT / ref).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError as exc:
        raise LiveAdapterError(f"prompt_ref escapes repository: {ref}") from exc
    if not candidate.is_file():
        raise LiveAdapterError(f"prompt_ref not found: {ref}")
    return candidate


def prompt_for(resource: str, request: dict) -> str:
    ref = request.get("prompt_ref") or RESOURCE_DEFAULT_PROMPTS[resource]
    if not isinstance(ref, str) or not ref.strip():
        raise LiveAdapterError("prompt_ref must be a non-empty string")
    parts = [safe_repo_path(ref).read_text(encoding="utf-8")]
    telos_ref = request.get("telos_ref")
    if telos_ref is not None:
        if not isinstance(telos_ref, str) or not telos_ref.strip():
            raise LiveAdapterError("telos_ref must be a non-empty string when present")
        parts.append("\n# Referenced telos document\n" + safe_repo_path(telos_ref).read_text(encoding="utf-8"))
    parts.append(bridge_contract(resource, request.get("phase")))
    return "\n\n".join(parts)


def bridge_contract(resource: str, phase: object) -> str:
    if resource == "RND" and phase == "DIAGNOSE":
        return """# Adapter bridge contract\nReturn exactly ONE JSON object and no Markdown. Required fields:\n- material_question: non-empty string\n- bottleneck: non-empty string\n- resource_assessment: non-empty array; each item has exactly resource, expected_contribution, authority_ceiling, uncertainty (all non-empty strings)\n- candidate_moves: non-empty array; each item has exactly move, resource, expected_decision_value, reversibility (all non-empty strings)\n- needs: object containing exactly these boolean keys: signal_interpretation_ambiguity, multiple_plausible_mechanisms, proxy_substitution_risk, research_to_intervention_transition, broad_reasoning_needed, architecture_alternatives_needed, novel_synthesis_needed, external_research_needed, owner_authority_needed, repo_authority_needed, environment_authority_needed, field_authority_needed\n- rationale: non-empty string\nDo not add fields."""
    if resource == "RND" and phase == "SYNTHESIZE":
        return """# Adapter bridge contract\nReturn exactly ONE JSON object and no Markdown. Required fields:\n- decision_before: string\n- decision_after: string\n- next_move: string\n- resource_deltas: array of objects, each with resource, material (boolean), unique_delta\n- learning_records: array of objects describing what future routing/allocation learned\n- stop_or_continue: STOP or CONTINUE\n- routing_amendment_proposed: null unless repeated evidence justifies a proposed routing change\nPreserve conflicts and authority ceilings. Do not treat same-model peer agreement as independent triangulation."""
    if resource in {"NETA", "SCAFFOLD"}:
        return f"""# Adapter bridge contract\nReturn exactly ONE JSON object and no Markdown with exactly these fields:\n- resource: \"{resource}\"\n- summary: non-empty string\n- unique_delta: non-empty string\n- evidence_refs: array of strings; only references actually present in the request\n- limitations: array of strings\nDo not add fields."""
    raise LiveAdapterError(f"unsupported resource/phase: {resource}/{phase}")


def model_for(resource: str) -> str:
    return env_for(resource, "MODEL", DEFAULT_MODEL) or DEFAULT_MODEL


def effort_for(resource: str) -> str:
    return env_for(resource, "REASONING_EFFORT", DEFAULT_EFFORT) or DEFAULT_EFFORT


def web_search_enabled(resource: str) -> bool:
    raw = env_for(resource, "WEB_SEARCH", "0") or "0"
    return raw.strip().lower() in {"1", "true", "yes", "on"}


def build_api_payload(resource: str, request: dict) -> dict:
    payload: dict = {
        "model": model_for(resource),
        "instructions": prompt_for(resource, request),
        "input": json.dumps(request, ensure_ascii=False, sort_keys=True),
        "reasoning": {"effort": effort_for(resource)},
        "max_output_tokens": int(env_for(resource, "MAX_OUTPUT_TOKENS", "8000") or "8000"),
    }
    if web_search_enabled(resource):
        payload["tools"] = [{"type": "web_search"}]
    return payload


def post_response(payload: dict) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise LiveAdapterError("OPENAI_API_KEY is required for live adapter execution")
    request = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    timeout = int(os.environ.get("OPENAI_TIMEOUT_SECONDS", "180"))
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise LiveAdapterError(f"OpenAI API HTTP {exc.code}: {body[:2000]}") from exc
    except urllib.error.URLError as exc:
        raise LiveAdapterError(f"OpenAI API connection failed: {exc}") from exc


def extract_output_text(response: dict) -> str:
    direct = response.get("output_text")
    if isinstance(direct, str) and direct.strip():
        return direct.strip()
    texts: list[str] = []
    for item in response.get("output", []):
        if not isinstance(item, dict) or item.get("type") != "message":
            continue
        for content in item.get("content", []):
            if isinstance(content, dict) and content.get("type") == "output_text" and isinstance(content.get("text"), str):
                texts.append(content["text"])
    if texts:
        return "\n".join(texts).strip()
    raise LiveAdapterError("OpenAI response contained no output_text")


def parse_json_object(text: str) -> dict:
    stripped = text.strip()
    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", stripped, flags=re.DOTALL | re.IGNORECASE)
    if fenced:
        stripped = fenced.group(1).strip()
    try:
        payload = json.loads(stripped)
    except json.JSONDecodeError as exc:
        raise LiveAdapterError(f"model returned non-JSON semantic output: {stripped[:1000]}") from exc
    if not isinstance(payload, dict):
        raise LiveAdapterError("model semantic output must be one JSON object")
    return payload


def validate_semantic_shape(resource: str, phase: object, payload: dict) -> None:
    if resource in {"NETA", "SCAFFOLD"}:
        required = {"resource", "summary", "unique_delta", "evidence_refs", "limitations"}
        if set(payload) != required:
            raise LiveAdapterError(f"{resource} semantic fields drift: {sorted(set(payload) ^ required)}")
        if payload.get("resource") != resource:
            raise LiveAdapterError(f"{resource} semantic resource identity mismatch")
        if not all(isinstance(payload.get(k), str) and payload[k].strip() for k in ("summary", "unique_delta")):
            raise LiveAdapterError(f"{resource} summary/unique_delta must be non-empty")
        if not isinstance(payload.get("evidence_refs"), list) or not all(isinstance(x, str) for x in payload["evidence_refs"]):
            raise LiveAdapterError(f"{resource} evidence_refs must be string array")
        if not isinstance(payload.get("limitations"), list) or not all(isinstance(x, str) for x in payload["limitations"]):
            raise LiveAdapterError(f"{resource} limitations must be string array")
    elif resource == "RND" and phase == "DIAGNOSE":
        required = {"material_question", "bottleneck", "resource_assessment", "candidate_moves", "needs", "rationale"}
        if set(payload) != required:
            raise LiveAdapterError(f"RND diagnosis fields drift: {sorted(set(payload) ^ required)}")
    elif resource == "RND" and phase == "SYNTHESIZE":
        required = {"decision_before", "decision_after", "next_move", "resource_deltas", "learning_records", "stop_or_continue", "routing_amendment_proposed"}
        missing = required - set(payload)
        if missing:
            raise LiveAdapterError(f"RND synthesis missing fields: {sorted(missing)}")
    else:
        raise LiveAdapterError(f"unsupported resource/phase: {resource}/{phase}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--resource", choices=["RND", "NETA", "SCAFFOLD"], required=True)
    parser.add_argument("--print-request", action="store_true", help="Print the OpenAI request payload without calling the API")
    args = parser.parse_args()
    try:
        request = load_request()
        if request.get("resource") != args.resource:
            raise LiveAdapterError(f"request resource must be {args.resource}")
        api_payload = build_api_payload(args.resource, request)
        if args.print_request:
            print(json.dumps(api_payload, ensure_ascii=False, indent=2))
            return 0
        response = post_response(api_payload)
        semantic = parse_json_object(extract_output_text(response))
        validate_semantic_shape(args.resource, request.get("phase"), semantic)
        # Metadata is deliberately nested so the semantic contract remains visible and lineage is retained.
        semantic["_adapter_meta"] = {
            "provider": "openai",
            "model": api_payload["model"],
            "reasoning_effort": api_payload["reasoning"]["effort"],
            "web_search_enabled": bool(api_payload.get("tools")),
            "response_id": response.get("id"),
        }
        print(json.dumps(semantic, ensure_ascii=False))
        return 0
    except (LiveAdapterError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"adapter_error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
