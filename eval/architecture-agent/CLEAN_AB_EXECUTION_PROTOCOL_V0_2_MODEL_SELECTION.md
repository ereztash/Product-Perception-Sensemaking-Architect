# Architecture Clean A/B Execution Protocol v0.2 — Explicit Model Selection

Status: `FROZEN_AFTER_MODEL_AVAILABILITY_FAILURE · BEFORE_NEXT_RERUN · VERDICT_THRESHOLDS_UNCHANGED`
Date: 2026-09-06

## Trigger

The first technical run used `auto`, which does not prove same underlying runner model across A/B calls.

The first pinned rerun attempted `gpt-5.3-codex`, but the workflow entitlement returned `Model "gpt-5.3-codex" ... is not available` before the first case completed.

Neither event changes the benchmark verdict rule. Neither is promotion evidence.

## Selection rule frozen before the next case run

Before loading any benchmark case, probe the following explicit Copilot CLI model IDs **in this fixed order**:

1. `gpt-5.4`
2. `claude-sonnet-4.6`
3. `gpt-5-mini`
4. `claude-haiku-4.5`
5. `gemini-3.5-flash`

Each probe is a fresh, non-interactive invocation with no repository tools requested and no benchmark case/GOLD content.

Selection:
- `runner_model` = first explicit model in the ordered list that completes a minimal probe;
- `judge_model` = second distinct explicit model that completes a minimal probe;
- if exactly one explicit model is available, use that same pinned model for blind judging as well;
- if zero explicit models are available, STOP. `auto` is not an admissible substitute for the protocol-conforming A/B because model identity would remain uncontrolled.

The selected model IDs and full available subset must be written to `runtime/architecture_ab/MODEL_SELECTION.json` before the benchmark begins.

## Why this does not move the goalposts

The original protocol required the same clean runner model but did not freeze a provider/model identity. This amendment operationalizes that pre-existing requirement under the actual Copilot entitlement.

The corpus, prompts, neutral output schema, blind X/Y mapping, GOLD barrier, dimensions, harm rule and continuation thresholds remain unchanged.

## Continuation threshold — unchanged

Proceed to unseen HOLDOUT only if:
1. candidate material wins >= 2;
2. candidate wins span >= 2 frozen case families;
3. candidate material wins > baseline material wins;
4. candidate HARM <= 1.
