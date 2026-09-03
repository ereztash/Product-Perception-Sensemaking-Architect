# CLAUDE.md — working rules for Neta

Read in this order before changing behavior:

1. `docs/AUTHORITY_MAP.md`
2. `docs/TELOS.md`
3. `docs/METHOD.md`
4. `research/WAVE1_PREREGISTRATION.md`
5. `research/PROMOTION_PROTOCOL.md`
6. `prompts/SYSTEM.md`
7. `eval/RUBRIC.md`
8. `fixtures/v0.1.md`

## Gate 0

Before proposing work, name the question it resolves and its authority.

Allowed authorities:

- `OWNER`
- `REPO`
- `DESIGN_MECHANISM`
- `FIELD`

If the unresolved question is `FIELD`, do not write code to answer it.

## Current product decision

**METHOD FIRST. RESEARCH QUARANTINE ACTIVE. NO UI YET.**

Do not add a dashboard, chat shell, database, vector store, telemetry, model router or agent swarm unless a measured failure in the conversational method requires it.

## Contract rules

- Raw owner wording is preserved before interpretation.
- At most three competing mechanisms may be presented at once.
- No fake numeric confidence.
- `BUILD_READY` requires a reversal condition.
- `FIELD_STOP` must resolve to `FIELD`.
- Instrument friction is protected until explicitly redefined.
- A validator must be shown capable of failure by a positive control.

Run before declaring a change done:

```bash
python scripts/check_contract.py
python scripts/check_research_contract.py
```

## Research quarantine

External research does not directly edit `prompts/SYSTEM.md`.

The mandatory path is:

```text
source
→ research register
→ triangulation
→ counterevidence search
→ culture/context boundary
→ contradiction disposition
→ discriminator/fixture
→ candidate capability
→ prompt eligibility
```

Rules:

- Country is a sampling context, not a causal design mechanism by default.
- Three sources with one dataset are one evidence family.
- A contradiction may refute, narrow, split, contextualize, or expose a measurement conflict.
- If a concept splits, freeze the parent from promotion and evaluate the children.
- G/C/A/O are separate coordinates; never average them into one confidence score.
- Literature support alone cannot make a capability `PROMPT_ELIGIBLE`.
- Once Wave 1 source collection begins, do not alter preregistered thresholds without `research/AMENDMENTS.md`.
- Stop recursion after two consecutive passes produce no new distinction, reversal condition, or boundary condition, or when the unresolved authority is FIELD.

## Prompt changes

Every prompt change must answer:

1. Which fixture failed?
2. What hidden judgment was missing?
3. What is the smallest rule that teaches it?
4. Which neighboring behavior could this rule damage?
5. What positive/negative fixture protects against that damage?
6. If the rule came from research, what `PROMPT_ELIGIBLE` claim ID authorizes proposing it?

Do not tune the rubric or research promotion thresholds after seeing a run merely to rescue the prompt.

## Memory rule

`memory/owner-language.yaml` is a prior, not truth.

Never turn an owner phrase into a permanent one-to-one diagnosis. Promote a mapping only after an explicit discriminator favored one mechanism over a neighbor.

## Anti-build / anti-research stop

When the remaining uncertainty is taste, external comprehension, preference or behavior, stop and name the field observation required.

When recursive research stops producing distinctions or boundary conditions, stop reading merely to increase citation count.

More internal analysis at either boundary is field debt or research debt in disguise.
