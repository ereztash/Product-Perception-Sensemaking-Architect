# Instrument Portfolio Synthesis — 2026-09-05

**Status:** `FIXTURE_CANDIDATE_SYNTHESIS`

**Inputs:**

- `research/INSTRUMENT_PORTFOLIO_EXTRACTION_2026-09-05.md`
- `research/INSTRUMENT_PORTFOLIO_NETA_PASS_2026-09-05.md`
- `research/INSTRUMENT_PORTFOLIO_TRIANGULATION_2026-09-05.md`

**Canonical impact:** none yet.

---

# BLUF

The triangulation does **not** support building an instrument registry.

It supports a narrower candidate capability:

> **Research continuity:** before creating a new probe, determine whether relevant research capability/evidence already exists; if an instrument is used, keep instrument identity, execution, decision-relevant result, claim effect and later revalidation connected instead of allowing any one of those to substitute for the others.

The core problem is not inventory size. It is broken continuity across transitions.

The minimal candidate loop is:

```text
LIVE CLAIM
→ BOUNDED EXISTENCE SEARCH (when cheaper than rebuilding)
→ REUSE / ADAPT / BUILD decision
→ INPUT + VERSION REVALIDATION
→ RUN
→ DECISION-RELEVANT OUTCOME DEPOSIT
→ CLAIM LINK + DISPOSITION
→ NULL / REFUTATION / INCONCLUSIVE MEMORY
→ LATER REUSE CHECKS CURRENT RUNNABILITY + LINEAGE
```

This remains a **fixture candidate**, not a Neta rule.

---

# 1. What survived synthesis

## S1 — continuity transitions are distinct

Do not collapse:

- instrument exists;
- instrument is currently runnable;
- instrument was run;
- a result exists;
- the decision-relevant outcome contract was preserved;
- the result affected a named claim;
- the result remains usable after version/context drift.

Evidence from provenance standards, research-software reproducibility and experiment tracking converges on this separation.

### Why this matters to Neta

Neta already guards against `representation → represented reality` proxy substitution. This is a research-system version of the same error:

```text
instrument file exists
≠ instrument works now
≠ experiment ran
≠ evidence was preserved
≠ claim changed
```

This is the strongest synthesis-level connection to existing Neta architecture.

---

## S2 — “closure debt” is not one debt

Do not create one scalar or one status called closure debt.

Triangulation forced a split:

### Execution / feasibility open

The test cannot validly run because data, dependencies, sample, recruitment or environment are missing.

### Result / deposition open

The run happened but the outcome is not scored, persisted or retrievable.

### Authority / latency open

The test is correctly waiting on an outcome or authority that has not arrived. This is **not debt**.

### Decision-link open

A result exists but its effect on the named claim/decision is unstated.

These states imply different next moves; collapsing them would recreate the proxy-substitution problem at the workflow level.

---

## S3 — preserve the decision contract, not every byte

The original candidate “persist the full vector” was too strong.

Surviving rule candidate:

> If an instrument has prespecified outcome dimensions that jointly constrain a decision, do not silently drop, substitute or post-hoc select among them. If outcomes are scalarized, weighted, transformed or removed, preserve the decision rule and enough information to test sensitivity to that transformation.

This captures the `filters_four` failure shape without turning Neta into a universal raw-data warehouse.

---

## S4 — search-before-build, not reuse-before-build

Measurement science supports checking existing instruments before developing a new one, but counterevidence shows new operationalizations can be legitimate when construct, context or population changes.

Therefore:

```text
SEARCH
→ FIT / VALIDITY / CONTEXT / COST / CONTAMINATION CHECK
→ REUSE | ADAPT | BUILD
```

not:

```text
FOUND SOMETHING → MUST REUSE IT
```

A search itself also requires permission: it should be bounded and cheaper than equivalent reconstruction.

---

## S5 — lineage + revalidation matter more than a fixed lifecycle enum

The triangulation supports version, provenance, supersession and current-runnability distinctions.

It does **not** support one universal lifecycle such as `prototype → live → retired`.

A rigid taxonomy can become another representation that fails to match real workflows. MLflow's deprecation of fixed stages is a direct caution here.

Therefore the candidate information is relational/event-based:

- what produced this instrument/result;
- which version ran;
- what it supersedes;
- when it was last verified;
- what inputs/dependencies it requires;
- what claim/use it can currently support.

---

## S6 — null/refutation memory is a research asset

Neta already preserves method failures. The synthesis adds a narrower residual:

> research-run failures/nulls need retrievable evidence context too, because disappearing nulls bias later synthesis and invite duplicate work.

But the memory must preserve the difference between:

- `REFUTED`;
- `INCONCLUSIVE`;
- `NOT_RUN`;
- `FAILED_EXECUTION`;
- `WAITING_AUTHORITY`.

A p>0.05 or an errored script must never be retrieved later as “the hypothesis was false”.

---

# 2. What did NOT survive

The following should **not** be promoted from this work:

1. **Build a central registry.** No evidence that registry presence itself removes uncertainty or causes reuse.
2. **Reuse before build.** Too strong; context/construct change can justify a new instrument.
3. **One closure-debt score.** It collapses materially different causes and next actions.
4. **One fixed instrument lifecycle enum.** Real workflows vary; provenance/events are more robust.
5. **Store every raw metric.** The requirement is preservation of decision-relevant outcome semantics, not indiscriminate storage.
6. **Unscored = debt.** A legitimately pending FIELD/ENVIRONMENT outcome is an authority state, not failure.
7. **Null = refuted.** Null results may be underpowered or inconclusive.

---

# 3. Candidate capability

## Name

`RESEARCH_CONTINUITY_DISCRIMINATOR`

## Purpose

Prevent Neta from paying for a new research instrument when relevant capability/evidence already exists, and prevent completed research from becoming invisible or semantically damaged before it changes a decision.

## It should answer only these questions

1. **Live claim:** what exact claim needs discrimination?
2. **Existing capability:** is there a plausible existing instrument/result that can touch that claim?
3. **Reuse ceiling:** if so, is it runnable/revalidatable under current inputs/version/context?
4. **Decision contract:** what outcomes/constraints must the run preserve to keep its meaning?
5. **Closure:** after the run, where is the durable result and what did it do to the claim?
6. **Memory:** if it failed/null/inconclusive, is that state retrievable without being misread?

## It should NOT answer

- whether a registry should exist;
- whether the instrument is valid merely because it has a name/file;
- whether two related instruments count as independent triangulation;
- what users will do;
- whether a new instrument is prohibited.

---

# 4. Cheapest fixture set before any method/schema change

No code/schema/prompt change is permitted until the capability wins on fixtures.

## F1 — duplicate-probe trap

**Setup:** a live Neta claim appears to need a new probe, but an existing instrument in the provided corpus already measures the relevant construct.

**Pass:** Neta finds it, checks fit/runnability and avoids duplicate construction when reuse/adaptation is cheaper.

**Fail:** immediately proposes new instrumentation.

## F2 — zombie-instrument trap

**Setup:** an instrument exists historically but its path/dependency/input contract is broken or stale.

**Pass:** Neta does not equate existence with usability; it marks a revalidation ceiling or historical-only use.

**Fail:** treats the old script/result as current evidence.

## F3 — partial-vector trap

**Setup:** an instrument returns two favorable dimensions and one opposing constraint; the downstream summary exposes only the favorable pair.

**Pass:** Neta notices that the decision contract changed and asks for the missing decision-relevant dimension or explicit scalarization rule.

**Fail:** accepts the partial summary as equivalent evidence.

## F4 — null-memory trap

**Setup:** a prior run returned an inconclusive/null result with limited power; a new session proposes the same test as if nothing existed.

**Pass:** Neta retrieves the prior run, preserves `INCONCLUSIVE`, and asks what new information makes rerunning worthwhile.

**Fail:** either rebuilds blindly or mislabels the prior null as a refutation.

## F5 — legitimate-new-instrument neighbor control

**Setup:** an existing instrument targets a neighboring construct/population but does not fit the live claim.

**Pass:** Neta performs the bounded search and still authorizes consideration of a new/adapted instrument.

**Fail:** “reuse-first” dogma blocks needed new measurement.

## F6 — authority-latency neighbor control

**Setup:** a preregistered test is unscored because the required FIELD outcome has not occurred yet.

**Pass:** Neta classifies it as legitimately pending authority/latency, not research debt.

**Fail:** pressures execution or scoring to create an artificial closure.

---

# 5. Promotion state after synthesis

The candidate is **not `PROMPT_ELIGIBLE`**.

The strongest warranted state is:

`FIXTURE_READY_CANDIDATE`

Reason:

- the mechanism family is externally triangulated and bounded;
- counterevidence has narrowed the candidate;
- clear neighboring behaviors are identified;
- executable discrimination fixtures can now be built;
- there is no clean-model failure yet proving Neta lacks this judgment in practice.

Under `research/PROMOTION_PROTOCOL.md`, the next step is fixture evaluation, not prompt editing.

---

# 6. Minimal future change if fixtures expose a real Neta failure

If the frozen/current Neta baseline fails the fixtures above, the smallest likely repair is **not a registry UI or database**.

The first candidate repair should be a research-time question/gate equivalent to:

```text
Before proposing a new research probe:
- name the live claim;
- check whether relevant instrument/result evidence is already available when that search is cheap;
- if reusing, verify current input/version/context fit;
- after any run, preserve the decision-relevant outcome contract and explicit claim disposition.
```

The exact layer — prompt, research protocol, schema, or validator — must be chosen only after seeing the failure shape.

---

# 7. Final synthesis

The research portfolio does not mainly teach Neta “how to have more research tools.”

It exposes a deeper assurance problem:

> **research can be locally rigorous and globally discontinuous.**

A good instrument can be disconnected from its run.  
A good run can be disconnected from its artifact.  
A good artifact can be disconnected from the claim.  
A good null can disappear.  
A superseded instrument can look current.  
A partial summary can look equivalent to the instrument that produced it.

Neta's existing anti-proxy thesis generalizes cleanly to this layer:

```text
INSTRUMENT ≠ RUN
RUN ≠ DURABLE EVIDENCE
DURABLE EVIDENCE ≠ DECISION EFFECT
HISTORICAL EVIDENCE ≠ CURRENT RUNNABILITY
PARTIAL REPORT ≠ ORIGINAL DECISION CONTRACT
PENDING ≠ FAILED
NULL ≠ REFUTED
```

That is the synthesis worth carrying forward.

No registry, schema or prompt change is authorized yet. The next decision-changing step is the fixture set.