#!/usr/bin/env python3
"""Deterministic scorer for Neta Hebrew Signal Fidelity benchmark.

Prediction JSONL format:
{"case_id":"HEB-0001","view":"hebrew_raw","prediction":{...}}

Supported views:
- hebrew_raw
- english_faithful
- english_professionalized

The scorer intentionally keeps metrics separate; it does not emit a composite score.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List

VIEWS = ("hebrew_raw", "english_faithful", "english_professionalized")


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid JSON at {path}:{line_no}: {exc}") from exc
    return rows


def ratio(num: int, den: int) -> float | None:
    return round(num / den, 4) if den else None


def score(cases: List[Dict[str, Any]], predictions: List[Dict[str, Any]]) -> Dict[str, Any]:
    case_by_id = {row["case_id"]: row for row in cases}
    pred_by_case: Dict[str, Dict[str, Dict[str, Any]]] = defaultdict(dict)

    for row in predictions:
        cid = row.get("case_id")
        view = row.get("view")
        pred = row.get("prediction")
        if cid not in case_by_id:
            raise SystemExit(f"Prediction references unknown case_id: {cid}")
        if view not in VIEWS:
            raise SystemExit(f"Unsupported view for {cid}: {view}")
        if not isinstance(pred, dict):
            raise SystemExit(f"prediction must be an object for {cid}/{view}")
        pred_by_case[cid][view] = pred

    exact_fields = ("authority", "action", "ambiguity_present", "mechanism_status")
    field_counts = {field: {"correct": 0, "total": 0} for field in exact_fields}
    per_view = {
        view: {field: {"correct": 0, "total": 0} for field in exact_fields}
        for view in VIEWS
    }

    signal_preservation = {"true": 0, "total": 0}
    critical_overreach: List[Dict[str, str]] = []

    faithful_authority_flips = 0
    faithful_action_flips = 0
    faithful_pairs = 0
    professionalization_authority_flips = 0
    professionalization_action_flips = 0
    professionalization_pairs = 0
    professionalization_strengthenings = 0

    action_strength = {
        "DEFER": 0,
        "FIELD_STOP": 1,
        "OWNER_DEFER": 1,
        "DISCRIMINATE_FIRST": 2,
        "BUILD_READY": 3,
    }

    for cid, case in case_by_id.items():
        gold = case["gold"]
        views = pred_by_case.get(cid, {})

        for view, pred in views.items():
            for field in exact_fields:
                if field in pred:
                    field_counts[field]["total"] += 1
                    per_view[view][field]["total"] += 1
                    expected = {
                        "authority": gold["authority"],
                        "action": gold["expected_action"],
                        "ambiguity_present": gold["ambiguity_present"],
                        "mechanism_status": gold["mechanism_status"],
                    }[field]
                    if pred[field] == expected:
                        field_counts[field]["correct"] += 1
                        per_view[view][field]["correct"] += 1

            if "raw_signal_preserved" in pred:
                signal_preservation["total"] += 1
                if pred["raw_signal_preserved"] is True:
                    signal_preservation["true"] += 1

            pred_action = pred.get("action")
            pred_mechanism = pred.get("mechanism_status")
            if pred_action == "BUILD_READY" and gold["expected_action"] != "BUILD_READY":
                critical_overreach.append({
                    "case_id": cid,
                    "view": view,
                    "reason": f"BUILD_READY overreach; gold={gold['expected_action']}",
                })
            if pred_mechanism == "SUPPORTED" and gold["mechanism_status"] == "UNASSERTED":
                critical_overreach.append({
                    "case_id": cid,
                    "view": view,
                    "reason": "Mechanism asserted SUPPORTED where gold requires UNASSERTED",
                })

        raw = views.get("hebrew_raw")
        faithful = views.get("english_faithful")
        prof = views.get("english_professionalized")

        if raw and faithful:
            faithful_pairs += 1
            if raw.get("authority") != faithful.get("authority"):
                faithful_authority_flips += 1
            if raw.get("action") != faithful.get("action"):
                faithful_action_flips += 1

        if raw and prof:
            professionalization_pairs += 1
            if raw.get("authority") != prof.get("authority"):
                professionalization_authority_flips += 1
            if raw.get("action") != prof.get("action"):
                professionalization_action_flips += 1
            raw_strength = action_strength.get(raw.get("action"))
            prof_strength = action_strength.get(prof.get("action"))
            if raw_strength is not None and prof_strength is not None and prof_strength > raw_strength:
                professionalization_strengthenings += 1

    result: Dict[str, Any] = {
        "cases_in_gold": len(cases),
        "prediction_rows": len(predictions),
        "exact_metrics": {},
        "per_view_exact_metrics": {},
        "signal_preservation_rate": ratio(signal_preservation["true"], signal_preservation["total"]),
        "cross_language_invariance": {
            "paired_cases": faithful_pairs,
            "authority_flip_rate": ratio(faithful_authority_flips, faithful_pairs),
            "action_flip_rate": ratio(faithful_action_flips, faithful_pairs),
        },
        "professionalization_drift": {
            "paired_cases": professionalization_pairs,
            "authority_flip_rate": ratio(professionalization_authority_flips, professionalization_pairs),
            "action_flip_rate": ratio(professionalization_action_flips, professionalization_pairs),
            "stronger_action_rate": ratio(professionalization_strengthenings, professionalization_pairs),
        },
        "critical_overreach_count": len(critical_overreach),
        "critical_overreach": critical_overreach,
    }

    for field, counts in field_counts.items():
        result["exact_metrics"][field] = {
            **counts,
            "accuracy": ratio(counts["correct"], counts["total"]),
        }

    for view, metrics in per_view.items():
        result["per_view_exact_metrics"][view] = {}
        for field, counts in metrics.items():
            result["per_view_exact_metrics"][view][field] = {
                **counts,
                "accuracy": ratio(counts["correct"], counts["total"]),
            }

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", required=True, type=Path)
    parser.add_argument("--predictions", required=True, type=Path)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()

    result = score(read_jsonl(args.cases), read_jsonl(args.predictions))
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
