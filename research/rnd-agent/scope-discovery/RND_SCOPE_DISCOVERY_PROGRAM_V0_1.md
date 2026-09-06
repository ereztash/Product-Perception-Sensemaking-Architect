# R&D Scope Discovery Program v0.1

Status: `RND_SELF_DESIGNED_PROTOCOL · NETA_REVIEWED · SEQUENTIAL_95PCT_TARGET · NOT_YET_RUN_CONFIRMATORILY`
Date: 2026-09-06

## 0. Decision after self-calibration

The strongest current scope hypothesis is:

> **R&D adds its highest marginal value when a consequential decision remains open and the system faces a nontrivial choice about whether, how, or how much to learn before responsibly advancing that decision.**

Candidate invariant telos remains:

> **Calibrate inquiry/learning effort to the uncertainty that can still change a consequential decision.**

This program exists to falsify, narrow, split or support that hypothesis.

---

# 1. What “>95% certainty” means here

The agent may not output a subjective confidence percentage.

`>95%` means:

> A prespecified statistical procedure gives at least 95% simultaneous / anytime-valid coverage for the primary scope claims over the frozen reference distribution and adjudication protocol.

This is not metaphysical certainty and does not generalize beyond the tested task distribution.

Because the owner requires sampling to continue until the criterion is satisfied, the confirmatory stage must use a **sequentially valid** procedure. Two admissible implementations:

1. a time-uniform confidence-sequence method for bounded/Bernoulli outcomes; or
2. a conservative alpha-spending sequence of one-sided binomial bounds at prespecified looks, with total familywise alpha <= 0.05.

Ordinary 95% fixed-N intervals may be shown descriptively but may not be repeatedly peeked at and used as the stopping rule.

---

# 2. Tested object

Freeze before confirmatory testing:

- exact CURRENT_RND prompt / version;
- exact strong baseline prompt / local-response policy;
- tools and context available to both;
- case-feature coding manual;
- outcome-adjudication rubric;
- candidate scope rule;
- primary statistical claims;
- alpha / confidence-sequence implementation.

No prompt or boundary repair mid-confirmation.

Any repair creates a new version and a new unseen confirmation stream.

---

# 3. Pre-outcome scope representation

Do **not** classify tasks using R&D's post-hoc diagnosis.

Every case is coded before model output on four primary axes.

## Axis A — DECISION_CONSEQUENCE

- `LOW_LOCAL`
- `MATERIAL_CONSEQUENTIAL`

A material decision commits meaningful resources, authority, external action, reusable policy, or forecloses important options.

## Axis B — EPISTEMIC_ALLOCATION_BURDEN

- `NONE`
  - no open learning allocation decision;
  - direct fact, settled OWNER intent, or execution.

- `OBVIOUS`
  - one cheap/reversible/legitimate discriminator or direct authority clearly dominates.

- `NONTRIVIAL`
  - at least two admissible learning/evidence moves differ materially in authority, cost, delay, validity, contamination, reversibility, reach or expected decision value, and the relative choice is unresolved before R&D output.

## Axis C — RESOLUTION_STRUCTURE

- `SINGLE_DIRECT_AUTHORITY`
- `CHANNEL_SELECTION_REQUIRED`
- `RESEARCH_METHOD_REQUIRED`

## Axis D — LEARNING_PHASE

- `PRE` — whether/what/how to learn;
- `MID` — evidence arrived; update / another iteration / channel change / stop;
- `POST` — reuse / retirement / generalization / future invocation.

## Modifiers

Record but do not initially explode into primary cells:
- cost;
- reversibility;
- delay;
- contamination/reactivity;
- reusable policy vs one-off;
- lineage / independence quality.

Only promote a modifier into a primary scope axis if discovery evidence shows a stable interaction that changes the scope decision.

---

# 4. A priori primary regions

## R1 — CORE CANDIDATE

```text
MATERIAL_CONSEQUENTIAL
× NONTRIVIAL epistemic allocation
× (CHANNEL_SELECTION_REQUIRED OR RESEARCH_METHOD_REQUIRED)
× PRE/MID/POST
```

Prediction: highest marginal R&D value.

## R2 — OBVIOUS-LEARNING NEIGHBOR

```text
MATERIAL_CONSEQUENTIAL
× OBVIOUS epistemic allocation
```

Prediction: R&D should usually bypass or add little; direct cheap test/authority should dominate.

## R3 — DIRECT-AUTHORITY / EXECUTION NEIGHBOR

```text
SINGLE_DIRECT_AUTHORITY OR EPISTEMIC_ALLOCATION_BURDEN=NONE
```

Prediction: R&D should route/stop; no material reasoning delta.

## R4 — NETA-PRIMARY NEIGHBOR

Core unresolved object is:

```text
RAW PRODUCT SIGNAL
→ COMPETING PRODUCT/DESIGN MECHANISMS
→ DISCRIMINATOR
→ INTERVENTION
```

Prediction: Neta is primary; R&D may support evidence planning only if a separate epistemic-allocation decision appears.

## R5 — LOW/LOCAL CONTROL

Low-consequence fact, explanation, generation or reversible local action.

Prediction: direct baseline should dominate on cost/latency; R&D should bypass.

---

# 5. Comparator design

## Primary paired comparator

Use the **same underlying model family/version** with identical tools/context where possible:

- `BASELINE`: strong direct general assistant / local response policy, no R&D doctrine;
- `CURRENT_RND`: frozen R&D prompt.

Using the same base model isolates whether the R&D architecture adds value beyond general-model competence.

Randomize A/B order and hide system identity from adjudicators.

## Boundary comparators

- R4: include Neta as the legitimate primary comparator.
- R3: include direct REPO/ENVIRONMENT/FIELD/OWNER authority output where available.

R&D is not credited for eventually reaching an answer after unnecessary ceremony if the legitimate comparator resolves the case directly.

---

# 6. Case-level outcome

Primary adjudication label:

- `MATERIAL_RND_WIN`
- `TIE_NO_MATERIAL_DELTA`
- `MATERIAL_RND_LOSS`
- `UNADJUDICABLE`

## MATERIAL_RND_WIN

R&D causes a materially better justified next decision path than the baseline by changing at least one of:
- what uncertainty is pursued;
- whether learning is needed;
- which evidence/authority/channel is selected;
- how much learning is justified;
- claim/evidence state;
- continue/change-channel/stop;
- future reuse/retirement of a learning method;

and the delta is large enough to justify the incremental R&D invocation burden.

Better terminology, longer analysis, agreement, more caveats, or a nicer explanation do not count.

## MATERIAL_RND_LOSS

Any of:
- worse next decision path;
- unnecessary delay of an obvious cheap action;
- authority crossing;
- opening a sound bounded inquiry without decision value;
- duplicate research/build;
- premature closure;
- materially higher burden with no compensating decision delta.

---

# 7. Adjudication independence

Same-model self-judgment cannot support the 95% claim.

Confirmatory cases require:

1. case frozen before R&D/baseline outputs;
2. A/B identity blinded;
3. primary adjudicator from a different model lineage **or** a qualified human/domain adjudicator;
4. second independent adjudication on all disagreements and a prespecified random audit subset;
5. unresolved disagreements become `UNADJUDICABLE`, not forced wins;
6. FIELD/REPO/ENVIRONMENT facts are checked by the matching authority when correctness depends on them.

Minimum audit recommendation:
- 25% randomly double-adjudicated;
- 100% of apparent R&D losses, authority violations and boundary-changing cases double-adjudicated.

---

# 8. Discovery corpus — does not count toward 95%

Purpose: learn whether the four-axis representation is missing interactions and identify a small number of candidate scope regions.

Sources:
- historical natural user tasks with preserved provenance;
- existing R&D eval controls/failures;
- repository issues/tasks;
- natural tasks from product, engineering, business/operations, research/science, content/marketing and other available domains.

Rules:
- code pre-outcome structural features before comparing outputs;
- run baseline and R&D;
- use external epistemology / zetetic / VOI only as failure labels, not as privileged challenger;
- split or merge candidate regions only in discovery;
- discovery cases are forever contaminated for final confirmation.

Target: enough cases to stabilize the taxonomy, not to hit a p-value.

Stop discovery when two consecutive substantial batches add no new material feature interaction or failure family that changes the candidate scope rule.

---

# 9. Confirmatory sequential corpus

After discovery, freeze:
- maximum 4 primary scope claims / regions if possible;
- nearest negative neighbor for each positive core claim;
- coding manual;
- adjudication rubric.

Collect **prospective or independently frozen unseen natural cases**.

## Balance requirements

For any region eligible for a final scope claim:
- minimum **60 independent adjudicable cases** before promotion, regardless of early statistical crossing;
- for R1, at least 20 PRE, 20 MID and 20 POST cases unless one phase is explicitly excluded and separately tested;
- no single application domain >25% of that region's confirmatory cases;
- include both one-off and reusable-policy cases where relevant;
- preserve nearest neighbors, not only obvious positives.

If a scope revision is required, freeze a new version and start a new confirmatory stream for the revised claim.

---

# 10. Primary rates per region

For each frozen region r estimate sequentially:

- `B_r = P(MATERIAL_RND_WIN | region r)`
- `H_r = P(MATERIAL_RND_LOSS | region r)`

A conservative lower bound on net benefit is:

```text
NET_LOWER_r = LCB(B_r) - UCB(H_r)
```

A conservative upper bound is:

```text
NET_UPPER_r = UCB(B_r) - LCB(H_r)
```

All bounds used for stopping must be simultaneous / anytime-valid under the frozen multiple-testing plan.

---

# 11. 95% scope classification rules

## HIGH-VALUE CORE

A region may be called `HIGH_VALUE_CORE` only when all are true:

1. minimum sample/balance requirements satisfied;
2. 95%-valid `LCB(B_r) > 0.50`;
3. 95%-valid `UCB(H_r) < 0.05`;
4. `NET_LOWER_r > 0`;
5. for each nearest tested negative neighbor n, either:
   - `NET_LOWER_r > NET_UPPER_n`, establishing separation; or
   - the two regions are merged / both reported as co-high-value rather than inventing a sharp boundary.

The >50% condition is a deliberately demanding operational definition of **core**, not a claim that lower-frequency value is worthless.

## CONDITIONAL / ROUTE-DEPENDENT

Use when R&D has positive material value but:
- the region does not meet the core threshold;
- value depends on a modifier/phase/domain;
- or confidence intervals overlap neighboring regions.

## LOW/NO-VALUE — BYPASS

Use only when the 95%-valid upper net bound is non-positive:

```text
NET_UPPER_r <= 0
```

or an equivalent frozen cost-adjusted criterion shows no positive marginal value over direct handling.

Do **not** call a region no-value merely because evidence is insufficient.

## WRONG AUTHORITY — HANDOFF

Use when the task's exact material question is owned by OWNER/Neta/REPO/ENVIRONMENT/FIELD and R&D's correct contribution is limited to bounded handoff/evidence planning.

Track authority violations separately; target `UCB(violation_rate) < 0.05` before claiming a safe scope boundary.

## UNKNOWN / INSUFFICIENT EVIDENCE

Mandatory whenever none of the above bounds cross.

---

# 12. Sequential 95% implementation

Preferred: established anytime-valid confidence sequences for bounded/Bernoulli outcomes.

Fallback executable design: **alpha-spending exact one-sided binomial bounds**.

Let:
- total familywise alpha = 0.05;
- M = frozen number of primary Bernoulli sequences being monitored (benefit, harm, authority-violation endpoints across primary regions);
- each sequence receives `alpha_seq = 0.05 / M`;
- at sequential look k = 1,2,... allocate:

```text
alpha_k = alpha_seq / [k(k+1)]
```

because:

```text
Σ 1/[k(k+1)] = 1
```

At each prespecified batch look, compute one-sided exact binomial bounds using `alpha_k`.

By union-bounding across looks and frozen endpoint sequences, total false-bound risk is <= 0.05, although this fallback is conservative.

If a dedicated time-uniform confidence-sequence implementation is available, prefer it for efficiency.

---

# 13. Anti-self-confirmation tests

Every confirmatory stream must contain cases designed to expose:

1. `FALSE_FIRE` — R&D adds ceremony but no decision value.
2. `FALSE_BYPASS` — a real epistemic-allocation problem is missed.
3. `OBVIOUS_ACTION_DELAY` — one cheap reversible discriminator already dominates.
4. `Neta_TAKEOVER` — R&D duplicates signal→mechanism work.
5. `AUTHORITY_TAKEOVER` — R&D reasons past REPO/ENV/FIELD/OWNER authority.
6. `INQUIRY_OVEROPENING` — a sound bounded question is reopened unnecessarily.
7. `CHEAPEST_LEXICOGRAPHIC` — cheap but low-value learning is preferred over higher net value.
8. `REUSE_POLICY_BLINDNESS` — locally cheap reusable methods with large downstream epistemic effect are underweighted.
9. `MID_LEARNING_OVERRESEARCH` — more evidence is purchased after the decision is already stable.
10. `POST_LEARNING_MEMORY_ERROR` — a method is reused/retired from weak or stale evidence.

Positive and neighboring negative cases must be paired where practical.

---

# 14. What the final boundary artifact must contain

For each region:
- pre-outcome structural definition;
- domains and phases sampled;
- N adjudicable / unadjudicable;
- material win/loss/tie counts;
- anytime-valid bounds;
- nearest neighbor;
- authority boundary;
- known failure modes;
- current classification;
- explicit generalization ceiling.

The final map must allow:

```text
TASK FEATURES
→ HIGH_VALUE_CORE
  | CONDITIONAL
  | BYPASS
  | HANDOFF
  | UNKNOWN
```

without requiring R&D to solve the case first in order to decide whether R&D should have been invoked.

---

# 15. Non-negotiable stop rule

The program **must not** stop with a promoted scope merely because:
- R&D agrees with its own telos;
- Neta agrees;
- theoretical literature converges;
- historical/manual cases look strong;
- a point estimate exceeds 95%;
- 20/20 synthetic cases pass.

Promotion may occur only when the confirmatory sequential criteria above cross under independent adjudication.

If they do not cross, the program remains active / `UNKNOWN` and continues collecting independent cases.

If evidence shows the boundary hypothesis is wrong, the hypothesis is revised in discovery, versioned, and a new confirmation stream begins. Existing failed confirmation is retained.

---

# 16. Current status

`SCOPE_PROGRAM_DESIGN: COMPLETE_ENOUGH_TO_EXECUTE`

`95PCT_SCOPE_CERTAINTY: NOT_YET_ACHIEVED`

Reason: current evidence is predominantly same-model/manual and therefore cannot satisfy the independent confirmatory requirement.

## Next move

`COLLECT + TEST`

Build the discovery dataset from natural historical tasks, freeze the first candidate scope map, then launch the independent sequential holdout.
