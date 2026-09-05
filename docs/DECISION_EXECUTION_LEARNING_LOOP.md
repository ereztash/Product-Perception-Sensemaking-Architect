# Decision → Execution → Verified State → Outcome → Learning

Status: `CROSS_AGENT_EXECUTION_CONTRACT_V0_1`

Purpose: close the gap between a bounded decision and evidence from reality without inventing an Execution Agent.

## Core invariant

```text
DECISION
→ EXECUTION
→ VERIFIED STATE
→ OUTCOME
→ LEARNING
```

These are five different objects.

Never collapse:

- decision made ≠ action executed;
- action executed ≠ intended state exists;
- intended state exists ≠ desired outcome occurred;
- outcome observed ≠ causal mechanism established;
- artifact created ≠ learning earned.

## Ownership

- `DECISION` — may belong to OWNER, Neta, R&D or deterministic runtime within its explicit authority.
- `EXECUTION` — human/tool/agent/runtime action. Execution is not truth authority merely because it changed something.
- `VERIFIED STATE` — resolved by the authority that can inspect the changed state: usually REPO or ENVIRONMENT; sometimes OWNER/FIELD.
- `OUTCOME` — resolved by the authority appropriate to the target claim. Human notice/comprehension/value/behavior remains FIELD.
- `LEARNING` — R&D may update resource allocation/claim state after the relevant evidence exists; peer-specific capability promotion still uses that peer's gate.

## Why this is not an agent

The missing capability is initially a trace/contract problem: decisions can hand off to existing executors and authorities. A new peer is justified only if repeated real traces show a recurring reasoning problem between decision and verified state that protocols/tools cannot handle cheaply.

## Machine-readable contract

- `schemas/decision-execution-learning.schema.json`
- `scripts/validate_decision_trace.py`
- `fixtures/decision-execution-learning-valid.json`

## Promotion discriminator for a future execution capability

Collect 10-15 real traces. Promote a distinct execution capability only if a recurring gap survives after explicit planning, artifact references and REPO/ENVIRONMENT verification are present, and that gap materially harms decision quality, cost, reversibility or learning.

Do not promote from missing telemetry, missing tool wiring, or one failed implementation.
