# Architecture historical benchmark v0

Status: `VISIBLE_TRAIN_CORPUS_FROZEN`

Purpose: test whether `ARCHITECTURE_DECISION_DISCRIMINATOR_V0` adds material architecture-specific decision value before an autonomous Architecture Agent is built.

## Corpus

- `HISTORICAL_CASES_V0.jsonl` — runner-visible frozen inputs only.
- `HISTORICAL_GOLD_V0.jsonl` — adjudication anchors revealed only after baseline/candidate outputs are frozen.
- 12 cases across 4 repositories.

This is a visible retrospective TRAIN corpus, not an unseen HOLDOUT.

## Critical evidence limit

The historical commit records what was ultimately implemented and why. It does **not** prove that implementation was optimal. Agreement with the historical resolution is therefore not the score.

The benchmark asks whether the candidate surfaced a material architecture distinction that would have improved the live decision compared with the baseline resources.

## Run protocol

For each case:

1. expose only the matching row from `HISTORICAL_CASES_V0.jsonl`;
2. run baseline resources without the Architecture Decision Discriminator;
3. freeze the baseline output;
4. run the candidate discriminator independently on the same frozen input;
5. freeze the candidate output;
6. only then reveal the matching historical adjudication row;
7. adjudicate decision-relevant delta.

Do not let either runner inspect source commits during steps 2-5. The commit SHA is provenance for the adjudicator, not permission to recover the answer.

## Delta dimensions

Record separately; no composite score is required:

- `BOUNDARY_DELTA` — did the candidate identify a materially better component/state/authority boundary?
- `AUTHORITY_DELTA` — did it prevent repo/runtime/owner/field authority laundering?
- `OPTION_DELTA` — did it add/remove an option that changes the decision?
- `DISCRIMINATOR_DELTA` — did it identify a cheaper fact that would discriminate alternatives?
- `MIGRATION_DELTA` — did it expose change propagation, rollback or transitional risk the baseline missed?
- `ANTI_BUILD_DELTA` — did it avoid an unnecessary new component/agent/abstraction?
- `HARM` — did architecture framing introduce unjustified structure, doctrine or confidence?

## Promotion rule

Visible historical wins are insufficient for agent promotion. After this corpus:

1. create unseen HOLDOUT cases after the candidate contract is frozen;
2. compare against the same baseline resources;
3. require repeated material delta across more than one architecture family;
4. include neighbor cases where architecture reasoning should *not* fire;
5. only then consider an autonomous Architecture Agent boundary.

If the candidate mostly produces cleaner explanations of decisions the baseline already reaches, keep architecture as a borrowed Scaffold/resource capability.
