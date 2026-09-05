# Architecture Decision Discriminator v0

Status: `CANDIDATE_CAPABILITY_NOT_AGENT`

Source decision: `CAL-ARCH-001-MANUAL-2026-09-05`

## Purpose

Test whether the peer-agent system is missing a distinct architecture-specific judgment capability before building an autonomous Architecture Agent.

This artifact is deliberately smaller than an agent.

## Telos

> Remove material uncertainty from a live architecture decision by making system boundaries, constraints, invariants, dependencies, failure/change costs and migration consequences explicit enough to discriminate among plausible structural alternatives.

The capability does **not** optimize for architecture novelty, pattern count, diagram completeness, abstraction purity or theoretical elegance.

## Unit of work

One live architecture decision.

Examples:

- Should canonical state move from file A to service B?
- Should two modules become one bounded component or remain separate?
- Is the current failure caused by coupling, authority duplication, runtime boundary, or merely implementation debt?
- Does a proposed agent deserve a separate peer boundary or is it a workflow/resource configuration?

## Required input

1. `TELOS` — what outcome the architecture should enable.
2. `CURRENT STATE` — what actually exists now.
3. `MATERIAL PRESSURE` — what decision/failure makes architecture relevant now.
4. `KNOWN CONSTRAINTS` — requirements/costs that may not be ignored.
5. `AVAILABLE AUTHORITIES` — which facts require OWNER / REPO / ENVIRONMENT / RESEARCH / FIELD.

If the telos is OWNER-owned and unresolved, stop rather than optimize an invented objective.

## Candidate architecture objects

These are candidate discriminators, not a mandatory checklist.

- `BOUNDARY` — what is inside/outside the unit.
- `CONSTRAINT` — what cannot/should not change.
- `INVARIANT` — what must remain true across variants/migrations.
- `DEPENDENCY_DIRECTION` — who may depend on whom and why.
- `STATE_AUTHORITY` — where canonical state lives; who may mutate it.
- `FAILURE_DOMAIN` — what can fail independently; blast radius.
- `CHANGE_PROPAGATION` — what downstream work/risk follows a local change.
- `TEMPORAL_COUPLING` — what must happen together/in order.
- `DEPLOYMENT_BOUNDARY` — what static repository evidence cannot establish.
- `MIGRATION_PATH` — how to move from current to candidate state.
- `REVERSIBILITY` — cost/possibility of undoing the decision.
- `TRADEOFF_LEDGER` — what is improved and what cost is accepted.
- `DECISION_LINEAGE` — why the decision exists and what would reverse it.

Do not assume every case needs every object.

## Operating loop

```text
LIVE ARCHITECTURE DECISION
→ CURRENT STRUCTURE / AUTHORITY MAP
→ 2–3 COMPETING ARCHITECTURAL MECHANISMS / OPTIONS
→ CONSTRAINTS + INVARIANTS
→ MATERIAL DEPENDENCIES / FAILURE OR CHANGE PATH
→ CHEAPEST DISCRIMINATING FACT
→ BOUNDED DECISION
→ MIGRATION / REVERSAL CONDITION
→ AUTHORITY STOP WHERE REQUIRED
```

## Required distinctions

Never collapse:

- pattern name ≠ architectural fitness;
- module count ≠ modularity;
- low coupling metric ≠ correct boundary;
- repository structure ≠ runtime behavior;
- clean interface ≠ correct state authority;
- service separation ≠ failure isolation;
- distributed ≠ scalable;
- centralized ≠ coupled;
- abstraction ≠ useful indirection;
- technical possibility ≠ justified migration;
- current pain ≠ architectural root cause;
- architecture recommendation ≠ OWNER tradeoff acceptance.

## Output v0

For a live case return:

1. `DECISION`
2. `TELOS`
3. `CURRENT STRUCTURE` — only observed/verified facts
4. `MATERIAL PRESSURE`
5. `CANDIDATE MECHANISMS / OPTIONS` — max 3
6. `CONSTRAINTS`
7. `INVARIANTS`
8. `DEPENDENCY / STATE AUTHORITY / FAILURE PATH` — only dimensions material to the case
9. `ONE CHEAP DISCRIMINATOR`
10. `AUTHORITY NEEDED`
11. `BOUNDED NEXT MOVE`
12. `MIGRATION / REVERSAL CONDITION`
13. `WHAT THIS DOES NOT ESTABLISH`

## Non-goals

This capability does not yet:

- autonomously refactor code;
- choose cloud/vendor/tooling;
- produce architecture diagrams for their own sake;
- enforce DDD, microservices, clean architecture or any named doctrine;
- score architectures with one composite number;
- replace REPO or ENVIRONMENT inspection;
- infer FIELD outcomes;
- own product/design decisions handled by Neta;
- own resource-allocation learning handled by R&D.

## Promotion question

The capability earns promotion toward an autonomous Architecture Agent only if repeated real cases show:

> Adding this architecture-specific decision contract changes material decisions more cheaply/reliably than using the existing combination of R&D + Scaffold + REPO/ENVIRONMENT evidence.

A prettier explanation, more terminology, more diagrams or agreement with the Scaffold do not count.

## First evidence program

1. Recover 8–15 historical architecture decisions from existing repos.
2. Freeze case inputs without exposing the desired answer.
3. Run a baseline using current resources without this contract.
4. Run the candidate discriminator.
5. Adjudicate only decision-relevant deltas.
6. Add targeted architecture research/OSS where a named distinction remains uncertain.
7. Create unseen HOLDOUT cases before prompt/agent implementation.

## Stop rule

If historical cases show no unique material decision delta, keep architecture expertise as a borrowed Scaffold/resource capability and do not build another peer.
