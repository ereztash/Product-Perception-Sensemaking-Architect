# Evidence-Bounded Peer-Agent System

This repository contains a peer-agent architecture under one shared epistemic constitution.

## Canonical rule

> **`main` is the only source of truth.**

Historical branches are lineage only. No decision-relevant research result, prompt rule, contract or runtime may live only on a side branch.

See `docs/REPOSITORY_MAP.md` for the canonical repository map and branch policy.

## System architecture

```text
                         OWNER / TELOS
                              |
                      CALIBRATION LOOP
                    deterministic routing
                    /                 \
                 NETA                 R&D
          product/design         resource↔telos
           sensemaking            calibration
                    \                 /
                 SHARED EPISTEMIC KERNEL
                    constitution only

External resource when useful:
SCAFFOLD = broad reasoning borrowed, not ground truth
```

Neta and R&D are peers. Call order does not create hierarchy.

A learned Orchestrator is **not built**. It must be justified by repeated coordination failures that the deterministic Calibration Loop cannot handle cheaply.

## Shared unit of progress

> **Progress = material uncertainty removed from a live decision.**

Not code written, sources collected, instruments created, agents added or prompts expanded.

## Shared Epistemic Kernel

The shared kernel carries cross-agent constraints such as:

`Claim → Evidence → Reality → Resolution Authority → Requested Use → Permission → Reversal / Stop`

Key files:

- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `docs/AGENT_AUTHORITY_BOUNDARIES.md`
- `docs/PEER_HANDOFF_PROTOCOL.md`
- `docs/REALITY_AUTHORITY_PERMISSION.md`
- `schemas/epistemic-claim.schema.json`
- `schemas/peer-handoff.schema.json`

Resolution authorities are `OWNER`, `REPO`, `ENVIRONMENT`, `RESEARCH`, and `FIELD`.

## Peer 1 — Neta

Neta turns raw product/design intuition into a bounded distinction without letting interpretation outrun evidence.

```text
RAW SIGNAL
→ CONCRETE MOMENT
→ OBSERVABLE
→ COMPETING MECHANISMS
→ CHEAP DISCRIMINATOR
→ DESIGN DISTINCTION
→ INTERVENTION / DEFER / FIELD
```

Canonical files:

- `prompts/SYSTEM.md` — frozen v0.1 prompt comparator
- `docs/NETA_ASSURANCE_THESIS.md`
- `docs/METHOD.md`
- `schemas/finding.schema.json`
- `eval/CAPABILITY_UPDATE_GATE_V1.md`

Neta is not a research authority and cannot manufacture FIELD evidence.

## Peer 2 — R&D

R&D now has two intentionally separate versions:

### v0.1 — frozen comparator

Research-continuity focused:

`LIVE CLAIM → RECOVER → REUSE/ADAPT/BUILD → RUN → DEPOSIT → CLAIM DISPOSITION → STOP/HANDOFF`

Files:

- `prompts/RND_AGENT_V0_1.md`
- `research/RND_AGENT_CHARTER_V0_1.md`
- `schemas/rnd-research-task.schema.json`
- `eval/rnd-agent/`

### v0.2 — candidate telos

Not yet promoted as validated.

> **Improve the fit between system resources and the live telos, given the actual current state.**

```text
TELOS
+ CURRENT STATE
+ AVAILABLE RESOURCES
→ BOTTLENECK / MISCALIBRATION
→ CANDIDATE RESOURCE MOVES
→ CHEAPEST DECISION-CHANGING LEARNING
→ OBSERVED DELTA
→ RECALIBRATE
→ UPDATED STATE
```

Files:

- `prompts/RND_AGENT_V0_2_CANDIDATE.md`
- `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`

Research is one instrument of R&D, not its top-level telos.

## Calibration Loop

`runtime/calibration_loop/` is the current coordination layer.

It is deliberately **not an agent**.

```text
TASK
 ↓
R&D DIAGNOSE
 ↓
DETERMINISTIC ROUTING
 ├─ NETA       only on discrimination/proxy/intervention triggers
 ├─ SCAFFOLD   only when broad reasoning is worth borrowing
 └─ OWNER/REPO/ENVIRONMENT/FIELD handoff when required
 ↓
R&D SYNTHESIZE
 ↓
TRACE + RESOURCE DELTAS + LEARNING RECORD
```

Key files:

- `runtime/calibration_loop/run.py`
- `runtime/calibration_loop/routing.py`
- `runtime/calibration_loop/README.md`
- `schemas/calibration-task.schema.json`
- `fixtures/calibration-valid-task.json`
- `scripts/check_calibration_loop.py`

The runner may record a proposed routing change. It may not self-modify the routing law from one attractive case.

## Repository structure

```text
docs/       canonical architecture, authority, method and repository map
prompts/    frozen/candidate agent prompts and scaffold prompts
schemas/    shared + peer + runtime contracts
runtime/    executable coordination/adapters/traces
research/   current research lineage and syntheses
eval/       independent agent evaluation/promotion lanes
fixtures/   test cases
scripts/    executable validators and CI checks
memory/     bounded owner-language priors
archive/    historical lineage only; never current authority
```

## Branch policy

- `main` = only canonical long-lived branch.
- work branches = temporary, one named purpose.
- before retirement, useful artifacts must be merged to `main` or archived under `archive/`.
- branch existence never proves current runnability or authority.

The 2026-09-05 branch consolidation is documented at:

- `archive/legacy-branches/BRANCH_MANIFEST_2026-09-05.md`

## Current next experiment

`CAL-ARCH-001` asks:

> **What is the smallest evidence-backed Architecture Agent capability and evaluation contract worth building next?**

The intended first pass is manual/independent:

1. R&D v0.2 diagnosis;
2. Neta pass without seeing the other outputs;
3. scaffold pass without seeing the other outputs;
4. R&D synthesis of the deltas;
5. only then decide whether an Architecture Agent capability is earned.

## Current status

**ONE CANONICAL MAIN · TWO PEERS · SHARED EPISTEMIC KERNEL · DETERMINISTIC CALIBRATION LOOP · R&D v0.2 CANDIDATE · ORCHESTRATOR DEFERRED.**
