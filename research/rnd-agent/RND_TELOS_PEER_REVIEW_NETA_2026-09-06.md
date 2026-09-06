# R&D Telos Peer Review — Neta Pass

Status: `ROLE_CONDITIONED_MANUAL_NETA_PASS · FROZEN_NETA_PROMPT · NOT_INDEPENDENT_MODEL_RUN`
Date: 2026-09-06
Prompt contract: `prompts/SYSTEM.md`
Task: `RND_TELOS_PEER_REVIEW_TASK_2026-09-06.md`

## RAW SIGNAL

> "בעצם לפני שהוא חוקר, הוא חוקר מה צריך לחקור?"

and the emerging shorthand:

> "מנהל תקציב אפיסטמי"

These are useful owner signals. Neither should be treated as the diagnosis yet.

## OBSERVABLE

Across the repository evidence already collected:

1. R&D adds material value when a decision is about to buy evidence, research, a reusable method, a rubric, a scoring policy, an agent workflow, or another consequential way of learning/deciding.
2. R&D often adds no value on bounded factual, creative, execution, or owner-fixed tasks.
3. R&D's useful move is frequently not `RESEARCH`; it may be `RECOVER`, `TEST`, `REPO`, `ENVIRONMENT`, `FIELD`, `WAIT`, or `STOP`.
4. R&D also evaluates the result *after* a learning move: whether it changed the decision, whether more learning is justified, and whether a resource/method deserves reuse.
5. The narrow benchmark miss (`Waze`) occurred because a cheap individual action became a durable reusable epistemic control policy.

## CANDIDATE MECHANISMS

### 1. META-RESEARCH / QUESTION SELECTION

Interpretation:
> R&D first decides what should be researched, then researches it.

Explains:
- why broad research requests are narrowed;
- why R&D identifies controlling uncertainty before source collection.

Does not explain:
- choosing REPO/FIELD/TEST/WAIT/STOP instead of research;
- deciding whether to continue after evidence arrives;
- evaluating whether a reusable method should be internalized or retired.

Disposition: **too activity-bound**. `Research` is one instrument, not the mechanism.

### 2. COMMITMENT QUALIFICATION

Interpretation:
> R&D determines whether a consequential resource/method commitment has earned itself.

Explains:
- expensive build/research/tool commitments;
- institutionalizing rubrics/workflows;
- cost/reversibility sensitivity;
- the Waze reusable-policy miss.

Does not fully explain:
- R&D's post-learning function: did the evidence produce enough delta, should another learning move be bought, should the method be reused/retired?
- cases where the live decision is still being bounded and no single downstream commitment is yet named.

Disposition: **strong FIRE condition, incomplete telos**.

### 3. EPISTEMIC-EFFORT CALIBRATION

Interpretation:
> R&D calibrates how much and what kind of learning a consequential decision deserves.

Explains:
- choosing among research/recovery/test/reality authorities;
- cost and authority discipline;
- continuing vs stopping;
- avoiding irrelevant evidence accumulation;
- evaluating whether a method/resource deserves future reuse;
- why a resource/method commitment often triggers R&D without becoming its final purpose.

Disposition: **best current mechanism fit**.

## PROXY / METAPHOR CHECK

### `budget`
Useful metaphor because it foregrounds scarcity and tradeoff.
Risk: implies one scalar pool or numerical optimization. The actual mechanism also contains authority, admissibility, contamination, reversibility, and stop conditions that are not reducible to one budget score.

Recommendation:
- keep `epistemic budget` as explanatory shorthand;
- do not make `budget manager` the formal telos yet.

### `before`
Too narrow as a formal temporal boundary.
R&D acts before a learning move, but also after it to decide whether the new state justifies continuation, reuse, adaptation, retirement or stop.

Recommendation:
- use `before` in user-facing explanation of the first move;
- do not encode it into the formal telos.

### `what to research`
Too narrow because it privileges one evidence channel.

### `resource commitment`
Better treated as an activation context / fire condition than as the objective itself.

## ONE DISCRIMINATOR

To distinguish `commitment qualification` from `epistemic-effort calibration`, use this question on unseen cases:

> **Can R&D add material value after one admissible learning move has already been completed, when the remaining decision is whether to buy another learning move, stop, or update future reuse?**

If yes repeatedly, `commitment qualification` is too phase-bound and `epistemic-effort calibration` better explains the full loop.

The current R&D contract already contains `OBSERVED DELTA → RECALIBRATE → UPDATED STATE`, so the repository predicts that such cases should exist.

## DESIGN DISTINCTION

The candidate telos should describe the invariant function, not its common trigger.

Trigger:

```text
CONSEQUENTIAL DECISION
+ MATERIAL UNCERTAINTY
+ NONTRIVIAL CHOICE OF HOW MUCH / HOW TO LEARN
→ invoke R&D
```

Invariant function:

```text
DECISION-CONTROLLING UNCERTAINTY
→ CALIBRATE EPISTEMIC EFFORT
→ CHEAPEST ADMISSIBLE LEARNING MOVE
→ OBSERVE DELTA
→ CONTINUE / CHANGE CHANNEL / STOP
```

## Neta candidate wording

### Formal candidate

> **R&D exists to make epistemic effort proportional to the uncertainty that can still change a consequential decision.**

### Operational candidate

> **Identify the uncertainty that can still change the decision, choose the cheapest admissible way to reduce it, and stop when further learning no longer justifies its cost.**

### Plain Hebrew

> **R&D קובע כמה ואיך שווה ללמוד כדי לקדם החלטה — ומתי כבר לא שווה להמשיך ללמוד.**

## Neighbor boundary

This does not make R&D the owner of:
- what the owner wants;
- what a product signal means;
- what reality is;
- generic routing;
- local clarification/premise correction;
- every reusable template.

It owns the **epistemic effort decision** around a consequential decision.

## Neta disposition

`EPISTEMIC_BUDGET_MANAGER` is a useful metaphor.

`EPISTEMIC_EFFORT_CALIBRATION` is the stronger mechanism candidate.

The phrase `before he researches, he researches what to research` captures the first visible move, but not the full telos.