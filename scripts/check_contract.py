#!/usr/bin/env python3
"""Neta contract gate with deliberate positive controls.

A green validator that has never been demonstrated to fail is not evidence of a gate.
This script first checks the canonical valid fixture, then injects defects that MUST be rejected.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

from validate_finding import ContractError, validate

ROOT = Path(__file__).resolve().parents[1]
VALID_FIXTURE = ROOT / "fixtures" / "valid-finding.json"
SYSTEM_PROMPT = ROOT / "prompts" / "SYSTEM.md"
METHOD = ROOT / "docs" / "METHOD.md"
AUTHORITY_MAP = ROOT / "docs" / "AUTHORITY_MAP.md"

REQUIRED_PROMPT_ANCHORS = (
    "RAW SIGNAL",
    "COMPETING MECHANISMS",
    "DISCRIMINATE_FIRST",
    "BUILD_READY",
    "FIELD_STOP",
    "rendered ≠ noticed",
    "Do not change intervention and measurement silently at the same time.",
)


def must_fail(name: str, payload: dict) -> None:
    try:
        validate(payload)
    except ContractError:
        print(f"CONTROL RED: {name}")
        return
    raise SystemExit(f"NOT-A-GATE: positive control stayed green: {name}")


def main() -> int:
    with VALID_FIXTURE.open("r", encoding="utf-8") as handle:
        valid = json.load(handle)

    validate(valid)
    print("FIXTURE GREEN: canonical valid finding")

    too_many = copy.deepcopy(valid)
    too_many["candidate_mechanisms"] = too_many["candidate_mechanisms"] * 4
    must_fail("more than three mechanisms", too_many)

    fake_precision = copy.deepcopy(valid)
    fake_precision["confidence"] = 87
    must_fail("fake numeric confidence field", fake_precision)

    field_mismatch = copy.deepcopy(valid)
    field_mismatch["status"] = "FIELD_STOP"
    field_mismatch["authority"] = "REPO"
    field_mismatch["evidence_state"] = "FIELD_REQUIRED"
    must_fail("FIELD_STOP with non-FIELD authority", field_mismatch)

    no_reversal = copy.deepcopy(valid)
    no_reversal["reversal_condition"] = None
    must_fail("BUILD_READY without reversal condition", no_reversal)

    prompt = SYSTEM_PROMPT.read_text(encoding="utf-8")
    for anchor in REQUIRED_PROMPT_ANCHORS:
        if anchor not in prompt:
            raise SystemExit(f"PROMPT CONTRACT MISSING: {anchor}")

    for required_file in (METHOD, AUTHORITY_MAP):
        if not required_file.exists() or required_file.stat().st_size < 200:
            raise SystemExit(f"MISSING OR EMPTY CONTRACT FILE: {required_file.relative_to(ROOT)}")

    print("PROMPT CONTRACT GREEN")
    print("Neta v0.1 contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
