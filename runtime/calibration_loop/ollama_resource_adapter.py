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


def _nonempty_string(max_length: int | None = None) -> dict:
    schema: dict = {"type": "string", "minLength": 1}
    if max_length is not None:
        schema["maxLength"] = max_length
    return schema


def _string_array(max_items: int | None = None, item_max_length: int | None = None) -> dict:
    schema: dict = {
        "type": "array",
        "items": _nonempty_string(item_max_length) if item_max_length else {"type": "string"},
    }
    if max_items is not None:
        schema["maxItems"] = max_items
    return schema


def schema_for(resource: str, request: dict) -> dict:
    """Return the exact semantic JSON schema expected by the canonical bridge.

    Ollama accepts a JSON Schema object in `format`. Using it here constrains only
    serialization/shape; the resource's native prompt still supplies the reasoning
    role and authority boundary. For synthesis, the schema also binds resource
    deltas to the peers actually invoked by the deterministic router so R&D cannot
    accidentally report itself as a peer or spend its budget restating the task.
    """
    phase = request.get("phase")

    if resource in {"NETA", "SCAFFOLD"}:
        return {
            "type": "object",
            "additionalProperties": False,
            "required": ["resource", "summary", "unique_delta", "evidence_refs", "limitations"],
            "properties": {
                "resource": {"type": "string", "enum": [resource]},
                "summary": _nonempty_string(700),
                "unique_delta": _nonempty_string(420),
                "evidence_refs": _string_array(max_items=8, item_max_length=180),
                "limitations": _string_array(max_items=6, item_max_length=220),
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
                "material_question": _nonempty_string(420),
                "bottleneck": _nonempty_string(520),
                "resource_assessment": {
                    "type": "array",
                    "minItems": 1,
                    "maxItems": 7,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["resource", "expected_contribution", "authority_ceiling", "uncertainty", "expected_delta"],
                        "properties": {
                            "resource": _nonempty_string(40),
                            "expected_contribution": _nonempty_string(320),
                            "authority_ceiling": _nonempty_string(260),
                            "uncertainty": _nonempty_string(280),
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
                    "maxItems": 5,
                    "items": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": ["move", "resource", "expected_decision_value", "reversibility"],
                        "properties": {
                            "move": _nonempty_string(360),
                            "resource": _nonempty_string(40),
                            "expected_decision_value": _nonempty_string(320),
                            "reversibility": _nonempty_string(240),
                        },
                    },
                },
                "needs": {
                    "type": "object",
                    "additionalProperties": False,
                    "required": list(needs_keys),
                    "properties": {key: {"type": "boolean"} for key in needs_keys},
                },
                "rationale": _nonempty_string(700),
            },
        }

    if resource == "RND" and phase == "SYNTHESIZE":
        expected_resources = [
            item.get("resource")
            for item in request.get("resource_results", [])
            if isinstance(item, dict) and isinstance(item.get("resource"), str) and item.get("resource")
        ]
        observed_props = {
            key: {"anyOf": [{"type": "null"}, _nonempty_string(240)]}
            for key in ("decision", "action", "reversal", "evidence", "allocation", "distinction")
        }
        resource_schema = (
            {"type": "string", "enum": expected_resources}
            if expected_resources
            else _nonempty_string(40)
        )
        resource_deltas: dict = {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["resource", "material", "unique_delta", "observed_delta"],
                "properties": {
                    "resource": resource_schema,
                    "material": {"type": "boolean"},
                    "unique_delta": _nonempty_string(320),
                    "observed_delta": {
                        "type": "object",
                        "additionalProperties": False,
                        "required": list(observed_props),
                        "properties": observed_props,
                    },
                },
            },
        }
        if expected_resources:
            resource_deltas["minItems"] = len(expected_resources)
            resource_deltas["maxItems"] = len(expected_resources)
        else:
            resource_deltas["maxItems"] = 0

        compact_learning_record = {
            "type": "object",
            "maxProperties": 4,
            "additionalProperties": {
                "anyOf": [
                    {"type": "null"},
                    {"type": "boolean"},
                    {"type": "number"},
                    {"type": "string", "maxLength": 280},
                ]
            },
        }
        compact_amendment = {
            "type": "object",
            "maxProperties": 4,
            "additionalProperties": {
                "anyOf": [
                    {"type": "null"},
                    {"type": "boolean"},
                    {"type": "number"},
                    {"type": "string", "maxLength": 280},
                ]
            },
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
                "decision_before": _nonempty_string(360),
                "decision_after": _nonempty_string(420),
                "next_move": _nonempty_string(520),
                "resource_deltas": resource_deltas,
                "learning_records": {
                    "type": "array",
                    "maxItems": 3,
                    "items": compact_learning_record,
                },
                "stop_or_continue": {"type": "string", "enum": ["STOP", "CONTINUE"]},
                "routing_amendment_proposed": {
                    "anyOf": [
                        {"type": "null"},
                        {"type": "string", "maxLength": 360},
                        compact_amendment,
                    ]
                },
            },
        }

    raise LiveAdapterError(f"unsupported resource/phase: {resource}/{phase}")


def build_payload(resource: str, request: dict) -> dict:
    phase = request.get("phase")
    if resource == "RND" and phase == "SYNTHESIZE":
        num_predict = int(os.environ.get("OLLAMA_SYNTH_NUM_PREDICT", os.environ.get("OLLAMA_NUM_PREDICT", "2200")))
    else:
        num_predict = int(os.environ.get("OLLAMA_NUM_PREDICT", "1600"))
    return {
        "model": model_for(resource),
        "stream": False,
        "format": schema_for(resource, request),
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
            "num_predict": num_predict,
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
