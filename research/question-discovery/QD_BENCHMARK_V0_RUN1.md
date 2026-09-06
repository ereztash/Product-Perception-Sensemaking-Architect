# Question Discovery Benchmark v0 — Run 1

Status: `MANUAL_SINGLE_MODEL_SMOKE_RUN · FROZEN_CASES_USED · NOT_GENERALIZATION_EVIDENCE`
Date: 2026-09-06
Cases/rubric frozen in: `QD_BENCHMARK_V0_FROZEN_CASES.md`

## Run contract

For each case:

```text
CURRENT QUESTION
→ UNDERLYING DECISION
→ PREMATURE OBJECT / HIDDEN ASSUMPTION (if material)
→ MOST DECISION-RELEVANT QUESTION
→ CHEAPEST ADMISSIBLE DISCRIMINATOR / NEXT MOVE
```

A case is not rewarded for sounding deeper. A challenge-case reframe counts only if it changes evidence, option set, resource/authority, build/defer/stop/act, reversal condition, or the object being decided. Neighboring controls pass by *not* being over-reframed.

---

## QD-01 — Microservices before launch

### Current question
Should a small pre-launch SaaS move to microservices now to avoid a future rewrite?

### Underlying decision
How much architecture complexity should be bought now to preserve growth/change capacity without paying for scale that does not yet exist?

### Premature object
`microservices` is treated as the necessary mechanism for future scalability/rewrite avoidance before a concrete scale, failure-isolation, team-boundary or deployment constraint has been established.

### Decision-relevant question
> **What concrete growth/change/failure property is the current architecture expected to fail, at what plausible threshold, and what is the cheapest architecture today that preserves a migration path if that threshold is reached?**

### Cheapest discriminator
Estimate the next credible workload/team/change horizon and inspect whether the current monolith has an evidenced boundary, deployment or scaling limit under that horizon. If none is material, keep the simpler runtime and preserve seams/observability that make later extraction reversible.

### Decision delta
`BUILD_MICROSERVICES_NOW` becomes `DEFER unless a named property/threshold is currently threatened; invest in migration-preserving boundaries rather than distribution by default.`

### Score
- UNDERLYING_DECISION_FOUND: YES
- PREMATURE_OBJECT_EXPOSED: YES
- QUESTION_DELTA: YES
- CHEAP_DISCRIMINATOR: YES
- NO_OVERREFRAME: N/A
- HARM: NO

---

## QD-02 — Lower price after three objections

### Current question
Should price be reduced by 20% because three prospects said it was high?

### Underlying decision
What change, if any, would improve conversion/revenue from qualified prospects?

### Premature object
The objection phrase `too expensive` is treated as evidence that price level is the causal bottleneck, and a 20% cut is treated as the remedy.

### Decision-relevant question
> **Are otherwise-qualified deals being lost because willingness-to-pay is below the current price, or is “too expensive” standing in for weak perceived value, trust, fit, budget timing, or packaging?**

### Cheapest discriminator
Review the recent lost/closed deals at the moment the objection appeared: what value had been established, what alternative/budget existed, whether a lower price would actually have closed the deal, and whether similar prospects closed at the current price. If uncertainty remains, test a bounded packaging/price variant rather than changing list price globally.

### Decision delta
`CUT_PRICE` becomes `DISCRIMINATE price sensitivity from value/fit/budget before changing price; preserve current price unless price itself survives as bottleneck.`

### Score
- UNDERLYING_DECISION_FOUND: YES
- PREMATURE_OBJECT_EXPOSED: YES
- QUESTION_DELTA: YES
- CHEAP_DISCRIMINATOR: YES
- NO_OVERREFRAME: N/A
- HARM: NO

---

## QD-03 — Post daily on LinkedIn

### Current question
Should posting frequency increase from twice a week to daily because inbound is low?

### Underlying decision
Where should effort be allocated to increase qualified inbound from LinkedIn?

### Premature object
Posting frequency is assumed to be the bottleneck without locating where the content-to-conversation path fails.

### Decision-relevant question
> **Is qualified inbound limited by insufficient reach volume, weak relevance/attention, profile/offer conversion, or failure to move interested readers into a conversation?**

### Cheapest discriminator
Use existing post/profile/conversation data to map a minimal funnel: impressions/reach → relevant engagement/profile visits → CTA/DM → qualified conversation. The first stage with weak conversion determines whether more posts can plausibly help.

### Decision delta
`POST_MORE` becomes `LOCATE BOTTLENECK; increase frequency only if reach volume is the constrained stage rather than conversion downstream.`

### Score
- UNDERLYING_DECISION_FOUND: YES
- PREMATURE_OBJECT_EXPOSED: YES
- QUESTION_DELTA: YES
- CHEAP_DISCRIMINATOR: YES
- NO_OVERREFRAME: N/A
- HARM: NO

---

## QD-04 — Hire a salesperson

### Current question
Should a salesperson be hired because the founder is overloaded with sales calls and close rate is still low?

### Underlying decision
What change will increase useful sales throughput without multiplying a broken sales process or constraining founder time unnecessarily?

### Premature object
Headcount is treated as the answer before separating a `capacity` bottleneck from a `conversion/process/qualification/offer` bottleneck.

### Decision-relevant question
> **Is the current sales constraint insufficient founder capacity to process qualified demand, or is the system failing to convert the demand already being processed?**

### Cheapest discriminator
Separate pipeline volume, founder hours, stage conversion and loss reasons. Ask the counterfactual: if call capacity doubled tomorrow with the same conversion rate and offer, would the added closed revenue justify the hire? If not, hiring scales the wrong mechanism.

### Decision delta
`HIRE_SALES` becomes `HIRE only if capacity survives as the bottleneck after conversion/process are bounded; otherwise repair the sales system first.`

### Score
- UNDERLYING_DECISION_FOUND: YES
- PREMATURE_OBJECT_EXPOSED: YES
- QUESTION_DELTA: YES
- CHEAP_DISCRIMINATOR: YES
- NO_OVERREFRAME: N/A
- HARM: NO

---

## QD-05 — Build native mobile apps

### Current question
Should native iOS/Android apps be built because several customers asked for “an app”?

### Underlying decision
What mobile-context job is currently blocked badly enough to justify a new delivery surface and its ongoing cost?

### Premature object
The requested artifact (`native app`) is treated as identical to the user need.

### Decision-relevant question
> **What task/context are users unable or unwilling to complete on the current surface, and which property of native mobile—notifications, offline use, camera/sensors, home-screen access, performance, authentication, distribution, etc.—is required to solve it?**

### Cheapest discriminator
For the actual requests, capture the blocked job and context rather than the requested solution. Test whether responsive web/PWA or one bounded mobile capability resolves the recurring need before funding two native applications.

### Decision delta
`BUILD_NATIVE_APPS` becomes `IDENTIFY the required mobile property; choose the cheapest surface that satisfies it.`

### Score
- UNDERLYING_DECISION_FOUND: YES
- PREMATURE_OBJECT_EXPOSED: YES
- QUESTION_DELTA: YES
- CHEAP_DISCRIMINATOR: YES
- NO_OVERREFRAME: N/A
- HARM: NO

---

## QD-06 — Collect 500 more observations

### Current question
Should another 500 observations be collected after a small effect with a wide CI crossing zero?

### Underlying decision
Is uncertainty about the claim worth reducing with more data under the current design, and can additional observations resolve the decision?

### Premature object
A fixed extra sample is assumed to be the appropriate remedy for uncertainty; this assumes sampling variance is the limiting uncertainty and that the design/measurement/estimand remain valid.

### Decision-relevant question
> **Would additional data under the same design reduce the uncertainty that actually controls the decision enough to change the claim/action, or is the limiting uncertainty structural (measurement, bias, specification, identification, or effect-size relevance)?**

### Cheapest discriminator
Before collecting data, compute the expected precision/power for the decision-relevant effect under the current variance and define what interval/effect would change the decision. Audit whether known design uncertainty would remain even at much larger n.

### Decision delta
`COLLECT_500` becomes `BUY more sample only if sample uncertainty is the active bottleneck and the required n is capable of crossing a predeclared decision boundary.`

### Score
- UNDERLYING_DECISION_FOUND: YES
- PREMATURE_OBJECT_EXPOSED: YES
- QUESTION_DELTA: YES
- CHEAP_DISCRIMINATOR: YES
- NO_OVERREFRAME: N/A
- HARM: NO

---

## QD-07 — Move to HubSpot

### Current question
Should the team migrate to HubSpot because the current CRM feels cumbersome and wastes time?

### Underlying decision
What change will remove material workflow cost without paying migration/lock-in cost for a problem the current tool may not cause?

### Premature object
`HubSpot` is proposed before the friction is decomposed into tool capability, configuration, data model, process, integration, or training causes.

### Decision-relevant question
> **Which recurring workflows create the material time/error burden, and does the burden come from a capability boundary of the current CRM or from how the workflow/configuration around it is designed?**

### Cheapest discriminator
Measure the top 2–3 recurring workflows end to end (steps, handoffs, waiting, duplicate entry, errors). Reproduce one high-cost workflow in a HubSpot trial only if a current-tool capability boundary survives; compare the whole workflow including migration/integration burden.

### Decision delta
`MIGRATE_CRM` becomes `ISOLATE workflow bottleneck; migrate only if the new system removes a material tool-owned constraint net of switching cost.`

### Score
- UNDERLYING_DECISION_FOUND: YES
- PREMATURE_OBJECT_EXPOSED: YES
- QUESTION_DELTA: YES
- CHEAP_DISCRIMINATOR: YES
- NO_OVERREFRAME: N/A
- HARM: NO

---

## QD-08 — Learn Kubernetes

### Current question
Should Kubernetes be learned now in order to learn to build scalable systems?

### Underlying decision
What knowledge/capability investment most improves the ability to make and implement scaling/reliability decisions?

### Premature object
A technology is treated as a prerequisite for the higher-level capability; tool fluency is conflated with architecture discrimination.

### Decision-relevant question
> **Which scaling/reliability decisions can I currently not make or implement, and is Kubernetes knowledge the cheapest missing capability for those live decisions?**

### Cheapest discriminator
Take several real architecture/scaling decisions from existing systems and ask whether Kubernetes-specific knowledge would have changed the mechanism, evidence, or implementation. If the gap is instead workload modeling, SLOs, caching, queues, state, failure domains, or deployment basics, learn that distinction first and open Kubernetes when a live case requires orchestration depth.

### Decision delta
`LEARN_KUBERNETES` becomes `LEARN the missing decision capability first; Kubernetes is on-demand unless it repeatedly changes live architecture decisions.`

### Score
- UNDERLYING_DECISION_FOUND: YES
- PREMATURE_OBJECT_EXPOSED: YES
- QUESTION_DELTA: YES
- CHEAP_DISCRIMINATOR: YES
- NO_OVERREFRAME: N/A
- HARM: NO

---

## QD-09 — Control: two supplier prices

### Current question
Which of two fully specified 12-month supplier offers is cheaper, and by how much?

### Question Discovery disposition
`NO_REFRAME`.

The question already contains the decision object, horizon and complete cost inputs. A broader question about vendor strategy, quality or switching risk would invent missing uncertainty that the user explicitly excluded from the calculation.

### Calculation
- Supplier A: 4,000 + (1,200 × 12) = **18,400 ₪**
- Supplier B: 1,650 × 12 = **19,800 ₪**
- Supplier A is cheaper by **1,400 ₪** in year one.

### Score
- UNDERLYING_DECISION_FOUND: YES (bounded cost comparison)
- PREMATURE_OBJECT_EXPOSED: NO / not needed
- QUESTION_DELTA: NO / correctly absent
- CHEAP_DISCRIMINATOR: N/A — calculation closes the question directly
- NO_OVERREFRAME: YES
- HARM: NO

---

## QD-10 — Control: reversible production rollback

### Current question
A deploy is immediately followed by a large checkout error spike, no other deploy occurred, and rollback is automated/reversible in under two minutes. Roll back now?

### Question Discovery disposition
`NO_REFRAME` for the immediate decision.

The live question is already decision-grade because:
- the harm is material and current;
- the candidate cause is temporally localized enough for mitigation;
- the intervention is cheap and reversible;
- rollback itself creates useful evidence by observing whether the error rate returns toward baseline.

A root-cause investigation is a **subsequent** question and should not delay mitigation.

### Bounded next move
Rollback now, observe checkout error rate, preserve logs/deploy evidence, then investigate cause before re-release.

### Score
- UNDERLYING_DECISION_FOUND: YES
- PREMATURE_OBJECT_EXPOSED: NO / no material premature object for mitigation
- QUESTION_DELTA: NO / correctly absent
- CHEAP_DISCRIMINATOR: N/A — the reversible action is also the fastest informative test
- NO_OVERREFRAME: YES
- HARM: NO

---

# Aggregate result

## Challenge cases QD-01..QD-08

- underlying decision found: **8/8**
- premature mechanism/object exposed: **8/8**
- material question delta: **8/8**
- bounded discriminator/next evidence: **8/8**
- harm observed: **0/8**

## Neighboring controls QD-09..QD-10

- correctly preserved original decision question: **2/2**
- over-reframed: **0/2**
- harm observed: **0/2**

## Smoke-run verdict

`SUPPORTED_AS_BEHAVIORAL_SMOKE_SIGNAL`

The candidate transformation behaved in the hypothesized direction on this frozen 10-case corpus:

1. when the prompt embedded a mechanism/tool/solution prematurely, the run moved upstream to the decision/bottleneck/causal distinction and changed what evidence or action was justified;
2. when the prompt was already bounded and decision-grade, the run did not manufacture a deeper question.

This is stronger than the originating single-session observation because it spans architecture, pricing, marketing, hiring, product, research design, operations tooling and learning allocation.

It is **not** product validation or generalization evidence.

## Major validity limits

### 1. Same-model construction contamination
The same reasoning system that knows the product hypothesis generated the challenge corpus and executed it. The cases may therefore be unusually compatible with the capability.

### 2. Synthetic prompts
Eight challenge cases were constructed examples, not naturally occurring user questions sampled before the hypothesis existed.

### 3. No baseline comparison
This run does not establish that ordinary strong LLM reasoning without the explicit Question Discovery contract would fail to produce equally useful reframes.

### 4. No external outcome
No prospective user acted on the revised question, so downstream decision quality, time saved, satisfaction and ownership remain unmeasured.

### 5. No independent adjudicator
Scoring was performed inside the same research context. A blinded independent adjudicator may disagree about whether each question delta is material.

## What would materially upgrade the evidence

The cheapest next experiment is not another synthetic batch.

Freeze 10–20 **natural prompts** drawn from prior conversations or new users, with the downstream answer hidden. Run:

- Baseline: answer the user's stated question directly with a strong general model instruction;
- Challenger: Question Discovery contract;
- blinded adjudication on decision delta, unnecessary work avoided, question ownership/preservation, and over-reframing;
- include at least 25% neighboring non-fire cases.

Only after that should the capability be called independently useful rather than an attractive reasoning pattern.
