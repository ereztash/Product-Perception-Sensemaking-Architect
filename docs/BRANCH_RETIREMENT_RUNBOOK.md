# Branch Retirement Runbook

Status: `CANONICAL`
Authority: `OWNER`, executable only outside an agent session

Twenty-one branches are strict ancestors of `main`. Deleting them loses no history. They
have been dispositioned for deletion since 2026-09-05 and are still present, because the
write is refused in every agent session, not because the decision is open.

## Why an agent cannot do this

Re-tested 2026-09-08 against `main` @ `74fc4af5`:

| Route | Result |
|---|---|
| `git push origin --delete <ref>` | `HTTP 403` on the send-pack; ordinary pushes over the same transport succeed; the ref survives |
| GitHub MCP server | exposes `create_branch`, `list_branches`, `delete_file`; no delete-ref tool exists |
| `DELETE /git/refs/heads/*` | refused before it reaches GitHub |

None of the branches is protected and the account holds admin rights, so this is neither a
repository permission nor a token scope. The session's egress proxy allows a fixed set of
GitHub write paths and ref deletion is not among them; the git transport passes through the
same proxy, which is why both routes fail identically.

The same symptom was recorded on 2026-09-05 and again on 2026-09-06. Three sessions have now
reproduced it. It is an `ENVIRONMENT` blocker with a stable cause, not an intermittent one.

## Verify before deleting

Never run the deletion from a stale list. Re-derive it:

```bash
git fetch origin --prune
python scripts/check_branch_inventory.py --live
```

That run fails if any branch declared `RETIRABLE` has moved since capture, if a branch on
the remote is undeclared, or if a branch declared retirable is in fact ahead of `main`. A
green run means every ref in the command below is still contained in `main`.

## The command

Run from a clone that is not behind an agent proxy:

```bash
git push origin --delete \
  archive/legacy-docs-2026-09-05 \
  archive/legacy-snapshots \
  claude/lichess-prerelease-gaps-qvlbv5 \
  neta/design-research-spine-v0.1 \
  neta/github-benchmark-v1 \
  neta/hebrew-observatory \
  neta/hebrew-signal-fidelity \
  neta/oss-observatory \
  neta/v0.1-agent-contract \
  refoundation/neta-assurance-v0.2 \
  repo/organization-canonical \
  repo/organization-canonical-v2 \
  repo/organization-final \
  repo/organization-pass \
  repo/organization-pass-2 \
  repo/organization-single-source \
  repo/organization-work \
  research/system-design-decision-lane-2026-09-06 \
  research/wave1-evidence-pass1 \
  research/wave1-triangulation \
  rnd/calibration-loop-v0.1
```

The GitHub Branches page deletes the same refs one at a time and works equally well.

## After deleting

```bash
git fetch origin --prune
python scripts/check_branch_inventory.py --live
```

This will fail, correctly: `docs/BRANCH_INVENTORY.md` still declares branches the remote no
longer has. Remove the deleted rows from the retirable table, update `Captured:` and
`Captured against:`, and re-run until green. The failure is the instrument working; the
inventory is a declaration, and a declaration that outlives its object is exactly what this
checker exists to catch.

## What this runbook does not cover

The twelve branches ahead of `main`. None of them may be deleted by this command; every one
carries commits that exist nowhere else. Their dispositions are in
`docs/BRANCH_INVENTORY.md` and their recovery is a separate `OWNER` decision.
