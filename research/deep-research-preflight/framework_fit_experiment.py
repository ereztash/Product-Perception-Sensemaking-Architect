from __future__ import annotations

import itertools
import json
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path('external/lichess_app/research/mechanism')
ANALYSIS = ROOT / 'analysis'
PIPELINE = ROOT / 'pipeline'
sys.path.insert(0, str(ANALYSIS))
sys.path.insert(0, str(PIPELINE))

from common import load_decisions, eligible, chronological_split  # type: ignore
import rstarstar_provenance as provenance  # type: ignore

OWNER_PATH = ROOT / 'data/decisions_erez281.parquet'
POP_PATH = ROOT / 'data/decisions_population_2026-06.parquet'
OWNER_SCORED = ROOT / 'data/scored_erez281_sf171_d12_mpv3.jsonl.zst'
POP_SCORED = ROOT / 'data/scored_population_sf171_d12_mpv3.jsonl.zst'
OUT = Path('runtime/framework_fit_results.json')

# Frameworks are bundles of attention operations, not causal claims.
# manual_burden is a transparent design estimate: number/weight of mental passes a player must run
# if the framework is recited on every move. It is NOT learned from outcome data.
FRAMEWORKS = {
    'CCTO': {
        'primitives': ['checks', 'captures', 'optimize_quiet'],
        'manual_burden': 4.0,
        'unscored_components': ['threats'],
        'note': 'Checks, Captures, Threats, Optimization; threats are not directly encoded in the frozen table, so measured coverage is a lower bound.',
    },
    'CCT_BOTH_WAYS_BLUNDER': {
        'primitives': ['checks', 'captures', 'opponent_intent', 'blunder_check'],
        'manual_burden': 4.5,
        'unscored_components': ['full opponent CCT after each candidate'],
        'note': 'Forcing-move scan in both directions plus final blunder check.',
    },
    'AWARENESS_WOW_STYLE': {
        'primitives': ['what_changed', 'opponent_intent', 'loose_scan'],
        'manual_burden': 3.0,
        'unscored_components': [],
        'note': 'A generic what-changed / opponent-intent / loose-or-weak scan. This is a WOW-style bundle, not a claim that WOW has one canonical public definition.',
    },
    'PROPHYLAXIS_FIRST': {
        'primitives': ['what_changed', 'opponent_intent', 'king_safety'],
        'manual_burden': 3.0,
        'unscored_components': ['long-horizon opponent plan'],
        'note': 'Update after the opponent move, identify their immediate resources, then prevent before improving.',
    },
    'CANDIDATE_PLUS_BLUNDER': {
        'primitives': ['candidate_compare', 'blunder_check'],
        'manual_burden': 3.5,
        'unscored_components': ['quality of human candidate generation'],
        'note': 'Generate/compare candidates, then run a final safety check.',
    },
    'CLOSURE_GATE': {
        'primitives': ['what_changed', 'persistent_closure', 'blunder_check'],
        'manual_burden': 3.0,
        'unscored_components': [],
        'note': 'Update the board, explicitly close a liability that survived a prior decision cycle, then sanity-check the intended move.',
    },
    'CCT_PLUS_CLOSURE': {
        'primitives': ['checks', 'captures', 'persistent_closure', 'blunder_check'],
        'manual_burden': 4.0,
        'unscored_components': ['threat generation'],
        'note': 'CCT forcing scan with a personal closure gate before commit.',
    },
}

CORE_FOR_PERSONAL = [
    'what_changed', 'loose_scan', 'persistent_closure', 'checks', 'captures',
    'opponent_intent', 'opponent_error_reset', 'king_safety', 'recapture', 'optimize_quiet',
]


def b(s):
    return s.fillna(0).astype(float) > 0


def add_provenance(df: pd.DataFrame, scored: Path) -> pd.DataFrame:
    wanted = set(zip(df['game_id'].astype(str), df['ply'].astype(int)))
    feats = provenance.reconstruct(str(scored), wanted)
    keep = [
        'game_id', 'ply', 'provenance_profile', 'current_move_unresolved',
        'current_liability_unresolved_n', 'any_overloaded_after',
    ]
    feats = feats[keep].copy()
    feats['game_id'] = feats['game_id'].astype(str)
    out = df.copy()
    out['game_id'] = out['game_id'].astype(str)
    out = out.merge(feats, on=['game_id', 'ply'], how='left', validate='one_to_one')
    if out['provenance_profile'].isna().any():
        raise RuntimeError('provenance merge missing rows')
    return out


def masks(df: pd.DataFrame) -> dict[str, dict[str, pd.Series]]:
    idx = df.index
    err = df['err'].astype(bool)
    cls = df['y_error_class'].fillna('')

    new_attack = b(df['new_attacks_on_own'])
    last_forcing = b(df['opp_last_check']) | b(df['opp_last_capture'])
    eval_change = df['eval_swing_last_move'].abs().fillna(0) >= 100
    what_changed_trigger = new_attack | last_forcing | eval_change

    loose_trigger = (
        (df['own_hanging_piece_count'].fillna(0) > 0)
        | (df['own_overloaded_piece_count'].fillna(0) > 0)
        | (df['own_pinned_count'].fillna(0) > 0)
    )
    opponent_intent_trigger = (
        new_attack
        | (df['own_attacked_piece_count'].fillna(0) > 0)
        | (df['own_king_ring_enemy_attacks'].fillna(0) >= 2)
    )
    persistent_trigger = df['provenance_profile'].isin(['PERSISTENT'])
    persistent_failed = persistent_trigger & (df['current_move_unresolved'].fillna(0).astype(int) == 1)

    checks_trigger = df['n_checks'].fillna(0) > 0
    captures_trigger = (df['n_good_captures'].fillna(0) > 0) | b(df['recapture_available'])
    recapture_trigger = b(df['recapture_available'])
    king_trigger = b(df['in_check']) | (df['own_king_ring_enemy_attacks'].fillna(0) >= 2)
    opp_error_trigger = b(df['opp_last_blunder'])
    quiet_trigger = (
        (df['n_checks'].fillna(0) == 0)
        & (df['n_good_captures'].fillna(0) == 0)
        & b(df['top_all_quiet'])
    )
    always = pd.Series(True, index=idx)

    tactical_safety_classes = cls.isin(['hung_material', 'allowed_check_tactic', 'bad_capture'])
    loose_classes = cls.isin(['hung_material', 'allowed_check_tactic', 'quiet_error'])

    return {
        'what_changed': {
            'trigger': what_changed_trigger,
            'addressed': err & what_changed_trigger,
        },
        'loose_scan': {
            'trigger': loose_trigger,
            'addressed': err & loose_trigger & loose_classes,
        },
        'persistent_closure': {
            'trigger': persistent_trigger,
            'addressed': err & persistent_failed,
        },
        'checks': {
            'trigger': checks_trigger,
            'addressed': err & checks_trigger & b(df['best_check']) & ~b(df['y_played_check']),
        },
        'captures': {
            'trigger': captures_trigger,
            'addressed': err & captures_trigger & b(df['best_capture']) & ~b(df['y_played_capture']),
        },
        'opponent_intent': {
            'trigger': opponent_intent_trigger,
            'addressed': err & opponent_intent_trigger & loose_classes,
        },
        'candidate_compare': {
            'trigger': always,
            'addressed': err & ~b(df['y_played_in_top3']) & (df['n_lines'].fillna(0) >= 3),
        },
        'blunder_check': {
            'trigger': always,
            'addressed': err & tactical_safety_classes,
        },
        'opponent_error_reset': {
            'trigger': opp_error_trigger,
            'addressed': err & opp_error_trigger,
        },
        'optimize_quiet': {
            'trigger': quiet_trigger,
            'addressed': err & quiet_trigger & (cls == 'quiet_error'),
        },
        'king_safety': {
            'trigger': king_trigger,
            'addressed': err & king_trigger & cls.isin(['allowed_check_tactic', 'hung_material', 'quiet_error']),
        },
        'recapture': {
            'trigger': recapture_trigger,
            'addressed': err & recapture_trigger & b(df['best_is_recapture']) & ~b(df['y_played_capture']),
        },
    }


def safe_rate(mask: pd.Series) -> float:
    return float(mask.mean()) if len(mask) else math.nan


def primitive_stats(df: pd.DataFrame, pm: dict[str, dict[str, pd.Series]]) -> dict:
    total_err = max(1, int(df['err'].sum()))
    total_loss = float(df.loc[df['err'] == 1, 'y_wp_loss'].sum())
    total_b10 = max(1, int(df['blunder10'].sum()))
    out = {}
    for name, m in pm.items():
        trig = m['trigger'].astype(bool)
        addr = m['addressed'].astype(bool)
        trig_n = int(trig.sum())
        addressed_loss = float(df.loc[addr, 'y_wp_loss'].sum())
        out[name] = {
            'trigger_rate': safe_rate(trig),
            'trigger_n': trig_n,
            'error_rate_when_triggered': float(df.loc[trig, 'err'].mean()) if trig_n else None,
            'mean_wp_loss_when_triggered': float(df.loc[trig, 'y_wp_loss'].mean()) if trig_n else None,
            'addressed_error_n': int(addr.sum()),
            'error_coverage': float(addr.sum() / total_err),
            'loss_coverage': float(addressed_loss / total_loss) if total_loss > 0 else 0.0,
            'blunder10_coverage': float((addr & (df['blunder10'] == 1)).sum() / total_b10),
        }
        if name == 'persistent_closure' and trig_n:
            out[name]['unresolved_rate_when_triggered'] = float(
                (df.loc[trig, 'current_move_unresolved'].fillna(0).astype(int) == 1).mean()
            )
            res = trig & (df['current_move_unresolved'].fillna(0).astype(int) == 0)
            unr = trig & (df['current_move_unresolved'].fillna(0).astype(int) == 1)
            out[name]['error_rate_resolved'] = float(df.loc[res, 'err'].mean()) if res.any() else None
            out[name]['error_rate_unresolved'] = float(df.loc[unr, 'err'].mean()) if unr.any() else None
    return out


def framework_stats(df: pd.DataFrame, pm: dict[str, dict[str, pd.Series]], frameworks: dict) -> dict:
    total_err = max(1, int(df['err'].sum()))
    total_loss = float(df.loc[df['err'] == 1, 'y_wp_loss'].sum())
    total_b10 = max(1, int(df['blunder10'].sum()))
    out = {}
    for name, spec in frameworks.items():
        addr = pd.Series(False, index=df.index)
        trigger_ops = np.zeros(len(df), dtype=float)
        for p in spec['primitives']:
            addr |= pm[p]['addressed'].astype(bool)
            trigger_ops += pm[p]['trigger'].astype(float).to_numpy()
        addressed_loss = float(df.loc[addr, 'y_wp_loss'].sum())
        out[name] = {
            'primitives': spec['primitives'],
            'manual_burden': spec['manual_burden'],
            'unscored_components': spec['unscored_components'],
            'note': spec['note'],
            'error_coverage': float(addr.sum() / total_err),
            'loss_coverage': float(addressed_loss / total_loss) if total_loss > 0 else 0.0,
            'blunder10_coverage': float((addr & (df['blunder10'] == 1)).sum() / total_b10),
            'conditional_trigger_ops_per_move': float(trigger_ops.mean()),
            'loss_coverage_per_manual_burden': float((addressed_loss / total_loss) / spec['manual_burden']) if total_loss > 0 else 0.0,
        }
    return out


def derive_personal(validate: pd.DataFrame, pm: dict[str, dict[str, pd.Series]]) -> dict:
    total_loss = float(validate.loc[validate['err'] == 1, 'y_wp_loss'].sum())
    candidates = []
    for k in (1, 2, 3):
        for subset in itertools.combinations(CORE_FOR_PERSONAL, k):
            addr = pd.Series(False, index=validate.index)
            ops = np.zeros(len(validate), dtype=float)
            for p in subset:
                addr |= pm[p]['addressed'].astype(bool)
                ops += pm[p]['trigger'].astype(float).to_numpy()
            loss_cov = float(validate.loc[addr, 'y_wp_loss'].sum() / total_loss) if total_loss > 0 else 0.0
            candidates.append({
                'primitives': list(subset),
                'k': k,
                'loss_coverage': loss_cov,
                'trigger_ops_per_move': float(ops.mean()),
            })
    max_cov = max(x['loss_coverage'] for x in candidates)
    near_best = [x for x in candidates if x['loss_coverage'] >= max_cov - 0.05]
    # Smallest conditional attention load among solutions within five points of best coverage;
    # ties go to fewer primitives, then higher coverage.
    chosen = sorted(near_best, key=lambda x: (x['trigger_ops_per_move'], x['k'], -x['loss_coverage']))[0]
    frontier = []
    for x in sorted(candidates, key=lambda z: (z['trigger_ops_per_move'], -z['loss_coverage'])):
        if not frontier or x['loss_coverage'] > max(y['loss_coverage'] for y in frontier) + 1e-12:
            frontier.append(x)
    return {'chosen': chosen, 'max_validate_loss_coverage': max_cov, 'pareto_frontier': frontier[:20]}


def eval_subset(df: pd.DataFrame, pm: dict, subset: list[str]) -> dict:
    total_err = max(1, int(df['err'].sum()))
    total_loss = float(df.loc[df['err'] == 1, 'y_wp_loss'].sum())
    total_b10 = max(1, int(df['blunder10'].sum()))
    addr = pd.Series(False, index=df.index)
    ops = np.zeros(len(df), dtype=float)
    for p in subset:
        addr |= pm[p]['addressed'].astype(bool)
        ops += pm[p]['trigger'].astype(float).to_numpy()
    return {
        'primitives': subset,
        'error_coverage': float(addr.sum()/total_err),
        'loss_coverage': float(df.loc[addr, 'y_wp_loss'].sum()/total_loss) if total_loss > 0 else 0.0,
        'blunder10_coverage': float((addr & (df['blunder10'] == 1)).sum()/total_b10),
        'conditional_trigger_ops_per_move': float(ops.mean()),
    }


def population_compare(owner_test_stats: dict, pop_stats: dict) -> dict:
    out = {}
    for p in owner_test_stats:
        o, q = owner_test_stats[p], pop_stats[p]
        oe, pe = o.get('error_rate_when_triggered'), q.get('error_rate_when_triggered')
        row = {
            'owner_trigger_rate': o.get('trigger_rate'),
            'population_trigger_rate': q.get('trigger_rate'),
            'owner_error_rate_when_triggered': oe,
            'population_error_rate_when_triggered': pe,
            'owner_minus_population_error_rate': (oe - pe) if oe is not None and pe is not None else None,
        }
        if p == 'persistent_closure':
            ou = o.get('unresolved_rate_when_triggered'); pu = q.get('unresolved_rate_when_triggered')
            row.update({
                'owner_unresolved_rate': ou,
                'population_unresolved_rate': pu,
                'owner_minus_population_unresolved_rate': (ou-pu) if ou is not None and pu is not None else None,
            })
        out[p] = row
    return out


def main():
    owner = eligible(load_decisions(str(OWNER_PATH)))
    owner = chronological_split(owner, 0.60, 0.20)
    pop = eligible(load_decisions(str(POP_PATH), corpus=None))

    owner = add_provenance(owner, OWNER_SCORED)
    pop = add_provenance(pop, POP_SCORED)

    val = owner[owner['split'] == 'VALIDATE'].copy()
    test = owner[owner['split'] == 'TEST'].copy()

    pm_val = masks(val); pm_test = masks(test); pm_pop = masks(pop)
    prim_val = primitive_stats(val, pm_val)
    prim_test = primitive_stats(test, pm_test)
    prim_pop = primitive_stats(pop, pm_pop)

    base_val = framework_stats(val, pm_val, FRAMEWORKS)
    base_test = framework_stats(test, pm_test, FRAMEWORKS)

    personal = derive_personal(val, pm_val)
    personal_val = eval_subset(val, pm_val, personal['chosen']['primitives'])
    personal_test = eval_subset(test, pm_test, personal['chosen']['primitives'])

    ranked = []
    for name, t in base_test.items():
        v = base_val[name]
        ranked.append({
            'framework': name,
            'validate_loss_coverage': v['loss_coverage'],
            'test_loss_coverage': t['loss_coverage'],
            'test_error_coverage': t['error_coverage'],
            'test_blunder10_coverage': t['blunder10_coverage'],
            'manual_burden': t['manual_burden'],
            'test_loss_coverage_per_manual_burden': t['loss_coverage_per_manual_burden'],
            'validate_to_test_delta': t['loss_coverage'] - v['loss_coverage'],
        })
    ranked.append({
        'framework': 'PERSONAL_DERIVED_VALIDATE_ONLY',
        'validate_loss_coverage': personal_val['loss_coverage'],
        'test_loss_coverage': personal_test['loss_coverage'],
        'test_error_coverage': personal_test['error_coverage'],
        'test_blunder10_coverage': personal_test['blunder10_coverage'],
        'manual_burden': len(personal['chosen']['primitives']),
        'test_loss_coverage_per_manual_burden': personal_test['loss_coverage']/max(1, len(personal['chosen']['primitives'])),
        'validate_to_test_delta': personal_test['loss_coverage']-personal_val['loss_coverage'],
    })
    ranked = sorted(ranked, key=lambda x: (-x['test_loss_coverage_per_manual_burden'], -x['test_loss_coverage']))

    result = {
        'status': 'OBSERVATIONAL_FRAMEWORK_FIT_NOT_CAUSAL',
        'instrument': {
            'owner_eligible_rows': int(len(owner)),
            'owner_games': int(owner.game_id.nunique()),
            'validate_rows': int(len(val)),
            'validate_games': int(val.game_id.nunique()),
            'test_rows': int(len(test)),
            'test_games': int(test.game_id.nunique()),
            'population_eligible_rows': int(len(pop)),
            'population_games': int(pop.game_id.nunique()),
            'split': 'chronological by game: 60% DERIVE / 20% VALIDATE / 20% TEST',
        },
        'measurement_definition': {
            'coverage': 'retrospective share of actual errors/loss occurring in states or error classes explicitly targeted by the framework primitives; this is addressability, NOT proven prevention',
            'loss_coverage': 'share of total Stockfish win-probability loss on erroneous decisions that falls inside addressable decisions',
            'conditional_trigger_ops_per_move': 'mean number of primitive cue masks active per decision; a data-side load proxy, distinct from manual mental burden',
            'manual_burden': 'design estimate fixed before scoring; not an empirical psychological measure',
        },
        'primitive_validate': prim_val,
        'primitive_test': prim_test,
        'primitive_population': prim_pop,
        'personalization_test_vs_population': population_compare(prim_test, prim_pop),
        'framework_validate': base_val,
        'framework_test': base_test,
        'personal_derived': {
            'selection_rule': 'On VALIDATE only, enumerate 1-3 observable/conditional primitives; find maximum loss coverage, then choose the lowest trigger-load subset within 5 percentage points of that maximum. TEST is not used in selection.',
            'selection': personal,
            'validate': personal_val,
            'test': personal_test,
        },
        'ranking_by_test_loss_coverage_per_manual_burden': ranked,
        'claim_boundary': [
            'This experiment can rank retrospective addressability and attention burden, not causal improvement.',
            'A framework component that is not encoded in the frozen trace (e.g. full human threat generation or candidate quality) is explicitly unscored, so some framework coverage is a lower bound.',
            'The personalized bundle is selected on VALIDATE and only then evaluated on TEST; a prospective intervention is still required to prove that asking the questions changes play.',
            'Population comparisons are coarse same-rating reference comparisons, not a fully matched causal baseline.',
        ],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False))

    compact = {
        'instrument': result['instrument'],
        'personal_selection': result['personal_derived']['selection']['chosen'],
        'personal_validate': personal_val,
        'personal_test': personal_test,
        'ranking': ranked,
        'key_personalization': {
            k: v for k, v in result['personalization_test_vs_population'].items()
            if k in ['persistent_closure', 'what_changed', 'opponent_intent', 'opponent_error_reset', 'loose_scan', 'checks', 'captures']
        },
    }
    print(json.dumps(compact, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()
