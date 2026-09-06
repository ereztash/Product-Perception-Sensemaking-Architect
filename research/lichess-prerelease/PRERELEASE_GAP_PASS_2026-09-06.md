# lichess_app pre-release gap pass, 2026-09-06

Status: `ONE_ENVIRONMENT_HANDOFF, ONE_FIELD_STOP`

Telos for this pass: move `ereztash/lichess_app` toward broad-public distribution by removing only
decision-relevant pre-release gaps.

Baseline: the latest calibrated Pre-release Gap Audit, not an older backlog.

## 1. Baseline recovered

The audit is the research contract at `ereztash/lichess_app docs/PRE_RELEASE_AUDIT.md`, implemented
by `scripts/pre-release-audit.mjs` and run by `.github/workflows/pre-release-audit.yml`. Both live on
the open pull request [ereztash/lichess_app#93](https://github.com/ereztash/lichess_app/pull/93),
`audit/pre-release-gap-scorecard`.

Latest run: [34029146340](https://github.com/ereztash/lichess_app/actions/runs/34029146340),
2026-09-06T11:10Z, target `broad-public`, candidate SHA `9f83d88` (the merge of head `ec73ecc` into
base `7c13887`).

Verdict: `NOT_READY_FOR_TARGET_DISTRIBUTION`, on exactly two blocking gaps.

| gap | criticality | layer | evidence | authority | blocking |
| --- | --- | --- | --- | --- | --- |
| `A-RELEASE-STALE-PR` | P1 | release-integrity | `verified-now` | ENVIRONMENT | yes |
| `F-HUMAN-CORE` | P1 | product-evidence | `field-required` | FIELD | yes |

Everything else in the report is P2 or below and does not block this target: `R-26`, `F-SCREEN-READER`,
`R-22`, `R-25`, `R-28`, `R-23`, `R-24`. Three rows are watch items with zero score effect (`R-08`,
`R-18`, `R-13`) and eighteen are historical or refuted and excluded from scoring. Watch is not
backlog and refuted is not debt, so none of them was worked.

## 2. `A-RELEASE-STALE-PR`, ENVIRONMENT

### What the live authority says

The audit reads the GitHub Rulesets API from inside the Action rather than trusting the tree. Two
gaps can come out of that read. Only one did.

`A-RELEASE-PROTECTION` fires unless `pull_request`, `non_fast_forward` and a required `verify` status
check are all present on an active ruleset. **It did not fire.** All three are enforced.

`A-RELEASE-STALE-PR` fires when `verify` is required but
`strict_required_status_checks_policy` is false. **It did fire**, `verified-now`, blocking.

So the live state is three of four controls in force, and one boolean unset.

### Recalibration, and it is the point of the external-authority rule

`ereztash/lichess_app docs/MASTER_PRODUCT_DEBT.md` R-21 is stated as *"`main` deploys before `verify`
has run"*, with the basis *"GitHub reports `main` `protected: false`"*, and
`docs/PRE_HUMAN_CEILING.md` repeats it as the highest of the four remaining items.

Live authority as of 2026-09-06T11:10Z contradicts that basis. A pull request is required, force-push
is blocked, and `verify` is a required check. The register is stale in the direction that matters:
it describes a bigger, differently-shaped problem than the one that is actually open.

The audit's own rule covers this exactly: *"Static repository text must not override a current
external authority."* The correction runs both ways. The register may not be used to re-open
controls the ruleset already enforces, and it may not be used to close the one it does not.

### What was executed, and what was not

Read: done, through the only authority-bearing path this session has. Direct calls to
`api.github.com` are refused by the session egress policy with HTTP 403, the connected GitHub tool
surface exposes no ruleset read or write, and an Actions `GITHUB_TOKEN` cannot carry
repository-administration write, so the Action cannot fix this either.

Write: **not authorised here.** Routed rather than attempted, per the proxy rule that a policy denial
is reported and not worked around.

The audit's closure condition has a second clause, *"or production deploy is otherwise bound to a
verified merge SHA"*. That was considered and declined. It is a larger repository change than the
one-field environment fix, it is not what the audit machine-checks, and building it would be work
whose completion could not change the current release decision.

### The smallest authorised fix, owner's hands

Settings, Rules, Rulesets, the active ruleset targeting `main`, the *Require status checks to pass*
rule: tick **Require branches to be up to date before merging**. Leave the pull-request,
non-fast-forward and `verify` rules exactly as they are.

Equivalently, `PUT /repos/ereztash/lichess_app/rulesets/{id}` with
`strict_required_status_checks_policy: true` on the `required_status_checks` rule, from a token that
holds repository administration.

One consequence worth stating before it is a surprise: strict checks mean a pull request behind
`main` must be updated and re-verified before it can merge. With one collaborator and
`concurrency` already on `verify`, that is a small cost, and it is the cost that buys the invariant.

### Verification, from live authority only

Dispatch **Pre-release Gap Audit** with target `broad-public` and confirm `A-RELEASE-STALE-PR` is
absent from the report. That path becomes available once
[#93](https://github.com/ereztash/lichess_app/pull/93) merges, because `workflow_dispatch` needs the
workflow on the default branch. Until then the audit only runs on pull requests that touch its own
three files.

A screenshot, a register edit or this document does not close the row.

Trace: `runtime/execution_traces/DEL-LICHESS-RELEASE-STALE-PR-001.json`.
Handoff: `runtime/handoffs/HANDOFF-LICHESS-ENV-001.json`.

## 3. `F-HUMAN-CORE`, FIELD

The instruction was to recover the frozen field and acquisition protocol first, prove it is
operationally runnable end to end, and make no code change if it is.

### The instrument, recovered

| artifact | what it fixes |
| --- | --- |
| `docs/ACQUISITION_PROTOCOL_V1.md`, frozen 2026-09-03 | the six things a trial can be invalidated by moving: route after the reveal, the `next_decision_started` definition, `ASK_AFTER_REVEALS = 2`, event denominators, prohibited inferences, question timing and placement |
| `docs/ACQUISITION_EVIDENCE.md` | every event, its denominator, its privacy class, and section 15's definition of acquisition-ready |
| `docs/VALUE_CLARITY_FIELD_PROTOCOL.md` | three arms, preregistered thresholds, a coding scheme frozen before data, and a recruitment package that states *"Ready to run. Nothing below requires another build."* |

A change to sections 1 to 6 requires `ACQUISITION_PROTOCOL_V2.md`, not an edit. That freeze was
respected: nothing in this pass touched them.

### Runnability, measured on `main@7c13887`

Everything below was run in this session against the current candidate.

| check | result |
| --- | --- |
| `npm ci`, `npm run build` | green |
| `tests/layout/the-loop-a-stranger-can-close.layout.test.ts` and `tests/layout/a-stranger-takes-their-first-decision.layout.test.ts`, real Chromium against `dist/public`, shipped Stockfish wasm not intercepted | 2 files, **9 of 9 tests pass**, 26.56 s |
| `npm run gates` | **35 of 35 pass**, including `GATE-CONTINUATION-IS-A-MOVE` and `GATE-REACHABILITY` |
| `GET https://lichessapp.vercel.app/` | 200 |
| `GET https://lichessapp.vercel.app/api/health` | 200, `ok: true`, `build.gitSha 7c13887…`, `protocolVersion 1.0.0` |
| served `assets/index-bhYxRjlo.js` against the local build | sha256 `52a5f724…`, **identical** |
| served `assets/index-Cx-EEMoX.css` against the local build | sha256 `2dda9f52…`, **identical** |
| `deployed.yml` run 152, scheduled, `main@7c13887`, 2026-09-06T11:00Z | success, with all three positive controls green, including the engine probe against the deployed origin |
| ledger handover surface | `client/src/components/SelfCheck.tsx` offers clipboard copy of `progressReport()` and a JSON download; `progressReport()` prints each visit's events verbatim with no derived funnel |

The two layout files walk the three frozen clauses as a stranger does them: front door to a recorded
reveal, reveal to another position in one press with only a placed move counted as continuation, and
the value question absent on reveal 1 and present on reveal 2. Because the served bundle is
byte-identical to the built one, that walk is the walk a recruited participant gets.

### What was attempted and could not run, stated rather than hidden

A live in-browser walk of `lichessapp.vercel.app` from this session. Chromium cannot reach the
network through this session's egress relay: tunnels close mid-exchange for every host, `example.com`
included. That is a limit on the observer, not a finding about the app, and the substitutes above are
narrower than the observation they stand in for.

### Disposition

Runnable. **No code change was made.** No repository blocker was found, so none was repaired.

Trace: `runtime/execution_traces/DEL-LICHESS-FIELD-INSTRUMENT-001.json`.
Handoff: `runtime/handoffs/HANDOFF-LICHESS-FIELD-001.json`.

## 4. Stop

The stop rule was: if the remaining broad-public blocker is FIELD-owned and the field instrument is
runnable, stop coding.

Both blockers are now outside the repository. One waits on a single environment toggle, the other on
people. Neither is a coding task, and P2 is not reconsidered until field evidence exists and a new
audit says no P1 remains.

Release state, unchanged and now correctly attributed:

```text
NOT_READY_FOR_BROAD_PUBLIC
  A-RELEASE-STALE-PR   ENVIRONMENT   one boolean, owner's hands, verified by re-running the audit
  F-HUMAN-CORE         FIELD         instrument runnable, waiting on participants
```

## 5. What would reverse this pass

- A Pre-release Gap Audit run reading `strict_required_status_checks_policy=true` closes the first
  row. A run still reading false after the owner reports making the change means the change did not
  land on the active ruleset.
- A recruited participant who cannot reach a first decision on either entry route reopens the second
  as a repository liveness defect rather than a field question. That is the field protocol's own stop
  condition, and it is the reversal test for the no-code-change decision recorded here.

---

# Pass 2, same day: the governance actions

Status: `TWO_DEPOSITS_CANONICAL, ENVIRONMENT_STILL_OWNER_ONLY`

Pass 1 ended with two handoffs and no landed action. Pass 2 executed the two actions that were
actually available, and established that the third is further out of reach than pass 1 recorded.

## 6. The R&D deposit is canonical

`ereztash/Product-Perception-Sensemaking-Architect` PR #15 was re-read on head `51c0c1a`: the
`contract` check green, no review threads, `mergeable_state: clean`, base unmoved at `51d8b2a`.
Marked ready for review and merged.

Landed: `main` = `75ebdf8457d988dc5fd378c2e63253d43d293a01`, carrying both traces, both handoffs, the
pass record, the CI step and the canonical-state section. A trace left on a work branch is not a
deposit, and this repository's own rule is that `main` is the only canonical source.

## 7. The audit is canonical in lichess_app

`ereztash/lichess_app` PR #93 was re-read on head `ec73ecc`: base `7c13887` equal to current `main`,
so already verified against it. `verify` green. `l6` skipped, which is the deployed workflow declining
a preview by design. No review threads; the single comment is the Vercel bot.

**The `audit` check on that PR was red, and it was merged anyway.** That check is the audit exiting
non-zero because verified `broad-public` blockers exist, which is the workflow doing its job on a
repository that has two open P1s. It is not a required status check, and treating it as a merge
blocker would make the audit unpromotable until the field trial it is waiting for has finished. That
is circular, and the workflow's own header says so.

Landed: `lichess_app main` = `07ccd11aaa9d41ed700f5096d4fc536e8394d869`. The workflow is registered as
id `351492931`, state active, and the merged file declares `workflow_dispatch` with a
`target` choice input.

### The merge moved the candidate, so the field evidence was re-verified rather than assumed

Production redeployed and now reports `build.gitSha 07ccd11`. The served
`assets/index-bhYxRjlo.js` and `assets/index-Cx-EEMoX.css` are **byte-identical** to the build that
the green protocol walk exercised on `7c13887`, and `deployed.yml` run
[154](https://github.com/ereztash/lichess_app/actions/runs/34035289334) passed on `07ccd11` with all
three positive controls green, engine probe included.

So the walk carries forward exactly, not by inference. A changed client byte would have required
re-running the walk instead.

## 8. `A-RELEASE-STALE-PR`: the block is bigger than pass 1 recorded

Pass 1 recorded a missing write permission. Pass 2 re-probed rather than assumed, and found a missing
read as well.

| probe | result |
| --- | --- |
| `GET /user` | 200, `ereztash` |
| `GET /repos/ereztash/lichess_app` | 403, session egress policy |
| `GET /repos/ereztash/lichess_app/branches/main/protection` | 403 |
| `GET /repos/ereztash/lichess_app/rulesets` | 403 |
| dispatch `pre-release-audit.yml` on `main` | 403, `Resource not accessible by integration` |
| connected GitHub tool surface | still exposes no ruleset operation |

The credential is fine and the block is on repository API paths. Promoting the audit removed the
workflow-availability obstacle and not the permission one: **capability present and capability
reachable are different states.**

**Consequence for the loop.** Verification is no longer a follow-up this system can perform after the
owner acts. It is part of the handoff. `HANDOFF-LICHESS-ENV-002.json` supersedes `001` for exactly
that reason, and `001` is retained rather than rewritten.

**And the current value of the flag is unknown here.** `strict=false` was true of the 11:10Z reading.
No newer read exists. Asserting it as current would be the documentation-over-authority error the
audit's own external-authority rule forbids.

## 9. Task 4 was not executed

The canonical audit could not be dispatched from this session. It was not worked around: the audit's
`pull_request` trigger fires on changes to its own three files, so a no-op commit touching one of them
would have produced a run. That is a code workaround for a missing permission, and it would also have
been pointless, because the flag it needs to read has not been changed yet.

## 10. State after pass 2

```text
PPSA main            75ebdf8   deposit canonical
lichess_app main     07ccd11   audit canonical, dispatchable by the owner
A-RELEASE-STALE-PR   ENVIRONMENT   open; owner acts AND owner verifies
F-HUMAN-CORE         FIELD          runnable on 07ccd11; run sheet issued
P2                                  not activated
```

Release disposition is still `NOT_READY_FOR_BROAD_PUBLIC`, and that is the correct answer rather than
a failure of the pass. Both remaining blockers now sit with the authority that owns them, which was
the purpose.

The FIELD handoff is operational at
[`FIELD_RUN_SHEET_TRIAL1.md`](FIELD_RUN_SHEET_TRIAL1.md). No frozen protocol section was modified.
