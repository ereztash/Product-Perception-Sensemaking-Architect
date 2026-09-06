# R&D Telos Peer Review — R&D SYNTHESIZE

Status: `ROLE_CONDITIONED_MANUAL_SYNTHESIS · RND + NETA · NOT_RUNTIME_EXECUTION · NOT_CANONICAL`
Date: 2026-09-06

Inputs:
- `RND_TELOS_PEER_REVIEW_TASK_2026-09-06.md`
- `RND_TELOS_PEER_REVIEW_RND_DIAGNOSE_2026-09-06.md`
- `RND_TELOS_PEER_REVIEW_NETA_2026-09-06.md`
- prior repository benchmarks referenced by the frozen task.

## Calibration synthesis

### decision_before

Current candidate alternatives were effectively:

1. v0.2 broad telos — improve fit between all system resources and telos;
2. owner shorthand — decide what is worth learning before spending meaningful resources or turning a way of thinking into policy;
3. narrow commitment formulation — reduce decision-controlling uncertainty enough to justify/reject the next consequential resource or epistemic-method commitment.

### decision_after

The strongest current candidate is **not** a generic resource-allocation telos and **not** a pre-research / pre-commitment-only telos.

The invariant function is:

> **calibrate epistemic effort to decision value.**

More exact formal candidate:

> **R&D exists to make epistemic effort proportional to the uncertainty that can still change a consequential decision.**

Operationally:

> **Identify the uncertainty that can still change the decision, choose the cheapest admissible way to reduce it, observe the decision delta, and stop when further learning no longer justifies its cost.**

Plain Hebrew:

> **R&D קובע כמה ואיך שווה ללמוד כדי לקדם החלטה — ומתי כבר לא שווה להמשיך ללמוד.**

## Why this is more precise than v0.2

The v0.2 formulation makes `all resources` the object of R&D and therefore overlaps with orchestration, project/resource management and OWNER tradeoffs.

The revised formulation makes the object explicit:

> **epistemic effort**

R&D may choose among RESEARCH / RECOVER / TEST / REPO / ENVIRONMENT / FIELD / SCAFFOLD / WAIT / STOP, but it chooses them only as **learning/evidence channels**. It does not thereby own the underlying resource, product, runtime or field decision.

## Why this is more precise than “before he researches, he researches what to research”

That phrase correctly captures a visible first move but collapses the function into the `RESEARCH` channel.

Observed R&D behavior includes:
- deciding that no research is needed;
- choosing a repo/environment/field observation instead;
- choosing a cheap test;
- evaluating evidence after it arrives;
- deciding whether another learning move is justified;
- learning whether a method/resource should be reused, adapted or retired;
- stopping.

Therefore `research what to research` is a useful explanation but not a complete telos.

## Why “epistemic budget manager” is useful but not formal enough

The metaphor correctly emphasizes scarcity and tradeoff.

However a single `budget` metaphor can hide non-scalar constraints:
- evidence authority;
- contamination/reactivity;
- reversibility;
- validity;
- lineage/independence;
- stopping thresholds.

Disposition:

`EPISTEMIC_BUDGET_MANAGER = GOOD_EXPLANATORY_METAPHOR`

`EPISTEMIC_EFFORT_CALIBRATION = BETTER_FORMAL_MECHANISM`

## Trigger vs telos

Neta added the decisive distinction here.

### FIRE / activation context

R&D should be invoked when there is:

```text
CONSEQUENTIAL DECISION
+ MATERIAL UNCERTAINTY THAT CAN CHANGE IT
+ NONTRIVIAL CHOICE OF WHETHER / HOW MUCH / HOW TO LEARN
→ R&D
```

Common high-value triggers include:
- expensive research/build effort;
- selecting among evidence channels;
- institutionalizing a reusable rubric/protocol/reasoning method;
- deciding whether another learning iteration is worth buying;
- deciding whether prior evidence/method deserves reuse.

### TELOS / invariant function

Once invoked:

```text
DECISION-CONTROLLING UNCERTAINTY
→ EPISTEMIC EFFORT CALIBRATION
→ CHEAPEST ADMISSIBLE LEARNING MOVE
→ OBSERVED DELTA
→ CONTINUE / CHANGE CHANNEL / STOP
```

A consequential commitment is therefore a frequent trigger, not the complete telos.

## Boundary to peers / authorities

### OWNER
Owns desired end state, tradeoffs and accepted risk.

### Neta
Owns signal → observable → competing product/design mechanisms → discriminator → intervention distinction.

### REPO / ENVIRONMENT / FIELD
Own reality/state claims in their respective domains.

### R&D
Owns the **epistemic-effort decision**:
- which unresolved uncertainty is worth spending learning effort on;
- which evidence/learning channel is admissible and cheapest;
- whether the observed delta warrants another iteration;
- when to stop.

### Front-door gate
May cheaply decide whether this full R&D function is needed at all.

### Orchestrator
Owns compound coordination/routing if ever earned; R&D does not become it.

## Neta resource delta

`material: YES`

Unique distinction added:

> **Do not encode a common trigger (`before a consequential commitment`) into the telos. Separate activation condition from invariant function.**

Neta also exposed:
- `research` as an activity-level proxy;
- `budget` as a useful but potentially over-scalar metaphor;
- `before` as temporally too narrow.

This changes the candidate telos, not merely its wording.

## next_move

`TEST`

Freeze a small neighbor benchmark around the new distinction:

1. **pre-learning** — choose among research/test/repo/field;
2. **mid-learning** — evidence arrived but is inconclusive; decide whether to buy another iteration;
3. **post-learning** — decide whether a resource/method deserves future reuse/retirement;
4. **NO-FIRE controls** — direct fact, owner-fixed execution, obvious cheap test, Neta-owned product discrimination.

Compare:
- broad v0.2;
- commitment-only telos;
- epistemic-effort-calibration telos.

The new candidate wins only if it preserves material-case recall while reducing unnecessary scope and correctly handles all three temporal phases.

## stop_or_continue

`CONTINUE`

Reason: the peer review produced a material framing delta, so one targeted discriminating benchmark is justified before promotion. External research is not justified yet.

## routing_amendment_proposed

`null`

No runtime/canonical routing change should occur from this same-model manual peer review alone.

## Current disposition

`EPISTEMIC_EFFORT_CALIBRATION_TELOS: STRONGEST_CURRENT_CANDIDATE`

Not yet:

`CANONICAL_RND_TELOS`
