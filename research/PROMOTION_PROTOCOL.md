# Research promotion protocol

This file is the authority for moving a research candidate toward Neta behavior.

## Principle

A source does not become a prompt rule.

The shortest allowed path is:

```text
SOURCE
→ CANDIDATE CLAIM
→ TRIANGULATION
→ FALSIFICATION
→ CONTEXT / CULTURE BOUNDING
→ DISCRIMINATOR
→ FIXTURE
→ CANDIDATE CAPABILITY
→ PROMPT ELIGIBILITY
```

Any skipped arrow is a defect.

## Required claim fields

Every claim must preserve:

- exact candidate wording;
- capability family;
- observable construct;
- neighboring explanations;
- supporting source IDs;
- independent evidence families;
- counterevidence search status;
- contradiction IDs;
- culture relevance and represented contexts;
- boundary conditions;
- reversal condition;
- one G/C/A/O vector;
- promotion state;
- recursive parent if split.

## Promotion is not confidence

Promotion state answers **what Neta is allowed to do with the claim**.

G/C/A/O answers **what kinds of evidence the claim has**.

Neither is a probability of truth.

## Source independence

The following do **not** count as independent triangulation by themselves:

- two papers using the same dataset;
- a review and one of the studies it summarizes;
- multiple vendor posts repeating one benchmark;
- translations of the same guidance;
- three papers from one lab operationalizing the same construct identically.

Record the common lineage in `independence_family`.

## Counterevidence search

Before `ADVERSARIAL`, record at least:

1. one query or strategy designed to find contrary/null results;
2. one competing mechanism or alternative explanation;
3. what evidence would force narrowing, splitting, or rejection.

"No contradictions found" is permitted only if the search itself is recorded.

## Culture/context gate

`culture_relevance` is one of:

- `material` — the construct plausibly changes with local convention, language, script, communication practice, or social meaning;
- `plausible` — possible context interaction, insufficient evidence to dismiss;
- `low` — primarily physical/technical mechanism with a written rationale.

For `material` or `plausible`, promotion to `BOUNDED` requires explicit represented and missing contexts.

For `low`, promotion requires a short reason; "universal" is not an allowed substitute.

## Contradiction dispositions

Every material contradiction gets exactly one disposition:

- `REFUTES`
- `NARROWS`
- `SPLITS`
- `CONTEXTUALIZES`
- `MEASUREMENT_CONFLICT`
- `NO_MATERIAL_EFFECT`

`SPLITS` creates child claims. The parent is frozen from further promotion until all surviving children have been evaluated.

`MEASUREMENT_CONFLICT` prevents synthesis into one effect until the constructs are separated.

## Prompt gate

Research alone cannot directly edit `prompts/SYSTEM.md`.

A claim may reach `PROMPT_ELIGIBLE` only if:

- the research gates are satisfied;
- a fixture exposes a Neta failure/blind spot without the capability;
- the smallest prompt change is specified;
- a neighboring behavior that could be damaged is named;
- a control fixture protects that neighbor.

This retains the Agent Architect rule: teach only hidden judgment that a failure demonstrated was missing.

## Demotion

Later evidence can:

- narrow wording;
- add a boundary;
- demote state;
- split a claim;
- reject a claim.

History is retained. Do not rewrite a failed candidate as if it was never proposed.
