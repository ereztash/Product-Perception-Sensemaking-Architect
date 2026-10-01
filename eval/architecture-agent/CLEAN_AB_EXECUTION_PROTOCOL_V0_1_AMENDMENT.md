# Architecture Clean A/B Execution Protocol v0.1 — Model-Pinning Amendment

Status: `FROZEN_AFTER_EXECUTION_DEFECT_DISCOVERY · BEFORE_RERUN · THRESHOLDS_UNCHANGED`
Date: 2026-09-06

## Why this amendment exists

The first successful technical execution, `ARCH-AB-20260906T102435Z`, used GitHub Copilot CLI with `--model auto` for both runner and judge calls.

That execution correctly preserved the strongest contamination barrier:
- 24 baseline/candidate outputs were completed first;
- `FREEZE_MANIFEST_BEFORE_GOLD` was written and hashed;
- only after freeze did judging begin;
- blind X/Y adjudication completed.

However, `auto` does not establish that all baseline/candidate invocations used the same underlying model. The frozen v0 protocol requires the **same clean model** for A and B. Therefore the first execution is retained as `DIAGNOSTIC_EXECUTION_SIGNAL`, not counted as the protocol-conforming clean A/B result.

This is an execution-contract repair, not a response to which side won. The continuation rule, dimensions, corpus, prompts, X/Y mapping rule and GOLD barrier remain unchanged.

## Pinned rerun

Runner model for **both baseline and candidate**:

`gpt-5.3-codex`

Blind adjudicator model:

`claude-sonnet-4.6`

Rationale:
- both are explicit model identifiers documented for GitHub Copilot CLI programmatic use;
- baseline and candidate now use one identical pinned runner model;
- a different pinned judge reduces same-model preference in pairwise adjudication;
- neither judge nor runner receives repository tools, web tools, prior conversation context or GOLD before the freeze barrier.

## Frozen continuation rule — unchanged

Proceed to unseen HOLDOUT only if all remain true:

1. candidate material wins >= 2;
2. candidate wins span >= 2 frozen case families;
3. candidate material wins > baseline material wins;
4. candidate HARM <= 1.

No threshold, family assignment, delta dimension or scoring rule is changed after observing the first diagnostic execution.

## First execution retained

`ARCH-AB-20260906T102435Z` remains useful for:
- validating the harness;
- validating Copilot authentication;
- validating the freeze-before-GOLD barrier;
- detecting gross instability if the pinned rerun differs radically.

It is not promotion evidence because runner-model identity was not fixed.
