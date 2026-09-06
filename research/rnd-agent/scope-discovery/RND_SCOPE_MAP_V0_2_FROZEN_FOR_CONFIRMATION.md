# R&D Scope Map v0.2 — Frozen for Confirmation

Status: `CONFIRMATORY_SCOPE_HYPOTHESIS_FROZEN · ZERO_CONFIRMATORY_CASES_COUNTED`
Date frozen: 2026-09-06
Supersedes for confirmation only: discovery region label `R4_NETA_PRIMARY`.
Does not rewrite historical v0.1 artifacts.

## Primary hypothesis

> **R&D's highest marginal value concentrates where a consequential decision remains open and there is a nontrivial unresolved choice about whether, how, or how much to learn before responsibly advancing that decision.**

Compact form:

```text
CONSEQUENTIAL DECISION
× NONTRIVIAL EPISTEMIC ALLOCATION
→ R&D CORE CANDIDATE
```

This is a hypothesis to confirm/falsify, not a canonical boundary.

---

## Frozen regions

### R1 — EPISTEMIC_ALLOCATION_CORE

All required:
- `DECISION_CONSEQUENCE = MATERIAL_CONSEQUENTIAL`
- `EPISTEMIC_ALLOCATION_BURDEN = NONTRIVIAL`
- `RESOLUTION_STRUCTURE ∈ {CHANNEL_SELECTION_REQUIRED, RESEARCH_METHOD_REQUIRED}`
- `LEARNING_PHASE ∈ {PRE, MID, POST}`

Interpretation:
At least two admissible learning/evidence moves differ materially in authority, cost, delay, validity, contamination, reversibility, reach or expected decision value, and that allocation choice is unresolved before R&D output.

Prediction: highest marginal R&D value.

### R2 — OBVIOUS_LEARNING_NEIGHBOR

- material decision may exist;
- one cheap/reversible/legitimate discriminator or direct learning move clearly dominates.

Prediction: act/test first; full R&D usually adds ceremony.

### R3 — DIRECT_AUTHORITY_OR_EXECUTION

Any:
- epistemic allocation burden is `NONE`;
- exact material question has one direct legitimate authority;
- OWNER has settled the relevant goal/constraint;
- work path is already justified and remaining task is execution.

Prediction: route/act; no material full-R&D delta.

### R4 — DOMAIN_METHOD_PRIMARY

The central unresolved object is a domain-method judgment/tradeoff rather than a learning-allocation judgment.

Examples:
- Neta: raw product signal → competing mechanisms → discriminator → intervention;
- Architecture: requirements/constraints/quality attributes → structural options → tradeoffs → architecture decision;
- any future earned domain method with its own legitimate judgment function.

Prediction:
- domain method is primary;
- R&D enters only if a separable `whether/how/how much to learn` decision appears.

### R5 — LOW_LOCAL_CONTROL

Low-consequence fact, explanation, generation, critique, communication or reversible local action.

Prediction: direct baseline dominates cost/latency; R&D bypass.

---

## Frozen pre-outcome axes

### A — DECISION_CONSEQUENCE
- `LOW_LOCAL`
- `MATERIAL_CONSEQUENTIAL`

### B — EPISTEMIC_ALLOCATION_BURDEN
- `NONE`
- `OBVIOUS`
- `NONTRIVIAL`

### C — RESOLUTION_STRUCTURE
- `SINGLE_DIRECT_AUTHORITY`
- `CHANNEL_SELECTION_REQUIRED`
- `RESEARCH_METHOD_REQUIRED`
- `DOMAIN_METHOD_REQUIRED`

`DOMAIN_METHOD_REQUIRED` is added in v0.2 to represent a legitimate domain-method judgment without pretending it is a direct truth authority or an R&D learning-allocation problem.

### D — LEARNING_PHASE
- `PRE`
- `MID`
- `POST`

---

## Secondary modifiers — not independent scope regions

Record:
- high cost;
- high delay;
- contamination/reactivity risk;
- high reversibility;
- reusable epistemic-policy effect;
- lineage/independence issue.

A modifier may become a primary axis only after a future discovery version shows a stable independent boundary effect. No such promotion is allowed inside v0.2 confirmation.

---

## Primary confirmatory claims

### C1 — R1 positive core

R1 meets all frozen HIGH_VALUE_CORE criteria:
- anytime/simultaneous 95%-valid `LCB(win rate) > 0.50`;
- `UCB(loss rate) < 0.05`;
- conservative net-benefit lower bound > 0;
- minimum 60 independent adjudicable cases;
- PRE/MID/POST balance;
- domain balance.

### C2 — R2 separation

R1 has materially greater net benefit than R2; otherwise the boundary must merge or become conditional.

### C3 — R3 separation / authority safety

R&D does not add positive marginal value by reasoning past direct legitimate authority/execution, and authority-violation upper bound remains < 0.05.

### C4 — R4 separation

R&D does not replace the primary domain method. R&D earns invocation only when a separable epistemic-allocation decision is present.

R4 is not assumed to be zero-value universally; it is a route-dependent boundary claim.

### C5 — R5 low/local burden discipline

Full R&D does not earn its incremental burden on low/local direct tasks.

---

## Comparator freeze

Primary A/B comparator, where executable:
- same base model/version;
- same tools/context;
- `A = strong general/local-response baseline`;
- `B = CURRENT_RND frozen prompt`;
- randomized identity/order;
- identity hidden from adjudicator.

Boundary comparators:
- R4: legitimate domain method when available;
- R3: matching OWNER/REPO/ENVIRONMENT/FIELD authority when factual correctness depends on it.

---

## Adjudication freeze

Primary labels:
- `MATERIAL_RND_WIN`
- `TIE_NO_MATERIAL_DELTA`
- `MATERIAL_RND_LOSS`
- `UNADJUDICABLE`

A win must materially improve the next decision path enough to justify R&D burden. Terminology, verbosity, caution or agreement do not count.

The 95% stream requires blind adjudication by a different model lineage or qualified human/domain adjudicator. Same-model self-adjudication counts zero toward confirmation.

---

## Sequential stopping rule

Use the sequentially valid procedure frozen in `RND_SCOPE_DISCOVERY_PROGRAM_V0_1.md`:
- preferred anytime-valid confidence sequence;
- fallback prespecified familywise alpha-spending exact one-sided binomial bounds.

Do not repeatedly inspect ordinary fixed-N 95% intervals for stopping.

---

## Contamination register

The following are discovery/training only and contribute zero confirmation cases:
- Yishumi prompt bank;
- QD shadow-gate / narrow-telos cases;
- Neta Hebrew TRAIN seed;
- R&D TRAIN controls;
- Architecture historical benchmark used in discovery;
- applied/zetetic epistemology and VOI authored tests;
- cost/reversibility and authority-respect controlled pairs;
- any artifact created before this freeze that was inspected in designing v0.2.

---

## Start state

`CONFIRMATORY_N = 0`

`R1 = UNKNOWN`
`R2 = UNKNOWN`
`R3 = UNKNOWN`
`R4 = UNKNOWN`
`R5 = UNKNOWN`

No region may be promoted from discovery point estimates.
