#!/usr/bin/env python3
"""Check frozen visible Architecture historical corpus and separated adjudication anchors."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CASES=ROOT/"eval/architecture-agent/HISTORICAL_CASES_V0.jsonl"
GOLD=ROOT/"eval/architecture-agent/HISTORICAL_GOLD_V0.jsonl"
SHA=re.compile(r"^[0-9a-f]{40}$")

class CheckError(ValueError): pass

def req(ok: bool,msg: str)->None:
    if not ok: raise CheckError(msg)

def read_jsonl(path: Path)->list[dict]:
    rows=[]
    for n,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line.strip(): continue
        try: row=json.loads(line)
        except json.JSONDecodeError as exc: raise CheckError(f"{path}:{n}: {exc}") from exc
        req(isinstance(row,dict),f"{path}:{n}: row must be object"); rows.append(row)
    return rows

def main()->int:
    try:
        cases=read_jsonl(CASES); gold=read_jsonl(GOLD)
        req(8 <= len(cases) <= 15, "historical corpus must contain 8-15 cases")
        case_keys={"case_id","source_repo","source_commit","decision_question","frozen_input","known_constraints","available_authorities"}
        gold_keys={"case_id","historical_resolution","material_architecture_distinction","evidence_limit"}
        case_ids=[]; repos=set()
        for i,row in enumerate(cases,1):
            req(set(row)==case_keys,f"case {i} fields drift")
            req(all(isinstance(row[k],str) and row[k].strip() for k in ("case_id","source_repo","source_commit","decision_question","frozen_input")),f"case {i} text invalid")
            req(bool(SHA.fullmatch(row["source_commit"])),f"case {i} source_commit must be full sha")
            req(isinstance(row["known_constraints"],list) and row["known_constraints"] and all(isinstance(x,str) and x.strip() for x in row["known_constraints"]),f"case {i} constraints invalid")
            req(isinstance(row["available_authorities"],list) and row["available_authorities"] and all(x in {"OWNER","REPO","ENVIRONMENT","RESEARCH","FIELD"} for x in row["available_authorities"]),f"case {i} authorities invalid")
            case_ids.append(row["case_id"]); repos.add(row["source_repo"])
        req(len(case_ids)==len(set(case_ids)),"duplicate case ids")
        req(len(repos)>=3,"historical corpus must span at least three repositories")

        gold_ids=[]
        for i,row in enumerate(gold,1):
            req(set(row)==gold_keys,f"gold {i} fields drift")
            req(all(isinstance(row[k],str) and row[k].strip() for k in gold_keys),f"gold {i} text invalid")
            req("does not prove" in row["evidence_limit"],f"gold {i} must state historical evidence limit")
            gold_ids.append(row["case_id"])
        req(len(gold_ids)==len(set(gold_ids)),"duplicate gold ids")
        req(set(case_ids)==set(gold_ids),"case/gold id sets differ")
    except (OSError,CheckError) as exc:
        print(f"ARCHITECTURE HISTORICAL CORPUS INVALID: {exc}",file=sys.stderr); return 1
    print(f"ARCHITECTURE HISTORICAL CORPUS OK: {len(cases)} cases / {len(repos)} repos / gold separated")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
