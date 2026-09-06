# Value of Information Ranking v0

Status: `FROZEN_BEFORE_BASELINE · CONTROLLED_DECISION_ANALYSIS · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06

## Capability under test

Does an explicit Value-of-Information ranking rule improve R&D's choice among competing admissible learning moves beyond the current `expected_decision_value` + `cheapest decision-changing learning` doctrine?

## Challenger rule, frozen before baseline

For each admissible learning move estimate, using bounded qualitative or quantitative inputs when legitimate:

`NET_EXPECTED_DECISION_VALUE = expected decision improvement - acquisition cost - delay cost - contamination/reactivity cost`

Prefer the admissible move with the highest positive net expected decision value. Use `cheapest sufficient` only when the expected decision value of alternatives is materially equivalent or when an explicit satisficing threshold has already been set. If all moves have non-positive expected value, choose `STOP/WAIT` rather than buying information.

Authority and validity constraints dominate ranking: an inadmissible source cannot win because its nominal expected value is high.

## Output contract per case

Return exactly:
- `selected_move`
- `ranking_rationale`
- `stop_or_continue`
- `dominance_or_tradeoff`

## Cases

All numeric values are in the same normalized decision-value units unless stated otherwise. `gross expected decision improvement` is already probability-weighted unless a probability and conditional improvement are supplied separately.

### VOI-01 — cheap but dominated
Decision: whether to build a costly native mobile feature.
- A: 30-minute internal opinion poll. Cost 1. Probability of changing the build decision 0.10. Conditional improvement if it changes the decision 2. Delay 0. Contamination 0.
- B: one-day instrumented prototype with target users. Cost 4. Probability of changing decision 0.60. Conditional improvement 20. Delay 1. Contamination 0.

### VOI-02 — cheap sufficient neighbor
Decision: whether a deployment failure is caused by a missing environment variable.
- A: inspect current environment config. Cost 1. Gross expected decision improvement 8. Delay 0. Valid authority.
- B: reproduce entire deployment locally and instrument logs. Cost 5. Gross expected decision improvement 8. Delay 2. Valid authority.

### VOI-03 — all learning dominated by action
Decision: whether to keep a reversible UI copy change already deployed to 5% traffic.
- A: commission a literature review. Cost 5. Gross expected decision improvement 2. Delay 3.
- B: run the already-instrumented 24-hour field comparison. Cost 1. Gross expected decision improvement 6. Delay 1.
- C: revert immediately. Action cost 0.5; reversal remains available. Current evidence does not indicate harm.
Assume the decision can safely wait 24 hours.

### VOI-04 — delay reverses apparent value
Decision: which supplier to use before a hard procurement deadline.
- A: full technical audit. Acquisition cost 2. Gross expected decision improvement 12. Delay cost 11.
- B: verify the two contractual failure conditions that differ between suppliers. Cost 2. Gross expected decision improvement 7. Delay cost 1.

### VOI-05 — contamination reverses apparent value
Decision: whether users naturally discover a feature.
- A: ask users directly “Did you notice feature X?” immediately before observing them. Cost 1. Gross expected decision improvement before contamination 8. Contamination/reactivity cost 7.
- B: review first-run recordings without prompting. Cost 3. Gross expected decision improvement 7. Contamination 0.

### VOI-06 — authority dominates nominal value
Decision: whether users value a workflow enough to return next week.
- A: owner predicts user value from product intuition. Cost 0. Gross nominal expected decision improvement 9, but OWNER is not resolution authority for stranger value.
- B: observe return behavior in a bounded field cohort. Cost 5. Gross expected decision improvement 10. FIELD is valid authority.

### VOI-07 — no positive information value
Decision: whether to proceed with an owner-mandated, reversible formatting change. Owner has explicitly fixed the goal and accepts either implementation. Two research options could provide interesting general evidence but neither result would alter the mandated change, rollback rule, or later evaluation.
- A: literature review. Cost 4.
- B: expert interview. Cost 3.

### VOI-08 — high-value rare event
Decision: whether to migrate a critical dataset.
- A: quick sample check. Cost 1. Probability of changing decision 0.15. Conditional improvement 5. Delay 0.
- B: targeted integrity audit on the one failure mode that would cause irreversible corruption. Cost 6. Probability of changing decision 0.20. Conditional improvement 60. Delay 1.

### VOI-09 — equivalent value, choose cheaper
Decision: choose between two ways to estimate demand before a reversible pilot.
- A: five customer calls. Cost 2. Gross expected decision improvement 7. Delay 1.
- B: ten customer calls. Cost 5. Gross expected decision improvement 7.5. Delay 1.
Treat a 0.5-unit gross difference as not materially decision-relevant for this case.

### VOI-10 — sequential option value
Decision: whether to commission a three-week market study.
- A: commission full study now. Cost 12. Gross expected decision improvement 20. Delay 5.
- B: first inspect the last five lost deals. Cost 1. Gross expected decision improvement 8. If B leaves the decision unresolved, the full study remains available at the same later cost. Delay 0.
The lost-deal review has a 0.65 probability of resolving the controlling uncertainty sufficiently to avoid the full study.

## Preregistered scoring principles

- A correct challenger decision must respect authority/validity before arithmetic.
- `cheapest` wins only under value equivalence/satisficing, not as a lexicographic first rule.
- Sequential tests receive credit for preserving option value when a cheap first move can often avoid an expensive second move without foreclosing it.
- `STOP/WAIT` is correct when no information can change the live decision or when all admissible information has non-positive expected net value.
- Current R&D baseline is scored on its explicit selected move, not on whether its prose could be interpreted as VOI-compatible after the fact.

No case or scoring rule may be changed after baseline begins.