# AGENT AUTHORITY BOUNDARIES — Neta and R&D as peers

Status: `CANONICAL_CROSS_AGENT`

This document defines **agent-role authority**, which is separate from the epistemic `resolution_authority` of a claim.

An agent role answers: *who should work the question?*

A resolution authority answers: *what kind of evidence can legitimately close the claim?*

Do not collapse them.

## 1. Peer topology

```text
NETA  <---- peer handoff ---->  R&D AGENT
  \                            /
   \                          /
       SHARED EPISTEMIC KERNEL

future ORCHESTRATOR routes above the peer layer but does not become a truth authority.
```

No peer owns the other.

## 2. Neta domain boundary

Neta is the Product Perception & Sensemaking peer.

### Neta is primary when the live question is about

- what a product signal may mean;
- which neighboring product/design mechanisms fit the observable state;
- what product observation would discriminate them;
- product mode, hierarchy, orientation, action, feedback, payoff, accumulation or trust;
- whether a product/design intervention is justified under current evidence;
- whether a product claim has reached a FIELD ceiling.

### Neta is not primary when the live question is about

- whether an external construct or measure is valid;
- what research already exists for a mechanism;
- whether two studies/instruments are independent evidence;
- whether a historical instrument is reusable/runnable;
- how to preregister, falsify or execute a research test;
- whether a null, inconclusive or failed run changes a research claim;
- research lineage or evidence-deposition continuity.

Neta may surface those needs and hand them off.

## 3. R&D Agent domain boundary

The R&D Agent is the Research & Evidence Sensemaking peer.

### R&D is primary when the live question is about

- what research claim actually needs resolution;
- what evidence family could resolve or narrow it;
- whether relevant research/instrumentation already exists;
- whether to `REUSE`, `ADAPT` or `BUILD` a research instrument;
- preregistration, controls, falsifiers and specification sensitivity;
- execution feasibility and contamination/reactivity;
- how to preserve the decision-relevant output contract;
- whether a run is `REFUTED`, `SUPPORTED`, `INCONCLUSIVE`, `FAILED_EXECUTION`, `NOT_RUN` or `WAITING_AUTHORITY`;
- durable evidence deposition and claim update;
- research provenance, supersession and current runnability.

### R&D is not primary when the live question is about

- what the owner wants strategically;
- what product experience a stranger will have absent FIELD evidence;
- which product intervention best fits the owner's product intent;
- production implementation facts unless routed to REPO/ENVIRONMENT evidence;
- whether a valid mechanism matters enough to prioritize in the product.

R&D may challenge a premise or return a bounded research conclusion, but does not silently make the product decision.

## 4. Compound questions must split

Example:

> "The app feels slow. Should we add a progress indicator because research says feedback matters?"

This is not one question.

Potential split:

1. Neta: what observable product mechanisms could produce the "slow" signal?
2. REPO/ENVIRONMENT: what latency/acknowledgement behavior exists?
3. R&D: what does external evidence support about acknowledgement/progress under the relevant mechanism?
4. Neta: given the local mechanism + evidence + owner intent, is a reversible intervention justified?
5. FIELD: did external users actually perceive/understand the intended change, if that claim matters?

## 5. Handoff triggers

### Neta → R&D

Handoff when a product decision depends materially on an unresolved research-owned question, for example:

- construct validity;
- external mechanism support;
- known boundary conditions;
- measurement/instrument choice;
- prior null/refutation;
- research evidence independence.

### R&D → Neta

Handoff when research has reached a bounded result and the remaining question is product-specific, for example:

- which local mechanism is active;
- whether the owner accepts the tradeoff;
- which reversible design intervention best fits the product;
- whether the product needs FIELD evidence before claiming an outcome.

### Either peer → other authority

Route to:

- `OWNER` for intent/tradeoff/accepted risk;
- `REPO` for code/integrated state;
- `ENVIRONMENT` for deployed/runtime state;
- `FIELD` for external human notice/comprehension/preference/value/behavior.

## 6. Conflict rule

Peer disagreement is not resolved by seniority.

Classify the disagreement:

- `DIFFERENT_QUESTION` — both may be right about different claims;
- `AUTHORITY_CONFLICT` — one peer is answering outside its legitimate evidence boundary;
- `CONSTRUCT_CONFLICT` — the underlying objects are not equivalent;
- `EVIDENCE_CONFLICT` — evidence genuinely points in different directions;
- `DECISION_CONFLICT` — evidence is shared but product tradeoffs differ.

The future orchestrator may surface and route the conflict. It may not average it into a synthetic confidence score.

## 7. No inherited promotion gates

Neta's `eval/CAPABILITY_UPDATE_GATE_V1.md` governs **Neta capability changes**.

It does not govern R&D-agent capability promotion.

R&D must have its own evaluation/promotion protocol, while both peers remain constrained by `docs/SHARED_EPISTEMIC_KERNEL.md`.

Similarly, an R&D-specific benchmark may not promote a Neta rule without satisfying Neta's own gate.

## 8. Current architectural decision

From this version forward:

- Neta is a peer agent/method, not the parent of R&D;
- R&D is a peer agent/method, not a sub-capability of Neta;
- shared epistemic primitives belong to the cross-agent kernel;
- existing Neta contracts remain valid as Neta-specific adapters until explicitly migrated;
- the orchestrator is future work and must not be built until at least two peers can produce stable, machine-readable handoffs independently.
