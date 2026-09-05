#!/usr/bin/env python3
"""Validate the semantic invariants of an R&D Agent v0.1 task object.

This intentionally uses only the Python standard library. JSON Schema remains the
shape authority; this script protects cross-field invariants that are easy to
violate while still producing syntactically valid JSON.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

AUTHORITIES = {"OWNER", "REPO", "ENVIRONMENT", "RESEARCH", "FIELD"}
TASK_STATUSES = {"DIAGNOSE", "RECOVER", "DISCRIMINATE", "EXECUTE", "CLOSE", "AUTHORITY_STOP"}
RESEARCH_DECISIONS = {"REUSE", "ADAPT", "BUILD", "NO_INSTRUMENT", "WAIT_AUTHORITY"}
RUNNABILITY = {"VERIFIED", "STALE", "BROKEN", "UNKNOWN", "HISTORICAL_ONLY"}
CONTAMINATION = {"LOW", "MATERIAL", "UNKNOWN"}
RUN_RESULTS = {"SUPPORTED", "REFUTED", "INCONCLUSIVE", "FAILED_EXECUTION", "WAITING_AUTHORITY"}
CLOSURE_STATES = {"OPEN_EXECUTION", "OPEN_DEPOSITION", "OPEN_DECISION_LINK", "WAITING_AUTHORITY", "CLOSED"}
CLAIM_EFFECTS = {"SUPPORTS", "REFUTES", "NARROWS", "SPLITS", "INCONCLUSIVE", "NO_MATERIAL_EFFECT", "PENDING"}
HANDOFF_TARGETS = {"NETA", "OWNER", "REPO", "ENVIRONMENT", "FIELD", "ORCHESTRATOR_FUTURE"}


class ContractError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(payload: dict) -> None:
    require(isinstance(payload, dict), "task must be an object")

    for key in (
        "task_id",
        "status",
        "live_claim",
        "material_question",
        "resolution_authority",
        "existing_capability_search",
        "research_path",
        "closure",
    ):
        require(key in payload, f"missing required field: {key}")

    require(nonempty(payload["task_id"]), "task_id required")
    require(payload["status"] in TASK_STATUSES, "unknown task status")
    require(nonempty(payload["material_question"]), "material_question required")
    require(payload["resolution_authority"] in AUTHORITIES, "unknown resolution authority")

    claim = payload["live_claim"]
    require(isinstance(claim, dict), "live_claim must be an object")
    if "resolution_authority" in claim:
        require(
            claim["resolution_authority"] == payload["resolution_authority"],
            "task authority and live_claim authority disagree",
        )

    search = payload["existing_capability_search"]
    require(isinstance(search, dict), "existing_capability_search must be object")
    require(isinstance(search.get("required"), bool), "existing_capability_search.required must be boolean")
    require(nonempty(search.get("bounded_by")), "existing_capability_search.bounded_by required")
    refs = search.get("candidate_refs")
    require(isinstance(refs, list), "existing_capability_search.candidate_refs must be list")
    require(all(nonempty(ref) for ref in refs), "candidate_refs must contain non-empty strings")

    path = payload["research_path"]
    require(isinstance(path, dict), "research_path must be object")
    decision = path.get("decision")
    require(decision in RESEARCH_DECISIONS, "unknown research_path.decision")
    require(nonempty(path.get("rationale")), "research_path.rationale required")

    instrument = path.get("instrument")
    if decision in {"REUSE", "ADAPT"}:
        require(isinstance(instrument, dict), f"{decision} requires an instrument")
    if decision == "NO_INSTRUMENT":
        require(instrument is None, "NO_INSTRUMENT must not attach an instrument")
    if decision == "WAIT_AUTHORITY":
        require(payload["status"] in {"AUTHORITY_STOP", "CLOSE", "DISCRIMINATE"}, "WAIT_AUTHORITY requires a stopping/defer state")

    if instrument is not None:
        require(isinstance(instrument, dict), "instrument must be object or null")
        for key in ("instrument_id", "source_ref", "construct", "version_ref", "runnability_state", "decision_contract"):
            require(key in instrument, f"instrument.{key} required")
        require(instrument["runnability_state"] in RUNNABILITY, "bad instrument.runnability_state")
        require(instrument.get("contamination_risk") in CONTAMINATION, "instrument.contamination_risk required")
        contract = instrument["decision_contract"]
        require(isinstance(contract, dict), "instrument.decision_contract must be object")
        dims = contract.get("outcome_dimensions")
        require(isinstance(dims, list) and dims and all(nonempty(d) for d in dims), "decision_contract.outcome_dimensions required")
        require(nonempty(contract.get("decision_rule")), "decision_contract.decision_rule required")

        if decision == "REUSE":
            require(
                instrument["runnability_state"] == "VERIFIED",
                "REUSE requires VERIFIED current runnability; otherwise ADAPT/BUILD/NO_INSTRUMENT",
            )

    run = payload.get("run")
    if payload["status"] == "EXECUTE":
        require(isinstance(run, dict), "EXECUTE requires run object")
    if run is not None:
        require(isinstance(run, dict), "run must be object or null")
        for key in ("run_id", "instrument_id", "version_ref", "input_ref", "started_state", "result_state", "artifact_refs"):
            require(key in run, f"run.{key} required")
        require(run["result_state"] in RUN_RESULTS, "bad run.result_state")
        require(isinstance(run["artifact_refs"], list), "run.artifact_refs must be list")
        if instrument is not None:
            require(run["instrument_id"] == instrument["instrument_id"], "run instrument_id does not match selected instrument")
            require(run["version_ref"] == instrument["version_ref"], "run version_ref does not match selected instrument")

    closure = payload["closure"]
    require(isinstance(closure, dict), "closure must be object")
    require(closure.get("state") in CLOSURE_STATES, "bad closure.state")
    require(closure.get("claim_effect") in CLAIM_EFFECTS, "bad closure.claim_effect")
    require(nonempty(closure.get("next_authority_or_stop")), "closure.next_authority_or_stop required")

    cstate = closure["state"]
    deposit = closure.get("durable_deposit")
    effect = closure["claim_effect"]

    if cstate == "CLOSED":
        require(nonempty(deposit), "CLOSED requires durable_deposit")
        require(effect != "PENDING", "CLOSED cannot have PENDING claim_effect")

    if cstate == "OPEN_DEPOSITION":
        require(not nonempty(deposit), "OPEN_DEPOSITION should not claim a durable deposit")

    if cstate == "WAITING_AUTHORITY":
        require(effect == "PENDING", "WAITING_AUTHORITY requires PENDING claim_effect")

    if run is not None and run["result_state"] == "FAILED_EXECUTION":
        require(cstate != "CLOSED", "FAILED_EXECUTION cannot be CLOSED as evidence")
        require(nonempty(closure.get("reversal_or_rerun_condition")), "FAILED_EXECUTION requires rerun condition")

    if run is not None and run["result_state"] == "WAITING_AUTHORITY":
        require(cstate == "WAITING_AUTHORITY", "WAITING_AUTHORITY run must preserve waiting closure")

    # A non-research authority cannot be silently 'solved' by R&D.
    if payload["resolution_authority"] != "RESEARCH":
        require(
            decision in {"NO_INSTRUMENT", "WAIT_AUTHORITY"} or payload.get("handoff") is not None,
            "non-RESEARCH authority requires handoff/stop rather than autonomous research closure",
        )

    handoff = payload.get("handoff")
    if handoff is not None:
        require(isinstance(handoff, dict), "handoff must be object or null")
        require(handoff.get("to") in HANDOFF_TARGETS, "bad handoff target")
        require(nonempty(handoff.get("question")), "handoff.question required")
        require(isinstance(handoff.get("evidence_refs"), list), "handoff.evidence_refs must be list")
        require(nonempty(handoff.get("requested_return")), "handoff.requested_return required")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_rnd_task.py <task.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        validate(payload)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
