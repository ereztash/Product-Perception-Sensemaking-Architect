#!/usr/bin/env python3
"""Executable contract for Neta's research quarantine.

Stdlib only. The point is not full JSON-Schema compliance; the point is to make
promotion invariants executable and prove the checker can fail on deliberate
violations in the same run.
"""

from __future__ import annotations

import copy
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STATUSES = {
    "QUARANTINE",
    "TRIANGULATED",
    "ADVERSARIAL",
    "BOUNDED",
    "FIXTURE_READY",
    "CANDIDATE_CAPABILITY",
    "PROMPT_ELIGIBLE",
    "DEFER_FIELD",
    "REJECTED",
}
CAPABILITIES = {f"W{i}" for i in range(1, 9)}

EXPECTED_HEADERS = {
    "research/registers/sources.tsv": [
        "source_id", "capability_family", "citation", "url_or_locator",
        "source_type", "discipline", "population_or_context", "culture_axes",
        "independence_family", "primary_or_secondary", "claim_ids", "notes",
    ],
    "research/registers/contradictions.tsv": [
        "contradiction_id", "claim_id", "source_id", "contradiction_type",
        "description", "disposition", "child_claim_ids", "resolution_notes",
    ],
    "research/registers/culture-scope.tsv": [
        "scope_id", "claim_id", "source_id", "geography_or_community", "language",
        "script_direction", "visual_density_convention", "communication_context",
        "expertise_or_fluency", "domain_culture", "institutional_context",
        "accessibility_or_cognitive_context", "device_or_infrastructure",
        "represented_or_missing", "notes",
    ],
}


def fail(msg: str) -> None:
    raise ValueError(msg)


def require(condition: bool, msg: str) -> None:
    if not condition:
        fail(msg)


def validate_vector(vector: dict) -> None:
    require(set(vector) == {"G", "C", "A", "O"}, "vector must contain exactly G/C/A/O")
    require(isinstance(vector["G"], int) and 1 <= vector["G"] <= 7, "G out of range")
    require(isinstance(vector["C"], int) and 0 <= vector["C"] <= 4, "C out of range")
    require(isinstance(vector["A"], int) and 0 <= vector["A"] <= 4, "A out of range")
    require(isinstance(vector["O"], int) and 0 <= vector["O"] <= 5, "O out of range")


def validate_claim(c: dict) -> None:
    required = {
        "claim_id", "wave", "capability_family", "candidate_wording",
        "observable_construct", "neighboring_explanations", "supporting_source_ids",
        "independence_families", "counterevidence_search_completed",
        "contradiction_ids", "culture_relevance", "culture_relevance_rationale",
        "represented_contexts", "missing_contexts", "boundary_conditions",
        "reversal_condition", "vector", "status",
    }
    missing = sorted(required - set(c))
    require(not missing, f"missing required fields: {missing}")
    require(c["wave"] == "WAVE1", "wave must be WAVE1")
    require(c["capability_family"] in CAPABILITIES, "unknown capability family")
    require(c["status"] in STATUSES, "unknown status")
    require(isinstance(c["candidate_wording"], str) and len(c["candidate_wording"].strip()) >= 8,
            "candidate wording too short")
    require(isinstance(c["observable_construct"], str) and c["observable_construct"].strip(),
            "observable construct required")
    require(isinstance(c["neighboring_explanations"], list) and len(c["neighboring_explanations"]) <= 5,
            "neighboring explanations must be a list of at most five")
    require(c["culture_relevance"] in {"material", "plausible", "low"},
            "culture_relevance must be material/plausible/low")
    require(isinstance(c["culture_relevance_rationale"], str) and c["culture_relevance_rationale"].strip(),
            "culture relevance needs a rationale")
    require(isinstance(c["reversal_condition"], str) and c["reversal_condition"].strip(),
            "every claim needs a reversal condition")
    validate_vector(c["vector"])

    # No scalar confidence theatre.
    forbidden = {"confidence", "confidence_score", "certainty", "probability"}
    require(not (forbidden & set(c)), "numeric/scalar confidence field is forbidden")

    status = c["status"]
    rank = [
        "QUARANTINE", "TRIANGULATED", "ADVERSARIAL", "BOUNDED",
        "FIXTURE_READY", "CANDIDATE_CAPABILITY", "PROMPT_ELIGIBLE",
    ]
    if status in rank:
        i = rank.index(status)
    else:
        i = -1

    if i >= 1:  # TRIANGULATED+
        require(len(set(c["independence_families"])) >= 2,
                "TRIANGULATED+ requires at least two independent evidence families")
        require(len(c["supporting_source_ids"]) >= 2,
                "TRIANGULATED+ requires at least two recorded sources")

    if i >= 2:  # ADVERSARIAL+
        require(c["counterevidence_search_completed"] is True,
                "ADVERSARIAL+ requires completed counterevidence search")
        require(bool(str(c.get("counterevidence_strategy", "")).strip()),
                "ADVERSARIAL+ requires counterevidence strategy")
        require(len(c["neighboring_explanations"]) >= 1,
                "ADVERSARIAL+ requires a neighboring explanation")
        require(c["vector"]["A"] >= 2, "ADVERSARIAL+ requires A>=2")

    if i >= 3:  # BOUNDED+
        if c["culture_relevance"] in {"material", "plausible"}:
            require(len(c["represented_contexts"]) >= 1,
                    "culture-relevant BOUNDED+ claim needs represented contexts")
            require(len(c["missing_contexts"]) >= 1,
                    "culture-relevant BOUNDED+ claim must name missing contexts")
            require(c["vector"]["C"] >= 1,
                    "culture-relevant BOUNDED+ claim requires C>=1")
        else:
            require("universal" not in c["culture_relevance_rationale"].lower(),
                    "low culture relevance may not be justified by saying universal")

    if i >= 4:  # FIXTURE_READY+
        require(bool(str(c.get("discriminator", "")).strip()),
                "FIXTURE_READY+ requires a discriminator")
        require(bool(str(c.get("fixture_path", "")).strip()),
                "FIXTURE_READY+ requires fixture_path")
        require(c["vector"]["O"] >= 3, "FIXTURE_READY+ requires O>=3")

    if i >= 5:  # CANDIDATE_CAPABILITY+
        require(c["vector"]["G"] >= 3, "CANDIDATE_CAPABILITY+ requires G>=3")
        require(c["vector"]["A"] >= 2, "CANDIDATE_CAPABILITY+ requires A>=2")
        require(c["vector"]["O"] >= 3, "CANDIDATE_CAPABILITY+ requires O>=3")
        require(not c.get("unresolved_material_contradiction", False),
                "candidate capability cannot carry unresolved material contradiction")

    if i >= 6:  # PROMPT_ELIGIBLE
        require(bool(str(c.get("prompt_rule_candidate", "")).strip()),
                "PROMPT_ELIGIBLE requires smallest prompt rule candidate")
        require(bool(str(c.get("neighbor_behavior_at_risk", "")).strip()),
                "PROMPT_ELIGIBLE requires neighboring behavior at risk")


def validate_registers() -> None:
    for rel, expected in EXPECTED_HEADERS.items():
        path = ROOT / rel
        require(path.exists(), f"missing register {rel}")
        with path.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.reader(fh, delimiter="\t")
            actual = next(reader, [])
        require(actual == expected, f"header drift in {rel}: {actual}")

    claims_path = ROOT / "research/registers/claims.json"
    data = json.loads(claims_path.read_text(encoding="utf-8"))
    require(data.get("schema_version") == "1.0", "claim register schema_version drift")
    require(data.get("wave") == "WAVE1", "claim register wave drift")
    require(isinstance(data.get("source_collection_started"), bool),
            "source_collection_started must be boolean")
    claims = data.get("claims")
    require(isinstance(claims, list), "claims must be a list")
    ids = []
    for claim in claims:
        validate_claim(claim)
        ids.append(claim["claim_id"])
    require(len(ids) == len(set(ids)), "duplicate claim ids")


def validate_preregistration() -> None:
    text = (ROOT / "research/WAVE1_PREREGISTRATION.md").read_text(encoding="utf-8")
    required_tokens = [
        "FROZEN BEFORE SOURCE COLLECTION",
        "W1. Tacit → explicit design knowledge",
        "W2. Perceptual hierarchy",
        "W3. Aesthetic judgment / perceived craft",
        "W4. Interaction feedback",
        "W5. Cognitive economy",
        "W6. Orientation & navigation",
        "W7. Trust & uncertainty communication",
        "W8. Adaptive instrumentation",
        "two consecutive recursion passes",
        "Do not change promotion thresholds to rescue a favored claim",
    ]
    for token in required_tokens:
        require(token in text, f"preregistration invariant missing: {token}")


def positive_controls(valid: dict) -> None:
    controls = []

    c = copy.deepcopy(valid)
    c["status"] = "TRIANGULATED"
    controls.append(("triangulated-one-family", c))

    c = copy.deepcopy(valid)
    c["status"] = "ADVERSARIAL"
    c["supporting_source_ids"] = ["S1", "S2"]
    c["independence_families"] = ["F1", "F2"]
    c["vector"]["A"] = 2
    controls.append(("adversarial-without-countersearch", c))

    c = copy.deepcopy(valid)
    c["status"] = "BOUNDED"
    c["supporting_source_ids"] = ["S1", "S2"]
    c["independence_families"] = ["F1", "F2"]
    c["counterevidence_search_completed"] = True
    c["counterevidence_strategy"] = "search contrary evidence"
    c["vector"]["A"] = 2
    c["represented_contexts"] = []
    c["missing_contexts"] = []
    controls.append(("bounded-without-culture-scope", c))

    c = copy.deepcopy(valid)
    c["status"] = "FIXTURE_READY"
    c["supporting_source_ids"] = ["S1", "S2"]
    c["independence_families"] = ["F1", "F2"]
    c["counterevidence_search_completed"] = True
    c["counterevidence_strategy"] = "search contrary evidence"
    c["vector"].update({"C": 1, "A": 2, "O": 3})
    c["represented_contexts"] = ["context A"]
    c["missing_contexts"] = ["context B"]
    c["fixture_path"] = None
    controls.append(("fixture-ready-without-fixture", c))

    c = copy.deepcopy(valid)
    c["confidence_score"] = 0.91
    controls.append(("fake-confidence-field", c))

    for name, broken in controls:
        try:
            validate_claim(broken)
        except ValueError:
            continue
        fail(f"NOT-A-GATE: positive control stayed green: {name}")


def main() -> None:
    validate_registers()
    validate_preregistration()

    fixture = json.loads((ROOT / "fixtures/research-valid-candidate.json").read_text(encoding="utf-8"))
    validate_claim(fixture)
    positive_controls(fixture)

    print("RESEARCH-CONTRACT: PASS")
    print("positive controls: 5/5 correctly failed")


if __name__ == "__main__":
    main()
