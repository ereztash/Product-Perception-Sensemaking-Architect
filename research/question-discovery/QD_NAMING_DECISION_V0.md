# Question-Selection Capability — Naming Decision v0

Status: `NAMING_DECISION_CANDIDATE · REPO-GROUNDED · NOT_MARKET_VALIDATED · NOT_YET_CANONICAL`
Date: 2026-09-06

## Decision being made

Choose the most precise positive name for the capability currently called `Question Discovery`, using the evidence already deposited in this repository.

The name must describe the successful function without defining the product by the failure it prevents.

## Recovered positive telos

The capability is not primarily:
- preventing bad questions;
- detecting mistakes;
- guarding against premature framing;
- making questions sound smarter;
- always producing a new question.

The positive transformation supported by current evidence is:

```text
CURRENT QUESTION + DECISION CONTEXT
→ identify the decision actually being served
→ surface candidate question framings when needed
→ compare which unresolved question can most materially change the decision
→ SELECT THE QUESTION TO RESOLVE NOW
→ preserve the current question when it already wins
→ identify the cheapest admissible way to resolve it
```

Positive telos candidate:

> **Select the question whose resolution is most decision-relevant now, given the current decision, evidence and cost of learning.**

This wording deliberately avoids claiming mathematically optimal or globally maximal value.

## Naming constraints derived from evidence

A valid name should satisfy all of the following:

1. **Positive function** — describe what the capability enables, not the failure it prevents.
2. **Decision anchor** — distinguish it from generic curiosity, brainstorming, coaching or clarification.
3. **Question as unit** — the selected object is the question to resolve next.
4. **NO_REFRAME compatible** — the current question may remain the selected question.
5. **No unsupported optimality claim** — current evidence does not justify `best`, `optimal`, `highest-value` as a measured property.
6. **No forced novelty** — a name should not imply that a new question must always be discovered/generated.
7. **No mechanism lock-in** — avoid naming the capability after `guard`, `check`, `reframe` or another implementation detail.
8. **Cross-domain** — must fit architecture, research, marketing, data, tooling, learning and other consequential decisions.
9. **Distinct from R&D** — R&D allocates resources toward telos; this capability selects which question should control the next information/decision step.
10. **Distinct from Neta** — Neta discriminates product/design meanings; this capability can operate on any decision domain.

## Candidate comparison

Scale: `0 = poor`, `1 = acceptable`, `2 = strong`.

| Candidate | Positive | Decision anchor | NO_REFRAME | No overclaim | Cross-domain | Functional precision | Total /12 | Disposition |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `Question Discovery` | 2 | 0 | 1 | 2 | 2 | 1 | 8 | too broad; implies novelty |
| `Decision Question Discovery` | 2 | 2 | 1 | 2 | 2 | 1 | 10 | strong but still implies a question must be discovered |
| `Decision Question Selection` | 2 | 2 | 2 | 2 | 2 | 2 | **12** | **winner** |
| `Decision Question Prioritization` | 2 | 2 | 2 | 2 | 2 | 1 | 11 | suggests ranking an existing backlog rather than deriving a better framing |
| `Decision Framing` | 2 | 2 | 2 | 2 | 2 | 0 | 10 | too broad; could include options, narratives, criteria, not specifically questions |
| `Highest-Leverage Question` | 2 | 2 | 2 | 0 | 2 | 1 | 9 | excellent promise/output phrase; unsupported superlative as capability name |
| `Highest-Value Question` | 2 | 2 | 2 | 0 | 2 | 1 | 9 | same overclaim; `value` is ambiguous |
| `Question Leverage` | 2 | 1 | 2 | 1 | 2 | 0 | 8 | brandable but not self-describing |
| `Decision Dependency Check` | 0 | 2 | 2 | 2 | 2 | 1 | 9 | negative/mechanistic; names one internal step |
| `Decision Framing Guard` | 0 | 2 | 2 | 2 | 2 | 1 | 9 | prevention framing, not positive telos |

## Why `Decision Question Selection` wins

### 1. It describes the actual decision the capability makes

The capability itself makes a bounded meta-decision:

> **Which question should govern the next learning/decision step?**

That is selection.

### 2. It handles both reframe and no-reframe

`Discovery` subtly biases toward novelty.

`Selection` permits:

```text
candidate A = the user's current question
candidate B = upstream question
candidate C = neighboring framing

SELECT A
```

This matches the natural-prompt controls where API-key feasibility, domain attachment and maintenance explanation should remain as asked.

### 3. It stays positive

It does not define the user as mistaken and does not define the capability as a guard against waste.

Its successful act is choosing the question to resolve.

### 4. It does not claim an unmeasured optimum

The current repository can support `decision-relevant`, `material decision delta`, `cheapest admissible discriminator` and `selection under current evidence`.

It cannot yet support a literal claim that the chosen question is globally the `highest-value`, `optimal`, or `highest-leverage` question among all possible questions.

Therefore those phrases belong in positioning hypotheses, not the canonical capability name.

### 5. It fits the ecosystem boundary

Current conceptual decomposition:

```text
Decision Question Selection
→ WHICH QUESTION should control the next learning step?

R&D
→ WHICH RESOURCE / LEARNING MOVE should be used to resolve the live decision question?

Neta
→ WHAT PRODUCT/DESIGN INTERPRETATION best fits a product signal?

Architecture Decision capability
→ WHICH SYSTEM STRUCTURE best fits accepted drivers/constraints?
```

This is a cleaner orthogonal boundary than `Question Discovery`, which can sound like generic research-question generation and collide with R&D.

## Exact recommended naming stack

### Capability name — recommended

> **Decision Question Selection**

Abbreviation: `DQS`.

### Capability telos — recommended

> **Select the question to resolve now whose answer can most materially improve the current decision, given available evidence, authority and cost of learning.**

### User-facing promise — candidate, not canonical

> **Find the highest-leverage question to answer next.**

This is useful language for explaining the benefit, but `highest-leverage` should remain a positioning hypothesis until comparative/prospective evidence supports the superlative.

### Plain-language Hebrew description

> **לבחור איזו שאלה הכי כדאי להכריע עכשיו כדי לדעת טוב יותר מה לעשות אחר כך.**

A stricter non-superlative version:

> **לבחור את השאלה שהכרעה בה צפויה לשנות באופן המהותי ביותר את ההחלטה הבאה, ביחס למה שידוע כרגע.**

## Names explicitly rejected as canonical capability names

### `Question Discovery`
Useful historical working name. Too broad and novelty-biased.

### `The Question Before the Question`
Memorable framing, but structurally wrong for `NO_REFRAME`; there is not always another question before the current one.

### `Highest-Leverage Question`
Strong output/marketing phrase, not a safe capability name yet.

### `Decision Framing Guard`
Accurate failure-prevention mechanism, but violates the requested positive framing and names prevention rather than value creation.

### `Decision Question Optimizer`
Implies an objective function and measurable optimum that do not yet exist.

## Current decision

`SELECT_CANDIDATE_NAME = Decision Question Selection`

Confidence form: **repo-supported naming decision, not market validation**.

The name should be promoted to canonical only after a small neighboring-name test confirms that users understand it as `which question should I resolve next for this decision?` rather than `choose wording for a question`.

## Cheapest reversal test

Present only the capability name + one-line description for these three names, randomized:

1. `Decision Question Selection`
2. `Decision Question Discovery`
3. `Highest-Leverage Question`

Ask independent users what they expect the tool to do before showing examples.

Reversal condition:
- if `Decision Question Selection` is consistently interpreted as copy-editing/choosing among already-written questions while another candidate correctly evokes upstream decision-question identification without overpromising, revisit the name.
- otherwise retain `Decision Question Selection` as the canonical capability candidate.
