# R&D Narrow Telos Scope Benchmark v0 — Adjudication

Status: `HISTORICAL_UNSEEN_SCOPE_SIGNAL · SAME_MODEL_MANUAL_ADJUDICATION · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06

Inputs:
- `RND_NARROW_TELOS_BENCHMARK_V0_FROZEN.md`
- `RND_NARROW_TELOS_BENCHMARK_V0_NARROW.md`
- `RND_NARROW_TELOS_BENCHMARK_V0_BROAD_REFERENCE.md`

## Case matrix

| Case | Narrow | Broad R&D material? | Adjudication |
|---|---|---:|---|
| NT-01 | NO_FIRE | NO | CORRECT_NO_FIRE |
| NT-02 | FIRE | YES | CORRECT_FIRE |
| NT-03 | FIRE | YES | CORRECT_FIRE |
| NT-04 | FIRE | YES | CORRECT_FIRE |
| NT-05 | NO_FIRE | NO | CORRECT_NO_FIRE |
| NT-06 | NO_FIRE | NO | CORRECT_NO_FIRE |
| NT-07 | FIRE | YES | CORRECT_FIRE |
| NT-08 | FIRE | YES | CORRECT_FIRE |
| NT-09 | NO_FIRE | NO | CORRECT_NO_FIRE |
| NT-10 | NO_FIRE | NO | CORRECT_NO_FIRE |
| NT-11 | NO_FIRE | YES | **FALSE_NO_FIRE** |
| NT-12 | NO_FIRE | NO | CORRECT_NO_FIRE |
| NT-13 | NO_FIRE | NO | CORRECT_NO_FIRE |

## Metrics

### MATERIAL_CASE_RECALL
Broad v0.2 found 6 material cases; narrow telos caught 5.

**5/6 = 83.3%**

### FALSE_NO_FIRE
Narrow telos emitted NO_FIRE on 8 cases; one was materially changed by broad R&D.

**1/8 = 12.5%**

### FALSE_FIRE
Narrow telos fired on 5 cases; broad R&D found material delta in all 5.

**0/5 = 0%**

### NON-MATERIAL SPECIFICITY
Broad R&D found 7 non-material cases; narrow telos bypassed all 7.

**7/7 = 100%**

### OVERALL_SCOPE_AGREEMENT

**12/13 = 92.3%**

## Verdict

The narrowed telos is **directionally much better bounded than v0.2**, but its current FIRE definition is too strict to promote.

Current disposition:

`NARROW_TELOS_V0: REJECT_AS_WRITTEN_BUT_REPAIRABLE`

Reason: missing 1/6 material cases is too costly for a scope boundary whose main purpose is to decide when R&D should not run.

## Failure mechanism — NT-11

The narrow rule treated each invocation of the Waze/Latent-Space prompt as cheap and reversible.

That is locally true but globally incomplete.

The prompt is a **reusable epistemic policy**. It repeatedly decides:
- which semantic anchors are privileged;
- which reasoning topology is allowed;
- what counts as the critical path;
- which answer regions are suppressed as generic;
- which persona shapes the search;
- what reasoning trace becomes part of the output.

Thus the commitment is not the cost of one run. It is the cumulative decision effect of adopting a method as a repeated control layer.

Failure pattern:

```text
CHEAP PER-USE ACTION
+ REUSABLE EPISTEMIC CONTROL POLICY
+ REPEATED DOWNSTREAM DECISION EFFECT
→ narrow rule mistakes local reversibility for low consequence
```

## Minimal repair hypothesis — not retroactively scored

Replace `consequential resource commitment` with a bounded two-family object:

> **consequential resource-or-method commitment**

A commitment is consequential when either:

### A. Material allocation
It consumes meaningful time, money, research/build effort, authority, lock-in or opportunity cost.

### B. Durable epistemic policy
It institutionalizes a reusable method/rubric/protocol that can repeatedly shape what evidence is collected, what alternatives are considered, how claims are scored, or which actions are selected.

The revised candidate telos becomes:

> **R&D exists to reduce decision-controlling uncertainty enough to justify or reject the next consequential resource or epistemic-method commitment, using the cheapest admissible learning move.**

Plain language:

> **R&D decides what is worth learning before we spend meaningful resources or turn a way of thinking into policy.**

## Neighbor protection

This repair must not make every reusable template fire.

Neighbor NT-10 (`WSN`) remains NO_FIRE because it is:
- lightweight;
- transparent;
- easily reversible;
- primarily an output/attention scaffold;
- not strongly committing evidence selection, causal claims, authority or hidden reasoning topology;
- ordinary use itself provides a cheap observation of utility.

A reusable method should fire only when its repeated use can **materially constrain the evidence/decision space**, not merely because it has a template.

## Next required test

Freeze a neighbor benchmark specifically around:

```text
REUSABLE BUT LOCAL/TRANSPARENT SCAFFOLD
vs
REUSABLE EPISTEMIC CONTROL POLICY
```

Include at least:
- WSN-like formatting/process scaffolds;
- reusable research/source hierarchies;
- scoring rubrics;
- forced causal decompositions;
- reasoning-topology prompts;
- owner-fixed reusable artifact templates;
- cheap reversible checklists.

Promote the repair only if it catches epistemic-control policies without reviving the previous `DOWNSTREAM_SCHEMA_USE` false-positive problem.