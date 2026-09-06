# Epistemology Transfer Ablation v0 — Comparative Run

Status: `MANUAL_SAME_MODEL_CONTRACT_RUN · REPO_GROUNDED · EXTERNAL_CONCEPT_INFORMED · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06
Frozen cases: `EPISTEMOLOGY_TRANSFER_ABLATION_V0_FROZEN.md`

## Comparison summary

| Case | CURRENT_RND | RND_PLUS_EPI | Material B-only delta? | Ownership |
|---|---|---|---:|---|
| EPI-01 same-model agreement | Rejects agreement as independent triangulation due shared lineage; require independent authority/evidence before strong claim/build | Social epistemology gives vocabulary for testimony/group belief but reaches same decision | NO | Existing kernel |
| EPI-02 domain-specific reliability warning | Resource assessment explicitly includes neighboring weak tasks, uncertainty and prior invocation usefulness; reliability warning justifies retest / independent check before action | Higher-order evidence/reliabilism names the warning as evidence about the inference process that can defeat/downweight first-order support | NO material path delta; sharper rationale | Existing R&D + useful vocabulary |
| EPI-03 peer disagreement | Preserve disagreement rather than average; because wait is cheap, acquire discriminating evidence / check authority or remain unresolved | Disagreement literature treats disagreement as possible higher-order evidence, but gives no single uncontested equal-weight rule; confidence should not be mechanically averaged | NO | Existing conflict rule; social epistemology is refinement |
| EPI-04 asymmetric error cost | Sandbox: TEST is cheap/reversible; production migration: requested use + reversibility + permission demand stronger support / safer evidence path | Epistemic/inductive risk explains why evidence thresholds can differ when error consequences differ | NO material path delta | Existing kernel/R&D; strong conceptual support |
| EPI-05 best-of-three explanation | Costly intervention + multiple mechanisms triggers Neta/discriminator; do not treat best current explanation as uniquely established | Underdetermination/abduction adds `best among considered ≠ true/unique if candidate set poor` | NO vs existing Calibration Loop; useful generic guard if Neta absent | Primarily Neta / shared guard candidate |
| EPI-06 evidence after decision | Provenance/decision lineage distinguishes original intuition-based decision from current evidence-supported state; new study may justify proceeding now without rewriting history | Epistemic basing sharpens `evidence available now ≠ reason for which original belief was held` | NO current-decision delta; YES retrospective lineage clarity | Existing provenance + possible wording repair |
| EPI-07 quantified update | Fake precision rule does not prohibit legitimate quantitative evidence; route to appropriate statistical/research method when priors/likelihoods are defensible | Bayesian epistemology supplies credence/conditionalization norms | NO core R&D delta | Domain/statistics/formal epistemology as optional tool |
| EPI-08 which uncertainty to buy | Current contract asks expected decision value and cost, but `cheapest decision-changing learning` can be read too lexicographically. A disciplined run should prefer U2 because expected gain dominates cost; the contract does not define a calculation | VOI explicitly ranks information by expected improvement in the decision net of acquisition/delay cost; U1 expected gross decision gain=0.2 vs cost=1; U2 expected gross gain=12 vs cost=4, so U2 is strongly preferred | **PARTIAL MATERIAL DELTA: formal decision rule closes an ambiguity in current doctrine** | Decision analysis / VOI, not epistemology proper |

## Aggregate

### Epistemology proper

Across EPI-01..EPI-07:
- clean material next-move distinctions unavailable to current R&D + Neta/kernel: **0/7 established**;
- cases where external epistemology materially sharpens the explanation / hidden judgment: **4/7** (higher-order evidence, epistemic risk, underdetermination/abduction, basing lineage);
- cases where importing broad machinery risks duplication/over-formalization: **multiple**, especially Bayesian numerics and generic disagreement rules.

This does **not** support `BROAD_EPISTEMOLOGY_LAYER` as a new peer/capability.

### Adjacent decision analysis / Value of Information

EPI-08 exposes a real doctrinal ambiguity:

```text
CHEAPEST MOVE THAT CAN CHANGE THE DECISION
≠
MOVE WITH HIGHEST EXPECTED DECISION IMPROVEMENT NET OF LEARNING COST
```

When multiple admissible learning moves can change a decision, literal `cheapest` may be inferior to a more expensive observation with much greater expected decision value.

The v0.2 documents partially anticipate this through `expected_decision_value`, but no explicit ranking law resolves the conflict.

Candidate repair concept:

> Prefer the admissible learning move with the highest expected decision value net of learning/delay/contamination cost; use `cheapest sufficient` only when expected decision value is materially equivalent or a threshold/satisficing rule has been set.

This is much closer to formal Value of Information / decision analysis than to classical epistemology.

## Important convergence result

The lack of a broad epistemology win is not evidence that R&D is unrelated to epistemology.

On the contrary, the current repo already independently implements many applied-epistemic distinctions:
- evidence is claim- and use-relative;
- authority is claim-specific;
- agreement is not independence;
- null is not refutation;
- provenance matters;
- falsifiers and reversal conditions matter;
- method/resource reliability is learned over time;
- more information is not automatically valuable;
- stop when remaining uncertainty cannot change the decision.

External epistemology therefore functions more as **theoretical convergence and edge-case vocabulary** than as a missing broad engine.

## Current hypothesis disposition

- H0 vocabulary-only: **PARTIALLY SUPPORTED, but too strong** — several concepts sharpen hidden judgments.
- H1 broad-domain upgrade: **NOT SUPPORTED**.
- H2 targeted-subdomain transfer: **SUPPORTED AS A RESEARCH DIRECTION, not yet as a prompt change**.

Strongest targeted epistemology candidates:
1. `HIGHER_ORDER_EVIDENCE / DEFEAT` — make process-reliability evidence explicitly capable of changing first-order claim state;
2. `EPISTEMIC_RISK` — explicitly test whether false-positive vs false-negative consequences should change evidence sufficiency for a requested use;
3. `CANDIDATE_SET_UNDERDETERMINATION` — generic guard against best-of-sampled closure when Neta is not the active peer;
4. `BASING_LINEAGE` — distinguish `decision was evidence-based then` from `decision is evidence-supported now`.

Strongest overall capability challenger:
5. `VALUE_OF_INFORMATION` — explicit ranking/stop logic for competing learning investments.

## Falsifier

The targeted-transfer thesis weakens if unseen cases show that current R&D already handles all four epistemology candidates with no material error or burden reduction.

The VOI challenger weakens if current R&D consistently chooses the same learning move as an explicit VOI-style comparator across cases with cost/value tradeoffs, including neighboring cases where cheap sufficient evidence should win.
