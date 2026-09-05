# Canonical Neta State

Last consolidated: 2026-09-05

## Canonical identity

Neta is an evidence-bounded Product Perception & Sensemaking method with an assurance layer. The current canonical method state is the **v0.2 assurance re-foundation**.

The canonical prompt remains the **frozen v0.1 baseline**. The GitHub benchmark did not earn a prompt edit.

This distinction is intentional:

- `method/version`: v0.2 assurance architecture;
- `prompt/baseline`: v0.1 frozen clean-model comparator;
- `evaluation`: empirical benchmark evidence may constrain claims about Neta but may not silently rewrite the prompt.

## Canonical evidence chain

`Evidence → Judgment → Rule Candidate → Gate → Version`

A result may move downstream only when its authority and reality floor permit it. Recurrence alone is not promotion.

## GitHub Benchmark Wave 1

Wave 1 is frozen and closed at BATCH-016 because routine broad sampling reached low marginal decision gain.

Frozen state:

- 48 adjudicated repositories;
- 16 HOLDOUT repositories;
- all four decision modes represented: BUILD_READY, DISCRIMINATE_FIRST, OWNER_DEFER, FIELD_STOP;
- 14 fully surviving Neta-vs-baseline decision deltas;
- 8 partially supported deltas;
- 1 clean Neta failure;
- 9 tracked failure families;
- 0 promoted new core rules;
- 0 prompt updates.

The wave **did not reach minimum viable evidence** because the preregistered decision threshold required at least 3 clean Neta failures and only 1 was observed.

The closure therefore means:

> the current broad GitHub sampling distribution is saturated for useful learning;

not:

> Neta has been proven reliable or has a low true failure rate.

The machine-readable closeout is `eval/github-benchmark/WAVE1_CLOSEOUT.json`.

## Branch authority

### `main`

Canonical released state. Only evidence, contracts, protocols, and changes that are ready to be treated as the repository's source of truth belong here.

### `neta/oss-observatory`

Historical execution branch for GitHub Benchmark Wave 1. After consolidation, it is not the canonical product version. New routine broad batches are paused unless a new sampling amendment is preregistered.

### `neta/hebrew-signal-fidelity`

Primary Hebrew decision-fidelity evaluation track. It asks whether natural Israeli Hebrew preserves uncertainty, inference boundaries, authority, and action across raw Hebrew, faithful translation, and professionalized paraphrase.

This is the closest Hebrew extension to Neta's core assurance thesis.

### `neta/hebrew-observatory`

Secondary Hebrew affect/pragmatics track. It distinguishes:

1. expressed affect;
2. inferred speaker state;
3. recipient/reader effect.

This track should not redefine the core Hebrew benchmark. It extends it where affect and pragmatics are decision-relevant.

### `neta/design-research-spine-v0.1`

Quarantined provenance/crosswalk layer for external design knowledge. It is research support, not a Neta version and not independent empirical validation.

## Hebrew consolidation decision

There are two non-equivalent Hebrew questions and they must remain distinct:

### Track H1 — Signal Fidelity

Core question:

> Does Neta preserve decision-relevant meaning, ambiguity, authority, and action when the input is natural Israeli Hebrew?

Primary failure families include metaphor laundering, mitigation erasure, hyperbole literalization, negation collapse, code-switch normalization, irony literalization, affect-to-mechanism laundering, deixis/context loss, perceived-state/system-state collapse, and professionalization drift.

### Track H2 — Reader Effect

Extension question:

> Can Neta distinguish what a Hebrew utterance says, what it implies about the speaker, and what it is likely to evoke in a recipient?

H2 may use lexical/sentence affect and pragmatics corpora as controls, but those labels do not become Neta ground truth for product decisions.

H1 and H2 must not be collapsed into one composite Hebrew-understanding score.

## Next authorized execution

1. Keep the canonical prompt frozen.
2. Merge/freeze the Hebrew Signal Fidelity protocol without treating TRAIN examples as validation.
3. Freeze a hidden Hebrew HOLDOUT only after the exact tested Neta prompt/hash, scorer, and strata are fixed.
4. Run Neta and a baseline on identical Hebrew evidence.
5. Adjudicate before any Hebrew-specific rule change.
6. Use H2 Reader Effect only as a separate diagnostic layer where recipient effect is material.

The next unit of progress is a **clean Hebrew judgment failure or surviving decision delta**, not additional corpus volume.
