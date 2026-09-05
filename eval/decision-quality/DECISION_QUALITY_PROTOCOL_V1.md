# Neta Prospective Decision Quality Protocol v1

Status: `PREREGISTERED_BEFORE_PROSPECTIVE_CASE_COLLECTION`

Purpose: test whether Neta improves real product decisions, not merely whether its reasoning looks disciplined.

## Primary comparison

For each eligible decision event, compare three independent lanes when feasible:

1. `OWNER_ALONE` — owner's initial decision before seeing model advice.
2. `GENERAL_BASELINE` — general product-review model using the same frozen evidence boundary.
3. `NETA` — frozen Neta prompt/version using the same evidence boundary.

The owner may ultimately choose any action. The benchmark measures decision quality, not obedience to Neta.

## Eligible decision event

A case enters only when all are true:
- a real product decision exists now;
- at least two materially different actions are plausible;
- the evidence available at decision time can be frozen;
- the eventual result can produce independent adjudication or a meaningful discriminator;
- the case is not manufactured only to make Neta look good.

Examples:
- build vs discriminate vs defer;
- which mechanism to test first;
- whether a UI change is justified by current evidence;
- whether an apparent issue belongs to REPO/OWNER/FIELD/ENVIRONMENT;
- whether a measurement probe is valid or reactive.

## Freeze before advice

Persist before any lane sees the others:
- case_id;
- timestamp;
- product/domain;
- exact evidence boundary;
- owner raw signal;
- material claim/question;
- candidate actions;
- cost/risk class;
- what evidence could later adjudicate the choice.

Freeze `OWNER_ALONE` first.
Then run baseline and Neta independently on identical evidence.

## Outputs

Each lane must record:
- decision/action;
- mechanism claim(s);
- authority;
- evidence state;
- next discriminator if any;
- predicted reversal condition;
- estimated implementation/measurement burden in ordinal bands only (`LOW | MEDIUM | HIGH`).

No scalar confidence score.

## Outcome dimensions — no composite

Track separately:

### D1. Decision correctness after adjudication
Was the chosen action supported, refuted, unresolved, or authority-invalid after independent evidence arrived?

### D2. False-build rate
Did the lane authorize implementation when a cheaper discriminator/owner/field decision was required?

### D3. False-defer rate
Did the lane defer when evidence already justified a narrow reversible build?

### D4. Reversal quality
When later evidence contradicted the initial judgment, did the lane state a reversal condition that actually caught it?

### D5. Evidence debt created
Did the decision create an unresolved claim that later had to be repaired because the original authority/reality floor was exceeded?

### D6. Decision latency / work
Count concrete steps or evidence acquisitions required to reach adjudicable action. Do not substitute subjective speed for measured steps.

### D7. Decision usefulness to owner
After adjudication, owner rates whether the lane changed the decision, clarified why, or merely restated what was known. This is subjective and must remain separate from correctness.

## Minimum first wave

`DQ1` minimum viable evidence requires:
- 12 prospective real decision events;
- at least 3 products/domains;
- at least 3 BUILD candidates;
- at least 3 DEFER/OWNER/FIELD candidates;
- at least 3 cases where a discriminator can resolve competing mechanisms;
- at least 2 Neta failures or explicit evidence that targeted failure discovery remains underpowered;
- at least 2 surviving Neta-vs-baseline decision deltas.

These are decision thresholds, not statistical proof.

## Independence and contamination

- Do not rewrite the evidence boundary after seeing Neta/baseline outputs.
- Do not let one lane see another before freeze.
- Do not count retrospective reconstructions as prospective cases.
- If the owner already knows the adjudication evidence, the event is training/history, not prospective evaluation.

## Adjudication

Preferred authority order depends on claim:
- REPO for implementation facts;
- OWNER for deliberate policy/tradeoffs;
- ENVIRONMENT for operational behavior;
- FIELD for external-user perception/behavior;
- independent experiment where mechanism requires it.

Adjudication states:
- `SUPPORTED`
- `PARTIALLY_SUPPORTED`
- `UNRESOLVED`
- `REFUTED`
- `AUTHORITY_INVALID`

## Stop / escalation

Pause if:
- lane contamination becomes recurrent;
- most cases cannot obtain independent adjudication;
- case mix collapses into one product or one action type;
- Neta version changes before the wave closes;
- owner-following behavior makes the benchmark measure compliance instead of decision quality.

## Current state

`READY_FOR_PROSPECTIVE_CASE_COLLECTION`

No retrospective case may be relabeled as a DQ1 prospective case.
