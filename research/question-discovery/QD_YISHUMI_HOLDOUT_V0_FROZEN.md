# Yishumi Holdout v0 — Frozen Corpus

Status: `HISTORICAL_HOLDOUT_FROZEN_BEFORE_GATE · MECHANICAL_SELECTION · RESEARCH_ONLY`
Date: 2026-09-06

Source: Google Sheet `יישומי`
Spreadsheet ID: `1A1pdaOYGSkfJCU8QjFl8ts8xoRQ6vcnwqUp_saPrVm4`
Sheet: `גיליון1`
Frozen Drive revision: `179`

## Mechanical selection rule

Take the first 20 rows in sheet order for which:
- column B is non-empty;
- column C is non-empty;
- skip only the literal table-header row `מטרה | פרומפט`.

No row is selected based on whether it looks favorable to the gate hypothesis.

## Selected rows

1. Row 1 — `ביקורת וצוות אדום` — premortem / hostile retrospective on project X.
2. Row 2 — `ביקורת וצוות אדום` — two-lens decision critique: logic vs emotion/culture.
3. Row 3 — `ביקורת וצוות אדום` — critique attention, coverage, coherence and sequencing.
4. Row 4 — `חשיפת כלי הDeveloper` — ask what Developer mode enables for connectors.
5. Row 5 — `יצירת הסבר מקיף על החומר` — generate the questions whose answers would build a comprehensive explanatory document.
6. Row 6 — `יצירת פרומפט לניתוח נתונים` — universal meta-prompt for generating data-analysis prompts with fixed structure and Precision Score.
7. Row 7 — `מחקר אידיאלי אינטגרטיבי` — reusable deep-research protocol for thought-leadership sources.
8. Row 8 — `מחקר על אווטאר [איש מדגמי מקהל היעד הרלוונטי]` — comprehensive avatar research template used for marketing decisions.
9. Row 9 — `מטא פרומפט` — nested prompt workflow for coordinating marketing experts/agents.
10. Row 10 — `מטא פרומפט לשיפור פרומפטים` — reusable multi-stage prompt-engineering protocol with gap maps, personas, decomposition, formal logic and QA.
11. Row 12 — `מצגת למידה` — reusable pedagogical interactive-HTML presentation prompt.
12. Row 13 — `נוסחה לאימון מודלים` — AAM total-loss formula and component explanation.
13. Row 14 — `סגנון כתיבה שלי` — stylometric DNA profile intended to guide writing behavior.
14. Row 15 — `פיתרון בעיות` — externalize problem X as a separate entity and analyze it.
15. Row 16 — `פרומפט לדיוק רעיונות של פוסטים` — ask what questions reveal the one-sentence core message.
16. Row 17 — `פרומפט להכנת תמונות יפות` — deep research + infer high-exposure VEO image techniques + produce and execute optimal image prompt.
17. Row 18 — `פרומפט להפקת רעיונות לפוסט בלינקדאין או בפייסבוק` — search viral/current stories and turn one into a viral LinkedIn post structure.
18. Row 19 — `פרומפט לחילוץ תובנות מסוכנים` — infer a prompt author's thinking/hidden rules from dialogue and reuse them in a personalized agent.
19. Row 20 — `פרומפט לניהול פרויקטים דיגיטלים` — teach a digital PM how to assemble scope/tasks/team.
20. Row 21 — `פרומפט לסקירת פרופיל בלינקדאין` — audit LinkedIn profile with composite score and generate an HTML strategic-roadmap slideshow.

## Evaluation question

For each row, freeze the front-door gate label before shadow R&D:
- `DIRECT_EARNED`
- `CHEAP_TEST`
- `FIXED_CONSTRAINT`
- `DOMAIN_HANDOFF`
- `NEEDS_CALIBRATION`

Then apply R&D v0.2 / Calibration Loop as shadow reference and adjudicate whether full calibration materially changes the next decision/work path.

This corpus is historical, not prospective. Its value is anti-cherry-picking: the prompts predate the current gate hypothesis and were selected mechanically from an external sheet.