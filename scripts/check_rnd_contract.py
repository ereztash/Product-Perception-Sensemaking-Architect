#!/usr/bin/env python3
"""Executable positive controls for the R&D Agent v0.1 runtime contract."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from validate_rnd_task import ContractError, validate

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "rnd-valid-task.json"


def expect_valid(payload: dict, label: str) -> None:
    try:
        validate(payload)
    except ContractError as exc:
        raise AssertionError(f"{label}: expected VALID, got {exc}") from exc


def expect_invalid(payload: dict, label: str) -> None:
    try:
        validate(payload)
    except ContractError:
        return
    raise AssertionError(f"{label}: positive control unexpectedly passed")


def main() -> int:
    base = json.loads(FIXTURE.read_text(encoding="utf-8"))
    expect_valid(base, "canonical valid R&D task")

    stale_reuse = copy.deepcopy(base)
    stale_reuse["research_path"]["instrument"]["runnability_state"] = "STALE"
    expect_invalid(stale_reuse, "REUSE must not accept stale instrument")

    closed_without_deposit = copy.deepcopy(base)
    closed_without_deposit["closure"]["durable_deposit"] = None
    expect_invalid(closed_without_deposit, "CLOSED requires durable deposit")

    failed_but_closed = copy.deepcopy(base)
    failed_but_closed["run"]["result_state"] = "FAILED_EXECUTION"
    failed_but_closed["closure"]["reversal_or_rerun_condition"] = "Repair the runtime and rerun."
    expect_invalid(failed_but_closed, "FAILED_EXECUTION must not masquerade as CLOSED evidence")

    waiting_without_pending = copy.deepcopy(base)
    waiting_without_pending["closure"]["state"] = "WAITING_AUTHORITY"
    waiting_without_pending["closure"]["claim_effect"] = "SUPPORTS"
    expect_invalid(waiting_without_pending, "WAITING_AUTHORITY must preserve PENDING claim effect")

    run_instrument_mismatch = copy.deepcopy(base)
    run_instrument_mismatch["run"]["instrument_id"] = "different-instrument"
    expect_invalid(run_instrument_mismatch, "run must stay linked to selected instrument")

    run_version_mismatch = copy.deepcopy(base)
    run_version_mismatch["run"]["version_ref"] = "other-version"
    expect_invalid(run_version_mismatch, "run must stay linked to selected version")

    owner_takeover = copy.deepcopy(base)
    owner_takeover["resolution_authority"] = "OWNER"
    owner_takeover["live_claim"]["resolution_authority"] = "OWNER"
    owner_takeover["handoff"] = None
    expect_invalid(owner_takeover, "R&D must not silently close OWNER-owned uncertainty")

    wait_authority_bad_state = copy.deepcopy(base)
    wait_authority_bad_state["research_path"]["decision"] = "WAIT_AUTHORITY"
    wait_authority_bad_state["status"] = "EXECUTE"
    expect_invalid(wait_authority_bad_state, "WAIT_AUTHORITY cannot remain in EXECUTE state")

    no_instrument_with_instrument = copy.deepcopy(base)
    no_instrument_with_instrument["research_path"]["decision"] = "NO_INSTRUMENT"
    expect_invalid(no_instrument_with_instrument, "NO_INSTRUMENT must not carry an instrument")

    print("R&D CONTRACT OK: canonical fixture valid and all deliberate positive controls rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
