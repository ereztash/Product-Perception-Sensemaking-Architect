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
        declared[branch] = {"disposition": found[0], "tip": tip.group(1)}

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

        if args.live:
            verdicts = check_live(declared, remote=args.remote)
            retirable = sum(1 for v in verdicts.values() if v == "RETIRABLE")
            print(
                f"LIVE: {len(verdicts)} branches on {args.remote}, "
                f"{retirable} contained in `{CANONICAL_BRANCH}`, "
                f"{len(verdicts) - retirable} ahead, declaration matches"
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
