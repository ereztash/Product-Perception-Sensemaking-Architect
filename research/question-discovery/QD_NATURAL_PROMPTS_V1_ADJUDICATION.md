# Question Discovery Natural-Prompt Benchmark v1 — Adjudication

Status: `RETROSPECTIVE_NATURAL_SIGNAL · SAME_MODEL_ADJUDICATION · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06
Inputs: `QD_NATURAL_PROMPTS_V1_FROZEN.md`
Baseline: `QD_NATURAL_PROMPTS_V1_BASELINE.md`
Challenger: `QD_NATURAL_PROMPTS_V1_CHALLENGER.md`

## Scoring rule

A challenger win requires an incremental decision-path improvement over the direct-answer baseline. Merely naming the same idea more elegantly does not count.

Ratings:
- `MATERIAL_WIN` — changes what is investigated/built/spent or changes ordering enough to plausibly avoid material work.
- `PARTIAL_DELTA` — adds a useful distinction but baseline already reaches much of the same action.
- `NO_INCREMENTAL_DELTA` — mostly explanation/wording improvement.
- `CORRECT_NO_REFRAME` — challenger correctly preserves a bounded question.
- `HARM` — challenger adds unnecessary delay/abstraction or changes owner intent.

---

| Case | Challenger disposition | Comparative result | Why |
|---|---|---|---|
| NP-01 Vercel | REFRAME | `PARTIAL_DELTA` | Baseline already checks platform compatibility and can choose another host; challenger improves ordering by selecting target from runtime requirements before Vercel-specific work, but the baseline is not blindly committed. |
| NP-02 Sheet | REFRAME | `MATERIAL_WIN` | Baseline builds the Sheet as source of truth; challenger first decides authority/state semantics and permits Sheet as projection. This changes architecture and can avoid automating around an inadequate store. |
| NP-03 research ROI | REFRAME | `MATERIAL_WIN` | Baseline optimizes the research program; challenger makes research compete with repo inspection, field observation, reversible action, waiting and stopping. The resource class itself changes. |
| NP-04 Lichess history | REFRAME | `MATERIAL_WIN` | Baseline exports/analyzes because the data source is promising; challenger requires a named unresolved claim and smallest sufficient sample before export/engine work. Material analysis can be avoided. |
| NP-05 API key | NO_REFRAME | `CORRECT_NO_REFRAME` | Both answer the bounded feasibility dependency directly. A strategic reframe would be friction. |
| NP-06 marketing assets | REFRAME | `MATERIAL_WIN` | Baseline creates a prioritized asset inventory; challenger ties creation to the next blocked customer decision and builds only the first missing artifact. Changes scope from completeness to bottleneck removal. |
| NP-07 Instagram videos | REFRAME_WITHIN_OWNER_INTENT | `PARTIAL_DELTA` | Challenger reframes topics into audience-state transitions, but baseline already proposes a sequence from problem→proof/trust→CTA. Useful improvement, not clear avoided-work evidence. |
| NP-08 domain | NO_REFRAME | `CORRECT_NO_REFRAME` | Domain attachment is bounded, cheap and purpose-clear once deployment exists. Challenger does not reopen platform strategy. |
| NP-09 maintenance | NO_REFRAME | `CORRECT_NO_REFRAME` | Pure conceptual question; no decision-grade reframe is justified. |
| NP-10 MECE layers | REFRAME | `MATERIAL_WIN` | Baseline notices overlap and cross-cutting concerns but remains inside the three-layer taxonomy. Challenger first chooses one decomposition axis and supplies a falsification test, preventing arbitrary category proliferation. |

## Aggregate

Across 10 natural historical prompts:

- `MATERIAL_WIN`: **5/10**
- `PARTIAL_DELTA`: **2/10**
- `CORRECT_NO_REFRAME`: **3/10**
- `NO_INCREMENTAL_DELTA`: **0/10**
- `HARM`: **0/10**

Among the 7 cases where challenger fired:

- material incremental delta over baseline: **5/7**
- partial incremental delta: **2/7**
- clear harm: **0/7**

Among 3 non-fire cases:

- correct no-reframe: **3/3**

## Strongest evidence for the problem definition

The strongest wins are not cases where the user was vague. They are cases where the question was already concrete and answerable but embedded an object that could absorb resources prematurely:

1. `Sheet` as source of truth before state-authority requirements;
2. `research program` before research competes with cheaper resource moves;
3. `personal Lichess history` before a named unresolved claim requires it;
4. `marketing asset inventory` before a blocked customer decision requires an asset;
5. `product / engineering / operations` before the decomposition axis itself is justified.

The candidate problem therefore remains better described as:

> **Downstream question commitment: resources are about to be allocated to an answerable question that has already fixed a mechanism, object, resource class or decomposition before the uncertainty controlling the decision has been resolved.**

This is narrower and more falsifiable than “users do not know the right question.”

## What the baseline comparison changes

The synthetic v0 run made Question Discovery look nearly universally strong. The natural-prompt baseline comparison weakens that claim in a useful way:

- a strong direct model often performs some implicit reframing already;
- the challenger advantage is largest when the **unit of investment itself** is premature (store, research, dataset, asset inventory, taxonomy);
- the advantage is smaller when ordinary reasoning already checks compatibility or already structures a funnel/sequence;
- therefore the product cannot be justified as “better questions in general.”

## Best current fire condition

Question Discovery should fire when all of the following are plausible:

1. a consequential decision/resource allocation is present;
2. the current question names a mechanism/tool/resource/decomposition/metric as though it were already the right object;
3. an upstream uncertainty could make work on that object unnecessary or materially different;
4. that uncertainty can be checked more cheaply than fully answering/executing the current question.

Otherwise prefer `NO_REFRAME` or ordinary direct reasoning.

## Evidence ceiling

This run still does not establish independent product value because:

- prompts are historical but the evaluator knows later context;
- baseline, challenger and adjudication are the same model/research context;
- no blinded external judge scored the outputs;
- no prospective user outcome or actual avoided cost is measured.

The next evidential upgrade should be prospective and blinded: new natural prompts captured before answer, baseline and challenger outputs randomized, independent judgment on decision delta/avoided work/over-reframing, followed where possible by the user's actual next action.