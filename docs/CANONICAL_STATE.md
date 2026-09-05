# Canonical Repository State

Last consolidated: 2026-09-05

## Canonical architecture

The repository contains two peer agents/methods under a shared epistemic constitution:

- **Neta** — Product Perception & Sensemaking;
- **R&D Agent** — Research & Evidence Sensemaking.

A future Orchestrator is explicitly **deferred** until at least two peers can produce stable machine-readable outputs/handoffs and real routing failures justify a coordination layer.

Canonical cross-agent artifacts:

- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `docs/AGENT_AUTHORITY_BOUNDARIES.md`
- `docs/PEER_HANDOFF_PROTOCOL.md`
- `schemas/epistemic-claim.schema.json`
- `schemas/peer-handoff.schema.json`

Neta is not the parent of R&D. R&D is not a sub-capability of Neta. Historical derivation order does not define authority.

## Shared constitutional decision

Across peers:

> **material uncertainty removed from a live decision** is the unit of progress.

Resolution authority belongs to claims, not agents.

The current detailed R0–R6 and OWNER/REPO/ENVIRONMENT/RESEARCH/FIELD semantics remain in `docs/REALITY_AUTHORITY_PERMISSION.md` and are adopted cross-agent through the shared kernel.

## Neta canonical identity

Neta remains an evidence-bounded Product Perception & Sensemaking method with an assurance layer. The current canonical Neta method state is the **v0.2 assurance re-foundation**.

The canonical Neta prompt remains the **frozen v0.1 baseline**. The GitHub benchmark did not earn a prompt edit.

This distinction remains intentional:

- `Neta method/version`: v0.2 assurance architecture;
- `Neta prompt/baseline`: v0.1 frozen clean-model comparator;
- `Neta evaluation`: empirical benchmark evidence may constrain claims about Neta but may not silently rewrite the prompt.

Neta capability changes remain governed by `eval/CAPABILITY_UPDATE_GATE_V1.md`.

## R&D Agent canonical identity

The R&D Agent is the peer responsible for research/evidence sensemaking and research continuity.

Current canonical R&D artifacts:

- charter: `research/RND_AGENT_CHARTER_V0_1.md`;
- frozen prompt baseline: `prompts/RND_AGENT_V0_1.md`;
- frozen prompt blob SHA: `bc0e725d0449478d53b93bb6643d24404c22708c`;
- baseline freeze record: `eval/rnd-agent/BASELINE_FREEZE_V0_1.md`;
- runtime contract: `schemas/rnd-research-task.schema.json`;
- semantic validator: `scripts/validate_rnd_task.py`;
- evaluation/promotion protocol: `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`;
- visible controls: `eval/rnd-agent/TRAIN_CONTROLS_V0_1.jsonl`;
- targeted OSS lane: `research/rnd-agent/`;
- OSS-derived challenger queue: `eval/rnd-agent/OSS_CHALLENGER_QUEUE_V0_1.md`;
- prospective eval-integrity amendment: `eval/rnd-agent/EVAL_AMENDMENT_2026-09-05_OSS.md`.

Current R&D state:

- architecture/charter specified;
- cross-repository instrument extraction imported;
- triangulation/synthesis completed and retained as lineage;
- 8 original TRAIN controls defined;
- minimal v0.1 prompt baseline frozen **before OSS-derived transfer is allowed to modify behavior**;
- runtime semantic validator added;
- targeted OSS transfer completed across materially different research-agent architectures and closed at architecture saturation;
- OSS-derived Priority-A and architecture challenger fixtures are quarantined from unseen validation;
- no clean model/tool execution of the frozen baseline has yet been adjudicated;
- no unseen HOLDOUT run yet;
- no R&D capability repairs promoted yet.

Therefore the R&D Agent is **FROZEN BASELINE / PRE-EXECUTION**, not empirically validated.

R&D capability changes are governed by the R&D eval protocol, not Neta's capability gate.

## R&D targeted OSS decision

The targeted OSS lane deliberately sampled architecture families rather than maximizing repository count, including:

- research/development role split;
- tree/graph exploration;
- phase-specialized multi-agent research;
- scientific retrieval/evidence gathering;
- reproducible agent benchmark/runtime infrastructure;
- stochastic long-horizon agent evaluation;
- report/citation verification;
- experience memory and graph search;
- self-evolving research systems.

A final LoongFlow saturation probe repeated already represented patterns (plan/execute/summary, reflection, experience memory) rather than exposing a new decision-relevant architecture axis.

Routine OSS expansion is therefore stopped.

The strongest residuals are not a demonstrated need for multi-agent architecture. They are:

1. attempt/result-selection provenance;
2. stochastic stability when variance is material;
3. execution environment/model/tool identity;
4. trace-level protocol integrity;
5. dependency-safe claim/experiment/finding state;
6. checkpoint/rollback semantics;
7. structured recovery of prior attempts/failures.

These remain challenger hypotheses until the frozen baseline fails a discriminating case.

## Canonical evidence chain

Shared constitutional chain:

`Claim → Evidence → Reality → Resolution Authority → Requested Use → Permission → Reversal / Stop`

Neta adds product/design objects around this chain.

R&D adds research continuity:

`Live Claim → Recovery → Reuse/Adapt/Build → Version/Input Fit → Run → Durable Deposit → Claim Disposition → Later Revalidation`

The OSS transfer adds candidate verification residuals around attempts, stochastic/runtime provenance and dependency-safe recovery; these are **not yet canonical R&D behavior**.

A result may move downstream only when its authority and reality floor permit it. Recurrence alone is not promotion.

## GitHub Benchmark Wave 1 — Neta

Wave 1 is frozen and closed at BATCH-016 because routine broad sampling reached low marginal decision gain.

Frozen state:

- 48 adjudicated repositories;
- 16 HOLDOUT repositories;
- all four Neta decision modes represented: BUILD_READY, DISCRIMINATE_FIRST, OWNER_DEFER, FIELD_STOP;
- 14 fully surviving Neta-vs-baseline decision deltas;
- 8 partially supported deltas;
- 1 clean Neta failure;
- 9 tracked failure families;
- 0 promoted new core rules;
- 0 Neta prompt updates.

The wave did **not reach minimum viable evidence** because the preregistered threshold required at least 3 clean Neta failures and only 1 was observed.

Closure means the current broad GitHub sampling distribution is saturated for useful Neta learning, not that Neta has been proven reliable.

## Branch authority

### `main`

Canonical released state for shared architecture, Neta, R&D contracts, frozen comparators and empirical records.

### Historical/specialized Neta branches

Existing `neta/*` branches remain historical or specialized execution tracks. The peer-architecture refactor does not reinterpret their historical results.

Key examples:

- `neta/oss-observatory` — historical GitHub Benchmark Wave 1 execution branch;
- `neta/hebrew-signal-fidelity` — Hebrew decision-fidelity track;
- `neta/hebrew-observatory` — Hebrew affect/pragmatics track;
- `neta/design-research-spine-v0.1` — quarantined design-knowledge crosswalk.

No R&D execution branch is canonical yet. The prompt comparator is frozen on `main`; an execution branch/run must additionally freeze the exact model/tool/runtime/evaluator boundary before unseen HOLDOUT creation.

## Hebrew consolidation decision — Neta-specific

Two non-equivalent Hebrew questions remain distinct:

### Track H1 — Signal Fidelity

Does Neta preserve decision-relevant meaning, ambiguity, authority and action when input is natural Israeli Hebrew?

### Track H2 — Reader Effect

Can Neta distinguish what a Hebrew utterance says, what it implies about the speaker, and what it is likely to evoke in a recipient?

H1 and H2 must not collapse into one composite score.

These are Neta evaluation tracks, not R&D Agent promotion evidence by default.

## Current next authorized execution

### Neta

1. Keep Neta prompt frozen.
2. Continue only already-authorized targeted/Hebrew/field evaluation programs when they remove named Neta uncertainty.
3. Do not promote R&D findings directly into Neta behavior.

### R&D Agent

1. Keep `prompts/RND_AGENT_V0_1.md` frozen at blob `bc0e725d0449478d53b93bb6643d24404c22708c`.
2. Verify controlled task objects against `scripts/validate_rnd_task.py` and the runtime schema.
3. Freeze the exact foundation model, inference configuration, tools/runtime, resource budget and evaluator boundary used for execution.
4. Run the 8 original visible TRAIN controls only to verify baseline judgment/contract behavior.
5. Run Priority-A OSS challengers as visible/adversarial tests; they cannot count as unseen validation.
6. Create unseen HOLDOUT cases only after the complete execution baseline is frozen.
7. Adjudicate case-level decisions across the orthogonal R&D capability dimensions and prospective eval-integrity amendment.
8. Promote no repair until the R&D-specific gate is crossed.
9. Compare tree/graph search, experience memory or multi-agent challengers only if the simpler baseline exposes a failure those architectures plausibly address under matched resource budgets.

### Orchestrator

Do not build yet.

The first orchestrator-worthy evidence would be repeated failures such as:

- ambiguous ownership between stable peers;
- lost dependencies across peer handoffs;
- contradictory peer outputs that users cannot route correctly;
- repeated manual routing overhead that materially harms decision quality or cost.

Until such failures exist, peer handoffs are the cheaper admissible architecture.
