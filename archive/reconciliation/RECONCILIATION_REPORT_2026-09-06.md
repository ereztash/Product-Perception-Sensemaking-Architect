# Repository Reconciliation Report — 2026-09-06

Status: `RECONCILIATION_COMPLETE · TWO_ACTIVE_EXPERIMENTS_BLOCKED`
Scope: repository canonicalization and research-state reconciliation.
Not in scope: any change to an agent prompt, capability, routing rule, threshold or benchmark.

Pre-state record: `REPO_STATE_BEFORE_RECONCILIATION_2026-09-06.md`.

## 1. What was split or contradictory

`main` asserted it was the only source of truth while 43 decision-relevant research artifacts existed only on `research/system-design-decision-lane-2026-09-06`, which had accumulated 44 commits after PR 13 merged.

Five concrete contradictions:

1. `docs/CANONICAL_STATE.md` claimed every visible branch ref pointed at `main`. Three branches were ahead of it.
2. `docs/CANONICAL_STATE.md` named the next Architecture step as freezing baseline outputs in a clean runner. A staged A/B had already executed as `ARCH-AB-20260906T102435Z`, and its diagnostic result lived only on a branch.
3. `README.md` named `CAL-ARCH-001` as the current next experiment. That run had completed and been superseded twice.
4. Neither canonical document mentioned the R&D v0.2 scope hypothesis, the confirmation stream, `CONFIRMATORY_N = 0`, or the Agent Discovery closeout.
5. `runtime/calibration_loop/README.md` still headed `CAL-ARCH-001` as "First live task: Architecture Agent" after that run had decided against defining one.

## 2. Branch disposition

| Branch | Head | Classification | Disposition | Action taken |
|---|---|---|---|---|
| `main` | `51d8b2a` | canonical | remains the only source of truth | reconciliation merged into it via PR |
| `research/system-design-decision-lane-2026-09-06` | `8533222` | `CANONICAL_CANDIDATE` | recovered in full | 44 commits merged with history preserved; retire after merge |
| `research/architecture-clean-ab-2026-09-06` | `e617caf` | `ACTIVE_EXPERIMENT` | keep | PR 14 retargeted onto `main` |
| `run/claude-prerelease-prompt-telos-2026-09-06` | `5be34ad` | `ACTIVE_EXPERIMENT` | keep | documented as a live blocked run; holds no result |
| `archive/legacy-docs-2026-09-05` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead of `main` |
| `archive/legacy-snapshots` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `neta/design-research-spine-v0.1` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `neta/github-benchmark-v1` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `neta/hebrew-observatory` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `neta/hebrew-signal-fidelity` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `neta/oss-observatory` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `neta/v0.1-agent-contract` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `refoundation/neta-assurance-v0.2` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `repo/organization-canonical` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `repo/organization-canonical-v2` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `repo/organization-final` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `repo/organization-pass` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `repo/organization-pass-2` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `repo/organization-single-source` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `repo/organization-work` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `research/wave1-evidence-pass1` | `4072bb1` | `SUPERSEDED` | retire | unique documents already at `archive/legacy-branches/research-wave1-evidence-pass1/` |
| `research/wave1-triangulation` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |
| `rnd/calibration-loop-v0.1` | `4072bb1` | `SUPERSEDED` | retire | 0 commits ahead |

No branch was classified `UNKNOWN_REQUIRES_REVIEW`, and none was merged under that label.

Retirement of the 19 `SUPERSEDED` refs is a repository-owner action. Every one is a strict ancestor of `main`, so deletion loses no history. Their tips are recorded here and in `archive/legacy-branches/BRANCH_MANIFEST_2026-09-05.md`.

An earlier revision of this section said 17. The table above has always listed 19 rows, and 19 refs point at `4072bb1`. The prose count was wrong, not the table.

### Deletion attempt, 2026-09-06

Deletion was attempted after PR 16 merged and did not succeed. It is an `ENVIRONMENT` blocker, not a decision:

| Route | Result |
|---|---|
| `git push origin --delete`, batch and single ref | `HTTP 403`; ordinary pushes over the same transport succeed |
| GitHub MCP server | exposes `create_branch`, `list_branches`, `delete_file`; no delete-ref tool exists |
| `DELETE /git/refs/heads/*` | `HTTP 403`: `Write access to this GitHub API path is not permitted through this proxy.` |

None of the 19 branches is protected, and the account holds admin rights, so this is not a repository permission and not a token scope. The third route names the actual cause: the session's egress proxy allows a fixed set of GitHub API write paths, and ref deletion is not among them. The first route fails for the same reason, since the git transport passes through that proxy.

The 2026-09-05 pass recorded the same symptom and attributed it to "the GitHub tooling could move refs but could not delete them". That description was directionally right and mechanically wrong in the same way this report's first revision was: the constraint is the proxy path allowlist, not the tool and not the credential.

The practical consequence is that no permission granted to this session can complete the retirement. It has to be done from a context that does not sit behind this proxy: the GitHub Branches page, or `git push origin --delete <branch>` from the owner's own machine.

Ancestry was re-verified against `main` at `6b7d674` immediately before the attempt: all 19 contained, zero commits ahead, none protected. The safety gate passed; only the write was refused.

Three further refs became retirable when PR 16 merged and are not counted in the 19:

| Branch | Head | Why retirable now |
|---|---|---|
| `research/system-design-decision-lane-2026-09-06` | `8533222` | recovered in full by PR 16; the table above already marked it "retire after merge" |
| `claude/lichess-prerelease-gaps-qvlbv5` | `c7c0dcf` | both its passes merged as PR 15 and PR 17 |
| `claude/repo-canonicalization-reconciliation-aufvq6` | `e11c79f` | PR 16 merged, but it now carries open PR 18; retire only after that closes |

Three refs remain legitimately ahead of `main` and must not be deleted: `research/architecture-clean-ab-2026-09-06` (PR 14, 9 ahead), `run/claude-prerelease-prompt-telos-2026-09-06` (2 ahead) and `run/product-value-completion-2026-09-06` (2 ahead, opened by a separate session after this pass began).

### Owner command for the 21 currently retirable refs

```bash
git push origin --delete \
  archive/legacy-docs-2026-09-05 archive/legacy-snapshots \
  neta/design-research-spine-v0.1 neta/github-benchmark-v1 \
  neta/hebrew-observatory neta/hebrew-signal-fidelity \
  neta/oss-observatory neta/v0.1-agent-contract \
  refoundation/neta-assurance-v0.2 \
  repo/organization-canonical repo/organization-canonical-v2 \
  repo/organization-final repo/organization-pass repo/organization-pass-2 \
  repo/organization-single-source repo/organization-work \
  research/wave1-evidence-pass1 research/wave1-triangulation \
  rnd/calibration-loop-v0.1 \
  research/system-design-decision-lane-2026-09-06 \
  claude/lichess-prerelease-gaps-qvlbv5
```

Every ref in that list was verified contained in `main` at `6b7d674`. Deleting them loses no history. The list deliberately omits `claude/repo-canonicalization-reconciliation-aufvq6`, which carries open PR 18, and the three refs ahead of `main`.

## 3. Artifacts recovered into the canonical lane

All 43 were verified byte-identical to their source blobs after the merge. No status marker was raised.

### Agent Discovery — 8 files, `research/agent-discovery/`

`AGENT_DISCOVERY_PROTOCOL_V0.md`, `FUNCTION_SPACE_MAP_PASS1.md`, `AGENT_DISCOVERY_SYNTHESIS_PASS1_2026-09-06.md`, `DECISION_SUPPORT_OBSERVATORY_V0.md`, `DECISION_SUPPORT_NATURAL_SCREEN_PASS1.md`, `ARCHITECTURE_FRONT_DOOR_NATURAL_SCREEN_PASS1.md`, `AGENT_DISCOVERY_CLOSEOUT_2026-09-06.md`, `ARCHITECTURE_RESIDUAL_DECOMPOSITION_2026-09-06.md`.

### R&D epistemology — 23 files, `research/rnd-agent/epistemology/`

Source register and capability gap map; frozen transfer ablation and its run; frozen latent inquiry, VOI ranking and zetetic inquiry audit benchmarks with baseline and challenger runs; three Neta reviews; three syntheses; the applied epistemology transfer map; the calibration task.

### R&D scope discovery — 10 files, `research/rnd-agent/scope-discovery/`

Discovery task, diagnosis, program, synthesis and batch report; the Neta decomposition review; `RND_SCOPE_MAP_V0_2_FROZEN_FOR_CONFIRMATION.md`; `RND_SCOPE_CONFIRMATION_STREAM_V0_2.md`; and under `external-tests/`, the frozen outputs and external-maintainer adjudication of GitHub batch 01.

### Schemas — 2 files

`schemas/rnd-scope-case.schema.json`, `schemas/rnd-scope-case-v0.2.schema.json`.

## 4. Artifacts moved

Nine R&D telos artifacts moved from `research/rnd-agent/` into `research/rnd-agent/telos/` so the lane map reads `telos / scope-discovery / epistemology`. All nine blobs are unchanged. Two path-prefixed sibling references in `RND_TELOS_PEER_REVIEW_TASK_2026-09-06.md` were updated; every other reference was already sibling-relative and survived the move.

- `RND_TELOS_PEER_REVIEW_TASK_2026-09-06.md`
- `RND_TELOS_PEER_REVIEW_RND_DIAGNOSE_2026-09-06.md`
- `RND_TELOS_PEER_REVIEW_NETA_2026-09-06.md`
- `RND_TELOS_PEER_REVIEW_SYNTHESIS_2026-09-06.md`
- `RND_TELOS_SELF_CALIBRATION_2026-09-06.md`
- `RND_NARROW_TELOS_BENCHMARK_V0_FROZEN.md`
- `RND_NARROW_TELOS_BENCHMARK_V0_NARROW.md`
- `RND_NARROW_TELOS_BENCHMARK_V0_BROAD_REFERENCE.md`
- `RND_NARROW_TELOS_BENCHMARK_V0_ADJUDICATION.md`

### Deviation from the requested layout

The requested structure listed `external-tests/` as a sibling of `scope-discovery/`. It was left nested at `research/rnd-agent/scope-discovery/external-tests/` because those batches test that specific scope hypothesis, and `RND_SCOPE_CONFIRMATION_STREAM_V0_2.md` is a frozen artifact that references them by that relative path. Moving them would have required editing a frozen document to gain nothing epistemic. Recorded here rather than done silently.

## 5. Artifacts archived or superseded

Nothing was archived in this pass. No recovered artifact was superseded, and no draft required retirement: the research lane was purely additive against `main`, with zero modified and zero deleted files.

Three documents were rewritten in place, with their prior versions preserved in git history:

- `docs/CANONICAL_STATE.md` — rebuilt around an explicit status vocabulary;
- `README.md` — restructured, and now shorter than `CANONICAL_STATE`;
- `docs/REPOSITORY_MAP.md` — updated to the structure as it now stands.

One stale heading was corrected in `runtime/calibration_loop/README.md`.

## 6. Semantic-status audit

Every status marker in the recovered set is unchanged. Verified by blob comparison against the source branch and by direct grep:

```text
CONFIRMATORY_N = 0                    preserved
ZERO_CONFIRMATORY_CASES_COUNTED       preserved
R1..R5 = UNKNOWN                      preserved
NEW_AGENT_PROMOTED = NONE             preserved
ARCHITECTURE_AGENT = NOT_EARNED       preserved
ARCHITECTURE_SELECTION_CAPABILITY
  = UNIQUE_DELTA_NOT_SHOWN            preserved
CANDIDATE_CAPABILITY_NOT_AGENT        preserved
DISCOVERY_ONLY                        preserved
STRUCTURAL_CHANGE_ENVELOPE
  = candidate contract, unbuilt       preserved
```

Frozen prompt blobs unchanged and now CI-enforced:

```text
prompts/SYSTEM.md          339b9a1be2fd0f1f6f6c7960e5be58e5566d3691
prompts/RND_AGENT_V0_1.md  bc0e725d0449478d53b93bb6643d24404c22708c
```

No agent prompt, schema, routing rule, benchmark threshold or scoring dimension was modified. No new agent, layer, orchestrator, ontology, dashboard, database or knowledge base was created.

## 7. Drift prevention added

`scripts/check_canonical_state.py`, wired into `.github/workflows/verify.yml`. Six invariants, each with a positive control proving the gate can fail:

| Invariant | What it blocks |
|---|---|
| prompt freeze | a frozen comparator moving without its recorded hash moving |
| canonical branch rule | a decision-relevant document naming a side branch as authoritative |
| status discipline | a `CANDIDATE` or `DISCOVERY_ONLY` artifact appearing under a validated-capabilities heading |
| confirmation discipline | `CONFIRMATORY_N` rising without stated admission conditions |
| capability creep | a production file declaring an unearned agent before its promotion artifact exists |
| orchestrator status | either top-level document dropping the record that it is unbuilt |

The fifth invariant found the stale `runtime/calibration_loop/README.md` heading on its first real run.

### What these checks do not cover

They are file-level and offline. They cannot detect that a commit exists on an unmerged branch. The branch-level half of the canonical rule remains a review responsibility, backed by the "Active branches" table in `docs/CANONICAL_STATE.md` and the branch policy in `docs/REPOSITORY_MAP.md`.

## 8. Unresolved blockers

### B1 — No independent adjudication channel

`CONFIRMATORY_N` cannot rise. The environment exposes no second model lineage and no qualified human adjudicator, and same-model self-adjudication is disallowed from supporting the 95% scope claim.

Authority: `OWNER` / `ENVIRONMENT`. Not resolvable by more research.

### B2 — No explicit Copilot model in GitHub Actions

The protocol-conforming Architecture clean A/B cannot run. All five explicit model IDs in the frozen probe list returned unavailable; the rule stopped rather than substituting `auto`.

Authority: `ENVIRONMENT` / `OWNER`. Full diagnosis and the permitted and forbidden remediation classes: `eval/architecture-agent/EXECUTION_BLOCKER_2026-09-06.md`.

### B3 — No live adapter credential

The Calibration Loop cannot execute live. Run 34033377233 returned `FAILED_EXECUTION` with `OPENAI_API_KEY is required for live adapter execution`.

Authority: `ENVIRONMENT` / `OWNER`.

### B4 — No independent Hebrew HOLDOUT authority

Neta H1 has no valid run. A native-Hebrew authority must author or sample the holdout outside the tested context. H2 human annotation is commissioned but undelivered.

Authority: `OWNER` / `FIELD`.

### B5 — 19 superseded refs cannot be deleted from this session

They are strict ancestors of `main` and lose no history. Retirement is blocked by the session's egress proxy, which refuses `DELETE /git/refs/heads/*` and the equivalent `git push --delete`; see "Deletion attempt, 2026-09-06" in section 2 for the evidence and the owner command.

Counting note: 19 refs carry the `SUPERSEDED` classification from the capture snapshot. Two more became retirable after PR 16 merged, so the owner command in section 2 covers 21. The reconciliation branch itself is a twenty-second candidate but is excluded while PR 18 is open.

Authority: `OWNER`, unblocked only from outside this proxy.

B1, B2 and B3 are the same family: the repository can specify admissible evidence but cannot currently generate it. That is an honest stop, not a defect in any hypothesis.

## 9. Ambiguities recorded rather than resolved

1. **`external-tests/` placement.** Kept under `scope-discovery/`; rationale in section 4.
2. **The `run/claude-prerelease-prompt-telos` branch.** It holds a frozen calibration task and a workflow, not a result. Left unmerged as an active experiment. If it ever produces a durable trace, that trace belongs on `main`.
3. **`STRUCTURAL_CHANGE_ENVELOPE`.** The strongest current residual candidate, and explicitly not built. Its own baseline-vs-challenger test must be designed and frozen before any implementation.
4. **The v0.3 scope coding repair.** The external batch exposed a probable false-fire, where ordinary multi-hypothesis debugging was coded as nontrivial epistemic allocation. Preserved as a candidate repair to test on unseen neighbors, not retrofitted into v0.2.
5. **`research/rnd-agent/` top-level OSS files.** `OSS_TARGETED_TRANSFER_2026-09-05.md` and `OSS_TRANSFER_CLOSEOUT_2026-09-05.md` were left at the lane root rather than moved into a fourth sub-lane. The lane is closed at saturation, so a directory for it would add structure without adding a distinction.

## 10. Candidate follow-ups

Recorded, not built, per the anti-build rule:

- an offline branch-level check that no unmerged commit touches a decision-relevant path, if the CI environment gains the ability to fetch refs;
- a `STRUCTURAL_CHANGE_ENVELOPE_V0` freeze, only after its 8-12 natural-trace comparison is designed;
- a v0.3 scope map, only after new unseen neighbor cases exist to test the coding repair against.

## 11. Verification

```text
main is the only source of truth                       yes
material research result living only on a side branch  none
README and CANONICAL_STATE contradict                  no
Neta prompt changed                                    no
R&D narrow hypothesis promoted to canonical            no
CONFIRMATORY_N                                         0, unchanged
Agent Discovery closeout present on the canonical lane yes
third peer added                                       no
Architecture status                                    candidate capability, not agent
PR 14 based on current canonical state                 yes, retargeted onto main
Architecture benchmark failure classified              environment/execution blocker
contract CI                                            green
```

## 12. Parallel work that opened during this pass

`claude/lichess-prerelease-gaps-qvlbv5` (PR 15) was pushed at 12:52 UTC on 2026-09-06, after the Phase 0 snapshot was taken. It is one commit, based on current `main`, CI green.

It carries durable artifacts that belong on `main`:

- `runtime/execution_traces/DEL-LICHESS-RELEASE-STALE-PR-001.json` — `WAIT_AUTHORITY`, ENVIRONMENT;
- `runtime/execution_traces/DEL-LICHESS-FIELD-INSTRUMENT-001.json` — `STOP`, FIELD;
- `runtime/handoffs/HANDOFF-LICHESS-ENV-001.json`;
- `runtime/handoffs/HANDOFF-LICHESS-FIELD-001.json`;
- `research/lichess-prerelease/PRERELEASE_GAP_PASS_2026-09-06.md`.

They are the first real `DECISION → EXECUTION → VERIFIED STATE → OUTCOME → LEARNING` traces against an external product target, and they count toward the 10-15 traces required before an execution capability becomes eligible.

### Collision

Both pull requests edit two files:

| File | PR 15 | PR 16 |
|---|---|---|
| `docs/CANONICAL_STATE.md` | adds an "External-target execution traces" section after the execution-contract section | rewrites the whole file around an explicit status vocabulary |
| `.github/workflows/verify.yml` | adds a step validating the two lichess traces, after the Architecture corpus step | adds a step running the canonicalization invariants, after the Neta finding step |

The workflow edits are in different regions and should merge cleanly. The `CANONICAL_STATE.md` edits will conflict, because PR 16 rewrote the surrounding text.

### Resolution

The two changes are semantically compatible. Neither raises a status, and PR 15's section documents artifacts PR 16 does not mention.

Recommended order: **merge PR 15 first, then PR 16.** PR 16 then resolves one conflict by re-inserting PR 15's "External-target execution traces" section verbatim, under the rewritten Decision → Execution → Learning heading.

The reverse order also works but is worse: it would put a `CANONICAL_STATE.md` on `main` that references trace and handoff files not yet present, which is exactly the dangling-reference failure this reconciliation exists to remove.

PR 15's content was deliberately **not** copied into PR 16. Copying the documentation without the data files it references would create that dangling reference, and PR 15 is another author's open work.

### Outcome

The recommended order held. PR 15 merged at 13:09 UTC (`main` = `75ebdf8`) and a second pass, PR 17, merged at 13:23 UTC (`main` = `e6f770e`) before this branch had integrated the first. Both were taken in one merge rather than two, so the conflict was resolved once against final state.

What actually happened:

| File | Result |
|---|---|
| `.github/workflows/verify.yml` | auto-merged as predicted; the canonicalization invariant step and all five lichess trace validations are present |
| `docs/CANONICAL_STATE.md` | conflicted as predicted; the rewritten structure was kept and `main`'s "External-target execution traces" section re-inserted verbatim under the rewritten heading |

PR 17 expanded the section PR 15 introduced: five traces instead of two, a second ENVIRONMENT handoff superseding the first, a field run sheet, and three recalibrations instead of one. The expanded version is what was carried across, byte-identical to `main`.

Two follow-on edits were required because the merge made this branch's own text false:

- the `claude/lichess-prerelease-gaps-qvlbv5` row was removed from the Active branches table, since the branch is no longer ahead of `main`;
- the collision note now records the merge rather than predicting it.

No status moved on either side. All ten lichess artifacts are byte-identical to `main`, all 43 recovered research artifacts remain present, and the frozen prompt blobs are unchanged.
