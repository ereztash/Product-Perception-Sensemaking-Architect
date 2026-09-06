# Value of Information Ranking v0 — CURRENT R&D Baseline

Status: `MANUAL_CURRENT_RND_CONTRACT_RUN · FROZEN_CASES_ALREADY_COMMITTED · NOT_RUNTIME_EXECUTION`
Date: 2026-09-06
Reference prompt: `prompts/RND_AGENT_V0_2_CANDIDATE.md`

No explicit VOI formula/ranking rule was supplied to this pass.

| Case | selected_move | ranking_rationale | stop_or_continue | dominance_or_tradeoff |
|---|---|---|---|---|
| VOI-01 | B | A is cheaper but has very low expected decision effect; B's much larger probability × conditional improvement justifies its extra cost/delay before a costly build | CONTINUE | B dominates on expected decision value net of cost despite not being cheapest |
| VOI-02 | A | both appear equally capable of changing the decision, but A is direct valid authority with lower cost and delay | CONTINUE | A is cheapest sufficient and dominates B |
| VOI-03 | B | the existing bounded field comparison is cheap, valid, and can materially decide keep/revert while preserving reversibility; literature is slower and less local | CONTINUE | B dominates A; immediate revert is not justified by current evidence when safe observation is available |
| VOI-04 | B | A's nominal information gain is largely consumed by deadline delay; B targets the actual discriminating contractual conditions quickly enough to remain actionable | CONTINUE | B wins after delay cost |
| VOI-05 | B | A contaminates the very natural-discovery behavior being measured; B costs more but preserves construct validity | CONTINUE | validity/reactivity makes B superior |
| VOI-06 | B | OWNER cannot close stranger-value claims; FIELD evidence is admissible while owner intuition is not resolution authority regardless of nominal convenience | CONTINUE | authority constraint removes A from ranking |
| VOI-07 | STOP | neither information source can alter the fixed reversible change, rollback rule, or evaluation; collecting it would be research irrelevance | STOP | all information value is effectively zero for the live decision |
| VOI-08 | B | A is cheap but has negative/near-zero expected value relative to cost; B targets a rare but very high-consequence corruption mode and has substantially higher expected decision value | CONTINUE | B wins on expected loss avoided despite higher acquisition cost |
| VOI-09 | A | the 0.5-unit gross advantage of B is preregistered as immaterial; A therefore supplies materially equivalent decision value at lower cost | CONTINUE | cheapest sufficient wins under value equivalence |
| VOI-10 | B first | B can resolve the uncertainty cheaply in 65% of cases without foreclosing the full study; preserve the expensive study as a contingent second move | CONTINUE | sequential option value favors cheap staged learning over buying full study immediately |

## Baseline aggregate

Current R&D selected the same qualitative move that an explicit VOI-style comparator would be expected to select in **10/10 controlled cases**.

Important mechanism evidence:
- it did **not** apply `cheapest` lexicographically in VOI-01 or VOI-08;
- it respected delay and contamination costs;
- it let authority/validity dominate nominal value;
- it used `cheapest sufficient` under material value equivalence;
- it preserved sequential option value;
- it stopped when information could not change the decision.

## Baseline interpretation

The phrase `cheapest decision-changing learning` is doctrinally ambiguous in isolation, but the full v0.2 contract also requires `expected_decision_value`, reversibility, authority ceilings and cost/burden assessment. In this controlled run, those surrounding constraints were enough to recover VOI-compatible choices without an explicit VOI formula.

Therefore the VOI challenger must demonstrate one of:
1. a case where current R&D actually chooses a materially inferior learning move;
2. a repeatable burden/consistency advantage from explicit ranking;
3. a boundary condition current qualitative doctrine cannot adjudicate reliably.

A formula that merely explains the same 10 decisions more formally is not a capability gain.