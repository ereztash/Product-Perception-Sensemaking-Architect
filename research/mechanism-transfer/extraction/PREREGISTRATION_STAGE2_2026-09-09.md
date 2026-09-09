# Autonomous Mechanism Extraction — Stage 2 preregistration

Status: `PREREGISTERED_NOT_RUN`
Date: 2026-09-09
Stage 1 result: `ADVANCE_TO_REPLICATION` with structured +3.5 GOLD_RECALL_POINTS on lichess_app.

## Decision

Test whether the Stage 1 structured reverse-engineering advantage replicates out-of-sample when the structured prompt is frozen unchanged on source systems that did not contribute to its design.

Current default: **do not build an autonomous mechanism extractor**.

## Frozen prompts

The exact Stage 1 prompt files are reused without modification:
- `ARM_S_STRUCTURED_PROMPT.txt`
- `ARM_B_BASELINE_PROMPT.txt`

No new domain-specific instruction may be added to either arm.

## Sources

### Source L — Lessons / Genesis runtime

Repository: `ereztash/lessons`
Frozen commit: `252f1446582afa5e627bc397dae516399dc49b75`
Code-only extraction surface: `saas/app/scripts/genesis/` plus package/config files only if needed for interpretation.
Docs, specs, README, tests, research and git history are removed before extraction.

### Source R — Product-Perception Calibration runtime

Repository: `ereztash/Product-Perception-Sensemaking-Architect`
Frozen pre-extraction commit: `8a6e63c5118a6082e396dbffdaa9e8c40f2de1ad`
Code-only extraction surface: `runtime/calibration_loop/`, `scripts/validate_calibration_task.py`, and existing machine-readable contracts/schemas when present.
README, docs, prompts, research, tests and git history are removed before extraction.

## Gold

Each source has an 8-target hidden gold frozen from documentation that predates Stage 2. Gold is limited to preservation-worthy mechanisms expected to leave traces in the supplied production/runtime code.

The gold files are never copied into either extraction directory.

## Replications

For each source, run two independent paired comparisons (`replicate=1,2`).

Each paired comparison:
- same sanitized snapshot for both arms;
- same Copilot CLI/provider-default lineage;
- one extraction run per arm;
- randomized candidate mapping;
- identical output schema and maximum 12 items;
- deterministic path/leakage integrity checks;
- three blinded semantic judges;
- per-target median score 0/0.5/1;
- primary score = sum of eight target medians.

Total: four paired comparisons across two source systems.

## Primary comparison

For pair i:

`PAIRED_ADVANTAGE_i = structured GOLD_RECALL_POINTS - baseline GOLD_RECALL_POINTS`.

A pair is a structured win only when `PAIRED_ADVANTAGE_i > 0` and both arms pass source-isolation integrity.

## Decision rule frozen before execution

### `BUILD_REVERSIBLE`
Earned only if all are true:
1. structured wins at least **3 of 4** paired comparisons;
2. median paired advantage across all four pairs is **>= 1.5** GOLD_RECALL_POINTS;
3. median paired advantage is **> 0 on Source L and > 0 on Source R** separately;
4. no structured run has source-isolation leakage or invalid evidence-path integrity failure;
5. median unsupported-mechanism count for structured is not more than 1 greater than baseline across the four pairs.

This authorizes only a bounded extractor prototype around the frozen structured protocol. It does not establish general-purpose software synthesis.

### `ADAPT`
If structured shows a positive but inconsistent/localized advantage — e.g. wins 2/4, succeeds on one source but not the other, or median advantage is 0.5–1.0 — freeze the source-specific misses before changing the protocol.

### `STOP_EXTRACTION_UNIQUE_DELTA_UNSHOWN`
If structured wins <=1/4, median advantage <=0, or the apparent advantage depends on leakage/invalid paths/judge failure.

## Anti-overfitting rule

No prompt wording, category, output schema, judge rubric, source subset or gold target may be changed after any Stage 2 extraction output is observed. Any such change constitutes a new experiment.

## Stopping rule

Stop after these four pairs. Do not add a fifth source or extra repetitions merely to rescue a weak result. The frozen decision rule decides current resource allocation.
