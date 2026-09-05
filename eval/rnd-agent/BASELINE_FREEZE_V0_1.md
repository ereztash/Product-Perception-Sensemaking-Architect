# R&D Agent v0.1 Baseline Freeze

Status: `FROZEN_PRE_OSS_TRANSFER_BASELINE`

Freeze date: 2026-09-05

## Tested baseline

- prompt path: `prompts/RND_AGENT_V0_1.md`
- prompt blob SHA: `bc0e725d0449478d53b93bb6643d24404c22708c`
- runtime schema: `schemas/rnd-research-task.schema.json`
- semantic validator: `scripts/validate_rnd_task.py`
- charter source: `research/RND_AGENT_CHARTER_V0_1.md`
- eval protocol: `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`

## Contamination boundary

This baseline is intentionally a direct operationalization of the already-canonical R&D charter and runtime contract.

The targeted open-source transfer study began in parallel, but **no OSS-derived architecture pattern is permitted to modify this baseline before the baseline receives its own TRAIN/ADVERSARIAL/HOLDOUT readout**.

In particular, the baseline does not add any of the following merely because they appear in external systems:

- tree/graph search;
- global experience memory;
- specialized multi-agent roles;
- checkpoint orchestration;
- literature-RAG subsystems;
- critic/reviewer agents;
- search-branch fusion;
- automatic report-writing pipelines.

Any such pattern must enter as a candidate intervention with a named R&D failure family, neighboring non-fire case, expected information/cost benefit and post-baseline evaluation.

## Freeze rule

Do not edit `prompts/RND_AGENT_V0_1.md` in place.

If evidence later earns a repair:

1. retain this blob SHA as comparator;
2. create a new versioned prompt/implementation;
3. name the clean failure it repairs;
4. preserve the red target and green neighbor;
5. run unseen HOLDOUT and regression checks under the R&D-specific promotion gate.

## What this freeze establishes

It establishes a reproducible comparator only.

It does not establish that the R&D Agent is effective, that the prompt is sufficient, or that the runtime contract is complete.
