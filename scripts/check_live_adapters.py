#!/usr/bin/env python3
"""Offline controls for live OpenAI Calibration Loop adapters.

These tests never call the network and require no API key.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "runtime" / "calibration_loop"
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))

from openai_resource_adapter import (  # noqa: E402
    LiveAdapterError,
    build_api_payload,
    parse_json_object,
    prompt_for,
    validate_semantic_shape,
)


def main() -> int:
    task = json.loads((ROOT / "fixtures" / "calibration-valid-task.json").read_text(encoding="utf-8"))

    rnd_request = {
        "resource": "RND",
        "phase": "DIAGNOSE",
        "prompt_ref": "prompts/RND_AGENT_V0_2_CANDIDATE.md",
        "telos_ref": "research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md",
        "task": task,
        "instruction": "diagnose",
    }
    rnd_prompt = prompt_for("RND", rnd_request)
    assert "resource↔telos calibration" in rnd_prompt
    assert "external_research_needed" in rnd_prompt
    rnd_api = build_api_payload("RND", rnd_request)
    assert rnd_api["model"]
    assert rnd_api["reasoning"]["effort"]
    assert "tools" not in rnd_api

    old = os.environ.get("CALIBRATION_RND_WEB_SEARCH")
    os.environ["CALIBRATION_RND_WEB_SEARCH"] = "1"
    try:
        with_web = build_api_payload("RND", rnd_request)
        assert with_web["tools"] == [{"type": "web_search"}]
    finally:
        if old is None:
            os.environ.pop("CALIBRATION_RND_WEB_SEARCH", None)
        else:
            os.environ["CALIBRATION_RND_WEB_SEARCH"] = old

    neta_request = {
        "resource": "NETA",
        "phase": "ANALYZE",
        "prompt_ref": "prompts/SYSTEM.md",
        "task": task,
        "requested_focus": ["proxy_substitution_risk"],
    }
    neta_prompt = prompt_for("NETA", neta_request)
    assert 'resource: "NETA"' in neta_prompt
    validate_semantic_shape(
        "NETA",
        "ANALYZE",
        {
            "resource": "NETA",
            "summary": "Bounded analysis.",
            "unique_delta": "A proxy risk was exposed.",
            "evidence_refs": [],
            "limitations": ["No field observation."],
        },
    )

    scaffold_request = {
        "resource": "SCAFFOLD",
        "phase": "ANALYZE",
        "task": task,
        "requested_focus": ["architecture_alternatives_needed"],
    }
    scaffold_prompt = prompt_for("SCAFFOLD", scaffold_request)
    assert "external reasoning scaffold" in scaffold_prompt.lower()

    fenced = parse_json_object('```json\n{"resource":"SCAFFOLD"}\n```')
    assert fenced["resource"] == "SCAFFOLD"

    try:
        validate_semantic_shape("NETA", "ANALYZE", {"resource": "NETA"})
    except LiveAdapterError:
        pass
    else:
        raise AssertionError("invalid Neta output unexpectedly passed")

    print("LIVE ADAPTER CONTROLS OK: prompts, routing payloads, web-search toggle and semantic shapes validated offline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
