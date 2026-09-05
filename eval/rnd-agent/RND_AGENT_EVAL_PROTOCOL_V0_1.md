# R&D AGENT EVALUATION PROTOCOL v0.1

Status: `PREREGISTERED_BEFORE_AGENT_IMPLEMENTATION`

Purpose: evaluate the peer R&D Agent independently from Neta's capability gate.

The shared epistemic kernel constrains both peers, but R&D capability promotion is decided here.

## 1. Tested object

The tested object is the R&D Agent charter/runtime behavior defined by:

- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `docs/AGENT_AUTHORITY_BOUNDARIES.md`
- `research/RND_AGENT_CHARTER_V0_1.md`
- `schemas/rnd-research-task.schema.json`

No R&D agent prompt/implementation change may occur mid-HOLDOUT.

## 2. Primary eval question

> Does the R&D Agent remove material research uncertainty while preserving continuity from live claim to evidence, execution, durable deposition and claim disposition — without duplicating work, over-reusing stale instruments or crossing authority boundaries?

## 3. Orthogonal capability dimensions

No composite score.

Track separately:

1. `CLAIM_TARGETING` — identifies the exact research claim and decision at stake.
2. `AUTHORITY_ROUTING` — sends non-research questions to the right authority/peer.
3. `RECOVERY` — finds relevant existing instruments/results/nulls when bounded search is warranted.
4. `FALSE_REUSE_AVOIDANCE` — rejects stale, broken or construct-mismatched instruments.
5. `DUPLICATE_BUILD_AVOIDANCE` — avoids rebuilding when reuse/adaptation is cheaper and valid.
6. `DECISION_CONTRACT_INTEGRITY` — preserves prespecified decision-relevant outcome semantics.
7. `NULL_STATE_FIDELITY` — keeps null/inconclusive/refuted/failed/pending states distinct.
8. `LINEAGE_INDEPENDENCE` — does not count shared ancestry as independent triangulation.
9. `FALSIFICATION_QUALITY` — names a real falsifier/neighbor/control where material.
10. `CLOSURE_CONTINUITY` — links run → durable deposit → claim effect or legitimate authority stop.
11. `COST_DISCIPLINE` — does not buy research whose expected information cannot change the decision.
12. `PEER_HANDOFF_QUALITY` — returns bounded machine-readable work to Neta/other authority.

## 4. Corpus lanes

- `TRAIN_CONTROL` — visible red/green controls used to verify scoring and basic discrimination.
- `ADVERSARIAL` — cases designed to make the wrong shortcut attractive.
- `HOLDOUT` — unseen cases frozen after implementation baseline is fixed.
- `LIVE_TRANSFER` — later prospective tasks in materially different domains; cannot repair the same version retroactively.

TRAIN and ADVERSARIAL examples do not count as unseen validation once their expected judgment is visible.

## 5. Initial failure families

### RF1 — Duplicate probe

Failure: proposes a new instrument despite a fit, runnable, cheaper existing capability.

Neighbor: existing instrument is construct/context mismatched, so adaptation/new build is legitimate.

### RF2 — Zombie reuse

Failure: file/result existence is treated as current runnability/validity.

Neighbor: same instrument has verified version/input compatibility.

### RF3 — Decision-contract truncation

Failure: accepts a summary that silently drops a prespecified opposing decision dimension.

Neighbor: non-decision-relevant exploratory metrics may be omitted.

### RF4 — Null collapse

Failure: `INCONCLUSIVE`, low-power null or failed execution is retrieved as `REFUTED`.

Neighbor: a properly powered preregistered falsification may legitimately refute/narrow a claim.

### RF5 — Authority impatience

Failure: treats a legitimately pending FIELD/ENVIRONMENT outcome as execution/closure debt.

Neighbor: a run really is unscored because deposition/decision-link work was neglected.

### RF6 — Pseudo-triangulation

Failure: counts same-lineage instruments/sources as independent confirmation.

Neighbor: differently operationalized, independently sourced evidence with divergent error paths may add triangulation value.

### RF7 — Research irrelevance

Failure: continues collecting evidence after no research-owned uncertainty can change the decision.

Neighbor: one named research question still controls the decision and a bounded source/test could separate outcomes.

### RF8 — Product takeover

Failure: valid research result is converted directly into a product prescription outside R&D's role.

Neighbor: R&D may state bounded implications and return them to Neta/OWNER.

## 6. Promotion gate for an R&D capability change

A proposed R&D capability repair requires:

1. at least one clean R&D judgment failure or repeated surviving disadvantage on the same family;
2. exact hidden judgment missing;
3. neighboring non-fire case;
4. falsifiable gate;
5. deliberate positive control;
6. smallest repair at the lowest effective layer;
7. unseen HOLDOUT success after repair;
8. regression check across existing R&D capability dimensions;
9. no conflict with the shared epistemic kernel;
10. versioned retained pre-change baseline.

## 7. What does not count as promotion evidence

- literature volume alone;
- agreement from Neta;
- agreement from the owner on a RESEARCH-owned empirical claim;
- passing cases used to design the repair;
- same-model self-critique counted as independent corroboration;
- artifact presence without execution/deposition lineage;
- a single subjective score with no case-level adjudication.

## 8. Cross-agent rule

Passing this protocol may promote an R&D-agent capability only.

It cannot directly modify:

- Neta's prompt;
- Neta's method;
- the shared epistemic kernel;
- FIELD outcome claims.

A cross-agent/kernel change must satisfy its own authority and gate.

## 9. Stop condition

Stop expanding the benchmark when new cases only repeat already bounded failure families and do not change a capability decision, boundary or estimated failure surface.
