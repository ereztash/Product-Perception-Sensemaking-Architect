# Question Discovery / Decision Framing — Capability Profile v2

Status: `FROZEN_BEFORE_RUN · NATURAL_HISTORICAL_CORPUS · RESEARCH_ONLY`
Date: 2026-09-06

## Goal

Identify what the candidate capability is actually good at, not merely whether it can generate plausible reframes.

We compare four conditions on the same natural historical prompts:

- `A_DIRECT`: answer the stated question directly with strong ordinary reasoning.
- `B_DECISION_ONLY`: identify the underlying decision, then answer; do not explicitly inspect premature commitments.
- `C_COMMITMENT_ONLY`: inspect whether the stated question prematurely fixes a tool/mechanism/resource/decomposition, then answer; do not explicitly search a wider question space.
- `D_FULL`: underlying decision → premature commitment → controlling uncertainty → best question to resolve now or NO_REFRAME → cheapest admissible check.

## Scoring

Per case:
- `MATERIAL_DELTA`: changes evidence, resource allocation, build/defer/stop, or object of decision.
- `PARTIAL_DELTA`: useful distinction but little change to next move.
- `NO_DELTA`: mostly wording/explanation.
- `CORRECT_NO_REFRAME`: preserves a question already fit for purpose.
- `HARM`: adds delay, abstraction, or changes owner intent without authority.

Additional attribution:
- which step first creates the material delta: `DECISION`, `COMMITMENT`, `CONTROLLING_UNCERTAINTY`, `QUESTION_SELECTION`, or none.

## Natural prompts

### CP-01 — Computational Empathy
> "Computational Empathy תוכל ללמד אותי על זה?"

### CP-02 — Empathimetry field existence
> "האם זה תחום מחקרי קיים."

### CP-03 — UX/UI consequence from findings
> "האם זה אומר שיש שינויים שצריך לעשות בUX ובUI של האפליקציה?"

### CP-04 — Claude Code execution plan
> "תעשה את זה בבקשה, כתוב את כל הצעדים מקצה לקצה. תסביר את כל הצעדים בעברית נגישה וברורה לקריאה"

### CP-05 — New tool for LinkedIn acquisition
> "What new tool should I add?"
Context: LinkedIn acquisition system.

### CP-06 — Where acquisition system loses people
> "Where is my system currently losing people?"
Context: LinkedIn acquisition system.

### CP-07 — What should change first vs later
> "What should change first vs later?"
Context: product / UX changes.

### CP-08 — What should remain untouched
> "What should remain untouched for now?"
Context: product / UX scope control.

### CP-09 — Minimum product state model
> "What is the minimum product state model needed for the new loop?"

### CP-10 — Idea-to-execution management process
> "How do I turn an idea into a short process from idea to execution in a meeting with management?"

### CP-11 — Basic two-week roadmap
> "What is a basic two-week roadmap in the context of an AI product?"

### CP-12 — Engineering debt before behavioral adaptation
> "אני חושב שקודם צריך להשלים את החוב ההנדסי, ואז צריך להשלים את החוב שהאפליקציה לא מלאה במקומות בהם הקוד כול ללמוד את התנהגות המשתמש כדי להתאים את האפליקציה אליו, מה דעתך? ככה האינרציוניות שלה אפליקציה תהיה עם פחות חיכוכים"

## Expected diversity

This corpus intentionally mixes:
- direct knowledge questions;
- direct execution requests;
- already-upstream diagnostic questions;
- bounded prioritization/scope questions;
- tool/resource-selection questions;
- architectural/model questions;
- sequencing hypotheses.

No case is labeled challenge/control before outputs. The run must discover where intervention is useful.

## Run discipline

1. Freeze this file before outputs.
2. Run A, B, C, D separately.
3. Preserve cases where a weaker condition performs equally well.
4. Attribute the earliest step that creates real decision delta.
5. Do not reward abstraction or longer answers.
6. The aim is capability decomposition: find the minimal mechanism that explains wins and the domain of cases where it should not fire.