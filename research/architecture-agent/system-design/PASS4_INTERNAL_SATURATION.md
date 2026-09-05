# Pass 4 — Solution Architecture Internal Saturation

Status: `INTERNAL_SATURATION_REACHED_EXTERNAL_RESIDUALS_NAMED`
Date: 2026-09-06
Task: `CAL-ARCH-SOLARCH-001`

## Purpose

Exhaust decision-relevant information already present in the ecosystem repository and Erez's implementation history before buying external Solution Architecture knowledge.

This pass does **not** attempt to prove an industry definition of Solution Architecture from internal evidence. It asks a narrower calibration question:

> Which parts of the `need → architecture-relevant requirements → structure` transformation are already encoded in the current ecosystem, which parts are only implicit/fragmented, and which residual questions cannot be reduced further without external evidence?

The result is a boundary for external research, not a canonical capability change.

---

## Internal corpus recovered

### Canonical ecosystem contracts

- `docs/ECOSYSTEM_TELOS.md`
- `docs/METHOD.md`
- `docs/AGENT_AUTHORITY_BOUNDARIES.md`
- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `prompts/SYSTEM.md`
- `prompts/RND_AGENT_V0_2_CANDIDATE.md`
- `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`
- `research/architecture-agent/ARCHITECTURE_DECISION_DISCRIMINATOR_V0.md`
- `research/PROMOTION_PROTOCOL.md`

### Architecture evaluation corpus

- `eval/architecture-agent/HISTORICAL_BENCHMARK_PROTOCOL_V0.md`
- `eval/architecture-agent/HISTORICAL_CASES_V0.jsonl`
- `eval/architecture-agent/HISTORICAL_GOLD_V0.jsonl`

### Current research lane

- `CAL_ARCH_SOLARCH_001_TASK.json`
- `PASS2_HISTORICAL_RECOVERY.md`
- `PASS3_SOLUTION_ARCHITECTURE_REFRAME.md`
- `RND_NETA_RESEARCH_PLAN_V0.md`
- `SOURCE_REGISTER_PASS1.md`

### Portfolio implementation evidence sampled

Primary examples were recovered from `ereztash/lichess_app`, `ereztash/_crm`, `ereztash/pre-call`, and `ereztash/proofminer`, including cases where an owner/product need had to be translated before the eventual structure was obvious.

---

# 1. What the repository already knows

## 1.1 Telos precedes architecture

The ecosystem constitution already rejects architecture as an end in itself.

The global unit of progress is material uncertainty removed from a consequential decision, with the cheapest admissible evidence and explicit stopping/handoff. This blocks architecture novelty, pattern count and autonomous activity as default objectives.

Architecture therefore has to inherit an accepted purpose; it may not invent one.

**Existing object:** `TELOS`.

**Authority:** usually OWNER for strategic intent/tradeoff acceptance, with FIELD/RESEARCH/REPO/ENVIRONMENT resolving claims that the owner cannot establish by preference alone.

## 1.2 Raw needs are not yet professional requirements

Neta's method explicitly preserves the owner's raw signal and refuses the shortcut:

`owner metaphor → professional label → redesign`.

Its conversation loop is:

`SIGNAL → MOMENT → OBSERVABLE → HYPOTHESES → DISCRIMINATOR → DISTINCTION`.

This is already a powerful upstream mechanism for turning an ambiguous experience into a defensible distinction.

However, Neta stops at product/design sensemaking and bounded intervention. It does not define a general architecture-requirements object or translate every accepted need into technical quality attributes.

## 1.3 Claims, evidence, authority and permission are already first-class

The Shared Epistemic Kernel already provides most of the epistemic infrastructure a requirements layer would otherwise need to reinvent:

- exact claim;
- resolution authority;
- required/observed reality;
- evidence refs;
- requested use;
- permission;
- provenance;
- reversal condition.

Therefore a future architecture front door should **reuse these constitutional objects**, not create a parallel truth/confidence system.

## 1.4 R&D already owns the question “is architecture worth buying now?”

R&D v0.2 explicitly owns:

`TELOS → CURRENT STATE → RESOURCE MAP → BOTTLENECK/MISCALIBRATION → CANDIDATE MOVES → CHEAPEST DECISION-CHANGING LEARNING → OBSERVED DELTA → RECALIBRATE`.

This means Solution Architecture must not absorb prioritization/resource-allocation simply because architecture work can be expensive.

R&D may decide:
- use existing architecture capability;
- buy research;
- collect REPO/ENVIRONMENT evidence;
- adapt/build/retire;
- wait/stop.

Once the architecture problem is justified, internal structural fitness is a different transformation.

## 1.5 Architecture Decision Discriminator v0 already owns most of the downstream structural work

The current v0 input is:

1. `TELOS`
2. `CURRENT STATE`
3. `MATERIAL PRESSURE`
4. `KNOWN CONSTRAINTS`
5. `AVAILABLE AUTHORITIES`

It already compares:

- boundaries;
- constraints;
- invariants;
- dependency direction;
- state authority;
- failure domains;
- change propagation;
- temporal coupling;
- deployment boundaries;
- migration paths;
- reversibility;
- tradeoff ledger;
- decision lineage.

Its loop already goes from current structure to competing mechanisms/options, a discriminating fact, bounded decision and reversal/migration.

Therefore **System Design pattern knowledge is not the missing top-level function**.

---

# 2. The historical architecture benchmark has a front-door blind spot

The architecture benchmark is well designed for its original purpose: compare a baseline with Architecture Decision Discriminator v0 while hiding historical resolutions until outputs are frozen.

It includes 12 cases across 4 repositories and evaluates separate decision deltas rather than agreement with history.

But it is **not a valid test of the new need→requirements hypothesis**.

Why:

- every runner-visible row starts with a `decision_question` already expressed at architecture level;
- every row already includes `known_constraints`;
- every row already names `available_authorities`;
- many rows encode the essential architectural tension directly in the frozen input.

Examples:

- “provider/model-specific execution concerns relative to routing law” is already architecture language;
- “where should current repository truth be represented” already states canonical-authority tension;
- “what state should be persisted” already specifies two-sources-of-truth and think-time contamination constraints.

Thus the benchmark tests:

`STRUCTURED ARCHITECTURE PROBLEM → ARCHITECTURE JUDGMENT`

not:

`RAW/ACCEPTED NEED → ARCHITECTURE-RELEVANT REQUIREMENTS`.

### Consequence

A no-delta result on the existing 12 cases cannot refute the front-door capability; the front door has already been supplied by the case author.

A separate fixture family must begin earlier in the causal chain.

---

# 3. Portfolio evidence that translation changes decisions

Historical implementation evidence does not prove an optimal general method, but it does show repeated real cases where the eventual architecture decision depended on translating a vague/compound need into a sharper property.

## P1 — “The buttons sometimes don't feel responsive”

Initial signal:
- perceived non-responsiveness.

Discrimination split it into at least two materially different properties:
- physical/visual press acknowledgement must be immediate;
- long-running engine completion may legitimately take seconds but needs an explicit busy/wait state.

The measurement showed a synchronous chip and a multi-second commit both felt dead because neither acknowledged press state. The structural response was therefore not “make everything faster”; it introduced interaction-state acknowledgement while leaving computation latency unchanged.

**Translation lesson:** subjective “fast” can encode multiple response properties with different architecture/intervention consequences.

## P2 — “Database available”

Initial architectural assumption:
- configured DB implies server storage availability.

Required property after discrimination:
- a configured database must actually respond to a real operation within a bounded deadline before the system routes storage to it.

The resolution used an actual `select 1` with a deadline and separated “not configured” from “configured but unreachable”.

**Translation lesson:** an implementation proxy is not the required service property.

## P3 — Engine readiness timeout

Initial problem:
- engine readiness takes too long; 15-second bound appears to constrain engine startup.

Measured decomposition:
- local engine initialization was fast once bytes were present;
- the real limiting variable was downloading ~5.6 MB gzipped over low bandwidth.

The requirement became a relationship between payload size, bandwidth and acceptable readiness latency, not an arbitrary engine timeout.

**Translation lesson:** workload/resource conditions can change which subsystem the requirement constrains.

## P4 — Return to a chess position

Initial need:
- return to the position/session rather than the opening.

Architecture-relevant decomposition:
- preserve resumability;
- avoid a second canonical board representation;
- do not count time away from the product as decision think-time;
- reuse the existing move-history derivation path.

The chosen persistence object was move history, not board snapshot or in-progress measurement state.

**Translation lesson:** one user need can imply multiple quality/integrity requirements whose interaction determines the state boundary.

## P5 — PRE-CALL / POST-CALL data continuity

Initial problem:
- all user/business data lived only in localStorage and could vanish on cache clear/new device.

Architecture-relevant properties:
- recoverability/portability of data;
- privacy boundary around secrets/license keys;
- import/export integrity.

The system added explicit backup/restore while refusing to export credentials.

**Translation lesson:** “backup” is not one requirement; recoverability and confidentiality can pull the solution in opposite directions.

## P6 — CRM production readiness / pilot scale

Readiness work explicitly separated operational properties:
- security;
- observability;
- performance/scale;
- SLA/disaster recovery.

The same commit family deliberately refused WSGI/ASGI/reverse-proxy/vendor APM migration as premature for pilot scale while adding bounded-server, metrics, rate limiting, backup/restore and load-test mechanisms.

**Translation lesson:** a quality requirement needs a scale/context boundary; otherwise “production ready” invites unjustified infrastructure.

## P7 — Evidence store migration

The JSON store had allowed relational-integrity failures.

The requirement was not “use a database”; it was:
- make orphan/invalid states unrepresentable or fail loudly at write time;
- preserve reproducibility and local deployment constraints;
- avoid synced-filesystem/WAL corruption risk.

SQLite emerged as a mechanism after those requirements were explicit.

**Translation lesson:** mechanisms should follow integrity and deployment requirements, not reverse-engineer a need from a preferred tool.

---

# 4. Internal pattern extracted

Across the repository, the recurrent hidden transformation is:

```text
RAW / ACCEPTED NEED
→ split compound need into claims/properties
→ assign authority to each property
→ identify what must be true for the need to count as satisfied
→ identify context/workload under which the property matters
→ make a measurable/discriminable criterion where useful
→ expose conflicts among required properties
→ hand the resulting architecture pressure to structural option analysis
```

This is richer than `MATERIAL_PRESSURE` as one prose field but smaller than a new autonomous peer.

---

# 5. Provisional missing objects

These objects are **internal hypotheses**, not yet externally validated terminology.

## 5.1 NEED / STAKEHOLDER CLAIM

What outcome/problem is being accepted as relevant, in whose terms, and under what authority?

Why it may be needed:
- preserve lineage from raw need to technical requirement;
- avoid technical optimization against an invented owner objective.

Existing support:
- Neta raw signal;
- Kernel Claim + OWNER/FIELD authority.

Potentially no new object needed if represented as ordinary kernel claims with a relation.

## 5.2 ARCHITECTURE-RELEVANT REQUIREMENT

A bounded statement of what the system must do or preserve that can constrain structural options.

Current repository has `CONSTRAINT`, `INVARIANT`, `MATERIAL_PRESSURE`, but no explicit requirement object linking a need to those consequences.

## 5.3 REQUIRED QUALITY / RESPONSE PROPERTY

A property such as latency, availability, recoverability, consistency, integrity, confidentiality, maintainability, evolvability or operability that matters to the accepted need.

The repository already uses many such properties in implementation work, but there is no canonical architecture quality model.

## 5.4 ACCEPTANCE / DISCRIMINATION MEASURE

A criterion that says what observation would establish that the required property is currently satisfied or violated enough to matter.

Examples already present:
- real DB query under a 3s deadline;
- bundle ceiling;
- bandwidth/payload readiness arithmetic;
- restore drill;
- p50/p95/p99 load-test reporting.

Not every requirement must become a numeric SLO. The missing distinction is when measurement is decision-changing versus ceremonial.

## 5.5 CONTEXT / WORKLOAD CONDITION

The conditions under which the requirement is meaningful.

Examples:
- pilot-scale vs large-scale operation;
- slow network vs local asset;
- one session vs return after absence;
- signed-out local record vs server-backed identity.

Pass 2 already identified this as part of the narrow `MATERIAL_PRESSURE` residual.

## 5.6 REQUIREMENT CONFLICT / TRADEOFF ACCEPTANCE

The Architecture Discriminator has a `TRADEOFF_LEDGER`, but upstream conflict among needs/properties is not explicitly represented before options are generated.

Examples:
- recoverability vs secret non-export;
- consistency vs latency;
- instrumentation value vs measurement contamination;
- operational sophistication vs pilot-scale cost.

OWNER owns deliberate business/product tradeoff acceptance; research/engineering evidence may bound consequences.

## 5.7 TRACE LINK

Potential chain:

`NEED → REQUIREMENT/QUALITY → ARCHITECTURE DECISION → IMPLEMENTATION/MEASURE → OBSERVED RESULT`.

The repository has excellent provenance for claims and decisions, but not yet a canonical trace relation showing **which requirement an architecture decision exists to satisfy** and which observation would reverse it.

This is a strong candidate because it would connect existing objects rather than add a new ontology island.

---

# 6. What internal evidence cannot settle

At this point additional internal examples are likely to repeat the same shape. The remaining uncertainties concern the professional/domain method itself and require external RESEARCH evidence.

## RQ1 — Minimal architecture-significant requirement representation

What is the smallest useful representation of a requirement that reliably constrains architecture without importing a heavyweight requirements process?

Internal evidence cannot tell whether the provisional fields above correspond to established, empirically/practically useful constructs or merely our own coherent decomposition.

## RQ2 — Quality attribute elicitation and scenarios

How do mature architecture methods operationalize qualities such as performance, reliability, security, modifiability and usability into scenarios/response measures that actually discriminate structures?

We need to know whether a general scenario grammar exists and which parts are essential.

## RQ3 — Functional requirements vs quality attributes vs constraints

What distinctions materially improve architecture decisions, and which are merely documentation taxonomy?

The repository uses all three kinds informally but has not tested a clean decomposition.

## RQ4 — Stakeholder conflict and prioritization

The current ecosystem is strongly owner-centric. Organizational Solution Architecture often has multiple stakeholders with incompatible priorities, budgets, regulatory requirements and operational responsibilities.

We need external methods for preserving conflict without collapsing it into one score or letting an architect invent priority.

## RQ5 — Need→decision traceability

Which traceability practices meaningfully improve change/reversal/verification, and when do they become documentation burden?

The repository strongly values lineage, but has not externally tested the architecture-specific link from requirement to ADR/design to verification.

## RQ6 — Boundary of Requirements Engineering vs Solution Architecture vs Software/System Architecture

Industry titles are inconsistent. We need function-level boundaries, not job-title popularity:

- who elicits/accepts requirements;
- who translates qualities/constraints into architectural drivers;
- who chooses structural mechanisms;
- who owns business tradeoff acceptance;
- who verifies runtime satisfaction.

## RQ7 — What should remain borrowed domain knowledge

Caching, queues, replication, sharding, storage engines, cloud services and similar mechanisms may be architecture knowledge without deserving first-class constitutional objects.

External research should determine the stable **decision grammar**, not internalize every mechanism.

## RQ8 — Lightweight vs heavyweight method boundary

When does explicit quality/requirements work pay for itself, and when does it become architecture ceremony for a small reversible system?

This question is essential to R&D's anti-build/resource-calibration telos.

---

# 7. Internal saturation decision

## Decision before

Possible residual:

`ACCEPTED NEED → ARCHITECTURE-RELEVANT REQUIREMENTS / QUALITY ATTRIBUTES → MATERIAL PRESSURE → existing Architecture Decision Discriminator`.

## Decision after internal recovery

**The residual survives and is now better specified.**

The repository already supplies:
- raw-signal preservation and discrimination (Neta);
- claim/evidence/authority/permission/provenance infrastructure (Kernel);
- resource calibration/anti-build (R&D);
- structural option analysis/tradeoff/migration/reversal (Architecture v0).

What is not yet explicit is a domain method for translating an accepted need into architecture-significant requirements/properties with traceable acceptance conditions and conflict boundaries.

### Provisional minimal chain

```text
ACCEPTED NEED / CLAIM
→ ARCHITECTURE DRIVER(S)
    - required behavior/property
    - constraints/invariants
    - context/workload
    - acceptance/discriminator where material
    - stakeholder/authority
→ conflicts + accepted tradeoffs
→ MATERIAL PRESSURE
→ ARCHITECTURE DECISION DISCRIMINATOR v0
→ TRACE TO VERIFICATION / REVERSAL
```

`ARCHITECTURE DRIVER` is only a provisional umbrella label until external research is complete.

---

# 8. External research authorized by the repository

External work is now justified only for RQ1–RQ8 above.

## Source families, in priority order

1. **Normative/consensus standards**
   - architecture description;
   - requirements engineering;
   - quality models.

2. **Established architecture methods**
   - quality-attribute elicitation/evaluation;
   - architecture tradeoff analysis;
   - architecture decision methods.

3. **Open-source methods/templates/tools**
   - requirements/quality-scenario templates;
   - ADR/decision records;
   - architecture documentation systems;
   - reference implementations where process is executable/inspectable.

4. **Real architecture case studies/postmortems**
   - evidence of how requirements/constraints actually drove or reversed structural decisions;
   - migration and failure costs;
   - cases where overengineering was avoided.

5. **Practitioner videos/talks**
   - hypothesis generation and tacit judgment;
   - must be traced to stronger evidence before becoming a general rule.

6. **Multilingual source ecosystems**
   - add a language only when it exposes a distinct school/method/case family, not as a quota.

## Initial language hypotheses

- **English** — standards, SEI methods, vendor/cloud frameworks, large engineering case studies.
- **German** — arc42 / iSAQB and architecture communication/quality-scenario tradition; high expected unique yield.
- **French** — architecture/urbanisation SI and public/security architecture traditions; inspect for organizational/system-boundary distinctions.
- **Spanish** — Latin American/Spanish practitioner case studies and architecture communities; inspect for operational case diversity.
- **Russian** — strong practitioner/engineering long-form ecosystem (e.g. architecture/system-design case writing); discovery unless claims trace to primary evidence.
- other languages only if the first passes reveal a named residual.

---

# 9. External promotion / stop rules

For every external claim preserve:

- exact claim;
- source class;
- language;
- lineage/independence family;
- which RQ it serves;
- what internal object it challenges/adds;
- boundary/counterexample;
- allowed use;
- denied inference;
- whether it changes a discriminator/fixture/capability decision.

Stop a source/language lane after two consecutive passes add no new:

- architecture-driver field;
- decision distinction;
- counterindication;
- stakeholder/authority boundary;
- tradeoff mechanism;
- traceability relation;
- fixture design;
- anti-build condition.

Do not collect another framework merely because it is famous.

---

# 10. Next authorized sequence

1. Research standards/methods for RQ1–RQ6.
2. Crosswalk each external construct against existing Neta/R&D/Kernel/Architecture objects.
3. Search explicitly for counterevidence/criticism and lightweight alternatives.
4. Inspect open-source implementations/templates for how the method is operationalized.
5. Recover real-world cases where requirement translation changed or failed architecture.
6. Run multilingual lanes only where they promise distinct source families.
7. Build a candidate `Architecture Driver` contract only after source convergence.
8. Create new **pre-translation** fixtures from raw portfolio signals; do not reuse the already-structured historical architecture corpus as evidence for the front door.
9. Compare current combined workflow against the candidate front door.
10. Canonicalize only if material decision delta survives neighboring non-fire cases.
