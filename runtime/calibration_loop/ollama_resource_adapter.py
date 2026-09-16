#!/usr/bin/env python3
"""Local Ollama adapter for Calibration Loop resources.

Runs entirely inside the GitHub Actions runner and therefore requires no external
model credential. The adapter preserves the same semantic contracts used by the
canonical Calibration Loop.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request

from openai_resource_adapter import (
    LiveAdapterError,
    load_request,
    parse_json_object,
    prompt_for,
    validate_semantic_shape,
)

API_URL = os.environ.get("OLLAMA_CHAT_URL", "http://127.0.0.1:11434/api/chat")
DEFAULT_MODEL = os.environ.get("OLLAMA_MODEL", "qwen3:4b-instruct")


def model_for(resource: str) -> str:
    return os.environ.get(f"CALIBRATION_{resource}_OLLAMA_MODEL", DEFAULT_MODEL)


def _nonempty_string() -> dict:
    return {"type": "string", "minLength": 1}


def _string_array() -> dict:
    return {"type": "array", "items": {"type": "string"}}


def schema_for(resource: str, phase: object) -> dict:
    """Return the exact semantic JSON schema expected by the canonical bridge.

    Ollama accepts a JSON Schema object in `format`. Using it here constrains only
    serialization/shape; the resource's native prompt still supplies the reasoning
    role and authority boundary.
    """
    if resource in {"NETA", "SCAFFOLD"}:
        return {
            "type": "object",
            "additionalProperties": False,
            "required": ["resource", "summary", "unique_delta", "evidence_refs", "limitations"],
            "properties": {
                "resource": {"type": "string", "enum": [resource]},
                "summary": _nonempty_string(),
                "unique_delta": _nonempty_string(),
                "evidence_refs": _string_array(),
                "limitations": _string_array(),
            },
        }

    if resource == "RND" and phase == "DIAGNOSE":
        delta_props = {
            key: {"type": "boolean"}
            for key in ("decision", "action", "reversal", "evidence", "allocation", "distinction")
        }
        needs_keys = (
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
        )
        return {
            "type": "object",
            "additionalProperties": False,
            "required": ["material_question", "bottleneck", "resource_assessment", "candidate_moves", "needs", "rationale"],
            "properties": {
                "material_question": _nonempty_string(),
                "bottleneck": _nonempty_string(),
                "resource_assessment": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["resource", "expected_contribution", "authority_ceiling", "uncertainty", "expected_delta"],
                        "properties": {
                            "resource": _nonempty_string(),
                            "expected_contribution": _nonempty_string(),
                            "authority_ceiling": _nonempty_string(),
                            "uncertainty": _nonempty_string(),
                            "expected_delta": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": list(delta_props),
                                "properties": delta_props,
                            },
                        },
                    },
                },
                "candidate_moves": {
                    "type": "array",
                    "minItems": 1,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["move", "resource", "expected_decision_value", "reversibility"],
                        "properties": {
                            "move": _nonempty_string(),
                            "resource": _nonempty_string(),
                            "expected_decision_value": _nonempty_string(),
                            "reversibility": _nonempty_string(),
                        },
                    },
                },
                "needs": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": list(needs_keys),
                    "properties": {key: {"type": "boolean"} for key in needs_keys},
                },
                "rationale": _nonempty_string(),
            },
        }

    if resource == "RND" and phase == "SYNTHESIZE":
        observed_props = {
            key: {"anyOf": [{"type": "null"}, _nonempty_string()]}
            for key in ("decision", "action", "reversal", "evidence", "allocation", "distinction")
        }
        return {
            "type": "object",
            "additionalProperties": False,
            "required": [
                "decision_before",
                "decision_after",
                "next_move",
                "resource_deltas",
                "learning_records",
                "stop_or_continue",
                "routing_amendment_proposed",
            ],
            "properties": {
                "decision_before": {"type": "string"},
                "decision_after": {"type": "string"},
                "next_move": {"type": "string"},
                "resource_deltas": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["resource", "material", "unique_delta", "observed_delta"],
                        "properties": {
                            "resource": _nonempty_string(),
                            "material": {"type": "boolean"},
                            "unique_delta": _nonempty_string(),
                            "observed_delta": {
                                "type": "object",
                                "additionalProperties": False,
                                "required": list(observed_props),
                                "properties": observed_props,
                            },
                        },
                    },
                },
                "learning_records": {"type": "array", "items": {"type": "object"}},
                "stop_or_continue": {"type": "string", "enum": ["STOP", "CONTINUE"]},
                "routing_amendment_proposed": {"anyOf": [{"type": "null"}, {"type": "object"}, {"type": "string"}]},
            },
        }

    raise LiveAdapterError(f"unsupported resource/phase: {resource}/{phase}")


def build_payload(resource: str, request: dict) -> dict:
    return {
        "model": model_for(resource),
        "stream": False,
        "format": schema_for(resource, request.get("phase")),
        "messages": [
            {"role": "system", "content": prompt_for(resource, request)},
            {
                "role": "user",
                "content": json.dumps(request, ensure_ascii=False, sort_keys=True),
            },
        ],
        "options": {
            "temperature": 0.1,
            "num_ctx": int(os.environ.get("OLLAMA_NUM_CTX", "32768")),
            "num_predict": int(os.environ.get("OLLAMA_NUM_PREDICT", "1600")),
        },
    }


def post_chat(payload: dict) -> dict:
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    timeout = int(os.environ.get("OLLAMA_TIMEOUT_SECONDS", "900"))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise LiveAdapterError(f"Ollama HTTP {exc.code}: {body[:2000]}") from exc
    except urllib.error.URLError as exc:
        raise LiveAdapterError(f"Ollama connection failed: {exc}") from exc


def extract_content(response: dict) -> str:
    message = response.get("message")
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, str) or not content.strip():
        raise LiveAdapterError("Ollama response contained no message content")
    return content.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--resource", choices=["RND", "NETA", "SCAFFOLD"], required=True)
    args = parser.parse_args()
    try:
        request = load_request()
        resource = args.resource
        if request.get("resource") != resource:
            raise LiveAdapterError(f"request resource must be {resource}")
        payload = build_payload(resource, request)
        response = post_chat(payload)
        semantic = parse_json_object(extract_content(response))
        validate_semantic_shape(resource, request.get("phase"), semantic)
        if resource in {"NETA", "SCAFFOLD"}:
            semantic["_adapter_meta"] = {
                "provider": "ollama-local",
                "model": payload["model"],
                "prompt_eval_count": response.get("prompt_eval_count"),
                "eval_count": response.get("eval_count"),
            }
        print(json.dumps(semantic, ensure_ascii=False))
        return 0
    except (LiveAdapterError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"adapter_error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
