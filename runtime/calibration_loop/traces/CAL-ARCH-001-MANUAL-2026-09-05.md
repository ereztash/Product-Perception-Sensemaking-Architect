# CAL-ARCH-001 — Manual Calibration Run

Date: 2026-09-05  
Execution: `MANUAL_ROLE_SEPARATED`  
API/model adapters: not used  
Status: `COMPLETE_WITH_SHARED_MODEL_LINEAGE_LIMIT`

## Independence caveat

The R&D, Neta and Scaffold passes below were executed manually as role-separated passes in one ChatGPT session.

They were kept logically separate before synthesis, but they share one foundation model/session lineage. Therefore agreement among them is **not independent triangulation**. The purpose of this run is to test decision structure and resource delta, not to claim three independent evidence families.

## Calibration task

### Telos

Develop the most useful architecture-expertise capability for the peer-agent system without building more machinery than the current state justifies.

### Blocked decision

> What is the smallest evidence-backed Architecture Agent capability and evaluation contract worth building next?

### Starting default

Do not build a full Architecture Agent until the missing architecture-specific judgments and their tests are discriminated.

---

# Pass 1 — R&D v0.2 DIAGNOSE

## Material question

Which architecture-specific judgment, if any, is repeatedly valuable enough that the system should internalize it rather than continue borrowing broad reasoning from the Scaffold plus REPO/ENVIRONMENT facts?

## Bottleneck / miscalibration

The system currently has a desired role label (`Architecture Agent`) but not yet evidence that a distinct agent is the cheapest resource configuration.

The missing object is not architecture knowledge in general. It is evidence about a **unique decision capability** that existing resources fail to supply cheaply/reliably.

## Resource assessment

| Resource | Expected contribution | Authority ceiling | Current uncertainty |
|---|---|---|---|
| R&D | calibrate build-vs-borrow decision; recover prior architecture cases; test candidate capability | cannot decide OWNER telos or invent REPO/ENVIRONMENT facts | whether repeated architecture failures exist across real cases |
| Neta | detect proxy substitution, premature build, mechanism collapse | not architecture doctrine/research authority | whether `Architecture Agent` is replacing a more precise missing decision |
| Scaffold | generate architecture-specific candidate distinctions/alternatives cheaply | candidate reasoning only; not REPO/ENVIRONMENT/FIELD truth | which architectural judgments are plausibly orthogonal to Neta/R&D |
| REPO | establish actual dependencies, boundaries, state flow, coupling, interfaces | static/current repository facts only | which historical cases reveal architecture-specific decision failures |
| ENVIRONMENT | establish runtime/deployment/performance/failure facts | current environment only | whether static architecture concerns manifest operationally |
| OWNER | define tradeoffs/telos and accepted costs | owner intent/tradeoff only | which architecture outcomes matter most |
| FIELD | external user/organization behavior where architecture creates downstream effects | observed field behavior only | not needed for the first internal capability-discrimination pass |

## Candidate moves

1. `BUILD_FULL_AGENT` — high cost, low reversibility, not yet earned.
2. `USE_SCAFFOLD_ONLY` — cheapest current baseline; risks repeated loss of architecture-specific continuity.
3. `DEFINE_ARCHITECTURE_DECISION_DISCRIMINATOR` — low-cost specification/fixture layer that tests whether a distinct judgment exists before agent implementation.
4. `TARGETED_RESEARCH` — validate candidate judgment objects/failure families against architecture literature and OSS after the decision anatomy is specified.
5. `RECOVER_HISTORICAL_CASES` — test candidate capability on real repo decisions before adding autonomy.

## Needs emitted to routing

- signal_interpretation_ambiguity: true
- multiple_plausible_mechanisms: true
- proxy_substitution_risk: true
- research_to_intervention_transition: true
- broad_reasoning_needed: true
- architecture_alternatives_needed: true
- novel_synthesis_needed: false
- external_research_needed: true
- owner_authority_needed: false
- repo_authority_needed: false
- environment_authority_needed: false
- field_authority_needed: false

## R&D rationale

Invoke Neta to challenge the `agent` framing and Scaffold to propose candidate architecture-specific judgment objects. Then synthesize whether the smallest next investment is a capability discriminator rather than an agent implementation.

---

# Pass 2 — Neta (task-only pass)

## Raw signal

> “The next agent should be an architecture expert.”

## Observable

The system has Neta and R&D as peers plus an external reasoning scaffold. No repeated architecture-specific failure family has yet been shown in this calibration trace.

## Candidate mechanisms

### A. Missing architecture-specific judgment

The existing resources repeatedly fail to distinguish structural alternatives such as boundary placement, dependency direction, failure isolation or migration path.

Would justify a distinct capability if repeated on real cases.

### B. Role-label proxy

“Architecture Agent” may be a convenient name for broad expert reasoning that the Scaffold already supplies cheaply.

If so, a new agent adds identity/coordination cost without buying a unique decision.

### C. Continuity problem disguised as expertise problem

The missing value may be persistence of architecture constraints, invariants and prior decisions across sessions/repos rather than a smarter architecture reasoner.

If so, the intervention is architecture decision memory/contract, not necessarily another autonomous peer.

## One discriminator

Take a small set of historical architecture decisions from the user’s repos and ask:

> **Which decision-relevant distinction changes when we add an architecture-specific contract that is not already produced by R&D + Scaffold + REPO facts?**

If no unique material delta appears, do not build the agent.

## Neta unique delta

`Architecture Agent` is currently an **intervention label**, not yet the diagnosis. The first thing to discriminate is whether the missing resource is expert judgment, continuity/memory, or simply structured use of existing resources.

---

# Pass 3 — Scaffold (task-only pass)

## Candidate architecture-specific judgment space

Architecture expertise plausibly differs from generic reasoning by maintaining a coherent model of:

1. **System boundary** — what belongs inside/outside the unit being designed.
2. **Constraints** — what cannot or should not change.
3. **Invariants** — properties that must remain true across implementations/migrations.
4. **Dependency direction** — who may depend on whom and why.
5. **State/data authority** — where canonical state lives and who may mutate it.
6. **Failure domains / blast radius** — what can fail independently and what propagates.
7. **Change propagation** — how local changes create downstream work/risk.
8. **Temporal coupling** — what must happen together/in order.
9. **Deployment/runtime boundary** — what static structure cannot establish without environment evidence.
10. **Migration/reversibility** — how to move from current to candidate architecture without requiring a big-bang rewrite.
11. **Tradeoff ledger** — what the candidate optimizes and what cost it knowingly accepts.
12. **Decision lineage** — why a boundary/interface exists and what evidence would justify changing it.

## Three candidate capability shapes

### 1. Architecture Auditor

Maps the current system and flags structural risks.

Weakness: can become a metric/pattern museum without changing a decision.

### 2. Architecture Decision Discriminator

Given a live architecture decision, produces a small set of competing structural mechanisms/options, their constraints/invariants, the cheapest discriminating fact, and a reversible next move.

Strength: closest to the shared epistemic architecture and easiest to falsify.

### 3. Architecture Continuity Keeper

Maintains ADR-like lineage, invariants, supersession and drift across changes.

Strength: solves persistence; weakness: may be infrastructure before we prove judgment value.

## Scaffold unique delta

The smallest architecture-specific unit is likely **not a pattern recommendation**. It is a decision object that explicitly carries `boundary + constraints + invariants + dependencies + failure/change cost + migration/reversal`.

---

# Pass 4 — R&D SYNTHESIZE

## Decision before

Do not build the Architecture Agent until missing architecture judgments and tests are discriminated.

## Decision after

**Do not build a full Architecture Agent yet. Build and test an `Architecture Decision Discriminator` capability contract first.**

This is a specification/evaluation capability, not yet an autonomous peer.

## Why this changed the decision

### Neta material delta

Yes.

It changed the object from:

`we need an Architecture Agent`

to:

`we need to establish whether architecture-specific judgment or architecture continuity is the actual missing resource`.

### Scaffold material delta

Yes.

It supplied a candidate set of architecture-specific objects that are not already explicit in Neta/R&D:

`boundary, constraint, invariant, dependency direction, state authority, failure domain, change propagation, temporal coupling, migration/reversibility, tradeoff, decision lineage`.

### R&D material delta

Yes.

It changed resource allocation from high-cost agent construction to a cheaper discriminator + historical-case test + targeted research path.

## Smallest next move

Create:

1. `research/architecture-agent/ARCHITECTURE_DECISION_DISCRIMINATOR_V0.md`
2. visible TRAIN controls covering architecture-specific proxy/failure traps;
3. 8–15 historical architecture decisions from existing repos;
4. a baseline comparison: Scaffold + current peers versus the candidate discriminator;
5. targeted OSS/literature research only for distinctions that survive historical cases or expose a named uncertainty.

## Stop / continue

`CONTINUE`, but **do not implement autonomous Architecture Agent behavior yet**.

## Routing learning

- Neta was material because the task contained a proxy/intervention jump.
- Scaffold was material because architecture-specific candidate decomposition was cheaper to borrow than invent internally.
- Both resources shared one foundation-model lineage in this manual run; their agreement cannot be treated as independent evidence.
- The first promotion-worthy evidence must come from historical/REPO cases and independent architecture research, not from this three-role agreement.

## Reversal condition

Promote toward a full Architecture Agent only if repeated cases show that the candidate architecture decision contract produces material decisions that are not obtained as cheaply/reliably from Scaffold + R&D + repository/environment facts.
