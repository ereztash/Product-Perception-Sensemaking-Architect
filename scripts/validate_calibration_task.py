#!/usr/bin/env python3
"""Validate Calibration Loop v0.1 task inputs with stdlib-only semantics."""

from __future__ import annotations

import json
import sys
from pathlib import Path

RESOURCES = {"RND", "NETA", "SCAFFOLD", "OWNER", "REPO", "ENVIRONMENT", "FIELD"}


class ContractError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ContractError(message)


def nonempty(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate(payload: dict) -> None:
    require(isinstance(payload, dict), "calibration task must be an object")
    required = {
        "calibration_version",
        "task_id",
        "telos",
        "current_state",
        "decision_blocked",
        "allowed_resources",
        "context_refs",
    }
    optional = {"signals", "budget"}
    require(required <= set(payload), f"missing fields: {sorted(required - set(payload))}")
    require(set(payload) <= required | optional, f"unknown fields: {sorted(set(payload) - required - optional)}")
    require(payload["calibration_version"] == "0.1", "calibration_version must be 0.1")
    require(nonempty(payload["task_id"]), "task_id required")

    telos = payload["telos"]
    require(isinstance(telos, dict) and set(telos) == {"statement", "success_condition"}, "telos fields drift")
    require(nonempty(telos["statement"]), "telos.statement required")
    require(nonempty(telos["success_condition"]), "telos.success_condition required")

    state = payload["current_state"]
    require(isinstance(state, dict), "current_state must be object")
    require(set(state) == {"summary", "known_constraints", "available_resources"}, "current_state fields drift")
    require(nonempty(state["summary"]), "current_state.summary required")
    constraints = state["known_constraints"]
    require(isinstance(constraints, list) and all(nonempty(x) for x in constraints), "known_constraints must be strings")
    available = state["available_resources"]
    require(isinstance(available, list) and len(available) == len(set(available)), "available_resources must be unique list")
    require(set(available) <= RESOURCES, "unknown available resource")
    require("RND" in available, "RND must be available: it owns calibration diagnosis/synthesis")

    decision = payload["decision_blocked"]
    require(isinstance(decision, dict), "decision_blocked must be object")
    require(set(decision) == {"statement", "current_default", "reversal_condition"}, "decision_blocked fields drift")
    for key in decision:
        require(nonempty(decision[key]), f"decision_blocked.{key} required")

    allowed = payload["allowed_resources"]
    require(isinstance(allowed, list) and len(allowed) >= 1, "allowed_resources must be non-empty list")
    require(len(allowed) == len(set(allowed)), "allowed_resources must be unique")
    require(set(allowed) <= RESOURCES, "unknown allowed resource")
    require("RND" in allowed, "RND must be allowed")
    require(set(allowed) <= set(available), "allowed_resources must be a subset of current_state.available_resources")

    refs = payload["context_refs"]
    require(isinstance(refs, list) and all(nonempty(x) for x in refs), "context_refs must be strings")

    signals = payload.get("signals", [])
    require(isinstance(signals, list) and all(nonempty(x) for x in signals), "signals must be strings")

    budget = payload.get("budget")
    if budget is not None:
        require(isinstance(budget, dict), "budget must be object or null")
        require(set(budget) == {"max_resource_calls", "max_parallel_calls"}, "budget fields drift")
        require(isinstance(budget["max_resource_calls"], int) and budget["max_resource_calls"] >= 2, "budget.max_resource_calls >= 2")
        require(isinstance(budget["max_parallel_calls"], int) and budget["max_parallel_calls"] >= 1, "budget.max_parallel_calls >= 1")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_calibration_task.py <task.json>", file=sys.stderr)
        return 2
    path = Path(argv[1])
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        validate(payload)
    except (OSError, json.JSONDecodeError, ContractError) as exc:
        print(f"INVALID CALIBRATION TASK: {exc}", file=sys.stderr)
        return 1
    print("CALIBRATION TASK OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
