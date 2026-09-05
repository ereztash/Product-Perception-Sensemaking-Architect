# Chess Error Adaptation — Pass 6: Instrument Recovery + Research Stop

Status: `R&D_EXECUTION_PASS_6_COMPLETE / BROAD_RESEARCH_STOP`
Date: 2026-09-05
Task: `CAL-CHESS-ERROR-001`

## Question entering the pass

Can position criticality / value of computation and time-allocation deviation be estimated robustly enough from Lichess-style game data to become an executable instrument, rather than merely redescribing long/short move times?

## Neta challenge

The main remaining proxy risk:

> a hindsight engine measure can look like `position criticality` while using information the player could not have known before choosing.

Therefore the instrument must distinguish:

- hindsight `VOC`;
- expected/available-information `EVOC`;
- actual move time;
- remaining budget;
- downstream decision quality.

---

# P6.1 An open implementation already exists

The public repository `evanrussek/Thinking_Time_VOC_Chess`, released with the 2025 Cognitive Science paper *Time Spent Thinking in Online Chess Reflects the Value of Computation*, contains three separable analysis families:

1. `VOC_Analysis`
   - computes value of computation per move;
   - links it to response time;
   - aggregates by Elo and time-control setting;
   - computes VOC↔RT correlation by Elo.

2. `EVOC_Analysis`
   - extracts move/Stockfish data;
   - computes expected value of computation;
   - relates EVOC to move time and player strength.

3. `Cost_of_Time_Analysis`
   - estimates win-rate/value as a function of board advantage and time left;
   - computes implied cost of time;
   - computes implied optimal move-time policies under the paper's value-function assumptions.

The code uses public Lichess data, Stockfish and python-chess.

### R&D disposition

`REUSE_OR_ADAPT`, not `BUILD_FROM_SCRATCH`.

Before reuse, pin repository commit, Stockfish version, python-chess version, input schema and exact output contract.

---

# P6.2 VOC is reproducible enough to test, not yet canonical enough to trust blindly

The released workflow computes Stockfish move selections at multiple search depths, evaluates those moves at a higher reference depth, transforms engine values into win-probability-like utility, and derives benefit of additional computation.

### Why this is valuable

It creates a position-dependent estimate of whether deeper thinking *could buy decision quality*, rather than equating criticality with:

- long human move time;
- large CPL after the fact;
- number of legal moves;
- tactical theme count.

### Boundary

Engine depth is a computational surrogate for human cognitive computation. The mapping is useful as an instrument but is not a literal model of human search depth.

---

# P6.3 EVOC addresses the hindsight-leakage concern

The associated paper reports that the relationship between thinking time and benefit of computation becomes stronger when the estimate is constrained toward information available to the player at choice time. The released `EVOC_Analysis` is specifically designed to compute expected value of computation and relate it to move time/player strength.

### Surviving rule

For player-facing time-management diagnosis, prefer an `available-information / expected criticality` estimate when possible.

Keep hindsight VOC separately for retrospective analysis.

Do not silently substitute one for the other.

---

# P6.4 Cost of time is position- and clock-dependent

The released cost-of-time analysis computes value functions over combinations of board advantage and time left, separately by time control, then derives implied costs of spending additional time and corresponding move-time policies.

This supports the core time-allocation model:

```text
marginal benefit of thinking now
vs
marginal cost of consuming future clock budget
```

### Important boundary

The paper's implied `optimal policy` depends on its estimated value function and assumptions. It is a research comparator, not a universal coaching prescription.

The product should first test relative deviation and downstream outcomes before telling a player an exact number of seconds they `should` have spent.

---

# P6.5 Minimal executable instrument stack for the next phase

## Instrument A — `VOC/EVOC POSITION VALUE`

Input:
- FEN/history as required;
- Stockfish pinned version/config;
- time-control context.

Output:
- hindsight VOC;
- expected/available-information EVOC where implementation supports it;
- provenance/version.

## Instrument B — `TIME COST / BUDGET STATE`

Input:
- time left before move;
- increment;
- time-control family;
- current board utility/advantage.

Output:
- empirical/estimated cost of consuming time;
- comparison value function;
- provenance.

## Instrument C — `COHORT TIME POLICY`

Estimate from Lichess/open data:

```text
E[move_time | rating_context, time_control, budget_state, EVOC/VOC, phase, position features]
```

Output:
- expected move-time distribution;
- percentile/residual for observed move.

## Instrument D — `PLAYER TIME DEVIATION`

Across games:

- criticality↔time coupling;
- underinvestment events;
- low-value overspend events;
- reserve-depletion chains;
- pressure-error curve;
- stability/uncertainty.

---

# P6.6 First falsification program

Do **not** promote time-management labels before the following tests.

### F1 — Non-redundancy

Does EVOC/VOC predict/structure move time beyond:
- move number;
- time remaining;
- rating;
- engine evaluation;
- simple legal-move count / forcingness proxies?

If not, the expensive instrument may not earn its cost for our product.

### F2 — Error interaction

Does under-allocation relative to EVOC/cohort expectation predict worse decision quality after controlling for budget and position difficulty?

If not, `critical underinvestment` is not yet useful.

### F3 — Future-cost chain

Do low-value overspend events predict later forced time pressure/error after controlling for game length/state?

If not, reserve-depletion claims must be weakened.

### F4 — Skill dependence

Does criticality↔time coupling change meaningfully by rating/time-control cohort in our target distribution?

If not, rating conditioning can be simplified.

### F5 — Player specificity

Does the player's time-allocation profile predict held-out games beyond cohort priors?

If not, do not personalize this layer yet.

### F6 — Definition sensitivity

Repeat headline findings across:
- VOC vs EVOC;
- alternative engine depths/nodes;
- WDL/Win% vs CPL decision quality;
- multiple time controls;
- multiple player-history windows.

---

# P6.7 R&D stop decision

The broad research program has now produced:

1. a rating-conditioned but non-deterministic human prior;
2. player-specific deviation as a separate layer;
3. multi-view engine consequence rather than one blunder scalar;
4. an evidence ladder separating observed error form from cognitive mechanism;
5. a separate pedagogy/outcome lane;
6. an orthogonal time/resource-allocation ledger;
7. an executable open-source route for VOC, EVOC and cost-of-time estimation;
8. explicit falsifiers for the next phase.

Further broad multilingual / literature / OSS search is unlikely to remove more material uncertainty before execution.

## STOP REASON

Remaining uncertainties are now primarily empirical and distribution-specific:

- whether these instruments replicate on the target Lichess/game distribution;
- whether they add predictive/decision value over simpler baselines;
- whether player-specific time/error profiles stabilize with available history;
- whether resulting interventions improve future matched decisions.

These require `REPO / DATA / EXECUTION / FIELD` evidence, not more broad research.

### R&D decision

`STOP_BROAD_RESEARCH → EXECUTION_HANDOFF`

Resume research only when an execution result exposes a named failure, construct ambiguity, transfer problem, or intervention question that existing evidence cannot resolve.
