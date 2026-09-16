#!/usr/bin/env python3
"""GitHub Models adapter for Calibration Loop resources.

Reads one JSON request from stdin and writes one semantic JSON result to stdout.
Uses the automatic GitHub Actions GITHUB_TOKEN with `models: read`; no external
provider secret is required.
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

API_URL = os.environ.get(
    "GITHUB_MODELS_URL",
    "https://models.github.ai/inference/chat/completions",
)
DEFAULT_MODEL = os.environ.get("GITHUB_MODELS_MODEL", "openai/gpt-5")


def model_for(resource: str) -> str:
    return os.environ.get(f"CALIBRATION_{resource}_GITHUB_MODEL", DEFAULT_MODEL)


def build_payload(resource: str, request: dict) -> dict:
    return {
        "model": model_for(resource),
        "messages": [
            {"role": "system", "content": prompt_for(resource, request)},
            {
                "role": "user",
                "content": json.dumps(request, ensure_ascii=False, sort_keys=True),
            },
        ],
    }


def post_chat(payload: dict) -> dict:
    token = os.environ.get("GITHUB_MODELS_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise LiveAdapterError("GITHUB_MODELS_TOKEN or GITHUB_TOKEN is required")
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "X-GitHub-Api-Version": "2026-03-10",
        },
        method="POST",
    )
    timeout = int(os.environ.get("GITHUB_MODELS_TIMEOUT_SECONDS", "180"))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise LiveAdapterError(f"GitHub Models HTTP {exc.code}: {body[:2000]}") from exc
    except urllib.error.URLError as exc:
        raise LiveAdapterError(f"GitHub Models connection failed: {exc}") from exc


def extract_content(response: dict) -> str:
    choices = response.get("choices")
    if not isinstance(choices, list) or not choices:
        raise LiveAdapterError("GitHub Models response contained no choices")
    message = choices[0].get("message") if isinstance(choices[0], dict) else None
    content = message.get("content") if isinstance(message, dict) else None
    if not isinstance(content, str) or not content.strip():
        raise LiveAdapterError("GitHub Models response contained no message content")
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
        # Keep semantic contract clean for RND because run.py validates exact fields.
        if resource in {"NETA", "SCAFFOLD"}:
            semantic["_adapter_meta"] = {
                "provider": "github-models",
                "model": payload["model"],
                "response_id": response.get("id"),
            }
        print(json.dumps(semantic, ensure_ascii=False))
        return 0
    except (LiveAdapterError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"adapter_error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
