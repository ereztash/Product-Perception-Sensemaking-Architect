# R&D Scope Confirmation Stream v0.2

Status: `INITIALIZED · CONFIRMATORY_N=0 · BLOCKED_ON_INDEPENDENT_ADJUDICATION_CHANNEL`
Date: 2026-09-06
Frozen scope: `RND_SCOPE_MAP_V0_2_FROZEN_FOR_CONFIRMATION.md`
Case schema: `schemas/rnd-scope-case-v0.2.schema.json`

## Current counts

| Region | Adjudicable confirmatory N | Win | Tie | Loss | Status |
|---|---:|---:|---:|---:|---|
| R1 EPISTEMIC_ALLOCATION_CORE | 0 | 0 | 0 | 0 | UNKNOWN |
| R2 OBVIOUS_LEARNING | 0 | 0 | 0 | 0 | UNKNOWN |
| R3 DIRECT_AUTHORITY_EXECUTION | 0 | 0 | 0 | 0 | UNKNOWN |
| R4 DOMAIN_METHOD_PRIMARY | 0 | 0 | 0 | 0 | UNKNOWN |
| R5 LOW_LOCAL_CONTROL | 0 | 0 | 0 | 0 | UNKNOWN |

## Why historical cases are not copied here

All previously inspected Yishumi, Neta, R&D-control, Architecture, epistemology/VOI, cost/reversibility and authority cases are discovery-contaminated under v0.2.

They may justify the frozen hypothesis but contribute zero to confirmation.

## Required case admission

A case may enter this stream only if:

1. it is natural and unseen after the v0.2 freeze, or independently frozen before its outputs;
2. live decision and pre-outcome features are preserved before baseline/R&D output;
3. baseline and R&D use the frozen comparator conditions;
4. A/B identity is blinded for adjudication;
5. adjudication is performed by a different model lineage or a qualified human/domain adjudicator;
6. authority-dependent facts are checked by OWNER/REPO/ENVIRONMENT/FIELD as required;
7. any unresolved disagreement is `UNADJUDICABLE`.

## Current execution limitation

The active environment does not expose an external `OPENAI_API_KEY` to run the repository's live adapter as an independent model process, and no separate model-lineage adjudicator is currently connected through the repository runtime.

Manual self-adjudication by the current model is explicitly disallowed from supporting the 95% claim.

Therefore the correct current state is:

`95PCT_SCOPE_CERTAINTY = NOT ACHIEVED`

not a synthetic confidence estimate.

## Next admissible evidence

The next evidence must be one of:

- a newly arriving natural decision task frozen before outputs, followed by blind A/B judgment from an independent human/model lineage;
- an independently frozen external corpus with sufficient live-decision context and qualified gold/adjudication;
- a live runtime experiment after a separate adjudication channel is available.

## Stop rule remains active

No region may exit `UNKNOWN` until its frozen sequential criterion crosses and minimum balance/sample requirements are satisfied.

The program must retain failed/negative evidence; scope repair starts a new version rather than rewriting this stream.
