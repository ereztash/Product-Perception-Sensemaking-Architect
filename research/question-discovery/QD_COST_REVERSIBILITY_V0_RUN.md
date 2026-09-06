# Cost / Reversibility Sensitivity Challenge v0 — Run

Status: `MANUAL_SAME_MODEL_CONTROLLED_RUN · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06
Frozen cases: `QD_COST_REVERSIBILITY_V0_FROZEN.md`

## Results

| Pair | High-cost case | Full disposition | Low-cost case | Full disposition | Sensitivity |
|---|---|---|---|---|---|
| A CRM | 6-week full migration | `REFRAME` — first locate whether friction is tool-owned and whether migration removes it net of switching cost | 30-minute sandbox reproduction | `ACT_AS_TEST` — the proposed action is already the cheap discriminator | PASS |
| B Mobile | 8-week native build | `REFRAME` — identify blocked mobile job/property before funding native apps | 1-hour mock shown to requesters | `ACT_AS_TEST` — cheap reversible prototype directly discriminates the need | PASS |
| C Market uncertainty | 3-week market research project | `REFRAME` — first specify the live uncertainty and whether a cheaper evidence source can resolve it | review five lost deals today | `ACT_AS_TEST` — existing evidence review is cheap and directly informative | PASS |
| D Kubernetes | 40-hour course | `REFRAME` — identify which live scaling decisions actually require Kubernetes-specific knowledge | 20-minute mapping of decisions where Kubernetes knowledge was missing | `ACT_AS_TEST` — cheap self-audit is the discriminator | PASS |

## Detailed interpretation

### High-cost side
In all 4 high-cost cases the capability moved upstream before committing resources. It did not reject the named move categorically; it required the move to earn itself against the uncertainty that controls the decision.

### Low-cost side
In all 4 low-cost cases the capability did **not** manufacture a more abstract question. It recognized that the proposed action was:
- cheap;
- reversible;
- bounded;
- informative about the same uncertainty.

The correct output was therefore effectively:

```text
DO THE CHEAP TEST
→ OBSERVE
→ THEN DECIDE WHETHER THE EXPENSIVE COMMITMENT IS EARNED
```

## Aggregate

- expensive commitments correctly gated: **4/4**
- cheap informative actions allowed through: **4/4**
- mechanical over-reframe of cheap tests: **0/4**
- pairwise sensitivity: **4/4**

## What this experiment supports

This is stronger evidence for a **commitment-qualification / effort-allocation gate** than for a generic “better question” product.

The capability appears especially good at distinguishing:

> **a decision that needs more qualification before resources are committed**

from:

> **a cheap reversible action that should simply be used as the next piece of evidence.**

That distinction is central to the parent ecosystem telos: cheapest admissible decision-changing evidence before expensive action.

## Positive capability wording suggested by the result

The strongest positive formulation now is not:

> prevent wasted work

and not yet:

> find the globally highest-leverage question

but:

> **Earn the next move.**

Operationally:

> **Determine what deserves the next unit of effort, and what evidence is sufficient to justify it.**

or:

> **Match the next unit of effort to the evidence that can justify or redirect it.**

## Limit

This is a controlled synthetic pair test, so it establishes structural behavior under manipulated cost/reversibility; it does not establish that real users will supply enough context for the system to estimate those properties correctly.