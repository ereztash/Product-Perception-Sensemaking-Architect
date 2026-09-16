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


def build_payload(resource: str, request: dict) -> dict:
    return {
        "model": model_for(resource),
        "stream": False,
        "format": "json",
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
