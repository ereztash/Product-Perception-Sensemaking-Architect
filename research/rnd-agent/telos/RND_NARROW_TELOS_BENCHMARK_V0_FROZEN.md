# R&D Narrow Telos Scope Benchmark v0 — Frozen

Status: `FROZEN_BEFORE_NARROW_CLASSIFICATION · HISTORICAL_UNSEEN_RELATIVE_TO_TELOS_DERIVATION · RESEARCH_ONLY`
Date: 2026-09-06
Source: Google Sheet `יישומי`, spreadsheet id `1A1pdaOYGSkfJCU8QjFl8ts8xoRQ6vcnwqUp_saPrVm4`
Selection rule: rows 22–35 inclusive, excluding only row 33 because prompt column C is empty. These rows were not part of `QD_YISHUMI_HOLDOUT_V0` (which used the first 20 qualifying prompts through sheet row 21, excluding the internal header row).

## Tested hypothesis

Candidate narrowed telos:

> **R&D exists to reduce decision-controlling uncertainty enough to justify or reject the next consequential resource commitment, using the cheapest admissible learning move.**

### Frozen FIRE rule
R&D fires only when all are materially present:
1. a consequential commitment of time, money, build/research effort, attention, authority or reusable process is pending;
2. unresolved uncertainty could change whether/where/how much/in what form that commitment should occur;
3. resolving it requires a nontrivial choice among learning/evidence moves, or the proposed move itself is materially costly;
4. a cheaper admissible observation may exist before full commitment.

Otherwise `NO_FIRE` / direct / domain handoff / cheap test.

## Cases

| Case | Sheet row | Label | Frozen prompt signature |
|---|---:|---|---|
| NT-01 | 22 | פרומפט לשיפור פרומפטים | `אל תעשה את המשימה, תבנה את ההוראה.` |
| NT-02 | 23 | פרומפט לתמונות מפוסטים | Expert prompt-writing workflow for LinkedIn images: read post → infer message → perform comprehensive research on ways to convey it → choose method → write image prompt → execute/generate image. |
| NT-03 | 24 | פרומפט עבור סוכן מומחה גיוס | Reusable 11-part recruitment diagnosis protocol: analysis unit → one root hypothesis → 3–5 hypothesis tree → system map → decision map → experiments → edge cases → nonprofit risks → one optimal move → governor learning loop → fixed output rule. |
| NT-04 | 25 | שיפור תוצרים | `אני רוצה שתבצע מחקר על טכניקות של כתיבת פרומפטים, ותשתמש בטכניקות ... לטובת כתיבת הפרומפט שכתבתי - במטרה לקבל תוצר אידיאלי` |
| NT-05 | 26 | שיפור תוצרים | `הגבת מהר מדי. הפעל מצב Deep Think. אני דורש מינימום של 5 צעדים לוגיים לפני הגעה למסקנה.` |
| NT-06 | 27 | תיקון שגיאות במצגת HTML | `א. עליך לחשוב צעד אחר צעד, בתור מומחה QA לבעיות בקובץ HTML; ב. לתכנן תוכנית פעולה שתבטיח הימנעות מתקלות; ג. בצע.` |
| NT-07 | 28 | LLM יצירתי | Reusable autopoietic system constitution: success = persistence/system improvement; every output must synthesize rational-causal + ethical-axiomatic + systemic-adaptive axes; reflexive self-rewriting loops; ontology-break protocol; radical causal logging; begin. |
| NT-08 | 29 | LLM מסחרי | Reusable `Genesis 2.0` meta-system/trading agent: WFO/DSR/Occam quantitative rules, ethics-as-risk, fault tolerance/circuit breakers, human-machine dashboards, quant co-pilot + cognitive coach, fixed meta-trading heuristics, continual self-improvement. |
| NT-09 | 30 | מסגור מחדש | `אני רוצה שנתייחס לחסרונות האלה בגישה של "זה לא באג, זה פיצ'ר" ולהסביר למה` |
| NT-10 | 31 | פרומפט WSN | Reusable lightweight response scaffold: objective → facts-only + missing info → interpretation with 3 implications/probabilities/reversal → 3 actions with first step/success/risk → one recommendation. |
| NT-11 | 32 | GP-prompt | Reusable `Latent Space Navigator / Waze` protocol: 3–5 semantic anchors → DAG/critical path → avoid generic clusters → persona → self-check; output NAV-LOG + final answer. |
| NT-12 | 34 | שאלת שאלת מחקר | `אם הייתה לך גישה ל-Elicit, איזה פרומפט היית כותב שם כדי לקבל פרספקטיבה שיכולה להניב עבורך את האימפקט הרב ביותר עבור הפקת התובנות מהמקורות שיש לך?` |
| NT-13 | 35 | תתמצת ותשכנע | `כתוב מסמך המלצות מדויק ותמציתי: BLUF → הסיטואציה → ההשפעה/למה אכפת → מה עושים → למה דווקא את זה.` |

## Evaluation design

Order is locked:
1. classify all 13 using only the narrowed FIRE rule;
2. freeze those labels;
3. run broad R&D v0.2 contract as shadow reference against direct/domain execution;
4. adjudicate.

Reference question for broad v0.2:
> Would the full v0.2 calibration materially change the next work/decision path relative to direct execution, owner-set constraints, cheap test or domain handoff?

Metrics:
- `MATERIAL_CASE_RECALL`: among broad-R&D material cases, how many narrow FIRE catches;
- `FALSE_NO_FIRE`: narrow says NO_FIRE but broad R&D materially changes path;
- `FALSE_FIRE`: narrow fires but broad R&D adds no material delta;
- `NO_FIRE_SPECIFICITY`;
- `OVERALL_SCOPE_AGREEMENT`;
- failure-family analysis.

No prompt wording or FIRE rule may change before adjudication.