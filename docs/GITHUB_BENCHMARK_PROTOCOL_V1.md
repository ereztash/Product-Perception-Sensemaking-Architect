# GITHUB BENCHMARK PROTOCOL v1

## Purpose

Test whether Neta generalizes beyond Erez's portfolio and whether her assurance discipline creates marginal decision value over a normal product/code review.

The benchmark does **not** ask whether Neta can generate more findings. It asks whether she can keep claims, authority and action proportionate to reality across unfamiliar products.

Primary thesis under test:

> Neta can distinguish BUILD / DISCRIMINATE / OWNER / FIELD / STOP decisions on unfamiliar products while reducing false-build recommendations and authority laundering.

This protocol inherits the canonical grammar in `docs/REALITY_AUTHORITY_PERMISSION.md` and the scoring rules in `eval/RUBRIC.md`.

## Unit of analysis

One `repo-case` = one public repository at one pinned commit SHA, reviewed under one frozen evidence boundary.

A later review of the same repository at a different SHA is a new case.

## Eligibility

Include repositories that:

- are public and accessible;
- contain a user-facing product surface or interaction path;
- have meaningful product code, not only a library, template, awesome-list or paper;
- have activity in the previous 12 months;
- have enough repository evidence to identify at least one material product question;
- are not owned by Erez and were not used to design Neta.

Do not exclude a repository merely because it is old-looking, small, lightly tested or commercially weak. Those are properties of the population, not reasons to curate the answer.

## Sampling

Sampling is stratified so the benchmark does not become a TypeScript-SaaS benchmark by accident.

Target strata:

1. web application / SaaS-like product;
2. desktop/native application;
3. mobile application;
4. developer tool with an interactive surface;
5. dashboard / analytics / admin product;
6. knowledge / education / productivity product.

Within each stratum, prefer repositories surfaced by a reproducible GitHub query and pin the exact result plus commit SHA in the batch manifest.

Stars may be used as a sampling band, never as quality ground truth.

## Corpus separation

Every case belongs to exactly one corpus:

- `TRAIN`: adjudicated cases may later inform Neta's failure lineage.
- `HOLDOUT`: results may score Neta but may not be used to modify rules until the holdout wave is frozen and scored.
- `ADVERSARIAL`: intentionally misleading cases, e.g. polished UI with weak state logic, large test suites with weak gates, or simple products with complex repositories.

A repository may not move from TRAIN into HOLDOUT after Neta has seen its adjudication evidence.

## Reality caveat

This benchmark can be source-blind but cannot guarantee model-naivety. A model may have prior exposure to a public repository. Therefore every case records `prior_exposure_risk` and no claim of double blindness is allowed.

## Evidence phases

### Phase A — Selection freeze

Record before review:

- repository;
- pinned SHA;
- sampling query / stratum;
- corpus assignment;
- known deployment URL if discovered from repository metadata only;
- prior-exposure risk.

Do not read issues, discussions, support forums, PR commentary, reviews or bug reports yet.

### Phase B — Blind Neta pass

Allowed evidence:

- repository metadata;
- README/product docs needed to understand intended use;
- product source;
- tests;
- static assets/screenshots stored in the repository;
- deployment only when directly discoverable and actually operable.

Forbidden during this phase:

- GitHub issues;
- discussions;
- release notes used as bug history;
- support forums;
- external reviews;
- closed PRs whose purpose reveals a historical defect;
- searching the web for complaints.

Neta outputs material questions only. Each question must carry:

- raw signal or bounded observation;
- claim decomposition;
- observed reality level;
- required reality floor;
- resolution authority;
- requested use;
- permission;
- one next move;
- reversal condition.

Maximum: 3 material findings per repository. A repository with zero justified findings is a valid result.

### Phase C — Baseline reviewer

Run a general product/code reviewer on the **same Phase B evidence boundary** without Neta's assurance grammar.

Capture its recommendations before revealing ground truth.

The baseline is not scored on writing quality. It exists only to estimate Neta's marginal effect on decision quality and build restraint.

### Phase D — Ground-truth reveal

Only after both outputs are frozen, inspect independent evidence where available:

- issue reports;
- maintainers' confirmed bugs;
- merged PRs that repair the mechanism;
- changelog/release entries;
- reproducible tests/fixtures added after a reported defect;
- public user reports;
- deployment behavior;
- explicit maintainer product intent.

Ground truth is claim-specific. An issue that says "confusing" does not prove Neta's mechanism. A code fix does not prove user value.

Each finding becomes one of:

- `CONFIRMED_LOCAL` — independent evidence supports the local observation/mechanism;
- `PARTIALLY_SUPPORTED` — some but not all of the claim survives;
- `UNRESOLVED` — no admissible independent evidence closes it;
- `REFUTED` — independent evidence contradicts it;
- `AUTHORITY_CORRECT_STOP` — Neta correctly routed the question outside the available authority.

### Phase E — Adjudication

Score the frozen Neta output against `eval/RUBRIC.md` and record critical failures.

Never change the rubric to rescue a favored output.

## Benchmark vector — no composite score

These dimensions remain separate because they measure different failure modes.

### 1. Surviving Finding Precision (SFP)

`confirmed_local + partially_supported / adjudicated local findings`

Report numerator and denominator. Do not report when denominator < 5.

### 2. False-Build Rate (FBR)

Among Neta recommendations with `ALLOW` for build/change, the fraction later refuted or shown to require a different authority.

Lower is better.

### 3. Build-Restraint Precision (BRP)

Among cases where Neta denied/deferred a build while the baseline recommended building, the fraction where adjudication supports Neta's restraint.

This tests the distinctive anti-backlog claim.

### 4. False-Stop Rate (FSR)

Among `FIELD_STOP`, `OWNER`, or equivalent routed stops, the fraction where admissible repository/environment evidence actually could have resolved the material question.

Lower is better. Neta must not earn restraint by stopping too early.

### 5. Authority Accuracy (AA)

Fraction of adjudicated material questions assigned to the authority that could actually resolve them.

Record disagreements by authority pair, e.g. `REPO→FIELD`, not only a percentage.

### 6. Critical Failure Count

Count CF1–CF12 from `eval/RUBRIC.md`. Any critical failure fails that case regardless of other metrics.

### 7. Decision Delta vs baseline

For each case, classify Neta's effect relative to baseline:

- prevented unjustified build;
- found justified build baseline missed;
- chose a cheaper discriminator;
- routed to correct authority;
- no material difference;
- worse than baseline.

### 8. Generalization coverage

Report results separately by stratum and implementation family. Do not average away a domain-specific collapse.

## What this benchmark may not claim

Even strong results do not establish that:

- Neta improves conversion, retention or revenue;
- Neta produces better user experience in the field;
- Neta is better than a named human expert;
- a repository issue corpus is complete ground truth;
- absence of an issue means a finding is false.

Those remain separate FIELD/RESEARCH questions.

## Pilot and waves

### Pilot — 20 repos

Purpose: validate the benchmark instrument itself. Results may identify schema/rubric defects but may not be marketed as a final generalization estimate.

Stop and repair the protocol if:

- >20% of selected repos turn out not to contain an eligible product surface;
- adjudication cannot distinguish local confirmation from field claims in >20% of findings;
- baseline and Neta receive materially different evidence;
- corpus leakage is discovered;
- a metric rewards indiscriminate stopping or indiscriminate building.

### Wave 1 — 100 repos

Freeze Neta version, rubric, schema and sampling rules before the first HOLDOUT case.

Do not update Neta from HOLDOUT evidence until all 100 cases are frozen and scored.

## Continuous observatory rule

Continuous execution occurs in bounded batches, not an unbounded stream of prose.

Each batch:

1. selects 3 previously unseen eligible repositories;
2. pins SHAs and corpus assignments;
3. completes Phases B–E;
4. writes machine-readable case files;
5. updates only aggregate counters allowed for the current corpus;
6. never teaches Neta from HOLDOUT until the wave closes.

The unit of progress is adjudicated uncertainty removed, not repository count.

## Stop conditions for the observatory

Pause new sampling when any of these becomes true:

- benchmark schema or rubric changes materially;
- corpus leakage is suspected;
- >2 consecutive batches have >50% ineligible selections;
- critical-failure rate rises above 10% over the latest 20 adjudicated cases;
- adjudication backlog exceeds 2 completed batches;
- a new Neta version is introduced before the current holdout wave is frozen.

Resume only after the cause is documented.
