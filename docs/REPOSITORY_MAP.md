# Repository Map

Status: `CANONICAL`
Last reconciled: 2026-09-06

This repository is a **peer-agent system**, not a collection of independent historical branches.

## Single source of truth

`main` is the only canonical branch.

All product, research, evaluation and runtime claims must be readable from `main` without checking a historical branch.

Historical branches are lineage only. They must not contain the only copy of decision-relevant knowledge.

`scripts/check_canonical_state.py` enforces the machine-checkable half of this rule in CI.

## Canonical layers

```text
docs/
  shared constitution, authority boundaries, canonical state, repository map

prompts/
  agent and scaffold prompts, frozen or candidate only

schemas/
  shared, peer and runtime contracts

runtime/
  executable coordination, resource adapters, traces

research/
  non-canonical research programs, lineage, syntheses and agent charters

eval/
  frozen benchmarks, promotion gates, controls and scoring

fixtures/
  executable and visible test inputs

scripts/
  validators, runners and CI-facing contract checks

memory/
  bounded owner-language priors; never cross-agent ground truth

archive/
  superseded artifacts, historical lineage and reconciliation records
```

Nothing under `research/` is canonical. Nothing under `archive/` is current authority. `docs/CANONICAL_STATE.md` is the only place where a component's evidence status is authoritative.

## Research lane structure

Research is organized so that the discovery/confirmation boundary is visible from the directory tree.

```text
research/
  README.md                     Neta quarantine + R&D peer lineage, and their separation
  agent-discovery/              closed broad discovery for a third peer
  architecture-agent/           architecture candidate contract and system-design lineage
  chess-error-adaptation/       Neta/R&D joint research lane
  design-spine/                 quarantined frontend design crosswalk
  question-discovery/           front-door qualification research
  registers/                    claims, sources, contradictions, culture scope
  rnd-agent/
    telos/                      R&D telos formulation, narrow-vs-broad benchmark, peer review
    scope-discovery/            where R&D marginal value concentrates
      external-tests/           post-freeze external outcome batches, directional only
    epistemology/               epistemology / applied epistemology / VOI transfer tests
```

`research/rnd-agent/README.md` states the three evidence streams and the current `CONFIRMATORY_N`. `research/agent-discovery/README.md` states the closeout dispositions and the reopen conditions.

`external-tests/` is nested inside `scope-discovery/` because those batches test that specific scope hypothesis, and the frozen confirmation stream references them by that relative path.

## Evaluation lane structure

```text
eval/
  CAPABILITY_UPDATE_GATE_V1.md  Neta promotion gate
  RUBRIC.md                     Neta scoring
  architecture-agent/           frozen corpus, protocols, execution blockers
  decision-quality/
  field-outcomes/
  github-benchmark/             Neta Wave 1, closed at saturation
  hebrew-reader-effect/         H2, awaiting human annotation authority
  hebrew-signal-benchmark/      H1, awaiting independent holdout authority
  rnd-agent/                    R&D eval protocol and controls
  targeted-falsification/
```

A benchmark directory containing a protocol proves that a protocol exists. It does not prove the benchmark ran, that a run was admissible, or that its result counts.

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

`SCAFFOLD` is an external reasoning resource used when broad synthesis is cheaper to borrow than internalize.

No learned Orchestrator exists. No third peer exists.

## Canonical status by component

Authoritative statuses live in `docs/CANONICAL_STATE.md`. This is the file index only.

### Shared kernel
`docs/SHARED_EPISTEMIC_KERNEL.md`, `docs/AGENT_AUTHORITY_BOUNDARIES.md`, `docs/AUTHORITY_MAP.md`, `docs/PEER_HANDOFF_PROTOCOL.md`, `docs/REALITY_AUTHORITY_PERMISSION.md`, `schemas/epistemic-claim.schema.json`, `schemas/peer-handoff.schema.json`.

### Neta
`prompts/SYSTEM.md` (frozen), `docs/NETA_ASSURANCE_THESIS.md`, `docs/METHOD.md`, `docs/V0_1_FREEZE.md`, `schemas/finding.schema.json`, `eval/CAPABILITY_UPDATE_GATE_V1.md`.

### R&D
`prompts/RND_AGENT_V0_1.md` (frozen comparator), `prompts/RND_AGENT_V0_2_CANDIDATE.md` (implementation candidate), `research/RND_AGENT_CHARTER_V0_1.md`, `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`, `schemas/rnd-research-task.schema.json`, `schemas/rnd-scope-case-v0.2.schema.json`, `eval/rnd-agent/`.

### Calibration Loop
`runtime/calibration_loop/`, `schemas/calibration-task.schema.json`, `fixtures/calibration-valid-task.json`, `scripts/check_calibration_loop.py`.

### Decision → Execution → Learning
`docs/DECISION_EXECUTION_LEARNING_LOOP.md`, `schemas/decision-execution-learning.schema.json`, `scripts/validate_decision_trace.py`, `runtime/execution_traces/`.

### Architecture candidate
`research/architecture-agent/`, `eval/architecture-agent/`, `scripts/check_architecture_historical_cases.py`.

## Branch policy

1. `main` is the only long-lived authoritative branch.
2. New work branches are temporary and must have one named purpose.
3. Before a temporary branch is retired, all decision-relevant artifacts must be merged into `main` or copied under `archive/`.
4. No benchmark or research branch may remain the only place where a result exists.
5. A branch that is ahead of `main` must be a live, named, documented experiment, listed under "Active branches" in `docs/CANONICAL_STATE.md`.
6. A stale branch is never evidence that its code or result is current.
7. Branch names do not define authority.
8. Every branch on the remote must be declared in `docs/BRANCH_INVENTORY.md` with exactly one disposition,
   within a day of its newest commit. A branch younger than that may exist undeclared; the rule is that
   nothing lives only on a side branch indefinitely, not that a branch is declared before its first push.

Rules 1 through 7 were written on 2026-09-05 and enforced by review. By 2026-09-08 twelve
branches were ahead of `main` against two declared, and sixty-nine files existed on no
canonical path. Rule 8 exists because the others had no instrument.

`scripts/check_branch_inventory.py --live` compares the declaration against the actual
remote and fails on any disagreement. It also recomputes the numbers the declaration
publishes. A count in that file is measured tree to tree, `git ls-tree -r --name-only` on
both sides; never `git diff main...branch`, which compares against the merge base and
answers a different question. Eleven of sixteen rows were wrong for three days because the
published number and the prose describing it came from different commands, and nothing
compared either to the repository.

`SUPERSEDED` is checked the same way. The named successor must carry every path the branch
holds and hold each at the branch's content or at a version its own history contains. Paths
alone would license deleting a branch whose refinement a successor never took. Retirement of a contained branch is an `OWNER` action
executed outside an agent session: `docs/BRANCH_RETIREMENT_RUNBOOK.md`.

## Where a new file goes

| The file is | It belongs in |
|---|---|
| a claim about what is currently true | `docs/` |
| a prompt that an agent runs | `prompts/` |
| a machine-readable contract | `schemas/` |
| code that coordinates or executes | `runtime/` or `scripts/` |
| evidence gathering that has not been promoted | `research/` |
| a frozen benchmark, gate or score | `eval/` |
| an input to a validator or runner | `fixtures/` |
| superseded, or kept only for lineage | `archive/` |
| an agent skill definition | unresolved; see below |

If a file would be decision-relevant and does not fit any row, the ambiguity is the finding. Record it before creating the file.

### Unresolved placement: `skills/`

`skills/evidence-bounded-best-effort-runtime/skill.md` exists on three branches, at two
different contents, and on none of them canonically. `skills/` matches no row above. A
skill definition is closest to `prompts/`, since it is text an agent runs, but it was
created without that decision being made.

Recorded here rather than resolved: choosing the row is an `OWNER` call, and the three
copies must be reconciled before any of them is placed.

## Consolidation history

- `archive/legacy-branches/BRANCH_MANIFEST_2026-09-05.md` — the 2026-09-05 branch audit and tip dispositions.
- `archive/reconciliation/REPO_STATE_BEFORE_RECONCILIATION_2026-09-06.md` — observed state before the 2026-09-06 reconciliation.
- `archive/reconciliation/RECONCILIATION_REPORT_2026-09-06.md` — what moved, what was archived, what stayed blocked.
- `archive/legacy-branches/BRANCH_AUDIT_2026-09-05.md` — the 2026-09-05 per-branch dispositions.
- `docs/BRANCH_INVENTORY.md` — the current declaration, and the enforcement that keeps it current.

## Rule for future work

If a question cannot be answered from `main` plus explicitly labeled `archive/`, repository organization has failed.
