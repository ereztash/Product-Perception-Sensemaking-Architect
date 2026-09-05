#!/usr/bin/env python3
"""Provider-neutral command adapters and deterministic mocks for Calibration Loop v0.1."""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass


class AdapterError(RuntimeError):
    pass


@dataclass(frozen=True)
class CommandAdapter:
    resource: str
    command: list[str]

    def invoke(self, request: dict) -> dict:
        try:
            proc = subprocess.run(
                self.command,
                input=json.dumps(request, ensure_ascii=False),
                text=True,
                capture_output=True,
                check=False,
            )
        except OSError as exc:
            raise AdapterError(f"{self.resource} adapter failed to start: {exc}") from exc

        if proc.returncode != 0:
            detail = proc.stderr.strip() or proc.stdout.strip() or f"exit={proc.returncode}"
            raise AdapterError(f"{self.resource} adapter failed: {detail}")

        try:
            payload = json.loads(proc.stdout)
        except json.JSONDecodeError as exc:
            raise AdapterError(f"{self.resource} adapter returned non-JSON output") from exc
        if not isinstance(payload, dict):
            raise AdapterError(f"{self.resource} adapter must return one JSON object")
        return payload


def mock_rnd_diagnosis(task: dict) -> dict:
    """A deliberate deterministic mock for CI; not a model of real R&D judgment."""
    return {
        "material_question": task["decision_blocked"]["statement"],
        "bottleneck": "The architecture capability is desired but its unique decision value versus existing resources is not yet discriminated.",
        "resource_assessment": [
            {
                "resource": "NETA",
                "expected_contribution": "Challenge framing, proxy substitution and premature intervention.",
                "authority_ceiling": "Cannot establish architecture doctrine or external empirical validity.",
                "uncertainty": "Unknown marginal value until compared with other resources on the same task."
            },
            {
                "resource": "SCAFFOLD",
                "expected_contribution": "Generate broad architecture alternatives and candidate judgment dimensions.",
                "authority_ceiling": "Candidate reasoning only; not independent empirical evidence.",
                "uncertainty": "May add breadth without changing the blocked decision."
            },
            {
                "resource": "RND",
                "expected_contribution": "Compare evidence/resource deltas and decide the cheapest next learning move.",
                "authority_ceiling": "Cannot close OWNER/FIELD/REPO/ENVIRONMENT claims outside their authorities.",
                "uncertainty": "v0.2 calibration telos is a candidate and not yet validated."
            }
        ],
        "candidate_moves": [
            {
                "move": "INVOKE_NETA",
                "resource": "NETA",
                "expected_decision_value": "Reduce proxy/framing error before an Architecture Agent is specified.",
                "reversibility": "HIGH"
            },
            {
                "move": "USE_SCAFFOLD",
                "resource": "SCAFFOLD",
                "expected_decision_value": "Expand candidate architecture judgments before fixtures are frozen.",
                "reversibility": "HIGH"
            },
            {
                "move": "RESEARCH",
                "resource": "RND",
                "expected_decision_value": "Test which candidate judgments survive external evidence and OSS counterexamples.",
                "reversibility": "HIGH"
            }
        ],
        "needs": {
            "signal_interpretation_ambiguity": True,
            "multiple_plausible_mechanisms": True,
            "proxy_substitution_risk": True,
            "research_to_intervention_transition": True,
            "broad_reasoning_needed": True,
            "architecture_alternatives_needed": True,
            "novel_synthesis_needed": False,
            "external_research_needed": True,
            "owner_authority_needed": False,
            "repo_authority_needed": False,
            "environment_authority_needed": False,
            "field_authority_needed": False
        },
        "rationale": "Use Neta and scaffold as independent resources, then let R&D compare their decision deltas before allocating further research/build effort.",
    }


def mock_neta_result(request: dict) -> dict:
    return {
        "resource": "NETA",
        "summary": "Do not equate architecture metrics, diagrams or pattern names with architectural quality; first separate observable structure from competing failure mechanisms and the decision they would change.",
        "unique_delta": "Exposes proxy substitution and premature build risk in the Architecture Agent brief.",
        "evidence_refs": [],
        "limitations": ["Does not establish which architecture mechanisms are externally valid."],
    }


def mock_scaffold_result(request: dict) -> dict:
    return {
        "resource": "SCAFFOLD",
        "summary": "Candidate architecture judgments include boundary choice, dependency direction, invariant preservation, failure-domain isolation, change propagation and migration reversibility.",
        "unique_delta": "Expands the candidate architecture judgment space without claiming those candidates are validated.",
        "evidence_refs": [],
        "limitations": ["Broad reasoning scaffold is not independent empirical evidence."],
    }


def mock_rnd_synthesis(task: dict, diagnosis: dict, resource_results: list[dict], route: dict) -> dict:
    by_resource = {r.get("resource"): r for r in resource_results if isinstance(r, dict)}
    deltas = []
    for resource in ("NETA", "SCAFFOLD"):
        if resource in by_resource:
            result = by_resource[resource]
            deltas.append({
                "resource": resource,
                "material": True,
                "unique_delta": result.get("unique_delta", ""),
            })
    return {
        "decision_before": task["decision_blocked"]["current_default"],
        "decision_after": "Freeze an Architecture Agent telos/authority brief and judgment fixtures before implementing a full architecture agent.",
        "next_move": "Use the combined deltas to define the smallest Architecture Agent judgment surface; then let R&D research/falsify those candidate judgments before build.",
        "resource_deltas": deltas,
        "learning_records": [
            {
                "resource": d["resource"],
                "invoked_because": route.get("fired", {}).get(d["resource"], []),
                "material": d["material"],
                "unique_delta": d["unique_delta"],
            }
            for d in deltas
        ],
        "stop_or_continue": "CONTINUE",
        "routing_amendment_proposed": None,
    }
