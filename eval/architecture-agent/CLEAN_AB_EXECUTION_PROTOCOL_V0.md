# Architecture Clean A/B Execution Protocol v0

Status: `FROZEN_BEFORE_LIVE_RUN · VISIBLE_TRAIN_ONLY · NO_AGENT_PROMOTION`
Date: 2026-09-06

## Decision under test

Does `ARCHITECTURE_DECISION_DISCRIMINATOR_V0` add material decision value beyond the strongest current composed baseline?

This run is **not** allowed to promote an autonomous Architecture Agent. It can only decide whether an unseen HOLDOUT is worth buying.

## Frozen corpus

- runner-visible: `HISTORICAL_CASES_V0.jsonl`
- adjudication-only after runner freeze: `HISTORICAL_GOLD_V0.jsonl`
- 12 retrospective visible TRAIN cases

## Comparison

### A — current composed baseline

The same clean model receives:
- the frozen R&D core;
- the strongest current R&D scope override: R&D owns whether/how/how much learning/evidence is worth buying, not structural architecture selection;
- the frozen External Reasoning Scaffold core;
- the case only.

### B — Architecture challenger

Identical to A, plus:
- `ARCHITECTURE_DECISION_DISCRIMINATOR_V0`.

The challenger does **not** receive the baseline output.

Both A and B return the same neutral serialization schema so the adjudicator cannot rely on output shape to identify the challenger.

## Isolation

Runner model calls are stateless Responses API calls with:
- no web tool;
- no repository/file tools;
- no conversation context;
- no source repository name;
- no historical resolution;
- no GOLD.

The benchmark process must write and hash all 24 runner outputs before opening `HISTORICAL_GOLD_V0.jsonl`.

The freeze artifact is:

`FREEZE_MANIFEST_BEFORE_GOLD.json`

plus its SHA-256 digest.

## Blind adjudication

After runner outputs are frozen:

1. GOLD may be read.
2. Baseline and challenger outputs are mapped deterministically to `Response X` / `Response Y`.
3. The judge receives case + GOLD context + X + Y, but not which is baseline/challenger.
4. The judge scores pairwise decision delta.
5. Only after judge output is frozen does the script reveal the X/Y mapping.

Historical resolution is explicitly `CONTEXT_NOT_ANSWER_KEY`.

## Delta dimensions

No composite architecture score is used.

- `BOUNDARY_DELTA`
- `AUTHORITY_DELTA`
- `OPTION_DELTA`
- `DISCRIMINATOR_DELTA`
- `MIGRATION_DELTA`
- `ANTI_BUILD_DELTA`
- `HARM`

A vocabulary/clarity improvement without a material decision-path change is not a win.

## Frozen case-family map

Used only to decide whether wins repeat across more than one architecture family:

- `COORDINATION_BOUNDARY`: 001, 004, 005
- `RUNTIME_DEPLOYMENT`: 002, 007
- `STATE_AUTHORITY_LINEAGE`: 003, 010, 011, 012
- `KNOWLEDGE_CODE_BOUNDARY`: 006, 008
- `SHARED_INFRASTRUCTURE`: 009

## Frozen TRAIN continuation rule

Proceed to an unseen HOLDOUT only if all are true:

1. Architecture is the **material winner** in at least **2** cases.
2. Those wins span at least **2** frozen case families.
3. Architecture material wins are **strictly greater** than baseline material wins.
4. Architecture is judged `HARM` in at most **1** case.

If the rule fails: `STOP_OR_REVISE_BEFORE_HOLDOUT`.

If the rule passes: `CONTINUE_TO_UNSEEN_HOLDOUT`.

Passing this rule is **not** agent promotion.

## Limitations frozen before run

- Retrospective TRAIN, not unseen HOLDOUT.
- Historical resolution is not proof of optimality.
- Runner and judge may use the same model family; blind labeling reduces but does not remove evaluator bias.
- The composed baseline tests capability content, not every routing/runtime overhead of the live Calibration Loop.
- Any future HOLDOUT must be frozen after this challenger contract and continuation rule are fixed.
