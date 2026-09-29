# Agent-Assurance Market: Result of the 2026-09-08 Frozen Instrument

Status: `SCORED · DISCONFIRMATION_RESULT · ZERO_CONFIRMATORY_N`
Run: 2026-09-29
Instrument: `AGENT_ASSURANCE_MARKET_2026-09-08.PLAN.md` (arm B) and `AGENT_ASSURANCE_MARKET_2026-09-08.AB_COMPARISON.md` (arm A and the comparison rule), frozen 2026-09-08 at `main` @ `04574ab`. Both are byte-identical copies of the files on `claude/repo-cleanup-590u82` (commit `3cc1210`, open PR 22), placed here so the rubric and the result it grades sit on one branch.
Reports: `AGENT_ASSURANCE_MARKET_2026-09-29.ARM_B_REPORT.md`, `AGENT_ASSURANCE_MARKET_2026-09-29.ARM_A_REPORT.md`, verbatim.

## Execution and deviations

| Item | Protocol | Actual |
|---|---|---|
| Executor | a commercial deep-research product | two general-purpose Claude agents with web search and fetch |
| Prompt | verbatim | verbatim, inside an identical wrapper for both arms (date, web-only, no repository access, write report to file, return only the path) |
| Separation | separate clean sessions | separate agents; neither could read the repository, so neither saw the other prompt or the preregistered prediction |
| Reading order | read neither until both complete | kept: arm B finished first and stayed unread until arm A finished |
| Arm A | one run | first attempt died on an account rate limit with no output; rerun with identical wrapper and prompt |

The prompts were written by a Claude session and executed by Claude agents. This contributes zero confirmatory N to any claim about R&D capability or about the market. The adjudicator did not independently verify the reports' sources; the two reports disagree on minor facts (for example Galileo acquisition dates), so individual figures should be rechecked before reuse.

## Arm B: kill conditions

| Condition | Result |
|---|---|
| K1 platform absorption | `CONFIRMED`: AWS, Google, Microsoft, OpenAI and Anthropic ship evaluation, guardrails, tracing and policy natively, metered in cents or unpriced |
| K2 bundled feature | `NOT_CONFIRMED`: standalone price lines exist, but only for developer-metered tools |
| K3 buyer size | `NOT_CONFIRMED`: agent governance is sold into the 50–300 band via IT licensing; no COO, CFO or VP People budget owner found |
| K4 blocker is something else | `NOT_CONFIRMED`: trust ranks near cost and integration; no survey isolates the owner's buyer |

Confirmed kills: **1**. Frozen disposition: **`INTERNAL_ASSET`**: keep the capability as consulting differentiation, not a separate product.

Sensitivity: arm A reports bundling at the operator's layer (Salesforce Agentforce Observability unmetered from 2026-07-21; Zendesk; Intercom certifying Fin). Read as K2 evidence, the tally becomes 2 and the disposition `STOP`. Both dispositions forbid building the assurance layer as a product.

## Arm A: verdict

`EXISTS_BUT_ONLY_AT_ENTERPRISE_SCALE`. Paid, standalone assurance exists as developer tooling (bought by engineers, being absorbed by platforms) and as certification or audit (AIUC-1, ISO 42001, HITRUST AI, NYC bias audits), paid by agent vendors to sell into Fortune-1000, federal and health-system procurement. No COO, CFO or VP People at 50–300 employees was found paying a third party to check agent output.

## Comparison metrics

| # | Result |
|---|---|
| `D1` same allocation decision | Yes. Neither supports building a sellable assurance layer for the owner's buyer. |
| `D2` kills | B confirms 1 (K1). A marks the same finding explicitly, and additionally reports buyer-layer bundling that B's literal K2 did not count. |
| `D3` what A returned that B could not, and that would have changed the decision | Empty. A's extra material (procurement text, funding and exits, regulatory detail) reinforced the negative without changing it. B's admissible list still included regulatory text and job postings, and B used both. |
| `D4` admissible share | Similar. Both lean on vendor-sponsored surveys for buyer voice and flag them; A flags more of its unverified figures explicitly. |
| `D5` answerable without research | Partly. The decisive finding is an absence at the owner's buyer size, which desk research cannot close; both reports name a field observation as the cheapest flip. |

Work, from the executor telemetry: arm B 127 tool calls, 263,908 tokens, 18.0 min, 10.9 KB report; arm A 189 tool calls, 301,354 tokens, 24.8 min, 43.8 KB report.

Frozen verdict rule applied: same decision, `D3` empty, less work → **`EARNED_ITS_KEEP`**.

The preregistered prediction was `COST_INCURRED`. It did not occur.

## What this result does not establish

- It does not establish that the R&D scoping pass improves research quality. Both arms reached the same decision; B reached it with roughly a third fewer tool calls and a report a quarter the length. One run per arm, same model lineage.
- It does not establish that no operator buyer exists. The absence is a web-search absence; both reports name a field observation (an invoice or purchase order) as the cheapest flip.

## Lineage

Parent claim: a sellable assurance layer over agent output, bought by a COO, CFO or VP People at a 50–300 employee operator. Disposition: `INTERNAL_ASSET` (sensitivity: `STOP`).

One opening appeared outside the parent claim's buyer: agent vendors buying AIUC-1 certification, whose requirements D002 and D004 call for third-party evaluation of hallucinated outputs and tool calls at least every three months. That is a different buyer, and therefore a **new claim** (`C-VENDOR-ASSURANCE`) with its own instrument: `AGENT_VENDOR_ASSURANCE_2026-09-29.PLAN.md`. It is not evidence for the parent claim and cannot revive it.
