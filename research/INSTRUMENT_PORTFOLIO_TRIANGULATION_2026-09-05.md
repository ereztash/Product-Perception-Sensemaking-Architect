# Instrument Portfolio Triangulation — 2026-09-05

**Status:** `TRIANGULATION_PASS`

**Parent:** `research/INSTRUMENT_PORTFOLIO_NETA_PASS_2026-09-05.md`

**Scope:** external triangulation and falsification search for T1–T6 only. This file does not change Neta method, prompt, schema or promotion state by itself.

---

# 0. Independence families used

The pass deliberately used evidence from different lineages rather than citation volume.

## F1 — research-software reproducibility / provenance

- W3C PROV Primer — provenance model for entities, activities and agents: https://www.w3.org/TR/prov-primer/
- Barker et al. (2022), FAIR Principles for Research Software, *Scientific Data*: https://doi.org/10.1038/s41597-022-01710-x
- Trisovic et al. (2022), “A large-scale study on research code quality and execution”, *Scientific Data*: https://doi.org/10.1038/s41597-022-01143-6

## F2 — operational experiment/model tracking

- MLflow Tracking — runs persist parameters, code versions, metrics and artifacts: https://mlflow.org/docs/latest/ml/tracking/
- MLflow Model Registry — lineage, versioning, aliases, metadata and lifecycle management: https://mlflow.org/docs/latest/ml/model-registry/
- MLflow model-registry workflow / stage deprecation: https://mlflow.org/docs/latest/ml/model-registry/workflow/

## F3 — preregistration / discontinuation / reporting meta-research

- Kasenda/Blümle et al. repeated metaresearch on randomized trials: https://pmc.ncbi.nlm.nih.gov/articles/PMC9094518/
- PLOS Medicine version: https://journals.plos.org/plosmedicine/article?id=10.1371/journal.pmed.1003980

## F4 — selective outcome reporting

- Dwan et al. (2013) updated systematic review: https://journals.plos.org/plosone/doi?id=10.1371/journal.pone.0066844
- Cochrane methodology review on selective outcome inclusion/reporting: https://www.cochrane.org/evidence/MR000035_bias-due-selective-inclusion-and-reporting-outcomes-and-analyses-systematic-reviews-randomised
- Copas et al. model-based correction for outcome-reporting bias: https://academic.oup.com/biostatistics/article/15/2/370/226361

## F5 — multi-criteria decision robustness

- “Sensitivity analysis approaches in multi-criteria decision analysis: A systematic review”, *Applied Soft Computing* 148 (2023), 110915: https://doi.org/10.1016/j.asoc.2023.110915

## F6 — measurement-instrument selection / reuse

- COSMIN, selecting the most suitable outcome measurement instrument: https://www.cosmin.nl/finding-right-tool/select-best-measurement-instrument/
- GESIS ZIS instrument archive/toolbox: https://zis.gesis.org/s/?lang=en
- APA PsycTests overview: https://www.apa.org/pubs/databases/psyctests
- Anvari et al. (2025), “A Fragmented Field: Construct and Measure Proliferation in Psychology”: https://doi.org/10.1177/25152459251360642
- best-practice scale-development guidance requiring review of existing measures before a new scale: https://pubmed.ncbi.nlm.nih.gov/39916786/

## F7 — counterevidence on measure proliferation

- “Proliferation of measures contributes to advancing psychological science” (2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11332101/

## F8 — null / unpublished-result preservation

- “Reporting all results efficiently: A RARE proposal to open up the file drawer” (2021/2022): https://pubmed.ncbi.nlm.nih.gov/34933997/
- updated survey-experiment file-drawer study: https://pmc.ncbi.nlm.nih.gov/articles/PMC11962440/

---

# 1. T1 — lifecycle transitions: instrument existence vs evidence existence

## Candidate

A research instrument can exist while usable evidence does not, because design, execution, result persistence, provenance and decision linkage are separable transitions.

## Supporting evidence

**F1:** W3C PROV explicitly separates entities from activities and agents; provenance records how an artifact came to exist rather than treating artifact existence as sufficient history.

**F1:** FAIR4RS exists because research software has distinctive executability, evolution and versioning requirements; software presence alone is not equivalent to reusable research capability.

**F1:** Trisovic et al. executed >9,000 R files from >2,000 public replication datasets. 74% failed on initial execution and 56% still failed after code cleaning. This is direct evidence that “available research code” and “re-executable research instrument” are different states.

**F2:** MLflow separates a *run* from its logged metrics/artifacts and separately manages model lineage/version metadata. This operationally instantiates the same decomposition.

## Falsification / boundary

The evidence does **not** establish one universal lifecycle taxonomy. In fact MLflow deprecated its fixed Staging/Production/Archived model stages after feedback that the fixed stages were too inflexible for real workflows.

## Disposition

`NARROWS + TRIANGULATES`

Surviving wording:

> Instrument identity, execution, result persistence, provenance and current usability are distinct research states/transitions; do not infer one from another.

Rejected stronger wording:

> Every research instrument should use one fixed prototype→live→retired lifecycle enum.

---

# 2. T2 — preregistration / design rigor without closure

## Candidate

Run/closure debt can be distinct from instrument-design debt.

## Supporting evidence

**F3:** in 326 approved randomized trials, 30% were prematurely discontinued and 21% remained unpublished at ten-year follow-up. Registration and protocol existence therefore did not guarantee completion or result availability.

**F8:** the RARE proposal treats registered studies whose results never become available as a distinct infrastructure problem and argues that fuller result reporting can reduce repeated unsuccessful investigations and wasted funding.

## Falsification / contradiction

The original Neta-pass hypothesis that the limiting cause might be “operator execution capacity” is too strong. In the randomized-trial cohort, poor recruitment was a major discontinuation reason; other closure failures may reflect feasibility, delayed outcomes, reporting incentives or authority boundaries rather than operator bandwidth.

A preregistered study can also be legitimately open because its outcome is not yet observable. “Unscored” is not automatically debt.

## Disposition

`SPLITS`

Parent claim frozen. Surviving children:

### C2a — execution/feasibility closure

A designed/locked test may never reach a valid run because required inputs, recruitment, dependencies or feasibility fail.

### C2b — result/deposition closure

A run may occur but its result is not scored, persisted or made retrievable.

### C2c — authority/latency open state

A test may be legitimately unresolved because the required FIELD/ENVIRONMENT/outcome has not arrived. This must not be called debt.

### C2d — decision-link closure

A persisted result may still fail to alter or explicitly preserve the state of the claim/decision it was designed to inform.

No evidence in this pass identifies which child dominates the owner's portfolio without a source-repository denominator audit.

---

# 3. T3 — partial output vectors / selective reporting / scalarization

## Candidate

Persisting only a favorable subset of a multi-dimensional instrument can change the decision problem.

## Supporting evidence

**F4:** systematic reviews of outcome-reporting bias found direct evidence that statistically significant outcomes are more likely to be fully reported. Across protocol-publication comparisons, 40–62% of studies had at least one primary outcome changed, introduced or omitted in the reviewed cohorts. Selective outcome reporting can therefore distort the accessible evidence set.

**F4:** Cochrane's review explicitly treats post-result selection among multiple outcomes/analyses as a bias risk and recommends prespecification plus complete reporting of outcomes/effect estimates regardless of result.

**F5:** MCDA sensitivity-analysis literature treats stability of rankings under changes in underlying criteria/data as a core robustness question. Multi-criteria decisions are not invariant to what dimensions, weights or representations are retained.

## Falsification / narrowing

“Always preserve the full raw vector forever” is not supported. Legitimate decision systems can scalarize, weight, aggregate or omit redundant dimensions when the transformation is defined and its sensitivity is understood.

The integrity failure is not compression itself. It is **silent post-hoc dimension loss that changes or can change decision meaning without preserving the decision function.**

## Disposition

`NARROWS + TRIANGULATES`

Surviving wording:

> Preserve the prespecified decision-relevant outcome contract. If dimensions are transformed, weighted, scalarized or removed, preserve the transformation/decision rule and enough information to test whether the decision is sensitive to that choice.

This is stronger and more precise than “store every metric”.

---

# 4. T4 — search/reuse before building a new instrument

## Candidate intervention

Before building a new research probe, search for an existing instrument that might measure the construct.

## Supporting evidence

**F6:** COSMIN's workflow explicitly begins instrument selection by looking for available instruments and judging reliability, validity, responsiveness and feasibility rather than defaulting to new development.

**F6:** recent scale-development guidance includes reviewing existing measures as part of the preliminary decision about whether a new measure is needed.

**F6:** APA PsycTests says its metadata/database is designed in part to save researchers from reproducing tests for previously measured constructs. ZIS likewise acts as an archive/toolbox for tested instruments.

**F6:** Anvari et al. found large and increasing measure fragmentation over decades; most measures are used very few times. This supports the existence of a costly “new measure by default” failure mode.

## Counterevidence

**F7:** measure proliferation is not inherently waste. Context, population, theory refinement and validity boundaries may legitimately require new measures; diversity of operationalizations can itself strengthen science.

The existence of large registries also does not demonstrate that registry presence causes reuse. Anvari et al. found continuing fragmentation despite large measurement databases.

## Disposition

`NARROWS / CONTEXTUALIZES`

Rejected rule:

> Reuse before build.

Surviving intervention candidate:

> **Search-before-build, not reuse-before-build.** For a live claim, perform a bounded existence search when its cost is lower than building/revalidating from scratch; then discriminate among reuse, adaptation and new construction using construct fit, validity, context, dependencies and contamination risk.

Permission remains `DEFER` until a Neta fixture shows that the search changes a probe decision at acceptable cost.

A global registry is not authorized.

---

# 5. T5 — instrument lifecycle and research-software decay

## Candidate

Instrument lifecycle/supersession state is distinct from claim promotion state.

## Supporting evidence

**F1:** FAIR4RS treats versioning/evolution as defining properties of research software.

**F1:** Trisovic et al. show that even publicly archived research code frequently fails to run because of documentation/dependency/path problems. An instrument can therefore remain historically meaningful while losing present runnability.

**F2:** MLflow separates model version lineage from experiment runs and supports aliases/metadata; this is operational evidence that object identity/version and evidential run history are different concerns.

## Counterevidence

**F2:** MLflow's deprecation of fixed lifecycle stages is direct evidence against importing a rigid universal lifecycle state machine. Real workflow semantics vary.

## Disposition

`NARROWS`

Surviving distinction:

> Neta needs to be able to tell historical identity/lineage, current runnability/revalidation state, and claim effect apart. It does not yet need a universal `prototype/live/retired` enum.

Candidate minimal properties to test later: version/provenance, supersedes/superseded-by, last verified execution, dependencies/input contract, current reuse ceiling.

---

# 6. T6 — null/refutation preservation

## Candidate residual

Neta already preserves its own failures, but should research-run null/refutation outcomes be first-class retrievable assets too?

## Supporting evidence

**F8:** the file-drawer literature shows that non-significant/null results are less likely to enter the cumulative scientific record, leaving a biased view of evidence.

**F8:** RARE explicitly argues that coordinated reporting of all results can prevent researchers from wasting time investigating the same questions in ways that have already failed.

**F4:** selective outcome reporting likewise demonstrates that inaccessible/omitted outcomes distort later synthesis.

## Boundary

A non-significant result is not automatically evidence of absence. Preserving nulls must preserve power/design/estimand context so an inconclusive test is not later retrieved as a falsification.

## Disposition

`TRIANGULATES + NARROWS`

Surviving wording:

> Preserve retrievable failed/null research runs with enough design and interpretation context to distinguish `REFUTED` from `INCONCLUSIVE`, because absence from memory creates both bias and duplicate-work risk.

This is related to `docs/FAILURE_LINEAGE.md` but is not identical: failure lineage records Neta-method failures; this candidate concerns the evidence memory of the research system.

---

# 7. Cross-candidate result

After triangulation, the strongest common structure is **not an instrument registry**.

Independent families converge on a transition/provenance problem:

```text
claim/question
→ candidate instrument exists or is created
→ version/input contract identified
→ run actually occurs
→ outcomes/artifacts are persisted
→ decision-relevant reporting contract is preserved
→ result is linked to the claim
→ result gets a disposition
→ later reuse checks lineage + current runnability
```

Failures at these arrows are materially different and can require different repairs.

The external evidence does **not** justify assuming one universal cause, one fixed lifecycle enum, mandatory reuse, or preservation of every raw metric.

---

# 8. Candidate dispositions summary

- **C1 instrument existence ≠ evidence existence:** `TRIANGULATED / NARROWED`.
- **C2 run/closure debt:** `SPLIT` into execution, deposition, authority/latency and decision-link closure.
- **C3 partial output deposition:** `TRIANGULATED / NARROWED` to prespecified decision-relevant outcome contract + explicit transformation/sensitivity.
- **C4 existence search before build:** `CONTEXTUALIZED`; search-before-build survives, reuse-before-build does not.
- **C5 lifecycle/supersession:** `NARROWED`; lineage + current runnability survive, rigid lifecycle enum does not.
- **C6 shared ancestry:** already covered by Neta; no new promotion.
- **C7 null/refutation preservation:** `TRIANGULATED / NARROWED`; preserve with conclusive-vs-inconclusive context.
- **C8 registry as progress proxy:** remains blocked by current Neta anti-build rules.

---

# 9. Research ceiling

Further broad literature search is not justified merely to increase source count. The main candidates have now received independent support and counterevidence.

The next useful step is synthesis into the smallest candidate Neta capability/fixture set, without changing canonical behavior yet.