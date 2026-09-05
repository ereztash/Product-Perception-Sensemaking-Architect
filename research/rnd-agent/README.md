# R&D Agent Research Lane

Status: `ACTIVE_PRE_HOLDOUT`

This directory contains research about the peer R&D Agent. It is separate from Neta's Wave 1 research lane and cannot directly modify Neta behavior.

## Canonical R&D behavior/eval references

- charter: `../RND_AGENT_CHARTER_V0_1.md`
- frozen baseline prompt: `../../prompts/RND_AGENT_V0_1.md`
- baseline freeze: `../../eval/rnd-agent/BASELINE_FREEZE_V0_1.md`
- runtime schema: `../../schemas/rnd-research-task.schema.json`
- semantic validator: `../../scripts/validate_rnd_task.py`
- eval protocol: `../../eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`
- OSS-derived eval amendment: `../../eval/rnd-agent/EVAL_AMENDMENT_2026-09-05_OSS.md`

## Targeted OSS transfer

- `OSS_TARGETED_TRANSFER_2026-09-05.md` — architecture extraction and boundaries.
- `OSS_TRANSFER_CLOSEOUT_2026-09-05.md` — saturation decision and next authorized sequence.
- `../../eval/rnd-agent/OSS_CHALLENGER_QUEUE_V0_1.md` — visible/adversarial challengers derived after baseline freeze.

## Current research state

The targeted OSS lane is closed at architecture saturation.

The sample intentionally covered different roles rather than maximizing repository count:

- research/development role split;
- tree/graph exploration;
- phase-specialized multi-agent workflow;
- scientific retrieval/evidence gathering;
- benchmark/runtime reproducibility;
- stochastic long-horizon agent evaluation;
- report/citation evaluation;
- experience memory and cross-branch search;
- self-evolving research organizations.

The strongest residuals are provenance/verification and dependency-safe continuity, not a demonstrated need for more agents.

## Next unit of progress

A frozen-baseline case failure or surviving decision advantage.

Do not add another architecture source unless it can change a named challenger, boundary, fixture or repair decision.
