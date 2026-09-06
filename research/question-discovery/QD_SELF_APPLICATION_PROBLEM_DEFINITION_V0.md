# Question Discovery — Self-Application Problem Definition v0

Status: `SELF_APPLICATION_RESEARCH_DEPOSIT · NOT_CANONICAL`
Date: 2026-09-06
Parent artifacts:
- `SESSION_2026-09-06_QUESTION_REFRAMING_LINEAGE.md`
- `QD_BENCHMARK_V0_FROZEN_CASES.md`
- `QD_BENCHMARK_V0_RUN1.md`

## Current question being self-applied

> What problem does Question Discovery solve best?

## Why this question may itself be premature

It assumes:
1. `Question Discovery` is already the correct product object/name;
2. the core failure is a person's inability to formulate a good question;
3. the product should be defined by its output (`a better question`) rather than by the costly failure it prevents.

The self-application therefore treats `Question Discovery` as a candidate mechanism, not the problem definition.

---

## Underlying product decision

> Which recurring, costly, externally recognizable failure should this capability be positioned and tested against, such that success can be observed without rewarding clever wording?

This is the decision that determines:
- who the product is for;
- when it should fire;
- what counts as value;
- what baseline it must beat;
- what outcome should be measured;
- what neighboring cases it must leave alone.

---

## Evidence recovered from the 10-case smoke run

Across QD-01..QD-08, the successful cases shared the same structural pattern despite spanning architecture, pricing, marketing, hiring, product, research design, CRM tooling and learning allocation:

```text
CONSEQUENTIAL DECISION
→ OBSERVED SIGNAL / GOAL
→ NAMED MECHANISM / TOOL / ACTION ENTERS TOO EARLY
→ USER ASKS WHETHER / HOW MUCH / WHEN TO DO THAT THING
→ DIRECT ANSWER WOULD OPTIMIZE INSIDE THE ASSUMPTION
→ REFRAME MOVES UPSTREAM TO BOTTLENECK / CAUSAL / REQUIREMENT DISTINCTION
→ CHEAP EVIDENCE CHANGES BUILD / DEFER / STOP / ACT
```

Examples:
- growth fear → microservices;
- `too expensive` → 20% price cut;
- low inbound → daily posting;
- founder overload → salesperson;
- mobile request → native app;
- wide CI → exactly 500 more observations;
- CRM friction → HubSpot migration;
- scalability goal → Kubernetes curriculum.

The two controls reveal the opposite boundary:
- a fully specified cost calculation should be answered directly;
- an urgent, cheap, reversible rollback should be acted on directly.

Therefore the capability is not valuable whenever a question can be made more abstract. It is valuable when a *prematurely fixed object* causes the stated question to sit downstream of the uncertainty that controls the decision.

---

## Competing problem definitions

### P1 — "People do not know how to ask good questions"

**Explains:** why reformulation can help.

**Fails because:** too broad; many users ask perfectly adequate questions; frames a competence deficit in the user; gives no clear fire/no-fire boundary; rewards eloquence over decision delta.

Disposition: `REJECT_AS_PRIMARY`.

### P2 — "LLMs answer the question asked instead of the question that should be asked"

**Explains:** product contrast with direct-answer assistants.

**Fails because:** defines the problem relative to one implementation category (LLMs) rather than the user's costly failure; humans, consultants and search/research workflows can make the same error.

Disposition: `USEFUL_COMPETITIVE_FRAMING, NOT CORE_PROBLEM`.

### P3 — "Decision-makers prematurely commit to a solution/mechanism and then spend resources optimizing it"

**Explains:** all eight challenge cases; directly connects to avoided research/build/migration/hiring/learning cost; gives a clear intervention point.

**Incomplete because:** the premature object is not always literally a solution; it can be a proxy, metric, causal interpretation, fixed sample size, role label or research program.

Disposition: `NARROW_BUT_CLOSE`.

### P4 — "The question being answered is downstream of the uncertainty that actually controls the decision"

**Explains:** all eight challenge cases without requiring the premature object to be a literal solution; explains why changing the question changes evidence, options and action; also explains both controls because their stated question already sits at the controlling uncertainty/action boundary.

**Risk:** wording is abstract and not immediately user-facing.

Disposition: `BEST_STRUCTURAL_DEFINITION`.

---

## Best current problem definition

### Structural form

> **A decision-maker is about to spend attention, research, money or implementation effort answering a question that is already downstream of the uncertainty that actually controls the decision.**

The common cause is often that the question has silently fixed one of these too early:
- mechanism;
- solution;
- tool/vendor;
- causal explanation;
- metric/proxy;
- resource amount;
- professional label;
- research program.

A direct answer can therefore be locally correct while globally wasteful.

### More operational form

> **The user has a reasonable, answerable question — but answering it now would optimize an unverified assumption instead of resolving the decision.**

### User-facing form

> **Before you spend time answering the question in front of you, check whether its answer can actually change the decision you care about.**

---

## The failure being prevented

Candidate name: `DOWNSTREAM_QUESTION_COMMITMENT`.

Definition:

```text
A question is downstream-committed when:
1. a consequential decision remains unresolved;
2. the question fixes an object/mechanism/proxy before that object is established as decision-controlling;
3. answering the question can consume material resources;
4. an upstream distinction could change the evidence, option set or action.
```

Failure chain:

```text
SIGNAL / GOAL
→ PREMATURE OBJECT
→ ANSWERABLE DOWNSTREAM QUESTION
→ HIGH-QUALITY ANSWER
→ RESEARCH / BUILD / HIRE / MIGRATE / LEARN
→ LITTLE OR NO MOVEMENT ON THE ACTUAL DECISION
```

This is why answer quality alone is an inadequate product metric.

---

## Candidate capability reframe

If the problem definition above survives, `Question Discovery` may not be the best final name for the capability.

The transformation is closer to:

```text
CURRENT QUESTION
→ DECISION DEPENDENCY CHECK
→ PREMATURE COMMITMENT DETECTION
→ UPSTREAM CONTROLLING UNCERTAINTY
→ DECISION-GRADE QUESTION OR NO-REFRAME
→ CHEAPEST RESOLUTION
```

Candidate capability names for later testing:
- `Decision Framing Guard`
- `Decision Question Discovery`
- `Upstream Question Check`
- `Decision Dependency Check`

No rename is authorized by this self-run alone.

---

## Fire boundary

The capability should fire when all/most are true:
1. there is a consequential unresolved decision;
2. the stated question embeds a mechanism/tool/proxy/resource/action as if already justified;
3. different upstream explanations would imply different actions;
4. answering the current question costs non-trivial effort or creates lock-in;
5. a bounded discriminator can alter the path.

Strong fire examples from v0:
- adopt architecture pattern;
- cut price;
- increase content frequency;
- hire role;
- build platform/app;
- collect more data;
- migrate tool;
- learn technology.

## No-fire boundary

Do **not** reframe when:
- the question is a bounded calculation with sufficient inputs;
- the action is cheap, reversible, urgent and itself informative;
- the controlling uncertainty is already explicit;
- no plausible reframe changes evidence/options/action;
- reframing would merely increase abstraction or delay a justified action.

---

## Product value unit

The strongest current value unit is not `better question quality`.

It is:

> **resources not spent answering a downstream question that would not have controlled the decision.**

Potential observable outcomes:
- avoided unnecessary build/migration/hire/research;
- fewer evidence calls before a decision;
- changed `BUILD → DEFER/STOP` or `RESEARCH → TEST/ACT`;
- shorter time to a stable bounded decision;
- fewer reversals caused by invalid initial framing;
- preserved ownership because the system exposes the distinction rather than merely supplying a conclusion.

---

## Falsifiers

This problem definition should be weakened/rejected if prospective natural prompts show any of the following:

1. most valuable reframes occur without any downstream commitment/premature object;
2. direct-answer baselines already detect the controlling uncertainty at the same rate/cost;
3. reframing improves wording but rarely changes evidence/options/action;
4. over-reframing delays cheap reversible action often enough to offset avoided waste;
5. users cannot recognize the revised question as serving their original decision;
6. resource savings do not materialize prospectively.

---

## Self-application decision delta

### Before

> `Question Discovery helps people ask the question they would have asked if they knew how to formulate it.`

### After

> **The capability is best aimed at preventing downstream-question commitment: spending resources answering a reasonable, answerable question that has already fixed an unverified assumption upstream of the actual decision.**

The `better question` is the mechanism/output.

The product problem is **misallocated decision effort caused by premature framing**.

---

## Cheapest next test

Do not ask users whether they want "better questions".

Sample natural, pre-existing questions where a real action/resource spend followed. Blindly classify whether each question was downstream-committed *before seeing the eventual outcome*. Then compare:

- direct-answer baseline;
- Question Discovery / Decision Framing challenger;

on:
- whether the eventual resource spend would have changed;
- whether the reframe identifies the controlling uncertainty earlier;
- over-reframe rate on already decision-grade cases;
- amount of research/build/work plausibly avoided.

A clean positive result would support the problem definition more strongly than another set of synthetic reframes.
