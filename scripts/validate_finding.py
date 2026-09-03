#!/usr/bin/env python3
"""Validate the executable subset of Neta's finding contract.

Stdlib-only by design. The JSON Schema is the declarative source; this file enforces the
load-bearing rules in CI without adding a dependency on jsonschema.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

STATUSES = {"DISCRIMINATE_FIRST", "BUILD_READY", "FIELD_STOP"}
AUTHORITIES = {"OWNER", "REPO", "DESIGN_MECHANISM", "FIELD"}
EVIDENCE_STATES = {
    "OWNER_SIGNAL",
    "REPRODUCED",
    "MECHANISM_SUPPORTED",
    "MEASURED",
    "FIELD_REQUIRED",
    "FIELD_REPLICATED",
}

REQUIRED = {
    "status",
    "raw_signal",
    "observations",
    "candidate_mechanisms",
    "authority",
    "evidence_state",
    "next_step",
}

ALLOWED = REQUIRED | {
    "design_distinction",
    "rejected_explanations",
    "intervention",
    "must_not_change",
    "perceptual_success_criterion",
    "check",
    "reversal_condition",
}

MECHANISM_KEYS = {"name", "explains", "does_not_explain", "discriminator"}


class ContractError(ValueError):
    pass


def _nonempty_string(value: Any, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{field} must be a non-empty string")


def _string_list(value: Any, field: str) -> None:
    if not isinstance(value, list):
        raise ContractError(f"{field} must be a list")
    for index, item in enumerate(value):
        _nonempty_string(item, f"{field}[{index}]")


def validate(payload: dict[str, Any]) -> None:
    if not isinstance(payload, dict):
        raise ContractError("finding must be a JSON object")

    missing = REQUIRED - payload.keys()
    if missing:
        raise ContractError(f"missing required fields: {sorted(missing)}")

    unknown = payload.keys() - ALLOWED
    if unknown:
        raise ContractError(f"unknown top-level fields: {sorted(unknown)}")

    if payload["status"] not in STATUSES:
        raise ContractError(f"invalid status: {payload['status']!r}")
    if payload["authority"] not in AUTHORITIES:
        raise ContractError(f"invalid authority: {payload['authority']!r}")
    if payload["evidence_state"] not in EVIDENCE_STATES:
        raise ContractError(f"invalid evidence_state: {payload['evidence_state']!r}")

    _nonempty_string(payload["raw_signal"], "raw_signal")
    _nonempty_string(payload["next_step"], "next_step")
    _string_list(payload["observations"], "observations")

    mechanisms = payload["candidate_mechanisms"]
    if not isinstance(mechanisms, list):
        raise ContractError("candidate_mechanisms must be a list")
    if len(mechanisms) > 3:
        raise ContractError("candidate_mechanisms may contain at most 3 items")

    for index, mechanism in enumerate(mechanisms):
        if not isinstance(mechanism, dict):
            raise ContractError(f"candidate_mechanisms[{index}] must be an object")
        if set(mechanism) != MECHANISM_KEYS:
            raise ContractError(
                f"candidate_mechanisms[{index}] must contain exactly {sorted(MECHANISM_KEYS)}"
            )
        for key in MECHANISM_KEYS:
            _nonempty_string(mechanism[key], f"candidate_mechanisms[{index}].{key}")

    if "rejected_explanations" in payload:
        _string_list(payload["rejected_explanations"], "rejected_explanations")

    for optional in (
        "design_distinction",
        "intervention",
        "must_not_change",
        "perceptual_success_criterion",
        "check",
        "reversal_condition",
    ):
        if optional in payload and payload[optional] is not None:
            _nonempty_string(payload[optional], optional)

    status = payload["status"]

    if status == "DISCRIMINATE_FIRST":
        if not 1 <= len(mechanisms) <= 3:
            raise ContractError("DISCRIMINATE_FIRST requires 1-3 candidate mechanisms")

    if status == "BUILD_READY":
        for field in (
            "design_distinction",
            "intervention",
            "perceptual_success_criterion",
            "reversal_condition",
        ):
            if not payload.get(field):
                raise ContractError(f"BUILD_READY requires {field}")

    if status == "FIELD_STOP":
        if payload["authority"] != "FIELD":
            raise ContractError("FIELD_STOP requires authority=FIELD")
        if payload["evidence_state"] not in {"FIELD_REQUIRED", "FIELD_REPLICATED"}:
            raise ContractError(
                "FIELD_STOP requires evidence_state FIELD_REQUIRED or FIELD_REPLICATED"
            )


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ContractError("top-level JSON value must be an object")
    return value


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_finding.py FINDING.json", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        validate(load(path))
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1

    print("VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
