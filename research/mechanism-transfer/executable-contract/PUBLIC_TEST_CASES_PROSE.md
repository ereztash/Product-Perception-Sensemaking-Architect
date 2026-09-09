# Public repair cases — prose form

These cases contain the same public information encoded by the executable contract arm. Use them to inspect and repair the application. They are not hidden evaluator cases.

## Case P1 — draft roundtrip

1. Start in DECIDE.
2. Enter non-empty values into: plant, condition, intended action, objective, expected response, confidence, alternatives, and rationale.
3. Submit to reach COMMIT.
4. Choose back-to-edit.
5. Expected: DECIDE renders with every staged value unchanged, including alternatives and rationale.

## Case P2 — actual chronology substrate

1. Create and commit a valid decision.
2. Enter RESULT.
3. Set the user-facing `observationDate` to a date earlier than the commitment date.
4. Submit.
5. Expected: submission is rejected visibly and RESULT remains open.
6. Change `observationDate` to the same calendar date as commitment.
7. Submit again.
8. Expected: submission is accepted and REVEAL is reached.

The relevant value is the user-entered `observationDate`; do not substitute current time, render time, `loggedAt`, or another timestamp.

## Case P3 — validator discrimination

The validation surface contains two public chronology controls:

- malformed: `committedAt = 2026-08-20`, `observationDate = 2026-08-19`, expected chronology predicate = false;
- valid: `committedAt = 2026-08-20`, `observationDate = 2026-08-21`, expected chronology predicate = true.

Expected: both controls are reported as correctly classified. The classification should test whether `actual === expected`.

## Case P4 — reached state topology

1. Create a valid decision.
2. Commit it.
3. Record a valid same-day result.
4. Reach REVEAL.
5. Close REVEAL.
6. Expected: the normal core flow reaches EXPLORE, where retrospective records are visible and a new-decision action is available.

## Regression check

After repair, DECIDE and COMMIT must still avoid exposing retrospective records/history while a new decision is being produced. Do not add causal or improvement recommendations.
