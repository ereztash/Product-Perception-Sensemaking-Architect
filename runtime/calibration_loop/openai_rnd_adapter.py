#!/usr/bin/env python3
"""Strict R&D-only OpenAI adapter that preserves the runner's exact control-flow JSON shape."""

from __future__ import annotations

import json
import sys

from openai_resource_adapter import (
    LiveAdapterError,
    build_api_payload,
    extract_output_text,
    load_request,
    parse_json_object,
    post_response,
    validate_semantic_shape,
)


def main() -> int:
    try:
        request = load_request()
        if request.get("resource") != "RND":
            raise LiveAdapterError("request resource must be RND")
        api_payload = build_api_payload("RND", request)
        response = post_response(api_payload)
        semantic = parse_json_object(extract_output_text(response))
        validate_semantic_shape("RND", request.get("phase"), semantic)
        print(json.dumps(semantic, ensure_ascii=False))
        return 0
    except (LiveAdapterError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"adapter_error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
