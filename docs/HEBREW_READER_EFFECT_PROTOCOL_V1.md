# HEBREW READER-EFFECT PROTOCOL v1

## Purpose

Measure whether Neta can understand Hebrew affect and pragmatics without collapsing three different objects:

1. **expressed affect** — what emotion the text itself expresses;
2. **speaker-state inference** — what the reader infers about the speaker;
3. **reader effect** — what the utterance is likely to evoke in the recipient.

The benchmark exists to find clean judgment failures before any Hebrew-specific rule is promoted into Neta.

## Non-goal

This is not a generic Hebrew sentiment benchmark and not a fine-tuning dataset by default. Existing Hebrew resources already cover much of polarity, emotion classification and word-level affect. The unique target here is the missing pragmatic bridge from Hebrew wording to likely recipient effect.

## Evidence layers

### Layer A — lexical affect

Use open Hebrew affect resources as external reference data:

- Hebrew VAD Lexicon — valence/arousal/dominance at word level.
- hebnoRms / E-Millim-derived norms — valence/arousal over large Hebrew token vocabularies.

These resources are **not** reader-effect ground truth. They only constrain lexical affect claims.

### Layer B — sentence affect

Use manually annotated Hebrew sentence resources where available, especially the manually annotated VAD subset of the VAD Knesset Corpus and HebEMO.

These resources score expressed/evoked affect at sentence level but still do not establish recipient-specific pragmatic effect.

### Layer C — pragmatics

Use Hebrew pragmatics resources such as IronySet to test whether Neta distinguishes literal surface form from pragmatic meaning.

### Layer D — reader effect

Use a purpose-built minimal-pair corpus. Human annotators answer what they themselves would likely feel or infer as recipients, not what emotion the author "has".

## Separation rules

Every item belongs to exactly one corpus:

- `TRAIN`: may inform later failure analysis after adjudication.
- `HOLDOUT`: score-only until the wave is frozen and closed.
- `ADVERSARIAL`: deliberately constructed to make lexical sentiment misleading.

Never move an item from TRAIN to HOLDOUT after Neta has seen its gold label.

Never teach Neta from HOLDOUT before the wave closes.

## Minimal-pair design

Prefer pairs or small sets where propositional content is held approximately constant while pragmatic effect changes through one bounded feature:

- punctuation: `בסדר` / `בסדר.` / `בסדר...`;
- discourse marker: `בסדר` / `טוב, בסדר`;
- repetition: `כן` / `כן כן`;
- mitigation: `תשלח לי` / `רק תשלח לי`;
- distancing: `תעשה מה שאתה רוצה` / `תעשה מה שנראה לך`;
- authority: `צריך לסיים היום` / `אני צריך שתסיים היום`;
- irony/sarcasm;
- understatement;
- politeness markers;
- particles such as `דווקא`, `רק`, `כבר`, `נו`, `טוב`, `כאילו`;
- emoji and punctuation only when needed to isolate a pragmatic variable.

A pair is invalid if the edit changes the factual proposition enough that the reader effect can be explained without pragmatics.

## Annotation target

Annotators score the **recipient-facing effect** on separate dimensions. No composite score.

Required dimensions:

- `valence`: -2 very negative ... +2 very positive;
- `arousal`: 0 calm/low activation ... 4 highly activating;
- `dominance_pressure`: 0 no pressure/control ... 4 strong pressure/control;
- `warmth`: 0 cold/distancing ... 4 warm/affiliative;
- `threat_tension`: 0 none ... 4 strong interpersonal threat/tension;
- `ambiguity`: 0 clear pragmatic reading ... 4 highly context-dependent;
- `likely_pragmatic_act`: categorical, multi-label allowed;
- `free_effect`: short natural-language description of what the recipient may feel or infer.

Suggested pragmatic-act labels:

`literal_neutral`, `request`, `reminder`, `softened_request`, `pressure`, `withdrawal`, `dismissal`, `reassurance`, `affiliation`, `criticism`, `irony`, `sarcasm`, `threat`, `boundary_setting`, `deference`, `uncertain`.

## Context policy

Reader effect is conditional. Each item must declare one of:

- `context_free`: intended to be interpretable with minimal context;
- `relationship_context`: relationship supplied (peer / manager / partner / client / stranger);
- `dialogue_context`: one or two preceding turns supplied.

Do not adjudicate context-sensitive disagreement as model failure when `ambiguity` is high.

## Neta blind pass

For each item Neta must output:

- literal/propositional reading;
- expressed affect estimate;
- pragmatic reading(s);
- likely recipient effect by dimension;
- uncertainty / context dependence;
- one contrastive cue responsible for the difference in a minimal pair.

Neta may abstain when the text is genuinely underdetermined. Abstention is scored separately from error.

## Baseline

Run a general Hebrew-capable model on the same item and same context without this protocol's ontology. Freeze both outputs before revealing human labels.

## Adjudication

Classify each item or pair as:

- `SUPPORTED` — Neta captures the human-supported direction and pragmatic distinction;
- `PARTIALLY_SUPPORTED` — some dimensions/direction survive;
- `UNRESOLVED` — human disagreement/context dependence prevents clean adjudication;
- `REFUTED` — Neta confidently predicts the wrong direction or pragmatic act;
- `BASELINE_ADVANTAGE` — baseline materially outperforms Neta on the same evidence;
- `NETA_ADVANTAGE` — Neta materially outperforms baseline and survives adjudication.

A **clean Neta failure** requires a material wrong judgment with sufficient human agreement, not merely a label mismatch.

## Promotion discipline

Do not promote a Hebrew-specific rule because a pattern recurs.

A rule candidate requires all of:

1. a real judgment failure or repeated Neta-vs-baseline advantage;
2. the hidden judgment stated explicitly;
3. a neighboring case where the rule must not fire;
4. a falsifiable gate;
5. a deliberate positive control that turns the gate red;
6. success on unseen HOLDOUT items.

Otherwise retain the pattern as case memory only.

## Saturation dimensions

Track separately:

- lexical affect errors;
- sentence affect errors;
- pragmatic-act errors;
- reader-effect direction errors;
- context/ambiguity calibration errors;
- Hebrew-specific cue families;
- baseline decision deltas.

Do not collapse these into one composite score.

## Initial execution order

1. Register and pin external resources; do not copy gold labels into prompts.
2. Run a small sentence-level HOLDOUT using independently annotated Hebrew VAD material.
3. Run a pragmatics HOLDOUT using IronySet-compatible items.
4. Annotate the seed minimal-pair reader-effect corpus with multiple native Hebrew readers.
5. Only after adjudication, derive failure families and possible rule candidates.

## Contamination rule

The existing GitHub Benchmark Wave 1 remains frozen. This Hebrew observatory lives on a separate branch and may not change the Neta prompt or canonical rules while the GitHub HOLDOUT wave is open.
