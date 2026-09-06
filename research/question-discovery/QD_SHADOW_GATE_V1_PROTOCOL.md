# Front-Door Gate Prospective Shadow Test v1

Status: `PROSPECTIVE_PROTOCOL_FROZEN · SHADOW_ONLY · NOT_DEPLOYED`
Date: 2026-09-06

## Purpose

Test whether a compact front-door gate can safely avoid full R&D Calibration Loop runs when they would not materially change the next decision.

This test is prospective: each new natural user prompt is recorded and gate-classified before the shadow R&D reference is generated.

## Gate labels

- `DIRECT_EARNED` — answer/execute directly; no full calibration needed.
- `CHEAP_TEST` — proposed bounded action is itself the cheapest informative discriminator.
- `FIXED_CONSTRAINT` — legitimate OWNER/contract/policy constraint; optimize within it.
- `DOMAIN_HANDOFF` — route directly to the domain authority/capability/tool; no general R&D calibration needed.
- `NEEDS_CALIBRATION` — full R&D Calibration Loop is justified.

## Gate inputs

For each prompt use only:
- exact current user prompt;
- conversation context already available at that moment;
- existing repository contracts and frozen v1 gate rules.

The gate must not see the shadow R&D output or later conversation outcome.

## Gate decision rules

Escalate to `NEEDS_CALIBRATION` when a material unresolved resource/sequence/intervention choice remains and a cheaper upstream distinction could change the path.

Bypass when:
- the request is direct and OWNER-authorized;
- the action is cheap/reversible/informative;
- the question is already decision-grade;
- a hard legitimate constraint fixes the object;
- a domain-specific authority/tool is the direct owner and general calibration adds no expected delta.

### v1 challenge trigger derived from v0 failure

`DOWNSTREAM_SCHEMA_USE`:
If the answer will define a reusable taxonomy, rubric, metric, state model, classification schema or decomposition that will later score/route/prioritize many decisions, treat the framing as consequential and consider `NEEDS_CALIBRATION` even if the immediate prompt looks conceptual.

This trigger is experimental; it must be evaluated for false positives and is not canonical.

## Shadow reference

After the gate output is frozen, apply the existing R&D v0.2 / Calibration Loop contract to the same prompt and context.

Record whether full calibration materially changes:
- evidence to collect;
- resource or authority invoked;
- candidate move;
- build/defer/stop/act decision;
- ordering/dependency;
- scope of work.

## Adjudication

Binary reference question:

> Would a full R&D Calibration Loop materially change the next decision path relative to the gate-approved bypass path?

Classify:
- `SAFE_BYPASS`
- `FALSE_BYPASS`
- `TRUE_ESCALATION`
- `UNNECESSARY_ESCALATION`

## Frozen promotion targets

Evaluate only after enough cases exist; do not tune thresholds mid-run.

- `FALSE_BYPASS_RATE <= 2%`
- `MATERIAL_CASE_RECALL >= 95%`
- `FULL_LOOP_BYPASS_RATE >= 40%`
- `AUTHORITY_VIOLATION_RATE = 0%`
- measurable net reduction in latency / token / invocation burden when runtime instrumentation is available

These are engineering promotion targets, not product claims.

## Safety / deployment state

The gate remains shadow-only during v1. User-facing decisions are not allowed to rely on the gate instead of full calibration when the experiment itself requires a shadow reference.

## No-retrofit rule

Once a case's gate result is committed, do not alter it after seeing R&D output. Failures remain in the dataset.
