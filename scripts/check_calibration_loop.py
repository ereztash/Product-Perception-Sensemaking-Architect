#!/usr/bin/env python3
"""Executable controls for Calibration Loop v0.2 routing, independence and delta semantics."""

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
from run import RuntimeErrorBounded, annotate_peer_invocations, run, validate_diagnosis, validate_synthesis  # noqa: E402
from validate_calibration_task import ContractError, validate as validate_task  # noqa: E402

FIXTURE = ROOT / "fixtures" / "calibration-valid-task.json"
PREFLIGHT_TRACES = RUNTIME / "traces" / "preflight-2026-09"


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


def empty_expected_delta(**overrides: bool) -> dict:
    value = {
        "decision": False,
        "action": False,
        "reversal": False,
        "evidence": False,
        "allocation": False,
        "distinction": False,
    }
    value.update(overrides)
    return value


def diagnosis(needs: dict[str, bool]) -> dict:
    return {
        "material_question": "What changes the decision?",
        "bottleneck": "Unknown marginal resource value.",
        "resource_assessment": [{
            "resource": "RND",
            "expected_contribution": "Calibrate resources.",
            "authority_ceiling": "Does not inherit peer authority.",
            "uncertainty": "Value not yet measured.",
            "expected_delta": empty_expected_delta(decision=True, action=True, allocation=True),
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
    require(trace["runtime_version"] == "0.2", "resource-delta accounting must bump runtime trace version")
    require(trace["final_state"] == "COMPLETE", "mock end-to-end run must complete")
    require(trace["routing"]["resources"] == ["NETA", "SCAFFOLD"], "fixture must route independently to Neta and scaffold")
    phases = [(x["resource"], x["phase"]) for x in trace["resource_invocations"]]
    require(phases[0] == ("RND", "DIAGNOSE"), "R&D must diagnose first")
    require(phases[-1] == ("RND", "SYNTHESIZE"), "R&D must synthesize last")

    peer_invocations = [x for x in trace["resource_invocations"] if x["resource"] in {"NETA", "SCAFFOLD"}]
    for invocation in peer_invocations:
        request = invocation["request"]
        require("diagnosis" not in request, "peer analysis request must not receive R&D diagnosis conclusion")
        require("resource_results" not in request, "peer analysis request must not receive another peer's result")
        require("expected_delta" not in request, "peer must remain blind to R&D's ex-ante expected delta")
        require(set(invocation["expected_delta"]) == {"decision", "action", "reversal", "evidence", "allocation", "distinction"}, "peer trace must carry the six expected-delta dimensions")
        require(isinstance(invocation["observed_delta"], dict), "completed peer invocation must be annotated with observed_delta after synthesis")
        require(invocation["material"] is True, "mock peer deltas should be material")

    synthesis = trace["synthesis"]
    require(synthesis["routing_amendment_proposed"] is None, "one mock case must not self-modify routing")
    require({d["resource"] for d in synthesis["resource_deltas"]} == {"NETA", "SCAFFOLD"}, "synthesis must preserve per-resource deltas")
    for delta in synthesis["resource_deltas"]:
        derived_material = any(value is not None for value in delta["observed_delta"].values())
        require(delta["material"] == derived_material, "materiality must be derivable from observed_delta")

    inconsistent = copy.deepcopy(synthesis)
    inconsistent["resource_deltas"][0]["material"] = False
    try:
        validate_synthesis(inconsistent, trace["routing"]["resources"])
    except RuntimeErrorBounded:
        pass
    else:
        raise AssertionError("material label that conflicts with observed_delta must be rejected")

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

    bad_delta_diag = diagnosis(base_needs())
    del bad_delta_diag["resource_assessment"][0]["expected_delta"]["decision"]
    try:
        validate_diagnosis(bad_delta_diag)
    except RuntimeErrorBounded:
        pass
    else:
        raise AssertionError("incomplete expected_delta must be rejected")

    saturated_diag = diagnosis({key: True for key in base_needs()})
    try:
        validate_diagnosis(saturated_diag)
    except RuntimeErrorBounded as exc:
        require("saturated" in str(exc), "saturated needs must be rejected for saturation, not another defect")
    else:
        raise AssertionError("diagnosis with every routing flag true must be rejected")

    near_saturated = {key: True for key in base_needs()}
    near_saturated["field_authority_needed"] = False
    validate_diagnosis(diagnosis(near_saturated))

    for first, second in (("same change", "same change"), ("Same  change", "same change ")):
        repeated = copy.deepcopy(synthesis)
        repeated["resource_deltas"][0]["observed_delta"]["decision"] = first
        repeated["resource_deltas"][0]["observed_delta"]["action"] = second
        try:
            validate_synthesis(repeated, trace["routing"]["resources"])
        except RuntimeErrorBounded as exc:
            require("repeats identical text" in str(exc), "repeated delta text must be rejected for repetition")
        else:
            raise AssertionError("observed_delta repeating one text across dimensions must be rejected")

    for invocation in peer_invocations:
        require(invocation["expectation_mismatch"] is False, "mock peers had non-empty ex-ante expectations")

    def annotated(expected: dict, observed: dict) -> dict:
        probe = {"resource_invocations": [{"resource": "NETA", "phase": "ANALYZE", "expected_delta": expected}]}
        material = any(v is not None for v in observed.values())
        annotate_peer_invocations(probe, {"resource_deltas": [{"resource": "NETA", "material": material, "observed_delta": observed}]})
        return probe["resource_invocations"][0]

    no_change_expected = empty_expected_delta()
    changed = {key: None for key in no_change_expected}
    changed["action"] = "Changed the next move from BUILD to TEST."
    require(annotated(no_change_expected, changed)["expectation_mismatch"] is True, "material result after an all-false expectation must be marked")
    require(annotated(empty_expected_delta(action=True), changed)["expectation_mismatch"] is False, "expected material result must not be marked")
    require(annotated(no_change_expected, {key: None for key in no_change_expected})["expectation_mismatch"] is False, "Δ0 after an all-false expectation is not a mismatch")

    # Real positive controls: archived live traces that passed the pre-2026-09-29 gates.
    archived = sorted(PREFLIGHT_TRACES.glob("run*.json"))
    completed = [(p.name, json.loads(p.read_text(encoding="utf-8"))) for p in archived]
    completed = [(name, t) for name, t in completed if t.get("diagnosis") is not None]
    require(len(completed) == 7, f"expected 7 archived traces with a diagnosis, got {len(completed)}")
    for name, archived_trace in completed:
        try:
            validate_diagnosis(archived_trace["diagnosis"])
        except RuntimeErrorBounded as exc:
            require("saturated" in str(exc), f"{name}: archived diagnosis must fail on saturation")
        else:
            raise AssertionError(f"{name}: archived saturated diagnosis stayed green")

    repeated_names = set()
    mismatches = 0
    for name, archived_trace in completed:
        try:
            validate_synthesis(archived_trace["synthesis"], archived_trace["routing"]["resources"])
        except RuntimeErrorBounded as exc:
            require("repeats identical text" in str(exc), f"{name}: archived synthesis must fail only on repeated delta text")
            repeated_names.add(name.split("-DR-")[0])
        reannotated = copy.deepcopy(archived_trace)
        annotate_peer_invocations(reannotated, reannotated["synthesis"])
        mismatches += sum(1 for inv in reannotated["resource_invocations"] if inv.get("expectation_mismatch") is True)
    require(repeated_names == {"run17", "run19", "run20-attempt1", "run20-attempt2"}, f"repeated-text control drifted: {sorted(repeated_names)}")
    require(mismatches == 5, f"expected 5 archived expectation mismatches, got {mismatches}")

    pending = run(task, config={"adapters": {}}, mock=False, strict=False)
    require(pending["final_state"] == "PENDING_RESOURCE", "unwired real runtime must expose pending R&D rather than fabricate output")

    print("CALIBRATION LOOP OK: routing, independence, authority, prospective resource-delta accounting and saturation/repetition controls passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
