# R&D Transfer Challengers v1 — Frozen Cases

Status: `VISIBLE_ADVERSARIAL_CASES_FROZEN_BEFORE_COMPARATIVE_RUN · NOT_HOLDOUT`
Date: 2026-09-06

Purpose: discriminate three candidate transfers without combining them:

A. `TARGETED_EPISTEMIC_EDGE_RULES`
B. `VALUE_OF_INFORMATION_RANKING`
C. `APPLIED_EPISTEMOLOGY_INQUIRY_RULES`

No case below counts as unseen validation because the families were deliberately designed to expose the candidate distinctions.

## A — Targeted epistemic edge rules

### TE-01 — domain-specific higher-order defeat

A forecasting model has strong overall validation and predicts that Segment X will convert well. A later audit shows that on Segment X specifically, the model's historical errors are unusually large and systematically optimistic. The product team wants to use the original prediction to allocate a large campaign budget.

Question: what should R&D do next?

### TE-02 — irrelevant reliability warning neighbor

The same forecasting model has a poor track record on a completely different task: predicting delivery delays. Its conversion predictions for Segment X were independently validated on the same type of customers and remain well calibrated. The team wants to allocate a campaign budget based on the conversion prediction.

Question: what should R&D do next?

### TE-03 — basing lineage

A team chose Architecture A in January because the lead engineer preferred it. In March, a high-quality benchmark appears showing Architecture A outperforms B under the project's actual workload. The team now writes: “We chose A based on benchmark evidence.”

Question: what should R&D preserve or change?

### TE-04 — asymmetric evidence threshold

The same moderate evidence suggests a data transformation is probably safe. Case 1: run it on a disposable sandbox copy with instant rollback. Case 2: run it on the only production dataset where corruption would be costly and restoration uncertain.

Question: should the evidence requirement be the same?

### TE-05 — best-of-generated-set

Three internally generated explanations for a recurring failure are compared. Explanation B fits the evidence better than A or C, but all three were generated from the same initial assumption that the failure is caused by user behavior. A cheap system-state inspection could reveal a fourth class of explanation: infrastructure timing.

Question: is B sufficiently established to drive a costly intervention?

## B — Value of Information ranking

### VI-01 — cheap but low expected decision value

Decision: choose between Path A and Path B.
- Test 1 costs 1 unit. There is a 10% chance it changes the choice; if it does, expected decision improvement is 2 units.
- Test 2 costs 4 units. There is a 60% chance it changes the choice; if it does, expected decision improvement is 20 units.
Both are admissible and equally fast.

Question: which learning move should R&D prefer?

### VI-02 — cheap sufficient neighbor

Decision: whether a feature should be shipped at all.
- Test 1 costs 1 unit and is expected to settle the ship/no-ship threshold with high reliability.
- Test 2 costs 8 units and would produce a much richer causal model, but that extra detail would not change the current ship/no-ship decision.

Question: which learning move should R&D prefer?

### VI-03 — delay cost dominates

A decision worth 100 units must be made today. Current evidence already favors A over B enough that additional research has only a small chance of reversing the choice. A new study costs 3 units but delays the decision by a week, with expected delay loss of 20 units.

Question: research more or decide now?

### VI-04 — sequential information

A broad field study costs 20 units. A 1-unit screening check can first determine whether the disputed mechanism is even active; if absent, the field study cannot change the decision. If present, the field study may be valuable.

Question: what sequence should R&D choose?

### VI-05 — information cannot change action

Two interventions are available. Policy constraints force Intervention A regardless of whether the uncertain mechanism is true or false. A proposed study would resolve that mechanism with high confidence at moderate cost.

Question: should R&D buy the study for the current decision?

## C — Applied epistemology / inquiry design

### AE-01 — rigorous evidence inside a narrowed frame

An organization wants to reduce employee turnover. The inquiry is framed as “Which compensation change will reduce turnover most?” Researchers have excellent salary data, market benchmarks and compensation experiments. Exit interviews repeatedly mention manager behavior and scheduling, but those variables are excluded because the inquiry was commissioned by the compensation team.

Question: what should R&D do before buying more compensation research?

### AE-02 — situated evidence exclusion

A workflow redesign is being evaluated using interviews with experienced power users because they are articulate and easy to recruit. New users are the group most likely to abandon the workflow, but their testimony is excluded as “uninformed.” The decision is whether the workflow is understandable enough to deploy broadly.

Question: what evidence should count and from whom?

### AE-03 — expert consensus with shared mediation

Three respected experts independently appear in company briefing materials and all recommend the same intervention. Inspection shows that all three briefing summaries were written from the same consultancy memo, and the original experts expressed more qualified positions than the summaries imply.

Question: how should R&D treat the apparent agreement?

### AE-04 — expert authority neighbor

A specialist with direct access to the relevant logs, a strong domain track record, no identified conflict, and a conclusion consistent with independently observed system state says a specific failure is caused by a known subsystem limit. No comparably qualified expert disagrees.

Question: does applied-epistemic caution require another expert before acting on a cheap reversible test?

### AE-05 — line-of-inquiry framing

A team investigating why a launch underperformed has collected accurate evidence about marketing channels, creative quality and campaign timing. Every follow-up question is generated from the frame “the launch failed because acquisition underperformed.” Product activation after signup has never been inspected, even though the business decision is where to invest the next month of effort.

Question: should R&D continue improving evidence inside the acquisition frame or reopen what counts as relevant to the inquiry?

## Scoring dimensions

For each case compare variants on:
- `NEXT_MOVE_DELTA`
- `CLAIM_STATE_DELTA`
- `EVIDENCE_CHANNEL_DELTA`
- `STOP_CONTINUE_DELTA`
- `UNNECESSARY_CEREMONY`
- `AUTHORITY_VIOLATION`

A challenger earns transfer interest only if it creates a material correct delta on its positive cases without changing the correct path on neighbor controls.
