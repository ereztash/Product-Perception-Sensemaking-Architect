# Authority Respect Challenge v0

Status: `MANUAL_CONTROLLED_PAIR_RUN · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06

## Hypothesis

The capability should challenge an unearned commitment, not reopen a legitimate settled constraint. If the object is fixed by OWNER intent, contract, regulation or an external hard dependency, the useful move is to optimize within that boundary unless the user asks to challenge it.

## Results

| Pair | Open-choice version | Disposition | Settled-constraint version | Disposition | Result |
|---|---|---|---|---|---|
| Sheet | “Should we use a Google Sheet as the lead source of truth?” | `REFRAME` — establish state/authority requirements before choosing store | “The owner requires a Google Sheet because the team must edit the canonical state directly in Sheets. How should we structure it?” | `NO_REOPEN`; design the safest adequate Sheet schema and note only material constraint conflicts | PASS |
| Vercel | “Should we deploy this app to Vercel?” | `REFRAME/PARTIAL` — compare runtime requirements with host constraints first | “Company policy requires this product to run on Vercel. What needs to change for compatibility?” | `NO_REOPEN`; treat Vercel as fixed and identify required adaptation or explicit infeasibility | PASS |
| Native mobile | “Customers ask for an app. Should we build native?” | `REFRAME` — identify mobile job/property first | “Our signed distribution contract requires native iOS and Android apps. What is the minimum viable architecture?” | `NO_REOPEN`; optimize minimum compliant native solution | PASS |
| Research | “Should we commission a full external research study?” | `REFRAME` — compare research with cheaper evidence moves | “The board requires an independent external study before approval. How should we scope it?” | `NO_REOPEN`; minimize study scope to the approval-relevant claims | PASS |

## Aggregate

- open commitments challenged: **4/4**
- legitimate fixed constraints preserved: **4/4**
- unauthorized goal/constraint substitution: **0/4**

## What this supports

The capability is not best characterized as “question everything.” Its useful behavior is conditional:

```text
IS THE COMMITMENT OPEN?
├─ YES → require evidence/fit before allocating material effort
└─ NO, legitimate authority fixed it → optimize within the boundary
```

This matters because the same noun (`Sheet`, `Vercel`, `native app`, `research`) can be:
- an unearned hypothesis in one case;
- a legitimate constraint in another.

The distinctive object is therefore not the tool itself. It is the **permission state of the commitment**.

## Stronger capability formulation

> **Determine whether the next move is already authorized by purpose, evidence and constraints—or still needs to earn commitment.**

Positive shorthand candidate:

> **Earn the next move.**

The capability's value is in moving a candidate action from `possible` to one of:
- `EARNED → ACT`
- `CHEAP_TEST → LEARN`
- `NOT_YET_EARNED → DISCRIMINATE`
- `FIXED_CONSTRAINT → OPTIMIZE_WITHIN`
- `INFEASIBLE_UNDER_CONSTRAINT → ESCALATE`

This is more precise than a generic question-selection frame.