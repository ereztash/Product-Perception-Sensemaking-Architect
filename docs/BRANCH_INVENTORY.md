# Branch Inventory

Status: `CANONICAL`
Captured: 2026-09-08, after the retirement and the branch-by-branch read
Captured against: `main` @ `04574ab10e76f56cb30302d47114565bcc9f34ae`

This file is the branch-level half of the canonical rule. `docs/REPOSITORY_MAP.md` states
the rule; `scripts/check_branch_inventory.py` enforces it; this file is the declaration
the enforcement compares reality against.

## Why this file exists

`archive/reconciliation/RECONCILIATION_REPORT_2026-09-06.md`, section 8, recorded the hole:

> They are file-level and offline. They cannot detect that a commit exists on an unmerged
> branch. The branch-level half of the canonical rule remains a review responsibility.

Review responsibility drifted. On 2026-09-06 two branches were declared active. On
2026-09-08 twelve were ahead of `main`, carrying 69 files that existed nowhere else, and
nothing in CI could see it. That count is the observation that produced this file, not a
live number; the tables below are the live number.

A declaration that no instrument checks is not a rule. It is a note.

## Disposition vocabulary

| Disposition | Meaning | Action it implies |
|---|---|---|
| `RETIRABLE` | Strict ancestor of `main`. Deletion loses no history. | Owner deletes; see `docs/BRANCH_RETIREMENT_RUNBOOK.md`. Currently unused: no branch holds this disposition. |
| `OPEN_PR_TO_MAIN` | Ahead of `main`, open pull request targeting `main`. | Merge or close the pull request. |
| `OPEN_PR_TO_BRANCH` | Ahead of `main`, open pull request targeting a side branch. | Its content cannot reach `main` through that pull request. Retarget or reopen against `main`. |
| `SUPERSEDED` | Ahead of `main`, but every path unique to it also exists on a named successor branch. | Retire when the successor lands. Deleting it before that loses nothing the successor does not hold. |
| `STRANDED` | Ahead of `main`, no open pull request. Artifacts exist only here. | Recover to `main`, copy to `archive/`, or record why neither. |

A branch carrying an unfinished experiment is not thereby exempt. `STRANDED` describes
where the bytes live, not whether the work was worth doing.

### Two states the checker does not fail on

**Within the first 24 hours.** A branch may exist undeclared while its newest commit is under
a day old. The invariant is that nothing decision-relevant lives *only* on a side branch, not
that a branch is declared before its first push. Requiring declaration up front would redden
every open pull request the moment a `run/` branch is created to drive a workflow, which is
how a checker gets switched off. Past a day, an undeclared branch fails.

**Merged.** `OPEN_PR_TO_MAIN` is the one disposition whose expected end state is reaching
`main`. A branch in that state that becomes contained, or disappears, has succeeded; the
checker reports it as merged and asks for its row to be removed. Every other disposition
still fails on both, because for them containment or disappearance is drift.

## Retirable — contained in `main`

None. The retirable lane is empty.

## Retired on 2026-09-08

Every tip below was verified with `git merge-base --is-ancestor <tip> origin/main`
immediately before deletion; all twenty-one were strict ancestors, so no history was lost.
The owner deleted all twenty-one on 2026-09-08 and the remote went from thirty-five branches
to fifteen. These rows are lineage: the refs no longer exist, and nothing here is a live
declaration.

| Branch | Tip | Origin |
|---|---|---|
| `archive/legacy-docs-2026-09-05` | `4072bb1282` | 2026-09-05 consolidation |
| `archive/legacy-snapshots` | `4072bb1282` | 2026-09-05 consolidation |
| `claude/lichess-prerelease-gaps-qvlbv5` | `c7c0dcf243` | merged as PR 15 and PR 17 |
| `neta/design-research-spine-v0.1` | `4072bb1282` | merged as PR 8 |
| `neta/github-benchmark-v1` | `4072bb1282` | benchmark protocol merged |
| `neta/hebrew-observatory` | `4072bb1282` | H2 observatory merged |
| `neta/hebrew-signal-fidelity` | `4072bb1282` | H1 benchmark merged |
| `neta/oss-observatory` | `4072bb1282` | BATCH-001..016 and closeout merged |
| `neta/v0.1-agent-contract` | `4072bb1282` | merged as PR 1 |
| `refoundation/neta-assurance-v0.2` | `4072bb1282` | assurance re-foundation merged |
| `repo/organization-canonical` | `4072bb1282` | superseded organization pass |
| `repo/organization-canonical-v2` | `4072bb1282` | superseded organization pass |
| `repo/organization-final` | `4072bb1282` | superseded organization pass |
| `repo/organization-pass` | `4072bb1282` | superseded organization pass |
| `repo/organization-pass-2` | `4072bb1282` | superseded organization pass |
| `repo/organization-single-source` | `4072bb1282` | superseded organization pass |
| `repo/organization-work` | `4072bb1282` | superseded organization pass |
| `research/system-design-decision-lane-2026-09-06` | `8533222ac2` | recovered in full by PR 16 |
| `research/wave1-evidence-pass1` | `4072bb1282` | artifacts under `archive/legacy-branches/` |
| `research/wave1-triangulation` | `4072bb1282` | superseded by Wave 1 closeout |
| `rnd/calibration-loop-v0.1` | `4072bb1282` | calibration loop merged |

Seven of those names describe the same job attempted seven times. That is the finding this
file was opened on: the 2026-09-05 audit dispositioned nineteen of these refs
`MERGED_SAFE_TO_DELETE`, and for three days none was deleted, because the deletion write is
refused in every agent session and the owner action was never surfaced as one command.
`docs/BRANCH_RETIREMENT_RUNBOOK.md` records the blocker, the procedure and this execution.

## Ahead of `main`

| Branch | Tip | Unique paths | Disposition |
|---|---|---|---|
| `claude/product-value-completion-run-if7ito` | `b358884a97` | 31 | `OPEN_PR_TO_BRANCH` |
| `claude/repo-canonicalization-reconciliation-aufvq6` | `7c5465ae61` | 0 | `OPEN_PR_TO_MAIN` |
| `research/architecture-clean-ab-2026-09-06` | `e617caff68` | 4 | `OPEN_PR_TO_MAIN` |
| `research/rnd-self-triangulation-challenges-2026-09-08` | `9756465715` | 17 | `STRANDED` |
| `research/rnd-self-triangulation-adjudication-2026-09-08` | `dd59bf7ae1` | 12 | `STRANDED` |
| `research/rnd-self-triangulation-2026-09-08` | `e56b74d766` | 11 | `SUPERSEDED`, superseded by `research/rnd-self-triangulation-challenges-2026-09-08` |
| `run/meta-calibrate-best-effort-reasoning-2026-09-08` | `bd0ae563d7` | 7 | `STRANDED` |
| `run/self-calibrate-best-effort-skill-2026-09-08` | `1896497474` | 5 | `SUPERSEDED`, superseded by `run/meta-calibrate-best-effort-reasoning-2026-09-08` |
| `run/lichess-premove-ownership-copilot-2026-09-07` | `9badd02a2b` | 3 | `SUPERSEDED`, superseded by `run/meta-calibrate-best-effort-reasoning-2026-09-08` |
| `skill/evidence-bounded-best-effort-runtime` | `e022cc642f` | 1 | `STRANDED` |
| `run/product-value-completion-2026-09-06` | `bdaba4849d` | 8 | `SUPERSEDED`, superseded by `claude/product-value-completion-run-if7ito` |
| `run/delta-v02-batch-2026-09-08` | `db5d10676e` | 5 | `STRANDED` |
| `run/lichess-whitepaper-calibration-2026-09-06` | `4be4625f9a` | 4 | `STRANDED` |
| `run/claude-prerelease-prompt-telos-2026-09-06` | `5be34ad7fd` | 2 | `STRANDED` |
| `feat/resource-delta-accounting-v0-2` | `9f1cf9bf65` | 0 | `SUPERSEDED`, superseded by `main` |
| `claude/repo-cleanup-590u82` | `04574ab10e` | 2 | `OPEN_PR_TO_MAIN` |

Tips in this table are last-observed values, not pins. An active branch is expected to
receive commits, and `scripts/check_branch_inventory.py --live` reports such movement
without failing. A `RETIRABLE` tip is pinned: the runbook would be about to delete that
ref, and a ref that moved since capture may no longer be contained in `main`.

### PR 19 cannot reach `main`

PR 19 has head `claude/product-value-completion-run-if7ito` and base
`run/product-value-completion-2026-09-06`. Both are ahead of `main`. Merging PR 19
moves 31 files from one side branch to another. No pull request currently targets
`main` from either.

This is the structural version of the drift: the work looks reviewed, and the review
terminates outside the canonical lane.

### Forked artifacts with no canonical copy

The same four artifacts exist on several branches, at different contents, with no copy
on `main`. Nothing selects between the versions.

| Artifact | Branches | Distinct contents |
|---|---|---|
| `.github/workflows/best-effort-lichess-copilot.yml` | 3 | 3 |
| `skills/evidence-bounded-best-effort-runtime/skill.md` | 3 | 2 |
| `runtime/calibration_loop/copilot_resource_adapter.py` | 3 | 1 |
| `runtime/calibration_loop/copilot-config.best-effort.json` | 3 | 1 |
| `runtime/calibration_loop/copilot_resource_adapter_v02.py` | 2 | 1 |
| `runtime/calibration_loop/copilot-config-v02.best-effort.json` | 2 | 1 |

The `_v02` rows are a second generation of the same adapter, carried identically by
`run/delta-v02-batch-2026-09-08` and `research/rnd-self-triangulation-2026-09-08`. Neither
generation is on `main`, so a change to the adapter now has six side-branch copies to chase
and no canonical one to change.

`research/rnd-self-triangulation-2026-09-08` was pushed on 2026-09-08 at 14:26, after this
inventory was first written. `scripts/check_branch_inventory.py --live` failed on it within
the hour, which is the first observation the instrument produced that review had not already
made.

`skills/` does not appear in the placement table in `docs/REPOSITORY_MAP.md`. A directory
that exists on three branches and in no rule is a placement question, not a file question.

## Branch-by-branch read, 2026-09-08

Every branch was read. "Unique paths" counts paths that exist on the branch and nowhere on
`main`, compared tree to tree. It is the number that matters, because a branch can sit many
commits ahead and still hold nothing: `feat/resource-delta-accounting-v0-2` is six commits
ahead and has zero unique paths, since `main` took its work as the squash `74fc4af`. A
commit count is not evidence of content.

### Four branches hold nothing their successor does not

Verified with `git merge-base --is-ancestor`: each is a strict ancestor of the successor
named in its row. Deleting any of them before its successor lands loses nothing.

Sixteen open questions become twelve.

### The adjudication rubric and the result it grades are on different branches

`research/rnd-self-triangulation-adjudication-2026-09-08` carries
`RND_SELF_TRIANGULATION_CHALLENGE_RUBRIC_1.md`, frozen to adjudicate the blind challenges.

`research/rnd-self-triangulation-challenges-2026-09-08` carries the challenges `C1` to `C4`
and `RND_SELF_TRIANGULATION_CHALLENGE_RESULT_1.md`.

Neither branch contains the other. From either one alone, the blind result cannot be graded
against its own frozen rubric. Both were pushed within an hour of this read, so this is a
live research program, not archaeology, and the split is `OWNER`'s to resolve.

### The skill has two versions and the newer one is on the smaller branch

`skills/evidence-bounded-best-effort-runtime/skill.md` is 205 lines on
`skill/evidence-bounded-best-effort-runtime` and 140 lines on the two `run/` branches. The
205-line version is the later one: it was committed as "tighten best-effort skill after
self-calibration". A merge that took the run branches' copy would silently revert that
refinement.

`skills/` still matches no row in the placement table in `docs/REPOSITORY_MAP.md`.

### PR 19 still cannot reach `main`

Its base is `run/product-value-completion-2026-09-06`, which this read confirms is fully
contained in PR 19's own head. The base branch holds nothing the head does not. Retargeting
PR 19 at `main` would both unblock its 31 files and make the base branch retirable.

### What is decided and what is not

Decided here: which branches hold nothing, and what each remaining branch actually contains.

Not decided here: whether the twelve remaining branches should be recovered into `main` or
copied under `archive/`. Each holds real content, several are being written to now, and one
belongs to a parallel session's open pull request. That is an `OWNER` decision per branch,
and taking it inside a repository-organization pass would be the same encodability bias the
kernel forbids.

## What this inventory does not claim

It does not say the stranded work is good, bad, finished or admissible. It does not
promote anything. It records where bytes live relative to `main`, and which of those
locations violate the rule the repository already wrote down.

Recovery, archival or abandonment of any branch above is an `OWNER` decision and is not
taken here.
