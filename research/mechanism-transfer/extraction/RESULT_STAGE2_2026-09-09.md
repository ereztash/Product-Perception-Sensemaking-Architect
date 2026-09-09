# Autonomous Mechanism Extraction — Stage 2 result

Status: `STOP_EXTRACTION_UNIQUE_DELTA_UNSHOWN`
Date: 2026-09-09
Preregistration: `research/mechanism-transfer/extraction/PREREGISTRATION_STAGE2_2026-09-09.md`
Execution commit: `4db7dc41b1fd78ca2f2817eab3dbe8865cab41a2`
GitHub Actions run: `34337649513`

## Why Stage 2 was run

Stage 1 on `lichess_app` produced a +3.5 / 8 GOLD_RECALL_POINTS advantage for the structured extraction protocol. However, that protocol was designed after extensive work on lichess_app and explicitly emphasized categories that overlapped its known mechanisms. Stage 2 therefore froze the structured prompt unchanged and tested it out-of-sample.

## Frozen sources

- Lessons / Genesis runtime: `ereztash/lessons@252f1446582afa5e627bc397dae516399dc49b75`
- Calibration runtime: `ereztash/Product-Perception-Sensemaking-Architect@8a6e63c5118a6082e396dbffdaa9e8c40f2de1ad`

Both extractors received sanitized code-only snapshots with docs, README, research, tests and git history removed. Hidden gold was not available during extraction. Each pair was scored by three blinded judges; per-target medians were aggregated before arm mapping was opened.

## Blind scores before mapping

| Pair | Candidate 1 | Candidate 2 |
|---|---:|---:|
| Lessons r1 | 6.0 | 6.0 |
| Lessons r2 | 7.0 | 6.5 |
| R&D r1 | 8.0 | 8.0 |
| R&D r2 | 8.0 | 7.0 |

All eight candidate outputs passed deterministic integrity checks:
- valid required JSON shape;
- <=12 items;
- zero invalid evidence paths;
- zero forbidden docs/README/tests/research leakage.

Before mapping, the frozen BUILD_REVERSIBLE condition was already impossible because only two pairs were non-ties, while the rule required structured wins in at least 3/4.

## Mapping and paired effects

| Source | Replicate | Structured | Baseline | Structured - Baseline |
|---|---:|---:|---:|---:|
| Lessons | 1 | 6.0 | 6.0 | 0.0 |
| Lessons | 2 | 6.5 | 7.0 | -0.5 |
| R&D runtime | 1 | 8.0 | 8.0 | 0.0 |
| R&D runtime | 2 | 7.0 | 8.0 | -1.0 |

Structured wins: **0 / 4**.
Ties: **2 / 4**.
Structured losses: **2 / 4**.
Median paired advantage: **-0.25** GOLD_RECALL_POINTS.

Per-source median paired advantage:
- Lessons: **-0.25**
- R&D runtime: **-0.5**

Unsupported-mechanism medians did not create a hidden structured advantage: Lessons r1 was 1 for both candidates; the other three pairs were 0 for both candidates.

## Frozen decision rule applied

`STOP_EXTRACTION_UNIQUE_DELTA_UNSHOWN`

The preregistration required STOP when structured won <=1/4 or median advantage <=0. Both conditions are met.

Do not build an autonomous mechanism extractor from the current structured protocol.

## Interpretation

The Stage 1 lichess_app advantage did not replicate when the prompt was held frozen and moved to two out-of-sample codebases. The strongest current explanation is therefore that Stage 1 captured **source/protocol fit** rather than a general unique extraction capability.

The structured protocol's fixed decomposition around state, authority, evidence boundaries, action derivation and persistence was unusually well aligned with lichess_app. On Lessons and the calibration runtime, a strong conventional reverse-engineering request recovered the preservation targets equally well or better.

Concrete examples of the reversal:
- Lessons r2: baseline recovered the source/IR mechanisms at 7.0 while structured scored 6.5; structured partially missed the single-IR/all-artifacts relation and did not recover domain-fixture separation as strongly.
- R&D r2: baseline scored 8.0 while structured scored 7.0; structured only partially recovered full pre-execution task-contract validation and resource/phase-specific semantic adapter validation.

## What this result supports

For the tested capable model/provider and explicit production/runtime codebases, adding the frozen structured reverse-engineering decomposition does **not** currently improve mechanism recovery over a strong ordinary architect prompt.

This is an anti-build finding for the proposed extraction layer.

## What it does not establish

It does not show that all automated reverse engineering is impossible or useless. It shows that the current candidate's claimed unique delta is unearned. New work would need a different source of leverage rather than more iterations of this prompt decomposition.

Possible future hypotheses must be treated as new hypotheses, not reinterpretations of this result — for example selection of the right analogue/source system, multi-repo empirical induction, field-observed failure discovery, or unattended longitudinal assurance. None is supported by this experiment yet.

## Resource decision

**STOP building the mechanism-extraction/compiler path as currently defined.**

Do not add more structured prompt steps, more target domains, or more repetitions to rescue it. Any continuation should begin from a newly specified decision and competing explanation.
