# Framework Fit V2 — Erez281

Run: `34762514956`

Status: observational addressability, not causal prevention.

## Instrument

- Owner eligible decisions: 52,881 across 2,161 games.
- VALIDATE: 10,626 decisions across 432 games.
- TEST: 10,404 decisions across 432 games.
- Population reference: 34,794 eligible decisions across 600 games.
- Split: chronological by game, 60% DERIVE / 20% VALIDATE / 20% TEST.

## Selection rule

Fixed frameworks were compared on VALIDATE by historical Stockfish win-probability-loss coverage per fixed manual-burden estimate. TEST was opened only after selection. Coverage means retrospective addressability: the share of actual historical errors/loss occurring in decisions a framework primitive explicitly points at. It is not evidence that asking the question would have prevented the loss.

## Base framework result

Winner on VALIDATE: `CLOSURE_GATE`

Primitives:
1. `what_changed`
2. `persistent_closure`
3. `blunder_check`

VALIDATE:
- error coverage: 75.77%
- loss coverage: 83.58%
- blunder10 coverage: 86.79%
- conditional trigger operations per move: 1.78

TEST:
- error coverage: 73.11%
- loss coverage: 80.64%
- blunder10 coverage: 84.67%
- conditional trigger operations per move: 1.76

## Fixed-framework ranking

| Framework | VALIDATE efficiency | VALIDATE loss coverage | TEST loss coverage | Manual burden |
|---|---:|---:|---:|---:|
| CLOSURE_GATE | 0.2786 | 83.58% | 80.64% | 3.0 |
| AWARENESS_SAFETY | 0.2719 | 81.56% | 78.52% | 3.0 |
| PROPHYLAXIS_FIRST | 0.2719 | 81.56% | 78.52% | 3.0 |
| CANDIDATE_PLUS_BLUNDER | 0.2265 | 79.28% | 79.86% | 3.5 |
| CCT_BOTH_WAYS_BLUNDER | 0.1678 | 75.52% | 74.12% | 4.5 |
| CCT_PLUS_CLOSURE | 0.1285 | 51.41% | 50.31% | 4.0 |
| CCTO | 0.0832 | 33.27% | 34.78% | 4.0 |

CCTO is only partially measured here: full human threat generation is not encoded in the frozen traces, so its measured coverage is a lower bound rather than a complete evaluation of the framework.

## Personal compression

Among selective observable gates, using VALIDATE only, the lowest-load bundle within the frozen selection rule was simply:

`WHAT CHANGED?`

VALIDATE:
- loss coverage: 75.30%
- error coverage: 68.34%
- blunder10 coverage: 78.52%
- trigger rate / conditional operations per move: 68.59%

TEST:
- loss coverage: 71.90%
- error coverage: 66.30%
- blunder10 coverage: 74.97%
- trigger rate / conditional operations per move: 67.28%

Key VALIDATE Pareto points:
- persistent closure alone: 9.35% loss coverage at 9.17% trigger rate.
- big opponent error reset alone: 33.65% loss coverage at 16.12% trigger rate.
- persistent closure + big opponent error reset: 39.50% at 25.29%.
- urgent safety alone: 55.44% at 63.22%.
- what changed alone: 75.30% at 68.59%.
- what changed + persistent closure: 77.82% at 77.75%.

## Population discrimination

### Big opponent error reset

Definition: opponent's previous move lost at least 10 percentage points of Stockfish win probability.

- Owner TEST trigger rate: 15.32%.
- Population trigger rate: 13.02%.
- Owner error rate after trigger: 56.59%.
- Population error rate after trigger: 56.72%.

Interpretation: this is a high-value conditional state, but the current evidence does not make it player-specific; comparable players also struggle strongly after a large opponent error.

### Persistent closure

- Owner TEST trigger rate: 8.24%.
- Population trigger rate: 7.38%.
- Owner unresolved rate when triggered: 77.596%.
- Population unresolved rate when triggered: 77.600%.

Interpretation: Erez is not unusually likely to leave the persistent liability unresolved. The earlier player-specific result concerns the excess consequence/risk when he does leave the liability unresolved, not the raw frequency of non-resolution.

## Product translation

Current evidence supports a two-layer architecture rather than selecting one named framework for all moves:

1. A compact base routine.
2. Conditional gates that activate only in high-value states.

For Erez281, the current best evidence-bounded translation is:

Base routine:
1. What changed after the opponent's last move?
2. Is something from the previous position still unresolved?
3. Before committing, what is the opponent's strongest reply?

Conditional interrupt:
- If the opponent just made a large error, reset the previous plan and re-scan the position before continuing.

This is a candidate intervention. A prospective test is required before claiming that using it reduces errors, improves rating, or prevents the historical loss it retrospectively addresses.
