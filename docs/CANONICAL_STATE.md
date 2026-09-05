# Canonical Repository State

Last consolidated: 2026-09-05

## Canonical architecture

The repository now contains two peer agents/methods under a shared epistemic constitution:

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
- runtime contract: `schemas/rnd-research-task.schema.json`;
- evaluation/promotion protocol: `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`;
- visible controls: `eval/rnd-agent/TRAIN_CONTROLS_V0_1.jsonl`.

Current R&D state:

- architecture/charter specified;
- cross-repository instrument extraction imported;
- triangulation/synthesis completed and retained as lineage;
- 8 TRAIN controls defined;
- no frozen executable agent implementation yet;
- no unseen HOLDOUT run yet;
- no R&D capability repairs promoted yet.

Therefore the R&D Agent is **SPECIFIED / TEST-READY**, not empirically validated.

R&D capability changes are governed by the R&D eval protocol, not Neta's capability gate.

## Canonical evidence chain

Shared constitutional chain:

`Claim → Evidence → Reality → Resolution Authority → Requested Use → Permission → Reversal / Stop`

Neta adds product/design objects around this chain.

R&D adds research continuity:

`Live Claim → Recovery → Reuse/Adapt/Build → Version/Input Fit → Run → Durable Deposit → Claim Disposition → Later Revalidation`

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

The wave did **not** reach minimum viable evidence because the preregistered threshold required at least 3 clean Neta failures and only 1 was observed.

Closure means the current broad GitHub sampling distribution is saturated for useful Neta learning, not that Neta has been proven reliable.

## Branch authority

### `main`

Canonical released state for shared architecture, Neta, R&D contracts and frozen empirical records.

### Historical/specialized Neta branches

Existing `neta/*` branches remain historical or specialized execution tracks. The peer-architecture refactor does not reinterpret their historical results.

Key examples:

- `neta/oss-observatory` — historical GitHub Benchmark Wave 1 execution branch;
- `neta/hebrew-signal-fidelity` — Hebrew decision-fidelity track;
- `neta/hebrew-observatory` — Hebrew affect/pragmatics track;
- `neta/design-research-spine-v0.1` — quarantined design-knowledge crosswalk.

No R&D Agent branch is canonical yet; a future implementation branch must freeze the tested baseline before HOLDOUT creation.

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
2. Continue only the already-authorized targeted/Hebrew/field evaluation programs when they remove named Neta uncertainty.
3. Do not promote R&D findings directly into Neta behavior.

### R&D Agent

1. Implement the smallest executable baseline that follows `RND_AGENT_CHARTER_V0_1.md` and emits `rnd-research-task` objects.
2. Freeze exact implementation/model/prompt/tool boundary before unseen evaluation.
3. Run the 8 visible TRAIN controls only to verify evaluator/contract behavior.
4. Create unseen HOLDOUT and adversarial cases after the baseline is frozen.
5. Adjudicate case-level decisions across the orthogonal R&D capability dimensions.
6. Promote no repair until the R&D-specific gate is crossed.

### Orchestrator

Do not build yet.

The first orchestrator-worthy evidence would be repeated failures such as:

- ambiguous ownership between stable peers;
- lost dependencies across peer handoffs;
- contradictory peer outputs that users cannot route correctly;
- repeated manual routing overhead that materially harms decision quality or cost.

Until such failures exist, peer handoffs are the cheaper admissible architecture.
