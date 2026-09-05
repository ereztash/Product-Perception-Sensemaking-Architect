#!/usr/bin/env python3
"""Executable controls for Calibration Loop v0.1 routing and trace semantics."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNTIME = ROOT / "runtime" / "calibration_loop"
if str(RUNTIME) not in sys.path:
    sys.path.insert(0, str(RUNTIME))
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

from routing import route  # noqa: E402
from run import RuntimeErrorBounded, run, validate_diagnosis  # noqa: E402
from validate_calibration_task import ContractError, validate as validate_task  # noqa: E402

FIXTURE = ROOT / "fixtures" / "calibration-valid-task.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def base_needs() -> dict[str, bool]:
    return {
        "signal_interpretation_ambiguity": False,
        "multiple_plausible_mechanisms": False,
        "proxy_substitution_risk": False,
        "research_to_intervention_transition": False,
        "broad_reasoning_needed": False,
        "architecture_alternatives_needed": False,
        "novel_synthesis_needed": False,
        "external_research_needed": False,
        "owner_authority_needed": False,
        "repo_authority_needed": False,
        "environment_authority_needed": False,
        "field_authority_needed": False,
    }


def diagnosis(needs: dict[str, bool]) -> dict:
    return {
        "material_question": "What changes the decision?",
        "bottleneck": "Unknown marginal resource value.",
        "resource_assessment": [{
            "resource": "RND",
            "expected_contribution": "Calibrate resources.",
            "authority_ceiling": "Does not inherit peer authority.",
            "uncertainty": "Value not yet measured."
        }],
        "candidate_moves": [{
            "move": "TEST",
            "resource": "RND",
            "expected_decision_value": "Discriminate next move.",
            "reversibility": "HIGH"
        }],
        "needs": needs,
        "rationale": "Bounded test."
    }


def main() -> int:
    task = json.loads(FIXTURE.read_text(encoding="utf-8"))
    validate_task(task)

    trace = run(task, config={"adapters": {}}, mock=True, strict=True)
    require(trace["final_state"] == "COMPLETE", "mock end-to-end run must complete")
    require(trace["routing"]["resources"] == ["NETA", "SCAFFOLD"], "fixture must route independently to Neta and scaffold")
    phases = [(x["resource"], x["phase"]) for x in trace["resource_invocations"]]
    require(phases[0] == ("RND", "DIAGNOSE"), "R&D must diagnose first")
    require(phases[-1] == ("RND", "SYNTHESIZE"), "R&D must synthesize last")

    peer_requests = [x["request"] for x in trace["resource_invocations"] if x["resource"] in {"NETA", "SCAFFOLD"}]
    for request in peer_requests:
        require("diagnosis" not in request, "peer analysis request must not receive R&D diagnosis conclusion")
        require("resource_results" not in request, "peer analysis request must not receive another peer's result")

    synthesis = trace["synthesis"]
    require(synthesis["routing_amendment_proposed"] is None, "one mock case must not self-modify routing")
    require({d["resource"] for d in synthesis["resource_deltas"]} == {"NETA", "SCAFFOLD"}, "synthesis must preserve per-resource deltas")

    needs = base_needs()
    needs["proxy_substitution_risk"] = True
    d = diagnosis(needs)
    validate_diagnosis(d)
    decision = route(d, ["RND", "NETA", "SCAFFOLD"])
    require(decision.resources == ("NETA",), "Neta trigger must not automatically invoke scaffold")

    needs = base_needs()
    needs["architecture_alternatives_needed"] = True
    d = diagnosis(needs)
    decision = route(d, ["RND", "NETA", "SCAFFOLD"])
    require(decision.resources == ("SCAFFOLD",), "scaffold trigger must not automatically invoke Neta")

    needs = base_needs()
    d = diagnosis(needs)
    decision = route(d, ["RND", "NETA", "SCAFFOLD"])
    require(decision.resources == (), "no trigger must mean no peer ceremony")

    needs = base_needs()
    needs["field_authority_needed"] = True
    d = diagnosis(needs)
    decision = route(d, ["RND", "NETA", "SCAFFOLD", "FIELD"])
    require(decision.resources == (), "FIELD requirement must not cause Neta/scaffold invocation")
    require(decision.authority_handoffs == ("FIELD",), "FIELD authority must remain explicit")

    unavailable_neta = route(diagnosis({**base_needs(), "proxy_substitution_risk": True}), ["RND", "SCAFFOLD"])
    require(unavailable_neta.resources == (), "runner must not invoke a resource outside allowed_resources")
    require("NETA" in unavailable_neta.fired, "blocked useful resource should remain visible in fired trace")

    bad_task = copy.deepcopy(task)
    bad_task["allowed_resources"].remove("RND")
    try:
        validate_task(bad_task)
    except ContractError:
        pass
    else:
        raise AssertionError("calibration task without RND must be rejected")

    bad_diag = diagnosis(base_needs())
    bad_diag["needs"]["invented_trigger"] = True
    try:
        validate_diagnosis(bad_diag)
    except RuntimeErrorBounded:
        pass
    else:
        raise AssertionError("unknown routing trigger must be rejected")

    pending = run(task, config={"adapters": {}}, mock=False, strict=False)
    require(pending["final_state"] == "PENDING_RESOURCE", "unwired real runtime must expose pending R&D rather than fabricate output")

    print("CALIBRATION LOOP OK: routing, independence, authority, non-self-modification and pending-resource controls passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
