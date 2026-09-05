# H1 Hebrew Signal Fidelity — Independent HOLDOUT Commissioning

Status: `REQUIRED_BEFORE_VALID_H1_RUN`

This document closes the last procedural gap before a valid H1 hidden-HOLDOUT run. It does **not** contain HOLDOUT text or gold labels.

## Why this exists

The repository already contains visible TRAIN examples with visible gold. They are useful for schema/scorer smoke tests and for future training, but they cannot measure unseen generalization.

A valid H1 HOLDOUT must be authored or sampled by an authority that does not expose item text or gold to the tested Neta/baseline context before predictions are frozen.

## Frozen tested system

The authoritative freeze is `eval/hebrew-signal-benchmark/H1_FREEZE.json`.

No H1 run is valid if any of these change after HOLDOUT authoring starts:
- `prompts/SYSTEM.md` blob SHA;
- H1 protocol blob SHA;
- scorer blob SHA;
- strata/count requirements;
- output schema or critical-error definitions.

## Independent authoring roles

Minimum acceptable setup:

1. **HOLDOUT author/adjudicator** — native Hebrew speaker(s) who create or select cases and gold outside the tested model context.
2. **Runner** — receives only item text/context and case IDs, never gold.
3. **Neta pass** — frozen Neta prompt/version.
4. **Baseline pass** — general-review model with identical evidence boundary and no H1 ontology prompt.
5. **Reveal/adjudication** — only after both outputs are frozen.

The same agent that writes the gold may not be treated as an independent blind runner for that item.

## Minimum hidden set

At least 20 cases, satisfying the frozen H1 strata:
- metaphor / analogy: 3
- hedging / mitigation: 2
- hyperbole: 2
- negation / contrast: 2
- Hebrew-English code switching: 3
- irony / pragmatic reading: 2
- affect vs mechanism: 2
- deixis / reference ambiguity: 2
- perceived vs system state: 2

At least 8 cases must combine two or more phenomena.
At least 15 cases in the wave must have all three views:
- natural Hebrew;
- faithful English translation;
- deliberately professionalized English perturbation.

## Pre-run manifest

Before predictions, commit only a manifest containing:
- wave ID;
- authoring authority/provenance category;
- case count;
- stratum counts;
- SHA-256 hash for each hidden case payload;
- SHA-256 hash for the complete hidden gold file;
- timestamp;
- exact tested Neta prompt SHA;
- exact scorer SHA.

Do **not** commit hidden item text or gold before predictions are frozen.

## Gold contract

Each hidden case gold must specify at minimum:
- raw-signal preservation requirement;
- plausible interpretations;
- must-not-infer claims;
- ambiguity present/absent;
- mechanism status;
- authority;
- expected action;
- cheapest discriminator when applicable;
- critical-error conditions;
- reversal condition when material.

Professionalized English is a perturbation, never gold.

## Execution order

1. Independently create/select hidden cases and gold.
2. Hash and commit the pre-run manifest only.
3. Give runner item text/context without gold.
4. Freeze Neta outputs.
5. Freeze baseline outputs.
6. Reveal gold.
7. Run deterministic scorer.
8. Adjudicate material disagreements, including ambiguity/high-disagreement cases.
9. Persist results and failure families.
10. Do not edit Neta until the wave closes or a preregistered stop condition fires.

## What counts as progress

Primary progress is one of:
- a clean Neta Hebrew judgment failure;
- a surviving Neta-vs-baseline decision delta;
- a falsified suspected Hebrew failure family;
- a boundary/counterexample that narrows a rule candidate.

Case count alone is not progress.

## Current blocker

`BLOCKED_ON_INDEPENDENT_HIDDEN_CASE_AUTHORING_AND_GOLD`

This is an evidence requirement, not an engineering defect. Synthetic gold authored by the same evaluating model must not be relabeled as independent HOLDOUT evidence.
