#!/usr/bin/env python3
"""Neta v0.2 assurance gate with deliberate epistemic positive controls.

The canonical finding must be green. Each injected authority/reality/permission defect
must go red in the same run. The v0.1 prompt hash is also frozen so architectural
re-foundation cannot silently contaminate the clean-model baseline.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from validate_finding import ContractError, validate

ROOT = Path(__file__).resolve().parents[1]
VALID_FIXTURE = ROOT / "fixtures" / "valid-finding.json"
SYSTEM_PROMPT = ROOT / "prompts" / "SYSTEM.md"
FROZEN_PROMPT_BLOB = "339b9a1be2fd0f1f6f6c7960e5be58e5566d3691"

REQUIRED_DOCS = (
    ROOT / "docs" / "V0_1_FREEZE.md",
    ROOT / "docs" / "NETA_ASSURANCE_THESIS.md",
    ROOT / "docs" / "REALITY_AUTHORITY_PERMISSION.md",
    ROOT / "docs" / "LESSONS_COVERAGE_AUDIT.md",
    ROOT / "docs" / "FAILURE_LINEAGE.md",
    ROOT / "docs" / "METHOD.md",
    ROOT / "docs" / "AUTHORITY_MAP.md",
    ROOT / "research" / "WAVE1_ASSURANCE_REVIEW.md",
)


def git_blob_sha(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def must_fail(name: str, payload: dict) -> None:
    try:
        validate(payload)
    except ContractError as exc:
        print(f"CONTROL RED: {name} :: {exc}")
        return
    raise SystemExit(f"NOT-A-GATE: positive control stayed green: {name}")


def claim(payload: dict, cid: str) -> dict:
    return next(c for c in payload["claims"] if c["id"] == cid)


def main() -> int:
    valid = json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))
    validate(valid)
    print("FIXTURE GREEN: canonical v0.2 finding")

    controls: list[tuple[str, dict]] = []

    # 1. Conversational compression still matters.
    broken = copy.deepcopy(valid)
    broken["candidate_mechanisms"] = broken["candidate_mechanisms"] * 4
    controls.append(("more-than-three-mechanisms", broken))

    # 2. No scalar confidence theatre anywhere in the ledger.
    broken = copy.deepcopy(valid)
    claim(broken, "C2")["confidence"] = 0.91
    controls.append(("fake-confidence-field", broken))

    # 3. Reality laundering: a claim cannot be SUPPORTED below its own floor.
    broken = copy.deepcopy(valid)
    c = claim(broken, "C1")
    c["required_reality"] = "R4"
    c["observed_reality"] = "R3"
    c["state"] = "SUPPORTED"
    controls.append(("supported-below-reality-floor", broken))

    # 4. Field outcome cannot borrow REPO authority.
    broken = copy.deepcopy(valid)
    claim(broken, "C4")["resolution_authority"] = "REPO"
    controls.append(("field-outcome-with-repo-authority", broken))

    # 5. Deployed evidence still cannot authorize a field assertion.
    broken = copy.deepcopy(valid)
    c = claim(broken, "C4")
    c["state"] = "SUPPORTED"
    c["permission"] = "ALLOW"
    c["observed_reality"] = "R4"
    controls.append(("field-assertion-from-r4", broken))

    # 6. Strong wording cannot turn unresolved into permission.
    broken = copy.deepcopy(valid)
    c = claim(broken, "C3")
    c["state"] = "UNRESOLVED"
    c["permission"] = "ALLOW"
    controls.append(("allow-unresolved-intervention", broken))

    # 7. Build-ready work must leave a falsifier/control/reversal.
    broken = copy.deepcopy(valid)
    broken["gate"] = None
    controls.append(("build-ready-without-gate", broken))

    # 8. FIELD_STOP is a real authority boundary, not a status label.
    broken = copy.deepcopy(valid)
    broken["status"] = "FIELD_STOP"
    broken["claims"] = [c for c in broken["claims"] if c["id"] != "C4"]
    broken["field_requirement"] = "Ask a stranger."
    # Remove the allowed build intervention so the test targets missing FIELD claim.
    claim(broken, "C3")["permission"] = "DENY"
    controls.append(("field-stop-without-field-claim", broken))

    # 9. A waiver may accept risk but never impersonate another authority.
    broken = copy.deepcopy(valid)
    broken["waiver"] = {
        "accepted_by": "SYSTEM",
        "reason": "ship anyway",
        "scope": "all field claims",
        "revisit": "never",
    }
    controls.append(("non-owner-waiver", broken))

    for name, payload in controls:
        must_fail(name, payload)

    # Freeze the clean-model v0.1 prompt during re-foundation.
    prompt_bytes = SYSTEM_PROMPT.read_bytes()
    observed_blob = git_blob_sha(prompt_bytes)
    if observed_blob != FROZEN_PROMPT_BLOB:
        raise SystemExit(
            "BASELINE CONTAMINATION: prompts/SYSTEM.md changed during re-foundation "
            f"(expected {FROZEN_PROMPT_BLOB}, got {observed_blob})"
        )
    print(f"PROMPT BASELINE FROZEN: {observed_blob}")

    for path in REQUIRED_DOCS:
        if not path.exists() or path.stat().st_size < 300:
            raise SystemExit(f"MISSING OR EMPTY RE-FOUNDATION ARTIFACT: {path.relative_to(ROOT)}")

    print(f"positive controls: {len(controls)}/{len(controls)} correctly failed")
    print("Neta Assurance v0.2 contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
