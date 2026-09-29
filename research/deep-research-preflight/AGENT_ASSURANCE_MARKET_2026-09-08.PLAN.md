# Agent-Assurance Market — Frozen Disconfirmation Plan

Status: `FROZEN_BEFORE_RUN · DISCONFIRMATION_INSTRUMENT · NOT_CANONICAL`
Frozen: 2026-09-08
Frozen at `main` @ `04574ab10e76f56cb30302d47114565bcc9f34ae`
Task: `AGENT_ASSURANCE_MARKET_2026-09-08.task.json`
Comparison arm: `AGENT_ASSURANCE_MARKET_2026-09-08.AB_COMPARISON.md`

## Decision this serves

Three months of owner time, between building breadth of agents into a service
catalogue and building a sellable assurance layer over agent output.

## Why this is scoped as disconfirmation

Willingness to pay by a 50 to 300 employee company resolves to `FIELD`. No scan of
public sources can settle it; that sits above the authority ceiling of every source
this instrument can read.

The value is therefore asymmetric. A negative finding is decisive and cheap. A
positive finding leaves the buyer question fully open and cannot authorize the build
on its own.

Everything that could only support a positive answer was removed from the prompt for
that reason, including funding-round mapping and broad vendor enumeration. A category
that investors fund is not a category the named buyer purchases.

## The frozen prompt

Run verbatim. A reworded question retires everything measured before the change.

```text
DECISION THIS RESEARCH SERVES

Three months of my own time, choosing between building breadth of agents
and building a sellable assurance layer over agent output.

This research is a DISCONFIRMATION instrument. It cannot establish that my
buyer will pay; that resolves to field contact and is out of scope here.
Its entire job is to tell me cheaply if the idea is already dead.
Scope the work accordingly. Do not pad a weak answer to look balanced.

THE FOUR KILL CONDITIONS

Answer each one separately. Any single confirmed kill is decisive.

K1 — PLATFORM ABSORPTION
Are the model platforms shipping agent-output evaluation, guardrails,
tracing and policy enforcement natively, and at what price. If the
functionality is converging to a free or near-free platform feature,
a third-party layer is commoditized before it ships.
Look at: released product pages with dates, changelogs, pricing tiers.

K2 — BUNDLED FEATURE, NOT PRODUCT
Where assurance is sold, is it ever sold standalone with its own price,
or is it always packaged inside an agent or observability product.
A capability that never has its own line item is a feature.
Look at: pricing pages, not landing pages. Public contract values.

K3 — BUYER SIZE MISMATCH
My buyer is a COO, CFO or VP People at 50 to 300 employees in
cybersecurity, fintech or healthtech. Where assurance is bought, at what
company size, with what budget owner and out of which budget line.
If every demonstrated buyer is above 5,000 employees with a dedicated
AI governance function, that is a negative answer for me.

K4 — THE BLOCKER IS SOMETHING ELSE
When buyers describe what stops them deploying agents, in their own words,
how often is trust in the output named, compared with cost, accuracy,
integration effort and data access.
Look at: first-person buyer statements with attribution, deployment
post-mortems, survey instruments where the question wording is visible.

ADMISSIBLE

Pricing pages. Product pages and changelogs with dates. Regulatory text
with compliance dates. Job postings. First-person buyer statements with
attribution. Deployment post-mortems.

INADMISSIBLE

Analyst market sizing. Vendor claims about their own category. Anything
projecting past 2027. Commentary without a named source.

OUTPUT

Per kill condition: CONFIRMED / NOT_CONFIRMED / NO_EVIDENCE, the two
strongest sources with links and dates, and one sentence on why that
evidence settles or fails to settle it.

Then one line: how many of K1 to K4 are CONFIRMED.

Then the cheapest single observation that would flip any NOT_CONFIRMED
to CONFIRMED.

If a kill condition has no evidence, write NO_EVIDENCE and list what you
searched. Absence is a finding. Do not fill the gap with adjacent material.
```

## Preregistered stop rule

Frozen before any result is read. Recorded here so a weak result cannot be rescued
after the fact.

| Confirmed kills | Disposition |
|---|---|
| 2 or more | `STOP`. Do not build the assurance layer as a product. Return to consulting. |
| exactly 1 | `INTERNAL_ASSET`. Keep it as consulting differentiation, not a separate product. |
| 0 | `FIELD_AUTHORIZED`. Spend five ICP contacts and no more. |

`0` does not mean a market exists. It means no cheap reason to abandon was found.

`NO_EVIDENCE` on a kill condition counts as `NOT_CONFIRMED` for the tally and is
recorded separately as a coverage gap, not converted into a weak positive.

## What this instrument cannot do

It cannot establish demand, price, willingness to pay, or that the owner's buyer has a
budget line. Those resolve to `FIELD` and require contact with named people. If the
result is `FIELD_AUTHORIZED`, the next instrument is five conversations, not more
reading.

## Ordering, and why

Cold contacts in the owner's ICP are non-renewable. This research burns money instead.
It therefore runs first even though field contact is the higher-authority instrument,
because a confirmed kill saves the contacts entirely.

## Contamination note

The R&D diagnosis that produced this scoping was executed manually against the frozen
`prompts/RND_AGENT_V0_2_CANDIDATE.md` by the same session and model lineage that wrote
the surrounding analysis, because this environment holds no adapter credential. It is
method discipline applied to a question, not an independent peer opinion, and it
contributes zero confirmatory N. A later run through the calibration loop with a live
adapter would supersede it and should be recorded as a separate trace.
