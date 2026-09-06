# Agent Discovery — Pass 1 Synthesis

Status: `ROLE_CONDITIONED_RND+NETA_SYNTHESIS · REPO_GROUNDED · EXTERNAL_COMPLETENESS_CHECK · NOT_RUNTIME_EXECUTION · NO_AGENT_PROMOTION`
Date: 2026-09-06

## Decision before

The ecosystem has two central peers:
- Neta;
- R&D.

The open question was whether the system's function space is sufficiently covered, and which recurring residual judgment functions — if any — justify adding peers.

## Method

Pass 1 did not search for agent names.

It:
1. froze an Agent Discovery admission/promotion rule;
2. mapped the decision lifecycle against existing peers, authorities, domain methods, runtime/protocol and execution;
3. used Decision Quality, NASA Systems Engineering / Decision Analysis and SEBoK only as completeness references;
4. inspected architecture research, execution-learning contracts, handoff/routing contracts, Neta failure lineage, R&D scope failures and natural historical user cases;
5. treated `NO_NEW_AGENT` as a valid result.

## Neta framing challenge

The largest framing error to avoid is:

```text
IMPORTANT FUNCTION
→ BLANK BOX
→ AGENT
```

The correct object is:

```text
RECURRING MATERIAL FAILURE
→ MISSING JUDGMENT
→ CURRENT OWNER EXCLUSION
→ MINIMAL CAPABILITY
→ COMPARATIVE DELTA
→ FORM FACTOR
```

Neta also separates five entities that previous agent brainstorming can collapse:

1. `PEER METHOD`
2. `AUTHORITY`
3. `DOMAIN METHOD`
4. `COORDINATION / PROTOCOL`
5. `EXECUTION / TOOL`

Only the first class is necessarily an agent-like candidate.

## R&D synthesis

The question is no longer “what expertise could be useful?”

The decision-controlling uncertainty is:

> Which residual judgments are worth **internalizing** rather than continuing to borrow/route/execute through cheaper resources?

That makes the next research program a build-vs-borrow test for judgment functions.

---

# Strongest structural insight

The ecosystem likely contains **two different peer families**.

## A. Cross-cutting decision methods

These operate across domains.

Current example:
- `R&D` — epistemic effort / evidence-program allocation.

Open challenger:
- `Decision Support / Tradeoff Structuring` — compare already-admissible alternatives against explicit owner priorities and test ranking robustness.

## B. Domain judgment methods

These own a recurring domain object.

Current example:
- `Neta` — product perception/design sensemaking.

Open challenger:
- `Architecture / Solution Architecture` — need/requirements → structural options/tradeoffs/migration.

Other specialties such as debugging, security, legal and finance remain **borrowed domain methods by default**, not peers.

This two-family model is more coherent than forcing peers into one flat MECE taxonomy.

---

# Candidate dispositions

| Candidate | Evidence of distinct judgment | Evidence of recurring need | Comparative delta | Current form | Disposition |
|---|---|---|---|---|---|
| Neta | strong | strong OSS corpus | supported in bounded cases | peer | `KEEP` |
| R&D epistemic allocation | strong structural/external convergence | strong historical/discovery signal | scope confirmation incomplete | peer/candidate telos | `KEEP_AND_CONFIRM` |
| Architecture Decision Discriminator | explicit orthogonal structural judgment | 12 historical cases + repeated architecture work | **not yet validly measured** | candidate capability | `TEST, DO_NOT_PROMOTE` |
| Need→Architecture Requirement Translation | explicit front-door gap in architecture research + external SE separation | repeated architecture cases begin downstream, so recurrence plausible but not directly scored | unmeasured | candidate subcapability | `TEST_AS_ARCHITECTURE_ADAPTATION` |
| General Decision Support / Tradeoff Structuring | externally well-defined orthogonal method; one plausible natural positive case | insufficient internal corpus after owner priorities are known | unmeasured | observatory | `COLLECT_CASES, NO_AGENT` |
| Orchestrator | conceptual function exists | no recurring coordination failure family found | none | deterministic routing + handoff protocol | `NOT_EARNED` |
| Execution Agent | execution gap exists as lifecycle stage | no recurring reasoning gap after explicit planning/verification shown | none | tools + trace contract | `NOT_EARNED` |
| Verification/Validation Agent | important function | authority already explicit | category error as truth owner | authority/tooling | `REJECT_AS_AGENT` |
| Debugging Agent | deep recurring work in software | ordinary domain diagnostic method | external R&D scope test showed false-fire risk | borrow/domain method | `DO_NOT_GENERALIZE` |
| Epistemology / VOI Agent | strong theoretical fit | behavior largely already in R&D | no unique next-move delta in controlled tests | R&D internal theory/eval | `ABSORB_IN_RND` |
| Question Discovery Agent | front-door behavior is useful | overlaps R&D/routing/Neta | no separate epistemic capability shown | gate/workflow | `DO_NOT_SPLIT` |
| Strategy Agent | strategy is consequential | telos/values/accepted tradeoffs are OWNER-owned | no orthogonal judgment isolated | OWNER + decision support/domain methods | `NOT_EARNED` |
| Risk Agent | risk is ubiquitous | cross-cutting but embedded in thresholds/tradeoffs/domain analysis | no independent residual | modifier | `NOT_EARNED` |
| Memory Agent | continuity essential | repo already needs lineage | state/trace problem, not hidden judgment | shared infrastructure | `NOT_AGENT` |

---

# Candidate 1 — Architecture

## What is already earned

A distinct judgment exists:

```text
REQUIREMENTS / CONSTRAINTS / INVARIANTS
+ CURRENT STRUCTURE
→ STRUCTURAL OPTIONS
→ DEPENDENCY / FAILURE / CHANGE TRADEOFFS
→ ARCHITECTURE DECISION
→ MIGRATION / REVERSAL
```

This is not Neta and not R&D.

## What is not earned

A persistent `Architecture Agent`.

The repo's own execution trace records that the 12-case corpus exists but a valid clean baseline-vs-candidate result has not yet been measured.

Therefore:

`ARCHITECTURE_CAPABILITY = PLAUSIBLE`

`ARCHITECTURE_PEER = NOT_EARNED`

## Front-door residual

The stronger gap is upstream:

```text
ACCEPTED NEED
→ ARCHITECTURE-SIGNIFICANT REQUIREMENT / QUALITY ATTRIBUTE
→ ACCEPTANCE MEASURE
→ MATERIAL PRESSURE
→ ARCHITECTURE DECISION
```

This should first be tested as an adaptation of the Architecture capability, not a separate Requirements Agent.

---

# Candidate 2 — Decision Support / Tradeoff Structuring

## Why it is plausible

External decision-analysis frameworks distinguish:
- decision criteria/priorities;
- alternatives;
- consequences/tradeoffs;
- uncertainty sensitivity;
- recommendation;
- final decision authority.

This is adjacent to but not identical with R&D.

Possible clean boundary:

```text
CURRENT KNOWLEDGE + OWNER PRIORITIES + ALTERNATIVES
→ DECISION SUPPORT compares/ranks

if unresolved uncertainty can flip ranking
→ R&D decides whether learning is worth buying

if values are missing
→ OWNER

if domain judgment is missing
→ DOMAIN METHOD

if robust enough
→ OWNER commits
```

## Internal evidence

Negative controls dominate current OWNER_DEFER cases: Actual Budget, SparkleShare, Organic Maps and SiYuan stop because owner policy itself is missing. Formal decision analysis would be premature there.

One natural Lichess case is a plausible positive signal: two already-built/measured reveal-routing alternatives were compared on user friction, funnel denominator, experimental integrity and protocol comparability, with recommendation but OWNER decision retained.

One case is not recurrence.

Therefore:

`DECISION_SUPPORT_CAPABILITY = OPEN_CHALLENGER`

`DECISION_SUPPORT_AGENT = NOT_EARNED`

The new `DECISION_SUPPORT_OBSERVATORY_V0.md` exists specifically to falsify or establish this residual.

---

# Candidates rejected by form-factor logic

## Coordination

The handoff protocol and deterministic calibration loop already preserve:
- source peer;
- target peer;
- claim;
- evidence;
- authority;
- requested return;
- dependency/stop.

Do not build an orchestrator until real traces show recurring material failures that cannot be cheaply prevented by this explicit state machine.

## Execution

The repo has already made the correct distinction:

```text
DECISION != EXECUTION != VERIFIED STATE != OUTCOME != LEARNING
```

Missing execution capability is not missing reasoning authority. Collect the required real traces before revisiting.

## Verification/Validation

These are essential functions but are resolved by authorities. An agent can design tests or inspect evidence; it cannot turn itself into REPO/ENVIRONMENT/FIELD truth.

---

# Revised ecosystem hypothesis

The most coherent current architecture is not a board of many specialist agents.

It is:

```text
OWNER
values / goals / accepted risk / commitment authority

        ↓

CROSS-CUTTING METHODS
- R&D: epistemic allocation
- [Decision Support?]: alternative/tradeoff structuring — UNPROVEN

        ↕

DOMAIN METHODS
- Neta: product perception/design
- [Architecture?]: structural/system design — CANDIDATE
- debugging/security/legal/finance/etc.: borrowed until recurrence earns internalization

        ↕

DETERMINISTIC COORDINATION
Calibration Loop + handoff protocol

        ↕

AUTHORITIES
REPO / ENVIRONMENT / RESEARCH / FIELD

        ↓

EXECUTION / VERIFIED STATE / OUTCOME
human + tools + runtime + trace contracts

        ↓

LEARNING / LINEAGE
R&D + peer-specific gates + shared epistemic kernel
```

This is a stronger architecture than a flat agent list because it separates judgment, authority, coordination and execution.

---

# Next research allocation

## Priority 1 — Decision Support Observatory

Reason: this is the only currently plausible **cross-cutting third judgment function**. If it survives, it changes the ecosystem architecture materially. If it fails, the cross-cutting layer may remain R&D + OWNER/general reasoning.

Collect 15–25 natural cases that begin after OWNER criteria are explicit.

Primary falsifier:

> Neta + R&D + domain method + OWNER constraints already produce the same material decision path as the minimal Decision Support contract.

If true, retire the candidate.

## Priority 2 — Architecture front-door fixtures

Freeze 6–10 cases that begin with messy accepted needs rather than pre-formed architecture questions.

Compare:
- current Architecture Decision Discriminator;
- same capability preceded by explicit need→quality/requirement translation.

Promote only if downstream architecture decision/evidence/authority changes materially.

## Priority 3 — Clean Architecture candidate A/B

Run the existing 12 frozen architecture cases in a clean context that can see CASES but not GOLD.

Compare strongest current ecosystem baseline against candidate Architecture capability.

Until this occurs, architecture remains a candidate capability, not peer.

## Deferred research

Do not spend more effort on:
- generic orchestrator design;
- execution agent design;
- risk agent;
- epistemology agent;
- generic debugging agent;
- memory agent.

Reopen only after observed failure creates new decision-changing evidence.

---

# Pass-1 decision

`NEW_AGENT_PROMOTED: NONE`

`STRONGEST_DOMAIN_CAPABILITY_CANDIDATE: ARCHITECTURE`

`STRONGEST_CROSS_CUTTING_OPEN_CHALLENGER: DECISION_SUPPORT / TRADEOFF_STRUCTURING`

`STRONGEST_ARCHITECTURE_ADAPTATION_CANDIDATE: NEED_TO_REQUIREMENT_TRANSLATION`

`ORCHESTRATOR: NOT_EARNED`

`EXECUTION_AGENT: NOT_EARNED`

`BROAD_AGENT_DISCOVERY: STOP`

`TARGETED_FALSIFICATION: START`

## Reversal condition

This synthesis must change if targeted cases show:
- a new recurring judgment family not captured here;
- Decision Support materially beats the composed baseline;
- Architecture fails to beat Scaffold + existing peers;
- coordination/execution traces expose a recurring hidden judgment rather than a protocol/tool problem.
