# Yishumi Holdout v0 — Adjudication

Status: `HISTORICAL_HOLDOUT_SIGNAL · MECHANICAL_SELECTION · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06
Corpus: `QD_YISHUMI_HOLDOUT_V0_FROZEN.md`
Gate: `QD_YISHUMI_HOLDOUT_V0_GATE.md`
Shadow R&D: `QD_YISHUMI_HOLDOUT_V0_RND.md`

## Per-case adjudication

| Case | Gate | R&D material delta? | Result |
|---|---|---:|---|
| YH-01 | DIRECT_EARNED | NO | SAFE_BYPASS |
| YH-02 | DIRECT_EARNED | NO | SAFE_BYPASS |
| YH-03 | DOMAIN_HANDOFF | NO | SAFE_BYPASS |
| YH-04 | DOMAIN_HANDOFF | NO | SAFE_BYPASS |
| YH-05 | DIRECT_EARNED | NO | SAFE_BYPASS |
| YH-06 | NEEDS_CALIBRATION | YES | TRUE_ESCALATION |
| YH-07 | NEEDS_CALIBRATION | YES | TRUE_ESCALATION |
| YH-08 | NEEDS_CALIBRATION | YES | TRUE_ESCALATION |
| YH-09 | NEEDS_CALIBRATION | YES | TRUE_ESCALATION |
| YH-10 | NEEDS_CALIBRATION | YES | TRUE_ESCALATION |
| YH-11 | NEEDS_CALIBRATION | NO | **UNNECESSARY_ESCALATION** |
| YH-12 | DIRECT_EARNED | NO | SAFE_BYPASS |
| YH-13 | DIRECT_EARNED | NO | SAFE_BYPASS |
| YH-14 | CHEAP_TEST | NO | SAFE_BYPASS |
| YH-15 | DIRECT_EARNED | NO | SAFE_BYPASS |
| YH-16 | NEEDS_CALIBRATION | YES | TRUE_ESCALATION |
| YH-17 | DOMAIN_HANDOFF | NO | SAFE_BYPASS |
| YH-18 | NEEDS_CALIBRATION | YES | TRUE_ESCALATION |
| YH-19 | DOMAIN_HANDOFF | NO | SAFE_BYPASS |
| YH-20 | NEEDS_CALIBRATION | YES | TRUE_ESCALATION |

## Metrics

### FULL_LOOP_BYPASS_RATE
Gate proposed bypass on 11/20 cases.

**55%**

### FALSE_BYPASS_RATE
Among 11 bypasses, shadow R&D materially changed the path in 0 cases.

**0/11 = 0%**

### MATERIAL_CASE_RECALL
Shadow R&D found 8 material calibration cases; gate escalated all 8.

**8/8 = 100%**

### UNNECESSARY_ESCALATION_RATE
Gate escalated 9 cases; one received no material R&D delta.

**1/9 = 11.1%**

### NON-MATERIAL BYPASS SPECIFICITY
There were 12 non-material cases; gate bypassed 11.

**11/12 = 91.7%**

### OVERALL ROUTING AGREEMENT
19/20 cases agree with the binary reference `full calibration needed?`.

**95%**

### AUTHORITY VIOLATION RATE
No observed case reopened a settled owner/contract constraint on a bypass path.

**0/20 observed**

## Promotion-target comparison

Frozen v1 engineering targets from the prospective protocol:
- false-bypass <= 2% → **PASS on this historical holdout (0%)**
- material-case recall >= 95% → **PASS (100%)**
- full-loop bypass >= 40% → **PASS (55%)**
- authority violations = 0 → **PASS observed**
- measurable net latency/token/invocation reduction → **NOT MEASURED**

Because this is a historical holdout rather than prospective traffic and uses same-model manual adjudication, these passes do not authorize deployment.

## Failure analysis — YH-11

The gate over-escalated the reusable pedagogical-presentation template because `DOWNSTREAM_SCHEMA_USE` interpreted reuse as consequential framing.

But the row already contains explicit OWNER-set artifact and technical requirements:
- interactive pedagogical presentation;
- HTML output;
- Tailwind / JS;
- RTL;
- interaction and navigation expectations.

Full R&D should respect those as accepted constraints and let pedagogical/domain reasoning execute inside them.

Failure mechanism:

```text
REUSABLE TEMPLATE
→ gate sees propagation risk
→ escalates
BUT
OWNER ALREADY FIXED THE PRODUCT SURFACE / CONSTRAINTS
→ calibration adds ceremony, not decision delta
```

## Candidate v1.1 refinement — not retroactively scored

`DOWNSTREAM_SCHEMA_USE` should not escalate merely because an artifact/template is reusable.

A stronger trigger would require both:

```text
REUSABLE CONTROL STRUCTURE
AND
ONE OR MORE OPEN DECISION AXES EMBEDDED AS IF SETTLED
```

Examples of open axes:
- arbitrary metric/score used downstream;
- source/evidence hierarchy treated as universally valid;
- causal/intervention ownership fixed without evidence;
- forced decomposition/persona/sequence that may alter decisions;
- inferred latent traits encoded as durable policy.

If the reusable template merely operationalizes explicit OWNER constraints, prefer bypass/domain execution.

This refinement is a hypothesis generated from one holdout failure and must be tested on neighboring cases before promotion.

## What this holdout adds

Compared with the earlier hand-assembled retrospective test, this corpus was:
- external to the repo;
- created long before the gate hypothesis;
- selected mechanically from sheet order;
- heterogeneous in purpose and complexity.

The result therefore weakens the cherry-picking concern while preserving one clear false-positive failure.

Current status:

`FRONT_DOOR_GATE_HYPOTHESIS: STRENGTHENED_BY_MECHANICAL_HISTORICAL_HOLDOUT`

`SAFE_DEPLOYMENT: NOT_YET`

`SEPARATE_EPISTEMIC_ENGINE: STILL_NOT_SUPPORTED`

## Next step

Keep the prospective v1 stream unchanged. Do not edit its frozen rules mid-run.
Use the Yishumi result only to define a future v1.1 candidate after enough prospective cases accumulate.