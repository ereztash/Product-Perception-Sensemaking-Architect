# External GitHub Scope Test — Batch 01 External-Outcome Adjudication

Status: `EXTERNAL_MAINTAINER_OUTCOME_ADJUDICATION · FROZEN_OUTPUTS_PREDATE_OUTCOME_READ · SAME_MODEL_OUTPUTS · EXTERNAL_GOLD_DIRECTIONAL · NOT_95PCT_CONFIRMATION`
Date: 2026-09-06
Frozen outputs commit: `dc484a2b9f39972510b1ddbb44be423bb7936424`

## Method

For each issue, the issue body was read and the following were frozen before reading resolution comments / linked fix PRs:
- pre-outcome scope region;
- strong-baseline next move;
- R&D next move;
- predicted material delta.

Only after that freeze were maintainer comments / linked PRs read.

External outcomes are stronger than same-model self-adjudication because the resolution was produced outside this project. They still do not satisfy the v0.2 95% confirmation protocol because baseline/R&D outputs were role-conditioned by the same model and the outcome is observational rather than a blinded independent adjudicator.

## Results

| Case | Frozen region | External outcome | Adjudication | Scope note |
|---|---|---|---|---|
| EXT-01 VS Code #325111 | R2 | Closed as duplicate of a more specific regression issue (#324985), which isolated a UI-overlay-triggered degradation and received an Insiders fix | `TIE_NO_MATERIAL_DELTA` | Direct duplicate/repro/performance triage was sufficient; full R&D not earned |
| EXT-02 Z3 #10645 | R2 | Maintainer investigated interacting solver changes; final finding involved instantiation guidance / hash behavior, i.e. direct solver diagnosis from the supplied regression artifact | `TIE_NO_MATERIAL_DELTA` | Adjacent good/bad commits + concrete SMT artifact correctly made this direct domain diagnosis, not R&D allocation |
| EXT-03 winappCli #729 | R2 | PR #751 found two flaky-test mechanisms; for tree-kill the apparent timeout masked a failed child start + empty PID file; fix surfaced root task/stderr and removed blind timing assumptions | `TIE_NO_MATERIAL_DELTA` | Frozen baseline and R&D both pointed at process lifecycle / timing instrumentation; R&D did not add a unique next move |
| EXT-04 gh-aw #53729 | R2 | PR #53777 hardened benchmark methodology: time-based benchtime, median history baseline, multi-benchmark environment-noise detection; no code regression investigation first | `TIE_NO_MATERIAL_DELTA` | Issue body already contained the key cheap discriminator/noise hypothesis; full R&D unnecessary |
| EXT-05 Beam #39010 | R3 | Issue closed with no comments and no uniquely linked resolution recoverable from issue/PR search | `UNADJUDICABLE` | External outcome insufficient; retain without forcing a label |
| EXT-06 Checkstyle #20818 | R1 | Maintainers rejected hardcoded cross-run baseline as confounded by runner variance; PR #20843 measured master and PR on the same runner and verified that the new dynamic baseline was stable and still detects controlled regressions | `MATERIAL_RND_WIN` | R&D uniquely protected the measurement objective and kept multiple evidence-system designs open instead of prematurely choosing manual trigger / threshold tweaking |
| EXT-07 Paperclip #4328 | R1 | Later evidence showed missing comments were a test-observation race; merged PR #8315 used a test-only wait predicate so assertions occur after the relevant async writes commit | `MATERIAL_RND_LOSS` | Full R&D allocation framing was overkill. The issue was fundamentally domain debugging/test synchronization; frozen R1 coding was a false fire |
| EXT-08 Pulsar #24628 | R4 | PR #26243 traced the flake to a production shutdown deadlock in `TableViewLoadDataStoreImpl`, built a deterministic reproducer, and fixed blocking close under a synchronized monitor with async close | `TIE_NO_MATERIAL_DELTA` | Correctly domain-method primary: deep engineering diagnosis solved it; R&D had no separate allocation judgment to own |

## Aggregate

Adjudicable: 7 / 8

- `MATERIAL_RND_WIN`: 1
- `TIE_NO_MATERIAL_DELTA`: 5
- `MATERIAL_RND_LOSS`: 1
- `UNADJUDICABLE`: 1

### Frozen R1 subset

- EXT-06: WIN
- EXT-07: LOSS

Observed external-outcome directional rate in this tiny R1 subset:
- win 1/2
- loss 1/2

This is far below the frozen HIGH_VALUE_CORE target if treated as confirmatory, but N=2 and this batch is not protocol-compliant confirmation evidence. It must not be converted into a confidence claim.

## Most important new information

The Paperclip failure exposes an ambiguity in the pre-outcome coding manual:

```text
MULTIPLE TECHNICAL HYPOTHESES
!=
NONTRIVIAL EPISTEMIC ALLOCATION
```

A domain method such as debugging often contains:
- multiple hypotheses;
- instrumentation choices;
- discriminating tests;
- sequential evidence.

Those facts alone do not make R&D primary.

The sharper candidate distinction is:

### DOMAIN DIAGNOSTIC BRANCHING
The evidence moves are part of the normal domain method for resolving the domain object (bug, architecture tradeoff, product mechanism).

→ `R4_DOMAIN_METHOD_PRIMARY`

### EPISTEMIC ALLOCATION DECISION
The system faces a separable meta-decision about which evidence program/channel/method deserves resources because the alternatives differ materially in validity, authority, cost, delay, contamination, reach, or future policy effect.

→ `R1_EPISTEMIC_ALLOCATION_CORE`

Paperclip looked like the latter on the first coding pass because it listed competing mechanisms and fixes. The external resolution indicates it was the former.

## Checkstyle as positive contrast

Checkstyle is not merely a performance bug. The live object was the **measurement system itself**:
- hardcoded baseline vs same-run baseline;
- manual vs automatic invocation;
- repetitions / variance;
- cost vs sensitivity;
- whether noise reduction destroys the ability to catch true regressions.

That is a separable allocation/design question about how to acquire decision-relevant evidence, and the external fix converged on redesigning the measurement method rather than bypassing measurement.

This contrast provides a useful neighbor pair:

```text
PAPERCLIP
bug diagnosis with several mechanisms
→ DOMAIN METHOD

CHECKSTYLE
which measurement/evidence system should govern future regression decisions?
→ R&D CANDIDATE
```

## Scope consequence

Do not alter frozen confirmation v0.2 retroactively.

Current v0.2 state remains `UNKNOWN` because this batch is not confirmatory evidence.

But for a future v0.3 discovery/coding repair, test the following candidate rule:

> `NONTRIVIAL_EPISTEMIC_ALLOCATION` requires a separable choice over the learning/evidence program itself; ordinary diagnostic branching internal to an established domain method remains `DOMAIN_METHOD_REQUIRED`.

This repair must be tested on unseen neighbors before any promotion.

## External-test verdict

`EXTERNAL_TESTING: EXECUTED`

`SCOPE_HYPOTHESIS: SURVIVES_DIRECTIONALLY_BUT_BOUNDARY_CODING_IS_TOO_PERMISSIVE`

`NEW_FAILURE_FAMILY: DOMAIN_DIAGNOSTIC_BRANCHING_MISCLASSIFIED_AS_EPISTEMIC_ALLOCATION`

`95PCT_SCOPE_CERTAINTY: NOT ACHIEVED`
