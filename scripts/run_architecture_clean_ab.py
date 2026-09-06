#!/usr/bin/env python3
"""Clean staged Architecture A/B: runner freeze before GOLD, then blind judge."""
from __future__ import annotations
import argparse, datetime as dt, hashlib, json, os, sys, time
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'runtime/calibration_loop'))
from openai_resource_adapter import post_response, extract_output_text, parse_json_object  # noqa:E402

CASES=ROOT/'eval/architecture-agent/HISTORICAL_CASES_V0.jsonl'
GOLD=ROOT/'eval/architecture-agent/HISTORICAL_GOLD_V0.jsonl'
RND=ROOT/'prompts/RND_AGENT_V0_2_CANDIDATE.md'
SCAFFOLD=ROOT/'prompts/SCAFFOLD_RESOURCE_V0_1.md'
ARCH=ROOT/'research/architecture-agent/ARCHITECTURE_DECISION_DISCRIMINATOR_V0.md'
MODEL=os.getenv('ARCH_BENCH_MODEL',os.getenv('OPENAI_MODEL','gpt-5.6-sol'))
JUDGE_MODEL=os.getenv('ARCH_BENCH_JUDGE_MODEL',MODEL)
EFFORT=os.getenv('ARCH_BENCH_REASONING_EFFORT','high')
JUDGE_EFFORT=os.getenv('ARCH_BENCH_JUDGE_EFFORT','high')

FAMILIES={
'ARCH-HIST-001':'COORDINATION_BOUNDARY','ARCH-HIST-002':'RUNTIME_DEPLOYMENT',
'ARCH-HIST-003':'STATE_AUTHORITY_LINEAGE','ARCH-HIST-004':'COORDINATION_BOUNDARY',
'ARCH-HIST-005':'COORDINATION_BOUNDARY','ARCH-HIST-006':'KNOWLEDGE_CODE_BOUNDARY',
'ARCH-HIST-007':'RUNTIME_DEPLOYMENT','ARCH-HIST-008':'KNOWLEDGE_CODE_BOUNDARY',
'ARCH-HIST-009':'SHARED_INFRASTRUCTURE','ARCH-HIST-010':'STATE_AUTHORITY_LINEAGE',
'ARCH-HIST-011':'STATE_AUTHORITY_LINEAGE','ARCH-HIST-012':'STATE_AUTHORITY_LINEAGE'}
RULE={'candidate_material_wins_min':2,'candidate_win_families_min':2,
      'candidate_wins_must_exceed_baseline_wins':True,'candidate_harm_max':1}
DIMS=['BOUNDARY_DELTA','AUTHORITY_DELTA','OPTION_DELTA','DISCRIMINATOR_DELTA','MIGRATION_DELTA','ANTI_BUILD_DELTA']

SERIAL='''This neutral benchmark serialization overrides any earlier output format. Return exactly one JSON object, no Markdown, with exactly these fields:\ndecision (string); purpose (string); observed_facts (string array); alternatives (1-3 objects, each exactly name, mechanism, main_benefit, main_cost); decision_relevant_considerations (string array); unresolved_uncertainties (string array); authority_needed (array using only OWNER, REPO, ENVIRONMENT, FIELD, RESEARCH); cheapest_next_check (string); bounded_next_move (string); reversal_condition (string); limitations (string array). Do not invent repository/runtime/field facts.'''
RND_SCOPE='''For this benchmark use the strongest current R&D scope: calibrate learning/evidence effort to uncertainty that can still change a consequential decision. R&D decides whether/how/how much to learn; it does not own structural architecture selection.'''
BASE='''You are the strongest CURRENT COMPOSED BASELINE. Apply R&D epistemic-effort discipline plus the External Reasoning Scaffold. Preserve authority ceilings, generate few plausible alternatives/failure modes, prefer the cheapest decision-changing check, do not privilege BUILD, and answer the live decision. You are not the Architecture Decision Discriminator and must not force architecture framing.'''
CAND='''You are the same CURRENT COMPOSED BASELINE plus Architecture Decision Discriminator v0. Apply the architecture contract only when it materially improves this case; do not force architecture vocabulary. Answer the live decision.'''
JUDGE='''You are a blind adjudicator. You receive a frozen case, historical resolution/provenance, and two independently frozen responses X/Y. You do not know which is baseline/candidate. Historical resolution is CONTEXT_NOT_ANSWER_KEY, not proof of optimality. Vocabulary, polish, or agreement with history are not wins. A win requires material improvement of the decision path while respecting authority ceilings. For each of BOUNDARY_DELTA, AUTHORITY_DELTA, OPTION_DELTA, DISCRIMINATOR_DELTA, MIGRATION_DELTA, ANTI_BUILD_DELTA choose X/Y/TIE/NEITHER. HARM is X/Y/BOTH/NONE. Return exactly one JSON object with exactly: case_id; dimension_winners (six keys); dimension_rationales (same six keys); harm; harm_rationale; material_winner (X/Y/TIE/NEITHER); material_decision_difference (boolean); material_rationale; judge_confidence (LOW/MEDIUM/HIGH); gold_role exactly CONTEXT_NOT_ANSWER_KEY.'''

def core(path,marker): return path.read_text(encoding='utf-8').split(marker,1)[0].rstrip()
def baseline_prompt(): return '\n\n'.join([core(RND,'\n## Calibration diagnosis output'),RND_SCOPE,core(SCAFFOLD,'\n## Calibration-loop return'),BASE,SERIAL])
def candidate_prompt(): return '\n\n'.join([core(RND,'\n## Calibration diagnosis output'),RND_SCOPE,core(SCAFFOLD,'\n## Calibration-loop return'),ARCH.read_text(encoding='utf-8'),CAND,SERIAL])
def canon(x): return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(',',':'))
def sha(x): return hashlib.sha256(x.encode()).hexdigest()
def write(path,obj): path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(obj,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
def rows(path): return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
def case_input(c): return {'case_id':c['case_id'],'decision_question':c['decision_question'],'frozen_input':c['frozen_input'],'known_constraints':c.get('known_constraints',[]),'available_authorities':c.get('available_authorities',[]),'instruction':'Use only this frozen case. Do not infer source repository, historical resolution, or hidden facts.'}

def call(prompt,inp,model,effort,max_tokens):
    payload={'model':model,'instructions':prompt,'input':canon(inp),'reasoning':{'effort':effort},'max_output_tokens':max_tokens}
    last=None
    for n in range(4):
        try:
            raw=post_response(payload); sem=parse_json_object(extract_output_text(raw))
            return sem,{'response_id':raw.get('id'),'model_requested':model,'model_actual':raw.get('model'),'reasoning_effort':effort,'usage':raw.get('usage')}
        except Exception as e:
            last=e
            if n<3: time.sleep(2**n)
    raise RuntimeError(f'model call failed: {last}')

def valid_neutral(o):
    req={'decision','purpose','observed_facts','alternatives','decision_relevant_considerations','unresolved_uncertainties','authority_needed','cheapest_next_check','bounded_next_move','reversal_condition','limitations'}
    if set(o)!=req: raise ValueError(f'neutral fields drift: {sorted(set(o)^req)}')
    if not isinstance(o['alternatives'],list) or not 1<=len(o['alternatives'])<=3: raise ValueError('alternatives length')

def valid_judge(o,cid):
    req={'case_id','dimension_winners','dimension_rationales','harm','harm_rationale','material_winner','material_decision_difference','material_rationale','judge_confidence','gold_role'}
    if set(o)!=req or o['case_id']!=cid: raise ValueError('judge fields/case drift')
    if set(o['dimension_winners'])!=set(DIMS) or set(o['dimension_rationales'])!=set(DIMS): raise ValueError('judge dims drift')
    if any(v not in {'X','Y','TIE','NEITHER'} for v in o['dimension_winners'].values()): raise ValueError('judge dim value')
    if o['harm'] not in {'X','Y','BOTH','NONE'} or o['material_winner'] not in {'X','Y','TIE','NEITHER'}: raise ValueError('judge verdict value')
    if o['gold_role']!='CONTEXT_NOT_ANSWER_KEY': raise ValueError('gold role')

def x_is_candidate(cid): return hashlib.sha256((cid+'|ARCH-BLIND-V0').encode()).digest()[0]%2==0
def unblind(v,xisc):
    if v in {'TIE','NEITHER','BOTH','NONE'}: return v
    return ('CANDIDATE' if xisc else 'BASELINE') if v=='X' else ('BASELINE' if xisc else 'CANDIDATE')

def summarize(js):
    cw=bw=ch=bh=0; fam=set(); dims={d:{'CANDIDATE':0,'BASELINE':0,'TIE':0,'NEITHER':0} for d in DIMS}
    for r in js:
        w=r['unblinded_material_winner']
        if r['judge']['material_decision_difference'] and w=='CANDIDATE': cw+=1; fam.add(r['case_family'])
        if r['judge']['material_decision_difference'] and w=='BASELINE': bw+=1
        h=r['unblinded_harm']; ch+=h in {'CANDIDATE','BOTH'}; bh+=h in {'BASELINE','BOTH'}
        for d,v in r['unblinded_dimension_winners'].items(): dims[d][v]+=1
    cont=cw>=2 and len(fam)>=2 and cw>bw and ch<=1
    return {'cases':len(js),'candidate_material_wins':cw,'baseline_material_wins':bw,'candidate_harm_cases':ch,'baseline_harm_cases':bh,'candidate_win_families':sorted(fam),'candidate_win_family_count':len(fam),'dimension_counts':dims,'continue_rule_frozen':RULE,'visible_train_disposition':'CONTINUE_TO_UNSEEN_HOLDOUT' if cont else 'STOP_OR_REVISE_BEFORE_HOLDOUT','promotion_note':'Visible retrospective TRAIN can never promote an autonomous Architecture Agent.'}

def validate_inputs():
    for p in [CASES,GOLD,RND,SCAFFOLD,ARCH]:
        if not p.is_file(): raise FileNotFoundError(p)
    cs=rows(CASES); ids=[c.get('case_id') for c in cs]
    if len(cs)!=12 or len(ids)!=len(set(ids)) or set(ids)!=set(FAMILIES): raise ValueError('frozen CASES drift')
    return cs  # GOLD deliberately not opened here

def run(outroot):
    if not os.getenv('OPENAI_API_KEY'): raise RuntimeError('OPENAI_API_KEY missing')
    cs=validate_inputs(); runid=dt.datetime.now(dt.timezone.utc).strftime('ARCH-AB-%Y%m%dT%H%M%SZ'); out=outroot/runid
    bp,cp=baseline_prompt(),candidate_prompt(); write(out/'run_meta.json',{'run_id':runid,'status':'RUNNER_STARTED_GOLD_UNREAD','model':MODEL,'judge_model':JUDGE_MODEL,'case_count':len(cs),'prompt_hashes':{'baseline':sha(bp),'candidate':sha(cp),'architecture':sha(ARCH.read_text(encoding='utf-8'))},'continue_rule_frozen':RULE,'gold_read_before_freeze':False})
    manifest=[]
    for i,c in enumerate(cs,1):
        cid=c['case_id']; inp=case_input(c); print(f'[{i:02d}/12] {cid} baseline',flush=True)
        b,bm=call(bp,inp,MODEL,EFFORT,6000); valid_neutral(b)
        print(f'[{i:02d}/12] {cid} candidate',flush=True)
        a,am=call(cp,inp,MODEL,EFFORT,6000); valid_neutral(a)
        obj={'case_id':cid,'case_family':FAMILIES[cid],'case_input_sha256':sha(canon(inp)),'baseline':b,'baseline_meta':bm,'candidate':a,'candidate_meta':am}
        p=out/'frozen_pairs'/f'{cid}.json'; write(p,obj); manifest.append({'case_id':cid,'path':str(p.relative_to(out)),'sha256':sha(p.read_text(encoding='utf-8')),'baseline_sha256':sha(canon(b)),'candidate_sha256':sha(canon(a))})
    freeze={'run_id':runid,'frozen_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),'gold_read_before_freeze':False,'rows':manifest}; write(out/'FREEZE_MANIFEST_BEFORE_GOLD.json',freeze); msh=sha((out/'FREEZE_MANIFEST_BEFORE_GOLD.json').read_text(encoding='utf-8')); (out/'FREEZE_MANIFEST_BEFORE_GOLD.sha256').write_text(msh+'\n')
    print('FREEZE',msh,flush=True)
    gs={g['case_id']:g for g in rows(GOLD)}  # GOLD BARRIER: first GOLD read
    if set(gs)!=set(FAMILIES): raise ValueError('GOLD ids drift')
    judged=[]
    for i,c in enumerate(cs,1):
        cid=c['case_id']; f=json.loads((out/'frozen_pairs'/f'{cid}.json').read_text()); xisc=x_is_candidate(cid); x=f['candidate'] if xisc else f['baseline']; y=f['baseline'] if xisc else f['candidate']
        ji={'case':case_input(c),'historical_gold_context':gs[cid],'response_X':x,'response_Y':y,'freeze_manifest_sha256':msh}; print(f'[{i:02d}/12] {cid} judge',flush=True)
        j,jm=call(JUDGE,ji,JUDGE_MODEL,JUDGE_EFFORT,5000); valid_judge(j,cid)
        r={'case_id':cid,'case_family':FAMILIES[cid],'blind_map_revealed_after_judgment':{'X':'CANDIDATE' if xisc else 'BASELINE','Y':'BASELINE' if xisc else 'CANDIDATE'},'judge':j,'judge_meta':jm,'unblinded_dimension_winners':{d:unblind(v,xisc) for d,v in j['dimension_winners'].items()},'unblinded_harm':unblind(j['harm'],xisc),'unblinded_material_winner':unblind(j['material_winner'],xisc)}; judged.append(r); write(out/'adjudication'/f'{cid}.json',r)
    s=summarize(judged); s.update({'run_id':runid,'freeze_manifest_sha256':msh,'model':MODEL,'judge_model':JUDGE_MODEL,'status':'COMPLETE_VISIBLE_TRAIN_CLEAN_RUNNER_BLIND_ADJUDICATION'}); write(out/'SUMMARY.json',s); print(json.dumps(s,ensure_ascii=False,indent=2)); return 0

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output-root',type=Path,default=ROOT/'runtime/architecture_ab'); ap.add_argument('--validate-only',action='store_true'); a=ap.parse_args()
    try:
        cs=validate_inputs()
        if a.validate_only: print(f'ARCH CLEAN A/B INPUTS OK: {len(cs)} cases; GOLD intentionally unread'); return 0
        return run(a.output_root)
    except Exception as e: print(f'ARCH CLEAN A/B FAILED: {e}',file=sys.stderr); return 1
if __name__=='__main__': raise SystemExit(main())
