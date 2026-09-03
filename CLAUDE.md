# CLAUDE.md — working rules for Neta

Read in this order before changing behavior:

1. `docs/AUTHORITY_MAP.md`
2. `docs/TELOS.md`
3. `docs/METHOD.md`
4. `prompts/SYSTEM.md`
5. `eval/RUBRIC.md`
6. `fixtures/v0.1.md`

## Gate 0

Before proposing work, name the question it resolves and its authority.

Allowed authorities:

- `OWNER`
- `REPO`
- `DESIGN_MECHANISM`
- `FIELD`

If the unresolved question is `FIELD`, do not write code to answer it.

## Current product decision

**METHOD FIRST. NO UI YET.**

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
```

## Prompt changes

Every prompt change must answer:

1. Which fixture failed?
2. What hidden judgment was missing?
3. What is the smallest rule that teaches it?
4. Which neighboring behavior could this rule damage?
5. What positive/negative fixture protects against that damage?

Do not tune the rubric after seeing a run merely to rescue the prompt.

## Memory rule

`memory/owner-language.yaml` is a prior, not truth.

Never turn an owner phrase into a permanent one-to-one diagnosis. Promote a mapping only after an explicit discriminator favored one mechanism over a neighbor.

## Anti-build stop

When the remaining uncertainty is taste, external comprehension, preference or behavior, stop and name the field observation required.

More internal analysis at that boundary is field debt in disguise.
