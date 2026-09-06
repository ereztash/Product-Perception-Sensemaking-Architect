# Evidence-Bounded Peer-Agent System

Two peer agents under one shared epistemic constitution, with a deterministic coordination runtime and no orchestrator.

> **`main` is the only source of truth.**

No decision-relevant research result, prompt rule, contract or runtime may live only on a side branch. Full component state lives in `docs/CANONICAL_STATE.md`; this file is the short map.

## 1. Telos

> **Remove material uncertainty from consequential decisions while preserving the lineage needed to understand, challenge, reverse and reuse what was learned.**

The unit of progress is **material uncertainty removed from a live decision**. Not code written, sources collected, instruments built, agents added or prompts expanded.

Full statement: `docs/ECOSYSTEM_TELOS.md`.

## 2. Current architecture

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
```

Neta and R&D are peers. Call order does not create hierarchy. `SCAFFOLD` is external broad reasoning borrowed when cheaper than internalizing; it is not ground truth.

The shared kernel carries `Claim → Evidence → Reality → Resolution Authority → Requested Use → Permission → Reversal / Stop`. Resolution authorities are `OWNER`, `REPO`, `ENVIRONMENT`, `RESEARCH`, `FIELD`.

- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `docs/AGENT_AUTHORITY_BOUNDARIES.md`
- `docs/PEER_HANDOFF_PROTOCOL.md`
- `docs/REALITY_AUTHORITY_PERMISSION.md`
- `schemas/epistemic-claim.schema.json`
- `schemas/peer-handoff.schema.json`

## 3. Neta

Turns raw product/design intuition into a bounded distinction without letting interpretation outrun evidence.

```text
RAW SIGNAL → CONCRETE MOMENT → OBSERVABLE → COMPETING MECHANISMS
→ CHEAP DISCRIMINATOR → DESIGN DISTINCTION → INTERVENTION / DEFER / FIELD
```

- method: v0.2 assurance re-foundation;
- prompt: **frozen v0.1** at `prompts/SYSTEM.md`. No core prompt update has been earned;
- promotion gate: `eval/CAPABILITY_UPDATE_GATE_V1.md`;
- GitHub Wave 1: closed at saturation, 0 prompt updates;
- Hebrew H1 and H2: frozen, awaiting an independent holdout/annotation authority.

Neta is not a research authority and cannot manufacture FIELD evidence.

## 4. R&D

Three states, held apart on purpose.

### v0.1 — frozen comparator

`LIVE CLAIM → RECOVER → REUSE/ADAPT/BUILD → RUN → DEPOSIT → CLAIM DISPOSITION → STOP/HANDOFF`

`prompts/RND_AGENT_V0_1.md`, `research/RND_AGENT_CHARTER_V0_1.md`, `eval/rnd-agent/`.

### v0.2 broad — implementation candidate

What the system runs today. Not validated by being used.

> **Improve the fit between system resources and the live telos, given the actual current state.**

`prompts/RND_AGENT_V0_2_CANDIDATE.md`, `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`.

### Narrow scope — research hypothesis only

```text
CONSEQUENTIAL DECISION × NONTRIVIAL EPISTEMIC ALLOCATION → R&D CORE CANDIDATE
```

Frozen for testing at `CONFIRMATORY_N = 0`. It has not replaced the broad formulation. See section 6.

## 5. Calibration Loop

`runtime/calibration_loop/` is the coordination layer. It is deliberately **not an agent**.

```text
TASK → R&D DIAGNOSE → DETERMINISTIC ROUTING
 ├─ NETA       only on discrimination/proxy/intervention triggers
 ├─ SCAFFOLD   only when broad reasoning is worth borrowing
 └─ OWNER/REPO/ENVIRONMENT/FIELD handoff when required
→ R&D SYNTHESIZE → TRACE + RESOURCE DELTAS + LEARNING RECORD
```

The runner may record a proposed routing change. It may not self-modify the routing law from one attractive case. It stops at `PENDING_RESOURCE`, `AUTHORITY_STOP` or `FAILED_EXECUTION` rather than fabricate an answer.

`schemas/calibration-task.schema.json`, `scripts/check_calibration_loop.py`, `fixtures/calibration-valid-task.json`.

## 6. Active hypotheses

Each is frozen, testable and unpromoted.

| Hypothesis | Status | What would settle it |
|---|---|---|
| R&D value concentrates at consequential decision × nontrivial epistemic allocation | `CONFIRMATORY_N = 0`, all five regions `UNKNOWN` | admissible cases judged blind by an independent model lineage or qualified human |
| The Architecture Decision Discriminator adds material delta over the strongest composed baseline | `UNIQUE_DELTA_NOT_SHOWN` | the protocol-conforming clean A/B, then unseen HOLDOUT |
| The real residual is a structural transition contract, not an architecture decision-maker | `STRONGEST_NEW_RESIDUAL_CANDIDATE` | a frozen baseline-vs-challenger test on 8-12 natural structural-change traces |

Nothing in this table may be cited as a finding.

## 7. Active experiments

| Experiment | Branch | State |
|---|---|---|
| Architecture clean A/B | `research/architecture-clean-ab-2026-09-06` (PR 14) | `EXECUTION_BLOCKED` — no explicit Copilot model available in the Actions environment; the frozen protocol stopped rather than substituting `auto` |
| Live Calibration Loop run on an external prompt telos | `run/claude-prerelease-prompt-telos-2026-09-06` | `FAILED_EXECUTION` — no live adapter credential in the environment |

Both are execution/environment blockers, not research results. Diagnosis: `eval/architecture-agent/EXECUTION_BLOCKER_2026-09-06.md`.

## 8. What is explicitly not built

Learned Orchestrator. Third peer. Architecture Agent. Execution Agent. Requirements Agent. Decision Support capability.

Each is `NOT_EARNED` with a written condition that would change that, listed in `docs/CANONICAL_STATE.md`. Broad agent discovery is closed at saturation: `research/agent-discovery/AGENT_DISCOVERY_CLOSEOUT_2026-09-06.md`.

"We can build it" is never sufficient permission.

## 9. Where current truth lives

```text
docs/       canonical architecture, authority, state and repository map
prompts/    frozen and candidate agent prompts
schemas/    shared, peer and runtime contracts
runtime/    executable coordination, adapters and traces
research/   non-canonical research programs and syntheses
eval/       frozen benchmarks, promotion gates and scoring
fixtures/   test inputs
scripts/    validators and CI checks
memory/     bounded owner-language priors
archive/    superseded history and reconciliation records
```

Read in this order:

1. `docs/CANONICAL_STATE.md` — what is true now, and at what evidence status;
2. `docs/REPOSITORY_MAP.md` — where things belong and the branch policy;
3. `docs/SHARED_EPISTEMIC_KERNEL.md` — the constitution;
4. `CLAUDE.md` — working rules for changing any of it.

Nothing under `research/` is canonical. Nothing under `archive/` is current authority.

### Branch policy

- `main` is the only long-lived authoritative branch;
- work branches are temporary and carry one named purpose;
- before retirement, decision-relevant artifacts must be merged to `main` or copied under `archive/`;
- a branch that exists proves nothing about runnability or authority.

Consolidation records: `archive/legacy-branches/BRANCH_MANIFEST_2026-09-05.md` and `archive/reconciliation/RECONCILIATION_REPORT_2026-09-06.md`.

## Verify

```bash
python scripts/check_contract.py
python scripts/check_research_contract.py
python scripts/check_rnd_contract.py
python scripts/check_canonical_state.py
```

CI runs the full contract suite in `.github/workflows/verify.yml`.

---

**ONE CANONICAL MAIN · TWO PEERS · SHARED EPISTEMIC KERNEL · DETERMINISTIC CALIBRATION LOOP · R&D v0.2 CANDIDATE · ARCHITECTURE CANDIDATE CAPABILITY · CONFIRMATORY_N = 0 · ORCHESTRATOR DEFERRED.**
