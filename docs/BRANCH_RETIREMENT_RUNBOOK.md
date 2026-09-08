# Branch Retirement Runbook

Status: `CANONICAL`
Authority: `OWNER`, executable only outside an agent session
Last executed: 2026-09-08, twenty-one refs retired

Nothing is currently retirable. This file is the procedure for the next time something is,
plus the record of the one execution that has happened.

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

Never delete from a stale list. Re-derive it:

```bash
git fetch origin --prune
python scripts/check_branch_inventory.py --live
```

That run fails if a branch declared `RETIRABLE` has moved since capture, if a branch on the
remote is undeclared, if a branch declared retirable is in fact ahead of `main`, or if the
runbook's deletion commands and the inventory's `RETIRABLE` set disagree. A green run means
every ref the runbook names is still contained in `main`.

## The command

While the retirable lane is empty there is no command here to run. When it is not, write the
list twice, as a POSIX block and as a single line, and let
`scripts/check_branch_inventory.py` hold both to the inventory's `RETIRABLE` set. It fails
when either drifts, and it fails on a live command while nothing is retirable.

### Windows

The backslash continuation used in POSIX shells is not honoured by `cmd.exe`, which uses `^`,
or by PowerShell, which uses a backtick. A pasted multi-line block therefore truncates at the
first line and deletes one ref instead of the list. Always paste the single-line form on
Windows; it is identical across `cmd.exe`, PowerShell and bash.

A Hebrew or spaced path can also fail to resolve under the default `cmd.exe` codepage. Open
the folder in Explorer, type `cmd` in the address bar and press Enter: the shell opens in
that directory and the path is never typed.

The GitHub Branches page deletes the same refs one at a time and works equally well.

## Execution record — 2026-09-08

Twenty-one refs deleted by the owner from a local clone, after
`check_branch_inventory.py --live` confirmed all twenty-one were strict ancestors of `main`
at `74fc4af5`. The remote went from thirty-five branches to fifteen: `main` plus fourteen
ahead of it.

Retired: `archive/legacy-docs-2026-09-05`, `archive/legacy-snapshots`,
`claude/lichess-prerelease-gaps-qvlbv5`, `neta/design-research-spine-v0.1`,
`neta/github-benchmark-v1`, `neta/hebrew-observatory`, `neta/hebrew-signal-fidelity`,
`neta/oss-observatory`, `neta/v0.1-agent-contract`, `refoundation/neta-assurance-v0.2`,
`repo/organization-canonical`, `repo/organization-canonical-v2`, `repo/organization-final`,
`repo/organization-pass`, `repo/organization-pass-2`, `repo/organization-single-source`,
`repo/organization-work`, `research/system-design-decision-lane-2026-09-06`,
`research/wave1-evidence-pass1`, `research/wave1-triangulation`,
`rnd/calibration-loop-v0.1`.

Their tips are recorded in `docs/BRANCH_INVENTORY.md` under "Retired on 2026-09-08", in
`archive/legacy-branches/BRANCH_AUDIT_2026-09-05.md` and in
`archive/reconciliation/RECONCILIATION_REPORT_2026-09-06.md`.

Nineteen of them had been dispositioned `MERGED_SAFE_TO_DELETE` on 2026-09-05 and survived
three days. The decision was never open; the write was refused in every session that could
have made it, and no session had written the owner action down as one pasteable command.

## After deleting

```bash
git fetch origin --prune
python scripts/check_branch_inventory.py --live
```

This fails, correctly: `docs/BRANCH_INVENTORY.md` still declares refs the remote no longer
has. Move the deleted rows out of the `RETIRABLE` table into a dated "Retired on" section,
update `Captured:`, and re-run until green. The failure is the instrument working; a
declaration that outlives its object is exactly what it exists to catch.

## What this runbook does not cover

The fourteen branches ahead of `main`. None of them may be deleted by this command; every one
carries commits that exist nowhere else. Their dispositions are in
`docs/BRANCH_INVENTORY.md` and their recovery is a separate `OWNER` decision.
