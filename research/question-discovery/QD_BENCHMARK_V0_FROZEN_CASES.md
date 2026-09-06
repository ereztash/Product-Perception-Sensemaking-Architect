# Question Discovery Benchmark v0 — Frozen Cases

Status: `FROZEN_BEFORE_RUN · RESEARCH_ONLY · NOT_CANONICAL`
Date: 2026-09-06
Parent hypothesis: `research/question-discovery/SESSION_2026-09-06_QUESTION_REFRAMING_LINEAGE.md`

## Hypothesis under test

A bounded Question Discovery capability can take a user's current question and identify a more decision-relevant question **when one exists**, while leaving already decision-grade questions alone.

Candidate transformation:

```text
USER'S CURRENT QUESTION
→ UNDERLYING DECISION
→ HIDDEN ASSUMPTIONS / PREMATURE OBJECTS
→ NEIGHBORING QUESTION SPACE
→ MOST DECISION-CHANGING QUESTION
→ CHEAPEST ADMISSIBLE WAY TO RESOLVE IT
```

## Critical anti-goal

A reformulation is not a success merely because it sounds deeper, more strategic, more professional, or more abstract.

Over-reframing an already adequate question is harm.

## Scoring rubric — frozen before outputs

For each case record these dimensions separately.

### `UNDERLYING_DECISION_FOUND`
Did the run identify the actual decision/use behind the surface question rather than merely restate the topic?

### `PREMATURE_OBJECT_EXPOSED`
Did it expose a hidden assumption, proposed mechanism, proxy, job title, tool, metric, or solution that the original question treated as settled too early?

This dimension may legitimately be `NO` when the original question contains no such defect.

### `QUESTION_DELTA`
Did the proposed question materially change at least one of:
- evidence to collect;
- option set;
- resource/authority to invoke;
- BUILD / DEFER / STOP / ACT decision;
- reversal condition;
- object being decided.

Cleaner wording alone does not count.

### `CHEAP_DISCRIMINATOR`
Did the run identify a bounded next observation/calculation/test that could resolve the improved question without unnecessary research?

### `NO_OVERREFRAME`
For neighboring controls, did the capability recognize that the current question was already decision-grade and avoid manufacturing a deeper problem?

### `HARM`
Record `YES` if the reformulation:
- replaces a concrete decision with vague strategy language;
- adds unnecessary research;
- changes the user's objective without authority;
- hides a straightforward calculation/action behind abstraction;
- invents uncertainty that does not matter to the decision.

## Case classes

- QD-01 through QD-08: challenge cases. No gold reformulation is frozen.
- QD-09 and QD-10: neighboring controls where the current question is intentionally close to decision-grade. Expected behavior is `NO_REFRAME` unless a genuinely material missing distinction is found.

The scorer must not reward a reframe on controls merely for being plausible.

---

## QD-01 — Architecture mechanism proposed early

> אנחנו בונים SaaS קטן שעוד לא הושק. כרגע יש backend אחד ו-database אחד. אני רואה המון חומר על microservices וחושש שאם נצמח נצטרך לשכתב הכל. האם כדאי לעבור למיקרו-סרביסים לפני ההשקה?

---

## QD-02 — Price mechanism proposed from objection signal

> בשלוש שיחות מכירה השבוע אמרו לי שהמחיר גבוה. האם כדאי להוריד את המחיר ב-20% כדי לשפר את אחוזי הסגירה?

---

## QD-03 — Content frequency proposed from weak outcome

> אני מפרסם בלינקדאין בערך פעמיים בשבוע וכמעט לא מגיעות פניות. האם כדאי להתחיל לפרסם כל יום?

---

## QD-04 — Hiring proposed from sales overload

> אני עושה הרבה שיחות מכירה, מרגיש עמוס, ועדיין לא סוגר מספיק. האם הגיע הזמן לגייס איש מכירות?

---

## QD-05 — Mobile app proposed from user requests

> כמה לקוחות ביקשו שיהיה לנו גם אפליקציה לנייד. האם הגיע הזמן לבנות אפליקציית iOS ואנדרואיד?

---

## QD-06 — More data proposed from statistical uncertainty

> הרצתי ניסוי וקיבלתי אפקט קטן בכיוון שרציתי, אבל רווח הסמך רחב וחוצה אפס. האם פשוט לאסוף עוד 500 תצפיות?

---

## QD-07 — Tool migration proposed from workflow pain

> הצוות מתלונן שה-CRM הנוכחי מעיק ומבזבז זמן. האם כדאי לעבור ל-HubSpot?

---

## QD-08 — Curriculum proposed from capability goal

> אני רוצה לדעת לבנות מערכות שיכולות לגדול בלי לקרוס. כולם אומרים ש-Kubernetes הוא בסיס חשוב. האם כדאי לי ללמוד Kubernetes עכשיו?

---

## QD-09 — Neighboring control: bounded cost comparison

> יש לי שתי הצעות ספק לאותו שירות. ספק A גובה 4,000 ₪ הקמה ועוד 1,200 ₪ בחודש. ספק B בלי הקמה וגובה 1,650 ₪ בחודש. אין עלויות נוספות והצורך הוא ל-12 חודשים בדיוק. איזו הצעה זולה יותר בשנה הראשונה ובכמה?

Expected control behavior: answer the bounded calculation; do not replace it with a broader vendor-strategy question unless a material missing fact is identified.

---

## QD-10 — Neighboring control: bounded reversible incident decision

> העלינו גרסה ב-14:00. בתוך חמש דקות שיעור שגיאות ה-checkout עלה מ-0.8% ל-6%. לא היה שום deploy אחר, ויש rollback אוטומטי לגרסה הקודמת שלוקח פחות משתי דקות. האם להחזיר עכשיו לגרסה הקודמת?

Expected control behavior: preserve the urgent bounded decision. Do not delay a cheap reversible rollback by manufacturing a broad root-cause research program.

## Run discipline

1. Freeze this file before generating any case outputs.
2. Run the same Question Discovery contract on all 10 cases.
3. Record the proposed decision question and cheapest discriminator before scoring.
4. Score each case against the frozen rubric.
5. Preserve failures; do not rewrite the prompt or rubric mid-run.
6. This is a single-model/manual research run unless an independent runner is later executed. It is not evidence of cross-model generalization.
