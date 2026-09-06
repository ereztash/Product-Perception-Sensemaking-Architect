# Epistemology Transfer Ablation v0 — Frozen Cases

Status: `FROZEN_BEFORE_COMPARATIVE_RUN · CONTROLLED_BOUNDARY_CASES`
Date: 2026-09-06

## Compared conditions

### A — CURRENT_RND
Apply current `prompts/RND_AGENT_V0_2_CANDIDATE.md` + Shared Epistemic Kernel only.

### B — RND_PLUS_EPI
Apply A plus the residual concepts in `CAPABILITY_GAP_MAP_PASS1.md`:
- basing lineage;
- higher-order defeat/process reliability;
- testimony/disagreement;
- candidate-set underdetermination;
- epistemic-risk-sensitive evidence sufficiency;
- legitimate Bayesian updating where inputs support it;
- VOI-style ranking as adjacent decision-analysis challenger.

A B-win requires a material path difference, not a more sophisticated explanation.

## Cases

### EPI-01 — Same-model agreement
Three role-conditioned agents using the same underlying model independently endorse the same product mechanism. The owner asks whether this is strong triangulation and whether to build.

Potential issue: social/higher-order epistemology vs existing lineage rule.

### EPI-02 — Domain-specific reliability warning
A reasoning model analyzes a dataset and strongly supports hypothesis H. Before acting, we learn that on this exact task family the same model/judge has a documented failure mode that produces false positives, though its general benchmark performance is high.

Potential issue: higher-order evidence / process reliabilism.

### EPI-03 — Peer disagreement
Two independent experts with comparable credentials and access to the same evidence reach opposite conclusions. No new first-order evidence is immediately available. The decision can wait one day at low cost.

Potential issue: disagreement as higher-order evidence.

### EPI-04 — Asymmetric error cost pair
The same evidence supports intervention X in two contexts:
A. a 20-minute reversible sandbox experiment;
B. an irreversible production migration with substantial customer harm if wrong.
The owner asks whether current evidence is sufficient.

Potential issue: epistemic/inductive risk vs existing reversibility/permission discipline.

### EPI-05 — Best-of-three explanation
Three candidate mechanisms are compared; H1 best explains the observations. However all three were generated from the same initial framing and no check was made for omitted explanation families. Acting on H1 requires one week of engineering.

Potential issue: abduction / underdetermination / candidate-set completeness.

### EPI-06 — Evidence arrives after the decision
A team chose intervention X on intuition. A week later, before implementation, an independent high-quality study is found that supports X. The team claims: `our original decision was evidence-based`, and asks whether to proceed now.

Potential issue: epistemic basing vs provenance/decision lineage. Distinguish retrospective justification from current decision support.

### EPI-07 — Quantified update
A domain provides a defensible prior probability and validated likelihood ratios for a new diagnostic signal. The current repo would normally avoid fake precision. The decision threshold is explicitly probabilistic.

Potential issue: Bayesian epistemology should not be rejected merely because fake precision is prohibited.

### EPI-08 — Which uncertainty to buy
Two unresolved uncertainties can affect a decision.
- U1 costs 1 unit to investigate, has a 10% chance of flipping the decision, and if it flips improves outcome value by 2 units.
- U2 costs 4 units to investigate, has a 60% chance of flipping the decision, and if it flips improves outcome value by 20 units.
Both are admissible and independent; delay costs are negligible.

Potential issue: `cheapest decision-changing learning` vs expected Value of Information.

## Adjudication questions

For each case:
1. Does A identify the material issue?
2. Does B change the next move, evidence threshold, claim state, or stop/continue decision?
3. If B adds a distinction, is it epistemology proper, decision analysis, Neta, or existing kernel logic?
4. Would importing the concept create a neighboring false positive?
