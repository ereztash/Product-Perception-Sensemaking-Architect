# Architecture Clean A/B — Execution Blocker

Status: `ENVIRONMENT_EXECUTION_BLOCKER · NOT_A_CANDIDATE_RESULT · PROTOCOL_UNCHANGED`
Date: 2026-09-06
Experiment: protocol-conforming clean Architecture A/B
Branch: `research/architecture-clean-ab-2026-09-06`
Pull request: [ereztash/Product-Perception-Sensemaking-Architect#14](https://github.com/ereztash/Product-Perception-Sensemaking-Architect/pull/14)

## What this document is

A record that the next discriminating Architecture experiment **did not execute**. It contains no benchmark evidence and changes no threshold.

The distinction this file exists to protect:

```text
the candidate failed             ≠  the benchmark ran and produced nothing
the benchmark produced nothing   ≠  the benchmark never started
```

Only the third is true.

## Failure stage

The frozen v0.2 selection rule requires probing an ordered list of explicit Copilot CLI model IDs before any benchmark case is loaded, and stopping if none is available.

Failure occurred **at that probe step**, in the first stage of the job.

| Stage | Reached | Result |
|---|---|---|
| Checkout, Python setup, Copilot CLI install | yes | success |
| Explicit model probe | yes | all five unavailable |
| Freeze `MODEL_SELECTION.json` | no | never written |
| Validate frozen inputs | no | not reached |
| Load benchmark CASES | no | not reached |
| Generate baseline and candidate outputs | no | not reached |
| Freeze manifest before GOLD | no | not reached |
| Reveal GOLD, blind adjudication | no | not reached |

No case was loaded. No GOLD was read. No output was generated, frozen or judged. The contamination barrier was never approached, let alone crossed.

## Attempted explicit models

GitHub Actions run [34027916604](https://github.com/ereztash/Product-Perception-Sensemaking-Architect/actions/runs/34027916604), head `e617caf`, job `architecture-clean-ab`:

```text
MODEL_UNAVAILABLE gpt-5.4
MODEL_UNAVAILABLE claude-sonnet-4.6
MODEL_UNAVAILABLE gpt-5-mini
MODEL_UNAVAILABLE claude-haiku-4.5
MODEL_UNAVAILABLE gemini-3.5-flash
No explicit Copilot model is available; auto is inadmissible for the frozen same-model protocol.
Process completed with exit code 1.
```

Each probe was a fresh non-interactive invocation with no repository tools requested and no benchmark case or GOLD content.

### Prior attempts in the same lane

| Run | Head | Attempt | Outcome |
|---|---|---|---|
| 34027324904 | `cf3d441` | Copilot CLI with `--model auto` | executed; retained as `DIAGNOSTIC_EXECUTION_SIGNAL` only, because `auto` does not establish one underlying runner model across A and B |
| 34027791744 | `9bb6397` | pinned `gpt-5.3-codex` runner, `claude-sonnet-4.6` judge | `Model "gpt-5.3-codex" ... is not available`, before the first case completed |
| 34027916604 | `e617caf` | ordered probe of five explicit model IDs | all unavailable; frozen rule stopped the run |

The underlying condition is the same across all three: the workflow's Copilot entitlement exposes no explicit model identifier, only `auto`.

## Why this is an execution failure, not a candidate failure

1. **The candidate was never invoked.** No Architecture Decision Discriminator output exists for this run.
2. **The corpus was never opened.** `HISTORICAL_CASES_V0.jsonl` was not read; `HISTORICAL_GOLD_V0.jsonl` was not read.
3. **The stop was the protocol working.** The v0.2 selection rule explicitly says that if zero explicit models are available, STOP, because `auto` leaves model identity uncontrolled. The job exiting non-zero is the rule being obeyed.
4. **The blocker is an entitlement fact, not a repository fact.** It belongs to `ENVIRONMENT` authority. No change to the corpus, prompts, thresholds or dimensions can resolve it.
5. **The repository contract CI passed on the same commit.** Run 34027916604 had two jobs: `contract` succeeded, `architecture-clean-ab` failed. The contract suite is green on every head where it ran.

Therefore:

```text
ARCHITECTURE_CANDIDATE_STATUS      = unchanged, CANDIDATE_CAPABILITY_NOT_AGENT
CLEAN_AB_RESULT                    = none
COUNTABLE_EVIDENCE_FROM_THIS_RUN   = zero
BLOCKER_AUTHORITY                  = ENVIRONMENT
```

## Resolution authority

`ENVIRONMENT`, with `OWNER` where entitlement or credential provisioning is required.

Neither `RESEARCH` nor `REPO` can resolve it. R&D cannot buy learning that removes it. Nothing about the Architecture hypothesis changes while it stands.

## Acceptable remediation classes

Any of these resolves the blocker without touching the frozen protocol:

1. **Provision an explicit-model channel.** Grant the workflow an entitlement that exposes at least one explicit Copilot model ID, or supply a credential for a provider whose model identifiers are explicit and pinnable.
2. **Extend the ordered probe list** with additional explicit model IDs, appended in a frozen amendment written **before** the next run, never after seeing a result.
3. **Run the benchmark outside GitHub Actions** in an environment where an explicit model can be pinned, provided the same isolation holds: no repository tools, no prior conversation context, no GOLD before the freeze manifest.
4. **Use a single pinned model for both runner and judge** if exactly one explicit model becomes available. The v0.2 rule already permits this and records the reduced judge independence.
5. **Record the blocker and wait.** A blocked experiment that stays blocked is an honest state.

## Forbidden remediation classes

None of these may be used to make the job pass:

1. **Falling back to `auto`.** Explicitly inadmissible under v0.2. It would repeat the exact defect that made the first execution diagnostic-only.
2. **Opening GOLD.** `HISTORICAL_GOLD_V0.jsonl` may not be read before baseline and candidate outputs are frozen and hashed.
3. **Running with source resolutions visible.** The runner must not recover the source commits behind the historical cases before outputs are frozen.
4. **Changing pass thresholds, dimensions, families or the harm rule** after observing a failure. The continuation rule is frozen: candidate material wins >= 2, spanning >= 2 frozen case families, exceeding baseline material wins, with candidate HARM <= 1.
5. **Reusing the `auto` diagnostic run as the protocol-conforming result.** `ARCH-AB-20260906T102435Z` stays `DIAGNOSTIC_EXECUTION_SIGNAL`.
6. **Substituting the current session's model as runner or judge.** Self-adjudication by the context that authored or froze the corpus is contamination, not a shortcut.
7. **Deleting or disabling the `architecture-clean-ab` job to obtain a green PR.** The blocker is the finding; hiding it destroys it.
8. **Promoting the Architecture candidate on the strength of the diagnostic pattern.** Migration, discriminator and anti-build deltas from a `model=auto` run are a hypothesis, not evidence.

## What stays true while this is blocked

- `prompts/SYSTEM.md` remains frozen.
- The Architecture candidate remains `CANDIDATE_CAPABILITY_NOT_AGENT`.
- `ARCHITECTURE_SELECTION_CAPABILITY = UNIQUE_DELTA_NOT_SHOWN`.
- No unseen HOLDOUT may be created; HOLDOUT comes after the clean A/B, not instead of it.
- `STRUCTURAL_CHANGE_ENVELOPE` remains a candidate contract shape, unbuilt.

## Reversal condition

This document is superseded when a protocol-conforming clean A/B completes: an explicit runner model pinned for both baseline and candidate, outputs frozen and hashed before GOLD is revealed, and blind X/Y adjudication recorded.

At that point the result, whatever it is, replaces this file as the Architecture lane's current state.
