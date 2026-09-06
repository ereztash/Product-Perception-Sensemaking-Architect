# Front-Door Gate Shadow Test v0 — Adjudication

Status: `RETROSPECTIVE_SHADOW_SIGNAL · GATE_FROZEN_BEFORE_REFERENCE · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06
Inputs: `QD_SHADOW_GATE_V0_FROZEN.md`
Gate: `QD_SHADOW_GATE_V0_GATE.md`
Shadow reference: `QD_SHADOW_GATE_V0_RND.md`

## Per-case comparison

| Case | Gate | Shadow R&D material delta? | Adjudication |
|---|---|---:|---|
| SG-01 | NEEDS_CALIBRATION | YES | TRUE ESCALATION |
| SG-02 | DIRECT_EARNED | NO | SAFE BYPASS |
| SG-03 | DIRECT_EARNED | NO | SAFE BYPASS |
| SG-04 | DIRECT_EARNED | NO | SAFE BYPASS |
| SG-05 | DOMAIN_HANDOFF | NO | SAFE BYPASS |
| SG-06 | DIRECT_EARNED | NO | SAFE BYPASS |
| SG-07 | NEEDS_CALIBRATION | YES | TRUE ESCALATION |
| SG-08 | DIRECT_EARNED | NO | SAFE BYPASS |
| SG-09 | NEEDS_CALIBRATION | YES | TRUE ESCALATION |
| SG-10 | DOMAIN_HANDOFF | NO | SAFE BYPASS |
| SG-11 | DOMAIN_HANDOFF | NO | SAFE BYPASS |
| SG-12 | DOMAIN_HANDOFF | NO | SAFE BYPASS |
| SG-13 | DOMAIN_HANDOFF | NO | SAFE BYPASS |
| SG-14 | DIRECT_EARNED | NO | SAFE BYPASS |
| SG-15 | DOMAIN_HANDOFF | NO | SAFE BYPASS |
| SG-16 | DOMAIN_HANDOFF | NO | SAFE BYPASS |
| SG-17 | DIRECT_EARNED | YES | **FALSE BYPASS** |
| SG-18 | DIRECT_EARNED | NO | SAFE BYPASS |
| SG-19 | NEEDS_CALIBRATION | YES | TRUE ESCALATION |
| SG-20 | DIRECT_EARNED | NO | SAFE BYPASS |

## Frozen metrics

### BYPASS_RATE
Gate bypassed full R&D on 16/20 cases.

**80%**

### FALSE_BYPASS_RATE
Among the 16 bypasses, shadow R&D materially changed the path in 1 case (SG-17).

**1/16 = 6.25%**

### DECISION_AGREEMENT_ON_BYPASS
15 of 16 bypassed cases preserved the materially same next move.

**15/16 = 93.75%**

### UNNECESSARY_ESCALATION_RATE
Gate escalated 4 cases; all 4 received a material calibration delta from shadow R&D.

**0/4 = 0%**

### MATERIAL-CASE RECALL
Shadow R&D identified 5 cases where calibration materially changed the decision path. Gate escalated 4 of them.

**4/5 = 80%**

### NON-MATERIAL BYPASS SPECIFICITY
There were 15 cases where shadow R&D added no material calibration delta. Gate bypassed all 15.

**15/15 = 100%**

### OVERALL ROUTING AGREEMENT
19/20 cases were routed consistently with the shadow reference under the binary question `full calibration needed?`.

**95%**

### AUTHORITY_VIOLATION_RATE
No case showed the gate reopening an explicitly settled OWNER/contract constraint.

**0/20 observed**

### GATE_HARM
No cheap/direct action was delayed by an unnecessary escalation in this corpus.

**0/20 observed**

## The one failure matters

### SG-17
Prompt:
> “Is maintainability part of a group of gaps?”

Gate interpretation:
- conceptual classification question;
- answer directly.

Shadow R&D interpretation:
- the classification is not merely educational;
- it is being used to construct a taxonomy for evaluating/scoring repository gaps;
- therefore a wrong decomposition axis can contaminate many downstream judgments.

The material upstream question is:

> **What single decomposition axis should own the gap taxonomy so that categories are mutually exclusive and collectively exhaustive, and where does maintainability map under that axis?**

Failure mechanism:

`apparently conceptual question → hidden downstream decision use → gate underestimates consequence of framing`.

This is distinct from the previously tested `premature tool/solution` trigger. The gate needs evidence about **intended downstream use** to distinguish harmless classification from schema/taxonomy decisions that propagate.

## What the experiment supports

The result is directionally strong for the front-door routing thesis:

```text
20 prompts
→ 16 proposed bypasses
→ 15 safe bypasses
→ 4 justified escalations
→ 1 unsafe bypass
```

On this corpus, the compact gate could have avoided **16 full R&D-loop invocations**, while disagreeing materially with the shadow reference once.

However, this does **not** establish an 80% real cost saving:
- the gate itself has a cost;
- domain handoffs still invoke tools/research;
- this run did not measure tokens, latency or monetary cost;
- shadow R&D was manually contract-applied rather than live-runtime executed.

The defensible claim is therefore:

> **80% potential full-loop bypass at 6.25% false-bypass in this retrospective corpus.**

Not:

> “80% cheaper.”

## Gate amendment candidate — not retroactively scored

Do not change the v0 score. For a future v1 holdout, add a trigger for:

```text
DOWNSTREAM_SCHEMA_USE
```

Possible condition:

> If the answer defines a taxonomy, rubric, state model, metric, schema, classification system or decomposition that will be reused to score/route/prioritize later decisions, treat the framing itself as consequential and consider calibration even when the immediate prompt looks conceptual.

This is a candidate derived from one failure and must not be promoted without neighboring controls; otherwise it could over-escalate ordinary conceptual questions.

## Decision against the hypothesis

### Front-door gate as routing optimization
`SUPPORTED_ENOUGH_FOR_PROSPECTIVE_V1_TEST`

### Front-door gate as separate epistemic/product reasoning engine
`NOT_SUPPORTED_BY_THIS_EXPERIMENT`

### Safe deployment in front of R&D now
`NOT_YET`

Reason: a 6.25% false-bypass rate on this small same-model retrospective sample is too high to place the gate in authority over the full loop without shadowing.

## Next evidential step

Run v1 in shadow mode on **new prompts prospectively**, with:
- gate output frozen immediately when the prompt arrives;
- full R&D shadow run regardless of gate decision;
- no access to later conversation outcomes during either run;
- latency/token/invocation counts measured separately;
- SG-17-style `DOWNSTREAM_SCHEMA_USE` cases deliberately included as challenge controls.

Promotion criterion should be set before the run. A plausible strict initial target:
- false-bypass <= 2%;
- material-case recall >= 95%;
- full-loop bypass >= 40%;
- zero authority violations;
- measurable net token/latency reduction.

Thresholds are candidate engineering targets, not empirically established product requirements.