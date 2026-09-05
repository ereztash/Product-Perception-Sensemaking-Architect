# Repository Map

Status: `CANONICAL`

This repository is a **peer-agent system**, not a collection of independent historical branches.

## Single source of truth

`main` is the only canonical branch.

All product, research, evaluation and runtime claims must be readable from `main` without checking a historical branch.

Historical branches are lineage only. They must not contain the only copy of decision-relevant knowledge.

## Canonical layers

```text
docs/
  shared constitution, authority boundaries, canonical state, repository map

prompts/
  agent/scaffold prompts and frozen comparators

schemas/
  shared and peer/runtime contracts

runtime/
  executable coordination and resource adapters

research/
  current research lineage, syntheses and agent charters/telos

eval/
  agent-specific promotion gates, controls and evaluation artifacts

fixtures/
  executable/visible test cases

scripts/
  validators and CI-facing contract checks

memory/
  bounded owner-language priors; never cross-agent ground truth

archive/
  historical artifacts retained for lineage but not current authority
```

## Current peer architecture

```text
                     OWNER / TELOS
                          |
                 CALIBRATION LOOP
               deterministic routing
                 /              \
              NETA              R&D
        product/design       resource↔telos
         sensemaking          calibration
                 \              /
              SHARED EPISTEMIC KERNEL
```

`SCAFFOLD` is an external reasoning resource used by the Calibration Loop when broad synthesis is cheaper to borrow than internalize.

No learned Orchestrator exists yet.

## Canonical status by component

### Shared kernel
Canonical.

Key files:
- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `docs/AGENT_AUTHORITY_BOUNDARIES.md`
- `docs/PEER_HANDOFF_PROTOCOL.md`
- `schemas/epistemic-claim.schema.json`
- `schemas/peer-handoff.schema.json`

### Neta
Canonical method; frozen prompt comparator.

Key files:
- `prompts/SYSTEM.md`
- `docs/NETA_ASSURANCE_THESIS.md`
- `docs/METHOD.md`
- `schemas/finding.schema.json`
- `eval/CAPABILITY_UPDATE_GATE_V1.md`

### R&D
Two explicit states are retained:

- `v0.1` — frozen research-continuity comparator;
- `v0.2 candidate` — resource↔telos calibration telos, not yet promoted as validated.

Key files:
- `prompts/RND_AGENT_V0_1.md`
- `research/RND_AGENT_CHARTER_V0_1.md`
- `prompts/RND_AGENT_V0_2_CANDIDATE.md`
- `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`
- `schemas/rnd-research-task.schema.json`
- `eval/rnd-agent/`

### Calibration Loop
Implementation candidate, now merged to `main`.

Key files:
- `runtime/calibration_loop/`
- `schemas/calibration-task.schema.json`
- `fixtures/calibration-valid-task.json`
- `scripts/check_calibration_loop.py`

The runner is deterministic. It does not become a truth authority and does not rewrite routing rules from one case.

## Branch policy

1. `main` is the only long-lived authoritative branch.
2. New work branches are temporary and must have one named purpose.
3. Before a temporary branch is retired, all decision-relevant artifacts must be merged into `main` or copied under `archive/`.
4. No benchmark/research branch may remain the only place where a result exists.
5. A stale branch is never evidence that its code/result is current.
6. Branch names do not define authority.

## Historical branch cleanup — 2026-09-05

A branch audit found:

- several historical branches were already strict ancestors of `main` and contained no unique commits;
- `neta/v0.1-agent-contract` diverged historically but its product files are superseded by later canonical versions in `main`;
- `research/wave1-evidence-pass1` contained three research documents not present in `main`; those are retained under `archive/legacy-branches/research-wave1-evidence-pass1/` before the old ref is normalized.

See `archive/legacy-branches/BRANCH_MANIFEST_2026-09-05.md` for exact branch-tip SHAs and disposition.

## Rule for future work

If a question cannot be answered from `main` plus explicitly labeled `archive/`, repository organization has failed.
