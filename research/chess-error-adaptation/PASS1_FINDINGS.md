# Chess Error Adaptation — Pass 1 Findings

Status: `R&D_EXECUTION_PASS_1`
Date: 2026-09-05
Task: `CAL-CHESS-ERROR-001`

This pass was planned after a role-separated R&D diagnosis and Neta challenge. It is not a generic bibliography sweep.

## Bottom line

The first pass rejects a simple model of:

`Elo band → typical mistake list → prescribed lesson`

The strongest evidence supports a richer structure:

```text
position/context
+ rating-conditioned human prior
+ objective move consequence
+ error-type/mechanism hypothesis
+ individual deviation
+ time/history context
→ diagnosis candidate
```

Pedagogical action remains a separate evidence problem.

---

## F1 — Skill-conditioned human move distributions are real and modelable

### Evidence

The Maia lineage (Maia 1 → Maia-2 → Maia-3) models human moves as a function of skill rather than attenuating a superhuman engine.

- Maia 1 showed separate rating-targeted models predict moves best near their target rating.
- Maia-2 unifies skill levels inside one skill-aware model and is explicitly intended to model improvement trajectories.
- Maia-3 (ICLR 2026 / Chessformer) continues rating-conditioned human move prediction and exposes Elo as a UCI conditioning parameter.

### Surviving claim

> Rating/skill contains real information about the distribution of human candidate moves and mistakes in a position.

### Does not establish

- that Elo defines a player's weakness profile;
- why a move was made;
- which feedback will improve the player;
- that a Lichess rating transfers directly to FIDE/Chess.com or another time control.

### Product implication candidate

Use rating as a **prior over human move likelihood**, not as a deterministic error label.

---

## F2 — Individual history contains material information beyond rating

### Evidence

The KDD work on individual Maia models reports material gains when models are adapted to individual players and shows that models capture identifiable personal decision style, including blunder style.

A 2026 Applied Intelligence blunder-prediction study reports that a learned latent user/blunder profile predicts errors better than Elo alone; in its ablation, user identity materially improves AUC/AUC-PR, while adding coarse Elo to a user-specific representation can even reduce performance.

### Surviving claim

> Two equally rated players can have meaningfully different error profiles; rating should be a cohort prior, then updated by player-specific evidence.

### Product implication candidate

Model:

`rating-conditioned prior → observed player deviations → personalized weakness profile`

rather than assigning all 1600 players the same taxonomy weights.

---

## F3 — The distribution of error forms changes with skill

### Evidence

The 2026 Applied Intelligence study operationalizes blunders as moves causing at least a 10% drop in winning probability and separates:

- `immediate` blunders — consequences become clear on the opponent's immediate response / immediate material consequence;
- `non-immediate` blunders — consequences materialize later.

Across five Elo bins (630–2390), immediate blunders become scarcer as rating rises; the authors interpret the remaining high-Elo errors as increasingly non-immediate/strategic and harder to predict.

### Surviving claim

> A single universal blunder type is inadequate across skill levels; the composition of observed errors changes with skill.

### Boundary

`immediate = tactical` and `non-immediate = strategic` is an operational simplification, not a complete cognitive taxonomy.

The categorization is based on consequence timing/material realization, not direct observation of the player's thought process.

---

## F4 — Error meaning depends on context, not rating alone

### Evidence

Multiple studies show material context effects:

- time pressure changes move quality and the predictive role of chess skill;
- a 2026 Scientific Reports study on elite blitz finds nonlinear interaction between low remaining time and positional ambiguity;
- 2026 work on post-error behavior over more than one million games reports post-error slowing plus subsequent accuracy impairment, moderated by player ability and error severity;
- game phase changes blunder prevalence/prediction characteristics in the Applied Intelligence dataset.

### Surviving claim

> An adaptive error model should condition on context such as time control/time remaining, game phase, position difficulty/ambiguity and recent error history where available.

### Product implication candidate

The same move-loss at 1600 blitz with 3 seconds left and at 1600 classical with 20 minutes left should not automatically receive the same diagnosis.

---

## F5 — Engine loss is consequence evidence, not mechanism evidence

### Evidence

Saariluoma's protocol-analysis work on chess error argues that errors are only partly explained by generic working-memory overload. Failures can arise from selecting the wrong problem representation or missing a crucial task-relevant cue.

Studies of chess expertise and intuition also show Elo relates to evaluation accuracy, but do not reduce expertise to one scalar error mechanism.

### Surviving claim

> CPL / win-probability loss can tell us that a decision was costly under an engine model; it cannot by itself tell us whether the human failure was candidate generation, tactical perception, calculation, evaluation, strategic knowledge, endgame knowledge, time management, or another mechanism.

### Product implication candidate

Mechanism labels require additional discriminators beyond Stockfish delta.

---

## F6 — Russian chess pedagogy offers useful candidate taxonomies, but not prevalence evidence

### Sources discovered

Russian coaching literature explicitly organizes recurring errors into families such as:

- tactical motifs;
- positional errors;
- endgame errors;
- psychological errors;
- recurring strategic/technical difficulties.

Voronkov & Persits, *Типичные ошибки* (1974), explicitly uses examples from players of different classes and says trainers can choose examples appropriate to students' preparation/qualification. Popov's *Шахматы: работа над ошибками* and related Russian training literature similarly center systematic work on characteristic errors.

### Surviving use

These books are valuable for **candidate taxonomy generation and coaching-language recovery**.

### Denied use

They do not, by themselves, establish frequency by Elo, causal mechanism, or learning effect. Some examples are pedagogically selected or even modified to make the error clearer.

---

## F7 — French expertise literature is useful primarily as synthesis/lineage

A French review of cognitive expertise in chess surveys the novice→expert literature since de Groot and reinforces the importance of knowledge structures, recognition and expertise mechanisms.

Useful for mechanism synthesis, but much of its evidence lineage overlaps foundational international chess-cognition work; French language does not make it independent triangulation.

---

## F8 — Chinese-language search produced a useful null in Pass 1

The first Chinese academic search located general novice→expert expertise literature that cites chess as a foundational domain, but did **not** yet surface a strong chess-specific dataset or study mapping error forms across rating levels.

Decision:

> Do not fill a language quota with low-yield sources.

Continue Chinese search only if a later question (e.g. training design, expert-blind-spot, youth chess pedagogy) has a plausible unique evidence family to recover.

---

## F9 — Spanish-language coaching material supplies hypotheses, not evidence-grade rating rules

Current Spanish coaching sources contain level-specific claims (e.g. recurring calculation/planning/tactical habits below a threshold), but the surfaced sources do not provide designs strong enough to promote those claims into prevalence rules.

Use: candidate labels/questions for later dataset tests.

Do not use: hard-coded `under 1400 → error X` rules.

---

## F10 — The largest unresolved gap is pedagogical efficacy

The strongest sources in this pass establish:

- move prediction;
- blunder prediction;
- rating-conditioned behavior;
- player-specific behavior;
- cognitive/contextual correlates;
- candidate error taxonomies.

They do **not yet establish** that presenting a rating-tailored error label or training recommendation causes better subsequent chess decisions or rating improvement.

Therefore:

`DESCRIPTIVE ERROR MODEL` and `PEDAGOGICAL INTERVENTION MODEL` remain separate research lanes.

---

# Candidate model after Pass 1

```text
ERROR EVENT
    |
    +-- engine consequence (CPL / WDL / material / tactical consequence)
    +-- position context (phase / ambiguity / motifs)
    +-- temporal context (time control / time remaining / post-error state)
    +-- skill-conditioned human likelihood (Maia-like prior)
    +-- candidate mechanism taxonomy
    +-- player-specific recurrence/deviation
    |
    v
EVIDENCE-BOUNDED ERROR DIAGNOSIS
    |
    +-- what is typical for cohort?
    +-- what is unusually recurrent for this player?
    +-- what mechanism is supported vs merely plausible?
    +-- what observation would discriminate it?
    |
    v
PEDAGOGICAL ACTION  <-- separate evidence/field lane
```

# What Pass 1 changed

Before:

`adapt mistakes by rating`

After:

> **Use rating to condition the human prior, then combine it with context, consequence, mechanism evidence and player-specific deviation. Do not let rating substitute for the player or CPL substitute for the error mechanism.**

# Next R&D uncertainty

The highest-value next pass is not another broad multilingual sweep. It is to operationalize the candidate dimensions against executable/open data:

1. exact Maia/BlunderPrediction inputs and outputs usable as instruments;
2. rating-system/time-control boundaries;
3. recoverable error taxonomies that can be automatically labeled from board/game data;
4. historical player-level data requirements needed to detect deviation from rating peers;
5. sensitivity of conclusions to the operational definition of `blunder`.

Only after this should the pedagogy/outcome lane be expanded.
