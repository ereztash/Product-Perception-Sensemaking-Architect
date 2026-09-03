#!/usr/bin/env python3
"""Validate Neta Assurance Finding v0.2.

Stdlib-only executable semantics for the parts JSON Schema cannot express:
reality floors, authority, requested use and permission.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

STATUSES = {"DISCRIMINATE_FIRST", "BUILD_READY", "FIELD_STOP"}
AUTHORITIES = {"OWNER", "REPO", "ENVIRONMENT", "RESEARCH", "FIELD"}
REALITIES = {f"R{i}" for i in range(7)}
REALITY_RANK = {f"R{i}": i for i in range(7)}
CLAIM_KINDS = {"OBSERVATION", "MECHANISM", "INTERVENTION", "OUTCOME"}
CLAIM_STATES = {"SUPPORTED", "UNRESOLVED", "REFUTED", "INSUFFICIENT_REALITY"}
REQUESTED_USES = {
    "HYPOTHESIZE",
    "DISCRIMINATE",
    "PROTOTYPE",
    "BUILD_REVERSIBLE",
    "CHANGE_PRODUCTION",
    "ASSERT_FIELD_OUTCOME",
    "DEFER",
}
PERMISSIONS = {"ALLOW", "DENY", "DEFER"}
EVIDENCE_TYPES = {
    "OWNER_SIGNAL",
    "REPO_MEASUREMENT",
    "RESEARCH_SOURCE",
    "ENVIRONMENT_CHECK",
    "FIELD_OBSERVATION",
}
FORBIDDEN_CONFIDENCE_KEYS = {"confidence", "confidence_score", "certainty", "probability"}


class ContractError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def reject_confidence_theatre(value: object, path: str = "$") -> None:
    if isinstance(value, dict):
        bad = FORBIDDEN_CONFIDENCE_KEYS & set(value)
        require(not bad, f"forbidden confidence field at {path}: {sorted(bad)}")
        for key, child in value.items():
            reject_confidence_theatre(child, f"{path}.{key}")
    elif isinstance(value, list):
        for i, child in enumerate(value):
            reject_confidence_theatre(child, f"{path}[{i}]")


def validate_evidence(items: object) -> set[str]:
    require(isinstance(items, list), "evidence must be a list")
    ids: list[str] = []
    for i, item in enumerate(items):
        require(isinstance(item, dict), f"evidence[{i}] must be object")
        allowed = {"id", "type", "description", "reality_level"}
        require(set(item) == allowed, f"evidence[{i}] fields drift: {sorted(set(item) ^ allowed)}")
        eid = item.get("id")
        require(isinstance(eid, str) and eid.startswith("E") and eid[1:].isdigit(), f"bad evidence id at {i}")
        require(item.get("type") in EVIDENCE_TYPES, f"bad evidence type at {eid}")
        require(nonempty(item.get("description")), f"evidence description required at {eid}")
        require(item.get("reality_level") in REALITIES, f"bad evidence reality at {eid}")
        ids.append(eid)
    require(len(ids) == len(set(ids)), "duplicate evidence ids")
    return set(ids)


def validate_claims(items: object, evidence_ids: set[str]) -> list[dict]:
    require(isinstance(items, list) and len(items) >= 1, "claims must be a non-empty list")
    ids: list[str] = []
    claims: list[dict] = []
    required = {
        "id",
        "kind",
        "statement",
        "resolution_authority",
        "required_reality",
        "observed_reality",
        "evidence_refs",
        "state",
        "requested_use",
        "permission",
    }

    for i, claim in enumerate(items):
        require(isinstance(claim, dict), f"claims[{i}] must be object")
        require(set(claim) == required, f"claims[{i}] fields drift: {sorted(set(claim) ^ required)}")

        cid = claim.get("id")
        require(isinstance(cid, str) and cid.startswith("C") and cid[1:].isdigit(), f"bad claim id at {i}")
        require(claim.get("kind") in CLAIM_KINDS, f"bad claim kind at {cid}")
        require(nonempty(claim.get("statement")), f"claim statement required at {cid}")
        require(claim.get("resolution_authority") in AUTHORITIES, f"bad authority at {cid}")
        require(claim.get("required_reality") in REALITIES, f"bad required reality at {cid}")
        require(claim.get("observed_reality") in REALITIES, f"bad observed reality at {cid}")
        require(claim.get("state") in CLAIM_STATES, f"bad state at {cid}")
        require(claim.get("requested_use") in REQUESTED_USES, f"bad requested use at {cid}")
        require(claim.get("permission") in PERMISSIONS, f"bad permission at {cid}")

        refs = claim.get("evidence_refs")
        require(isinstance(refs, list), f"evidence_refs must be list at {cid}")
        require(set(refs) <= evidence_ids, f"unknown evidence ref at {cid}: {sorted(set(refs) - evidence_ids)}")

        required_rank = REALITY_RANK[claim["required_reality"]]
        observed_rank = REALITY_RANK[claim["observed_reality"]]
        state = claim["state"]

        if state == "SUPPORTED":
            require(observed_rank >= required_rank, f"reality laundering at {cid}: supported below floor")
        if state == "INSUFFICIENT_REALITY":
            require(observed_rank < required_rank, f"INSUFFICIENT_REALITY but floor already met at {cid}")

        # Permission is a separate object, but ALLOW cannot outrun support/reality.
        if claim["permission"] == "ALLOW":
            require(state == "SUPPORTED", f"permission laundering at {cid}: ALLOW requires SUPPORTED")
            require(observed_rank >= required_rank, f"permission laundering at {cid}: ALLOW below reality floor")

        # External-human outcomes are field claims, not repo/research/owner claims.
        if claim["kind"] == "OUTCOME":
            require(claim["resolution_authority"] == "FIELD", f"field outcome authority laundering at {cid}")
            require(required_rank >= REALITY_RANK["R6"], f"field outcome requires R6 floor at {cid}")

        if claim["requested_use"] == "ASSERT_FIELD_OUTCOME" and claim["permission"] == "ALLOW":
            require(claim["resolution_authority"] == "FIELD", f"field assertion requires FIELD at {cid}")
            require(state == "SUPPORTED", f"field assertion requires supported claim at {cid}")
            require(observed_rank >= REALITY_RANK["R6"], f"field assertion below R6 at {cid}")

        ids.append(cid)
        claims.append(claim)

    require(len(ids) == len(set(ids)), "duplicate claim ids")
    return claims


def validate(payload: dict) -> None:
    require(isinstance(payload, dict), "finding must be an object")
    reject_confidence_theatre(payload)

    allowed_top = {
        "contract_version",
        "status",
        "raw_signal",
        "candidate_mechanisms",
        "evidence",
        "claims",
        "design_distinction",
        "intervention",
        "must_not_change",
        "perceptual_success_criterion",
        "gate",
        "reversal_condition",
        "field_requirement",
        "waiver",
        "next_step",
    }
    require(set(payload) <= allowed_top, f"unknown top-level fields: {sorted(set(payload) - allowed_top)}")

    for key in ("contract_version", "status", "raw_signal", "candidate_mechanisms", "evidence", "claims", "reversal_condition", "next_step"):
        require(key in payload, f"missing required field: {key}")

    require(payload["contract_version"] == "0.2", "contract_version must be 0.2")
    require(payload["status"] in STATUSES, "unknown status")
    require(nonempty(payload["raw_signal"]), "raw_signal required")
    require(nonempty(payload["reversal_condition"]), "reversal_condition required")
    require(nonempty(payload["next_step"]), "next_step required")

    mechanisms = payload["candidate_mechanisms"]
    require(isinstance(mechanisms, list) and len(mechanisms) <= 3, "at most three candidate mechanisms")
    mech_required = {"name", "explains", "does_not_explain", "discriminator"}
    for i, mech in enumerate(mechanisms):
        require(isinstance(mech, dict) and set(mech) == mech_required, f"bad candidate mechanism shape at {i}")
        for key in mech_required:
            require(nonempty(mech[key]), f"candidate mechanism {i}.{key} required")

    evidence_ids = validate_evidence(payload["evidence"])
    claims = validate_claims(payload["claims"], evidence_ids)

    waiver = payload.get("waiver")
    if waiver is not None:
        require(isinstance(waiver, dict), "waiver must be object or null")
        require(set(waiver) == {"accepted_by", "reason", "scope", "revisit"}, "waiver fields drift")
        require(waiver.get("accepted_by") == "OWNER", "only OWNER may accept a waiver")
        for key in ("reason", "scope", "revisit"):
            require(nonempty(waiver.get(key)), f"waiver.{key} required")

    status = payload["status"]
    allowed_build = [
        c for c in claims
        if c["kind"] == "INTERVENTION"
        and c["requested_use"] in {"BUILD_REVERSIBLE", "CHANGE_PRODUCTION"}
        and c["permission"] == "ALLOW"
    ]

    if status == "DISCRIMINATE_FIRST":
        require(not allowed_build, "DISCRIMINATE_FIRST may not contain an allowed build intervention")

    if status == "BUILD_READY":
        require(allowed_build, "BUILD_READY requires at least one allowed intervention claim")
        require(nonempty(payload.get("intervention")), "BUILD_READY requires intervention")
        require(nonempty(payload.get("design_distinction")), "BUILD_READY requires design_distinction")
        gate = payload.get("gate")
        require(isinstance(gate, dict), "BUILD_READY requires gate")
        require(set(gate) == {"falsifier", "positive_control"}, "gate fields drift")
        require(nonempty(gate.get("falsifier")), "BUILD_READY requires gate.falsifier")
        require(nonempty(gate.get("positive_control")), "BUILD_READY requires gate.positive_control")

    if status == "FIELD_STOP":
        unresolved_field = [
            c for c in claims
            if c["resolution_authority"] == "FIELD"
            and c["state"] in {"UNRESOLVED", "INSUFFICIENT_REALITY"}
        ]
        require(unresolved_field, "FIELD_STOP requires an unresolved material FIELD claim")
        require(nonempty(payload.get("field_requirement")), "FIELD_STOP requires field_requirement")
        require(not allowed_build, "FIELD_STOP may not hide an allowed build intervention")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_finding.py <finding.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    payload = json.loads(path.read_text(encoding="utf-8"))
    try:
        validate(payload)
    except ContractError as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    print("VALID: Neta Assurance Finding v0.2")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
