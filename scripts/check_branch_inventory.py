#!/usr/bin/env python3
"""Branch-level enforcement of the canonical rule.

`archive/reconciliation/RECONCILIATION_REPORT_2026-09-06.md` section 8 recorded that the
existing validators are file-level and offline, so they cannot detect that a commit exists
only on an unmerged branch, and that the branch-level half of the rule was therefore left
to review. Review drifted: two branches were declared active while twelve were ahead of
`main`, carrying sixty-nine files that existed nowhere else.

This checker closes that half. `docs/BRANCH_INVENTORY.md` is the declaration; the live
repository is the observation; a disagreement between them is a failure.

Stdlib only. Every invariant ships with a positive control so a run proves the checker can
fail, not merely that it passed.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

INVENTORY = "docs/BRANCH_INVENTORY.md"
CANONICAL_STATE = "docs/CANONICAL_STATE.md"
RUNBOOK = "docs/BRANCH_RETIREMENT_RUNBOOK.md"

# A branch gets one day before it must be declared. The invariant is that nothing
# decision-relevant lives only on a side branch, not that a branch is declared before
# its first push. Requiring declaration up front reddens every other pull request the
# moment a run branch is created, which is how a checker gets switched off.
GRACE_SECONDS = 24 * 60 * 60

CANONICAL_BRANCH = "main"

# Closed vocabulary. A branch carries exactly one of these.
DISPOSITIONS = {
    "RETIRABLE",
    "SUPERSEDED",
    "OPEN_PR_TO_MAIN",
    "OPEN_PR_TO_BRANCH",
    "STRANDED",
}

# Dispositions that assert the branch is ahead of `main`.
AHEAD_DISPOSITIONS = DISPOSITIONS - {"RETIRABLE"}

# `SUPERSEDED` is only meaningful with a named successor, so the row must name one.
SUCCESSOR_CELL = re.compile(r"superseded by `([^`]+)`", re.IGNORECASE)

BRANCH_CELL = re.compile(r"^\|\s*`([^`]+)`\s*\|(.*)\|\s*$")
# `| `old/path` | `canonical/path` |` under the Relocations heading. A path that `main`
# carries under a different name is not a path the branch holds alone, but the exemption
# has to be declared and checked, not assumed by the reader.
RELOCATION_CELL = re.compile(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*$")
TIP_SHA = re.compile(r"`([0-9a-f]{10,40})`")
CAPTURED_AGAINST = re.compile(
    r"Captured against:\s*`" + CANONICAL_BRANCH + r"`\s*@\s*`([0-9a-f]{40})`"
)
# Only fenced blocks. A prose mention such as `git push origin --delete <ref>` in a table
# is documentation, not a command anyone pastes.
RUNBOOK_DELETE = re.compile(r"```[^\n]*\n(git push origin --delete.*?)\n```", re.DOTALL)


class ContractError(Exception):
    """An invariant did not hold."""


def fail(message: str) -> None:
    raise ContractError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def read(rel: str) -> str:
    path = ROOT / rel
    require(path.is_file(), f"missing required document: {rel}")
    return path.read_text(encoding="utf-8")


# --- declaration parsing ------------------------------------------------------

def parse_inventory(text: str | None = None) -> dict[str, dict[str, str]]:
    """Return {branch: {"disposition": ..., "tip": ...}} as declared."""
    text = read(INVENTORY) if text is None else text
    declared: dict[str, dict[str, str]] = {}
    section = None

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            section = stripped[3:].strip()
            continue
        if stripped.startswith("### "):
            continue

        match = BRANCH_CELL.match(stripped)
        if not match:
            continue
        branch, rest = match.group(1), match.group(2)

        # Vocabulary and forked-artifact tables also start with a backticked cell.
        if branch in DISPOSITIONS:
            continue
        if section and not section.startswith(("Retirable", "Ahead of")):
            continue

        found = [d for d in DISPOSITIONS if d in rest]
        if section and section.startswith("Retirable"):
            found = ["RETIRABLE"]
        if not found:
            continue
        require(
            len(found) == 1,
            f"{INVENTORY}: `{branch}` carries {len(found)} dispositions; exactly one is allowed",
        )
        require(
            branch not in declared,
            f"{INVENTORY}: `{branch}` is declared more than once",
        )

        tip = TIP_SHA.search(rest)
        require(
            tip is not None,
            f"{INVENTORY}: `{branch}` is declared without a tip SHA",
        )

        # `| tip | ahead | new files | disposition |`. The new-file count is the number
        # the whole file exists to publish, so it is parsed and later checked against the
        # trees rather than read as prose.
        new_files: int | None = None
        if section and section.startswith("Ahead of"):
            cells = [cell.strip() for cell in rest.split("|")]
            require(
                len(cells) >= 4,
                f"{INVENTORY}: `{branch}` has {len(cells)} cells after the branch name; "
                "the ahead table is | tip | ahead | new files | disposition |",
            )
            require(
                cells[2].isdigit(),
                f"{INVENTORY}: `{branch}` declares new files as {cells[2]!r}, not a count",
            )
            new_files = int(cells[2])

        successor = SUCCESSOR_CELL.search(rest)
        declared[branch] = {
            "disposition": found[0],
            "tip": tip.group(1),
            "new_files": new_files,
            "successor": successor.group(1) if successor else None,
        }

    require(declared != {}, f"{INVENTORY}: no branch rows parsed; the declaration is empty")
    return declared


def parse_captured_against(text: str | None = None) -> str:
    text = read(INVENTORY) if text is None else text
    match = CAPTURED_AGAINST.search(text)
    require(
        match is not None,
        f"{INVENTORY}: no `Captured against: \\`{CANONICAL_BRANCH}\\` @ <40-hex>` line",
    )
    return match.group(1)


def parse_relocations(text: str | None = None) -> dict[str, str]:
    """Return {path on side branches: canonical path on `main`}.

    A file `main` kept under a new name still exists on `main`. Without a declared
    exemption every branch that predates the move looks like it holds a unique path,
    and a `SUPERSEDED` row that is true would fail. The exemption is declared here and
    verified against `main`, so it cannot quietly become a hole.
    """
    text = read(INVENTORY) if text is None else text
    relocations: dict[str, str] = {}
    inside = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            inside = stripped.lower().endswith("relocations")
            continue
        if not inside:
            continue
        match = RELOCATION_CELL.match(stripped)
        if not match:
            continue
        old, new = match.group(1), match.group(2)
        if old == "Path on side branches":
            continue
        require(
            old not in relocations,
            f"{INVENTORY}: `{old}` is declared relocated more than once",
        )
        require(
            old != new,
            f"{INVENTORY}: `{old}` is declared relocated to itself",
        )
        relocations[old] = new
    return relocations


def parse_active_branches(text: str | None = None) -> set[str]:
    """Branches named in the CANONICAL_STATE 'Active branches' table."""
    text = read(CANONICAL_STATE) if text is None else text
    active: set[str] = set()
    inside = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            inside = stripped.lower().endswith("active branches")
            continue
        if not inside:
            continue
        match = BRANCH_CELL.match(stripped)
        if match:
            active.add(match.group(1))
    return active


# --- offline invariants -------------------------------------------------------

def check_superseded_have_successors(text: str | None = None) -> None:
    """A SUPERSEDED row must name the successor that contains it.

    Without a named successor the disposition is an opinion. With one it is a claim
    anyone can check with `git merge-base --is-ancestor`.
    """
    text = read(INVENTORY) if text is None else text
    for line in text.splitlines():
        stripped = line.strip()
        match = BRANCH_CELL.match(stripped)
        if not match or "SUPERSEDED" not in match.group(2):
            continue
        branch = match.group(1)
        successor = SUCCESSOR_CELL.search(match.group(2))
        require(
            successor is not None,
            f"{INVENTORY}: `{branch}` is SUPERSEDED without naming a successor; "
            "write \"superseded by `<branch>`\"",
        )
        require(
            successor.group(1) != branch,
            f"{INVENTORY}: `{branch}` names itself as its own successor",
        )


def check_declaration_shape(declared: dict[str, dict[str, str]] | None = None) -> None:
    """Every declared branch carries one known disposition and a tip."""
    declared = parse_inventory() if declared is None else declared
    for branch, row in declared.items():
        require(
            row["disposition"] in DISPOSITIONS,
            f"{INVENTORY}: `{branch}` has unknown disposition {row['disposition']!r}",
        )
        require(
            re.fullmatch(r"[0-9a-f]{10,40}", row["tip"]) is not None,
            f"{INVENTORY}: `{branch}` has a malformed tip {row['tip']!r}",
        )
    require(
        CANONICAL_BRANCH not in declared,
        f"{INVENTORY}: `{CANONICAL_BRANCH}` must not be dispositioned; it is the canonical branch",
    )


def check_active_table_agrees(
    declared: dict[str, dict[str, str]] | None = None,
    active: set[str] | None = None,
) -> None:
    """CANONICAL_STATE may not name an active branch the inventory calls retirable or unknown."""
    declared = parse_inventory() if declared is None else declared
    active = parse_active_branches() if active is None else active
    for branch in sorted(active):
        require(
            branch in declared,
            f"{CANONICAL_STATE} lists `{branch}` as active; {INVENTORY} does not declare it",
        )
        require(
            declared[branch]["disposition"] in AHEAD_DISPOSITIONS,
            f"{CANONICAL_STATE} lists `{branch}` as active; {INVENTORY} calls it "
            f"{declared[branch]['disposition']}",
        )

    ahead = {b for b, r in declared.items() if r["disposition"] in AHEAD_DISPOSITIONS}
    missing = sorted(ahead - active)
    require(
        not missing,
        f"{INVENTORY} declares branches ahead of `{CANONICAL_BRANCH}` that "
        f"{CANONICAL_STATE} does not list as active: " + ", ".join(missing),
    )


def parse_runbook_commands(text: str | None = None) -> list[frozenset[str]]:
    """Ref sets named by each pasteable deletion command in the runbook."""
    text = read(RUNBOOK) if text is None else text
    commands = []
    for block in RUNBOOK_DELETE.findall(text):
        refs = block.replace("git push origin --delete", " ").replace("\\", " ").split()
        commands.append(frozenset(refs))
    return commands


def check_runbook_matches_inventory(
    declared: dict[str, dict[str, str]] | None = None,
    commands: list[frozenset[str]] | None = None,
) -> None:
    """Every deletion command must name exactly the refs declared RETIRABLE.

    The runbook carries the same list twice, once as a POSIX block and once as a single
    line for shells without backslash continuation. Two copies drift, and a drifted copy
    deletes a set nobody verified.

    While nothing is retirable the runbook must carry no deletion command at all. A command
    left behind after a retirement names refs that no longer exist, and a ref name is
    reusable: a later branch created under one of those names would be deleted by a stale
    paste.
    """
    declared = parse_inventory() if declared is None else declared
    commands = parse_runbook_commands() if commands is None else commands
    retirable = frozenset(b for b, r in declared.items() if r["disposition"] == "RETIRABLE")

    if not retirable:
        require(
            not commands,
            f"{RUNBOOK} carries {len(commands)} deletion command(s) while {INVENTORY} "
            f"declares nothing RETIRABLE; a stale command deletes refs nobody verified",
        )
        return

    require(
        len(commands) >= 2,
        f"{RUNBOOK}: expected a POSIX and a single-line deletion command, found "
        f"{len(commands)}",
    )
    for i, refs in enumerate(commands):
        extra = sorted(refs - retirable)
        require(
            not extra,
            f"{RUNBOOK}: deletion command {i + 1} names refs not declared RETIRABLE in "
            f"{INVENTORY}: " + ", ".join(extra),
        )
        missing = sorted(retirable - refs)
        require(
            not missing,
            f"{RUNBOOK}: deletion command {i + 1} omits refs declared RETIRABLE in "
            f"{INVENTORY}: " + ", ".join(missing),
        )


# --- live invariants ----------------------------------------------------------

def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, text=True, check=False
    )


def remote_heads(remote: str = "origin") -> dict[str, str]:
    proc = git("ls-remote", "--heads", remote)
    require(
        proc.returncode == 0,
        f"cannot reach remote {remote!r}: {proc.stderr.strip() or 'unknown error'}",
    )
    heads: dict[str, str] = {}
    for line in proc.stdout.splitlines():
        parts = line.split()
        if len(parts) == 2 and parts[1].startswith("refs/heads/"):
            heads[parts[1][len("refs/heads/") :]] = parts[0]
    require(heads != {}, f"remote {remote!r} reported no branches")
    return heads


def ensure_object(sha: str, branch: str, remote: str = "origin") -> bool:
    if git("cat-file", "-e", f"{sha}^{{commit}}").returncode == 0:
        return True
    git("fetch", "--quiet", remote, branch)
    return git("cat-file", "-e", f"{sha}^{{commit}}").returncode == 0


_TREE_CACHE: dict[str, frozenset[str]] = {}


def tree_paths(ref: str) -> frozenset[str]:
    """Every path in the tree at `ref`, read tree to tree.

    Not `git diff main...ref`. Three-dot compares against the merge base, so it reports
    nothing for work `main` absorbed as a squash and nothing for paths the branch has
    carried since before the fork point. The count this file publishes is "paths that
    exist on the branch and nowhere on `main`", and only a tree-to-tree read answers it.
    """
    if ref in _TREE_CACHE:
        return _TREE_CACHE[ref]
    proc = git("ls-tree", "-r", "--name-only", ref)
    require(
        proc.returncode == 0,
        f"cannot read the tree at {ref}: {proc.stderr.strip() or 'unknown object'}; "
        "deepen the clone (actions/checkout with fetch-depth: 0), or re-declare the row "
        "at a tip that still exists",
    )
    paths = frozenset(line for line in proc.stdout.splitlines() if line)
    require(paths != frozenset(), f"the tree at {ref} is empty")
    _TREE_CACHE[ref] = paths
    return paths


def check_relocations_resolve(
    relocations: dict[str, str] | None = None,
    resolve=tree_paths,
    anchor: str = CANONICAL_BRANCH,
) -> None:
    """Each declared relocation must be a fact about `main`, not a convenience."""
    relocations = parse_relocations() if relocations is None else relocations
    if not relocations:
        return
    main_paths = resolve(anchor)
    for old, new in sorted(relocations.items()):
        require(
            new in main_paths,
            f"{INVENTORY}: `{old}` is declared relocated to `{new}`, which is not on "
            f"`{CANONICAL_BRANCH}`; the exemption would excuse a path that exists nowhere",
        )
        require(
            old not in main_paths,
            f"{INVENTORY}: `{old}` is declared relocated but still exists on "
            f"`{CANONICAL_BRANCH}`; it never moved",
        )


def check_new_file_counts(
    declared: dict[str, dict[str, str]] | None = None,
    resolve=tree_paths,
    anchor: str = CANONICAL_BRANCH,
) -> None:
    """The published count must equal the tree-to-tree count at the declared tip.

    Both sides are pinned commits: the branch at the tip the row names, `main` at the
    anchor the file names. The assertion therefore stays true as branches move, and a
    row that was measured with the wrong command fails instead of reading as evidence.
    """
    declared = parse_inventory() if declared is None else declared
    main_paths = resolve(anchor)
    for branch, row in sorted(declared.items()):
        if row["disposition"] == "RETIRABLE":
            continue
        expected = row.get("new_files")
        if expected is None:
            continue
        actual = len(resolve(row["tip"]) - main_paths)
        require(
            actual == expected,
            f"{INVENTORY}: `{branch}` @ {row['tip']} declares {expected} new file(s) "
            f"against `{CANONICAL_BRANCH}` @ {anchor[:10]}, tree to tree it holds "
            f"{actual}",
        )


def check_superseded_containment(
    declared: dict[str, dict[str, str]] | None = None,
    relocations: dict[str, str] | None = None,
    resolve=tree_paths,
    anchor: str = CANONICAL_BRANCH,
) -> None:
    """A named successor must actually carry every path the branch holds.

    `SUPERSEDED` is what licenses deletion once the successor lands. Left unchecked it
    is an opinion that ages: a predecessor can receive a commit after the claim is
    written and quietly stop being contained.
    """
    declared = parse_inventory() if declared is None else declared
    relocations = parse_relocations() if relocations is None else relocations
    for branch, row in sorted(declared.items()):
        if row["disposition"] != "SUPERSEDED":
            continue
        successor = row.get("successor")
        if successor is None:
            continue  # check_superseded_have_successors owns this failure
        if successor == CANONICAL_BRANCH:
            successor_paths = resolve(anchor)
        else:
            require(
                successor in declared,
                f"{INVENTORY}: `{branch}` names `{successor}` as its successor, and "
                f"`{successor}` is not declared; the claim cannot be checked",
            )
            successor_paths = resolve(declared[successor]["tip"])
        missing = sorted((resolve(row["tip"]) - successor_paths) - set(relocations))
        require(
            not missing,
            f"{INVENTORY}: `{branch}` is declared SUPERSEDED by `{successor}`, which "
            f"does not carry {len(missing)} of its path(s): {', '.join(missing[:4])}"
            + (" ..." if len(missing) > 4 else "")
            + "; it is STRANDED, or the missing paths are a declared relocation",
        )


def check_live(
    declared: dict[str, dict[str, str]] | None = None,
    heads: dict[str, str] | None = None,
    remote: str = "origin",
) -> dict[str, str]:
    """The declaration must match the branches that actually exist."""
    declared = parse_inventory() if declared is None else declared
    heads = remote_heads(remote) if heads is None else heads

    require(
        CANONICAL_BRANCH in heads,
        f"remote has no `{CANONICAL_BRANCH}`; the canonical rule has no anchor",
    )
    main_sha = heads[CANONICAL_BRANCH]

    live = {name: sha for name, sha in heads.items() if name != CANONICAL_BRANCH}

    undeclared = sorted(set(live) - set(declared))
    overdue, in_grace = [], []
    for branch in undeclared:
        sha = live[branch]
        if not ensure_object(sha, branch, remote):
            overdue.append(f"{branch} (unresolvable at {sha[:10]})")
            continue
        proc = git("log", "-1", "--format=%ct", sha)
        age = None
        if proc.returncode == 0 and proc.stdout.strip().isdigit():
            age = time.time() - int(proc.stdout.strip())
        if age is not None and age < GRACE_SECONDS:
            in_grace.append(f"{branch} ({int(age // 3600)}h)")
        else:
            overdue.append(branch)
    require(
        not overdue,
        f"branches older than {GRACE_SECONDS // 3600}h exist on {remote} but are not "
        f"declared in {INVENTORY}: " + ", ".join(overdue),
    )

    # `OPEN_PR_TO_MAIN` is the one disposition whose expected end state is "merged".
    # A branch in that state that becomes contained, or disappears, has succeeded; a
    # checker that reddened `main` on every successful merge would be switched off
    # within a week. Every other disposition still fails on both.
    vanished = sorted(set(declared) - set(live))
    unexpected = [b for b in vanished if declared[b]["disposition"] != "OPEN_PR_TO_MAIN"]
    require(
        not unexpected,
        f"{INVENTORY} declares branches that no longer exist on {remote}: "
        + ", ".join(unexpected),
    )
    merged_and_gone = [b for b in vanished if b not in unexpected]

    verdicts: dict[str, str] = {}
    moved: list[str] = []
    # Undeclared branches inside the grace period have no row to check against yet.
    for branch in sorted(set(live) & set(declared)):
        sha = live[branch]
        row = declared[branch]
        # A retirable tip is pinned: the runbook is about to delete this ref, and a ref
        # that moved since capture may no longer be contained in `main`. An ahead branch
        # is expected to receive commits, so its recorded tip is a last-observed value,
        # not a pin.
        if row["disposition"] == "RETIRABLE":
            require(
                sha.startswith(row["tip"]),
                f"`{branch}` is declared RETIRABLE at tip {row['tip']} but the remote has "
                f"{sha[:10]}; re-verify containment before any deletion",
            )
        require(
            ensure_object(sha, branch, remote),
            f"cannot resolve `{branch}` at {sha[:10]}; deepen the clone "
            "(actions/checkout with fetch-depth: 0) before running --live",
        )
        if row["disposition"] != "RETIRABLE" and not sha.startswith(row["tip"]):
            moved.append(f"{branch} {row['tip']}->{sha[:10]}")
        contained = git("merge-base", "--is-ancestor", sha, main_sha).returncode == 0
        if contained:
            if row["disposition"] == "OPEN_PR_TO_MAIN":
                verdicts[branch] = "MERGED"
                continue
            require(
                row["disposition"] == "RETIRABLE",
                f"`{branch}` is contained in `{CANONICAL_BRANCH}` but declared "
                f"{row['disposition']}; it is retirable",
            )
            verdicts[branch] = "RETIRABLE"
        else:
            require(
                row["disposition"] in AHEAD_DISPOSITIONS,
                f"`{branch}` is ahead of `{CANONICAL_BRANCH}` but declared RETIRABLE; "
                "deleting it would lose commits",
            )
            verdicts[branch] = row["disposition"]

    if moved:
        print("MOVED SINCE CAPTURE (ahead branches, informational): " + ", ".join(moved))
    if in_grace:
        print(
            f"UNDECLARED, WITHIN THE {GRACE_SECONDS // 3600}h GRACE: "
            + ", ".join(in_grace)
        )
    settled = sorted(merged_and_gone) + sorted(b for b, v in verdicts.items() if v == "MERGED")
    if settled:
        print(
            "MERGED, REMOVE FROM THE INVENTORY: " + ", ".join(settled)
        )
    return verdicts


# --- positive controls --------------------------------------------------------

_GOOD_INVENTORY = """# Branch Inventory

Captured against: `main` @ `""" + "0" * 40 + """`

## Retirable — contained in `main`

| Branch | Tip | Origin |
|---|---|---|
| `dead/one` | `aaaaaaaaaa` | merged |

## Ahead of `main`

| Branch | Tip | Ahead | New files | Disposition |
|---|---|---|---|---|
| `live/one` | `bbbbbbbbbb` | 2 | 1 | `STRANDED` |
"""

_GOOD_STATE = """### Active branches

| Branch | Purpose | State |
|---|---|---|
| `live/one` | an experiment | running |
"""


# Trees for the controls. `main` carries `kept.md` and the archived copy of a file the
# side branches still hold at its old path; `live/one` predates both and adds one path of
# its own; `live/two` is a partial successor that never took `unique.md`.
_FAKE_TREES: dict[str, frozenset[str]] = {
    "main": frozenset({"kept.md", "archive/moved.md"}),
    "bbbbbbbbbb": frozenset({"moved.md", "unique.md"}),
    "cccccccccc": frozenset({"moved.md", "kept.md"}),
}


def _fake_trees(ref: str) -> frozenset[str]:
    require(ref in _FAKE_TREES, f"control fixture has no tree for {ref}")
    return _FAKE_TREES[ref]


def positive_controls() -> int:
    """Prove each invariant can fail. A gate that cannot go red is not a gate."""
    heads = {
        "main": "1" * 40,
        "dead/one": "a" * 40,
        "live/one": "b" * 40,
    }

    controls: list[tuple[str, object]] = [
        (
            "two-dispositions-on-one-branch",
            lambda: parse_inventory(
                _GOOD_INVENTORY.replace("| 2 | 1 | `STRANDED` |", "| 2 | 1 | `STRANDED` `RETIRABLE` |")
            ),
        ),
        (
            "branch-declared-without-tip",
            lambda: parse_inventory(_GOOD_INVENTORY.replace("`bbbbbbbbbb`", "unknown")),
        ),
        (
            "empty-declaration",
            lambda: parse_inventory("# Branch Inventory\n\nNothing here.\n"),
        ),
        (
            "no-captured-against-anchor",
            lambda: parse_captured_against("# Branch Inventory\n\nCaptured: yesterday\n"),
        ),
        (
            "canonical-branch-dispositioned",
            lambda: check_declaration_shape(
                {"main": {"disposition": "STRANDED", "tip": "c" * 10}}
            ),
        ),
        (
            "superseded-without-a-named-successor",
            lambda: check_superseded_have_successors(
                "| `a/one` | `aaaaaaaaaa` | 2 | 1 | `SUPERSEDED` |\n"
            ),
        ),
        (
            "superseded-by-itself",
            lambda: check_superseded_have_successors(
                "| `a/one` | `aaaaaaaaaa` | 2 | 1 | `SUPERSEDED`, superseded by `a/one` |\n"
            ),
        ),
        (
            "active-branch-not-in-inventory",
            lambda: check_active_table_agrees(
                parse_inventory(_GOOD_INVENTORY), {"ghost/branch"}
            ),
        ),
        (
            "retirable-branch-listed-as-active",
            lambda: check_active_table_agrees(
                parse_inventory(_GOOD_INVENTORY), {"dead/one", "live/one"}
            ),
        ),
        (
            "ahead-branch-missing-from-active-table",
            lambda: check_active_table_agrees(parse_inventory(_GOOD_INVENTORY), set()),
        ),
        (
            "runbook-command-omits-a-retirable-ref",
            lambda: check_runbook_matches_inventory(
                parse_inventory(_GOOD_INVENTORY),
                [frozenset(), frozenset()],
            ),
        ),
        (
            "runbook-command-names-an-unretirable-ref",
            lambda: check_runbook_matches_inventory(
                parse_inventory(_GOOD_INVENTORY),
                [frozenset({"dead/one", "live/one"}), frozenset({"dead/one", "live/one"})],
            ),
        ),
        (
            "runbook-command-while-nothing-is-retirable",
            lambda: check_runbook_matches_inventory(
                {"live/one": {"disposition": "STRANDED", "tip": "b" * 10}},
                [frozenset({"dead/one"}), frozenset({"dead/one"})],
            ),
        ),
        (
            "runbook-carries-only-one-command",
            lambda: check_runbook_matches_inventory(
                parse_inventory(_GOOD_INVENTORY), [frozenset({"dead/one"})]
            ),
        ),
        (
            "undeclared-branch-past-the-grace-period",
            lambda: check_live(
                parse_inventory(_GOOD_INVENTORY),
                {**heads, "surprise/branch": "d" * 40},
            ),
        ),
        (
            "declared-branch-gone-from-remote",
            lambda: check_live(
                parse_inventory(_GOOD_INVENTORY),
                {"main": heads["main"], "dead/one": heads["dead/one"]},
            ),
        ),
        (
            "stranded-branch-silently-contained-in-main",
            lambda: check_live(
                {"live/one": {"disposition": "STRANDED", "tip": "b" * 10}},
                {"main": "b" * 40, "live/one": "b" * 40},
            ),
        ),
        (
            "retirable-tip-does-not-match-remote",
            lambda: check_live(
                parse_inventory(_GOOD_INVENTORY),
                {**heads, "dead/one": "e" * 40},
            ),
        ),
        (
            "remote-unreachable",
            lambda: remote_heads("no-such-remote-for-controls"),
        ),
        (
            "relocation-target-absent-from-main",
            lambda: check_relocations_resolve(
                {"old/path.md": "archive/path.md"}, _fake_trees, "main"
            ),
        ),
        (
            "relocation-of-a-path-main-still-has",
            lambda: check_relocations_resolve(
                {"kept.md": "archive/moved.md"}, _fake_trees, "main"
            ),
        ),
        (
            "declared-relocated-to-itself",
            lambda: parse_relocations(
                "## Relocations\n\n| `same.md` | `same.md` |\n"
            ),
        ),
        (
            "new-file-count-does-not-match-the-tree",
            lambda: check_new_file_counts(
                {"live/one": {"disposition": "STRANDED", "tip": "bbbbbbbbbb", "new_files": 9}},
                _fake_trees,
                "main",
            ),
        ),
        (
            "new-file-count-taken-with-a-three-dot-diff",
            # `live/one` forked before `main` gained `kept.md`, so three-dot reports one
            # added path and the tree holds two. The wrong command is the failure this
            # control exists for: eleven of sixteen rows carried three-dot numbers.
            lambda: check_new_file_counts(
                {"live/one": {"disposition": "STRANDED", "tip": "bbbbbbbbbb", "new_files": 1}},
                _fake_trees,
                "main",
            ),
        ),
        (
            "new-file-count-that-is-not-a-count",
            lambda: parse_inventory(
                _GOOD_INVENTORY.replace("| 2 | 1 | `STRANDED` |", "| 2 | some | `STRANDED` |")
            ),
        ),
        (
            "successor-does-not-carry-a-path-of-its-predecessor",
            lambda: check_superseded_containment(
                {
                    "live/one": {
                        "disposition": "SUPERSEDED",
                        "tip": "bbbbbbbbbb",
                        "successor": "live/two",
                    },
                    "live/two": {"disposition": "STRANDED", "tip": "cccccccccc"},
                },
                {},
                _fake_trees,
                "main",
            ),
        ),
        (
            "successor-that-is-not-declared",
            lambda: check_superseded_containment(
                {
                    "live/one": {
                        "disposition": "SUPERSEDED",
                        "tip": "bbbbbbbbbb",
                        "successor": "ghost/branch",
                    }
                },
                {},
                _fake_trees,
                "main",
            ),
        ),
        (
            "relocation-exemption-cannot-hide-a-real-path",
            # The exemption covers `moved.md` only. `unique.md` still fails, so a
            # relocation row cannot be widened into a blanket excuse.
            lambda: check_superseded_containment(
                {
                    "live/one": {
                        "disposition": "SUPERSEDED",
                        "tip": "bbbbbbbbbb",
                        "successor": "live/two",
                    },
                    "live/two": {"disposition": "STRANDED", "tip": "cccccccccc"},
                },
                {"moved.md": "archive/moved.md"},
                _fake_trees,
                "main",
            ),
        ),
    ]

    for name, fn in controls:
        try:
            fn()  # type: ignore[operator]
        except ContractError:
            print(f"CONTROL RED: {name}")
            continue
        fail(f"NOT-A-GATE: positive control stayed green: {name}")
    return len(controls)


# --- entry point --------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--live",
        action="store_true",
        help="compare the declaration against the actual remote; fail if unreachable",
    )
    parser.add_argument("--remote", default="origin")
    args = parser.parse_args()

    try:
        declared = parse_inventory()
        anchor = parse_captured_against()
        check_declaration_shape(declared)
        print(
            f"DECLARATION: {len(declared)} branches, anchored at "
            f"`{CANONICAL_BRANCH}` @ {anchor[:12]}"
        )

        check_superseded_have_successors()
        check_active_table_agrees(declared)
        ahead = sorted(b for b, r in declared.items() if r["disposition"] in AHEAD_DISPOSITIONS)
        print(
            f"ACTIVE TABLE: {CANONICAL_STATE} and {INVENTORY} agree on "
            f"{len(ahead)} branches ahead of `{CANONICAL_BRANCH}`"
        )

        commands = parse_runbook_commands()
        check_runbook_matches_inventory(declared, commands)
        retirable = sum(1 for r in declared.values() if r["disposition"] == "RETIRABLE")
        if retirable:
            print(
                f"RUNBOOK: {len(commands)} deletion commands, each naming the same "
                f"{retirable} retirable refs"
            )
        else:
            print("RUNBOOK: nothing retirable, and no deletion command left behind")

        relocations = parse_relocations()
        if args.live:
            verdicts = check_live(declared, remote=args.remote)
            retirable = sum(1 for v in verdicts.values() if v == "RETIRABLE")
            print(
                f"LIVE: {len(verdicts)} branches on {args.remote}, "
                f"{retirable} contained in `{CANONICAL_BRANCH}`, "
                f"{len(verdicts) - retirable} ahead, declaration matches"
            )

            check_relocations_resolve(relocations, anchor=anchor)
            check_new_file_counts(declared, anchor=anchor)
            check_superseded_containment(declared, relocations, anchor=anchor)
            counted = sum(
                1
                for r in declared.values()
                if r["disposition"] != "RETIRABLE" and r.get("new_files") is not None
            )
            superseded = sum(1 for r in declared.values() if r["disposition"] == "SUPERSEDED")
            print(
                f"TREES: {counted} new-file counts and {superseded} successor claims "
                f"verified tree to tree against `{CANONICAL_BRANCH}` @ {anchor[:10]}, "
                f"{len(relocations)} declared relocation(s)"
            )

            head = git("rev-parse", f"{args.remote}/{CANONICAL_BRANCH}")
            if head.returncode == 0 and not head.stdout.strip().startswith(anchor):
                drift = git("rev-list", "--count", f"{anchor}..{head.stdout.strip()}")
                if drift.returncode == 0:
                    print(
                        f"ANCHOR: `{CANONICAL_BRANCH}` is {drift.stdout.strip()} commit(s) "
                        f"past the anchor; the counts above describe "
                        f"`{CANONICAL_BRANCH}` @ {anchor[:10]}, not its head"
                    )
        else:
            print("LIVE: skipped (pass --live to compare against the remote)")

        count = positive_controls()
        print(f"positive controls: {count}/{count} correctly failed")
    except ContractError as exc:
        print(f"BRANCH-INVENTORY CONTRACT: FAIL\n  {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    print("BRANCH-INVENTORY CONTRACT: PASS")


if __name__ == "__main__":
    main()
