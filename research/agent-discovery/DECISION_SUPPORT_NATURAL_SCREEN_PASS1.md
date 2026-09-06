# Decision Support Observatory — Natural Screen Pass 1

Status: `HISTORICAL_NATURAL_SCREEN · DISCOVERY_ONLY · SAME_CONTEXT_INTERPRETATION · NO_CAPABILITY_PROMOTION`
Date: 2026-09-06

## Purpose

Test whether the plausible cross-cutting residual from Agent Discovery Pass 1 actually recurs in natural historical work:

> explicit owner priorities + viable alternatives + sufficiently bounded information → nontrivial cross-criterion tradeoff / ranking robustness → owner commitment.

This screen is designed primarily to **exclude false positives** that merely look like alternative selection.

## Admission rule

A case is positive-looking only if:
- decision is consequential;
- >=2 viable alternatives remain;
- owner objectives/mandatory constraints are sufficiently explicit;
- the main missing object is not further evidence acquisition;
- the main missing object is not domain diagnosis;
- no direct authority fact or mandatory criterion already dominates;
- comparison/recommendation is the live unresolved judgment.

## Cases

### DS-NAT-01 — Lichess reveal routing

Natural historical artifact: `Pasted markdown(20260903-112504).md`.

Decision:
- A: direct route from reveal to next position;
- B: route through record, the existing path.

Available before recommendation:
- both options already built/measured;
- press-count difference;
- funnel denominator consequences;
- RNL-11 constraint against changing instrument/intervention together;
- protocol re-freeze consequence;
- mobile navigation risk.

The artifact compares consequences and recommends B while retaining OWNER decision.

Classification: `POSITIVE_LOOKING`.

Contamination/boundary concern:
The criteria are jointly product + experiment-design. Neta + R&D composition may already be sufficient. This is not yet evidence for an independent capability.

### DS-NAT-02 — ALUT business model: setup vs service vs hybrid

Natural artifact: `Pasted text(57).txt`.

The document presents three commercial models and tentatively recommends Hybrid for a pilot because it shares risk and permits learning before commitment.

However, the same artifact explicitly records unresolved owner/data questions before a real decision:
- exact telemarketing economics;
- data ownership/exportability;
- operational state;
- contract/exit terms;
- owner objective: cost reduction vs revenue growth vs data control;
- approval politics;
- pilot success criteria.

It asks the board to approve `audit + MVP`, not purchase/full model commitment.

Classification: `EXCLUDE_RND_OWNER_PRIMARY`.

The attractive three-option table is not evidence that information is sufficiently bounded for a post-information tradeoff capability.

### DS-NAT-03 — Agent Architect: outreach vs productization

Natural artifact: `Pasted text(15).txt`.

The important choice was to prefer an outreach-test agent over more product architecture when the buyer/action question dominated and the product was partially defined.

The chosen move was explicitly a 7-day evidence-generating test. The evidence-fit gate marked the bottleneck only partially proven.

Classification: `EXCLUDE_RND_PRIMARY`.

This is epistemic allocation / question qualification, not a clean post-information choice.

### DS-NAT-04 — COPT pricing model options

Natural artifact: `COPT_Unicorn_Validation_Report.pdf`.

Options include per-token pricing, revenue share and tiered SaaS. The report rejects per-token economics, flags revenue-share revenue density, and calls tiered SaaS optimal.

Classification: `EXCLUDE_DOMAIN_OR_DOMINATED` for this discovery pass.

Reason:
The comparison is largely commercial/unit-economics analysis; one option is described as economically nonviable and another marginal. This does not yet expose a hidden cross-cutting judgment beyond finance/business modeling + ordinary comparison.

### DS-NAT-05 — Lichess palette/density owner gate

Natural artifact: `Pasted markdown(20260901-170414).md`.

Technical work had established accessibility/systematic color and UI state, but the remaining questions were explicitly:
- is the palette liked?;
- is there too much on the screen?

The artifact correctly stops and asks OWNER to inspect the live preview.

Classification: `EXCLUDE_OWNER_VALUES_MISSING`.

A tradeoff engine must not manufacture taste/preferences merely because technical evidence is exhausted.

### DS-NAT-06 — Product deletion-policy OWNER_DEFER family

Repo cases:
- OSS-0014 Actual Budget;
- OSS-0030 SparkleShare;
- OSS-0034 Organic Maps;
- OSS-0039 SiYuan.

Each contains an apparent local alternative (confirmation vs undo/no-confirm; implement parity vs preserve asymmetry), but the decisive policy/value is explicitly OWNER-owned and missing or intentionally contextual.

Classification: `EXCLUDE_OWNER_VALUES_MISSING`.

## Aggregate

Natural decision families screened: 6.

- `POSITIVE_LOOKING`: 1
- `RND_PRIMARY`: 2
- `OWNER_VALUES_MISSING`: 2 families
- `DOMAIN_OR_DOMINATED`: 1

No recurring clean Decision Support residual is established.

## Decision delta from this screen

Before:

`DECISION_SUPPORT_CAPABILITY = PLAUSIBLE_OPEN_CHALLENGER`

After:

`DECISION_SUPPORT_CAPABILITY = PLAUSIBLE_BUT_RECURRENCE_NOT_OBSERVED`

`DECISION_SUPPORT_AGENT = NOT_EARNED`

The observatory remains useful because the current corpus structurally under-samples cases **after** owner priorities are explicit. But this is an observability gap, not permission to build.

## Strongest falsifier currently

If future post-OWNER cases continue to collapse into:
- R&D when ranking depends on information worth buying;
- Neta/Architecture/domain method when specialized judgment controls;
- OWNER when values are missing;
- direct action when one option dominates;

then the Decision Support candidate should be retired as a separate capability. Its useful behavior can remain a synthesis format composed from existing methods.

## Next evidence threshold

Do not design a Decision Support peer from the single Lichess positive-looking case.

Reopen capability design only after at least 5 natural admissible cases survive the exclusion rule, preferably across >=3 domains, before any baseline/challenger prompt is written.
