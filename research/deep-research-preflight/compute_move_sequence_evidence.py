#!/usr/bin/env python3
"""Deterministic evidence execution for the recursive Erez281 R&D calibration.

This is not an agent and makes no product claim. It executes the R&D-selected USE_EXISTING move:
reconstruct the already-defined R** liability/action signatures, then measure what happens to the
player-relative Stockfish evaluation over the next own decision cycles. It also scans a small fixed
set of coarse contexts for possible owner strengths vs the committed same-rating population table.

Outputs one JSON artifact for R&D to interpret. Any sequence result from TEST is a temporal holdout
for the post-hoc VALIDATE persistent/resolution localization, but this script remains observational:
resolved vs unresolved is not randomized.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
L = ROOT / "external" / "lichess_app"
AN = L / "research" / "mechanism" / "analysis"
sys.path.insert(0, str(AN))

import rstarstar_provenance as m  # type: ignore  # noqa: E402

OWNER = L / "research/mechanism/data/decisions_erez281.parquet"
POP = L / "research/mechanism/data/decisions_population_2026-06.parquet"
SCORED = L / "research/mechanism/data/scored_erez281_sf171_d12_mpv3.jsonl.zst"
OUT = ROOT / "runtime" / "move_sequence_evidence.json"
K = 0.00368208


def wp(cp):
    x = np.asarray(cp, dtype=float)
    x = np.clip(x, -3000, 3000)
    return 1.0 / (1.0 + np.exp(-K * x))


def add_future(all_rows: pd.DataFrame) -> pd.DataFrame:
    d = all_rows.sort_values(["game_id", "ply"]).copy()
    g = d.groupby("game_id", sort=False)
    for k in (1, 2, 3):
        d[f"future{k}_eval_before_cp"] = g["eval_before_cp"].shift(-k)
        d[f"future{k}_ply"] = g["ply"].shift(-k)
    d["wp_now"] = wp(d["eval_before_cp"])
    d["wp_after_move"] = wp(d["y_eval_after_cp"])
    for k in (1, 2, 3):
        d[f"wp_future{k}"] = wp(d[f"future{k}_eval_before_cp"])
        d[f"dwp_future{k}"] = d[f"wp_future{k}"] - d["wp_now"]
    return d


def summarize(d: pd.DataFrame) -> dict:
    out = {"n": int(len(d)), "games": int(d.game_id.nunique()) if len(d) else 0}
    if not len(d):
        return out
    for c in ["wp_now", "wp_after_move", "wp_future1", "wp_future2", "wp_future3",
              "dwp_future1", "dwp_future2", "dwp_future3"]:
        s = pd.to_numeric(d[c], errors="coerce").dropna()
        out[c] = {
            "n": int(len(s)),
            "mean": float(s.mean()) if len(s) else None,
            "median": float(s.median()) if len(s) else None,
        }
    out["hung_material_rate"] = float(d[m.TARGET].mean()) if m.TARGET in d else None
    out["tactical_rate"] = float(d["cls_tactical"].mean()) if "cls_tactical" in d else None
    out["accurate_rate"] = float(d["y_accurate"].mean()) if "y_accurate" in d else None
    return out


def contrast(frame: pd.DataFrame) -> dict:
    p = frame[frame.provenance_profile.eq("PERSISTENT")].copy()
    resolved = p[p.current_move_unresolved.eq(0)]
    unresolved = p[p.current_move_unresolved.eq(1)]
    out = {"persistent_resolved": summarize(resolved), "persistent_unresolved": summarize(unresolved)}
    diffs = {}
    for k in (1, 2, 3):
        c = f"dwp_future{k}"
        a = pd.to_numeric(resolved[c], errors="coerce").dropna()
        b = pd.to_numeric(unresolved[c], errors="coerce").dropna()
        diffs[f"resolved_minus_unresolved_future{k}_mean_dwp"] = (
            float(a.mean() - b.mean()) if len(a) and len(b) else None
        )
        diffs[f"resolved_minus_unresolved_future{k}_median_dwp"] = (
            float(a.median() - b.median()) if len(a) and len(b) else None
        )
    out["contrasts"] = diffs
    return out


def strength_scan(owner: pd.DataFrame, pop: pd.DataFrame) -> dict:
    # Fixed, predeclared coarse contexts only. These are candidate descriptions, not discovery search.
    dimensions = ["phase", "standing", "color", "speed"]
    rows = []
    for dim in dimensions:
        if dim not in owner or dim not in pop:
            continue
        values = sorted(set(owner[dim].dropna().astype(str)) & set(pop[dim].dropna().astype(str)))
        for val in values:
            o = owner[owner[dim].astype(str).eq(val)]
            q = pop[pop[dim].astype(str).eq(val)]
            if len(o) < 100 or len(q) < 300:
                continue
            oa = float(o["y_accurate"].mean())
            pa = float(q["y_accurate"].mean())
            rows.append({"context": f"{dim}={val}", "owner_n": int(len(o)), "population_n": int(len(q)),
                         "owner_accurate": oa, "population_accurate": pa, "gap": oa-pa})
    rows.sort(key=lambda x: x["gap"], reverse=True)
    return {"top_candidate_strengths": rows[:5], "top_candidate_weaknesses": list(reversed(rows[-5:]))}


def main():
    raw = pd.read_parquet(OWNER)
    raw_future = add_future(raw)

    design = m.vocab.DESIGN
    elig = m.eligible(m.load_decisions(str(OWNER)))
    split = m.chronological_split(elig, design["derive_frac"], design["validate_frac"])
    target = split[(split.speed == "blitz") & split.split.isin(["VALIDATE", "TEST"])].copy()
    target = target[m.rstarstar_mask(target)].copy()

    wanted = set(zip(target.game_id.astype(str), target.ply.astype(int)))
    probes = m.reconstruct(str(SCORED), wanted)
    target = m.add_probe(target, probes)

    future_cols = ["game_id", "ply", "wp_now", "wp_after_move", "wp_future1", "wp_future2", "wp_future3",
                   "dwp_future1", "dwp_future2", "dwp_future3"]
    target = target.merge(raw_future[future_cols], on=["game_id", "ply"], how="left", validate="one_to_one")

    frames = {}
    for name in ("VALIDATE", "TEST"):
        frames[name] = contrast(target[target.split.eq(name)])

    # A fixed coarse owner-vs-population scan on all eligible blitz rows. Population comparison is
    # descriptive; it does not establish a personal causal mechanism.
    owner_e = m.eligible(m.load_decisions(str(OWNER)))
    pop_e = m.eligible(m.load_decisions(str(POP), corpus=None))
    if "corpus" in pop_e:
        pop_e = pop_e[pop_e.corpus != "erez281"]
    owner_b = owner_e[owner_e.speed.eq("blitz")]
    pop_b = pop_e[pop_e.speed.eq("blitz")]

    out = {
        "status": "DETERMINISTIC_OBSERVATIONAL_EVIDENCE_FOR_RND",
        "owner_rows": int(len(raw)),
        "owner_games": int(raw.game_id.nunique()),
        "rstarstar_validate_test_rows": int(len(target)),
        "definition": {
            "region": m.RSTARSTAR,
            "resolved": "provenance_profile=PERSISTENT and current_move_unresolved=0",
            "unresolved": "provenance_profile=PERSISTENT and current_move_unresolved=1",
            "future1": "player's next own decision, after one opponent reply",
            "future2": "player's second subsequent own decision",
            "future3": "player's third subsequent own decision",
            "metric": "player-relative Stockfish win probability from eval_before_cp; descriptive, not causal"
        },
        "sequence_frames": frames,
        "coarse_owner_vs_population": strength_scan(owner_b, pop_b),
        "claim_boundary": [
            "VALIDATE persistent/resolution localization was post-hoc; TEST direction can serve as a later temporal check but actions are not randomized.",
            "A future-evaluation gap after resolved vs unresolved does not prove that spending a tempo caused the difference.",
            "Coarse owner-vs-population contexts are candidate strengths/weaknesses only and must not replace a more specific mechanism without further discrimination."
        ]
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
