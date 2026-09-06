# Front-Door Gate Shadow Test v0 — Frozen Natural Prompts

Status: `FROZEN_BEFORE_GATE · RETROSPECTIVE_NATURAL_HOLDOUT · RESEARCH_ONLY`
Date: 2026-09-06

## Question under test

Can a compact front-door gate safely avoid unnecessary full R&D/Calibration-Loop invocations while preserving the materially same next move?

## Gate output classes

- `DIRECT_EARNED` — answer/execute directly; no calibration needed.
- `CHEAP_TEST` — proposed action is already a cheap, reversible, informative discriminator.
- `FIXED_CONSTRAINT` — optimize within a legitimate settled boundary.
- `DOMAIN_HANDOFF` — route to a domain authority/capability rather than R&D calibration.
- `NEEDS_CALIBRATION` — run the full R&D Calibration Loop.

## Metrics frozen before outputs

- `BYPASS_RATE`: fraction classified outside `NEEDS_CALIBRATION`.
- `FALSE_BYPASS_RATE`: gate bypasses R&D but full R&D would materially change the next move.
- `UNNECESSARY_ESCALATION_RATE`: gate invokes R&D but full R&D adds no material decision delta.
- `DECISION_AGREEMENT_ON_BYPASS`: materially same next move between gate and shadow R&D.
- `AUTHORITY_VIOLATION_RATE`: gate reopens settled OWNER/contract/domain authority without justification.
- `GATE_HARM`: added delay/abstraction that worsens a cheap justified action.

A material disagreement means different evidence/resource/build/defer/stop/authority action, not wording.

## Frozen natural historical prompts

### SG-01
> "האם המבחן הזה מעלה את ערך המוצר?"
Context: after running a new empirical test on the Lichess app.

### SG-02
> "בוא נעשה את זה, בוא נריץ על כל 2,533 המשחקים הכשירים"
Context: an initial smaller game-history experiment had already run successfully.

### SG-03
> "תבנה פיצ'ר שמראה לי התקדמות באחוזים"
Context: a long-running batch analysis the owner had already chosen to execute.

### SG-04
> "אני רוצה שלאחר מכן תכין לי פרומפט שיוצר אפליקציה בHTML בGemini בממשק WEB שמלמדת את כל החומר, לא דמו, אפליקציה אמיתית, עם כל החומר"
Context: owner explicitly wants a complete teaching app after gathering the curriculum.

### SG-05
> "מה המוצרים שהכי דומים לנטע שנמכרו?"

### SG-06
> "אם נטע הייתה עובדת כחלק מצוות שמקים חברה, מי היו חברי הצוות האחרים?"

### SG-07
> "מעניין, אני רואה שהאינטגרציה לPM ותבניות העבודה בעצם אנחנו צריכים להפוך את זה לדורש כמה שפחות מאמץ מהמשתמש, החל מתבניות הביצוע ועד להתלבשות על ציר עבודה קיים?"

### SG-08
> "מה אני צריך לעשות תוך כדי צילום הסרטון?"
Context: owner had already decided to record the next Instagram video.

### SG-09
> "מה הדרך ללמוד מהשיחה בצורה הכי טובה? אולי כדאי לייצא לMD את התובנות שרשמת."

### SG-10
> "פשוט לא לענות?"
Context: live LinkedIn/DM thread after receiving a response that may not need continuation.

### SG-11
> "תעשה בדיקה נוכחית על המצב ריפו של נטע ושל ליצ'ס"

### SG-12
> "האם יש שיטות מוכחות?"
Context: handling sales objections.

### SG-13
> "אלגוריתם שמתאים שיטה לסיטואציה?"
Context: after asking about evidence-based objection-handling methods.

### SG-14
> "תכתוב ששלחתי לה את ההודעה"
Context: update a lead record after the owner had actually sent the message.

### SG-15
> "מה דעתך על הריפו של הCRM? עבדתי עליו כל הלילה עם פייבל באולטרה קוד"

### SG-16
> "אני לא הצלחתי לפתוח את זה ולראות את הCRM בפועל עם הUI שלו, אתה יכול להריץ ולבדוק?"

### SG-17
> "האם המיינטביליות, היא חלק מתוך קבוצת פערים?"
Context: repo assessment; asking where maintainability belongs conceptually.

### SG-18
> "בוא נלך לכיוון אחר, אם נטע הייתה עובדת כחלק מצוות שמקים חברה, מי היו חברי הצוות האחרים?"
Context: exploration of orthogonal functions around Neta.

### SG-19
> "אני רוצה למצוא דברים שלא קשורים בקוד ולא קשורים במשתמשים אחרים, מה עם חשבון הליצ'ס שלי? אולי אפשר להוציא משם דברים שיכולים לעזור?"
Context: deliberately retained as a positive-control case previously seen to require calibration; included here as an anchor, not a holdout.

### SG-20
> "רגע, המיינטננס, מה המשמעות שלו? מה החשיבות שלו?"
Context: deliberately retained as a negative-control/direct case previously seen to need no calibration; included here as an anchor.

## Validity note

SG-01..SG-18 are historical natural prompts not used in the prior gate-vs-R&D benchmark as scored cases. SG-19 and SG-20 are explicit anchors with known prior behavior, included to detect drift.

This is still retrospective and same-model. It is a shadow-routing experiment, not independent prospective validation.

## Run order

1. Freeze this file.
2. Produce and freeze gate classifications + next moves.
3. Only then produce shadow full-R&D decisions.
4. Adjudicate metrics after both are frozen.
5. Preserve all misses; do not amend the gate mid-run.