# Architecture Residual Decomposition — 2026-09-06

Status: `POST_A_B_DIAGNOSTIC_SYNTHESIS · MODEL_IDENTITY_CAVEAT · NO_AGENT_PROMOTION`

## Question

After broad agent discovery and the first staged Architecture A/B diagnostic, what exactly is still missing from the ecosystem?

The purpose of this pass is **not** to decide whether an `Architecture Agent` exists. It is to decompose the residual until the smallest missing judgment/contract is visible.

## Evidence used

1. `ARCHITECTURE_DECISION_DISCRIMINATOR_V0.md`.
2. `ARCHITECTURE_FRONT_DOOR_NATURAL_SCREEN_PASS1.md`.
3. `PASS3_SOLUTION_ARCHITECTURE_REFRAME.md` and `PASS4_INTERNAL_SATURATION.md`.
4. `DECISION_EXECUTION_LEARNING_LOOP.md` and `decision-execution-learning.schema.json`.
5. GitHub Actions Architecture A/B diagnostic run `ARCH-AB-20260906T102435Z`.

### Critical A/B evidence limit

The first complete A/B run preserved the intended `CASES → freeze → GOLD → blind judge` barrier, but used Copilot `model=auto`; therefore it is diagnostic evidence only and not the final same-model comparative result.

Diagnostic aggregate:

- candidate material wins: 1;
- baseline material wins: 1;
- candidate harm: 0;
- baseline harm: 0;
- candidate material win family: `STATE_AUTHORITY_LINEAGE` only.

Dimension-level diagnostic counts:

| Dimension | Architecture | Baseline | Tie/Neither |
|---|---:|---:|---:|
| Boundary | 2 | 3 | 7 |
| Authority | 2 | 3 | 7 |
| Option | 3 | 2 | 7 |
| Discriminator | 5 | 3 | 4 |
| Migration | 5 | 1 | 6 |
| Anti-build | 4 | 2 | 6 |

The pattern matters more than the raw score: Architecture did **not** dominate structural destination selection, authority, or boundaries. Its strongest repeated delta was around migration, bounded discrimination, staged change and anti-build.

---

# Decomposition by lifecycle position

## A. Before a structural decision — input qualification

Known transformation:

```text
RAW / ACCEPTED NEED
→ REQUIRED PROPERTIES / QUALITY ATTRIBUTES
→ CONSTRAINTS / INVARIANTS / CONTEXT
→ ARCHITECTURE-SIGNIFICANT PRESSURE
```

This transformation is real.

However, natural cases such as Vercel and Sheet-as-source-of-truth showed that existing upstream Question Discovery / R&D-style qualification can already produce the material reframe.

Therefore:

`UPSTREAM_REQUIREMENT_TRANSLATION = NECESSARY`

`UNIQUE_REQUIREMENTS_REASONING_CAPABILITY = NOT_SHOWN`

Best form:

`ARCHITECTURE_INPUT_GATE`

not a Requirements Agent.

---

## B. During the structural decision — choose architecture

Candidate transformation:

```text
REQUIREMENTS / CONSTRAINTS / INVARIANTS
+ CURRENT STRUCTURE
→ STRUCTURAL OPTIONS
→ BOUNDARY / AUTHORITY / DEPENDENCY / FAILURE TRADEOFFS
→ BOUNDED STRUCTURAL DECISION
```

The A/B diagnostic does **not** show that a dedicated Architecture method consistently improves this middle layer beyond the strongest composed baseline.

Evidence:
- material decision result was 1–1;
- Boundary and Authority dimensions actually favored baseline slightly;
- most cases reached the same structural next move.

Therefore:

`ARCHITECTURE_SELECTION_RESIDUAL = NOT_YET_DEMONSTRATED`

This is the key reason not to promote an Architecture peer.

---

## C. After the structural decision — make change safe

This is where the recurring residual appears.

Current cross-agent execution contract is:

```text
DECISION
→ EXECUTION
→ VERIFIED STATE
→ OUTCOME
→ LEARNING
```

The machine-readable `execution` object currently contains only:
- executor type;
- planned action;
- completed action;
- status;
- artifact refs.

There is no first-class object between `DECISION` and `EXECUTION` for a material structural transition.

### Missing transformation

```text
BOUNDED STRUCTURAL DECISION
+ CURRENT STATE
+ INVARIANTS
→ CHANGE SURFACE
→ STAGED TRANSITION
→ COMPATIBILITY / COEXISTENCE RULES
→ VERIFICATION CHECKPOINTS
→ ROLLBACK / REVERSAL TRIGGER
→ SAFE EXECUTION HANDOFF
```

This is the strongest current residual.

---

# Proposed minimal object — STRUCTURAL_CHANGE_ENVELOPE

Status: `CANDIDATE_CONTRACT_NOT_CAPABILITY_NOT_AGENT`

## Telos

Preserve the properties that made a structural decision valid while moving from current state to target state, with bounded blast radius, explicit verification and a usable reversal path.

## Unit of work

One material structural change after the destination decision is sufficiently bounded.

## Candidate fields

```text
STRUCTURAL_CHANGE_ENVELOPE

- decision_ref
- current_state_authority
- target_state
- change_surface[]
- preserved_invariants[]
- forbidden_changes[]
- dependency_order[]
- stages[]
- coexistence_or_compatibility_rule
- verification_checkpoints[]
    - stage
    - authority
    - expected_observation
    - fail_condition
- rollback_trigger
- rollback_action
- retirement_or_cutover_condition
- unresolved_uncertainties_that_block_stage[]
```

Not every field must be mandatory in every case. The invariant is that a material structural change may not collapse migration, verification and rollback into one prose `planned_action`.

## FIRE

Use the envelope when one or more are true:

- canonical state/authority moves;
- a component/boundary is added, removed or split;
- dependency direction changes;
- old and new structures may coexist temporarily;
- compatibility/backfill/migration is nontrivial;
- rollback is materially more expensive after a cutover point;
- the change can violate an invariant while still appearing locally successful;
- verification requires multiple authorities/stages.

## NO-FIRE

Do not invoke for:

- cheap local reversible edit;
- pure research/evidence acquisition;
- ordinary debugging with one direct fix path;
- decision where no structural state changes;
- implementation whose rollback/verification is already mechanically obvious and bounded.

---

# Why this is not R&D

R&D owns:

> Is more learning worth buying, and through which evidence program?

The change envelope assumes the structural decision is sufficiently bounded and asks:

> How can this decision be realized without losing the invariants that justified it?

If an envelope stage exposes uncertainty that can flip the plan, hand back to R&D.

---

# Why this is not Execution Agent

Execution performs the change.

The envelope is the contract that makes execution admissible.

It does not run commands, mutate repositories or establish that the target state exists.

REPO / ENVIRONMENT / FIELD still own verification.

Therefore the architecture is:

```text
DECISION
→ [STRUCTURAL_CHANGE_ENVELOPE when material]
→ EXECUTION
→ VERIFIED STATE
→ OUTCOME
→ LEARNING
```

not:

```text
DECISION
→ EXECUTION AGENT
```

---

# Why this may explain the A/B pattern

The diagnostic Architecture candidate repeatedly improved:

### Migration
It more often specified a bounded pilot, staged extraction, disposition list, or limited rollout rather than only naming the target structure.

### Discriminator
It more often attached a concrete check to a structural transition: compare before/after categories, verify incomplete cases, test same-run behavior, or gate expansion on observed compatibility.

### Anti-build
It more often constrained the first change to a smaller surface rather than generalizing immediately.

These are all properties of a **change envelope**.

By contrast, Boundary and Authority were not unique Architecture strengths; the Shared Epistemic Kernel + strong baseline already handle them well, and in at least one material case the baseline handled them better.

---

# Material cases from the diagnostic

## ARCH-HIST-012 — Architecture material win

Both responses selected the same core architecture:

> Outcome Summary as a projection over existing authoritative outputs, not a new source of truth.

The Architecture version won because it made the **transition/validation envelope** safer:
- explicit behavior for incomplete/conflicting outputs;
- source attribution preservation;
- measurable acceptance;
- bounded prototype before expansion;
- stronger anti-build guardrails.

This supports the transition hypothesis more than a general structural-selection hypothesis.

## ARCH-HIST-011 — Baseline material win

Both selected a derived debt register over authoritative sources.

Baseline won because it handled:
- non-authoritative status;
- claim-level verification/conflict;
- conditions under which not to build/derive status;
- source preservation.

This is evidence **against** claiming that Architecture uniquely owns authority/boundary reasoning.

---

# Revised architecture hypothesis

The evidence currently supports a three-part architecture shape:

```text
1. ARCHITECTURE_INPUT_GATE
   need → required properties / constraints / invariants
   form: gate/contract
   unique capability: not shown

2. STRUCTURAL DECISION
   options / boundaries / authority / dependency / failure tradeoffs
   form: borrowed Scaffold/domain method by default
   unique peer capability: not shown

3. STRUCTURAL_CHANGE_ENVELOPE
   decision → staged, verified, reversible structural transition
   form: missing contract candidate
   agent: not indicated
```

This is materially different from the previous assumption that the missing object was one broad `Architecture Agent`.

---

# Strongest current statement

> The ecosystem does not currently show a missing Architecture decision-maker. It shows a likely missing **structural transition contract** between a bounded decision and execution.

Plain version:

> We usually know what structure we want. What is less explicit is how to change the structure without breaking the things that made the decision correct.

---

# Cheapest decisive test

Do not build an Architecture Agent.

Freeze a `STRUCTURAL_CHANGE_ENVELOPE_V0` and compare on 8–12 natural structural-change traces:

```text
A = current decision → execution contract
B = same contract + STRUCTURAL_CHANGE_ENVELOPE_V0
```

Use cases involving:
- state/source-of-truth migration;
- provider/runtime boundary change;
- shared-infrastructure extraction;
- projection/read-model introduction;
- documentation/code boundary movement;
- persistence-model change.

Include NO-FIRE controls with local reversible edits and ordinary debugging.

## Material win metrics

Count only if the envelope prevents or materially reduces one of:

- invariant violation;
- authority duplication;
- compatibility break;
- unplanned coexistence ambiguity;
- unsafe cutover;
- missing verification authority;
- irreversible migration without rollback;
- unnecessary scope expansion;
- rework caused by an omitted transition dependency.

Better architecture prose does not count.

## Falsifier

If ordinary execution planning plus the existing decision/execution/verification trace produces the same safe migration path on these cases, do not create the object. Keep migration guidance as optional Scaffold reasoning.

---

# Current disposition

`ARCHITECTURE_AGENT = NOT_EARNED`

`ARCHITECTURE_SELECTION_CAPABILITY = UNIQUE_DELTA_NOT_SHOWN`

`ARCHITECTURE_INPUT_GATE = EARNED_AS_CONTRACT_SHAPE`

`STRUCTURAL_CHANGE_ENVELOPE = STRONGEST_NEW_RESIDUAL_CANDIDATE`

`STRUCTURAL_CHANGE_ENVELOPE_AGENT = CATEGORY_ERROR / NOT_PROPOSED`

`NEXT_HIGH_VALUE_TEST = CHANGE_ENVELOPE_BASELINE_VS_CHALLENGER`
