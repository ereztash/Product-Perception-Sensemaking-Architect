# Chess Error Adaptation — Pass 5: Error × Time Allocation

Status: `R&D_EXECUTION_PASS_5_COMPLETE`
Date: 2026-09-05
Task: `CAL-CHESS-ERROR-001`

## Trigger

Owner proposed crossing the error-adaptation model with in-game time management.

R&D treats this not as an extra feature but as a candidate orthogonal axis:

```text
DECISION QUALITY
×
TIME ALLOCATION QUALITY
```

## Neta challenge

Avoid the proxy:

> `long think = good time management` or `fast move = bad time management`.

Move time is only meaningful relative to:

- remaining clock budget;
- increment/delay;
- position difficulty/ambiguity;
- value of additional computation;
- game phase;
- player skill/time-control cohort;
- future opportunity cost of spending time now.

Therefore time-management judgment must be opportunity- and context-normalized.

---

# P5.1 Time allocation is itself a chess skill

A 2025 Cognitive Science study analyzed more than 12 million online chess games and modeled time spent per move as cognitive-resource allocation. Players spent more time in positions where additional computation was estimated to have greater value. The relationship was stronger in stronger players.

### Surviving claim

> Expertise includes not only making better decisions but allocating deliberation time more selectively to positions where thinking is more valuable.

This makes time allocation a legitimate adaptation target rather than merely a nuisance covariate.

---

# P5.2 Remaining time and move time are distinct variables

Recent elite-chess evidence separates:

- `move_time` — how much was spent on this decision;
- `time_budget_remaining` — how constrained the player was when the decision began.

Fast moves made with ample remaining time can be accurate intuitive decisions. Fast moves made under severe clock pressure have higher blunder propensity.

### Surviving distinction

```text
FAST + AMPLE BUDGET ≠ FAST + FORCED TIME PRESSURE
```

Do not infer impulsivity from short move time alone.

---

# P5.3 Error probability is nonlinear in time pressure × position difficulty

A 2026 Scientific Reports analysis of 39,922 ply-level positions from elite Lichess blitz found nonlinear amplification of blunder probability when low remaining time coincided with high positional ambiguity. The interaction survived multiple model specifications and game-phase controls.

### Product implication

Time pressure should not be modeled as a global penalty independent of the position.

Candidate interaction:

```text
ERROR RISK ~ TIME PRESSURE × POSITION CRITICALITY/AMBIGUITY
```

The same 8 seconds remaining can be adequate in a forced recapture and disastrous in a high-branching critical position.

---

# P5.4 Candidate `VALUE_OF_COMPUTATION` instrument

The 2025 resource-rationality work operationalizes the value of computation by estimating how much move quality improves when a deeper/higher-computation search is used instead of a shallower one.

This suggests an executable quantity for our stack:

`VOC(position, current_information)`

Possible proxies/features:

- evaluation gap between shallow and deeper engine search;
- best-vs-second-best move distinctness;
- branching / engine-search complexity;
- tactical forcingness;
- evaluation instability across depths;
- human-move entropy under Maia;
- number of plausible cohort-typical alternatives;
- phase / novelty / familiarity features.

### Authority boundary

These are proxies for expected benefit of additional computation, not direct measurements of subjective difficulty.

---

# P5.5 Time-allocation deviation should be cohort-conditioned

We should estimate an expected time-spending function rather than use absolute thresholds:

```text
E[move_time |
  rating_context,
  time_control,
  remaining_time,
  increment,
  move_number,
  position_features,
  value_of_computation]
```

Then model player-specific residuals:

`time_allocation_residual = observed_move_time - expected_move_time`

But residual sign is not yet a verdict. Positive can be useful deliberation or waste; negative can be efficient intuition or harmful underinvestment.

Decision quality and future clock consequences are required.

---

# P5.6 Candidate time-management error forms

These labels describe resource-allocation patterns and are safer than psychological labels.

## T1 — `CRITICAL_UNDERINVESTMENT`

Conditions:
- high estimated value of computation / criticality;
- sufficient clock budget was available;
- player spent materially less than matched expectation;
- resulting move quality was poor or the relevant opportunity was missed.

Interpretation ceiling:
> Too little time was allocated relative to the measured decision context.

Not:
> Player was lazy / impulsive / overconfident.

## T2 — `LOW_VALUE_OVERINVESTMENT`

Conditions:
- low estimated value of computation / forced or easy decision;
- materially above-expected time spent;
- no commensurate decision benefit;
- time expenditure creates meaningful future budget cost.

This is not just “slow move”; it is costly allocation with low observed benefit.

## T3 — `TIME_RESERVE_DEPLETION`

Cumulative over-spending earlier in the game leaves the player in later forced time pressure.

Important causal chain candidate:

```text
early allocation pattern
→ reduced future budget
→ high-pressure critical position
→ downstream error
```

The downstream blunder may therefore be partly a time-management event even if the immediate move mechanism is tactical.

## T4 — `FAILURE_TO_SCALE_TIME_WITH_CRITICALITY`

Across many moves, the player's time use is weakly coupled to estimated value of computation compared with skill-matched peers.

This is especially promising because stronger players in the large 2025 dataset showed stronger coupling between time spent and value of computation.

## T5 — `POST_ERROR_TIME_DYSREGULATION`

After a significant error, player timing shifts (e.g. slowing or abnormal allocation) and subsequent accuracy deteriorates relative to matched controls/player baseline.

Avoid psychological labels such as tilt unless additional evidence exists.

## T6 — `TIME_PRESSURE_RESILIENCE / VULNERABILITY`

Estimate the player's error amplification as remaining time falls, conditional on position difficulty and comparison cohort.

Two equal-rated players may differ materially in how quickly decision quality collapses under pressure.

---

# P5.7 Error taxonomy and time taxonomy must remain separable

A single event can have two simultaneous labels:

```text
CHESS ERROR FORM:
  missed tactical opportunity / non-immediate eval loss / endgame conversion error ...

TIME ALLOCATION FORM:
  critical underinvestment / reserve depletion / high-pressure vulnerability ...
```

This supports distinctions such as:

### Case A
`missed fork + normal time allocation`

Likely chess-specific weakness evidence; time not implicated.

### Case B
`missed fork + critical underinvestment with ample budget`

The same board error now has a time-allocation component.

### Case C
`missed fork + forced sub-3-second move after earlier overspending`

The immediate tactical miss may be downstream of reserve depletion.

### Case D
`correct move + 40-second overspend in a forced position`

No chess error occurred, but a time-management error may have created future risk.

This is why time management cannot be attached only to moves already labeled mistakes.

---

# P5.8 Candidate two-ledger player model

```text
PLAYER MODEL

A. DECISION LEDGER
   - observed error forms
   - opportunity-normalized weakness
   - human-likelihood deviations
   - candidate mechanisms

B. RESOURCE-ALLOCATION LEDGER
   - time budget state
   - move-time allocation
   - value-of-computation / criticality
   - allocation residual
   - future time-debt consequences
   - pressure-response curve

CROSS-LINK
   - when an error is plausibly mediated/amplified by allocation
   - when allocation is poor despite a correct move
```

---

# P5.9 Candidate metrics — no composite score

Do not create a single `time management score` yet.

Track orthogonally:

1. `criticality_time_coupling`
   - sensitivity of move time to estimated value of computation;
2. `underinvestment_error_rate`
   - error probability in high-value positions with below-expected allocation;
3. `low_value_overspend_cost`
   - time consumed in low-value decisions and downstream budget effect;
4. `pressure_error_curve`
   - decision-quality degradation as remaining time falls;
5. `reserve_depletion_events`
   - games where early allocation predicts later forced pressure;
6. `post_error_allocation_shift`
   - timing change after significant error;
7. `allocation_stability`
   - whether patterns replicate across games/windows/time controls.

Each requires uncertainty/sample counts.

---

# P5.10 Rating × time management

Rating should condition the comparison, not define the verdict.

Research suggests stronger players show more selective coupling between deliberation time and value of computation. Therefore the product should ask:

> Relative to players in the same platform/pool/time-control/rating context, where does this player allocate time differently — and does that difference predict decision quality?

This allows adaptation without hard-coded rules such as:

`1600 players think too quickly in tactics`.

---

# P5.11 Pedagogical consequences

The Error × Time model creates interventions unavailable from an error-only model.

Examples:

- repeated tactical weakness, normal allocation → motif/review intervention;
- strong chess knowledge but repeated critical underinvestment → critical-position recognition/time-allocation training;
- early low-value overspending → reserve-budget training;
- pressure-specific collapse → practice under matched clock conditions;
- correct moves with expensive deliberation → fluency/recognition training rather than error correction;
- post-error allocation disruption → recovery/reset protocol candidate.

Intervention effectiveness still requires prospective outcome evidence.

---

# Decision after Pass 5

The time axis materially improves the research model and should be promoted into the descriptive architecture as a first-class ledger.

The model becomes:

```text
POSITION / GAME STATE
        |
        +--> DECISION QUALITY / ERROR FORM
        |
        +--> TIME / COGNITIVE-RESOURCE ALLOCATION
        |
        +--> SKILL-CONDITIONED HUMAN PRIOR
        |
        +--> PLAYER-SPECIFIC DEVIATION
        v
EVIDENCE-BOUNDED PLAYER STATE
        |
        v
INTERVENTION CANDIDATE
        |
        v
FUTURE MATCHED-OPPORTUNITY OUTCOME
```

## Next R&D uncertainty selected

The key remaining research question is now operational rather than conceptual:

> Can `value of computation / position criticality` and time-allocation deviation be estimated robustly enough from Lichess-style game data to classify underinvestment, overspending and reserve depletion without merely redescribing move time?

This requires instrument recovery/prototyping and sensitivity testing, not another broad theory sweep.
