# Question Discovery Natural-Prompt Benchmark v1 — Challenger

Status: `CHALLENGER_FROZEN · SAME_MODEL_MANUAL_RUN · RETROSPECTIVE_NATURAL_CORPUS`
Date: 2026-09-06

Contract:

```text
CURRENT QUESTION
→ UNDERLYING DECISION
→ PREMATURE COMMITMENT (if any)
→ UPSTREAM DECISION-CONTROLLING UNCERTAINTY
→ DECISION-GRADE QUESTION or NO_REFRAME
→ CHEAPEST ADMISSIBLE CHECK
```

---

## NP-01 — Deploy CRM to Vercel

### QD disposition
`REFRAME`

### Underlying decision
Make the CRM reliably reachable and operable with the least deployment/migration burden appropriate to its current architecture.

### Premature commitment
`Vercel` is treated as the deployment target before the app's runtime/state requirements are compared with the platform boundary.

### Upstream uncertainty
What runtime properties does the current CRM actually require: persistent process, local/persistent filesystem, database connectivity, background work, long-running requests, scheduled jobs, environment configuration, stable URL/domain, and operational visibility?

### Decision-grade question
> **Which deployment target satisfies the CRM's current runtime/state/operability requirements with the least adaptation cost, and is Vercel actually inside that feasible set?**

### Cheapest check
Inventory the app's runtime/state assumptions from the repo and compare them against candidate platform constraints before modifying deployment code.

### Decision delta
Changes `deploy to Vercel` into `choose deployment target after a compatibility discriminator`.

### Avoided work
Potential Vercel-specific adaptation, deployment debugging, and later platform migration if the runtime is a poor fit.

---

## NP-02 — Use a Sheet as lead-state store

### QD disposition
`REFRAME`

### Underlying decision
Create one durable, inspectable current state for lead status and next actions that both the user and automation can safely update.

### Premature commitment
`Google Sheet` is treated as the source of truth before the required state semantics are specified.

### Upstream uncertainty
Does the workflow need only simple human-readable rows, or also concurrent writes, transactional consistency, audit history, deduplication, identity resolution, relationship state, permission boundaries, and automated transitions?

### Decision-grade question
> **What properties must the lead-state authority preserve, and is a Sheet the cheapest adequate source of truth—or should it be only a human-readable projection over another authority?**

### Cheapest check
Map the writes that must occur in one representative lead lifecycle: who writes, what must never conflict, what needs history, and what the user must edit directly. Test whether a Sheet preserves those invariants without manual repair.

### Decision delta
Changes `build a Sheet tracker` into `choose source-of-truth semantics first; Sheet may survive as authority or projection`.

### Avoided work
Building automations around a store that later cannot preserve identity/state/history safely.

---

## NP-03 — Maximize ROI of a research program

### QD disposition
`REFRAME`

### Underlying decision
Choose the next resource expenditure that most cheaply removes uncertainty controlling a consequential decision.

### Premature commitment
`the research` is already selected as the resource class before research is compared with repo inspection, field observation, instrumentation, a reversible test, or simply acting.

### Upstream uncertainty
What exact unresolved uncertainty controls the next decision, and which admissible resource move can resolve it most cheaply?

### Decision-grade question
> **Across research, repo/environment inspection, field evidence, reversible testing, building, waiting or stopping, which next move has the highest expected decision value per cost for the live decision?**

### Cheapest check
Name the decision and the one fact that could change it, then compare the minimum-cost ways to obtain that fact. Research competes rather than receives automatic priority.

### Decision delta
Changes `optimize this research` into `first decide whether research is the highest-ROI resource at all`.

### Avoided work
A comprehensive research program whose result would not change the decision.

---

## NP-04 — Use personal Lichess account data

### QD disposition
`REFRAME`

### Underlying decision
Acquire new evidence that materially improves a product/research decision not already resolvable from code or existing evidence.

### Premature commitment
The availability of a large personal game history is treated as sufficient reason to export/analyze it.

### Upstream uncertainty
Which open claim requires behavioral/game evidence, and can one account's historical games legitimately resolve or narrow that claim without being mistaken for population/generalization evidence?

### Decision-grade question
> **Which currently unresolved product/research claim could this account history materially discriminate, and what exact subset/measurement would be sufficient to change the decision?**

### Cheapest check
Crosswalk open claims against required evidence/reality. Only if a claim maps to personal historical games should the smallest sufficient sample/export be run first.

### Decision delta
Changes `export the account because data may help` into `export only the data required by a named unresolved claim`.

### Avoided work
Full-history extraction/engine analysis that produces interesting statistics but no decision delta.

---

## NP-05 — API key export feasibility

### QD disposition
`NO_REFRAME`

The question is a bounded feasibility question. The user is not yet asserting that the export is valuable; they are asking whether providing a credential enables the operation.

### Direct answer preserved
Yes, if the service exposes the required endpoint and the key has sufficient permission; the credential should be used only for the requested export and not persisted in repo/history.

### Cheapest check
Verify endpoint and permission scope.

### Why no deeper question
Replacing this with a strategy question would add friction before answering a concrete capability dependency.

---

## NP-06 — Marketing assets for Shaked Brand

### QD disposition
`REFRAME`

### Underlying decision
Decide what to create next to increase the probability of a specific acquisition/sales motion succeeding.

### Premature commitment
`marketing assets` is treated as an inventory to complete, which can reward completeness rather than movement of the current buyer journey.

### Upstream uncertainty
Where is the next intended customer path currently blocked: recognition, trust/proof, offer comprehension, conversion/contact, sales support, or follow-up?

### Decision-grade question
> **What is the next customer decision Shaked Brand needs to enable, what evidence/content is currently missing for that decision, and what is the minimum asset that removes that bottleneck?**

### Cheapest check
Choose the next real acquisition motion and walk it end to end with existing assets. Build only the first missing artifact that blocks movement.

### Decision delta
Changes `make a complete asset list` into `build the highest-leverage missing asset for the next real customer decision`.

### Avoided work
Creating decks, pages, case-study formats or content libraries before any live path requires them.

---

## NP-07 — Instagram video strategy

### QD disposition
`REFRAME_WITHIN_OWNER_INTENT`

The user's choice to create authentic Instagram videos is treated as an OWNER decision, not something the capability is authorized to undo.

### Underlying decision
Determine what each video must change in the viewer so the series accumulates toward qualified conversations rather than becoming disconnected content output.

### Premature commitment
No material premature commitment to the channel is asserted. The weaker object is `the bottom line of each video` as isolated content rather than a sequence of audience decisions/uncertainties.

### Upstream uncertainty
What must a relevant viewer believe, understand or do after each stage before a conversation becomes a plausible next move?

### Decision-grade question
> **Across the video series, which sequence of audience uncertainties must be resolved—from recognition of the problem, through trust in your way of working, to a reason to talk—and what single transition should each video own?**

### Cheapest check
Define the intended viewer state before and after the next three videos, then judge scripts by whether each one can plausibly produce one transition; do not optimize frequency/format before that.

### Decision delta
Changes `content topics/bottom lines` into `a sequence of decision-state transitions while preserving the chosen Instagram/video strategy`.

### Avoided work
Producing many individually good videos that do not accumulate toward a business outcome.

---

## NP-08 — Create a domain for deployed CRM

### QD disposition
`NO_REFRAME`

Given a deployed CRM that the owner wants to access through a stable branded address, a custom domain is a bounded, low-cost, reversible infrastructure step. No higher-order uncertainty is needed to answer whether a domain is appropriate.

### Direct answer preserved
Yes: attach the desired domain to the production deployment, configure DNS, verify TLS and ensure the production target is correct.

### Cheapest check
Confirm the production deployment is stable and the domain can point to it.

### Why no deeper question
Re-opening hosting/branding strategy would delay a cheap implementation whose purpose is already clear.

---

## NP-09 — Meaning and importance of maintenance

### QD disposition
`NO_REFRAME`

This is a conceptual learning question, not a consequential decision that embeds a premature mechanism. Answering the concept directly is the correct move.

### Direct answer preserved
Maintenance/maintainability concerns the continuing ability and cost to understand, correct, operate and change a system after initial delivery; it matters because future changes, failures, dependencies, people and environments create ongoing work and risk.

### Why no deeper question
There is no evidence that a different question would change a live decision at this point.

---

## NP-10 — MECE layers for repo gaps

### QD disposition
`REFRAME`

### Underlying decision
Create a decomposition that can reliably locate material gaps, assign them to the right authority/capability, and score completeness without overlap or blind spots.

### Premature commitment
`product / engineering / operations` is treated as the candidate unit of MECE decomposition before testing whether these are orthogonal dimensions. They mix purpose/value, construction qualities and lifecycle/runtime responsibility.

### Upstream uncertainty
What decomposition axis serves the decision: system functions, quality attributes, lifecycle stages, authorities, or ownership domains? A taxonomy cannot be MECE if rows belong to different axes.

### Decision-grade question
> **What single decomposition axis gives mutually exclusive and collectively exhaustive coverage of the system functions that must be owned, and how does maintainability map onto that axis without becoming a competing layer?**

### Cheapest check
Take several known gaps and attempt to assign each to exactly one category under the proposed axis. Any repeated multi-membership or unclassifiable case falsifies MECE. Compare the three-layer proposal against a function-level coverage map before scoring the repo.

### Decision delta
Changes `is maintainability another layer / are these three layers enough?` into `choose the decomposition axis first, then classify gaps`.

### Avoided work
Building scorecards whose categories overlap, omit responsibilities, or force cross-cutting qualities into arbitrary buckets.