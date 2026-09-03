# CLAUDE.md — working rules for Neta v0.2 re-foundation

Read in this order before changing behavior or assurance architecture:

1. `docs/AUTHORITY_MAP.md`
2. `docs/V0_1_FREEZE.md`
3. `docs/NETA_ASSURANCE_THESIS.md`
4. `docs/REALITY_AUTHORITY_PERMISSION.md`
5. `docs/TELOS.md`
6. `docs/METHOD.md`
7. `docs/FAILURE_LINEAGE.md`
8. `docs/LESSONS_COVERAGE_AUDIT.md`
9. `research/WAVE1_PREREGISTRATION.md`
10. `research/AMENDMENTS.md`
11. `research/PROMOTION_PROTOCOL.md`
12. `research/WAVE1_ASSURANCE_REVIEW.md`
13. `prompts/SYSTEM.md` — frozen v0.1 clean-model baseline
14. `eval/RUBRIC.md`

## Gate 0 — before proposing work

Name:

1. the material question;
2. the exact claim whose state matters;
3. the minimum reality needed by that claim;
4. the resolution authority;
5. the requested use;
6. whether current evidence permits `ALLOW`, `DENY` or `DEFER`;
7. what evidence could reverse the decision.

Allowed resolution authorities:

- `OWNER`
- `REPO`
- `ENVIRONMENT`
- `RESEARCH`
- `FIELD`

If all remaining material uncertainty belongs to another authority, the current authority has reached its ceiling. Route or stop.

## Current product decision

**METHOD FIRST · ASSURANCE FIRST · NO UI · NO SOURCE 29 · FROZEN PROMPT BASELINE.**

Do not add a dashboard, chat shell, database, vector store, telemetry, model router, agent swarm or extra research source because it is technically possible or intellectually interesting.

The unit of progress is material uncertainty removed.

## v0.1 prompt freeze

`prompts/SYSTEM.md` is the clean-model baseline frozen by `docs/V0_1_FREEZE.md`.

Do not edit it during the architectural re-foundation.

A future prompt change must answer:

1. Which clean-model fixture failed?
2. What hidden judgment was missing?
3. What is the smallest rule that teaches it?
4. Which neighboring behavior could the rule damage?
5. Which control protects that neighbor?
6. If research-derived, which `PROMPT_ELIGIBLE` claim allows proposing the rule?

## Finding contract

A v0.2 finding is a ledger, not one verdict.

It may contain strong local observations, a supported mechanism, an owner-authorized reversible intervention and an unresolved field outcome simultaneously.

Contract rules:

- preserve raw owner wording before interpretation;
- at most three competing mechanisms are surfaced at once;
- no numeric confidence theater;
- each material claim has a type, evidence refs, required reality, observed reality, resolution authority, requested use and permission;
- `SUPPORTED` requires observed reality at or above the claim's floor;
- external-human `OUTCOME` claims resolve to `FIELD` and ordinarily require `R6`;
- `ASSERT_FIELD_OUTCOME` cannot be allowed below R6;
- `BUILD_READY` requires an allowed intervention plus falsifier, positive control and reversal;
- `FIELD_STOP` requires an unresolved material FIELD claim and a concrete field requirement;
- a waiver can accept risk but cannot upgrade evidence/reality/authority;
- intervention and measurement may not change silently together.

Run before declaring a contract change done:

```bash
python scripts/check_contract.py
python scripts/check_research_contract.py
```

## Research quarantine

Wave 1 is frozen historical research. Source collection has already begun and Evidence Pass 1 is merged.

Do not rewrite its thresholds/statuses to fit v0.2.

The v0.2 assurance overlay is prospective. Use `research/WAVE1_ASSURANCE_REVIEW.md` to determine what existing candidates may inform next.

Research still follows:

```text
source
→ research register
→ triangulation
→ counterevidence
→ culture/context boundary
→ contradiction disposition
→ discriminator/fixture
→ candidate capability
→ prompt eligibility
```

G/C/A/O are evidence coordinates, not a permission score. Do not average them.

Stop research when the unresolved material question belongs to another authority or when recursion no longer buys a new distinction/boundary/reversal.

## Encodability-bias gate

Before building a new capability/probe, answer:

- Which live claim does it resolve?
- Which authority owns that claim?
- What information does it buy?
- Is there a cheaper admissible observation?
- What measurement/behavior could it contaminate?
- What would cause removal or reversal?

“We can build it” is never sufficient permission.

## Failure lineage

When a case exposes a Neta failure, record it in `docs/FAILURE_LINEAGE.md` before hiding the failure with a broad rule.

Repair at the lowest layer capable of preventing recurrence:

- schema/validator if it is a structural impossibility;
- fixture if it is a judgment distinction;
- research if the mechanism is externally unresolved;
- prompt only when clean-model failure proves hidden judgment is missing;
- field when field is the authority.

## Memory rule

`memory/owner-language.yaml` remains a prior, not truth.

A repeated metaphor may raise inspection priority. It never becomes a permanent phrase→diagnosis dictionary without discrimination.

## Stop rule

When remaining material uncertainty is taste, external comprehension, preference, value or behavior, and FIELD is the authority, stop internal reasoning/build.

When research cannot change a research-owned decision, stop reading.

When a feature has no live decision it can change, do not build it.
