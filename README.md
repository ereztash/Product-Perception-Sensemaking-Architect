# Evidence-Bounded Agent Architecture — Neta + R&D

This repository now contains two **peer agents/methods** built around a shared epistemic constitution:

- **Neta** — Product Perception & Sensemaking;
- **R&D Agent** — Research & Evidence Sensemaking.

A future **Orchestrator** may route and synthesize work across peers, but it is not built yet and will not be a truth authority.

## Architecture

```text
                    future ORCHESTRATOR
                 routing / dependencies /
                      synthesis only
                        /          \
                       /            \
                    NETA           R&D AGENT
               product/design      research/evidence
                sensemaking         sensemaking
                       \            /
                        \          /
                 SHARED EPISTEMIC KERNEL
                    constitution only
```

Neta and R&D are peers. The order in which one calls the other does not create hierarchy.

The shared kernel owns cross-agent epistemic rules such as claim/evidence separation, reality, resolution authority, requested use, permission, provenance, reversal and stopping. It is a protocol, not an agent.

See:

- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `docs/AGENT_AUTHORITY_BOUNDARIES.md`
- `docs/PEER_HANDOFF_PROTOCOL.md`
- `docs/AUTHORITY_MAP.md`

## Shared unit of progress

Across peers:

> **Progress = material uncertainty removed from a live decision.**

Not code written, citations collected, instruments created, screens redesigned or rules added.

## Peer 1 — Neta

Neta helps an owner-builder turn a raw product intuition into a defensible product/design decision without allowing the claim or action to outrun the evidence and authority that exist.

### Neta loop

```text
RAW SIGNAL
→ CONCRETE MOMENT
→ OBSERVABLE
→ COMPETING PRODUCT/DESIGN MECHANISMS
→ CHEAP DISCRIMINATOR
→ DESIGN DISTINCTION
→ BOUNDED INTERVENTION / FIELD REQUIREMENT
```

Neta's canonical method remains the **v0.2 assurance re-foundation**.

Neta's prompt comparator remains the **frozen v0.1 baseline** until a clean-model failure earns a change.

See:

- `docs/NETA_ASSURANCE_THESIS.md`
- `docs/METHOD.md`
- `schemas/finding.schema.json`
- `eval/CAPABILITY_UPDATE_GATE_V1.md`

## Peer 2 — R&D Agent

The R&D Agent removes research-owned uncertainty by connecting:

```text
LIVE CLAIM
→ BOUNDED RECOVERY
→ REUSE / ADAPT / BUILD / NO_INSTRUMENT / WAIT_AUTHORITY
→ INPUT + VERSION REVALIDATION
→ EXECUTION
→ DECISION-RELEVANT DEPOSIT
→ CLAIM DISPOSITION
→ HANDOFF / STOP
```

Its core failure target is **research discontinuity**:

```text
instrument ≠ run
run ≠ durable evidence
historical evidence ≠ current runnability
partial report ≠ original decision contract
agreement ≠ independent triangulation
null ≠ refuted
pending ≠ failed
```

The R&D Agent follows `search-before-build`, not `reuse-first`.

See:

- `research/RND_AGENT_CHARTER_V0_1.md`
- `schemas/rnd-research-task.schema.json`
- `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`
- `eval/rnd-agent/TRAIN_CONTROLS_V0_1.jsonl`

## Shared contracts

### Shared claim

`schemas/epistemic-claim.schema.json`

### Peer handoff

`schemas/peer-handoff.schema.json`

### Current reality/authority semantics

`docs/REALITY_AUTHORITY_PERMISSION.md`

These semantics were historically developed inside Neta and are now adopted as cross-agent constitutional infrastructure. Historical origin does not imply Neta owns the R&D peer.

## Resolution authority is not agent hierarchy

Claims resolve through:

- `OWNER`
- `REPO`
- `ENVIRONMENT`
- `RESEARCH`
- `FIELD`

Agent role answers **who should work the question**.

Resolution authority answers **what evidence can legitimately close it**.

An R&D Agent handling a FIELD claim cannot close it through literature. Neta handling a RESEARCH-owned measurement question should hand it to R&D rather than work harder internally.

## Peer handoffs

Neta ↔ R&D handoffs are bidirectional.

Examples:

- Neta → R&D: external mechanism support, construct validity, measurement choice, prior nulls, evidence independence.
- R&D → Neta: research is bounded; remaining decision is local product mechanism, intervention or owner tradeoff.

Either peer may challenge the other's premise without becoming its superior.

The future orchestrator should consume these same handoff objects rather than invent a second routing language.

## Independent promotion paths

Do not cross-promote.

### Neta capability promotion

`eval/CAPABILITY_UPDATE_GATE_V1.md`

### R&D capability promotion

`eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`

### Shared-kernel change

Requires a genuinely cross-agent constitutional failure plus impact analysis on both peer adapters.

Passing an R&D benchmark cannot directly edit Neta's prompt. Passing a Neta benchmark cannot directly rewrite the R&D charter.

## Existing Neta empirical state

The existing Neta evidence remains intact:

- GitHub Benchmark Wave 1 is closed at saturation under its broad sampling distribution;
- 48 adjudicated repositories;
- 16 HOLDOUT repositories;
- 14 fully surviving Neta-vs-baseline decision deltas;
- 1 clean Neta failure;
- 0 new core rules promoted;
- 0 prompt updates.

The architectural peer refactor does not rewrite that history.

## R&D Agent empirical state

Current state:

- cross-repository instrument extraction completed;
- Neta-only pass completed as historical derivation support;
- external triangulation and bounded synthesis completed;
- R&D charter frozen as v0.1;
- shared/R&D runtime schemas created;
- independent R&D eval protocol preregistered;
- 8 visible TRAIN controls created;
- **no R&D implementation/HOLDOUT evidence yet**.

Therefore the R&D Agent is architecturally specified but not yet empirically validated.

## Repository structure

```text
docs/          shared kernel, peer boundaries, handoffs + Neta-specific method/governance
schemas/       shared claim/handoff + Neta and R&D peer adapters
prompts/       frozen Neta v0.1 baseline until a Neta failure earns change
research/      Neta research quarantine + R&D charter + instrument-portfolio lineage
memory/        Neta owner-language priors, never shared ground truth
fixtures/      conversational/research/assurance cases
eval/          Neta evaluations + independent R&D-agent evaluation lane
scripts/       executable Neta/research gates and validators
```

## Current architectural status

**TWO PEERS · SHARED EPISTEMIC KERNEL · NETA PROMPT FROZEN · R&D v0.1 CHARTER + EVAL PREREGISTERED · ORCHESTRATOR DEFERRED.**

The next decision-changing R&D step is to implement/freeze a minimal R&D agent baseline and run it against the visible controls, then create unseen HOLDOUT cases before any R&D capability repair.
