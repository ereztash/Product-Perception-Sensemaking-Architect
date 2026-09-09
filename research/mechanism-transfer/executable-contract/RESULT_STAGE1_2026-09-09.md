# Executable Contract Repair Experiment — Stage 1 result

Status: `STOP_EXECUTABLE_UNIQUE_DELTA_UNSHOWN`
Date: 2026-09-09
Preregistration: `research/mechanism-transfer/executable-contract/PREREGISTRATION_STAGE1_2026-09-09.md`
Execution commit: `8be7b5c2d8478e8757b2252d28d2683740013c54`
GitHub Actions run: `34333744269`

## Frozen decision rule

Advance only if the executable-contract arm has at least 2 fewer hidden critical failures than the information-matched prose arm, with no test-integrity failure or capture regression.

Tie or executable loss => `STOP_EXECUTABLE_UNIQUE_DELTA_UNSHOWN`.

## Execution

The same prior generated application artifact was recovered for both arms. Four mechanism defects were present in the shared broken base:

- C1 draft lost on COMMIT → back-to-edit;
- C2 chronology checked a surrogate/current-date condition instead of user-entered `observationDate`;
- C3 validation classified `actual !== expected` as pass;
- C4 REVEAL close returned to DECIDE instead of reaching EXPLORE.

Both arms received the same contract semantics and public cases.

- Arm E additionally received immutable executable public contract tests and could run them repeatedly in one repair session.
- Arm P received the same public cases in prose and no executable contract test file.

Hidden evaluator files were absent from both repair directories until both repair sessions had ended.

## Blind score before mapping

| Candidate | Hidden critical failures | Detection recall | Input integrity |
|---|---:|---:|---|
| candidate-1 | 0 | 4 / 4 | PASS |
| candidate-2 | 0 | 4 / 4 | PASS |

Both candidates passed all preregistered hidden gates:

- H1 draft roundtrip variation;
- H2 temporal boundary on actual user field;
- H3 validator discrimination variation;
- H4 reached-state topology;
- H5 capture regression control;
- H6 syntax and immutable-input integrity.

The Stage 1 decision was therefore already fixed as STOP before opening arm mapping.

## Mapping

- candidate-1 = Arm E, executable contract;
- candidate-2 = Arm P, prose contract.

Arm E reported its public executable suite green at 4/4 after repair.

Both arms independently reported all four seeded contract violations before repair and both repaired all hidden gate families.

## Patch comparison

The repaired applications are nearly identical.

The only observed `app.js` difference is that the prose arm added an additional guard for missing `observationDate`:

- executable arm: reject when `observationDate < committedAt`;
- prose arm: reject when `!observationDate || observationDate < committedAt`.

This neighboring improvement was not a preregistered endpoint and does not change the decision. It is recorded only as an exploratory observation.

## Decision

`STOP_EXECUTABLE_UNIQUE_DELTA_UNSHOWN`

Do not run Stage 2 under the frozen protocol. The required Stage 1 advantage did not occur.

Do not build a mechanism-transfer verifier merely because executable contracts are encodable or because their public suite can turn green.

## What the result supports

In this bounded setting — one capable builder, one small static application, four explicit mechanism defects, and an information-matched prose contract that named the same semantics and public cases — executable red/green tests produced **no hidden repair advantage** over prose.

This strengthens H0 for this task regime: the builder could inspect and repair a small, explicit contract set without needing executable feedback to preserve the tested mechanisms.

## What the result does not support

This result does not establish that executable contracts have zero value generally. The experiment has a plausible ceiling condition:

- only four contract families;
- the defects were local and inspectable;
- both arms were explicitly told the exact contract semantics and public cases;
- one builder/model lineage;
- one artifact and one repair session per arm.

Executable contracts may still have unique value under a different decision-relevant regime, such as a much larger invariant surface, repeated stochastic generation, hidden interaction among contracts, regression-heavy repair, or repeated unattended verification. That is a new hypothesis and would require a new preregistration rather than reinterpretation of this result.

## Resource decision

Current allocation: **do not BUILD the verifier yet**.

Any next experiment should first identify a regime in which executable observability is expected to change a real build/repair decision beyond what a high-quality explicit prose specification already achieves. Repeating this four-defect setup has low expected decision value.
