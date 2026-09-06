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
                              |
                 DECISION→EXECUTION TRACE
                              |
                    REPO / ENV / FIELD
                              |
                         R&D LEARNING
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
- `docs/DECISION_EXECUTION_LEARNING_LOOP.md`
- `schemas/epistemic-claim.schema.json`
- `schemas/peer-handoff.schema.json`
- `schemas/decision-execution-learning.schema.json`

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

## Decision → Execution → Learning contract

Status: `CROSS_AGENT_EXECUTION_CONTRACT_V0_1 / CI-GATED`.

The system now carries an explicit non-agent bridge from bounded decision to reality:

`DECISION → EXECUTION → VERIFIED STATE → OUTCOME → LEARNING`

Canonical artifacts:

- `docs/DECISION_EXECUTION_LEARNING_LOOP.md`;
- `schemas/decision-execution-learning.schema.json`;
- `scripts/validate_decision_trace.py`;
- `fixtures/decision-execution-learning-valid.json`.

The first real trace is:

- `runtime/execution_traces/DEL-ARCH-CORPUS-001.json`.

Its invariant is that `action completed ≠ verified state ≠ measured outcome ≠ learning`. Execution does not inherit REPO, ENVIRONMENT or FIELD authority.

This contract does **not** justify an Execution Agent. A distinct execution capability must be earned by recurring failures across real traces that protocol/tool handoff cannot handle cheaply.

## External-target execution traces

`ereztash/lichess_app` is an external product target worked through this contract rather than a component of this repository. Traces and peer handoffs from that work are canonical here; the product code is not.

- `runtime/execution_traces/DEL-LICHESS-RELEASE-STALE-PR-001.json` — `WAIT_AUTHORITY`, ENVIRONMENT;
- `runtime/execution_traces/DEL-LICHESS-FIELD-INSTRUMENT-001.json` — `STOP`, FIELD;
- `runtime/handoffs/HANDOFF-LICHESS-ENV-001.json`;
- `runtime/handoffs/HANDOFF-LICHESS-FIELD-001.json`;
- `research/lichess-prerelease/PRERELEASE_GAP_PASS_2026-09-06.md` — the readable pass record.

The pass produced one recalibration worth carrying: a debt-register row can be stale in the direction that overstates a gap, and only the live external authority settles which. See the pass record, section 2.

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

Visible historical benchmark program is now frozen:

- `eval/architecture-agent/HISTORICAL_CASES_V0.jsonl` — 12 runner-visible frozen cases across 4 repositories;
- `eval/architecture-agent/HISTORICAL_GOLD_V0.jsonl` — historical adjudication anchors kept separate from runner inputs;
- `eval/architecture-agent/HISTORICAL_BENCHMARK_PROTOCOL_V0.md`;
- `scripts/check_architecture_historical_cases.py` — CI gate enforcing count, repository breadth and CASES/GOLD separation.

The visible corpus is retrospective TRAIN evidence only. Historical implementation is not ground truth and agreement with it is not a score.

No autonomous Architecture Agent prompt/implementation is canonical yet.

Promotion question:

> Does the architecture-specific decision contract change material decisions more cheaply/reliably than the existing combination of R&D + Scaffold + REPO/ENVIRONMENT evidence?

If not, architecture expertise should remain a borrowed resource rather than become a new peer.

Current contamination boundary:

The context that authored/froze `HISTORICAL_GOLD_V0.jsonl` is not eligible to generate countable baseline/candidate benchmark outputs for this corpus. The next countable run must occur in a clean context that can see CASES but not GOLD and must not recover the source commits before outputs are frozen.

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
- start accumulating real `DECISION → EXECUTION → VERIFIED STATE → OUTCOME → LEARNING` traces;
- do not equate repeated Scaffold/Neta agreement under shared model lineage with independent evidence.

### Architecture candidate

Completed:

1. recovered 12 historical architecture decisions from 4 existing repositories;
2. froze runner-visible case inputs separately from historical adjudication anchors;
3. added a CI-gated visible benchmark protocol and corpus validator.

Next:

1. in a clean runner that cannot see GOLD/source resolutions, freeze baseline outputs using current resources without the Architecture Decision Discriminator;
2. freeze candidate outputs on the exact same CASES;
3. reveal GOLD only after both outputs are frozen and adjudicate decision-relevant delta dimensions separately;
4. use visible TRAIN failures to refine the evaluation contract, not to claim promotion;
5. create unseen HOLDOUT after the candidate contract is frozen;
6. only HOLDOUT evidence may earn movement toward an autonomous Architecture Agent.

### Execution capability

Do not build an Execution Agent.

Collect 10-15 real traces using `decision-execution-learning.schema.json`. A distinct execution capability becomes eligible only if repeated traces show the same reasoning/coordination failure between bounded decision and verified state after ordinary protocol/tool handoff is already present.

### Orchestrator

Do not build yet.

Evidence that could earn an orchestrator includes repeated:

- ambiguous ownership among stable peers;
- lost dependencies across peer handoffs;
- contradictory peer outputs that deterministic routing cannot resolve cheaply;
- material routing overhead that harms decision quality/cost.
