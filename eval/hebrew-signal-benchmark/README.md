# Neta Hebrew Signal Fidelity Benchmark

This benchmark evaluates whether Neta preserves decision-relevant meaning and uncertainty when product signals arrive in natural Israeli Hebrew.

## What exists in v1

- `TRAIN_SEED_V1.jsonl` — 24 purpose-built TRAIN cases covering metaphor, hedging, hyperbole, negation, code-switching, irony, affect/mechanism separation, deixis, reference ambiguity, perceived-vs-system state, professionalization drift and RTL mixed-direction language.
- `SOURCES.json` — external Hebrew corpora registry with licensing/ingestion policy.
- `HOLDOUT_POLICY.md` — hidden holdout procedure.
- `../../schemas/hebrew-signal-case.schema.json` — case schema.
- `../../docs/HEBREW_SIGNAL_FIDELITY_PROTOCOL_V1.md` — benchmark protocol and promotion rules.
- `../../prompts/HEBREW_SIGNAL_EVAL.md` — structured evaluation prompt.
- `../../scripts/score_hebrew_signal_benchmark.py` — deterministic scorer for enum-level outcomes and language-view drift.

## Core design

Each Neta-specific case holds three views:

1. raw Hebrew;
2. faithful English translation;
3. deliberately professionalized English paraphrase.

The third view is a perturbation, **not** gold. It tests whether professional language launders uncertainty into a stronger design claim.

## External corpora

External datasets are used only as controls/adapters for their original strengths:

- Hebrew Paraphrase Dataset → semantic preservation.
- HebNLI → inference/contradiction boundary.
- HeQ → context/deixis/reference resolution.
- IronySet → pragmatics/irony, only after license verification.
- CoSIH / MaTaCOp → natural spoken Hebrew, research-only/manual-access lanes.

No external corpus label is silently reinterpreted as a Neta authority/action label.

## Wave H1

Minimum decision evidence before changing Neta's core prompt:

- 60 adjudicated Hebrew cases;
- 8+ phenomena;
- 20 hidden holdout cases;
- 15+ three-view triplets;
- 3 clean Neta failures;
- 3 professionalization-resistance wins;
- one counterexample per candidate Hebrew-specific rule.

Current seed status: **24 TRAIN cases; 0 hidden HOLDOUT exposed in repo.**

## Intended metrics

Keep separate:

- authority accuracy;
- action accuracy;
- ambiguity accuracy;
- mechanism-status accuracy;
- Hebrew ↔ faithful-English authority flip rate;
- Hebrew ↔ faithful-English action flip rate;
- professionalization drift rate;
- critical overreach count.

Do not create a single composite score.
