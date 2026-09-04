# Hebrew Signal Fidelity — Hidden Holdout Policy

The benchmark must not publish unseen holdout text before the tested Neta version is frozen.

## Why

If Neta can read the examples, the benchmark stops measuring generalization and starts measuring recall/adaptation.

## Holdout creation

For each wave:

1. Freeze the exact Neta prompt/version/hash.
2. Freeze the evaluation schema and scorer.
3. Choose strata before authoring/sampling examples.
4. Author or sample holdout cases outside the tested repository context.
5. Record only case hashes, stratum counts and source provenance before scoring.
6. Run all three views where applicable: Hebrew raw, faithful English, professionalized English.
7. Adjudicate errors before any Neta update.
8. After the wave closes, archive the old holdout as historical evidence; never reuse it as unseen holdout.

## H1 target composition

Minimum 20 hidden cases:

- 3 metaphor / analogy
- 2 hedging / mitigation
- 2 hyperbole
- 2 negation / contrast
- 3 Hebrew-English code-switching
- 2 irony / pragmatic reading
- 2 affect-vs-mechanism
- 2 deixis / reference ambiguity
- 2 perceived-vs-system state

At least 8 of the 20 should combine two or more phenomena.

## External-control sampling

External datasets may contribute control items, subject to `SOURCES.json`.

Preferred first-wave control recipes:

- Hebrew Paraphrase gold: 30 pairs, stratified sentence/paragraph, used for formulation invariance only.
- HeQ: 20 context-dependent items, used for premature reference-resolution checks.
- HebNLI gold: reference-only unless licensing is clarified; if lawful external evaluation is possible, sample balanced entailment/neutral/contradiction pairs.
- IronySet: do not ingest until license is verified.

External controls do **not** count toward the 20 Neta-specific hidden cases unless they receive independent Neta annotations and remain unseen.

## Leakage rule

If any holdout text is exposed to the tested prompt/model before outputs are frozen, quarantine the affected cases and replace them. Do not relabel them as HOLDOUT after the fact.

## Promotion rule

No Hebrew-specific Neta rule may be promoted from TRAIN performance alone. A candidate must survive unseen holdout and include a counterexample where the rule must not fire.
