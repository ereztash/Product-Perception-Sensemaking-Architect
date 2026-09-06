# Question-Space Challenge v0

Status: `MANUAL_SAME_MODEL_CHALLENGE · NATURAL_HISTORICAL_PROMPTS · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06

## Question under test

Does the full capability add unique value when there is **no explicit premature tool/solution/object** and the user instead asks a broad prioritization/diagnostic question?

Compare:
- `B_DECISION_ONLY`: identify the underlying decision/purpose and answer.
- `D_FULL`: decision → inspect commitments → identify controlling uncertainty → choose best question to resolve now → cheapest check.

If D does not materially outperform B here, the current evidence does not support positioning the product primarily as “finding the highest-leverage question.”

## Cases and adjudication

| Case | Natural prompt | B_DECISION_ONLY | D_FULL | Incremental D value |
|---|---|---|---|---|
| QS-01 | “What should I do first, second, third?” | Orders actions by goal, dependency, impact and reversibility | Adds explicit uncertainty check before ordering | `PARTIAL` — useful discipline, usually same sequence logic |
| QS-02 | “what should be demoted, not deleted” | Distinguishes core vs secondary functions and preserves optionality | Adds test of what future decision each retained element still serves | `PARTIAL` — cleaner preservation rule, little evidence of changed action |
| QS-03 | “what should be hidden until later” | Prioritizes information/actions by current user need | Adds question of which uncertainty/user state makes later exposure useful | `PARTIAL` — often same progressive-disclosure result |
| QS-04 | “what should not be designed before the infrastructure exists” | Identifies dependencies and postpones downstream design | Full chain finds no premature commitment and preserves the dependency question | `NO_INCREMENTAL_DELTA` |
| QS-05 | “What is the deepest thing it still risks getting wrong?” | Searches for highest-impact failure relative to telos | Full chain asks which unresolved uncertainty could invalidate the largest part of the current model | `PARTIAL` — sharper falsifier, but ordinary strong reasoning already seeks the same risk |
| QS-06 | “What really needs to change” | Locates bottleneck/root cause before recommending changes | Full chain explicitly chooses the cheapest discriminating question among competing mechanisms | `PARTIAL_TO_MATERIAL`, depending on available competing mechanisms; not reliably unique from prompt alone |
| QS-07 | “What should be fixed before use” | Prioritizes blockers by harm, necessity and reversibility | Full chain makes each proposed fix compete against a use-blocking criterion | `PARTIAL` — better stop rule, not a different core decision |
| QS-08 | “מה אתה מציע לעשות?” | Uses context to identify next decision/action | Full chain makes unresolved uncertainties explicit before choosing next move | `PARTIAL` — advantage depends on context complexity, not on question selection itself |

## Aggregate

- clear material unique wins for D over decision-only: **0/8 reliably established**
- partial discipline/clarity gains: **7/8**
- no incremental delta: **1/8**
- harm: **0/8**

## Interpretation

This challenge does **not** support the strong claim that the distinctive capability is a general search for the globally “highest-leverage question.”

When the user already asks an upstream prioritization/diagnostic question, a strong decision-oriented baseline usually performs most of the useful work. The full chain often adds:
- a clearer falsifier;
- a cheaper discriminator;
- a stop rule;
- explicit competing mechanisms.

Those are useful, but they do not yet demonstrate a separate product wedge called question selection.

## Updated hypothesis

The strongest distinctive behavior remains **commitment qualification**:

> Determine whether the object/action embedded in the current question has earned the right to receive the next unit of effort.

If it has, answer/act directly.
If it has not, move upstream to the smallest uncertainty that can qualify, redirect or reject that commitment.

The positive framing is therefore closer to:

> **Qualify the next move before you invest in it.**

or structurally:

> **Match the next unit of effort to the uncertainty that can most justify or redirect it.**

This remains a research hypothesis, not a final product name.