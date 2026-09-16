# CAL-WHITEPAPER-READER-001 — execution record

Status: `COMPLETE`
Report class: **WORK QA / EXECUTION NOTES**. No Neta, R&D or Scaffold conclusion is authored here; the repository output is the trace.
Date: 2026-09-06

## What executed

`runtime/calibration_loop/run.py --strict` drove the run. Nothing was authored by hand.

```text
R&D DIAGNOSE → routing.py → NETA + SCAFFOLD (parallel) → R&D SYNTHESIZE → COMPLETE
```

- Trace: `runtime/calibration_loop/traces/CAL-WHITEPAPER-READER-001.json`
- Provenance: `runtime/calibration_loop/traces/CAL-WHITEPAPER-READER-001-provenance.jsonl`
- Task: `fixtures/calibration-whitepaper-reader-2026-09-06.json`
- Evidence: `research/research-allocation/REPO_EVIDENCE_CONTEXT_2026-09-06.json` plus an in-task addendum
- Config: `runtime/calibration_loop/claude-cli-config.json`

### Routing verdict

```text
resources          = NETA, SCAFFOLD
NETA fired on      = signal_interpretation_ambiguity, multiple_plausible_mechanisms,
                     proxy_substitution_risk, research_to_intervention_transition
SCAFFOLD fired on  = broad_reasoning_needed, novel_synthesis_needed
authority handoffs = ENVIRONMENT, FIELD, OWNER
needs FALSE        = architecture_alternatives_needed, external_research_needed,
                     repo_authority_needed
```

`field_authority_needed` came back **true** here and **false** in `CAL-RESEARCH-ALLOCATION-001` on substantially the same evidence. The objective changed, not the facts: under the reader objective FIELD owns the binding question, so the deterministic gate produced a third authority handoff. This is a routing outcome worth preserving, not noise.

## Objective difference from the prior run

`CAL-RESEARCH-ALLOCATION-001` optimized marginal decision-uncertainty removed per unit cost for the **system's** telos and named candidate C, Neta prospective decision quality. This run optimized uncertainty removed for a **commercial reader** and re-ranked C to `CONTINUE_OPPORTUNISTICALLY`, naming a new candidate L instead. The prior synthesis was supplied in full so the divergence would be deliberate rather than accidental; the trace states which objective drives each change.

## Provenance

| Call | Served model | Turns | Stop | Cost USD |
|---|---|---|---|---|
| RND DIAGNOSE | `claude-opus-5` | 1 | end_turn | 1.584 |
| SCAFFOLD ANALYZE | `claude-opus-5` | 1 | end_turn | 1.501 |
| NETA ANALYZE | `claude-opus-5` | 1 | end_turn | 1.641 |
| RND SYNTHESIZE | `claude-opus-5` | 1 | end_turn | 2.323 |
| | | | **total** | **7.049** |

Input was roughly 341 KB per call. Same deviation as prior runs: configured transport is `gpt-5.6-sol`; this ran on `claude-opus-5` through the local command adapter. Routing law, frozen prompts, bridge contracts, semantic validators and trace contract are canonical.

One model lineage across all four calls. Convergence is role-conditioned, not independent triangulation, and contributes zero confirmatory N. The session operating the runtime shares that lineage, so this QA checks execution conformance, not reasoning quality.

## Contract conformance

Seven required synthesis fields present. All fifteen requested `learning_records` kinds present exactly once, plus two the runtime added on its own initiative: `preserved_conflicts_and_authority_ceilings` and `resource_routing_learning`. Eleven candidates, each carrying the twelve requested fields except candidate E, which omits `directly_supports`.

`stop_or_continue: CONTINUE`. The runtime did not self-modify its routing law.

## Owner assumptions recorded rather than absorbed

- **OA-1** — the White Paper exists and is updated. No such document is in the repository. Accepted as a working premise for scoping; no rewrite-to-include-existing-evidence was recommended.
- **OA-2** — the paper already carries buyer, urgency and adjacent-spend evidence. **Partially contradicted by a repository-wide audit**: zero buyer-interview artifacts, zero adjacent-spend artifacts, willingness-to-pay appearing only inside `NOT_ESTABLISHED` lists. The strength of any such evidence in the paper was treated as UNKNOWN.
- **OA-3** — quality is 8.9/10. Supplied with no scale, rubric or rater. The synthesis **declined to state any numeric movement** in either direction and recorded the refusal as the finding, citing the contract's prohibition on numeric confidence theater. Direction is given per candidate as a proposal.

## Substantive corrections the run made to the task as posed

1. **U6 is seller-held, not reader-held.** A reader knows their own budget. Evidence closing U6 never appears in the White Paper; it changes pricing and targeting. U6 was excluded from the reader ranking rather than ranked low within it.
2. **A single ranking across the seven named roles was refused** as averaging incompatible objection chains and encoding the undecided O1. Two role-classes are ranked separately.
3. **The binding item is not any of U1–U8** but the undiscriminated mechanism behind the reader's stop, because the three mechanisms rank the candidates in incompatible orders.
4. **A new OWNER item, O6**, was raised: whether O4's authorization of external contact with one artifact extends to the White Paper itself. It is not assumed.

## What this pass did not do

No status, prompt, telos, routing rule, schema or agent boundary changed. `CONFIRMATORY_N` stays 0. No evidence was collected, no reader was contacted, no claim was promoted, and no capability was built.
