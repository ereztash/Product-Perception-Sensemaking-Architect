# Agent-Assurance Market — A/B Comparison of the R&D Scoping Pass

Status: `FROZEN_BEFORE_RUN · SAME_MODEL_LINEAGE · NOT_PROSPECTIVE_VALIDATION`
Frozen: 2026-09-08
Frozen at `main` @ `04574ab10e76f56cb30302d47114565bcc9f34ae`
Companion to: `AGENT_ASSURANCE_MARKET_2026-09-08.PLAN.md`

## What is under test

Not the market. The **R&D scoping pass itself**.

The same underlying question was written twice: once directly, once after routing it
through the R&D v0.2 calibration method. Both are run as separate deep-research jobs
and compared.

The live question is whether routing a research question through R&D changes what comes
back, and whether the change is an improvement or a loss.

`QD_VS_RND_V0_RUN.md` found ten cases out of ten where the front-door gate produced no
unique decision beyond the existing loop. That result is the prior here. **R&D can lose
this comparison**, and the thresholds below are written so that it can.

## Arm A — direct framing, written before the R&D pass

```text
DECISION THIS RESEARCH SERVES

I am choosing between two allocations of the next three months:
(A) build more agents into a service catalogue
(B) build a sellable assurance layer that certifies whether any agent's
    output may be acted on, carrying evidence level, resolution authority,
    action permission and reversal condition

Do NOT research whether the AI agent market is growing. Assume it is.
That fact is consistent with both options and cannot discriminate between them.

PRIMARY QUESTION

Is anyone paying money, today, for assurance, verification or certification
of AI agent output, as a purchase separate from the agent itself?

BUYER CONSTRAINT

My buyer is a COO, CFO or VP People at a 50 to 300 employee growth-stage
company in cybersecurity, fintech or healthtech.
If the only demonstrated buyers are enterprises above 5,000 employees,
say so explicitly. That is a negative answer for me, not a positive one.

SUB-QUESTIONS, in order

1. Named vendors selling agent-output assurance standalone. Require a
   pricing page or a public contract value, not a landing page. Who buys,
   at what company size, in what industry.
2. Procurement evidence. RFP text, vendor security questionnaires, enterprise
   AI procurement checklists, SOC 2 or ISO addenda that require evidence an
   agent's output was validated before action. Quote the actual language.
3. Regulatory forcing functions. EU AI Act obligations with dates, sector
   rules in financial services and healthcare. Distinguish an obligation that
   creates an internal compliance task from one that creates a purchasable
   product.
4. Job postings. Is anyone hiring for AI evaluation, agent assurance or
   LLM QA as a named function. Seniority, industry, company size, volume
   trend over 18 months. Postings cost money, so they outrank analyst reports.
5. Funding. Rounds in the last 18 months where the investor's own description
   of the category is evaluation, assurance or observability for agent output.
   Names, amounts, stated wedge.
6. KILL CONDITION. To what extent are the model platforms shipping this
   natively as evals, guardrails and tracing. If a third-party layer is
   converging to a free platform feature, say so plainly.
7. Buyer voice. Find actual buyers, not vendors, describing trust in agent
   output as a blocker to deployment, in their own words, with attribution.
   Compare how often they name it against cost, accuracy and integration.

ADMISSIBLE EVIDENCE

Pricing pages. RFP and questionnaire text. Regulatory text with dates.
Job postings. Funding announcements naming the category. First-person buyer
statements with attribution. Post-mortems of failed agent deployments.

INADMISSIBLE AS PRIMARY EVIDENCE

Analyst TAM projections. Vendor blog posts describing their own category.
Forecasts about 2030. LinkedIn commentary. Any claim without a named source.

WHAT WOULD MAKE THIS A WASTE OF TIME

State it explicitly if you find any of the following:
- no vendor sells assurance standalone at a published price
- the pattern is that the agent vendor bundles it, making it a feature
- platforms already ship it and it is converging to free
- regulation creates an internal obligation with nothing to buy
- buyers name cost, accuracy or integration far more often than trust
- demonstrated buyers are all far larger than 300 employees

OUTPUT FORMAT

Per sub-question: what you found, the two or three strongest sources with
links and dates, and your confidence.

Then one verdict, chosen from exactly these:
  MARKET_EXISTS_AND_IS_BUYABLE_AT_MY_BUYER_SIZE
  EXISTS_BUT_ONLY_AS_A_BUNDLED_FEATURE
  EXISTS_BUT_ONLY_AT_ENTERPRISE_SCALE
  EMERGING_NOT_YET_BUYABLE
  NO_EVIDENCE

Then name the single cheapest observation that would flip your verdict.

DO NOT FILL GAPS

If a sub-question has no evidence, write "no evidence found" and list what
you searched. Absence is a finding and I want it reported as one.
Do not smooth a weak answer into a moderate one.
```

## Arm B — after the R&D pass

Verbatim in `AGENT_ASSURANCE_MARKET_2026-09-08.PLAN.md`, section "The frozen prompt".
Not duplicated here, so the two copies cannot drift.

## What the R&D pass actually changed

The difference is narrower than before-and-after. Arm A already carries a buyer
constraint, one kill condition and a waste-of-time list.

| | A | B |
|---|---|---|
| Role of the instrument | validation containing a kill condition | disconfirmation only |
| Sub-questions | 7 | 4 |
| Output | five verdicts | a count of confirmed kills |
| What decides | the researcher's judgement | a rule frozen in advance |

B removed four topics: broad vendor enumeration, procurement text, regulation, and
funding rounds.

**One of those removals is a bet that may be wrong.** The stated rationale was to remove
everything that could only support a positive answer. Regulation and job postings do not
behave that way. If nobody is hiring for agent assurance as a named function, and if the
EU AI Act creates an internal compliance obligation with nothing purchasable attached,
both are strong negative findings. B may have discarded two good disconfirmation sources
to buy tightness.

That is the specific thing this comparison exists to catch.

## Comparison metrics

Fill these in from the two reports before forming any opinion about which arm was better.

| # | Metric |
|---|---|
| `D1` | Do the two reports lead to the same allocation decision, yes or no |
| `D2` | How many kills does B confirm, and how many of those sit unmarked inside A's prose |
| `D3` | What did A return that B could not have returned, and that would have changed the decision |
| `D4` | Share of sources in each report meeting the admissibility criteria |
| `D5` | Could either question have been answered without buying research at all |

`D3` is the load-bearing one. It measures whether the R&D pass cost something.

## Frozen verdict rule

Written before any result. Recorded so a weak outcome cannot be rescued afterwards.

| Result | Verdict on the R&D scoping pass |
|---|---|
| B reaches the same decision with less work, `D3` empty | `EARNED_ITS_KEEP` |
| Both reach the same decision, `D3` empty, similar volume | `CEREMONY`. R&D added nothing here |
| `D3` non-empty | `COST_INCURRED`. Restore what B pruned and re-run |
| The two reach different decisions | `CONFLICT`. Record both, do not average. The disagreement is the finding |

## Preregistered prediction

The session that wrote both prompts predicts `COST_INCURRED`, on the grounds that
dropping regulation and job postings removed two sources capable of returning a decisive
negative.

Recorded here so the prediction can be wrong in public. A comparison whose author cannot
be embarrassed by it is not a comparison.

## Run hygiene

1. Run each arm in a separate clean session. Neither may see the other's prompt or output.
2. Read neither report until both have completed. Reading A first carries its framing into
   the reading of B, and the comparison stops being one.
3. Do not reword either prompt between runs. A reworded arm retires everything measured
   before the change.

## Admissibility of this comparison

Both arms will be executed by a commercial deep-research product, and both prompts were
written by the same session and model lineage. This is a scoping comparison, not
independent triangulation, and it contributes zero confirmatory N to any claim about R&D
capability. Its output is a decision about how to write the next research task, and the
allocation decision the task serves.
