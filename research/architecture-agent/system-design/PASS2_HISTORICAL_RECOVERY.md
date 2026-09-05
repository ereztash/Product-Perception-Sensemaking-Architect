# System Design Decision Research — Pass 2 Historical Recovery

Status: `RECOVERY_SIGNAL_NOT_BENCHMARK`
Date: 2026-09-06
Task: `CAL-ARCH-SYSDESIGN-001`

## Purpose

Recover real architecture decisions from existing Erez repositories before buying more external system-design knowledge.

This pass is intentionally retrospective and contaminated by known outcomes. It can narrow candidate discriminators and generate blinded fixtures; it **cannot** establish causal decision advantage for the candidate contract.

## Recovered cases

### H1 — Record-query cache invalidation after server writes
Repo: `ereztash/lichess_app`
Commit: `6b37a4aef0fc11508bce13811fc2a30301911fc3`

Observed problem:
- server-side decision/reveal writes returned before local-branch invalidation logic;
- signed-in sessions retained stale record queries;
- the UI could display a decision while counting its occurrence as zero.

Architecture dimensions already available in v0:
- `STATE_AUTHORITY`;
- `INVARIANT` (post-write reads must not contradict committed state);
- `CHANGE_PROPAGATION`;
- `DEPENDENCY_DIRECTION`.

Candidate-system-design delta:
- `MECHANISM_COUNTERINDICATION` for caching could name invalidation/coherence risk, but the architecture decision is already recoverable from v0's state-authority/invariant model.

Disposition: **NO UNIQUE DELTA YET**.

---

### H2 — Evaluation cache key omitted the root-set/policy identity
Repo: `ereztash/lichess_app`
Commit: `e40d131e40526ad40086bb7d2041b08bf51226d6`

Observed problem:
- two MultiPV searches over different root sets were merged as the same cached measurement;
- the cache key omitted a dimension that changed the semantics of the measurement;
- cached values from different searches contaminated results.

Architecture dimensions already available in v0:
- `INVARIANT`;
- `STATE_AUTHORITY`;
- `BOUNDARY` of measurement identity;
- `DECISION_LINEAGE`.

Candidate-system-design delta:
- generic cache knowledge adds terminology, but the decisive distinction is semantic identity/invariant, already v0 territory.

Disposition: **NO UNIQUE DELTA YET**.

---

### H3 — “Database available” measured configuration, not reachability
Repo: `ereztash/lichess_app`
Commit: `a2ed0c51f5d1c3bd5988093130e618c0f128c007`

Observed problem:
- `isAvailable()` effectively measured whether a DB URL was configured;
- the first real query could still fail;
- `/api/health` returned healthy while the configured database was unreachable;
- the product routed away from a working local fallback based on a false availability claim.

Candidate-system-design delta:
- `REQUIRED_PROPERTY`: the server may be selected only if it can actually store/respond within a bounded time;
- `BOTTLENECK/HEALTH EVIDENCE`: a real `select 1` under a 3s deadline rather than configuration presence;
- user-relevant service behavior is more informative than a component-existence proxy.

Existing v0 can flag repository/runtime distinction and authority, but it does not force a measurable service property before mechanism/routing choice.

Disposition: **CANDIDATE UNIQUE DELTA — SLO/OBSERVABLE PROPERTY**.

---

### H4 — Browser record cache crossed identity boundary
Repo: `ereztash/lichess_app`
Commit: `714779deefcc942d4c0603969a1b8d75666e318e`

Observed problem:
- react-query cache keys did not include signed-in identity;
- logout/session change could leave another account's record visible from cache;
- server ownership controls did not constrain browser cache lifecycle.

Architecture dimensions already available in v0:
- `BOUNDARY`;
- `STATE_AUTHORITY`;
- `INVARIANT`;
- `FAILURE_DOMAIN` / blast radius.

Candidate-system-design delta:
- cache counterindication is useful domain knowledge but does not appear to require a new first-class discriminator.

Disposition: **NO UNIQUE DELTA YET**.

---

### H5 — CRM cache bound to store version and invalidated on writes
Repo: `ereztash/_crm`
Commit: `23920a05cfc9825baf907ddbb334d5035cfc1eae`

Observed move:
- corpus/analysis/fingerprint cached per store version `(mtime, size)`;
- server writes invalidate the cache;
- health becomes a cheap stat operation and map recomputation occurs only after ingest.

Candidate-system-design delta:
- explicit workload/cost model could help justify caching (`recomputation cost` vs `stat cost`, mutation frequency), but the commit already derives the right invalidation boundary from state version.

Disposition: **POSSIBLE WORKLOAD DELTA, NOT YET ESTABLISHED**.

---

### H6 — Background analysis had to outlive the screen that started it
Repo: `ereztash/lichess_app`
Commit: `fc7058b5045a5240343a7961df130e2855936c63`

Observed problem:
- analysis lived in a screen-local effect and cancellation left stored games permanently `pending`;
- work was redefined over the stored record and moved to a page-level resumable runner;
- a hung analysis needed a timeout and cleanup path.

Architecture dimensions already available in v0:
- `TEMPORAL_COUPLING`;
- `STATE_AUTHORITY`;
- `FAILURE_DOMAIN`;
- `DEPLOYMENT_BOUNDARY`;
- `MIGRATION_PATH`.

Candidate-system-design delta:
- queue/worker literature may provide implementation alternatives, but the architectural judgment itself is already well-described by current v0 objects.

Disposition: **NO UNIQUE DELTA YET**.

---

### H7 — Engine readiness budget was really a bandwidth/download budget
Repo: `ereztash/lichess_app`
Commit: `8b953aabdafdba0711fc2ab7a7c2d90f818d11`

Correction: the exact engine-readiness commit is `8b953aabdafdba0711fc3ab6314661eb409595cb`.

Observed problem:
- a 15s readiness bound looked like an engine-computation constraint;
- measurement showed the engine itself became ready quickly once bytes were local;
- the actual pressure was downloading ~5.6 MB gzipped over slow connections;
- the time bound was recalibrated from a workload/resource model rather than guesswork.

Candidate-system-design delta:
- `WORKLOAD_PRESSURE`: payload size × network throughput;
- `REQUIRED_PROPERTY`: acceptable readiness latency;
- `BOTTLENECK_EVIDENCE`: timing breakdown of fetch/compile/readiness;
- this changes the mechanism/parameter decision and avoids fixing the wrong subsystem.

Disposition: **CANDIDATE UNIQUE DELTA — WORKLOAD + MEASURED BOTTLENECK**.

---

### H8 — Four record states were collapsed into “empty”
Repo: `ereztash/lichess_app`
Commit: `19cf5461cc99384908185ef115aa6ee45e9335b0`

Observed problem:
- no record, old record, damaged record and newer-build record collapsed to one fallback;
- a damaged/newer record could later be overwritten;
- repair chose preservation + session-only fallback rather than destructive normalization.

Architecture dimensions already available in v0:
- `STATE_AUTHORITY`;
- `INVARIANT`;
- `MIGRATION_PATH`;
- `REVERSIBILITY`;
- `DECISION_LINEAGE`.

Candidate-system-design delta:
- general storage/system-design knowledge is not the missing discriminator here.

Disposition: **NO UNIQUE DELTA YET**.

---

### H9 — Decision and engine reveal stored in separate tables
Repo: `ereztash/lichess_app`
Commit: `813269d122d82ef2e170ebcac6eee34722f9d48e`

Observed move:
- user-produced decision and engine-produced reveal intentionally separated;
- server refuses reveal without prior committed decision;
- storage failure is loud rather than indistinguishable from success.

Architecture dimensions already available in v0:
- `BOUNDARY`;
- `STATE_AUTHORITY`;
- `INVARIANT`;
- `DEPENDENCY_DIRECTION`;
- `DECISION_LINEAGE`.

Disposition: **STRONG POSITIVE CONTROL FOR CURRENT v0; NO NEW SYSTEM-DESIGN OBJECT NEEDED**.

---

### H10 — Lazy-loading reduced initial bundle and ceilings were tightened
Repo: `ereztash/lichess_app`
Commit: `154b1e2fa48930cebef47a07c70a5ea692d86271`

Observed move:
- a secondary exploration surface was moved behind a lazy boundary;
- initial bundle dropped materially;
- bundle ceilings were tightened after the improvement so the gain could not silently regress.

Candidate-system-design delta:
- `REQUIRED_PROPERTY`: initial-load/bundle budget;
- `BOTTLENECK_EVIDENCE`: measured raw/gzip/initial sizes;
- `REVERSAL/REGRESSION CONDITION`: ratchet ceiling.

Current v0 can represent constraint and reversal, but an explicit measurable quality target makes the architecture pressure sharper and testable.

Disposition: **CANDIDATE UNIQUE DELTA — MEASURABLE QUALITY TARGET**.

## Cross-case result

The broad Pass-1 candidate expansion was too large.

### Objects that appear mostly redundant with v0

- generic `MECHANISM_COUNTERINDICATION` — often expressible via existing `CONSTRAINT`, `INVARIANT`, `FAILURE_DOMAIN`, `STATE_AUTHORITY` and `TRADEOFF_LEDGER`;
- generic `OPERATIONAL_BURDEN` — likely useful as a tradeoff dimension, but not yet shown to require a first-class object;
- generic `WORKLOAD_PRESSURE` in every case — many architecture decisions are semantic/authority problems rather than scale problems.

### Narrow residual that survives recovery

A recurring gap appears when `MATERIAL_PRESSURE` is expressed qualitatively but the decision depends on a measurable service/workload property.

Candidate minimal refinement:

```text
MATERIAL_PRESSURE
  ├─ REQUIRED_PROPERTY / SERVICE OBJECTIVE
  ├─ RELEVANT WORKLOAD / RESOURCE CONDITIONS
  └─ OBSERVED BOTTLENECK / LIMIT EVIDENCE
```

This is smaller than adding five new architecture objects and preserves v0's existing structural ontology.

## Decision after recovery

**Do not build a system-design knowledge base and do not expand v0 broadly.**

Advance one narrow challenger:

> Does decomposing `MATERIAL_PRESSURE` into a bounded `required property + relevant workload conditions + observed limit evidence` improve architecture decisions on cases where performance/reliability/scale is material, while staying silent on semantic/state-authority cases?

## Next step

Create blinded fixtures from H3, H7, H10 as positive controls and H1/H2/H4/H9 as neighboring non-fire cases. Compare:

1. current Architecture Decision Discriminator v0;
2. v0 + the narrow `MATERIAL_PRESSURE` refinement.

Only if the refinement changes bounded decisions or required evidence should deeper source lanes for caching, queues, replication, CDN, observability/indexing/sharding be opened.
