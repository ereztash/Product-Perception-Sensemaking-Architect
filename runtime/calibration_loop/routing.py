#!/usr/bin/env python3
"""Deterministic routing law for Calibration Loop v0.1."""

from __future__ import annotations

from dataclasses import dataclass

NETA_TRIGGERS = {
    "signal_interpretation_ambiguity",
    "multiple_plausible_mechanisms",
    "proxy_substitution_risk",
    "research_to_intervention_transition",
}

SCAFFOLD_TRIGGERS = {
    "broad_reasoning_needed",
    "architecture_alternatives_needed",
    "novel_synthesis_needed",
}

AUTHORITY_FLAGS = {
    "owner_authority_needed": "OWNER",
    "repo_authority_needed": "REPO",
    "environment_authority_needed": "ENVIRONMENT",
    "field_authority_needed": "FIELD",
}

ALL_NEED_KEYS = NETA_TRIGGERS | SCAFFOLD_TRIGGERS | set(AUTHORITY_FLAGS) | {
    "external_research_needed",
}


@dataclass(frozen=True)
class RouteDecision:
    resources: tuple[str, ...]
    fired: dict[str, list[str]]
    authority_handoffs: tuple[str, ...]

    def as_dict(self) -> dict:
        return {
            "resources": list(self.resources),
            "fired": self.fired,
            "authority_handoffs": list(self.authority_handoffs),
        }


def _true_keys(needs: dict, candidates: set[str]) -> list[str]:
    return sorted(k for k in candidates if needs.get(k) is True)


def route(diagnosis: dict, allowed_resources: list[str]) -> RouteDecision:
    """Return deterministic resource routing from an R&D diagnosis.

    R&D itself is not included here because it is always invoked before and after
    this gate by the runner.
    """
    needs = diagnosis.get("needs")
    if not isinstance(needs, dict):
        raise ValueError("diagnosis.needs must be an object")

    unknown = set(needs) - ALL_NEED_KEYS
    if unknown:
        raise ValueError(f"unknown diagnosis need keys: {sorted(unknown)}")

    allowed = set(allowed_resources)
    resources: list[str] = []
    fired: dict[str, list[str]] = {}

    neta = _true_keys(needs, NETA_TRIGGERS)
    if neta:
        fired["NETA"] = neta
        if "NETA" in allowed:
            resources.append("NETA")

    scaffold = _true_keys(needs, SCAFFOLD_TRIGGERS)
    if scaffold:
        fired["SCAFFOLD"] = scaffold
        if "SCAFFOLD" in allowed:
            resources.append("SCAFFOLD")

    if needs.get("external_research_needed") is True:
        fired["RND_RESEARCH"] = ["external_research_needed"]

    handoffs: list[str] = []
    for flag, authority in AUTHORITY_FLAGS.items():
        if needs.get(flag) is True:
            handoffs.append(authority)
            fired.setdefault("AUTHORITY", []).append(flag)

    return RouteDecision(
        resources=tuple(resources),
        fired=fired,
        authority_handoffs=tuple(sorted(handoffs)),
    )
