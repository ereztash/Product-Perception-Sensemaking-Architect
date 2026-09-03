#!/usr/bin/env python3
"""Executable contract for Neta's research quarantine.

Stdlib only. The point is not full JSON-Schema compliance; the point is to make
promotion and register invariants executable and prove the checker can fail on
deliberate violations in the same run.
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
CONTRADICTION_TYPES = {
    "REFUTES",
    "NARROWS",
    "SPLITS",
    "CONTEXTUALIZES",
    "MEASUREMENT_CONFLICT",
    "NO_MATERIAL_EFFECT",
}

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


def nonempty_text(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def split_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def read_tsv(rel: str) -> list[dict[str, str]]:
    path = ROOT / rel
    require(path.exists(), f"missing register {rel}")
    with path.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.reader(fh, delimiter="\t")
        rows = list(reader)
    require(rows, f"empty register {rel}")
    expected = EXPECTED_HEADERS[rel]
    require(rows[0] == expected, f"header drift in {rel}: {rows[0]}")
    parsed: list[dict[str, str]] = []
    for line_no, raw in enumerate(rows[1:], start=2):
        if not raw or not any(cell.strip() for cell in raw):
            continue
        require(
            len(raw) == len(expected),
            f"column-count drift in {rel}:{line_no}: expected {len(expected)}, got {len(raw)}",
        )
        parsed.append(dict(zip(expected, raw, strict=True)))
    return parsed


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
    require(nonempty_text(c["candidate_wording"]) and len(c["candidate_wording"].strip()) >= 8,
            "candidate wording too short")
    require(nonempty_text(c["observable_construct"]), "observable construct required")
    require(isinstance(c["neighboring_explanations"], list) and len(c["neighboring_explanations"]) <= 5,
            "neighboring explanations must be a list of at most five")
    require(c["culture_relevance"] in {"material", "plausible", "low"},
            "culture_relevance must be material/plausible/low")
    require(nonempty_text(c["culture_relevance_rationale"]),
            "culture relevance needs a rationale")
    require(nonempty_text(c["reversal_condition"]),
            "every claim needs a reversal condition")
    validate_vector(c["vector"])

    forbidden = {"confidence", "confidence_score", "certainty", "probability"}
    require(not (forbidden & set(c)), "numeric/scalar confidence field is forbidden")

    rank = [
        "QUARANTINE", "TRIANGULATED", "ADVERSARIAL", "BOUNDED",
        "FIXTURE_READY", "CANDIDATE_CAPABILITY", "PROMPT_ELIGIBLE",
    ]
    i = rank.index(c["status"]) if c["status"] in rank else -1

    if i >= 1:
        require(len(set(c["independence_families"])) >= 2,
                "TRIANGULATED+ requires at least two independent evidence families")
        require(len(c["supporting_source_ids"]) >= 2,
                "TRIANGULATED+ requires at least two recorded sources")

    if i >= 2:
        require(c["counterevidence_search_completed"] is True,
                "ADVERSARIAL+ requires completed counterevidence search")
        require(nonempty_text(c.get("counterevidence_strategy")),
                "ADVERSARIAL+ requires counterevidence strategy")
        require(len(c["neighboring_explanations"]) >= 1,
                "ADVERSARIAL+ requires a neighboring explanation")
        require(c["vector"]["A"] >= 2, "ADVERSARIAL+ requires A>=2")

    if i >= 3:
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

    if i >= 4:
        require(nonempty_text(c.get("discriminator")),
                "FIXTURE_READY+ requires a discriminator")
        require(nonempty_text(c.get("fixture_path")),
                "FIXTURE_READY+ requires fixture_path")
        require(c["vector"]["O"] >= 3, "FIXTURE_READY+ requires O>=3")

    if i >= 5:
        require(c["vector"]["G"] >= 3, "CANDIDATE_CAPABILITY+ requires G>=3")
        require(c["vector"]["A"] >= 2, "CANDIDATE_CAPABILITY+ requires A>=2")
        require(c["vector"]["O"] >= 3, "CANDIDATE_CAPABILITY+ requires O>=3")
        require(not c.get("unresolved_material_contradiction", False),
                "candidate capability cannot carry unresolved material contradiction")

    if i >= 6:
        require(nonempty_text(c.get("prompt_rule_candidate")),
                "PROMPT_ELIGIBLE requires smallest prompt rule candidate")
        require(nonempty_text(c.get("neighbor_behavior_at_risk")),
                "PROMPT_ELIGIBLE requires neighboring behavior at risk")


def validate_contradiction_row(
    row: dict[str, str],
    claim_by_id: dict[str, dict],
    source_ids: set[str],
) -> None:
    require(nonempty_text(row.get("contradiction_id")), "contradiction_id required")
    require(row.get("claim_id") in claim_by_id, f"unknown contradiction claim: {row.get('claim_id')}")
    require(row.get("source_id") in source_ids, f"unknown contradiction source: {row.get('source_id')}")
    ctype = row.get("contradiction_type")
    disposition = row.get("disposition")
    require(ctype in CONTRADICTION_TYPES, f"unknown contradiction_type: {ctype}")
    require(disposition in CONTRADICTION_TYPES, f"unknown contradiction disposition: {disposition}")
    require(ctype == disposition, "contradiction_type and disposition must agree in v1")
    require(nonempty_text(row.get("description")), "contradiction description required")
    require(nonempty_text(row.get("resolution_notes")), "contradiction resolution_notes required")

    children = split_ids(row.get("child_claim_ids", ""))
    if disposition == "SPLITS":
        require(children, "SPLITS requires child_claim_ids")
        parent_id = row["claim_id"]
        for child_id in children:
            require(child_id in claim_by_id, f"SPLITS child claim missing: {child_id}")
            require(
                claim_by_id[child_id].get("recursive_parent_id") == parent_id,
                f"SPLITS child {child_id} must name recursive_parent_id={parent_id}",
            )
        require(
            claim_by_id[parent_id].get("status") not in {"CANDIDATE_CAPABILITY", "PROMPT_ELIGIBLE"},
            "a parent with unresolved SPLITS may not be promoted unchanged",
        )
    else:
        require(not children, f"{disposition} must not carry child_claim_ids")


def validate_registers() -> None:
    sources = read_tsv("research/registers/sources.tsv")
    contradictions = read_tsv("research/registers/contradictions.tsv")
    culture_rows = read_tsv("research/registers/culture-scope.tsv")

    source_ids = [row["source_id"] for row in sources]
    require(all(nonempty_text(sid) for sid in source_ids), "every source needs source_id")
    require(len(source_ids) == len(set(source_ids)), "duplicate source ids")
    source_id_set = set(source_ids)
    for row in sources:
        families = split_ids(row["capability_family"])
        require(families and all(f in CAPABILITIES for f in families),
                f"invalid source capability family: {row['capability_family']}")
        require(nonempty_text(row["citation"]), f"source {row['source_id']} needs citation")
        require(nonempty_text(row["independence_family"]),
                f"source {row['source_id']} needs independence_family")

    claims_path = ROOT / "research/registers/claims.json"
    data = json.loads(claims_path.read_text(encoding="utf-8"))
    require(data.get("schema_version") == "1.0", "claim register schema_version drift")
    require(data.get("wave") == "WAVE1", "claim register wave drift")
    require(isinstance(data.get("source_collection_started"), bool),
            "source_collection_started must be boolean")
    require(not sources or data["source_collection_started"] is True,
            "sources exist while source_collection_started is false")

    claims = data.get("claims")
    require(isinstance(claims, list), "claims must be a list")
    claim_ids: list[str] = []
    claim_by_id: dict[str, dict] = {}
    for claim in claims:
        validate_claim(claim)
        claim_id = claim["claim_id"]
        claim_ids.append(claim_id)
        claim_by_id[claim_id] = claim
    require(len(claim_ids) == len(set(claim_ids)), "duplicate claim ids")

    contradiction_ids: list[str] = []
    contradiction_by_id: dict[str, dict[str, str]] = {}
    for row in contradictions:
        validate_contradiction_row(row, claim_by_id, source_id_set)
        cid = row["contradiction_id"]
        contradiction_ids.append(cid)
        contradiction_by_id[cid] = row
    require(len(contradiction_ids) == len(set(contradiction_ids)), "duplicate contradiction ids")

    for claim in claims:
        for source_id in claim["supporting_source_ids"]:
            require(source_id in source_id_set,
                    f"claim {claim['claim_id']} references unknown source {source_id}")
        for contradiction_id in claim["contradiction_ids"]:
            require(contradiction_id in contradiction_by_id,
                    f"claim {claim['claim_id']} references unknown contradiction {contradiction_id}")
            require(contradiction_by_id[contradiction_id]["claim_id"] == claim["claim_id"],
                    f"contradiction {contradiction_id} belongs to a different claim")
        if claim.get("recursive_parent_id") is not None:
            require(claim["recursive_parent_id"] in claim_by_id,
                    f"claim {claim['claim_id']} has unknown recursive_parent_id")

    scope_ids: list[str] = []
    for row in culture_rows:
        scope_ids.append(row["scope_id"])
        require(nonempty_text(row["scope_id"]), "culture scope_id required")
        require(row["claim_id"] in claim_by_id, f"unknown culture-scope claim: {row['claim_id']}")
        if nonempty_text(row["source_id"]):
            require(row["source_id"] in source_id_set,
                    f"unknown culture-scope source: {row['source_id']}")
        require(row["represented_or_missing"] in {"represented", "missing"},
                "culture scope must be represented or missing")
    require(len(scope_ids) == len(set(scope_ids)), "duplicate culture scope ids")


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
    controls: list[tuple[str, dict]] = []

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

    # Register-level control: a split without actual descendants must never pass.
    synthetic_parent = copy.deepcopy(valid)
    synthetic_parent["claim_id"] = "W1-TEST-001"
    synthetic_parent["status"] = "BOUNDED"
    split_without_children = {
        "contradiction_id": "C-TEST",
        "claim_id": "W1-TEST-001",
        "source_id": "S1",
        "contradiction_type": "SPLITS",
        "description": "deliberate broken split",
        "disposition": "SPLITS",
        "child_claim_ids": "",
        "resolution_notes": "control",
    }
    try:
        validate_contradiction_row(
            split_without_children,
            {"W1-TEST-001": synthetic_parent},
            {"S1"},
        )
    except ValueError:
        pass
    else:
        fail("NOT-A-GATE: positive control stayed green: split-without-children")


def main() -> None:
    validate_registers()
    validate_preregistration()

    fixture = json.loads((ROOT / "fixtures/research-valid-candidate.json").read_text(encoding="utf-8"))
    validate_claim(fixture)
    positive_controls(fixture)

    print("RESEARCH-CONTRACT: PASS")
    print("positive controls: 6/6 correctly failed")


if __name__ == "__main__":
    main()
