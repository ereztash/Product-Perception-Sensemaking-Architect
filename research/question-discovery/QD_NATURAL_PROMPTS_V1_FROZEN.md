# Question Discovery Natural-Prompt Benchmark v1 — Frozen Inputs

Status: `FROZEN_BEFORE_BASELINE_AND_CHALLENGER · RETROSPECTIVE_NATURAL_PROMPTS · RESEARCH_ONLY`
Date: 2026-09-06

Purpose: test the problem definition discovered by self-application:

> misallocated decision effort caused by a question that has already committed to a mechanism / object / decomposition before the uncertainty controlling the decision has been resolved.

## Critical validity note

These are naturally occurring user prompts from prior conversations, not prompts invented for this benchmark. However, the evaluator has retrospective knowledge of some later conversation paths. This makes the corpus stronger than synthetic smoke cases but still contaminated relative to a true prospective holdout.

## Frozen scoring dimensions

For each prompt compare:

1. `BASELINE_ACTION` — what a strong direct answer would tend to do next.
2. `QD_DISPOSITION` — `REFRAME` or `NO_REFRAME`.
3. `PREMATURE_COMMITMENT` — mechanism/tool/decomposition/metric/resource assumed too early, if any.
4. `UPSTREAM_UNCERTAINTY` — the unresolved uncertainty that actually controls the decision.
5. `DECISION_DELTA` — whether the challenger changes evidence, resource use, build/defer/stop, or object of decision.
6. `AVOIDED_WORK` — concrete work likely avoided if the reframe is correct.
7. `HARM` — unnecessary abstraction/delay/goal substitution.

Success requires material decision delta or correct `NO_REFRAME`; better wording alone does not count.

---

## NP-01 — Deploy CRM to Vercel

> "אתה יכול לייצא את הריפו של CRM לורסל?"

---

## NP-02 — Use a Sheet as lead-state store

> "מה דעתך ליצור קובץ Sheet שאתה מעדכן בו סטטוסים של אנשים? אתה יכול לעשות את זה?"

---

## NP-03 — Maximize ROI of a research program

> "האם הROI של המחקר הזה יהיה הגבוה ביותר שאפשר?"

---

## NP-04 — Use personal Lichess account data

> "אני רוצה למצוא דברים שלא קשורים בקוד ולא קשורים במשתמשים אחרים, מה עם חשבון הליצ'ס שלי? אולי אפשר להוציא משם דברים שיכולים לעזור?"

---

## NP-05 — API key export feasibility

> "אם אני מביא לך מפתח API, אתה יכול לייצא?"

---

## NP-06 — Marketing assets for Shaked Brand

> "מה הם הנכסים השיווקיים שצריכים להיות לשקד ברנד?"

---

## NP-07 — Instagram video strategy

> "אני רוצה להכין סדרת סרטונים אותנטיים לאינסטגרם, העליתי כבר אחד שבו אמרתי שאני עובד סוציאלי עסקי וזה ושידברו איתי, מה צריך להיות השורה התחתונה בסרטונים הבאים? בנה לי אסטרטגיה בבקשה על סמך מה שאני יודע לבנות ולהציע"

---

## NP-08 — Create a domain for deployed CRM

> "אבל לזה אני רוצה ליצור דומיין, לא?"

---

## NP-09 — Meaning and importance of maintenance

> "רגע, המיינטננס, מה המשמעות שלו? מה החשיבות שלו?"

---

## NP-10 — MECE layers for repo gaps

> "המיינטביליות, היא חלק מתוך קבוצת פערים? האם אלו כל השכבות שיש להסתכל עליהם? מוצר, הנדסי ותפעולי? זה שלוש השכבות שתופסות MECE את הנדבכים הקריטיים?"

## Run discipline

1. Freeze this file before either output family is written.
2. Produce baseline outputs first under a direct-answer instruction, without using the Question Discovery contract explicitly.
3. Freeze baseline outputs.
4. Produce challenger outputs using the Question Discovery contract.
5. Compare decision paths, not rhetorical quality.
6. Preserve `NO_REFRAME` as a valid and necessary output.
7. Do not use later historical outcomes as gold correctness; they may only be used after both outputs are frozen to inspect whether the reframe would have changed resource allocation.