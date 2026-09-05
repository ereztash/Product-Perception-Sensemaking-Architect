# Chess Error Adaptation Research

Status: `BROAD_RESEARCH_CLOSED / EXECUTION_HANDOFF`

Purpose: build an evidence-bounded knowledge spine for adapting chess-error diagnosis to player skill/context without collapsing rating, engine loss, human likelihood, cognitive mechanism, individual weakness, time allocation and pedagogical action into one label.

## Research lineage

1. `CAL_CHESS_ERROR_001_TASK.md` — owner telos, blocked decision, authority and required peer process.
2. `RND_NETA_RESEARCH_PLAN_V0.md` — research plan produced after R&D diagnosis + Neta challenge.
3. `PASS1_FINDINGS.md` — rating-conditioned behavior, individual deviation, contextual error structure and multilingual/source-family findings.
4. `SOURCE_REGISTER_PASS1.md` — source register with evidence ceilings.
5. `PASS2_OPERATIONALIZATION.md` — executable descriptive stack: ratings, Maia human priors, engine consequence, board concepts, context and player deviation.
6. `PASS3_MECHANISM_EVIDENCE.md` — evidence ladder separating observed error form, statistical weakness and cognitive mechanism.
7. `PASS4_PEDAGOGY.md` — intervention/outcome lane; diagnosis fit is not pedagogical efficacy.
8. `PASS5_TIME_ERROR_CROSS.md` — orthogonal `decision quality × time allocation quality` model.
9. `PASS6_INSTRUMENT_RECOVERY_AND_STOP.md` — recovered open VOC/EVOC/cost-of-time instruments and broad-research stop decision.

## Current model

```text
POSITION / GAME STATE
        |
        +-- ENGINE CONSEQUENCE
        +-- OBSERVED ERROR FORM
        +-- SKILL-CONDITIONED HUMAN PRIOR
        +-- PLAYER-SPECIFIC DEVIATION
        +-- BOARD / GAME CONTEXT
        +-- TIME / COGNITIVE-RESOURCE ALLOCATION
        |
        v
EVIDENCE-BOUNDED PLAYER STATE
        |
        +-- statistical weakness
        +-- open mechanism hypotheses
        +-- time-allocation pattern
        |
        v
INTERVENTION CANDIDATE
        |
        v
FUTURE MATCHED-OPPORTUNITY OUTCOME
```

## Two independent ledgers

### A. Decision / error ledger

- what error form occurred;
- opportunity-normalized recurrence;
- cohort prior vs player deviation;
- mechanism hypotheses with evidence ceilings.

### B. Resource-allocation / time ledger

- remaining budget;
- move time;
- position criticality / VOC / EVOC;
- cohort-expected allocation;
- underinvestment / overspend / reserve-depletion candidates;
- pressure-response curve.

The ledgers cross-link only when evidence supports mediation/amplification. A correct move can still be a poor time allocation; a bad move can occur under reasonable allocation.

## Current strongest reusable instruments

- Maia-2 / Maia-3: rating-conditioned human move priors;
- Maia individual / Maia4All lineage: player-specific behavior beyond rating;
- Stockfish + WDL/Win% transforms: multi-view consequence;
- Maia skill-adaptation concept oracle + Lichess puzzle themes: observable board/concept features;
- `evanrussek/Thinking_Time_VOC_Chess`: open VOC, EVOC and cost-of-time pipelines on Lichess data.

These are instrument candidates with provenance requirements, not automatic truths.

## R&D stop decision

`STOP_BROAD_RESEARCH → EXECUTION_HANDOFF`

Further broad multilingual/literature/OSS search is not currently the cheapest decision-changing move.

The next evidence must come from execution on target data:

1. reproduce/adapt VOC/EVOC on the target Lichess distribution;
2. test whether it adds information beyond simple clock/position baselines;
3. cross `error form × time allocation` on held-out games;
4. estimate player-specific deviation learning curves;
5. test sensitivity across blunder definitions, engine configurations and time controls;
6. only then test intervention policies prospectively.

Resume research only when execution exposes a named unresolved construct, transfer failure, instrument failure or pedagogical question.

## Rule

Do not add sources because a language or source category is missing. Add a source only when it can change a live claim, discriminator, operationalization, boundary or next decision.
