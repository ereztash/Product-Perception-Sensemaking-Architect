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
OUT = Path('runtime/framework_fit_results_v2.json')

FRAMEWORKS = {
    'CCTO': {
        'primitives': ['checks', 'captures', 'optimize_quiet'],
        'manual_burden': 4.0,
        'unscored': ['threat-generation'],
    },
    'CCT_BOTH_WAYS_BLUNDER': {
        'primitives': ['checks', 'captures', 'urgent_safety', 'blunder_check'],
        'manual_burden': 4.5,
        'unscored': ['full opponent CCT after each candidate'],
    },
    'AWARENESS_SAFETY': {
        'primitives': ['what_changed', 'urgent_safety', 'loose_scan'],
        'manual_burden': 3.0,
        'unscored': [],
    },
    'PROPHYLAXIS_FIRST': {
        'primitives': ['what_changed', 'urgent_safety', 'king_safety'],
        'manual_burden': 3.0,
        'unscored': ['long-horizon opponent plan'],
    },
    'CANDIDATE_PLUS_BLUNDER': {
        'primitives': ['candidate_compare', 'blunder_check'],
        'manual_burden': 3.5,
        'unscored': ['quality of human candidate generation'],
    },
    'CLOSURE_GATE': {
        'primitives': ['what_changed', 'persistent_closure', 'blunder_check'],
        'manual_burden': 3.0,
        'unscored': [],
    },
    'CCT_PLUS_CLOSURE': {
        'primitives': ['checks', 'captures', 'persistent_closure', 'blunder_check'],
        'manual_burden': 4.0,
        'unscored': ['threat-generation'],
    },
}

# Only selective, player-observable gates are eligible for personal compression.
SELECTIVE = [
    'what_changed', 'urgent_safety', 'loose_scan', 'persistent_closure',
    'checks', 'captures', 'big_opponent_error_reset', 'king_safety', 'recapture', 'optimize_quiet',
]


def b(s):
    return s.fillna(0).astype(float) > 0


def add_provenance(df: pd.DataFrame, scored: Path) -> pd.DataFrame:
    wanted = set(zip(df['game_id'].astype(str), df['ply'].astype(int)))
    feats = provenance.reconstruct(str(scored), wanted)
    keep = ['game_id', 'ply', 'provenance_profile', 'current_move_unresolved']
    feats = feats[keep].copy()
    feats['game_id'] = feats['game_id'].astype(str)
    out = df.copy(); out['game_id'] = out['game_id'].astype(str)
    out = out.merge(feats, on=['game_id', 'ply'], how='left', validate='one_to_one')
    if out['provenance_profile'].isna().any():
        raise RuntimeError('provenance merge missing rows')
    return out


def primitive_masks(df: pd.DataFrame):
    err = df['err'].astype(bool)
    cls = df['y_error_class'].fillna('')
    new_attack = b(df['new_attacks_on_own'])
    last_forcing = b(df['opp_last_check']) | b(df['opp_last_capture'])
    large_change = df['eval_swing_last_move'].abs().fillna(0) >= 100
    what_changed = new_attack | last_forcing | large_change

    loose = (df['own_hanging_piece_count'].fillna(0) > 0) | (df['own_overloaded_piece_count'].fillna(0) > 0)
    urgent = loose | new_attack | b(df['in_check']) | (df['own_king_ring_enemy_attacks'].fillna(0) >= 3)
    persistent = df['provenance_profile'].eq('PERSISTENT')
    persistent_failed = persistent & (df['current_move_unresolved'].fillna(0).astype(int) == 1)
    checks = df['n_checks'].fillna(0) > 0
    captures = (df['n_good_captures'].fillna(0) > 0) | b(df['recapture_available'])
    big_opp_error = df['opp_last_wp_loss'].fillna(0) >= 0.10
    king = b(df['in_check']) | (df['own_king_ring_enemy_attacks'].fillna(0) >= 3)
    recapture = b(df['recapture_available'])
    quiet = (df['n_checks'].fillna(0) == 0) & (df['n_good_captures'].fillna(0) == 0) & b(df['top_all_quiet'])
    always = pd.Series(True, index=df.index)

    loose_classes = cls.isin(['hung_material', 'allowed_check_tactic', 'quiet_error'])
    safety_classes = cls.isin(['hung_material', 'allowed_check_tactic', 'bad_capture'])

    return {
        'what_changed': {'trigger': what_changed, 'addressed': err & what_changed},
        'urgent_safety': {'trigger': urgent, 'addressed': err & urgent & loose_classes},
        'loose_scan': {'trigger': loose, 'addressed': err & loose & cls.isin(['hung_material', 'allowed_check_tactic'])},
        'persistent_closure': {'trigger': persistent, 'addressed': err & persistent_failed},
        'checks': {'trigger': checks, 'addressed': err & checks & b(df['best_check']) & ~b(df['y_played_check'])},
        'captures': {'trigger': captures, 'addressed': err & captures & b(df['best_capture']) & ~b(df['y_played_capture'])},
        'big_opponent_error_reset': {'trigger': big_opp_error, 'addressed': err & big_opp_error},
        'king_safety': {'trigger': king, 'addressed': err & king & loose_classes},
        'recapture': {'trigger': recapture, 'addressed': err & recapture & b(df['best_is_recapture']) & ~b(df['y_played_capture'])},
        'optimize_quiet': {'trigger': quiet, 'addressed': err & quiet & cls.eq('quiet_error')},
        'candidate_compare': {'trigger': always, 'addressed': err & ~b(df['y_played_in_top3']) & (df['n_lines'].fillna(0) >= 3)},
        'blunder_check': {'trigger': always, 'addressed': err & safety_classes},
    }


def stats(df, pm):
    total_err = max(1, int(df.err.sum()))
    total_loss = float(df.loc[df.err == 1, 'y_wp_loss'].sum())
    total_b10 = max(1, int(df.blunder10.sum()))
    out = {}
    for name, m in pm.items():
        tr = m['trigger'].astype(bool); ad = m['addressed'].astype(bool)
        nt = int(tr.sum()); nf = int((~tr).sum())
        er_t = float(df.loc[tr, 'err'].mean()) if nt else None
        er_f = float(df.loc[~tr, 'err'].mean()) if nf else None
        loss = float(df.loc[ad, 'y_wp_loss'].sum())
        out[name] = {
            'trigger_rate': float(tr.mean()), 'trigger_n': nt,
            'error_rate_triggered': er_t, 'error_rate_untriggered': er_f,
            'risk_lift': (er_t-er_f) if er_t is not None and er_f is not None else None,
            'addressed_error_n': int(ad.sum()),
            'error_coverage': float(ad.sum()/total_err),
            'loss_coverage': float(loss/total_loss) if total_loss else 0.0,
            'blunder10_coverage': float((ad & (df.blunder10 == 1)).sum()/total_b10),
            'loss_coverage_per_trigger_rate': float((loss/total_loss)/max(float(tr.mean()), 1e-9)) if total_loss else 0.0,
        }
        if name == 'persistent_closure' and nt:
            unresolved = df.loc[tr, 'current_move_unresolved'].fillna(0).astype(int) == 1
            out[name]['unresolved_rate'] = float(unresolved.mean())
    return out


def fstats(df, pm):
    total_err = max(1, int(df.err.sum())); total_loss = float(df.loc[df.err == 1,'y_wp_loss'].sum()); total_b10=max(1,int(df.blunder10.sum()))
    out = {}
    for name, spec in FRAMEWORKS.items():
        ad = pd.Series(False,index=df.index); ops=np.zeros(len(df))
        for p in spec['primitives']:
            ad |= pm[p]['addressed'].astype(bool); ops += pm[p]['trigger'].astype(float).to_numpy()
        lc=float(df.loc[ad,'y_wp_loss'].sum()/total_loss) if total_loss else 0.0
        out[name]={
            'primitives':spec['primitives'], 'manual_burden':spec['manual_burden'], 'unscored':spec['unscored'],
            'error_coverage':float(ad.sum()/total_err), 'loss_coverage':lc,
            'blunder10_coverage':float((ad & (df.blunder10==1)).sum()/total_b10),
            'conditional_trigger_ops_per_move':float(ops.mean()),
            'loss_coverage_per_manual_burden':lc/spec['manual_burden'],
        }
    return out


def subset_metrics(df, pm, subset):
    total_loss=float(df.loc[df.err==1,'y_wp_loss'].sum()); total_err=max(1,int(df.err.sum())); total_b10=max(1,int(df.blunder10.sum()))
    ad=pd.Series(False,index=df.index); ops=np.zeros(len(df))
    for p in subset:
        ad |= pm[p]['addressed'].astype(bool); ops += pm[p]['trigger'].astype(float).to_numpy()
    lc=float(df.loc[ad,'y_wp_loss'].sum()/total_loss) if total_loss else 0.0
    return {'primitives':list(subset),'loss_coverage':lc,'error_coverage':float(ad.sum()/total_err),'blunder10_coverage':float((ad & (df.blunder10==1)).sum()/total_b10),'trigger_ops_per_move':float(ops.mean()),'efficiency':lc/max(float(ops.mean()),1e-9)}


def compression_frontier(val, pm):
    rows=[]
    for k in (1,2,3):
        for sub in itertools.combinations(SELECTIVE,k): rows.append(subset_metrics(val,pm,sub))
    # Non-dominated on lower trigger load + higher loss coverage.
    frontier=[]
    for x in sorted(rows,key=lambda z:(z['trigger_ops_per_move'],-z['loss_coverage'])):
        if not frontier or x['loss_coverage'] > max(y['loss_coverage'] for y in frontier)+1e-12: frontier.append(x)
    # Practical choice: at most 0.85 conditional prompts per move, maximize loss coverage; within 3pp choose lower load.
    feasible=[x for x in rows if x['trigger_ops_per_move']<=0.85]
    if not feasible: feasible=rows
    best=max(x['loss_coverage'] for x in feasible)
    near=[x for x in feasible if x['loss_coverage']>=best-0.03]
    chosen=sorted(near,key=lambda x:(x['trigger_ops_per_move'],len(x['primitives']),-x['loss_coverage']))[0]
    return chosen,frontier[:25]


def main():
    owner=chronological_split(eligible(load_decisions(str(OWNER_PATH))),0.60,0.20)
    pop=eligible(load_decisions(str(POP_PATH),corpus=None))
    owner=add_provenance(owner,OWNER_SCORED); pop=add_provenance(pop,POP_SCORED)
    val=owner[owner.split=='VALIDATE'].copy(); test=owner[owner.split=='TEST'].copy()
    mv=primitive_masks(val); mt=primitive_masks(test); mp=primitive_masks(pop)
    sv,st,sp=stats(val,mv),stats(test,mt),stats(pop,mp)
    fv,ft=fstats(val,mv),fstats(test,mt)

    # Base framework selected ONLY on VALIDATE by coverage per fixed manual burden.
    base_name=max(fv,key=lambda k:(fv[k]['loss_coverage_per_manual_burden'],fv[k]['loss_coverage']))

    chosen,frontier=compression_frontier(val,mv)
    chosen_test=subset_metrics(test,mt,chosen['primitives'])

    # Incremental personal gates beyond the selected base, evaluated without using TEST for selection.
    base_addr=pd.Series(False,index=val.index)
    for p in FRAMEWORKS[base_name]['primitives']: base_addr |= mv[p]['addressed'].astype(bool)
    total_loss=float(val.loc[val.err==1,'y_wp_loss'].sum())
    incremental=[]
    for p in SELECTIVE:
        if p in FRAMEWORKS[base_name]['primitives']: continue
        extra=mv[p]['addressed'].astype(bool) & ~base_addr
        inc=float(val.loc[extra,'y_wp_loss'].sum()/total_loss) if total_loss else 0.0
        incremental.append({'primitive':p,'validate_incremental_loss_coverage':inc,'validate_trigger_rate':sv[p]['trigger_rate'],'validate_risk_lift':sv[p]['risk_lift']})
    incremental=sorted(incremental,key=lambda x:(-x['validate_incremental_loss_coverage'],x['validate_trigger_rate']))

    comparison={}
    for p in SELECTIVE:
        comparison[p]={
            'owner_test_trigger_rate':st[p]['trigger_rate'],'population_trigger_rate':sp[p]['trigger_rate'],
            'owner_test_error_rate_triggered':st[p]['error_rate_triggered'],'population_error_rate_triggered':sp[p]['error_rate_triggered'],
            'owner_minus_population_error_rate':(st[p]['error_rate_triggered']-sp[p]['error_rate_triggered']) if st[p]['error_rate_triggered'] is not None and sp[p]['error_rate_triggered'] is not None else None,
            'owner_test_risk_lift':st[p]['risk_lift'],'population_risk_lift':sp[p]['risk_lift'],
        }
        if p=='persistent_closure':
            comparison[p]['owner_unresolved_rate']=st[p].get('unresolved_rate'); comparison[p]['population_unresolved_rate']=sp[p].get('unresolved_rate')

    ranking=[]
    for name in fv:
        ranking.append({'framework':name,'validate_efficiency':fv[name]['loss_coverage_per_manual_burden'],'validate_loss_coverage':fv[name]['loss_coverage'],'test_loss_coverage':ft[name]['loss_coverage'],'test_error_coverage':ft[name]['error_coverage'],'test_blunder10_coverage':ft[name]['blunder10_coverage'],'manual_burden':ft[name]['manual_burden'],'delta_test_minus_validate':ft[name]['loss_coverage']-fv[name]['loss_coverage']})
    ranking=sorted(ranking,key=lambda x:(-x['validate_efficiency'],-x['validate_loss_coverage']))

    result={
        'status':'DISCRIMINATION_AWARE_OBSERVATIONAL_FRAMEWORK_FIT_NOT_CAUSAL',
        'instrument':{'owner_eligible_rows':int(len(owner)),'owner_games':int(owner.game_id.nunique()),'validate_rows':int(len(val)),'validate_games':int(val.game_id.nunique()),'test_rows':int(len(test)),'test_games':int(test.game_id.nunique()),'population_rows':int(len(pop)),'population_games':int(pop.game_id.nunique()),'split':'60/20/20 chronological by game'},
        'changes_from_v1':['opponent error reset now requires >=10 percentage-point win-probability loss, not merely crossing the 2.76pp accuracy threshold','opponent/safety cue is narrowed to observable urgent danger instead of any attacked piece','selection reports a base framework separately from a low-frequency personal gate bundle','risk lift and trigger rate are reported so broad near-always-on masks cannot masquerade as discrimination'],
        'primitive_validate':sv,'primitive_test':st,'primitive_population':sp,'test_vs_population':comparison,
        'framework_validate':fv,'framework_test':ft,'framework_ranking_selected_on_validate':ranking,
        'base_selected_on_validate':{'framework':base_name,'validate':fv[base_name],'test':ft[base_name]},
        'personal_compression':{'rule':'search 1-3 selective observable gates on VALIDATE only; require <=0.85 conditional trigger-ops/move when possible; maximize loss coverage, then choose lowest load within 3pp of best','chosen_validate':chosen,'chosen_test':chosen_test,'pareto_frontier_validate':frontier},
        'incremental_gates_over_base_validate':incremental,
        'claim_boundary':['Addressability is not prevention. The experiment asks which checklist operations point at errors that actually occurred, not whether asking them would have prevented the errors.','Threat generation and quality of human candidate generation are not directly observed, so CCTO and candidate frameworks are partially measured.','The base framework and personal compressed gates are selected without TEST; TEST is used only as a temporal check.','A prospective intervention is required before claiming rating or error reduction.']
    }
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(json.dumps({'instrument':result['instrument'],'base':result['base_selected_on_validate'],'personal_compression':result['personal_compression'],'ranking':ranking,'incremental_top':incremental[:6],'key_comparison':{p:comparison[p] for p in ['persistent_closure','what_changed','urgent_safety','big_opponent_error_reset','checks','captures']}},indent=2,ensure_ascii=False))

if __name__=='__main__': main()
