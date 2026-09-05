# H2 Hebrew Reader Effect — Human Annotation Commissioning

Status: `READY_FOR_EXTERNAL_ANNOTATORS`

Purpose: obtain independent native-Hebrew recipient-effect gold without collapsing author emotion, speaker state, and reader effect.

## Annotator requirement

Use at least 3 native Hebrew readers per item for the first wave; 5 is preferred for items expected to be pragmatically ambiguous.

Annotators must not see Neta predictions, baseline predictions, candidate rule names, or expected failure families.

## Item presentation

For each item show only:
- Hebrew text;
- the preregistered context policy (`context_free`, `relationship_context`, or `dialogue_context`);
- minimal context required by that policy.

Do not explain what the item is supposed to evoke.

## Independent ratings

Rate separately:
- valence: -2..+2
- arousal: 0..4
- dominance/pressure: 0..4
- warmth: 0..4
- threat/tension: 0..4
- ambiguity/context dependence: 0..4
- likely pragmatic act: multi-label categorical
- short free-text: "What would this likely make you feel/expect as the recipient?"

Do not compute a composite score.

## Minimal-pair procedure

The seed contains 12 minimal pairs / 24 items. Randomize presentation order so pair membership is not obvious where practical.

After individual ratings are frozen:
- compute pairwise direction of change per dimension;
- record agreement/disagreement;
- mark high-ambiguity items rather than forcing consensus;
- preserve free-text disagreement when interpretations differ materially.

## Gold policy

Human gold is the distribution/consensus record, not one adjudicator's preferred interpretation.

A Neta failure may be called clean only when:
- the material reader-effect direction or pragmatic act has sufficient human agreement;
- Neta's output contradicts that agreement rather than merely choosing a minority plausible reading;
- the context supplied was sufficient for the human judgment.

## Separation from H1

H2 labels may not change H1 authority/action gold automatically.

Example: a phrase may feel pressuring to recipients while still leaving the product mechanism unresolved. Reader effect is evidence about recipient response, not automatic BUILD permission.

## First-wave minimum

- all 24 seed items independently annotated;
- at least 3 native Hebrew annotators per item;
- at least 8 minimal pairs with usable agreement on one or more recipient-effect dimensions;
- at least 4 deliberately high-ambiguity/context-sensitive items retained rather than discarded;
- Neta and baseline outputs frozen before human gold reveal for any item counted as HOLDOUT.

## Current blocker

`BLOCKED_ON_EXTERNAL_NATIVE_HEBREW_ANNOTATORS`

The model maintaining this repository must not manufacture synthetic annotations and call them independent human ground truth.
