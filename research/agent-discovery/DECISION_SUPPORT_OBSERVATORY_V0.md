# Decision Support Observatory v0

Status: `FROZEN_OBSERVATORY · CANDIDATE_CROSS_CUTTING_RESIDUAL · NOT_AGENT`
Date: 2026-09-06

## Why this observatory exists

Agent Discovery Pass 1 found a plausible gap **after** product/domain sensemaking and **after** epistemic allocation:

> When the decision maker's priorities/constraints are already explicit, feasible alternatives exist, and current evidence is bounded enough to compare them, does the ecosystem still lack a reusable judgment method for making tradeoffs and ranking robustness legible before OWNER commitment?

This is not yet a proven gap.

## Candidate function

```text
OWNER PRIORITIES / MANDATORY CONSTRAINTS
+ FEASIBLE ALTERNATIVES
+ CURRENT BOUNDED EVIDENCE
→ DECISION CRITERIA
→ CONSEQUENCES / TRADEOFFS
→ RANKING ROBUSTNESS
→ RECOMMENDATION OR CLOSE SET
→ OWNER COMMITMENT
```

The capability may recommend. It never becomes the final authority for owner values, preferences, accepted risk or commitment.

## Orthogonal boundary hypothesis

### Neta
Owns product signal → mechanism → discriminator → evidence-bounded intervention.

### R&D
Owns the meta-decision whether/how/how much further learning/evidence acquisition is worth buying.

### Domain method
Owns specialized judgments such as architecture structure, debugging mechanism, finance/legal/security analysis.

### Decision Support candidate
Would own only the **cross-domain comparison of already-admissible alternatives against explicit decision-maker criteria**, including whether the ranking is robust enough to commit.

Boundary handoff:

```text
DECISION SUPPORT
→ if ranking is sensitive to unresolved uncertainty:
     R&D decides whether that uncertainty is worth reducing
→ if one alternative requires domain-specific judgment:
     domain method resolves that object
→ if values/criteria are missing or contested:
     OWNER
→ if ranking is robust enough:
     OWNER commits
```

## Admission criteria

A natural case is admissible only when all are observable **before candidate output**:

1. consequential decision;
2. at least two feasible alternatives;
3. owner priorities, objectives or mandatory constraints are explicit enough to evaluate options;
4. the core problem is not merely missing OWNER intent;
5. no single direct authority fact settles the choice;
6. there is no obvious cheap discriminator that should be run first;
7. the central unresolved object is not ordinary domain diagnosis;
8. the case asks for comparison, recommendation, prioritization or commitment.

## Exclusions

### OWNER_INTENT_MISSING
If the owner has not said what matters, route to OWNER. Do not fabricate criteria/weights.

Examples already observed:
- Actual Budget confirmation vs undo policy;
- SparkleShare legacy TODO vs current product direction;
- Organic Maps confirmation/recovery policy;
- SiYuan explicit no-confirm option.

These are not positive Decision Support evidence.

### EPISTEMIC_ALLOCATION_PRIMARY
If more evidence could materially change which option is admissible/ranked and the main decision is what evidence to buy, route to R&D.

### DOMAIN_METHOD_PRIMARY
If the choice is primarily structural architecture, product mechanism/intervention, debugging, legal, finance, security, etc., use that method first. Domain outputs may later become inputs to Decision Support.

### DOMINATED_OPTION
If a mandatory criterion eliminates all but one option, do not manufacture a trade study.

### LOW_LOCAL
Do not invoke formal decision support for cheap, reversible local choices.

## Initial natural signal

One historical Lichess decision is a plausible positive case:

- alternatives: direct route after reveal vs route through record;
- both options already built/measured;
- criteria included interaction presses/friction, experimental denominator/comparability, RNL-11 instrument/intervention integrity, and interpretation risk;
- output compared consequences and recommended keeping the current record route while preserving OWNER commitment authority.

This is **one case only** and sits on a Neta×R&D boundary, so it cannot establish an independent capability.

A previous Agent Architect case (outreach test vs more productization) is not clean positive evidence because the selected outreach move was itself an evidence-generating test under partial uncertainty; R&D/question-discovery could own much of that judgment.

## Candidate contract to test — not yet promoted

### TELOS
Make the choice among currently admissible alternatives decision-legible without laundering missing owner values, missing evidence or domain judgments into a generic score.

### INPUT
- decision statement;
- explicit owner priorities/mandatory constraints;
- alternatives;
- domain outputs/evidence already available;
- uncertainties and authority labels;
- implementation cost/reversibility where material.

### EXACT JUDGMENT
Which alternatives remain admissible, how do they trade off against owner criteria, how robust is the ranking to bounded uncertainty, and is the state ready for OWNER commitment or another handoff?

### OUTPUT
```text
decision
mandatory_criteria[]
preference_criteria[]
alternatives[]
consequence_matrix
non_compensatory_failures[]
tradeoffs[]
ranking_or_close_set
ranking_sensitivity[]
uncertainty_that_could_flip_choice[]
next_authority
recommendation
owner_commitment_needed
```

### FIRE
Explicit values/constraints + viable alternatives + bounded evidence + nontrivial cross-criterion tradeoff.

### NO_FIRE
Missing owner values, evidence-acquisition decision, domain-method decision, direct authority, dominated option, obvious cheap test, low/local choice.

### AUTHORITY CEILING
OWNER retains values, accepted risk and final commitment.

## Comparator

Primary:

```text
A = Neta + R&D + relevant domain method/Scaffold + OWNER constraints
B = A + minimal Decision Support contract
```

Do **not** compare against a weakened generic answer.

## Win condition

A candidate win requires one of:
- materially different option set because a false alternative is exposed;
- material criterion/constraint the baseline misses;
- materially better tradeoff representation that changes OWNER choice;
- detection that ranking is non-robust and correct handoff to R&D;
- prevention of a weighted-score artifact / double-counting / compensation across mandatory constraints;
- reduction in later reversal/regret attributable to a missed decision criterion, where outcome is observable.

Better tables or more polished explanation do not count.

## Loss / overfire

Count a loss when the candidate:
- invents owner values/weights;
- converts value judgments into fake precision;
- reopens evidence gathering with no decision value;
- replaces a domain method;
- delays an obvious decision;
- recommends a dominated option because of score aggregation;
- hides uncertainty behind a ranking.

## Discovery target

Collect 15–25 natural historical/prospective cases across at least four domains.

The corpus must include:
- positive-looking post-information choices;
- missing-OWNER controls;
- R&D-primary controls;
- domain-method controls;
- dominated/obvious-choice controls.

Do not design a persistent peer before this corpus shows recurring material delta.

## Promotion path

```text
OBSERVATORY
→ recurring residual family
→ minimal Decision Support capability
→ baseline/challenger
→ external/prospective outcome
→ form-factor test
→ only then peer eligibility
```

Current disposition:

`DECISION_SUPPORT_AGENT = NOT_EARNED`

`DECISION_SUPPORT_CAPABILITY = PLAUSIBLE_OPEN_CHALLENGER`
