# Instrument Portfolio Extraction — 2026-09-05

**Status:** `QUARANTINED_EVIDENCE_IMPORT`

**Authority:** this file is a research artifact only. It does **not** modify `docs/METHOD.md`, `docs/AUTHORITY_MAP.md`, `research/PROMOTION_PROTOCOL.md`, `prompts/SYSTEM.md`, any Wave 1 status, or any Neta behavior.

**Provenance note:** this artifact imports a prior cross-repository extraction performed over the owner's adjacent working repositories and historical research artifacts. The underlying source repositories were **not re-audited in this commit**. Counts, file state and runnability therefore describe the inspected snapshots from that extraction and must be revalidated before any current-state claim or intervention.

---

## 0. Why this belongs in Neta

Neta's current research quarantine contains external research and promotion machinery, but the owner also has a large pre-existing portfolio of executable research instruments outside this repository.

The material question is not whether those instruments are "good". It is:

> What research capability has already been built, what kinds of uncertainty can it discriminate, what evidence does it actually leave behind, and what portfolio-level failure modes should Neta be able to notice before proposing yet another instrument?

This import exists so that future Neta work does not treat that portfolio as invisible and rebuild already-paid-for research machinery from memory.

### Requested use

`HYPOTHESIZE` / `DISCRIMINATE` only.

### Explicitly denied uses

This file alone may not:

- promote a Neta rule;
- change the frozen prompt;
- establish that any instrument is currently runnable;
- establish that any reported historical metric remains valid;
- treat agreement among self-built instruments as independent corroboration;
- infer FIELD outcomes from repository artifacts;
- create a universal "instrument portfolio management" doctrine.

---

# 1. Extraction-level observations

The prior extraction found a large, heterogeneous research portfolio distributed across multiple owner repositories rather than a single research registry.

At the inspected snapshots:

- `LinkedIn-Daily` contained **81 root Python files**; **63 were inspected in the extraction**, with 18 deliberately skipped under a held-out-data rule.
- The CRM analytics tree contained roughly **93 measurement/analytics modules** plus around **180 research-result artifacts** under its research-data area.
- Only about **14 instruments** appeared to bear directly on an explicit graph claim at the time of the crosswalk.
- In `LinkedIn-Daily`, **30/81** Python files wrote a durable artifact while **51/81** wrote only to stdout.
- **14** files wrote to a temporary/scratchpad path whose output could disappear with a session or machine cleanup.
- Several research chains had strong methodological machinery but weak evidence deposition: the instrument ran, but the decisive result was not durably written into the graph/ledger.
- A preregistration-calibration snapshot reported `locked_rows=902 · scored=0 · debt=902`: strong pre-event locking capacity with essentially no downstream scoring closure at that snapshot.

These are observations about the inspected portfolio state, not claims about current state.

---

# 2. Instrument families extracted from `LinkedIn-Daily`

## 2.1 Measurement substrate / ground truth

Observed instruments and support code included:

- `content_events.py` — append-only event spine.
- `ingest_export.py` — ingest of real content-performance data.
- `labeled_corpus.py` — joins post text with observed performance.
- `build_corpus.py` — corpus construction.
- `build_real_labels.py` — real impression/engagement labels.
- `draft_body.py` — extracts the measurement unit from a draft.
- `_qa_hook.py` — automatic post-write QA observation.
- `_stop_hook.py` — stop-time/staleness observation.
- `to_xlsx.py`.
- `inspect_xlsx.py`.
- `probe_engagement.py`.

Research function: create a durable measurement substrate and label spine rather than relying on narrative memory.

## 2.2 Text → engagement / performance experiments

Observed chain:

- `analyze_features.py`
- `scorecard.py`
- `scorecard_real.py`
- `lexsem_analysis.py`
- `lexsem_composite.py`
- `logreg_semantic.py`
- `master_features.py`
- `nb_model.py`
- `verify_predict.py`
- `verify_attack.py`
- `portfolio.py`
- `extract_posts.py`
- `extract_posts2.py`
- `hook_board.py`
- `hook_features.py`

Important lineage relationships from the extraction:

- `verify_attack` was the adversarial successor to `verify_predict`.
- `scorecard_real` superseded the hand-lexicon logic in `scorecard`; both were subsequently absorbed by `master_features.py`.
- `lexsem_composite` was described as the logical final test of its chain, yet its decisive result was not durably deposited.

Research function: feature validity, model/null comparison, adversarial re-check, specification alternatives, portfolio-level pattern analysis.

## 2.3 Timing instruments

Observed:

- `timing_analysis.py`
- `hour_analysis.py`
- `arima_check.py`
- `skeptic_hour.py`
- `skeptic_hour2.py`
- `skeptic_hour3.py`
- `dm_hour_analysis.py`

The chain is valuable as a **negative-result family**. The historical timing hypothesis was later retired after the apparent hour effect was identified as proxy-driven; `skeptic_hour3` functioned as a power/sensitivity kill test.

Research function: time effects, autocorrelation checks, specification sensitivity, power simulation, retirement of a hypothesis when the proxy collapses.

## 2.4 Prospective experiments / time curves

Observed:

- `experiment.py`
- `booster_spillover.py`
- `booster_experiment.py`
- `decay_curve.py`

Research function: pre-event assignment, locked experiments, bootstrap readout, time-decay representation.

## 2.5 ICP / network filtering / authority

Observed:

- `authority_axis.py`
- `icp_rank.py`
- `icp_score.py`
- `filters_four.py`
- `fit_scorer.py`
- `domain_cluster.py`
- `helping_baserate.py`
- `profsvc_check.py`
- `profsvc_meetings.py`

Important distinctions extracted:

- `icp_score.py` contained a **kill gate**: a candidate score/model had to beat a baseline under explicit thresholds rather than merely produce an attractive AUC.
- `filters_four.py` evaluated candidate filters on a **three-dimensional output vector**: precision, population coverage, and cost (how many engaged people the filter throws away).
- A downstream graph node historically carried only part of that vector. The missing cost dimension was not decorative; it opposed the optimization pressure of the other two metrics.

Candidate portfolio lesson: preserving only the convenient subset of a multi-output instrument can change the decision the instrument was designed to constrain.

## 2.6 DM / funnel / meeting / conversion instruments

Observed:

- `warm_test.py`
- `opener_check.py`
- `dm_hour_analysis.py`
- `verify_deck.py`
- `verify_deck2.py`
- `verify_deck3.py`
- `verify_reut.py`
- `build_label_queue.py`
- `log_meeting.py`
- `conversion_status.py`
- `attribution_build.py`
- `pipeline.py`
- `inbound.py`

Research function: move measurement from attention proxies toward actual business events — response, meeting, conversion, inbound attribution.

Historical caveat from the extraction: some of these tools depended on held-out/private exports and were deliberately not rerun during the inventory.

## 2.7 Draft-quality / novelty / friction instruments

Observed:

- `gate.py`
- `qa_check.py`
- `cadence_check.py`
- `friction_check.py`
- `slop_check.py`
- `novelty_check.py`
- `semantic_fit_check.py`
- `_sim_motif.py`
- `skill_lint.py`
- `graph_tagger.py`
- `saturation_map.py`

Research function: observer-first quality gates, novelty discrimination, semantic fit, motif duplication, process linting, saturation detection.

Important design feature: several of these instruments were observers first and did not directly rewrite the object they measured.

## 2.8 Seed / reuse instrumentation

Observed:

- `seed_ledger.py`
- `seed_tagger_build.py`
- `apply_seed_tags.py`

Research function: knowledge-resource reuse, tagging, utilization lineage.

## 2.9 Evidence-deposition bridges

Observed one-off writers:

- `_write_ledger_2026-07-23.py`
- `_write_ledger_filters.py`

These matter because they were rare examples of an explicit bridge:

```text
instrument result → durable evidence ledger
```

rather than:

```text
instrument result → stdout / transient file → forgotten
```

---

# 3. High-priority CRM research instruments

## 3.1 `analytics/construct_validity.py`

Extracted capabilities:

- ICC(2,1)
- ICC(2,k)
- Krippendorff alpha
- SEM
- MDC95
- convergent validity
- discriminant validity
- partial correlations
- leave-one-client-out
- 20,000-permutation tests
- specification curve

Historical portfolio issue: the decisive output files were absent in the inspected snapshot, so a sophisticated construct-validation run could exist without a durable evidence deposit.

## 3.2 `analytics/rating_kit.py`

Research function:

```text
raw transcript → blinded rating sheet → scored corpus → construct-validity run
```

This is an instrument for producing the measurement input, not merely a scoring function.

## 3.3 `analytics/drift_detector.py`

Research function: two-sample KS-style drift detection over an ownership distribution against a frozen baseline.

Portfolio question created: validation at time t0 is not identical to continued validity after distribution shift.

## 3.4 `analytics/method_triangulation.py`

Extracted design:

- VOICE channel
- MOVE channel
- SHAPE channel
- Spearman matrix
- PCA
- leave-one-channel-out style robustness
- comparison against AnnoMI

Research function: test whether differently operationalized signals converge on a latent structure.

Boundary: shared author/corpus/worldview can create correlated failure, so multi-instrument agreement is not automatically independent corroboration.

## 3.5 `analytics/metric_redundancy_analysis.py`

Extracted design:

- roughly 23 metrics
- Spearman matrix
- distance `1-|rho|`
- Ward clustering
- minimal representative core

Research function: redundancy detection, orthogonality checks, metric pruning.

Historical integrity issue: a later insufficient-data run overwrote a JSON result while an older Markdown report remained, producing a contradictory artifact pair.

## 3.6 `analytics/three_factor_analysis.py`

Extracted design:

- second-order partial Spearman
- incremental `ΔR²`
- incremental adjusted `R²`

Research function: whether a proposed third factor adds information beyond established anchors.

## 3.7 `analytics/coaching_style_detection.py`

Extracted design:

- PCA
- bimodality coefficient
- GMM BIC for k=1 vs k=2
- silhouette
- eta-squared between clients
- Kruskal-Wallis

Research function: detect whether a proposed style axis has empirical cluster/distribution structure.

## 3.8 `analytics/model_registry.py`

Research function: normalized source hashing, version/status integrity.

Portfolio question: are we running the instrument version we think we are running?

## 3.9 `business/funnel.py`

Research function: stage counts, conversion ratios, realized revenue, open pipeline.

## 3.10 `business/roi.py`

Research function: annual ROI, value capture, pricing-band calculations, follow-up/refresh anchors.

## 3.11 `business/value_capture.py`

Research function: capture/reprice classification, pricing-gap estimates and portfolio `total_on_table` style aggregation.

Historical issue: core output was transient by design rather than historically deposited.

## 3.12 `core/counter_thesis.py`

Research function: gate whether a counter-thesis changes operational permission rather than merely sounding critical.

## 3.13 `core/cognitive_value.py`

Research function: gate whether an idea has been translated into removed cognitive load and whether pricing permission follows.

---

# 4. Additional CRM instrument families

## 4.1 Signal engine

Observed names included:

- `owning_signal.py`
- `feature_matrix.py`
- `owned_differentiation.py`
- `authorship_transfer.py`
- `experiencing_depth.py`
- `ownership_stm.py`
- `keystone_construct_panel.py`
- `conversation_quality_index.py`
- `agency_detector.py`
- `question_effects.py`
- `owning_patterns.py`
- `psychological_markers.py`
- `reliability.py`
- `corpus_scores.py`
- `keystone.py`
- `outcomes.py`

## 4.2 Validation suite

Observed names included:

- `fidelity_anchor.py`
- `loco_prediction.py`
- owning-signal determinism / robustness / load-test / NLP-baseline checks
- `bias_audit.py`
- `heterogeneous_reliability.py`
- `lexical_triangulation.py`
- `category_creation_proof.py`
- `ownership_parity.py`
- `semantic_dependency_check.py`
- `reeval.py`
- `saturation_review.py`
- `corpus_snapshot.py`
- `self_verifying_pipeline.py`

## 4.3 Cross-corpus / far-domain

Observed families included:

- `analytics/annomi/*`
- `rogers_agency.py`
- `craigslist_agency.py`
- `dealornodeal_agency.py`
- `external_outcome_pilots.py`
- `service_sales_agency.py`
- `evidence_inventory.py`

## 4.4 Psychotherapy / interaction instruments

Observed:

- `holding_space.py`
- `alliance_detector.py`
- `containment_detector.py`
- `rupture_repair_detector.py`
- `relationship_axes.py`
- `interaction_quality.py`
- `projective_field_detector.py`
- `dynamic_interaction_layer.py`
- `pattern_map.py`

## 4.5 Meta/product instrumentation

Observed:

- `product_health.py`
- `local_explainer.py`
- `trust_ledger.py`
- `temporal_dynamics.py`
- `telemetry.py`
- `calibration.py`

## 4.6 Other notable harnesses

- `mechanism_turnlevel.py` — turn-level mechanism test with permutation logic.
- `product_fit_backtest.py` — deterministic backtest harness.
- adjacent `_analysis/pipeline` instruments such as `axis_a_ranking.py` and `axis_b_profile.py`.

---

# 5. Preregistration itself is part of the instrument portfolio

The extraction found at least 24 preregistration artifacts naming an executable instrument, including families such as:

- acquisition wave tests;
- blind structural transcript rating;
- decision-queue tests;
- graph-advice tests;
- cost-anchor tests;
- routing-hit tests;
- content-advice tests;
- model-scale isomorphism tests;
- LinkedIn profile-richness tests;
- within-post measurement;
- fresh-window disqualification-gate tests;
- claim-level survival tests;
- measure-before-structure tests;
- methodology-stage tests;
- margin-vs-cosine tests;
- professional-category-vs-meeting tests;
- session-allocation tests;
- H7 paraphrase tests;
- H8 resistance holdout;
- psycholinguistic-lexicon tests.

Portfolio-level observation: preregistration/locking had substantially more automation than outcome scoring/closure at the inspected snapshot.

This creates a distinct debt type:

> **run/closure debt** — a test can be well designed, preregistered and frozen yet never produce decision-changing evidence.

---

# 6. Normalized instrument capabilities already present in the portfolio

Across repositories, the owner had already built examples of the following research primitives:

## Ground truth and acquisition

- event ledgers
- label queues
- blinded rating sheets
- corpus builders
- outcome capture
- attribution bridges

## Reliability

- ICC
- Krippendorff alpha
- SEM / MDC
- test-retest style checks
- determinism
- robustness/load tests

## Construct validity

- convergent validity
- discriminant validity
- category-creation tests
- semantic dependency checks

## External/generalization checks

- holdout windows
- fresh-window tests
- leave-one-client-out
- cross-corpus replication
- far-domain stress tests

## Falsification and controls

- negative controls
- positive controls
- kill gates
- adversarial successor tests
- permutation tests
- counter-thesis gates

## Specification and sensitivity

- alternative operationalizations
- specification curves
- sensitivity analyses
- power simulations
- insufficient-data / abstention states

## Latent structure

- PCA
- clustering
- GMM / bimodality checks
- factor-style decompositions

## Orthogonality / incremental value

- metric-redundancy analysis
- partial correlations
- incremental `ΔR²`

## Confound handling

- within-session permutations
- speaker controls
- temporal controls
- baseline comparisons

## Drift

- frozen-baseline distribution-shift tests

## Prospective integrity

- preregistration
- locked predictions
- sealed/held-out windows
- append-outcome-only policies

## Triangulation

- multiple instruments
- multiple methods
- multiple corpora

## Provenance / integrity

- hashes
- model registries
- manifests
- corpus snapshots
- append-only ledgers
- supersession/backup artifacts

## Business reality

- funnel
- ROI
- value capture
- attribution
- meeting/conversion
- inbound

## Self-audit of the research system

- bias audits
- self-verifying pipeline
- saturation review
- metric redundancy
- drift detection
- provenance integrity

---

# 7. Candidate distinctions created by the extraction

These are **research candidates**, not Neta rules.

## C1 — instrument existence ≠ evidence existence

A sophisticated executable instrument can exist while its decisive result is printed to stdout, written to a dead scratchpad, overwritten by an insufficient-data rerun, or never linked to a claim.

Potential discriminator for future work:

- can the result be reconstructed from durable artifacts without rerunning the original private environment?

## C2 — instrument design debt ≠ run/closure debt

The portfolio contained many locked/preregistered tests. The visible bottleneck was often not missing methodology but failure to execute, score and deposit the result.

Potential discriminator:

- count tests that are designed/locked versus tests with scored outcomes and named claim effects.

## C3 — partial output deposition can invalidate the instrument's constraint structure

If an instrument intentionally returns an opposing metric vector, depositing only the favorable components can create a different optimization problem.

Potential discriminator:

- compare the instrument's complete output schema to what the downstream ledger/claim actually stores.

## C4 — multiple self-built instruments are not automatically independent triangulation

Shared author, corpus, labels, worldview, preprocessing or failure modes can make apparent agreement structurally unsurprising.

Potential discriminator:

- before calling agreement corroboration, state where the instruments' errors are expected to diverge.

## C5 — instrument lineage matters

The portfolio contains many clear successor chains (`verify_predict → verify_attack`, `scorecard → scorecard_real → master_features`, timing-series retirement, etc.). Counting every file as an independent instrument overstates capability and hides supersession.

Potential discriminator:

- classify prototype / successor / live / retired / superseded / dead-output-only before portfolio counts are used.

## C6 — nulls and retirements are high-value research assets

Several instrument families are most useful because they killed a proxy or mechanism, not because they produced a deployable rule.

Potential discriminator:

- does the research memory make a dead hypothesis easier to avoid rebuilding than a surviving hypothesis is to reuse?

## C7 — research capacity can be the limiting resource

A portfolio with many preregistrations and instruments but few closed runs may be bottlenecked on operator execution capacity rather than idea generation or methodological sophistication.

Potential discriminator:

- measure new-instrument creation rate against run/closure/deposition rate.

---

# 8. Neta-facing questions opened by this import

This extraction does **not** justify building a registry yet. It creates questions that may be worth resolving if they become material:

1. Should Neta perform an **instrument-existence search** before proposing a new probe?
2. Should Neta distinguish **instrument debt**, **run debt**, **evidence-deposition debt**, and **supersession debt**?
3. Should every instrument-backed claim preserve the **full decision-relevant output vector** rather than a selected scalar?
4. What minimum metadata is required before two instruments may count as independent triangulation?
5. Should a research instrument have a lifecycle such as `prototype → live → retired/superseded`, separate from claim promotion status?
6. Should Neta prefer reviving/revalidating an existing instrument when cheaper than building a new one?
7. What evidence would show that an instrument registry reduces uncertainty rather than becoming another catalog no one runs?
8. When does a null result deserve stronger preservation priority than a positive result because it prevents expensive rediscovery?

Under current Neta governance, these are `RESEARCH` questions until one is tied to a live decision whose outcome can change Neta behavior.

---

# 9. Revalidation requirements before operational use

Before any current action is justified from this import:

- refetch the relevant source repository;
- freeze an exact commit or working-tree snapshot where possible;
- verify the instrument path still exists;
- verify dependencies and input files;
- inspect whether the historical output is durable and matches the current code version;
- identify predecessor/successor/retirement status;
- identify the exact claim the instrument can discriminate;
- identify measurement contamination risk;
- identify the full output vector;
- identify a falsifier / control where appropriate;
- deposit the result durably if a run is performed.

The revalidation itself should be cheaper than rebuilding an equivalent instrument. If not, the instrument may be historical evidence rather than reusable infrastructure.

---

# 10. Stop condition

Do not turn this import into a registry project merely because the portfolio is large.

The next justified move exists only when a named Neta decision would change based on one of these distinctions.

Until then, this file's job is narrower:

> make the already-built research portfolio visible, preserve the extraction, and prevent future work from confusing "not present in Neta" with "never built or tested elsewhere".
