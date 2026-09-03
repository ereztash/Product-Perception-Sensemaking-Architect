# Research promotion protocol

This file is the authority for moving a research candidate toward Neta behavior.

## Principle

A source does not become a prompt rule.

The shortest allowed research path remains:

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

## v0.2 clarification — research promotion is not general action permission

This clarification is prospective and is logged in `research/AMENDMENTS.md`.

The original promotion state answers what the **research quarantine** permits Neta developers to do with a research candidate.

It does **not** by itself authorize every downstream product/design claim or action.

For a concrete Neta finding, downstream use is now separately evaluated through:

```text
Claim
→ Evidence
→ Reality floor
→ Resolution Authority
→ Requested Use
→ ALLOW / DENY / DEFER
```

See `docs/REALITY_AUTHORITY_PERMISSION.md`.

Examples:

- `CANDIDATE_CAPABILITY` may authorize use in an evaluation fixture while still denying a universal design prescription.
- `PROMPT_ELIGIBLE` permits proposing a prompt change; it does not prove the changed Neta improves field outcomes.
- strong RESEARCH evidence may support a mechanism while FIELD permission to assert external-user behavior remains denied.

This clarification does not change any frozen Wave 1 threshold or original claim status.

## Required research-claim fields

Every research claim preserves:

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

G/C/A/O answers what kinds of evidence the research claim has.

Promotion state answers what the research workflow permits next.

Neither is a probability of truth. Neither is a substitute for the per-finding Reality/Authority/Permission contract.

## Source independence

The following do not count as independent triangulation by themselves:

- two papers using the same dataset;
- a review and one of the studies it summarizes;
- multiple vendor posts repeating one benchmark;
- translations of the same guidance;
- three papers from one lab operationalizing the same construct identically.

Record common lineage in `independence_family`.

## Counterevidence search

Before `ADVERSARIAL`, record at least:

1. one query/strategy designed to find contrary or null results;
2. one competing mechanism;
3. what would force narrowing, splitting or rejection.

“No contradictions found” is allowed only if the search itself is recorded.

## Culture/context gate

`culture_relevance` is:

- `material`
- `plausible`
- `low`

For material/plausible candidates, `BOUNDED` requires explicit represented and missing contexts. For low relevance, record why; “universal” is not an admissible rationale.

Country is a sample/context unless evidence establishes a mechanism.

## Contradiction dispositions

Every material contradiction gets exactly one:

- `REFUTES`
- `NARROWS`
- `SPLITS`
- `CONTEXTUALIZES`
- `MEASUREMENT_CONFLICT`
- `NO_MATERIAL_EFFECT`

`SPLITS` creates child claims and freezes the parent from further promotion until surviving children are evaluated.

`MEASUREMENT_CONFLICT` prevents synthesis into one effect until constructs are separated.

## Prompt gate

Research alone cannot directly edit `prompts/SYSTEM.md`.

A claim may reach `PROMPT_ELIGIBLE` only if:

- research gates are satisfied;
- a clean-model fixture exposes a Neta failure/blind spot without the capability;
- the smallest prompt change is specified;
- a neighboring behavior that could be damaged is named;
- a control fixture protects that neighbor.

The v0.1 prompt is frozen during the v0.2 architectural re-foundation. Re-foundation elegance is not a fixture failure.

## Demotion

Later evidence may:

- narrow wording;
- add a boundary;
- demote state;
- split a claim;
- reject a claim.

History is retained. Do not rewrite a failed candidate as if it was never proposed.

## Research authority ceiling

Do not continue reading merely to increase citation count.

Additional research is justified when a named unresolved `RESEARCH` question can change a concrete discriminator, boundary, fixture or promotion decision.

If the remaining material question belongs to REPO, ENVIRONMENT, OWNER or FIELD, route it there instead of paying more literature to answer the wrong question.
