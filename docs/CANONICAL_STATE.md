# Canonical Repository State

Last consolidated: 2026-09-06 (repository canonicalization and research-state reconciliation)

## How to read this file

Every component below carries exactly one evidence status. The statuses are not interchangeable and this file exists to keep them apart.

| Status | Meaning |
|---|---|
| `CANONICAL` | Current authority. Change it only through its own gate. |
| `IMPLEMENTATION_CANDIDATE` | In use by the system, not validated by evidence. Use does not promote. |
| `RESEARCH_HYPOTHESIS` | Frozen, testable, not yet tested against admissible cases. |
| `DISCOVERY_ONLY` | Generated or sharpened a hypothesis. Contributes zero confirmation. |
| `CONFIRMATION_BLOCKED` | Testable, but the admissible evidence channel does not currently exist. |
| `CLOSED_AT_SATURATION` | Further routine sampling has low marginal value. Not a validity claim. |
| `NOT_EARNED` | Considered and declined on current evidence. |

A component that appears under one status may not be cited under a stronger one elsewhere in the repository.

## Repository authority

`main` is the only canonical branch.

As of this pass, every decision-relevant research artifact produced on `research/system-design-decision-lane-2026-09-06` has been recovered into the canonical lane. The pre-reconciliation state, including exact branch tips, ahead/behind counts and CI conclusions, is recorded at:

- `archive/reconciliation/REPO_STATE_BEFORE_RECONCILIATION_2026-09-06.md`
- `archive/reconciliation/RECONCILIATION_REPORT_2026-09-06.md`

Earlier branch-tip dispositions remain at:

- `archive/legacy-branches/BRANCH_MANIFEST_2026-09-05.md`

Repository organization rules are canonical at:

- `docs/REPOSITORY_MAP.md`

A question that requires opening a side branch to discover current truth indicates repository-organization failure.

### Active branches

Only branches carrying a live, unfinished experiment may remain ahead of `main`:

| Branch | Purpose | State |
|---|---|---|
| `research/architecture-clean-ab-2026-09-06` | protocol-conforming Architecture clean A/B (PR 14) | blocked, see `eval/architecture-agent/EXECUTION_BLOCKER_2026-09-06.md` |
| `run/claude-prerelease-prompt-telos-2026-09-06` | live Calibration Loop run against an external object | `FAILED_EXECUTION`, no adapter credential in environment |

Neither branch holds a research result. Both hold experiment inputs and an unexecuted protocol. If either produces a durable trace or outcome, that artifact belongs on `main`.

---

# Canonical architecture

Status: `CANONICAL`

Two peer agents under one shared epistemic constitution, plus one deterministic coordination runtime and one non-agent execution contract.

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

- **Neta** — Product Perception and Sensemaking.
- **R&D Agent** — resource↔telos calibration, with research continuity as a sub-capability.
- **Calibration Loop** — deterministic routing runtime. Not an agent. Not a truth authority.
- **Decision→Execution→Learning contract** — a non-agent bridge from bounded decision to verified reality.
- **SCAFFOLD** — external broad reasoning, borrowed when cheaper than internalizing. Not ground truth.

Neta and R&D are peers. Call order does not create hierarchy.

## What is explicitly not built

| Component | Status | What would change it |
|---|---|---|
| Learned Orchestrator | `NOT_EARNED` | repeated ambiguous ownership, lost cross-peer dependencies, or contradictory peer outputs deterministic routing cannot resolve cheaply |
| Third peer | `NOT_EARNED` | a recurring orthogonal judgment outside the mapped function space, per `research/agent-discovery/AGENT_DISCOVERY_CLOSEOUT_2026-09-06.md` |
| Architecture Agent | `NOT_EARNED` | unseen HOLDOUT evidence of unique comparative decision delta |
| Execution Agent | `NOT_EARNED` | a recurring residual judgment across 10-15 real traces after planning and verification contracts are present |
| Requirements Agent | `NOT_EARNED` | unique requirements reasoning beyond current upstream qualification; current best form is an input gate |
| Decision Support capability | `NOT_EARNED` | at least 5 natural admissible post-OWNER cases across at least 3 domains surviving the exclusion rule |

## Shared constitutional decision

Status: `CANONICAL`

Across peers:

> **material uncertainty removed from a live decision** is the unit of progress.

Resolution authority belongs to claims, not agents. Authorities are `OWNER`, `REPO`, `ENVIRONMENT`, `RESEARCH`, `FIELD`.

Canonical shared artifacts:

- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `docs/AGENT_AUTHORITY_BOUNDARIES.md`
- `docs/AUTHORITY_MAP.md`
- `docs/PEER_HANDOFF_PROTOCOL.md`
- `docs/REALITY_AUTHORITY_PERMISSION.md`
- `docs/DECISION_EXECUTION_LEARNING_LOOP.md`
- `schemas/epistemic-claim.schema.json`
- `schemas/peer-handoff.schema.json`
- `schemas/decision-execution-learning.schema.json`

---

# Neta

## Identity

Status: `CANONICAL` method, `FROZEN` prompt.

Neta is an evidence-bounded Product Perception and Sensemaking method with an assurance layer.

- method state: **v0.2 assurance re-foundation**;
- prompt comparator: **frozen v0.1** at `prompts/SYSTEM.md`, blob `339b9a1be2fd0f1f6f6c7960e5be58e5566d3691`;
- capability promotion gate: `eval/CAPABILITY_UPDATE_GATE_V1.md`;
- freeze record: `docs/V0_1_FREEZE.md`.

```text
RAW SIGNAL → CONCRETE MOMENT → OBSERVABLE → COMPETING MECHANISMS
→ CHEAP DISCRIMINATOR → DESIGN DISTINCTION → INTERVENTION / DEFER / FIELD
```

Neta does not own research validity, architecture doctrine or FIELD outcomes.

**No core prompt update has been earned.** R&D evidence cannot promote a Neta prompt rule.

## Empirical state

### GitHub Benchmark Wave 1

Status: `CLOSED_AT_SATURATION`

- 48 adjudicated repositories;
- 16 HOLDOUT repositories;
- 14 fully surviving Neta-vs-baseline decision deltas;
- 8 partially supported deltas;
- 1 clean Neta failure;
- 0 new core rules promoted;
- 0 Neta prompt updates.

Closure means low marginal gain from more routine GitHub sampling. It is not validated universal reliability.

### Hebrew Signal Fidelity H1

Status: `CONFIRMATION_BLOCKED`

H1 is frozen at `eval/hebrew-signal-benchmark/H1_FREEZE.json`. No valid H1 run exists.

The blocker is stated in `eval/hebrew-signal-benchmark/H1_HOLDOUT_COMMISSIONING.md`: a valid HOLDOUT must be authored or sampled by a native-Hebrew authority that does not expose item text or gold to the tested Neta or baseline context before predictions are frozen. That authority is not yet commissioned.

Synthetic gold authored by the same evaluating model must not be relabeled as independent HOLDOUT evidence. The TRAIN seed is not a holdout.

### Hebrew Reader Effect H2

Status: `CONFIRMATION_BLOCKED`

Observatory with a holdout manifest and an annotation guide. Human annotation is commissioned but not delivered. See `eval/hebrew-reader-effect/H2_HUMAN_ANNOTATION_COMMISSIONING.md`.

---

# R&D Agent

Two things are true at once and must not be collapsed into one statement.

## 1. Canonical implementation candidate — broad v0.2

Status: `IMPLEMENTATION_CANDIDATE`

This is what the system actually runs, and it stays the candidate implementation until evidence decides otherwise.

Telos:

> **Improve the fit between the system's resources and its telos, given the state from which the system is actually starting.**

```text
TELOS + CURRENT STATE + RESOURCES
→ BOTTLENECK / MISCALIBRATION
→ CANDIDATE MOVES
→ CHEAPEST DECISION-CHANGING LEARNING
→ OBSERVED DELTA
→ RECALIBRATE
→ UPDATED STATE
```

Canonical candidate artifacts:

- `prompts/RND_AGENT_V0_2_CANDIDATE.md`, blob `03e6c4e25a4fadc189ea26942d38249297371ee9`;
- `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`.

Research is one instrument of this telos, not the telos itself.

The v0.2 candidate has **not** been promoted as validated merely because the Calibration Loop uses it.

## 2. Strongest research hypothesis — narrower scope

Status: `RESEARCH_HYPOTHESIS` · `CONFIRMATION_BLOCKED` · `CONFIRMATORY_N = 0`

Later research proposes a narrower boundary than the broad formulation above. It is frozen for testing and **has not replaced anything**.

```text
CONSEQUENTIAL DECISION
× NONTRIVIAL EPISTEMIC ALLOCATION
→ R&D CORE CANDIDATE
```

> R&D's highest marginal value concentrates where a consequential decision remains open and there is a nontrivial unresolved choice about whether, how, or how much to learn before responsibly advancing that decision.

This is epistemic effort calibration and learning allocation. It is a hypothesis to confirm or falsify, not a canonical boundary.

Frozen artifacts:

- `research/rnd-agent/scope-discovery/RND_SCOPE_MAP_V0_2_FROZEN_FOR_CONFIRMATION.md` — five regions R1-R5, all `UNKNOWN`;
- `research/rnd-agent/scope-discovery/RND_SCOPE_CONFIRMATION_STREAM_V0_2.md` — the confirmation stream;
- `schemas/rnd-scope-case-v0.2.schema.json` — the case contract.

### Confirmation state

```text
CONFIRMATORY_N = 0

R1 EPISTEMIC_ALLOCATION_CORE   = UNKNOWN
R2 OBVIOUS_LEARNING            = UNKNOWN
R3 DIRECT_AUTHORITY_EXECUTION  = UNKNOWN
R4 DOMAIN_METHOD_PRIMARY       = UNKNOWN
R5 LOW_LOCAL_CONTROL           = UNKNOWN
```

The blocker: no independent model-lineage or qualified human adjudication channel is connected. Same-model self-adjudication is explicitly disallowed from supporting the claim. Therefore `95PCT_SCOPE_CERTAINTY = NOT ACHIEVED`, not a synthetic estimate.

### External directional evidence

Status: `DISCOVERY_ONLY`

An 8-issue external GitHub batch was run after the freeze against real maintainer outcomes: 1 material win, 5 ties, 1 material loss, 1 unadjudicable.

It contributes **zero** confirmatory N, because baseline and R&D outputs were same-model role-conditioned passes rather than independent executions, and adjudication was not blinded under the frozen protocol.

Its useful signal is a false-fire: ordinary multi-hypothesis technical debugging was coded as `NONTRIVIAL_EPISTEMIC_ALLOCATION` when it likely belongs to `DOMAIN_METHOD_PRIMARY`. That is a candidate v0.3 coding repair to test on new unseen neighbors, not a retrofit of v0.2.

See `research/rnd-agent/scope-discovery/external-tests/`.

## 3. Frozen comparator — v0.1

Status: `FROZEN_COMPARATOR`

Research-continuity focused.

- `prompts/RND_AGENT_V0_1.md`, blob `bc0e725d0449478d53b93bb6643d24404c22708c`;
- `research/RND_AGENT_CHARTER_V0_1.md`;
- `schemas/rnd-research-task.schema.json`;
- `scripts/validate_rnd_task.py`;
- `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`;
- `eval/rnd-agent/TRAIN_CONTROLS_V0_1.jsonl`.

Its continuity distinctions remain in force:

`instrument ≠ run ≠ durable evidence ≠ decision effect`

`historical evidence ≠ current runnability`, `null ≠ refuted`, `pending ≠ failed`, `agreement ≠ independent triangulation`.

## 4. Epistemology / applied epistemology / VOI transfer

Status: `DISCOVERY_ONLY`

Controlled challengers across latent inquiry, VOI ranking and a zetetic inquiry audit improved vocabulary and contract clarity but did not establish a unique next-move capability beyond current R&D.

See `research/rnd-agent/epistemology/`. These are R&D theory and an evaluation lens, not a capability.

## 5. Targeted OSS transfer

Status: `CLOSED_AT_SATURATION`

Strongest residual candidate needs remain challenger hypotheses until a discriminating failure earns them: attempt/result-selection provenance; stochastic stability where variance is material; execution environment/model/tool identity; trace-level protocol integrity; dependency-safe claim state; checkpoint/rollback semantics; structured recovery of prior attempts.

---

# Calibration Loop

Status: `IMPLEMENTATION_CANDIDATE / CI-GATED`

Canonical artifacts:

- `runtime/calibration_loop/README.md`, `run.py`, `routing.py`, `adapters.py`;
- `schemas/calibration-task.schema.json`;
- `scripts/validate_calibration_task.py`;
- `scripts/check_calibration_loop.py`;
- `fixtures/calibration-valid-task.json`.

```text
R&D DIAGNOSE → deterministic routing → Neta / Scaffold / authority as triggered
→ R&D SYNTHESIZE → trace + resource deltas + learning record
```

Routing rules are inspectable and are not self-modified from one case. The runtime may stop at `PENDING_RESOURCE`, `AUTHORITY_STOP` or `FAILED_EXECUTION` rather than fabricate an answer, and it did exactly that on the 2026-09-06 live run when no adapter credential was present.

## First manual run

`CAL-ARCH-001` was executed manually on 2026-09-05 without API/model adapters: `runtime/calibration_loop/traces/CAL-ARCH-001-MANUAL-2026-09-05.md`.

Limitation: R&D, Neta and Scaffold were role-separated but executed in one session and one foundation-model lineage. Their agreement is **not** independent triangulation.

It produced a material decision change, from "build an Architecture Agent" to "first test whether a distinct architecture-specific decision capability adds value beyond R&D + Scaffold + REPO/ENVIRONMENT evidence".

---

# Decision → Execution → Learning contract

Status: `CROSS_AGENT_EXECUTION_CONTRACT_V0_1 / CI-GATED`

```text
DECISION → EXECUTION → VERIFIED STATE → OUTCOME → LEARNING
```

Canonical artifacts:

- `docs/DECISION_EXECUTION_LEARNING_LOOP.md`;
- `schemas/decision-execution-learning.schema.json`;
- `scripts/validate_decision_trace.py`;
- `fixtures/decision-execution-learning-valid.json`;
- first real trace: `runtime/execution_traces/DEL-ARCH-CORPUS-001.json`.

Invariant: `action completed ≠ verified state ≠ measured outcome ≠ learning`. Execution does not inherit REPO, ENVIRONMENT or FIELD authority.

This contract does not justify an Execution Agent.

---

# Architecture

Status: `CANDIDATE_CAPABILITY_NOT_AGENT` · the **only** active peer candidate.

## Corpus and protocol

- `research/architecture-agent/ARCHITECTURE_DECISION_DISCRIMINATOR_V0.md` — the candidate contract;
- `eval/architecture-agent/TRAIN_CONTROLS_V0.jsonl` — first visible controls;
- `eval/architecture-agent/HISTORICAL_CASES_V0.jsonl` — 12 runner-visible frozen cases across 4 repositories;
- `eval/architecture-agent/HISTORICAL_GOLD_V0.jsonl` — adjudication anchors, kept separate from runner inputs;
- `eval/architecture-agent/HISTORICAL_BENCHMARK_PROTOCOL_V0.md`;
- `scripts/check_architecture_historical_cases.py` — CI gate on count, repository breadth and CASES/GOLD separation.

The visible corpus is retrospective TRAIN evidence only. Historical implementation is not ground truth and agreement with it is not a score.

Contamination boundary: the context that authored or froze `HISTORICAL_GOLD_V0.jsonl` is not eligible to generate countable baseline or candidate outputs for this corpus.

## A/B evidence to date

Status: `DISCOVERY_ONLY · MODEL_IDENTITY_CAVEAT`

One staged A/B has executed: `ARCH-AB-20260906T102435Z`, on 2026-09-06.

It preserved the strongest contamination barrier: 24 baseline and candidate outputs completed first, freeze manifest written and hashed, judging only after freeze, blind X/Y adjudication. But it used Copilot `--model auto`, which does not establish that A and B ran on the same underlying model. The frozen v0 protocol requires the same clean model.

It is therefore retained as `DIAGNOSTIC_EXECUTION_SIGNAL`, not as the protocol-conforming result, and it is not promotion evidence.

Diagnostic aggregate: candidate material wins 1, baseline material wins 1, candidate harm 0, baseline harm 0.

| Dimension | Architecture | Baseline | Tie/Neither |
|---|---:|---:|---:|
| Boundary | 2 | 3 | 7 |
| Authority | 2 | 3 | 7 |
| Option | 3 | 2 | 7 |
| Discriminator | 5 | 3 | 4 |
| Migration | 5 | 1 | 6 |
| Anti-build | 4 | 2 | 6 |

The pattern matters more than the score: Architecture did not dominate structural destination selection, authority or boundaries. Its repeated delta was around migration, bounded discrimination, staged change and anti-build.

## Current dispositions

```text
ARCHITECTURE_AGENT                  = NOT_EARNED
ARCHITECTURE_SELECTION_CAPABILITY   = UNIQUE_DELTA_NOT_SHOWN
ARCHITECTURE_INPUT_GATE             = EARNED_AS_CONTRACT_SHAPE
STRUCTURAL_CHANGE_ENVELOPE          = STRONGEST_NEW_RESIDUAL_CANDIDATE
STRUCTURAL_CHANGE_ENVELOPE_AGENT    = CATEGORY_ERROR / NOT_PROPOSED
```

`STRUCTURAL_CHANGE_ENVELOPE` is a candidate contract shape only, described in `research/agent-discovery/ARCHITECTURE_RESIDUAL_DECOMPOSITION_2026-09-06.md`. It is not built, not scheduled and not a capability. Do not implement it as part of repository maintenance.

## Next discriminating experiment

The protocol-conforming clean A/B, on PR 14.

Status: `EXECUTION_BLOCKED`, not `FAILED` and not a candidate result.

The frozen v0.2 model-selection rule probed five explicit Copilot model IDs and found none available in the Actions environment, then stopped rather than substituting `auto`. No case was loaded, no GOLD was read, no output was produced.

Full diagnosis, permitted and forbidden remediation classes: `eval/architecture-agent/EXECUTION_BLOCKER_2026-09-06.md`.

No promotion may follow from unseen-holdout evidence that does not yet exist.

---

# Agent Discovery

Status: `CLOSED_AT_SATURATION` · `NO_NEW_AGENT_EARNED`

Broad discovery asked which recurring material judgment functions remain unowned after subtracting the peers, the authorities, domain methods, deterministic coordination, execution and shared infrastructure.

Result: no third peer is earned. Current peers remain Neta and R&D. The only active peer candidate is Architecture, unpromoted.

Artifacts: `research/agent-discovery/`, closing at `AGENT_DISCOVERY_CLOSEOUT_2026-09-06.md`.

The closeout converges with the earlier independent repo trace `CAL-MECE-001`. Both share project lineage, so the agreement strengthens the default but is not independent statistical evidence.

Reopen broad discovery only if all of these hold: a real decision repeatedly fails despite correct routing; deterministic protocol or tool repair is insufficient; the same hidden judgment recurs across cases; and a minimal candidate changes material decisions over the strongest existing system.

---

# Current next authorized execution

## Neta

- keep `prompts/SYSTEM.md` frozen until Neta-specific evidence earns change;
- commission an independent Hebrew HOLDOUT authority, or leave H1 blocked;
- continue only decision-changing evaluation lanes;
- do not take over R&D or architecture authority.

## R&D

- keep v0.1 as frozen comparator;
- keep broad v0.2 as the implementation candidate until evidence decides;
- keep the narrow epistemic-allocation hypothesis at `CONFIRMATORY_N = 0` until an admissible case exists;
- the single blocking need is an independent adjudication channel: a different model lineage, or a qualified human adjudicator;
- do not count discovery, historical or same-model evidence toward confirmation;
- preserve the external-batch false-fire as a candidate v0.3 repair rather than editing v0.2.

## Architecture

- resolve the execution blocker without touching the frozen protocol;
- run the protocol-conforming clean A/B;
- only then create unseen HOLDOUT, and only HOLDOUT evidence may earn movement toward an autonomous agent;
- do not build `STRUCTURAL_CHANGE_ENVELOPE` before its own baseline-vs-challenger test is designed and frozen.

## Execution capability

Do not build an Execution Agent. Collect 10-15 real traces under `schemas/decision-execution-learning.schema.json`.

## Orchestrator

Do not build. The earning conditions are listed under "What is explicitly not built".
