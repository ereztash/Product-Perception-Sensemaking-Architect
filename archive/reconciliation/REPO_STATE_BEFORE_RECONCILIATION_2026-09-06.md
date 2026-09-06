# Repository State Before Reconciliation — 2026-09-06

Status: `PRE_RECONCILIATION_SNAPSHOT · READ_ONLY_RECORD`
Captured: 2026-09-06, before any merge, move, rebase or edit in this pass.

This file records observed Git/GitHub state. It makes no research claim and promotes nothing.

## Canonical head at capture time

```text
main                    = 51d8b2a3e845791bf07fa09115cbe9fcdf054da9
main subject            = Merge pull request #13 from ereztash/research/system-design-decision-lane-2026-09-06
main committed          = 2026-09-06T10:17:55+03:00
reconciliation branch   = claude/repo-canonicalization-reconciliation-aufvq6
reconciliation base     = 51d8b2a3e845791bf07fa09115cbe9fcdf054da9
```

## Branch inventory

Ahead/behind are measured against `origin/main` at capture time.

| Branch | Head | Ahead | Behind | Classification |
|---|---|---:|---:|---|
| `archive/legacy-docs-2026-09-05` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `archive/legacy-snapshots` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `neta/design-research-spine-v0.1` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `neta/github-benchmark-v1` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `neta/hebrew-observatory` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `neta/hebrew-signal-fidelity` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `neta/oss-observatory` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `neta/v0.1-agent-contract` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `refoundation/neta-assurance-v0.2` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `repo/organization-canonical` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `repo/organization-canonical-v2` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `repo/organization-final` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `repo/organization-pass` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `repo/organization-pass-2` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `repo/organization-single-source` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `repo/organization-work` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `research/architecture-clean-ab-2026-09-06` | `e617caf` | 52 | 1 | `ACTIVE_EXPERIMENT` |
| `research/system-design-decision-lane-2026-09-06` | `8533222` | 44 | 1 | `CANONICAL_CANDIDATE` |
| `research/wave1-evidence-pass1` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `research/wave1-triangulation` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `rnd/calibration-loop-v0.1` | `4072bb1` | 0 | 62 | `SUPERSEDED` |
| `run/claude-prerelease-prompt-telos-2026-09-06` | `5be34ad` | 2 | 0 | `ACTIVE_EXPERIMENT` |

### Classification rules used

- `CANONICAL_CANDIDATE` — carries decision-relevant artifacts absent from `main`; content is a strict superset of `main`; eligible for recovery.
- `ACTIVE_EXPERIMENT` — carries a live, unfinished experiment; not eligible for automatic recovery until the experiment is runnable and understood.
- `SUPERSEDED` — zero commits ahead of `main`; every commit is already an ancestor of `main`; safe to retire.
- `HISTORICAL_ONLY` — none observed at capture time.
- `UNKNOWN_REQUIRES_REVIEW` — none observed at capture time. No branch was merged under this label.

All 17 `SUPERSEDED` refs point at `4072bb1`, an earlier ancestor of `main`. They are the residue of the 2026-09-05 consolidation described in `archive/legacy-branches/BRANCH_MANIFEST_2026-09-05.md`, where the GitHub tooling could move refs but could not delete them.

## Open pull requests at capture time

| PR | Title | Head | Base | State | Note |
|---|---|---|---|---|---|
| 14 | Run clean Architecture A/B benchmark | `research/architecture-clean-ab-2026-09-06` @ `e617caf` | `research/system-design-decision-lane-2026-09-06` | open | base is a research branch, not `main` |

Closed/merged pull requests 1-13 are lineage only. PR 13 merged into `main` at `51d8b2a`; its head branch then received 44 further commits that never reached `main`.

## Branch-only decision-relevant state at capture time

### `research/system-design-decision-lane-2026-09-06` — 43 files, additive only

`git diff --name-status origin/main...origin/research/system-design-decision-lane-2026-09-06` reports 43 entries, all `A`. Zero files modified, zero deleted. The branch is a strict content superset of `main`.

Groups:

- `research/agent-discovery/` — 8 files, including the broad Agent Discovery closeout and the post-A/B Architecture residual decomposition;
- `research/rnd-agent/epistemology/` — 23 files, epistemology/applied-epistemology/VOI transfer tests, frozen benchmarks, runs, Neta reviews and syntheses;
- `research/rnd-agent/scope-discovery/` — 10 files, including the frozen v0.2 scope hypothesis, the confirmation stream and the external GitHub outcome batch;
- `schemas/` — 2 files, `rnd-scope-case.schema.json` and `rnd-scope-case-v0.2.schema.json`.

### `research/architecture-clean-ab-2026-09-06` — 5 files beyond the research lane

- `.github/workflows/verify.yml` (modified: adds a `copilot-requests: write` permission and an isolated `architecture-clean-ab` job);
- `eval/architecture-agent/CLEAN_AB_EXECUTION_PROTOCOL_V0.md`;
- `eval/architecture-agent/CLEAN_AB_EXECUTION_PROTOCOL_V0_1_AMENDMENT.md`;
- `eval/architecture-agent/CLEAN_AB_EXECUTION_PROTOCOL_V0_2_MODEL_SELECTION.md`;
- `scripts/run_architecture_clean_ab.py`.

### `run/claude-prerelease-prompt-telos-2026-09-06` — 2 files, additive only

- `.github/workflows/run-claude-prerelease-prompt-telos.yml`;
- `fixtures/calibration-claude-prerelease-prompt-telos-2026-09-06.json`.

This branch is 2 ahead and 0 behind `main`. It is a live Calibration Loop run against an external object, not a repository result.

## Diverged files

None. No file on any ahead-branch conflicts with `main`. `git merge-tree --write-tree origin/main origin/research/system-design-decision-lane-2026-09-06` returns a clean tree with no conflict record.

## CI status at capture time

| Workflow run | Branch | Head | Conclusion | Note |
|---|---|---|---|---|
| 98 | `main` | `51d8b2a` | success | contract job green on canonical head |
| 102 | `research/architecture-clean-ab-2026-09-06` | `6f658a0` | success | contract job green |
| 103 | `research/architecture-clean-ab-2026-09-06` | `9bb6397` | failure | `architecture-clean-ab` job only |
| 104 | `research/architecture-clean-ab-2026-09-06` | `5c5f24f` | failure | `architecture-clean-ab` job only |
| 105 | `research/architecture-clean-ab-2026-09-06` | `e617caf` | failure | 2 jobs, 1 failed: `contract` passed, `architecture-clean-ab` failed |
| 1 | `run/claude-prerelease-prompt-telos-2026-09-06` | `5be34ad` | failure | live calibration adapter |

The repository contract job is green on every head where it ran. The two failures are execution-environment failures in benchmark/live-run jobs, recorded verbatim below.

### Failure 1 — Architecture clean A/B, run 34027916604

```text
MODEL_UNAVAILABLE gpt-5.4
MODEL_UNAVAILABLE claude-sonnet-4.6
MODEL_UNAVAILABLE gpt-5-mini
MODEL_UNAVAILABLE claude-haiku-4.5
MODEL_UNAVAILABLE gemini-3.5-flash
No explicit Copilot model is available; auto is inadmissible for the frozen same-model protocol.
Process completed with exit code 1.
```

The frozen v0.2 selection rule stopped rather than substituting `auto`. No benchmark case was loaded. No GOLD was read. No output was produced.

### Failure 2 — live calibration, run 34033377233

```text
"final_state": "FAILED_EXECUTION",
"failure": "RND adapter failed: {\"adapter_error\": \"OPENAI_API_KEY is required for live adapter execution\"}"
```

The runtime returned `FAILED_EXECUTION` rather than fabricating a result.

## Contradictions observed before reconciliation

1. `README.md` and `docs/CANONICAL_STATE.md` both assert that `main` is the only source of truth, while 43 decision-relevant research artifacts existed only on a side branch.
2. `docs/CANONICAL_STATE.md` states that "every visible branch ref points to the same commit as `main`". Three branches were ahead of `main` at capture time.
3. `docs/CANONICAL_STATE.md` names the next Architecture step as freezing baseline outputs in a clean runner. A staged A/B had in fact already executed on 2026-09-06 as `ARCH-AB-20260906T102435Z`, and its result is recorded only in a branch-only artifact.
4. `README.md` names `CAL-ARCH-001` as the current next experiment. That run had already completed and had been superseded by the clean A/B and then by the change-envelope hypothesis, both branch-only.
5. Neither canonical document mentions the R&D v0.2 scope hypothesis, the confirmation stream, `CONFIRMATORY_N = 0`, or the Agent Discovery closeout.
