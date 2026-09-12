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
    assert "expected_delta" in rnd_prompt
    assert all(name in rnd_prompt for name in ("decision", "action", "reversal", "evidence", "allocation", "distinction"))
    rnd_api = build_api_payload("RND", rnd_request)
    assert rnd_api["model"]
    assert rnd_api["reasoning"]["effort"]
    assert "tools" not in rnd_api

    synth_request = {
        "resource": "RND",
        "phase": "SYNTHESIZE",
        "prompt_ref": "prompts/RND_AGENT_V0_2_CANDIDATE.md",
        "telos_ref": "research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md",
        "task": task,
        "diagnosis": {},
        "routing": {},
        "resource_results": [],
        "instruction": "synthesize",
    }
    synth_prompt = prompt_for("RND", synth_request)
    assert "observed_delta" in synth_prompt
    assert "material MUST equal" in synth_prompt
    assert "restatement" in synth_prompt

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
    assert "expected_delta" in neta_prompt
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

    # Every bridge contract must state the closure its validator enforces. The SYNTHESIZE
    # contract was the only one of the three that did not, while asking the model to "preserve
    # conflicts" with no field to put them in -- and a live run duly returned an extra
    # `_conflicts_preserved` key and was rejected after both peers had already been paid for.
    for phase in ("DIAGNOSE", "SYNTHESIZE"):
        contract = prompt_for("RND", {
            "resource": "RND", "phase": phase,
            "prompt_ref": "prompts/RND_AGENT_V0_2_CANDIDATE.md",
            "task": task, "instruction": phase.lower(),
        })
        assert "Do not add fields" in contract, f"{phase} bridge contract omits its closure rule"
    synth_contract = prompt_for("RND", {
        "resource": "RND", "phase": "SYNTHESIZE",
        "prompt_ref": "prompts/RND_AGENT_V0_2_CANDIDATE.md",
        "task": task, "instruction": "synthesize",
    })
    assert "IN learning_records" in synth_contract, "SYNTHESIZE asks for conflicts with no field named"

    # Context delivery. A task names context_refs; before this existed the peer received the
    # PATHS and, with Read disabled in the CLI adapter, could open none of them. The failure is
    # silent: a starved peer produces thinner output, which reads as a reason to add resources.
    ctx_request = {
        "resource": "NETA",
        "phase": "ANALYZE",
        "task": {"context_refs": ["docs/SHARED_EPISTEMIC_KERNEL.md"]},
        "requested_focus": ["proxy_substitution_risk"],
    }
    with_ctx = prompt_for("NETA", ctx_request)
    kernel = (ROOT / "docs" / "SHARED_EPISTEMIC_KERNEL.md").read_text(encoding="utf-8")
    assert "Referenced context documents" in with_ctx
    assert "docs/SHARED_EPISTEMIC_KERNEL.md` delivered" in with_ctx
    # The document itself, not its name.
    assert kernel[:400] in with_ctx, "context_refs delivered a path rather than the document"

    # A ref that cannot be resolved is REPORTED, never dropped: a peer told nothing about a
    # missing document reasons as though it had read one.
    missing = prompt_for("NETA", {
        "resource": "NETA",
        "phase": "ANALYZE",
        "task": {"context_refs": ["docs/NO_SUCH_DOCUMENT.md"]},
        "requested_focus": ["proxy_substitution_risk"],
    })
    assert "NOT DELIVERED" in missing
    assert "NO_SUCH_DOCUMENT" in missing

    # Truncation is stated on the document, so a bounded read is never mistaken for a whole one.
    import openai_resource_adapter as _ora
    original_cap = _ora.CONTEXT_DOC_BYTES
    try:
        _ora.CONTEXT_DOC_BYTES = 200
        clipped = prompt_for("NETA", ctx_request)
        assert "TRUNCATED to 200 of" in clipped
        assert kernel[:400] not in clipped
    finally:
        _ora.CONTEXT_DOC_BYTES = original_cap

    # No context_refs must not fabricate a section.
    bare = prompt_for("NETA", {
        "resource": "NETA",
        "phase": "ANALYZE",
        "task": {"context_refs": []},
        "requested_focus": ["proxy_substitution_risk"],
    })
    assert "Referenced context documents" not in bare

    print("LIVE ADAPTER CONTROLS OK: prompts, delta bridge, web-search toggle, context delivery and semantic shapes validated offline")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
