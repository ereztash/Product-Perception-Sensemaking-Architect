# Branch Inventory

Status: `CANONICAL`
Captured: 2026-09-09, after re-measuring every count tree to tree
Captured against: `main` @ `5e156cd291da2eedfe415fd7340dcc545af44d1f`

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

"New files" counts paths that exist in the branch tree at the tip below and in no path of
the `main` tree at the anchor above. Both sides are pinned commits, so each row stays
checkable as branches move. `scripts/check_branch_inventory.py --live` recomputes every
one of these numbers and fails on any that does not match.

| Branch | Tip | Ahead | New files | Disposition |
|---|---|---|---|---|
| `claude/product-value-completion-run-if7ito` | `1ceec96412` | 15 | 31 | `OPEN_PR_TO_MAIN` |
| `claude/repo-canonicalization-reconciliation-aufvq6` | `dabb85a27a` | 12 | 0 | `OPEN_PR_TO_MAIN` |
| `claude/repo-cleanup-590u82` | `120946bb4c` | 4 | 4 | `OPEN_PR_TO_MAIN` |
| `claude/ux-ui-analysis-v6ao5u` | `ab453a448b` | 1 | 1 | `OPEN_PR_TO_MAIN` |
| `feat/resource-delta-accounting-v0-2` | `9f1cf9bf65` | 6 | 1 | `SUPERSEDED`, superseded by `main` |
| `research/architecture-clean-ab-2026-09-06` | `e617caff68` | 9 | 14 | `OPEN_PR_TO_MAIN` |
| `research/rnd-self-triangulation-2026-09-08` | `bf346508d2` | 17 | 17 | `STRANDED` |
| `research/rnd-self-triangulation-adjudication-2026-09-08` | `dd59bf7ae1` | 13 | 13 | `SUPERSEDED`, superseded by `research/rnd-self-triangulation-anti-adjudication-2026-09-08` |
| `research/rnd-self-triangulation-anti-adjudication-2026-09-08` | `45e4019676` | 15 | 15 | `STRANDED` |
| `research/rnd-self-triangulation-anti-challenges-2026-09-08` | `3b51465235` | 23 | 23 | `STRANDED` |
| `research/rnd-self-triangulation-challenges-2026-09-08` | `9756465715` | 18 | 18 | `SUPERSEDED`, superseded by `research/rnd-self-triangulation-anti-challenges-2026-09-08` |
| `run/claude-prerelease-prompt-telos-2026-09-06` | `5be34ad7fd` | 2 | 12 | `STRANDED` |
| `run/delta-v02-batch-2026-09-08` | `c064fa1d58` | 10 | 9 | `STRANDED` |
| `run/lichess-premove-ownership-copilot-2026-09-07` | `9badd02a2b` | 6 | 4 | `SUPERSEDED`, superseded by `run/meta-calibrate-best-effort-reasoning-2026-09-08` |
| `run/lichess-whitepaper-calibration-2026-09-06` | `4be4625f9a` | 4 | 5 | `STRANDED` |
| `run/meta-calibrate-best-effort-reasoning-2026-09-08` | `bd0ae563d7` | 14 | 8 | `STRANDED` |
| `run/product-value-completion-2026-09-06` | `bdaba4849d` | 3 | 9 | `SUPERSEDED`, superseded by `claude/product-value-completion-run-if7ito` |
| `run/self-calibrate-best-effort-skill-2026-09-08` | `1896497474` | 9 | 6 | `SUPERSEDED`, superseded by `run/meta-calibrate-best-effort-reasoning-2026-09-08` |
| `skill/evidence-bounded-best-effort-runtime` | `e022cc642f` | 2 | 2 | `STRANDED` |

Tips in this table are last-observed values, not pins. An active branch is expected to
receive commits, and `scripts/check_branch_inventory.py --live` reports such movement
without failing; the new-file count stays true because it is measured at the tip the row
names. A `RETIRABLE` tip is pinned: the runbook would be about to delete that ref, and a
ref that moved since capture may no longer be contained in `main`.

## Relocations

`main` carries these paths under a different name. A branch that predates the move still
holds the old path, which is not a path that exists only on that branch. The exemption is
declared here so `scripts/check_branch_inventory.py --live` can verify it: the canonical
path must exist on `main` and the old path must not.

| Path on side branches | Canonical path on `main` |
|---|---|
| `docs/BRANCH_AUDIT_2026-09-05.md` | `archive/legacy-branches/BRANCH_AUDIT_2026-09-05.md` |

Fifteen of the eighteen branches carry the old path, all at one identical blob. `main`
holds a later copy: it spells out the three `archive/legacy-branches/` filenames the
side-branch copy names bare. The exemption covers this one path and nothing else, so it
cannot be widened into a blanket excuse for a stale branch.

## The counts in this file were wrong until 2026-09-09

The first version of this table published `git diff --diff-filter=A --name-only
main...branch`. Three-dot compares against the merge base, so it reports nothing for work
`main` absorbed as a squash and nothing for paths the branch has carried since before the
fork point. The prose above the table said "compared tree to tree". The two do not agree.

Eleven of sixteen rows were wrong. `run/claude-prerelease-prompt-telos-2026-09-06` was
published as 2 new files and holds 12: ten frozen `RND_TELOS_*` and
`RND_NARROW_TELOS_BENCHMARK_*` documents existed only there and the number said otherwise.
`research/architecture-clean-ab-2026-09-06` was published as 4 and holds 14.

The instrument passed green throughout, because nothing compared the published number to
the trees. That is the same substitution this repository is built to catch, occurring in
the file that names it: a measurement was replaced by a cheaper one that answers a
different question, and the gate could not tell.

Repaired at the instrument, not in prose. `--live` now recomputes every count and every
successor claim tree to tree, with positive controls including one that reproduces the
three-dot error and fails on it.

### PR 19 was retargeted at `main` and now can reach it

The 2026-09-08 read recorded that PR 19 had head `claude/product-value-completion-run-if7ito`
and base `run/product-value-completion-2026-09-06`: both ahead of `main`, so merging it
would have moved 31 files from one side branch to another and no pull request targeted
`main` from either. As of 2026-09-09 its base is `main`.

The finding is closed and the base branch is now `SUPERSEDED` by PR 19's own head, which
carries every path it has. It stays recorded because it is the structural form of the
drift this file exists for: work that looks reviewed while the review terminates outside
the canonical lane.

### Forked artifacts with no canonical copy

The same artifacts exist on several branches, at different contents, with no copy on
`main`. Nothing selects between the versions. Recounted 2026-09-09 across all eighteen
branches; every count below is higher than the 2026-09-08 reading, which sampled only the
branches then declared.

| Artifact | Branches | Distinct contents |
|---|---|---|
| `.github/workflows/best-effort-lichess-copilot.yml` | 3 | 3 |
| `skills/evidence-bounded-best-effort-runtime/skill.md` | 3 | 2 |
| `runtime/calibration_loop/copilot_resource_adapter.py` | 3 | 1 |
| `runtime/calibration_loop/copilot-config.best-effort.json` | 3 | 1 |
| `runtime/calibration_loop/copilot_resource_adapter_v02.py` | 6 | 1 |
| `runtime/calibration_loop/copilot-config-v02.best-effort.json` | 6 | 1 |

The `_v02` rows are a second generation of the same adapter, carried identically by six
branches: `run/delta-v02-batch-2026-09-08`, `research/rnd-self-triangulation-2026-09-08`
and the four `challenges`/`adjudication` branches. Neither generation is on `main`, so a
change to the adapter has nine side-branch copies to chase and no canonical one to change.

`research/rnd-self-triangulation-2026-09-08` was pushed on 2026-09-08 at 14:26, after this
inventory was first written. `scripts/check_branch_inventory.py --live` failed on it within
the hour, which is the first observation the instrument produced that review had not already
made.

`skills/` does not appear in the placement table in `docs/REPOSITORY_MAP.md`. A directory
that exists on three branches and in no rule is a placement question, not a file question.

The single most-copied path is `docs/BRANCH_AUDIT_2026-09-05.md`, on fifteen branches at
one blob. It is the one case where `main` does hold the content, under the canonical path
recorded in **Relocations** above.

## Branch-by-branch read, 2026-09-08, re-measured 2026-09-09

Every branch was read. The new-file count is the number that matters, because a branch can
sit many commits ahead and still hold almost nothing: `feat/resource-delta-accounting-v0-2`
is six commits ahead and holds one path, the relocated audit document, since `main` took
its work as the squash `74fc4af`. A commit count is not evidence of content.

The converse also holds, and is what the three-dot error hid:
`run/claude-prerelease-prompt-telos-2026-09-06` is two commits ahead and holds twelve paths
that exist nowhere on `main`.

### Six branches hold nothing their successor does not

Each row's successor carries every path the branch has, allowing the one relocation above.
`--live` verifies this tree to tree on every run, so a predecessor that receives a commit
and stops being contained fails the gate instead of aging quietly inside a claim.

That is not a hypothetical. `research/rnd-self-triangulation-2026-09-08` was declared
`SUPERSEDED` by the challenges branch on 2026-09-08 and received the five-path
mechanism-transfer set on 2026-09-09. It is `STRANDED` now, and it took a hand comparison to
notice, which is why the check exists.

Eighteen open questions become twelve.

### The rubric and the result it grades are on different branches, twice

`research/rnd-self-triangulation-adjudication-2026-09-08` carries
`RND_SELF_TRIANGULATION_CHALLENGE_RUBRIC_1.md`, frozen to adjudicate the blind challenges.
`research/rnd-self-triangulation-challenges-2026-09-08` carries the challenges `C1` to `C4`
and `RND_SELF_TRIANGULATION_CHALLENGE_RESULT_1.md`. Neither contains the other.

On 2026-09-09 the same split reappeared one generation later.
`research/rnd-self-triangulation-anti-adjudication-2026-09-08` carries
`anti-adjudication/ANTI_CHALLENGE_RUBRIC_V0.md` and `ANTI_CHALLENGE_RESULT_1.md`;
`research/rnd-self-triangulation-anti-challenges-2026-09-08` carries the anti-challenges
`A1` to `A4` and their workflow. Neither contains the other either. Each `anti-*` branch
does contain its own predecessor, which is why the two older branches are now `SUPERSEDED`
and the split moved rather than closed.

From either branch of a pair alone, the blind result cannot be graded against its own
frozen rubric. This is a live research program, not archaeology, and the split is `OWNER`'s
to resolve. The instrument records that it recurred; it does not resolve it.

### The skill has two versions and the newer one is on the smaller branch

`skills/evidence-bounded-best-effort-runtime/skill.md` is 205 lines on
`skill/evidence-bounded-best-effort-runtime` and 140 lines on the two `run/` branches. The
205-line version is the later one: it was committed as "tighten best-effort skill after
self-calibration". A merge that took the run branches' copy would silently revert that
refinement.

`skills/` still matches no row in the placement table in `docs/REPOSITORY_MAP.md`.

### PR 19 has been retargeted

The 2026-09-08 read recommended retargeting PR 19 at `main`, on the grounds that its base
`run/product-value-completion-2026-09-06` holds nothing PR 19's own head does not. That was
done. PR 19's 31 files can now reach `main`, and the base branch is `SUPERSEDED` by the
head.

### What is decided and what is not

Decided here: which branches hold nothing, and what each remaining branch actually contains.

Not decided here: whether the twelve remaining branches should be recovered into `main` or
copied under `archive/`. Each holds real content, several are being written to now, and two
belong to parallel sessions' open pull requests. That is an `OWNER` decision per branch,
and taking it inside a repository-organization pass would be the same encodability bias the
kernel forbids.

## What this inventory does not claim

It does not say the stranded work is good, bad, finished or admissible. It does not
promote anything. It records where bytes live relative to `main`, and which of those
locations violate the rule the repository already wrote down.

Recovery, archival or abandonment of any branch above is an `OWNER` decision and is not
taken here.
