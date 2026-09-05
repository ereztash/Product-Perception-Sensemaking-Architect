# Pass 3 — Solution Architecture Reframe

Status: `MANUAL_PEER_PASS_DECISION_RELEVANT`
Date: 2026-09-06
Task: `CAL-ARCH-SOLARCH-001`

## Decision before

The working question was whether `Solution Architecture / Architecture Decision-Making` is a distinct function/agent, a sub-domain of R&D/Neta, or a better framing of the existing Architecture Decision Discriminator.

Current default before this pass:
- do not create a new agent;
- treat Solution Architecture as a hypothesis about the telos/boundary of the Architecture Decision Discriminator;
- test for an unowned transformation rather than infer one from an industry job title.

## RECOVER

### Existing R&D boundary
R&D v0.2 owns resource↔telos calibration:

`TELOS → CURRENT STATE → RESOURCE MAP → BOTTLENECK/MISCALIBRATION → CANDIDATE MOVES → CHEAPEST DECISION-CHANGING LEARNING → OBSERVED DELTA → RECALIBRATE`

It decides whether architecture work deserves resources, what evidence to buy, and whether to use/adapt/build/retire a capability. It does not thereby own the internal structural design of the technical system.

### Existing Neta boundary
Neta owns product perception/sensemaking discrimination:

`RAW SIGNAL → CONCRETE MOMENT → OBSERVABLE → COMPETING MECHANISMS → CHEAP DISCRIMINATOR → DESIGN DISTINCTION → INTERVENTION/DEFER/FIELD`

It can help establish what a product/user-facing problem means and challenge proxy substitution, but it does not own general architecture doctrine or technical structure selection.

### Existing Architecture Decision Discriminator
The v0 capability already owns one live architecture decision and requires:
- TELOS;
- CURRENT STATE;
- MATERIAL PRESSURE;
- KNOWN CONSTRAINTS;
- AVAILABLE AUTHORITIES.

It then compares structural options using boundaries, invariants, dependency direction, state authority, failure domains, change propagation, temporal coupling, migration, reversibility and tradeoffs.

This means most of what an industry `Solution Architect` does at the structural decision layer is already represented in v0.

## NETA PASS — framing discrimination

### Raw signal
The owner moved one level upward from `System Design concepts` to:

> What stands behind architecture, and what do we call the expert who fits architecture to the need?

### Competing interpretations

1. **DOMAIN-KNOWLEDGE GAP**
   The missing thing is more knowledge of patterns/technologies: caching, queues, sharding, replication, etc.

2. **FIT-TRANSFORMATION GAP**
   The missing thing is the transformation from an accepted need + constraints + required qualities into structural alternatives and tradeoffs.

3. **RESOURCE-ALLOCATION GAP**
   The missing thing is deciding whether architecture deserves effort now, which would already be R&D.

### Cheap discriminator
Hold architecture pattern knowledge constant and vary the explicit need/quality constraints. If the chosen structure changes materially, the missing capability is not pattern recall; it is architecture fitness/requirements translation.

### Neta delta
The industry role label `Solution Architect` must not be treated as evidence for a new peer. The relevant unit is the unowned transformation.

Candidate transformation:

`ACCEPTED NEED + CONSTRAINTS + REQUIRED QUALITIES → STRUCTURAL OPTIONS → TRADEOFF → BOUNDED ARCHITECTURE DECISION`

This transformation is distinct from both Neta's signal interpretation and R&D's resource allocation.

## R&D PASS — resource↔telos calibration

### Material question
Does the current system already own the need→structure transformation cheaply enough, or is there a recurring residual that justifies adapting/building a capability?

### Bottleneck
The Architecture Decision Discriminator v0 appears to start **after** several architecture-relevant inputs are already supplied. It accepts `TELOS`, `MATERIAL PRESSURE` and `KNOWN CONSTRAINTS`, but it does not explicitly define how a messy accepted need becomes architecture-relevant requirements/quality attributes.

Therefore the likely residual is not `Solution Architecture` as a new peer. It is a possible **front-door translation gap** inside the existing architecture capability.

### Resource assessment

#### NETA
Useful when the need begins as a product/user signal and multiple mechanisms are plausible.
Authority ceiling: cannot establish architecture doctrine or choose technical structure merely from user-facing interpretation.

#### R&D
Useful for deciding whether architecture work is the current bottleneck and how much evidence/effort to allocate.
Authority ceiling: resource allocation is not structural design ownership.

#### ARCHITECTURE DISCRIMINATOR v0
Already owns structural alternatives, constraints, invariants, dependencies, failure/change paths, tradeoffs, migration and reversal.
Residual uncertainty: may assume architecture-relevant requirements are already specified enough.

#### OWNER / FIELD / REPO / ENVIRONMENT
OWNER owns telos and accepted tradeoffs; FIELD owns external user/business behavior where needed; REPO and ENVIRONMENT establish current/deployed technical facts.
No reasoning capability may inherit these truth authorities.

### Candidate moves

1. `USE_EXISTING`
   Keep v0 unchanged and borrow requirements/quality-attribute reasoning from Scaffold when needed.

2. `ADAPT`
   Add a narrow front-door step to v0:
   `NEED → ARCHITECTURE-RELEVANT REQUIREMENTS / QUALITY ATTRIBUTES → MATERIAL PRESSURE`.

3. `BUILD_SUBCAPABILITY`
   Create a separate requirements/quality-attribute elicitation capability only if repeated cases show that translation itself requires recurring state/contract distinct from architecture decisions.

4. `BUILD_PEER`
   Create a Solution Architect Agent. Current evidence does not justify this.

### Cheapest decision-changing learning
Recover historical cases where the initial input was a vague need/goal rather than an already-formed architecture pressure. Compare:

- baseline: current Architecture Decision Discriminator v0;
- challenger: v0 preceded by an explicit `NEED → REQUIRED QUALITIES / CONSTRAINTS / measurable acceptance criteria` translation.

Measure only whether this changes:
- selected structural option;
- anti-build/defer decision;
- evidence requested;
- authority handoff;
- tradeoff surfaced;
- migration/reversal condition.

## Decision after

### 1. `Solution Architecture` is **not currently a separate peer**
No new agent is earned by this pass.

### 2. It is a **better professional framing of the telos of the existing Architecture candidate**
The Architecture Decision Discriminator is already substantially about fitting structure to purpose, constraints and tradeoffs rather than about system-design pattern recall.

### 3. The strongest surviving gap is narrower
A possible missing transformation at the front door:

```text
ACCEPTED NEED
+ OWNER/FIELD constraints
→ ARCHITECTURE-RELEVANT REQUIREMENTS
→ REQUIRED QUALITY ATTRIBUTES / measurable acceptance criteria where material
→ MATERIAL PRESSURE
→ existing Architecture Decision Discriminator
```

This should be tested as an adaptation before any new capability or agent is built.

## Boundary map after the reframe

### Neta
`raw/product signal → defensible interpretation/design distinction`

### R&D
`telos + current state + resources → what deserves investment/evidence now`

### Solution Architecture / Architecture Decision capability
`accepted need + constraints + required qualities → system structure + tradeoffs + migration/reversal`

### System Design knowledge
A borrowed/internalized mechanism library used **inside** Solution Architecture when a live option requires domain depth.

## Naming recommendation

For the human profession/domain, `Solution Architecture` is a good umbrella term.

For the internal capability, do not rename canonically yet. The most precise candidate names are:
- `Solution Architecture Decision Capability`
- `Architecture Fitness Discriminator`
- retain `Architecture Decision Discriminator` and broaden its telos explicitly.

Do not promote a naming change until the front-door challenger shows decision delta.

## Falsifier

If historical vague-need cases show that current v0 + Neta/R&D already reaches the same bounded architecture decisions with no extra evidence/authority benefit, do not add a requirements front door. Treat Solution Architecture as a professional label for the existing combined workflow.

## Next authorized move

Build 6–10 blinded historical fixtures with two classes:

### Positive-control candidates
Cases where translating the need into explicit quality attributes/acceptance criteria should materially change the architecture decision or evidence requested.

### Neighboring non-fire candidates
Cases dominated by state authority, invariant, dependency or temporal-coupling problems where requirements translation should add no material delta.

Do not deepen System Design content before this discriminator test.
