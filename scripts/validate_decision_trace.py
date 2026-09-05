#!/usr/bin/env python3
"""Validate Decision→Execution→Verified State→Outcome→Learning traces."""
from __future__ import annotations
import json
import sys
from pathlib import Path

class ContractError(ValueError):
    pass

def require(ok: bool, message: str) -> None:
    if not ok:
        raise ContractError(message)

def nonempty(v: object) -> bool:
    return isinstance(v, str) and bool(v.strip())

def refs(v: object, name: str) -> None:
    require(isinstance(v, list) and all(nonempty(x) for x in v), f"{name} must be string array")

def validate(p: dict) -> None:
    require(isinstance(p, dict), "trace must be object")
    require(set(p) == {"trace_version","trace_id","decision","execution","verified_state","outcome","learning"}, "top-level fields drift")
    require(p["trace_version"] == "0.1", "trace_version must be 0.1")
    require(nonempty(p["trace_id"]), "trace_id required")

    d=p["decision"]
    require(isinstance(d,dict) and set(d)=={"statement","decision_owner","resolution_authority","evidence_refs","reversal_condition"}, "decision fields drift")
    require(nonempty(d["statement"]) and nonempty(d["reversal_condition"]), "decision text required")
    require(d["decision_owner"] in {"OWNER","NETA","RND","DETERMINISTIC_RUNTIME"}, "bad decision_owner")
    require(d["resolution_authority"] in {"OWNER","REPO","ENVIRONMENT","RESEARCH","FIELD"}, "bad resolution_authority")
    refs(d["evidence_refs"], "decision.evidence_refs")

    e=p["execution"]
    require(isinstance(e,dict) and set(e)=={"executor_type","planned_action","completed_action","status","artifact_refs"}, "execution fields drift")
    require(e["executor_type"] in {"HUMAN","TOOL","AGENT","RUNTIME","MIXED"}, "bad executor_type")
    require(nonempty(e["planned_action"]) and isinstance(e["completed_action"],str), "execution text invalid")
    require(e["status"] in {"NOT_STARTED","STARTED","PARTIAL","COMPLETED","FAILED"}, "bad execution status")
    refs(e["artifact_refs"], "execution.artifact_refs")
    if e["status"] == "COMPLETED":
        require(nonempty(e["completed_action"]), "completed execution needs completed_action")
        require(bool(e["artifact_refs"]), "completed execution needs artifact_refs")

    v=p["verified_state"]
    require(isinstance(v,dict) and set(v)=={"authority","expected_state","observed_state","status","evidence_refs"}, "verified_state fields drift")
    require(v["authority"] in {"REPO","ENVIRONMENT","FIELD","OWNER"}, "bad verification authority")
    require(nonempty(v["expected_state"]) and isinstance(v["observed_state"],str), "verification text invalid")
    require(v["status"] in {"NOT_VERIFIED","MATCH","MISMATCH","PARTIAL","FAILED_OBSERVATION"}, "bad verification status")
    refs(v["evidence_refs"], "verified_state.evidence_refs")
    if v["status"] in {"MATCH","MISMATCH","PARTIAL"}:
        require(nonempty(v["observed_state"]), "verified state needs observed_state")
        require(bool(v["evidence_refs"]), "verified state needs evidence_refs")

    o=p["outcome"]
    require(isinstance(o,dict) and set(o)=={"authority","target","observation","status","evidence_refs"}, "outcome fields drift")
    require(o["authority"] in {"FIELD","ENVIRONMENT","REPO","OWNER","NOT_YET_ELIGIBLE"}, "bad outcome authority")
    require(nonempty(o["target"]) and isinstance(o["observation"],str), "outcome text invalid")
    require(o["status"] in {"NOT_MEASURED","MEASURED","FIELD_REQUIRED","INCONCLUSIVE"}, "bad outcome status")
    refs(o["evidence_refs"], "outcome.evidence_refs")
    if o["status"] == "MEASURED":
        require(nonempty(o["observation"]), "measured outcome needs observation")
        require(bool(o["evidence_refs"]), "measured outcome needs evidence_refs")

    l=p["learning"]
    require(isinstance(l,dict) and set(l)=={"decision_delta","claim_updates","resource_delta","next_move","stop_or_continue"}, "learning fields drift")
    require(all(nonempty(l[k]) for k in ("decision_delta","resource_delta","next_move")), "learning text required")
    require(isinstance(l["claim_updates"],list) and all(nonempty(x) for x in l["claim_updates"]), "claim_updates must be strings")
    require(l["stop_or_continue"] in {"STOP","CONTINUE","WAIT_AUTHORITY"}, "bad stop_or_continue")

    # Critical non-collapse rules.
    if e["status"] == "COMPLETED":
        require(v["status"] != "NOT_VERIFIED" or o["status"] != "MEASURED", "measured outcome cannot bypass state verification")
    if o["status"] == "FIELD_REQUIRED":
        require(o["authority"] == "FIELD", "FIELD_REQUIRED must belong to FIELD")

def main(argv: list[str]) -> int:
    if len(argv)!=2:
        print("usage: validate_decision_trace.py <trace.json>", file=sys.stderr); return 2
    try:
        p=json.loads(Path(argv[1]).read_text(encoding="utf-8")); validate(p)
    except (OSError,json.JSONDecodeError,ContractError) as exc:
        print(f"INVALID DECISION TRACE: {exc}", file=sys.stderr); return 1
    print("DECISION TRACE OK"); return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
