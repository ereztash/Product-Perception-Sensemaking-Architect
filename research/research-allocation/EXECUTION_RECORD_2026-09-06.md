# CAL-RESEARCH-ALLOCATION-001 — execution record

Status: `COMPLETE`
Report class: **WORK QA / EXECUTION NOTES**. No Neta, R&D or Scaffold conclusion is authored here; the repository output is the trace.
Date: 2026-09-06

## What executed

`runtime/calibration_loop/run.py --strict` drove the run. Nothing was authored by hand.

```text
R&D DIAGNOSE → routing.py → NETA + SCAFFOLD (parallel) → R&D SYNTHESIZE → COMPLETE
```

- Trace: `runtime/calibration_loop/traces/CAL-RESEARCH-ALLOCATION-001.json`
- Provenance: `runtime/calibration_loop/traces/CAL-RESEARCH-ALLOCATION-001-provenance.jsonl`
- Task: `fixtures/calibration-research-allocation-2026-09-06.json`
- Evidence packet: `research/research-allocation/REPO_EVIDENCE_CONTEXT_2026-09-06.json`
- Config: `runtime/calibration_loop/claude-cli-config.json`

### Routing verdict, produced by `routing.py` from the live diagnosis

```text
resources          = NETA, SCAFFOLD
NETA fired on      = signal_interpretation_ambiguity, multiple_plausible_mechanisms,
                     proxy_substitution_risk, research_to_intervention_transition
SCAFFOLD fired on  = broad_reasoning_needed, novel_synthesis_needed
authority handoffs = OWNER, ENVIRONMENT
needs FALSE        = architecture_alternatives_needed, external_research_needed,
                     repo_authority_needed, field_authority_needed
```

Neta was not forced. `external_research_needed` came back false, so no external research was opened for an allocation question. `field_authority_needed` came back false, which is a substantive routing outcome: the diagnosis judged FIELD a named requirement of the candidates rather than a resource this iteration could use.

Two authority handoffs were recorded and neither was executed. `COMPLETE` coexists with both.

## Evidence recovery performed before the run

29 canonical documents were materialized verbatim with blob hashes into the evidence packet, covering canonical state, the Neta capability gate, the prospective decision-quality and field-outcome protocols, the improvement-program status, Wave 1 closeout, the R&D eval protocol, the R&D scope map and confirmation stream, the external scope batch adjudication, the Yishumi holdout adjudication, natural-prompt and question-discovery evidence, agent-discovery closeout, DR_PLAN_0, both competitor passes, and the N3 register-test protocol and pilot. Every artifact named in the request was found.

Nine execution observations were carried in a separate block so runs and environment facts are not mistaken for document contents.

`main` had moved to `950ea73` and was merged into the work branch first, which is how the deep-research preflight lane entered the packet.

## Provenance

| Call | Served model | Turns | Stop | Cost USD |
|---|---|---|---|---|
| RND DIAGNOSE | `claude-opus-5` | 1 | end_turn | 1.671 |
| SCAFFOLD ANALYZE | `claude-opus-5` | 1 | end_turn | 1.305 |
| NETA ANALYZE | `claude-opus-5` | 1 | end_turn | 1.451 |
| RND SYNTHESIZE | `claude-opus-5` | 1 | end_turn | 2.020 |
| | | | **total** | **6.447** |

Input was roughly 285 KB per call, about 75k tokens.

Same material deviation as the prior run: the configured transport is `gpt-5.6-sol` through the OpenAI adapter, and this ran on `claude-opus-5` through the local command adapter. Routing law, frozen prompts, bridge contracts, semantic validators and trace contract are the canonical ones.

All four calls share one model lineage. Their convergence is role-conditioned execution, not independent triangulation, and contributes zero confirmatory N. The synthesis states this about its own output, including about the anti-expansion default it upholds.

The session operating the runtime shares that lineage, so this QA checks that the runtime executed as specified, not whether the resources reasoned correctly.

## Contract conformance

The synthesis returned all seven required fields and exactly the ten requested `learning_records` kinds, once each. The candidate record carries nine candidates, each with all thirteen required fields. `final_disposition.value` is one of the permitted enum values.

`stop_or_continue: CONTINUE`. `routing_amendment_proposed: None`. The runtime did not self-modify its routing law.

## Facts recorded rather than smoothed over

- **No White Paper exists in the repository.** The request's premise that it has been updated with all repo evidence is an OWNER assertion this runtime cannot verify from REPO. It is recorded as observation `EO-7`, and the synthesis assigned no weight to its contents.
- **DR_PLAN_0 has never executed.** Both Actions attempts failed on the absent credential: run `34043132828` on `dcf14d7`, run `34043263247` on `d1e4a51`.
- Every gap-closing instrument in the Neta program is frozen and blocked on independent or prospective evidence.
- No willingness-to-pay, pricing, renewal or paid-pilot evidence of any kind exists in the repository.

## What this pass did not do

No status, prompt, telos, routing rule, schema or agent boundary changed. `CONFIRMATORY_N` stays 0. Nothing was promoted, no capability was built, and no research was executed beyond this allocation decision itself.
