# Commitment Qualification vs R&D v0.2 — Frozen Benchmark

Status: `FROZEN_BEFORE_COMPARATIVE_RUN · RESEARCH_ONLY`
Date: 2026-09-06

## Decision under test

Does the candidate `Earn the next move` / commitment-qualification capability create a material decision delta beyond existing R&D v0.2 + Calibration Loop, or is it a cheaper/front-door specialization of capabilities the system already owns?

## Conditions

### A — R&D SOLO
Apply `prompts/RND_AGENT_V0_2_CANDIDATE.md` only:
`TELOS → CURRENT STATE → RESOURCE MAP → BOTTLENECK → CANDIDATE MOVES → CHEAPEST DECISION-CHANGING LEARNING`.

### B — EXISTING CALIBRATION LOOP
R&D diagnoses; deterministic routing may invoke Neta when proxy/mechanism/intervention triggers fire; R&D synthesizes.

### C — COMMITMENT QUALIFICATION GATE
Apply the candidate compact gate:
`NEXT MOVE → OPEN OR FIXED? → EARNED / CHEAP TEST / NOT-YET-EARNED / INFEASIBLE → ACT / TEST / DISCRIMINATE / ESCALATE`.

### D — GATE + EXISTING LOOP
Run C first. Invoke the full existing Calibration Loop only if C cannot close the decision cheaply.

## Evaluation dimensions

- `DECISION_DELTA`: does a condition materially change build/research/tool/sequence/action?
- `UNIQUE_DISTINCTION`: does C identify something A/B do not?
- `RESOURCE_BURDEN`: how much system machinery must be invoked before the next move is bounded? (`LOW`, `MEDIUM`, `HIGH`; structural proxy, not measured compute cost).
- `AUTHORITY_RESPECT`: does it preserve OWNER/fixed constraints?
- `REVERSIBILITY_SENSITIVITY`: does it allow cheap informative action while gating expensive commitment?
- `HANDOFF_QUALITY`: if domain knowledge is needed, does it route instead of pretending to resolve it?

## Cases

### OR-01 — Sheet as lead-state authority
> “מה דעתך ליצור קובץ Sheet שאתה מעדכן בו סטטוסים של אנשים?”

### OR-02 — Research ROI
> “האם הROI של המחקר הזה יהיה הגבוה ביותר שאפשר?”

### OR-03 — Lichess history as evidence source
> “מה עם חשבון הליצ'ס שלי? אולי אפשר להוציא משם דברים שיכולים לעזור?”

### OR-04 — Marketing asset inventory
> “מה הם הנכסים השיווקיים שצריכים להיות לשקד ברנד?”

### OR-05 — Findings imply UX/UI changes
> “האם זה אומר שיש שינויים שצריך לעשות בUX ובUI של האפליקציה?”

### OR-06 — Engineering debt before adaptation debt
> “אני חושב שקודם צריך להשלים את החוב ההנדסי, ואז ... להתאים את האפליקציה להתנהגות המשתמש, מה דעתך?”

### OR-07 — Cheap reversible CRM test
> “הצוות אומר שה-CRM מבזבז זמן. האם להשקיע 30 דקות בלשחזר את ה-workflow הכי גרוע בסנדבוקס של CRM אחר?”

### OR-08 — Fixed Vercel constraint
> “מדיניות החברה מחייבת שהמוצר ירוץ על Vercel. מה צריך לשנות כדי שהוא יתאים?”

### OR-09 — Direct factual question
> “האם Empathimetry הוא תחום מחקרי קיים?”

### OR-10 — Already-upstream diagnostic
> “Where is my system currently losing people?”

## Promotion rule

Do **not** promote C as a separate product/capability merely because it is clearer or shorter.

A separate epistemic capability requires repeated cases where C produces a material distinction/decision unavailable from A/B at comparable evidence/authority.

A lightweight gate may still be justified if:
- C reaches the same safe decision with materially lower structural burden in common cases;
- C correctly stops/no-fires often;
- D reduces unnecessary Calibration Loop invocations without losing decisions or authority.

This would justify `front-door optimization`, not a new peer ontology.