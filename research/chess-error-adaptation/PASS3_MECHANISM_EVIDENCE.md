# Chess Error Adaptation — Pass 3: Mechanism Evidence

Status: `R&D_EXECUTION_PASS_3_COMPLETE`
Date: 2026-09-05
Task: `CAL-CHESS-ERROR-001`

## R&D question entering the pass

Which candidate error/mechanism labels can be supported from observable game/board/context data, and which inherently require an additional cognitive discriminator or player report?

## Neta challenge before execution

The main proxy risk is:

> `observable chess event → psychological explanation`

A fork on the board, a 150-centipawn loss, a shallow tactical refutation, or a rare Maia move are observations/model outputs. None is automatically evidence that the player `failed to see`, `failed to calculate`, `did not know`, `panicked`, or `mis-evaluated`.

The pass therefore builds an **evidence ladder**, not a flat taxonomy.

---

# P3.1 Four levels of error claims

## Level 1 — `OBSERVED_ERROR_FORM`

Directly supported by board/game/engine/context data.

Examples:

- illegal move / rules violation;
- move causes material loss within N plies;
- move permits mate / loses forced mate;
- move misses a machine-detectable fork, pin, skewer, discovered attack, back-rank motif, promotion tactic, etc.;
- played move has low probability under a skill-conditioned human model;
- error occurs under severe time pressure;
- opening departure occurs earlier than a matched skill cohort;
- endgame conversion is lost from an engine-winning state;
- a move crosses a prespecified WDL/Win%-loss threshold.

Authority: `REPO/ENGINE/DATA` depending on instrument.

These labels describe **what happened**, not why.

---

## Level 2 — `STATISTICAL_WEAKNESS`

Supported when a player repeatedly underperforms a defined opportunity denominator relative to a relevant cohort or their own baseline.

Minimum structure:

```text
feature_or_context
opportunities
errors_or_misses
player_rate
cohort_expected_rate
sample_n
uncertainty
heldout_stability
```

Examples:

- misses knight-fork opportunities materially more often than skill/time-control peers;
- loses winning rook endings more often than matched peers after controlling for engine advantage and time pressure;
- unusually high error rate immediately after a prior blunder;
- unusually high human-surprisal moves in a recurring pawn structure.

### Critical denominator rule

`number of errors` is insufficient.

A player who misses 8 forks out of 200 opportunities is not equivalent to a player who misses 8 out of 12.

### Authority ceiling

A statistical weakness supports:

> "This player underperforms their comparison baseline in this observable class."

It does not yet support a unique cognitive cause.

---

## Level 3 — `COGNITIVE_MECHANISM_HYPOTHESIS`

Candidate explanations generated because they could produce the observed pattern.

Examples:

- perceptual/cue-selection failure;
- candidate-generation failure;
- calculation/search failure;
- verification failure;
- position-evaluation / strategic-judgment failure;
- missing domain/opening/endgame knowledge;
- fixation / Einstellung on a familiar candidate;
- time-allocation failure;
- rules/procedural knowledge gap;
- attention/disengagement state.

These are hypotheses until a discriminator rules among plausible neighbors.

---

## Level 4 — `MECHANISM_SUPPORTED / CONFIRMED_FOR_USE`

Requires evidence beyond the outcome move itself.

Possible discriminators include:

- think-aloud / retrospective protocol with reactivity controls;
- candidate-move elicitation after natural search is complete;
- controlled positions that isolate one knowledge/motif variable;
- eye tracking / gaze data for perceptual-attention questions;
- repeated within-player contrast under time/no-time pressure;
- opening/familiarity manipulation;
- response to a targeted hint or probe;
- direct rules/knowledge task;
- prospective intervention and recurrence change.

The exact evidence required depends on the mechanism claim.

---

# P3.2 Why search depth cannot be inferred from a bad move

The chess-expertise literature does not support a simple monotonic rule that stronger players merely calculate more deeply.

Evidence families disagree in magnitude and task conditions:

- some complex-position studies find stronger players search more/deeper/faster;
- other analyses find little or no master-vs-intermediate difference in average/max depth and emphasize pattern recognition/evaluation;
- specialization changes search strategy within the same general-skill player;
- elite time-pressure work shows experts adaptively combine fast recognition and deliberation.

### Surviving claim

> `calculation depth` is a measurable candidate mechanism, not an outcome label.

A move refuted by a two-ply engine line supports:

> "a shallow tactical consequence existed."

It does **not** establish:

> "the player only calculated one ply."

### Instrument implication

If calculation process matters to the product, measure it with a dedicated protocol or infer it probabilistically from multiple discriminators; never derive it directly from Stockfish PV length.

---

# P3.3 Perception/cue selection is a distinct mechanism family

Eye-movement studies of expert vs novice players show experts detect task-relevant regions earlier and allocate gaze differently. Classic expertise work also supports rapid pattern/chunk recognition as a major skill component.

### Surviving claim

A player can fail before explicit calculation begins because the relevant cue/candidate does not enter the active problem representation.

### Product boundary

Board-concept presence can create a **perception hypothesis** when a motif is repeatedly missed, but without gaze/protocol/controlled-task evidence it cannot determine whether the motif was unnoticed, noticed but rejected, or calculated incorrectly.

---

# P3.4 Candidate generation is distinct from calculation

A player may fail because the correct move never enters the candidate set, even if they calculate chosen candidates accurately.

Einstellung research in chess shows familiar solution patterns can block discovery of a superior alternative, including among experts.

### Candidate discriminator

After a natural decision has been recorded, ask for the serious alternatives the player considered, or use a retrospective reconstruction that does not alter the original decision.

If the best move was never a candidate, `candidate-generation failure` gains support.
If it was considered but rejected, another mechanism is required.

### Reactivity warning

Do not ask "did you consider X?" before the move when measuring natural candidate generation; that question itself can introduce X.

---

# P3.5 Knowledge/specialization is not reducible to global rating

Opening-knowledge and specialization studies show substantial domain-specific effects. Players of similar general strength can perform around the level of materially stronger players inside their area of specialization, and alter their search behavior according to familiarity.

### Surviving claim

A player-specific model should eventually allow local priors such as:

- opening family / pawn structure;
- tactical motif exposure;
- endgame class;
- familiar vs unfamiliar position family.

### Denied inference

Do not label an unfamiliar-position failure as a `knowledge gap` unless opportunity/exposure or a direct knowledge test supports it.

---

# P3.6 Rules/procedural errors are one of the rare high-authority mechanism families at very low skill

A 2026 Spanish doctoral study of chess initiation built observational instruments for illegal and erroneous moves. It identified distinct illegal-move types and, in very young competitive beginners, found decisive errors associated more with short-horizon tactical motifs, undefended pieces and mating errors than strategic planning.

### Why this matters

At the earliest skill stages, some error forms can legitimately support stronger interpretations because the rules themselves define the competence being tested.

Example:

`king moved into check` can support a rules/procedural-knowledge or rule-application problem much more directly than `missed fork` supports a perceptual mechanism.

### Boundary

Child beginner findings do not generalize to adult 1600 online players.

---

# P3.7 Time allocation is a mechanism candidate with direct behavioral observables

Time use is observable when clock data exist. Elite and large-scale studies show time pressure affects blunder propensity even at very high skill, and experts strategically allocate deliberation time.

### Supported labels

- `error_under_high_relative_time_pressure`;
- `unusually_fast_decision_for_position/context` when a cohort/time model exists;
- `post-error_slowing` / `post-error_accuracy_drop` at aggregate/player level.

### Hypotheses, not direct facts

- panic;
- impulsivity;
- lack of confidence;
- tilt.

These require additional evidence.

---

# P3.8 Mechanism graph rather than one cause field

A single move may be compatible with multiple mechanisms.

Recommended representation:

```text
error_event
  ├─ observed_forms[]
  ├─ context[]
  ├─ statistical_weakness_links[]
  └─ mechanism_hypotheses[]
        ├─ evidence_for[]
        ├─ evidence_against[]
        ├─ discriminator
        └─ state: OPEN | SUPPORTED | REFUTED | INCONCLUSIVE
```

Do not force mutually exclusive classification before evidence earns it.

---

# P3.9 Candidate error families safe for automatic labeling

These are **event/form families**, not psych diagnoses:

1. `RULES / LEGALITY`
2. `MATERIAL HANG / IMMEDIATE TACTICAL CONSEQUENCE`
3. `MATE / KING-SAFETY CONSEQUENCE`
4. `MISSED TACTICAL OPPORTUNITY` with machine-readable motif
5. `NON-IMMEDIATE EVALUATION LOSS`
6. `OPENING / KNOWN-SEQUENCE DEPARTURE`
7. `ENDGAME CONVERSION / TECHNIQUE EVENT`
8. `TIME-PRESSURE ASSOCIATED ERROR`
9. `POST-ERROR ASSOCIATED ERROR`
10. `HUMAN-SURPRISING MOVE AT SKILL LEVEL`
11. `PLAYER-SPECIFIC RECURRENT DEVIATION`

Each must retain its operational definition and opportunity denominator.

---

# P3.10 Labels that must not be automatically asserted from game data alone

- `did not see the tactic`
- `calculated too shallowly`
- `failed to generate candidates`
- `mis-evaluated the position`
- `does not understand strategy`
- `lacks endgame knowledge`
- `was tilted`
- `was overconfident`
- `played automatically`
- `did not understand the opening`

These are permissible **candidate mechanisms**, not automatic verdicts.

---

# Decision after Pass 3

The mechanism boundary is sufficiently stable for implementation.

The product should not attempt a one-label cognitive classifier from PGN + engine data.

Instead it should maintain:

```text
OBSERVED FORM
→ OPPORTUNITY-NORMALIZED PLAYER DEVIATION
→ CANDIDATE MECHANISMS
→ CHEAP DISCRIMINATOR WHEN THE MECHANISM MATTERS
```

## Next material uncertainty selected by R&D

The descriptive/diagnostic architecture is now coherent enough that the largest remaining value question is pedagogical:

> Given an evidence-bounded weakness state, which intervention should be selected, when should it appear, and what outcome should count as learning?

This becomes Pass 4.
