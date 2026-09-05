# CLAUDE.md — working rules for the peer-agent architecture

Read in this order before changing behavior, assurance architecture or research-agent behavior:

1. `docs/SHARED_EPISTEMIC_KERNEL.md`
2. `docs/AGENT_AUTHORITY_BOUNDARIES.md`
3. `docs/AUTHORITY_MAP.md`
4. `docs/PEER_HANDOFF_PROTOCOL.md`
5. `docs/CANONICAL_STATE.md`
6. `docs/V0_1_FREEZE.md`
7. `docs/NETA_ASSURANCE_THESIS.md`
8. `docs/REALITY_AUTHORITY_PERMISSION.md`
9. `docs/TELOS.md`
10. `docs/METHOD.md`
11. `research/RND_AGENT_CHARTER_V0_1.md`
12. `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`
13. `docs/FAILURE_LINEAGE.md`
14. `docs/LESSONS_COVERAGE_AUDIT.md`
15. `research/WAVE1_PREREGISTRATION.md`
16. `research/AMENDMENTS.md`
17. `research/PROMOTION_PROTOCOL.md`
18. `research/WAVE1_ASSURANCE_REVIEW.md`
19. `prompts/SYSTEM.md` — frozen Neta v0.1 clean-model baseline
20. `eval/RUBRIC.md`

## Architecture first

Neta and the R&D Agent are **peers**.

Neither agent owns the other.

`docs/SHARED_EPISTEMIC_KERNEL.md` is a constitution, not an agent or orchestrator.

The future orchestrator may route, maintain dependencies and synthesize peer outputs, but it may not become a resolution authority merely because it sees all agents.

Do not create an implicit hierarchy from call order. A peer invoking another peer is a handoff, not subordination.

## Gate 0 — before proposing work

Name:

1. the material question;
2. the exact claim whose state matters;
3. the decision that could change;
4. the minimum reality needed by that claim;
5. the resolution authority;
6. the peer/domain that should work the question;
7. the requested use;
8. whether current evidence permits `ALLOW`, `DENY` or `DEFER`;
9. what evidence could reverse the decision.

Allowed resolution authorities:

- `OWNER`
- `REPO`
- `ENVIRONMENT`
- `RESEARCH`
- `FIELD`

If remaining material uncertainty belongs to another authority or peer, route or stop.

## Shared unit of progress

The unit of progress is **material uncertainty removed**.

Do not add a dashboard, chat shell, database, vector store, telemetry, model router, agent swarm, instrument registry or extra research source because it is technically possible or intellectually interesting.

## Neta boundary

Neta owns product/design sensemaking:

```text
SIGNAL
→ MOMENT
→ OBSERVABLE
→ COMPETING PRODUCT/DESIGN MECHANISMS
→ CHEAP DISCRIMINATOR
→ DESIGN DISTINCTION
→ BOUNDED INTERVENTION / FIELD REQUIREMENT
```

The Neta v0.1 prompt remains frozen under `docs/V0_1_FREEZE.md`.

A Neta capability change must satisfy `eval/CAPABILITY_UPDATE_GATE_V1.md`.

R&D evidence cannot directly promote a Neta prompt rule.

## R&D Agent boundary

R&D owns research/evidence sensemaking:

```text
DIAGNOSE
→ RECOVER
→ DISCRIMINATE
→ EXECUTE
→ CLOSE
→ HANDOFF / STOP
```

Before proposing a new research instrument, perform a bounded existence search when cheaper than equivalent reconstruction.

Do not equate:

- instrument existence with runnability;
- run with durable evidence;
- historical evidence with current validity;
- null with refutation;
- pending authority with debt;
- multiple shared-lineage instruments with independent triangulation.

R&D capability changes must satisfy `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`, not Neta's capability gate.

## Shared claim contract

Cross-agent claims use the constitutional semantics in:

- `docs/SHARED_EPISTEMIC_KERNEL.md`
- `schemas/epistemic-claim.schema.json`

Existing `schemas/finding.schema.json` remains Neta's v0.2 adapter.

`schemas/rnd-research-task.schema.json` is the R&D runtime adapter.

Do not weaken shared authority/reality/permission semantics silently inside a peer schema.

## Neta finding contract

A Neta v0.2 finding is a ledger, not one verdict.

It may contain strong local observations, a supported mechanism, an owner-authorized reversible intervention and an unresolved field outcome simultaneously.

Contract rules remain:

- preserve raw owner wording before interpretation;
- at most three competing product/design mechanisms surfaced at once;
- no numeric confidence theater;
- each material claim has evidence refs, required reality, observed reality, resolution authority, requested use and permission;
- `SUPPORTED` requires observed reality at or above the claim floor;
- external-human `OUTCOME` claims resolve to `FIELD` and ordinarily require `R6`;
- `ASSERT_FIELD_OUTCOME` cannot be allowed below R6;
- `BUILD_READY` requires allowed intervention + falsifier + positive control + reversal;
- `FIELD_STOP` requires unresolved material FIELD claim + concrete field requirement;
- waiver can accept risk but cannot upgrade evidence/reality/authority;
- intervention and measurement may not change silently together.

Run before declaring a Neta contract change done:

```bash
python scripts/check_contract.py
python scripts/check_research_contract.py
```

## R&D continuity contract

A research task is not closed because code ran.

It must preserve or explicitly stop across:

```text
live claim
→ bounded recovery
→ REUSE / ADAPT / BUILD / NO_INSTRUMENT / WAIT_AUTHORITY
→ instrument version/input fit
→ decision contract
→ run
→ durable deposit
→ claim disposition
→ later revalidation
```

R&D may end in `WAITING_AUTHORITY`, `FAILED_EXECUTION`, `INCONCLUSIVE`, `REFUTED`, `SUPPORTED` or a justified stop. Preserve these distinctions.

## Peer handoffs

Use `docs/PEER_HANDOFF_PROTOCOL.md` and `schemas/peer-handoff.schema.json`.

A handoff must name the live claim, current evidence, why the peer is needed, requested return, forbidden inference and stop condition.

Peer disagreement is not resolved by seniority or majority vote.

## Research quarantine

Wave 1 remains frozen historical Neta research. Do not rewrite its thresholds/statuses to fit the new peer architecture.

The new R&D Agent does not inherit Wave 1 promotion states as its lifecycle.

The cross-repository instrument extraction/triangulation/synthesis remains provenance for the R&D charter, not a retroactive rewrite of Wave 1.

## Encodability-bias gate

Before building any new capability/probe/system, answer:

- Which live claim does it resolve?
- Which authority owns that claim?
- Which peer should work it?
- What information does it buy?
- Is there a cheaper admissible observation or existing capability?
- What measurement/behavior could it contaminate?
- What would cause removal or reversal?

“We can build it” is never sufficient permission.

## Failure repair

Repair at the lowest layer capable of preventing recurrence without distorting neighbors:

- shared kernel only for genuinely cross-agent constitutional defects;
- peer schema/validator for structural peer-specific impossibilities;
- fixture for a judgment distinction;
- R&D research for externally unresolved mechanism/measurement questions;
- Neta prompt only when clean-model Neta failure earns it;
- FIELD when FIELD is the authority.

Retain lineage. Do not rewrite failed history away.

## Memory rule

`memory/owner-language.yaml` remains a Neta prior, not truth and not shared-agent ground truth.

R&D null/refutation/run memory must preserve provenance and disposition rather than becoming a phrase→claim dictionary.

## Stop rule

When the remaining uncertainty belongs to another peer or authority, route or stop.

When research cannot change a research-owned decision, stop reading/running.

When a product intervention has no live decision it can change, do not build it.

When an orchestrator would only reproduce routing already expressible through peer handoffs, do not build the orchestrator yet.
