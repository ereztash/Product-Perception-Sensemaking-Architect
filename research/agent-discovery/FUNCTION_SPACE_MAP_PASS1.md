# Agent Discovery — Function Space Map Pass 1

Status: `DISCOVERY_PASS_1 · REPO_GROUNDED + EXTERNAL_REFERENCE · NOT_AGENT_PROMOTION`
Date: 2026-09-06

## Question

What are the orthogonal judgment functions a system for consequential decisions must cover, which are already owned, and which residuals are plausible enough to test?

The map separates:
- **authority** — who can settle a claim/constraint;
- **cross-cutting judgment function** — a method that can recur across domains;
- **domain method** — a specialized judgment function whose object is domain-specific;
- **coordination/infrastructure** — state/routing/trace rather than substantive judgment;
- **execution** — changing state rather than deciding what is true/justified.

## External reference frames used only to check completeness

These references do not create repo capabilities by analogy. They are completeness probes.

### Decision Quality

The Decision Quality framework separates:
- frame;
- alternatives;
- information;
- values/tradeoffs;
- reasoning;
- commitment to action.

Source: https://decisionquality.org/decision-quality-in-practice

### NASA Systems Engineering

NASA's common technical process model separates:
- stakeholder expectations;
- technical requirements;
- logical decomposition;
- design solution;
- product realization;
- verification/validation;
- cross-cutting decision analysis and technical management.

Sources:
- https://www.nasa.gov/reference/4-0-system-design-processes/
- https://www.nasa.gov/reference/6-8-decision-analysis/

### SEBoK / ISO 15288 framing

Decision management is a structured analytical process for identifying, characterizing and evaluating alternatives against criteria while the authorized decision maker retains final choice.

Source: https://sebokwiki.org/w/index.php?title=Decision_Management

These frameworks suggest possible functions. Only repo evidence can earn a candidate.

---

# Map

| Function | Exact judgment object | Current owner/form | Pass-1 status |
|---|---|---|---|
| Intent / values / accepted risk | What outcome, preference, constraint or tradeoff is legitimate? | `OWNER` authority | `COVERED_AS_AUTHORITY` |
| Product signal sensemaking | What mechanism may explain a raw product/perception signal; what discriminator is cheapest; what intervention is currently justified? | `NETA` peer | `COVERED` |
| Epistemic allocation | Whether/how/how much to learn; which evidence program deserves resources; when to stop | `RND` candidate telos/scope | `COVERED_CANDIDATE_BOUNDARY_STILL_CONFIRMING` |
| Question/front-door qualification | Is the named object/resource already earned, or is a cheaper upstream distinction needed? | deterministic/front-door hypothesis + R&D/Neta | `DO_NOT_SPLIT_YET` |
| Evidence quality / epistemic hygiene | lineage, independence, authority, null states, falsifiers, provenance | shared epistemic kernel + R&D/Neta gates | `COVERED_CROSS_CUTTING` |
| Need → requirement translation | Which stakeholder/owner needs become architecture-significant, verifiable requirements/quality attributes and acceptance measures? | no dedicated current owner; architecture research names the gap | `RESIDUAL_CANDIDATE` |
| Structural architecture judgment | Which system structure best satisfies requirements/constraints/invariants under dependency/failure/migration tradeoffs? | Scaffold currently; `Architecture Decision Discriminator` candidate capability | `RESIDUAL_CANDIDATE_CAPABILITY` |
| General alternative/tradeoff analysis | Given owner priorities, feasible alternatives and current knowledge, how do alternatives compare; is ranking robust; what recommendation is decision-legible? | generic reasoning / OWNER handoff; no frozen capability | `OPEN_RESIDUAL_NEEDS_OBSERVATORY` |
| Domain diagnosis | What mechanism is active in debugging/security/legal/finance/etc.? | matching domain method/expert/tool | `NOT_GENERAL_PEER_BY_DEFAULT` |
| Risk analysis | What adverse outcomes/exposures matter and how do options change them? | modifier inside domain method / Decision Analysis / R&D uncertainty; OWNER accepts risk | `NO_ORTHOGONAL_PEER_EVIDENCE` |
| Coordination / dependency sequencing | Which unresolved claim/peer/authority must move first; how are dependencies/handoffs preserved? | deterministic Calibration Loop + handoff protocol | `COVERED_AS_COORDINATION_UNTIL_FAILURE` |
| Execution planning/action | How to perform an already-justified state change | human/tool/runtime + decision-execution-learning contract | `NOT_AGENT_EARNED` |
| Verification of changed state | Did the intended implementation/runtime state actually occur? | `REPO` / `ENVIRONMENT` / relevant authority | `AUTHORITY_NOT_AGENT` |
| Validation / field outcome | Did the external human/world outcome occur? | `FIELD` | `AUTHORITY_NOT_AGENT` |
| Learning / update | What claim/resource/capability state changes after outcome? | R&D + peer-specific promotion gates | `COVERED` |
| Memory / lineage continuity | Can later work recover what was decided, why, evidence, supersession, reversal? | schemas/docs/trace/kernel | `INFRASTRUCTURE_NOT_PEER` |

---

# Important structural distinction: cross-cutting vs domain peer

The current ecosystem mixes two legitimate peer shapes:

### Cross-cutting method

Example: R&D.

Its object is not a specific domain. It regulates the allocation of learning/evidence across domains.

### Domain method

Example: Neta.

Its object is product perception/design sensemaking.

Architecture, debugging, security, legal or finance expertise belong to this second class unless evidence shows a cross-domain judgment underneath them.

This distinction prevents a false MECE test where every professional specialty becomes a peer.

---

# Residual 1 — Need → architecture-significant requirement translation

## Evidence

The architecture research already identified a front-door gap:

```text
ACCEPTED NEED
→ ARCHITECTURE-RELEVANT REQUIREMENT / QUALITY ATTRIBUTE
→ MATERIAL PRESSURE
→ ARCHITECTURE OPTIONS
```

The historical architecture benchmark starts too late: its cases already provide an architecture-level decision question, constraints and authorities.

External systems-engineering references independently separate stakeholder expectations/needs from technical requirements and architecture/design.

## Candidate judgment

> Which accepted need/goal/constraint must become a measurable architecture-significant property, under what context/workload, and what observation would establish satisfaction?

Possible output contract:

```text
need_claim
stakeholders
architecture_relevance
required_property
context_or_workload
acceptance_measure
conflicting_requirement
trace_link
```

## Current disposition

`CANDIDATE_SUBCAPABILITY`

Not a separate agent yet. Strong prior that this belongs as the **front door of an Architecture/System capability**, not a new peer beside Architecture.

---

# Residual 2 — Architecture Decision Discrimination

## Evidence

Existing candidate contract explicitly carries:
- boundary;
- constraint;
- invariant;
- dependency direction;
- state authority;
- failure domain;
- change propagation;
- migration/reversibility;
- tradeoff ledger;
- decision lineage.

The repo has 12 frozen historical architecture cases, but the valid baseline-vs-candidate result is still unmeasured because the current evaluator has seen GOLD anchors.

## Candidate judgment

> Given validated architecture-relevant requirements and current system facts, which structural alternative best satisfies them, what tradeoff is accepted, and what migration/reversal path preserves optionality?

## Current disposition

`CANDIDATE_CAPABILITY_NOT_AGENT`

The next evidence is a clean-context baseline comparison, not more role design.

---

# Residual 3 — General Decision Analysis / Tradeoff Structuring

## External functional distinction

NASA Decision Analysis explicitly operates on:
- decision to be made;
- decision criteria/priorities;
- alternatives;
- current information/uncertainty;
- evaluation method;
- alternative comparison;
- recommendation to the decision authority.

The decision authority remains free to select or revise criteria.

This creates a plausible orthogonal boundary with R&D:

```text
DECISION ANALYSIS
current priorities + alternatives + current knowledge
→ compare options / robustness

if uncertainty could change ranking
→ R&D: is further learning worth buying?

if ranking is robust enough
→ OWNER: commit / choose / revise values
```

## Repo evidence against premature promotion

Existing `OWNER_DEFER` cases (Actual Budget OSS-0014, SparkleShare OSS-0030, Organic Maps OSS-0034, SiYuan OSS-0039) mostly stop because owner policy/intent is missing. They do **not** show that a formal tradeoff method is needed once owner priorities are known.

Question-discovery natural prompts include prioritization/strategy situations, but they do not isolate a recurring post-information alternative-evaluation failure.

Therefore the current repo has an **observability gap**, not a proven capability gap.

## Candidate judgment

> Given explicit owner priorities/mandatory constraints, viable alternatives and sufficiently bounded evidence, make the tradeoffs and ranking robustness legible without replacing owner authority.

Minimal output might be:

```text
decision
mandatory_criteria
preference_criteria
alternatives
consequence_by_criterion
uncertainties_that_could_flip_ranking
robustness
recommendation_or_close_set
owner_choice_needed
```

## Current disposition

`OPEN_RESIDUAL_NEEDS_OBSERVATORY`

Do not build a Decision Agent. First collect natural cases that begin **after** OWNER values/constraints are explicit.

---

# Rejected / not-earned candidates in Pass 1

## Orchestrator Agent

`NOT_EARNED`

Current deterministic routing and machine-readable handoff protocol already define dependency/authority flow. The ecosystem telos explicitly requires observed coordination failure before a learned orchestrator.

No recurring material failure family was found in the inspected traces showing that routing/dependency reasoning cannot be handled by the current loop/protocol.

## Execution Agent

`NOT_EARNED`

The repo explicitly treats Decision → Execution → Verified State → Outcome → Learning as a trace/contract problem first. Promotion requires 10–15 real traces showing a recurring reasoning gap after planning, artifact references and verification are already present.

No such evidence is currently accumulated.

## Verification / Validation Agent

`REJECT_AS_AUTHORITY_CONFUSION`

REPO/ENVIRONMENT/FIELD establish reality. A reasoning method may design a verification plan, but it cannot become truth authority by being called an agent.

## Debugging Agent

`DOMAIN_METHOD_ONLY`

External R&D scope testing produced a direct negative control: Paperclip's multi-hypothesis flaky-test problem was ordinary domain debugging/test synchronization, not a separate epistemic-allocation function. Pulsar's deep deadlock diagnosis similarly remained engineering-domain work.

## Epistemology Agent / VOI Agent

`ABSORBED_BY_RND`

Applied/zetetic epistemology and VOI challengers did not produce unique next-move delta over current R&D in the controlled runs. They remain theory/eval lenses and possible internal rules, not peers.

## Question Discovery Agent

`FRONT_DOOR_GATE_HYPOTHESIS`

Prior comparison found no separate epistemic capability beyond R&D + routing/Neta. Preserve as lightweight front-door behavior unless future evidence shows independent value.

## Strategy Agent

`OWNER_BOUNDARY_UNRESOLVED`

Strategy/telos/accepted tradeoffs remain OWNER authority. A Decision Analysis capability may structure options without owning strategy. No independent Strategy-peer judgment has been isolated.

## Risk Agent

`CROSS_CUTTING_MODIFIER_NOT_EARNED`

Risk enters evidence thresholds, architecture tradeoffs, decision criteria, reversibility and owner risk acceptance. No recurring residual currently requires a separate peer rather than those existing contexts.

## Memory Agent

`INFRASTRUCTURE_NOT_JUDGMENT`

Lineage/provenance/supersession/trace are durable infrastructure requirements. No evidence currently shows that a separate reasoning peer is required to own memory.

---

# Pass-1 candidate queue

Priority is evidential, not implementation priority.

1. `ARCHITECTURE_DECISION_DISCRIMINATOR` — candidate capability already specified; comparative delta unmeasured.
2. `NEED_TO_ARCHITECTURE_REQUIREMENT_TRANSLATION` — candidate subcapability/front door; needs own cases and neighbor tests.
3. `GENERAL_DECISION_ANALYSIS` — plausible cross-cutting residual, but currently an observability gap; needs natural post-OWNER cases before capability design is justified.

Everything else is currently better explained as existing peer, authority, domain method, protocol, execution/tooling or infrastructure.
