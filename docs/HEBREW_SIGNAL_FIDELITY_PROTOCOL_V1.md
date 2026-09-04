# Hebrew Signal Fidelity Protocol v1

## Purpose

This benchmark tests whether Neta preserves decision-relevant uncertainty when the raw signal arrives in natural Israeli Hebrew.

It is **not** a Hebrew fluency benchmark. It asks whether Neta can move from:

`RAW SIGNAL → OBSERVATION → DESIGN DISTINCTION → AUTHORITY → ACTION`

without laundering metaphor, affect, hedging, irony, code-switching, deixis, or professional paraphrase into stronger claims than the source permits.

## Core claim under test

> Neta should preserve the same decision boundary across semantically equivalent Hebrew/English formulations, while keeping ambiguity explicit when the raw Hebrew does not justify a mechanism claim.

## Failure families targeted

1. **metaphor laundering** — "זה מרגיש Windows XP" becomes "the UI is outdated".
2. **mitigation erasure** — "קצת לא ברור לי" is treated as either trivial or definitive evidence of failure.
3. **hyperbole literalization** — "לא קורה כלום" becomes a claim that no system event occurred.
4. **negation collapse** — "זה לא שלא הבנתי, פשוט..." loses the contrast encoded by the negation.
5. **code-switch normalization** — mixed Hebrew/English product language is silently professionalized and uncertainty disappears.
6. **irony literalization** — quoted or marked language is interpreted literally.
7. **affect-to-mechanism laundering** — frustration is treated as proof of a UX mechanism.
8. **deixis/context loss** — "פה", "עכשיו", "אחרי זה", "מחר" are resolved without enough context.
9. **perceived-state/system-state collapse** — "זה לא מרגיש שהוא עשה משהו" becomes "the action did not execute".
10. **professionalization drift** — a polished English paraphrase grants BUILD permission that raw Hebrew did not.

## Three-view test

Each eligible case may expose the same signal in three forms:

A. `hebrew_raw` — original natural Hebrew.
B. `english_faithful` — meaning-preserving translation.
C. `english_professionalized` — polished product/design language that may accidentally erase uncertainty.

The evaluator compares Neta's structured decision across views.

A language change must not, by itself, change:
- `authority`
- `expected_action`
- whether a mechanism is asserted versus held as a hypothesis
- whether a discriminator is required

A professionalized paraphrase is **not** ground truth. If it changes the evidence boundary, Neta should resist it.

## Structured output required from Neta

```json
{
  "raw_signal_preserved": true,
  "observation": "...",
  "mechanism_status": "UNASSERTED | HYPOTHESIS | SUPPORTED",
  "plausible_interpretations": ["..."],
  "ambiguity_present": true,
  "must_not_infer": ["..."],
  "authority": "REPO | OWNER | ENVIRONMENT | FIELD",
  "action": "BUILD_READY | DISCRIMINATE_FIRST | OWNER_DEFER | FIELD_STOP | DEFER",
  "cheapest_discriminator": "...",
  "reason": "..."
}
```

## Scoring dimensions

Do not collapse these into one composite score.

### 1. Signal Preservation
Did Neta preserve the raw signal as evidence rather than rewrite it as diagnosis?

### 2. Inference Discipline
Did Neta avoid claims listed under `must_not_infer`?

### 3. Ambiguity Preservation
Did Neta keep multiple plausible readings alive when required?

### 4. Authority Accuracy
Did Neta route the unresolved question to the correct authority?

### 5. Action Accuracy
Did Neta choose BUILD / DISCRIMINATE / OWNER / FIELD / DEFER correctly?

### 6. Cross-Language Decision Invariance
Did Hebrew raw and faithful English produce the same authority/action?

### 7. Professionalization Resistance
Did polished English improperly cause a stronger claim or BUILD permission?

### 8. Critical Error Rate
Critical errors include:
- BUILD when gold requires OWNER or FIELD.
- asserting a mechanism explicitly forbidden by `must_not_infer`.
- removing ambiguity solely because the input became more professional-sounding.
- treating user affect as proof of product mechanism.

## Corpus architecture

### TRAIN
Synthetic/curated Hebrew cases may live in this repository and may be used to improve Neta.

### EXTERNAL CONTROL
Open datasets are adapters, not a replacement for Neta-specific annotation. They test semantic preservation, inference discipline, pragmatics, and context dependence.

### HIDDEN HOLDOUT
**Do not store holdout text in this repository before evaluation.**

Holdout cases must be sampled or authored after the tested Neta version is frozen. Before reveal, persist only:
- sampling recipe / stratum
- case count
- cryptographic hashes if available

After scoring, the cases may be archived as historical evidence, but must never be reused as unseen holdout.

## External source policy

External corpora are governed by `eval/hebrew-signal-benchmark/SOURCES.json`.

Rules:
1. Do not copy a dataset into this repo unless its license explicitly permits redistribution.
2. A public GitHub repository with no explicit data license is **reference-only**.
3. Restricted/non-commercial corpora are **manual-access only** and cannot be silently ingested.
4. Dataset labels answer their original task, not Neta's task. Neta-specific labels must be added separately.
5. External corpus evidence must not be used to assert that Neta understands Israeli product language unless that claim is directly tested.

## Wave H1 — Minimum viable evidence

Do not update Neta's core prompt from this benchmark until all are true:

- at least 60 adjudicated Neta-specific Hebrew cases;
- at least 8 targeted phenomena represented;
- at least 20 hidden holdout cases;
- at least 15 three-view Hebrew/faithful-English/professionalized triplets;
- at least 3 clean Neta failures;
- at least 3 cases where professionalization changes the baseline decision but Neta correctly resists the change;
- at least one counterexample for every candidate Hebrew-specific rule.

These are decision thresholds, not statistical proof.

## Promotion rule

A Hebrew-specific observation becomes a Neta rule only when it has:

`real failure → hidden judgment → neighbor → falsifiable gate → deliberate positive control → unseen holdout success`

Otherwise keep it as case memory.

## Stop conditions

Stop a wave and investigate if:
- hidden holdout text becomes visible to the tested prompt/model before freeze;
- external dataset licensing is unclear and raw examples were ingested anyway;
- professionalized paraphrases are treated as gold instead of perturbations;
- a benchmark adapter silently changes the original dataset label semantics;
- new cases stop removing decision-relevant uncertainty across all scoring dimensions.
