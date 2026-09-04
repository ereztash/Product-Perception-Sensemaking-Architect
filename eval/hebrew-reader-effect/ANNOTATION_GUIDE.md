# Hebrew Reader-Effect Annotation Guide v1

## What you are judging

Judge the effect of the message **on you as the recipient in the supplied context**.

Do not answer:

- what emotion the writer probably has;
- whether the sentence is grammatically good;
- whether you agree with the content;
- what the dictionary meaning of the words is.

Answer: **If this message were sent to you in this context, what interpersonal effect would it create?**

## Procedure

1. Show one item at a time in randomized order.
2. Do not show pair IDs or the contrasting sentence.
3. Keep the supplied relationship/dialogue context exactly as written.
4. Each item should receive at least 3 independent native/near-native Hebrew judgments before adjudication; prefer 5 for ambiguous items.
5. Annotators must not discuss items before submitting.
6. Store raw judgments. Never overwrite disagreement with a single "clean" label.

## Scales

### Valence

- `-2` strongly unpleasant/negative effect
- `-1` somewhat unpleasant/negative
- `0` neutral/mixed
- `+1` somewhat pleasant/positive
- `+2` strongly pleasant/positive

### Arousal

- `0` calm / little activation
- `1` low
- `2` moderate
- `3` high
- `4` very high activation

### Dominance / pressure

How much pressure, control or demand does the message place on you?

`0` none → `4` very strong

### Warmth

How affiliative, caring or socially warm does it feel?

`0` cold/distancing → `4` very warm

### Threat / tension

How much interpersonal threat, conflict or tension does it create?

`0` none → `4` strong

### Ambiguity

How dependent is your reading on missing tone/context?

`0` clear → `4` highly ambiguous

## Pragmatic act

Choose one or more only when they fit:

- `literal_neutral`
- `request`
- `reminder`
- `softened_request`
- `pressure`
- `withdrawal`
- `dismissal`
- `reassurance`
- `affiliation`
- `criticism`
- `irony`
- `sarcasm`
- `threat`
- `boundary_setting`
- `deference`
- `uncertain`

## Free response

Finish this sentence in one short phrase:

> "If I received this, I might feel/infer..."

Do not explain literary interpretation. Record the immediate interpersonal effect.

## Pair adjudication

After individual labels are frozen, compare items within each minimal-pair group.

A pair is useful when:

- the propositional content is materially stable;
- annotators show a directional effect on at least one reader-effect dimension;
- the direction is not explained solely by changed factual content.

A pair should be marked `UNRESOLVED` rather than forced when:

- disagreement is high;
- context is insufficient;
- the purported pragmatic cue does not reliably move judgments.

## Gold construction

Gold is a distribution, not a single emotion word.

Store:

- number of annotators;
- per-dimension central tendency;
- dispersion/agreement;
- pragmatic-act frequencies;
- short summary of common free-effect descriptions.

Do not create a composite score.

## Model scoring rule

Neta is not wrong merely because it uses a neighboring emotion word. A material error requires one of:

- wrong direction on a reader-effect dimension with adequate human agreement;
- confidently missing the contrast between paired items;
- inventing a pragmatic act contradicted by the judgments;
- failing to represent genuine ambiguity when human judgments are split.

This keeps the benchmark about judgment, not label matching.
