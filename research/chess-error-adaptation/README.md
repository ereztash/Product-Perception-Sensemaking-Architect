# Chess Error Adaptation Research

Status: `ACTIVE_R&D_PROGRAM`

Purpose: build an evidence-bounded knowledge spine for adapting chess-error diagnosis to player skill/context without collapsing rating, engine loss, human likelihood, cognitive mechanism, individual weakness and pedagogical action into one label.

## Start here

1. `CAL_CHESS_ERROR_001_TASK.md` — owner telos, blocked decision, authority and required peer process.
2. `RND_NETA_RESEARCH_PLAN_V0.md` — research plan produced after R&D diagnosis + Neta challenge.
3. `PASS1_FINDINGS.md` — first executed research pass and surviving distinctions.
4. `SOURCE_REGISTER_PASS1.md` — multilingual/source-family register with evidence ceilings.

## Current state

Pass 1 rejects a hard-coded `Elo → mistake type → lesson` table.

Current candidate structure:

```text
ERROR EVENT
+ ENGINE CONSEQUENCE
+ POSITION/TIME CONTEXT
+ SKILL-CONDITIONED HUMAN PRIOR
+ ERROR-MECHANISM HYPOTHESES
+ PLAYER-SPECIFIC DEVIATION
→ EVIDENCE-BOUNDED DIAGNOSIS
→ PEDAGOGICAL ACTION (separate evidence lane)
```

## Next R&D question

Before expanding the pedagogy lane, operationalize the descriptive model against executable/open data:

1. Which exact outputs from Maia / blunder-prediction systems can serve as instruments?
2. How do Lichess/FIDE/Chess.com rating and time-control boundaries affect transfer?
3. Which error labels can be computed from board/game data without pretending to know the player's cognition?
4. How many historical games are needed before player-specific deviation is more useful than the rating prior?
5. How sensitive are conclusions to the operational definition of `blunder` (CPL, WDL drop, material horizon, tactical immediacy, etc.)?

## Rule

Do not add sources because a language or source category is missing. Add a source only when it can change a live claim, discriminator, operationalization, boundary or next decision.
