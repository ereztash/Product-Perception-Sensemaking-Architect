# Question Discovery / Decision Framing — Capability Profile v2 Run

Status: `MANUAL_SAME_MODEL_ABLATION · NATURAL_HISTORICAL_CORPUS · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06
Frozen inputs: `QD_CAPABILITY_PROFILE_V2_FROZEN.md`

## Conditions

- `A_DIRECT`: strong direct answer.
- `B_DECISION_ONLY`: identify underlying decision, then answer.
- `C_COMMITMENT_ONLY`: inspect premature tool/mechanism/resource/decomposition, then answer.
- `D_FULL`: decision → premature commitment → controlling uncertainty → best question/no-reframe → cheapest check.

## Comparative matrix

| Case | A_DIRECT | B_DECISION_ONLY | C_COMMITMENT_ONLY | D_FULL | Earliest material source | Full disposition |
|---|---|---|---|---|---|---|
| CP-01 Computational Empathy | Direct teaching is fit | No meaningful change | No premature object | Correctly teaches directly | none | `NO_REFRAME` |
| CP-02 Empathimetry existence | Direct factual verification is fit | No meaningful change | No premature object | Correctly answers factual question | none | `NO_REFRAME` |
| CP-03 UX/UI consequence | Tends to stay inside “what UI changes?” | Useful goal clarification but can still assume UI is intervention class | Exposes UX/UI as premature intervention object | Moves to: what observed user/system failure must change, and which intervention class can change it? | `COMMITMENT` | `REFRAME` |
| CP-04 Claude execution plan | Execute/write plan | Same plan with goal restated | No material premature object; owner already chose execution surface | Preserves request and writes plan | none | `NO_REFRAME` |
| CP-05 New LinkedIn tool | Suggest/compare tools | Moves upstream to acquisition bottleneck and often makes tool optional | Exposes “new tool” as premature resource class | Asks which bottleneck limits acquisition and which resource move has highest decision value | `DECISION` | `REFRAME` |
| CP-06 Where system loses people | Funnel diagnosis already upstream | Nearly identical | No premature object | Preserves diagnostic question | none | `NO_REFRAME` |
| CP-07 What changes first/later | Prioritize by impact/cost/dependency | Nearly identical | No premature object | Preserves sequencing question | none | `NO_REFRAME` |
| CP-08 What remain untouched | Scope-control answer is already decision-grade | Nearly identical | No premature object | Preserves question | none | `NO_REFRAME` |
| CP-09 Minimum state model | Derive minimum states/transitions from loop | Slightly improves goal linkage | “state model” may be a mechanism, but context already makes state explicit; aggressive challenge risks overreach | Answers with smallest state representation needed; does not reopen whether state exists | none | `NO_REFRAME` |
| CP-10 Idea→execution process | Build concise management workflow | Similar, with end-state restated | No material premature object | Preserves process-design request | none | `NO_REFRAME` |
| CP-11 Two-week AI roadmap | Build bounded roadmap | Similar | No material premature object | Preserves planning request | none | `NO_REFRAME` |
| CP-12 Engineering debt before adaptation | Tends to evaluate proposed sequence | Reframes to debt-prioritization objective but can retain proposed order as default | Exposes “engineering first, behavioral adaptation second” as an unproven sequence | Asks which current bottleneck/dependency makes one debt prerequisite and what evidence would reverse the order | `COMMITMENT` | `REFRAME` |

## Detailed material cases

### CP-03 — Findings → UX/UI changes

`A_DIRECT` can answer competently inside the proposed intervention category: identify screens, hierarchy, interaction changes, etc.

`B_DECISION_ONLY` improves the purpose: the decision is whether the findings justify intervention. But without an explicit commitment check it can still assume that the intervention belongs to UX/UI.

`C_COMMITMENT_ONLY` creates the first material delta:

> The finding may establish a user/system failure without establishing that visual/interface change is the causal lever.

`D_FULL` produces the useful question:

> **What observable failure must change, which competing mechanisms could produce it, and which intervention class has evidence that it can move that failure?**

Cheap check: take each finding and map `observable failure → plausible mechanism → intervention family`; only UI-owned failures become UI work.

Decision delta: `design UI changes` → `first establish intervention ownership`.

### CP-05 — “What new tool should I add?”

`A_DIRECT` tends to search the tool space.

`B_DECISION_ONLY` already creates a major improvement:

> **Where is the acquisition system currently constrained, and what resource move would improve that stage?**

At that point a new tool is only one candidate resource. `C_COMMITMENT_ONLY` reaches a similar correction by challenging `new tool` directly.

`D_FULL` is cleaner but not dramatically stronger than `B_DECISION_ONLY`:

> **Which acquisition bottleneck is currently decision-controlling, and what is the cheapest resource change that can move it?**

This case therefore does **not** demonstrate a unique Question-Discovery mechanism. Much of the value is ordinary telos/bottleneck/resource calibration.

### CP-12 — Engineering debt first, adaptation debt second

`A_DIRECT` tends to discuss whether the proposed sequence is sensible.

`B_DECISION_ONLY` asks which debt should be prioritized to improve product reliability/learning, but may still treat the proposed ordering as the candidate baseline.

`C_COMMITMENT_ONLY` creates the first material delta by challenging the embedded sequence itself.

`D_FULL` asks:

> **Which current bottleneck prevents useful learning or safe adaptation, what dependency makes one debt prerequisite to the other, and what observation would justify reversing the sequence?**

Decision delta: `engineering → adaptive behavior` as plan becomes a contingent ordering justified by dependency/bottleneck evidence.

## Aggregate selectivity

Out of 12 natural prompts:

- `D_FULL` materially reframed: **3/12**
- `D_FULL` correctly preserved the stated question: **9/12**
- observed over-reframe in adjudicated full outputs: **0/12**

This low fire rate is desirable if the capability is meant to be a gate rather than a conversational style.

## Ablation result

Among the 3 material reframe cases:

- first material delta from `DECISION` alone: **1/3** (`CP-05`)
- first material delta from explicit `COMMITMENT` inspection: **2/3** (`CP-03`, `CP-12`)
- cases requiring later `QUESTION_SELECTION` to create the first material delta: **0/3**

Interpretation:

1. `Find the underlying decision` is valuable but not unique; in at least one strong case it already explains most of the gain.
2. The more distinctive contribution is **detecting that the current question has prematurely committed to an intervention/resource/sequence that the evidence has not yet earned**.
3. `Question selection` is best understood as the output/routing consequence of that detection, not yet as the proven causal mechanism of value.
4. The full chain improves boundedness and supplies a cheap discriminator, but the unique wedge appears earlier than the final “best question” wording.

## Capability profile emerging

### Strongest fit
The capability is strongest when a user question has all of these properties:

```text
CONSEQUENTIAL NEXT MOVE
+ NAMED INTERVENTION / RESOURCE / ORDERING
+ THAT OBJECT IS NOT YET EARNED BY THE EVIDENCE
+ A CHEAPER UPSTREAM DISTINCTION CAN CHANGE THE PATH
```

Examples in this corpus:
- findings → UX/UI;
- acquisition problem → add a tool;
- two kinds of product debt → fixed sequence.

### Weak / unnecessary fit
It adds little when the question is already one of:
- factual verification;
- learning/explanation;
- explicit bottleneck diagnosis;
- bounded prioritization;
- scope control;
- requested execution after owner intent is settled;
- minimal implementation design within an already accepted architecture;
- bounded roadmap/process construction.

### Important negative finding
The evidence does **not** currently support the broad claim:

> “We are especially good at finding the highest-leverage question.”

Why: no case in this ablation required a wide search over competing questions to create the first material delta. The decisive move was usually **challenge the commitment embedded in the current question**, not search the global question space.

A narrower supported claim is:

> **We are good at detecting when a reasonable question has committed to a next move before the evidence has earned that commitment, and moving the decision back to the cheapest distinction that can justify or change it.**

That is a capability profile, not yet a market claim.

## Next experiments suggested by this result

1. `QUESTION-SPACE CHALLENGE`: cases with no explicit premature object, but several plausible upstream questions; test whether full question selection can outperform decision-framing alone.
2. `COMMITMENT FALSE-POSITIVE`: owner has deliberately chosen a tool/sequence for reasons omitted from the prompt; test whether the capability respects owner authority rather than reopening settled choices.
3. `COST SENSITIVITY`: vary the cost/reversibility of the proposed action; test whether fire rate appropriately falls as action becomes cheap/reversible.
4. `DOMAIN TRANSFER`: same structural case across software, sales, health-adjacent non-medical planning, operations, learning and personal decisions; test whether mechanism generalizes rather than relying on domain vocabulary.