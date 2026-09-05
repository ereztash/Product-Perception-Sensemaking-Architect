# Canonical Repository State

Last consolidated: 2026-09-05

## Repository authority

`main` is the only canonical branch.

Historical branch names may remain visible because the connected GitHub tool used during cleanup could move refs but could not delete them. As of this consolidation pass, **every visible branch ref points to the same commit as `main`**.

Historical pre-cleanup branch tips and dispositions are preserved at:

- `archive/legacy-branches/BRANCH_MANIFEST_2026-09-05.md`

Repository organization rules are canonical at:

- `docs/REPOSITORY_MAP.md`

A question that requires opening an old branch to discover current truth indicates repository-organization failure.

## Canonical architecture

The system currently contains two peer agents/methods under a shared epistemic constitution plus one deterministic coordination runtime:

- **Neta** — Product Perception & Sensemaking;
- **R&D Agent** — resource↔telos calibration with research continuity as a sub-capability;
- **Calibration Loop** — deterministic routing/runtime, not an agent and not a truth authority.

External broad reasoning may be borrowed through `SCAFFOLD`.

```text
                         OWNER / TELOS
                              |
                      CALIBRATION LOOP
                    deterministic routing
                    /                 \
                 NETA                 R&D
           product/design        resource↔telos
            sensemaking           calibration
                    \                 /
                 SHARED EPISTEMIC KERNEL
```

A learned Orchestrator remains deferred.

## Shared constitutional decision

Across peers:

> **material uncertainty removed from a live decision** is the unit of progress.

Resolution authority belongs to claims, not agents.

Canonical shared artifacts:

- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `docs/AGENT_AUTHORITY_BOUNDARIES.md`
- `docs/PEER_HANDOFF_PROTOCOL.md`
- `docs/REALITY_AUTHORITY_PERMISSION.md`
- `schemas/epistemic-claim.schema.json`
- `schemas/peer-handoff.schema.json`

## Neta canonical identity

Neta remains an evidence-bounded Product Perception & Sensemaking method with an assurance layer.

- method state: **v0.2 assurance re-foundation**;
- prompt comparator: **frozen v0.1** at `prompts/SYSTEM.md`;
- capability promotion: `eval/CAPABILITY_UPDATE_GATE_V1.md`.

Neta turns:

`RAW SIGNAL → CONCRETE MOMENT → OBSERVABLE → COMPETING MECHANISMS → CHEAP DISCRIMINATOR → DESIGN DISTINCTION → INTERVENTION / DEFER / FIELD`

Neta does not own research validity, architecture doctrine or FIELD outcomes.

## R&D canonical identity

R&D now has two intentionally separate states.

### R&D v0.1 — frozen comparator

Research-continuity focused.

Canonical comparator artifacts:

- `prompts/RND_AGENT_V0_1.md`;
- frozen prompt blob: `bc0e725d0449478d53b93bb6643d24404c22708c`;
- `research/RND_AGENT_CHARTER_V0_1.md`;
- `schemas/rnd-research-task.schema.json`;
- `scripts/validate_rnd_task.py`;
- `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`;
- `eval/rnd-agent/TRAIN_CONTROLS_V0_1.jsonl`.

Its continuity distinction remains useful:

`instrument ≠ run ≠ durable evidence ≠ decision effect`

plus:

`historical evidence ≠ current runnability`, `null ≠ refuted`, `pending ≠ failed`, `agreement ≠ independent triangulation`.

### R&D v0.2 — candidate telos

Status: `CANDIDATE_NOT_VALIDATED`.

Canonical candidate artifacts:

- `prompts/RND_AGENT_V0_2_CANDIDATE.md`;
- `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`.

Telos:

> **Improve the fit between the system's resources and its telos, given the state from which the system is actually starting.**

Loop:

`TELOS + CURRENT STATE + RESOURCES → BOTTLENECK/MISCALIBRATION → CANDIDATE MOVES → CHEAPEST DECISION-CHANGING LEARNING → OBSERVED DELTA → RECALIBRATE → UPDATED STATE`

Research is one instrument of this telos; it is not the telos itself.

The v0.2 candidate has not been promoted as validated merely because it is used by the Calibration Loop.

## Calibration Loop canonical identity

Status: `IMPLEMENTATION_CANDIDATE / CI-GATED`.

Canonical artifacts:

- `runtime/calibration_loop/README.md`;
- `runtime/calibration_loop/run.py`;
- `runtime/calibration_loop/routing.py`;
- `runtime/calibration_loop/adapters.py`;
- `schemas/calibration-task.schema.json`;
- `scripts/validate_calibration_task.py`;
- `scripts/check_calibration_loop.py`;
- `fixtures/calibration-valid-task.json`.

Flow:

`R&D DIAGNOSE → deterministic routing → Neta/Scaffold/authority as triggered → R&D SYNTHESIZE → trace + resource deltas + learning record`

Routing rules are inspectable and are not self-modified from one case.

The runtime may stop at `PENDING_RESOURCE`, `AUTHORITY_STOP` or `FAILED_EXECUTION` rather than fabricate an answer.

## First manual Calibration Loop run

`CAL-ARCH-001` was executed manually on 2026-09-05 without API/model adapters.

Artifact:

- `runtime/calibration_loop/traces/CAL-ARCH-001-MANUAL-2026-09-05.md`

Important limitation:

R&D, Neta and Scaffold were role-separated but executed in one ChatGPT session/foundation-model lineage. Their agreement is therefore **not independent triangulation**.

The run produced a material decision change:

From:

> build/define an Architecture Agent

To:

> first test whether a distinct architecture-specific decision capability exists and adds value beyond R&D + Scaffold + REPO/ENVIRONMENT evidence.

## Architecture capability state

The first architecture-specific candidate is:

- `research/architecture-agent/ARCHITECTURE_DECISION_DISCRIMINATOR_V0.md`

Status: `CANDIDATE_CAPABILITY_NOT_AGENT`.

Candidate unit:

`LIVE ARCHITECTURE DECISION → CURRENT STRUCTURE/AUTHORITY → 2–3 COMPETING OPTIONS/MECHANISMS → CONSTRAINTS/INVARIANTS → MATERIAL DEPENDENCY/FAILURE/CHANGE PATH → CHEAP DISCRIMINATOR → BOUNDED DECISION → MIGRATION/REVERSAL`

First visible controls:

- `eval/architecture-agent/TRAIN_CONTROLS_V0.jsonl`

No autonomous Architecture Agent prompt/implementation is canonical yet.

Promotion question:

> Does the architecture-specific decision contract change material decisions more cheaply/reliably than the existing combination of R&D + Scaffold + REPO/ENVIRONMENT evidence?

If not, architecture expertise should remain a borrowed resource rather than become a new peer.

## Neta empirical state

GitHub Benchmark Wave 1 remains frozen/closed at broad-sampling saturation:

- 48 adjudicated repositories;
- 16 HOLDOUT repositories;
- 14 fully surviving Neta-vs-baseline decision deltas;
- 8 partially supported deltas;
- 1 clean Neta failure;
- 0 new core rules promoted;
- 0 Neta prompt updates.

Closure means low marginal gain from more routine GitHub sampling, not validated universal reliability.

## R&D targeted OSS state

The R&D targeted OSS lane is closed at architecture saturation for routine sampling.

The strongest residual candidate needs remain:

1. attempt/result-selection provenance;
2. stochastic stability where variance is material;
3. execution environment/model/tool identity;
4. trace-level protocol integrity;
5. dependency-safe claim/experiment/finding state;
6. checkpoint/rollback semantics;
7. structured recovery of prior attempts/failures.

These remain challenger hypotheses until a discriminating failure earns them.

## Historical branch consolidation

The branch audit found:

- most historical branches were already strict ancestors of `main`;
- `neta/v0.1-agent-contract` diverged historically but its core artifacts are superseded on `main`;
- `research/wave1-evidence-pass1` held three research documents not present on `main`.

Those unique documents were copied exactly into:

- `archive/legacy-branches/research-wave1-evidence-pass1/PROMPT_GAP_AUDIT.md`;
- `archive/legacy-branches/research-wave1-evidence-pass1/RECURSION_LOG.md`;
- `archive/legacy-branches/research-wave1-evidence-pass1/WAVE1_RESULTS_PASS1.md`.

All visible branch refs were then normalized to the canonical `main` commit.

## Current next authorized execution

### Neta

- keep `prompts/SYSTEM.md` frozen until Neta-specific evidence earns change;
- continue only decision-changing Neta evaluation/research lanes;
- do not take over R&D or architecture authority.

### R&D

- keep v0.1 as frozen comparator;
- treat v0.2 as candidate until evidence earns promotion;
- use real tasks to learn which resources materially change decisions;
- do not equate repeated Scaffold/Neta agreement under shared model lineage with independent evidence.

### Architecture candidate

1. recover 8–15 historical architecture decisions from existing repos;
2. freeze task inputs;
3. compare current baseline resources against `ARCHITECTURE_DECISION_DISCRIMINATOR_V0`;
4. run visible controls;
5. use targeted architecture OSS/literature only where a named distinction remains unresolved;
6. create unseen HOLDOUT before autonomous Architecture Agent implementation.

### Orchestrator

Do not build yet.

Evidence that could earn an orchestrator includes repeated:

- ambiguous ownership among stable peers;
- lost dependencies across peer handoffs;
- contradictory peer outputs that deterministic routing cannot resolve cheaply;
- material routing overhead that harms decision quality/cost.
