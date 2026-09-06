# Value of Information Ranking v0 — Explicit VOI Challenger

Status: `MANUAL_CHALLENGER_RUN · FROZEN_RULE_AND_CASES · NOT_RUNTIME_EXECUTION`
Date: 2026-09-06

Challenger = CURRENT R&D + frozen explicit VOI ranking rule only.

| Case | selected_move | explicit VOI judgment | material delta vs CURRENT_RND? |
|---|---|---|---:|
| VOI-01 | B | A net ≈ -0.8; B net ≈ 7 after cost/delay. B dominates despite higher acquisition cost. | NO |
| VOI-02 | A | equal gross decision value; A has lower acquisition/delay cost and direct authority. | NO |
| VOI-03 | B | B has positive local information value and preserves reversibility; A is dominated. Immediate revert is not compelled. | NO |
| VOI-04 | B | A net ≈ -1; B net ≈ 4. Delay destroys A's nominal advantage. | NO |
| VOI-05 | B | A's reactivity/contamination nearly consumes its nominal information value; B preserves the construct. | NO |
| VOI-06 | B | A is inadmissible for stranger-value resolution; authority removes it before ranking. | NO |
| VOI-07 | STOP | neither possible result changes the live decision, so information value is zero before acquisition cost. | NO |
| VOI-08 | B | A expected improvement 0.75 < cost 1; B expected improvement 12, less cost/delay 7 ≈ positive 5. | NO |
| VOI-09 | A | value difference is preregistered immaterial; cheapest sufficient therefore wins. | NO |
| VOI-10 | B first | staged learning preserves option value: cheap first step has 65% chance of avoiding the full study while leaving it available if unresolved. | NO |

## Aggregate

- selected-move agreement with CURRENT_RND: **10/10**
- challenger-only material next-move delta: **0/10**
- cases where formula makes the doctrine more explicit/auditable: **multiple**

## Interpretation

The controlled benchmark does not establish a missing VOI capability. Current R&D's full contract already combines:
- `expected_decision_value`;
- cost/burden;
- reversibility;
- authority ceilings;
- cheapest decision-changing learning;
- stop when further learning cannot change the decision.

Together these produced the same decisions as explicit VOI in all frozen cases.

The remaining VOI value is therefore currently **doctrinal/consistency/auditability**, not demonstrated unique decision capability.

Disposition:

`VOI_RANKING_V0: NO_UNIQUE_DECISION_DELTA_ON_CONTROLLED_CASES`

A future test should use natural cases where expected value is not numerically supplied and must be inferred from the live decision structure; otherwise arithmetic makes the comparator too easy and may mask consistency differences.