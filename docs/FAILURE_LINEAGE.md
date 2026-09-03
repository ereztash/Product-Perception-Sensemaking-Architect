# FAILURE LINEAGE — failures are training data, not embarrassment

Neta improves by retaining the exact failure that forced a new distinction.

A repaired failure should leave enough lineage to answer:

1. What did Neta do?
2. Why was that wrong?
3. Which hidden judgment was missing?
4. What is the smallest repair?
5. What neighboring behavior could the repair damage?
6. What gate/control demonstrates the repair?
7. What would make us remove or narrow the repair later?

## FL-001 — metaphor laundering

**Failure shape:** `"Windows XP" → too many borders → redesign`.

**Why wrong:** owner metaphor was treated as if it already named the mechanism.

**Missing judgment:** raw owner language is a signal, not a diagnosis. Several neighboring mechanisms may produce the same metaphor.

**Gate left behind:** ambiguous cases require competing mechanisms + a discriminator before redesign.

**Control:** more than three mechanisms is also rejected; breadth cannot become backlog flood.

## FL-002 — field fabrication

**Failure shape:** static/repo evidence → “users will find this clearer”.

**Why wrong:** the claim crossed from implementation/perceptual mechanism into external-human behavior without touching the field.

**Missing judgment:** claim reality floor + resolution authority.

**Gate left behind:** an `OUTCOME` claim requires `FIELD`; asserting it requires R6.

**Positive control:** an apparently polished R4 deployed result is deliberately given `ASSERT_FIELD_OUTCOME`; validator must reject it.

## FL-003 — gate that could not see its own defect

**Observed incident:** Wave 1 research gate accepted `fixture_path = None` because `str(None)` became the non-empty string `"None"`.

**Why important:** a rule existing in code was mistaken for evidence that the invalid state was observable.

**Missing judgment:** a gate must be shown capable of failure for the exact class it claims to reject.

**Gate left behind:** deliberate positive controls execute in the same run as the green fixture.

**Historical record:** retained in `research/GATE_RELIABILITY.md`.

## FL-004 — authority semantics present but not architectural

**Failure shape:** Wave 1 named `permission/authority` under W7 and promotion prose said promotion controls use, yet G/C/A/O + promotion status became the operational center while Reality/Authority/Permission were not first-class across every finding.

**Why wrong:** a cross-cutting constitutional concept was treated as a local research topic.

**Missing judgment:** evidence state and action permission answer different questions for every capability, not just trust/uncertainty work.

**Repair:** v0.2 canonical finding ledger makes reality, authority, requested use and permission explicit per claim.

**Contamination protection:** Wave 1 thresholds/statuses are not rewritten retroactively. See `research/AMENDMENTS.md`.

## FL-005 — encodability bias

**Failure shape:** “we can ask which second chess move the player considered” → build the probe.

**Why wrong:** implementability and diagnostic usefulness do not establish that a probe should exist. The probe may also alter the behavior it measures.

**Missing judgment:** requested use needs permission; information gain, cost and contamination risk are separate.

**Gate left behind:** before new instrumentation receives build permission it must name the live claims it separates, the authority, the cheaper alternative, contamination risk and reversal/removal condition.

## Failure entry template

```text
ID:
Observed failure:
Evidence:
Claim that overreached or collapsed:
Missing hidden judgment:
Smallest repair:
Neighbor at risk:
Gate / control:
Reversal / narrowing condition:
Status: OPEN | GATED | FIELD_REQUIRED | RETIRED
```

## Promotion rule

A failure does not automatically create a prompt rule.

It may create:

- a schema constraint;
- a validator rule;
- a fixture;
- a research question;
- a prompt candidate;
- or only a warning in lineage.

The repair belongs at the **lowest layer capable of preventing recurrence without distorting neighboring behavior**.
