# Chess Error Adaptation — R&D + Neta Research Plan v0

Status: `PLAN_EARNED_BY_MANUAL_PEER_PASSES`
Date: 2026-09-05
Task: `CAL-CHESS-ERROR-001`

## Decision this research must support

Design a defensible knowledge model for adapting chess-error diagnosis to player skill while preserving the possibility that rating is only one useful conditioning variable.

The first research program is **descriptive/explanatory**, not yet a claim about which feedback causes improvement.

## Neta challenge that changed the plan

The initial phrase `errors by rating` risks several proxy collapses:

- rating ≠ complete skill profile;
- centipawn loss ≠ pedagogically useful error type;
- frequency by rating ≠ cognitive mechanism;
- human move likelihood ≠ move quality;
- aggregate cohort behavior ≠ an individual's recurring weakness;
- engine evaluation ≠ what a player can realistically perceive or execute;
- translated/multilingual repetition ≠ independent evidence;
- coaching doctrine ≠ empirical prevalence;
- error detection ≠ learning impact.

Therefore the research must preserve distinct objects instead of producing one Elo→mistake lookup table.

## R&D research objects

### 1. ERROR_EVENT
Observed move/position event with objective chess consequences and context.
Candidate fields include move quality/evaluation delta, tactical/strategic context, phase, time state, material state and resulting position.

### 2. SKILL_CONDITIONED_PRIOR
What moves/errors are more or less common/predictable at a given rating/skill range, under a named rating system and time control.

### 3. ERROR_MECHANISM_HYPOTHESIS
A candidate explanation for the error: missed cue, candidate-generation failure, calculation failure, evaluation failure, tactical motif blindness, strategic misconception, endgame technique, time-management effect, post-error disruption, etc.

Mechanism is not inferred from centipawn loss alone.

### 4. PLAYER_SPECIFIC_DEVIATION
How an individual differs from the rating-conditioned population prior.

### 5. PEDAGOGICAL_ACTION
What feedback/training is useful for this player now.

This requires a stronger evidence layer than mere error prevalence/prediction. Keep it separate until learning/outcome evidence is collected.

## Research questions

### Q1 — Distribution
How do error frequency, severity and broad error forms change with rating/skill?

### Q2 — Human predictability
Can skill-conditioned human models predict the mistakes/choices players at different levels actually make better than attenuated optimal engines?

### Q3 — Mechanism
What empirically studied cognitive mechanisms distinguish stronger from weaker chess decisions and explain errors beyond raw engine loss?

### Q4 — Individualization
How much information does player-specific history add beyond rating-conditioned population models?

### Q5 — Context
How do time control, move time, game phase, position complexity and prior errors change the distribution/meaning of mistakes?

### Q6 — Pedagogy (separate lane)
Which forms of diagnosis/feedback/training improve later decisions for players at different skill levels?

Do not answer Q6 merely from Q1–Q5.

## Source strategy

Priority is by evidential function, not language.

1. Peer-reviewed / strong empirical studies — mechanism, distributions, expertise effects.
2. Open datasets and executable models — operationalization and reproducibility.
3. Books and trainer literature — candidate taxonomies and pedagogical hypotheses.
4. Theses / local-language academic literature — context-specific mechanisms or methods absent from the dominant English corpus.
5. Community/coaching content — hypothesis discovery only unless independently validated.

## Multilingual strategy

Search languages are selected because they may expose different source ecosystems, not to hit a quota.

Initial lanes earned by source yield:

- English: empirical cognitive-science, ML, large-scale data, Maia lineage.
- Russian: long coaching/pedagogical tradition and explicit error taxonomies; treat primarily as taxonomy/pedagogy unless empirical design supports stronger use.
- French: chess-expertise/cognitive-psychology literature and reviews.
- Chinese: novice→expert / educational expertise literature; continue only if chess-specific material yields a new distinction.
- Spanish: coaching/error taxonomies and level-specific claims; quarantine as doctrine unless data are supplied.

Other languages are added only when they are likely to expose a new evidence family or distinction.

## Required source record

For every source preserve:

- title / author / year;
- language;
- source type;
- research question(s) served;
- exact claim supported;
- population + rating system + time control where relevant;
- operational definition of error;
- evidence family / lineage;
- limitations / counterevidence;
- product-use ceiling.

## Promotion rules

- A rating correlation does not establish a cognitive mechanism.
- A coach's taxonomy can become a candidate label, not a prevalence fact.
- Maia-style move prediction can establish skill-conditioned human likelihood, not pedagogical efficacy.
- Stockfish CPL can establish engine-defined value loss under a specified analysis setup, not the user's reason for the error.
- Individual-model gains establish residual player-specific structure beyond cohort priors; they do not prove the optimal intervention.
- Different-language sources citing the same foundational work count as shared lineage.

## Stop rules

Stop a source lane when two consecutive passes add no new distinction, boundary, contradiction, operationalization or dataset.

Stop the descriptive program when remaining material uncertainty is pedagogical FIELD/outcome evidence rather than error modeling.
