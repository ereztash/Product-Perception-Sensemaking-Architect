# Chess Error Adaptation — Pass 2: Operationalization

Status: `R&D_EXECUTION_PASS_2_COMPLETE`
Date: 2026-09-05
Task: `CAL-CHESS-ERROR-001`

## R&D question entering the pass

Can the Pass-1 descriptive model be turned into executable instruments without collapsing rating, engine consequence, board features, player history and cognitive mechanism into one label?

## Neta challenge before execution

Two proxy risks were preregistered:

1. `rating number ≠ universal skill coordinate` across platforms/time controls;
2. `detected board theme ≠ player's error mechanism`.

The pass therefore sought separable instruments with explicit authority ceilings rather than one universal error score.

---

# P2.1 Rating must retain platform/pool/time-control identity

Lichess documents that its ratings use Glicko-2, FIDE uses Elo, and other servers use other implementations/pools. It explicitly warns that ratings cannot be directly compared across servers because the system and player pool differ.

### Surviving rule

Never store only `rating=1600`.

Minimum rating context:

```text
platform
rating_pool / time_control
rating_value
rating_deviation / provisional state when available
observation_date
```

A cross-platform conversion may be a separate empirical model, but it is not a constitutional normalization step.

### Product consequence

A Lichess Blitz 1600 prior must not silently reuse a FIDE Standard 1600 or Chess.com Rapid prior.

---

# P2.2 Skill-conditioned move probability is an executable instrument

Maia-2 and Maia-3 expose human move distributions conditioned on player/opponent skill. Maia-3 exposes `Elo`, `SelfElo`, `OppoElo`, `Temperature`, `TopP` and `MultiPV` through UCI; its WDL/value outputs are human-game outcome predictions, not Stockfish search evaluations.

### Instrument candidate: `HUMAN_MOVE_PRIOR`

Input:
- position / reconstructed history as supported by the model;
- player skill context;
- opponent skill context;
- time-control-specific model where available.

Output:
- probability distribution over human moves;
- rank/probability of played move;
- likely human alternatives.

### Decision-relevant derived features

- `played_move_probability_at_skill`
- `played_move_rank_at_skill`
- `best_engine_move_human_probability_at_skill`
- `human_surprisal = -log P(played_move | skill, position)`
- probability delta versus neighboring skill levels.

### Authority ceiling

This establishes how typical/surprising a move is under a skill-conditioned human model. It does **not** establish why the player chose it or that an unusual move is a pedagogically important weakness.

---

# P2.3 Individual deviation is now feasible with much less history than older approaches

The individual-Maia lineage establishes material player-specific signal beyond cohort rating. Maia4All (2025) reports useful individual behavior modeling with roughly 20 games, compared with the thousands of games required by earlier individualized approaches.

### Surviving rule

`20 games` is a candidate cold-start test point, not a universal threshold.

### Instrument candidate: `PLAYER_DEVIATION_MODEL`

Compare a player's observed move/error-feature distribution against:

1. the skill-conditioned cohort prior;
2. the player's own posterior/history.

Candidate output:

```text
feature / motif / context
cohort_expected_rate
player_observed_rate
sample_n
effect / deviation
uncertainty
stability across windows
```

### Required validation

Run learning curves on the target user's own game distribution: 5 / 10 / 20 / 50 / 100 / 200 games. Promotion occurs only when player-specific predictions or actionable recurrence are reliably better than cohort prior under held-out games.

---

# P2.4 Engine consequence must be multi-view, not one scalar

## View A — raw centipawn loss

Useful for engine-relative magnitude, but strongly dependent on initial position evaluation and engine/depth semantics.

## View B — win-probability / Win% loss

Lichess maps Stockfish centipawns to empirical Win% and computes move accuracy from the before/after Win% difference. This addresses a major CPL problem: losing 300 cp in an equal position is not equivalent to losing 300 cp in a position already overwhelmingly won/lost.

## View C — Lichess judgement bands

The Lichess analysis code historically uses changes in winning chances to classify Inaccuracy / Mistake / Blunder (roughly 10 / 20 / 30 percentage-point loss bands in the referenced implementation).

## View D — immediate vs non-immediate consequence

The 2026 Applied Intelligence study distinguishes errors whose material/game consequence becomes clear immediately from those whose consequence emerges later.

### Surviving rule

Do not choose one `BLUNDER=true` definition at research-design time.

Store enough raw information to compute multiple definitions and run sensitivity analyses.

Candidate fields:

```text
cp_before
cp_best_after
cp_played_after
cpl
win_pct_before
win_pct_after
win_pct_loss
lichess_judgement
immediate_consequence_flag
consequence_horizon_plies
material_delta_by_horizon
mate_state
engine_version
engine_depth_or_nodes
```

---

# P2.5 Open data is sufficient for a large descriptive program

Lichess currently publishes:

- monthly rated game archives;
- a large Stockfish-evaluated-position corpus;
- more than six million rated/tagged puzzles;
- puzzle themes, puzzle rating/RD, popularity and solve-play counts;
- opening datasets.

The puzzle set is especially useful because it offers machine-readable, human-maintained tactical/theme labels and difficulty ratings over positions generated from real games.

### Authority ceiling

Puzzle themes are **position/solution labels**, not direct labels of the preceding player's cognitive failure.

They can support statements such as:

> "The missed opportunity was a fork / pin / back-rank motif."

They cannot alone support:

> "The player does not understand forks."

That second statement requires recurrence and comparison.

---

# P2.6 Maia skill-adaptation provides an executable concept-feature oracle

The Maia-2 skill-adaptation repository contains code for 172 measurable chess concepts and trains probes by Elo level. The oracle includes directly computable concepts such as king danger, captures, forks, pinned pieces and other board-state features.

### Candidate instrument: `BOARD_CONCEPT_ORACLE`

Use deterministic or tested concept functions to label what is present before/after a move.

### Important Neta boundary

```text
concept present ≠ concept noticed
concept noticed ≠ candidate generated
candidate generated ≠ line calculated correctly
line calculated ≠ position evaluated correctly
error repeated ≠ stable weakness unless denominator/opportunity is known
```

Therefore each feature should be modeled with both:

- `opportunities` (how often the motif/concept was materially present);
- `misses/errors` (how often the player failed under a defined decision condition).

---

# P2.7 Time and post-error state are first-class context

Recent large-scale naturalistic work defines errors via engine-evaluation drop and matches post-error decisions to control positions on player/opponent rating, move number, clock times, position evaluation and opponent response time. It finds post-error slowing and accuracy impairment, with moderation by ability/error severity.

### Surviving rule

Do not interpret a player's error feature without time context when clocks are available.

Minimum temporal context:

```text
time_control
initial_time
increment
remaining_time_before_move
move_time
relative_time_pressure
previous_move_error_severity
opponent_response_interval
```

---

# P2.8 Candidate executable stack

```text
1. GAME NORMALIZER
   PGN + clocks + platform + pool + ratings

2. ENGINE CONSEQUENCE LAYER
   Stockfish raw evals + WDL/Win% transforms + multiple blunder definitions

3. HUMAN PRIOR LAYER
   Maia-like P(move | position, skill, opponent skill, time-control model)

4. BOARD CONCEPT LAYER
   deterministic concepts + Lichess puzzle/theme vocabulary where applicable

5. CONTEXT LAYER
   phase, clocks, position ambiguity proxies, previous-error state

6. PLAYER DEVIATION LAYER
   recurrence/opportunity rates vs skill-matched cohort, with uncertainty

7. MECHANISM HYPOTHESIS LAYER
   may generate candidate explanations but cannot promote them without discriminator evidence
```

---

# Pass-2 sensitivity contract

For every headline finding, rerun across at least neighboring operationalizations when relevant:

- CPL thresholds;
- Win% loss thresholds;
- Lichess judgement;
- immediate/non-immediate consequence;
- engine depth/nodes/version;
- rating band width / continuous conditioning;
- time control;
- minimum player-history sample.

A finding that exists only under one arbitrary cut should remain fragile.

---

# Decision after Pass 2

The descriptive model is operationalizable. No additional broad search is needed on the existence of rating-conditioned move priors, individual signal, engine loss metrics or open data.

## Next material uncertainty selected by R&D

> Which candidate error/mechanism labels can be supported from observable game/board/context data, and which labels inherently require a cognitive discriminator or player report?

This becomes Pass 3.

## Explicit stop on one lane

Stop searching for a universal cross-platform Elo conversion unless a product decision later requires one. Preserve native rating identity instead.
