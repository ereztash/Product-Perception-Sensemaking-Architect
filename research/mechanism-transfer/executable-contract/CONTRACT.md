# Plant Decision Journal — repair contract

Repair the existing application without changing its product purpose or adding advice.

The app records a decision before feedback, freezes committed evidence, later records an observable result, reveals the comparison, then allows retrospective exploration. It must not claim that an action caused an outcome or improved the plant.

## C1 — DRAFT_ROUNDTRIP

DECIDE → COMMIT is a staging boundary, not destructive submission.

If the user chooses “back to edit” from COMMIT, every staged value must still be present when DECIDE renders again, including optional alternatives and rationale. Nothing should be committed merely by visiting COMMIT.

## C2 — ACTUAL_TEMPORAL_SUBSTRATE

The user-entered result field `observationDate` is the chronology substrate.

When a result is submitted:
- `observationDate < committedAt` must be rejected visibly and the result form must remain available;
- `observationDate == committedAt` is valid;
- the check must operate on the actual user-entered observation date, not on `loggedAt`, current date, render time, or another surrogate.

## C3 — VALIDATOR_DISCRIMINATION

The internal validation surface must discriminate the chronology rule rather than stay green by construction.

For a malformed fixture whose `observationDate` precedes `committedAt`, the chronology predicate should evaluate false and the fixture should be classified as a correctly caught malformed case.

For a valid control whose `observationDate` follows `committedAt`, the predicate should evaluate true and the control should be classified as correctly valid.

Both controls should therefore show that the validator behaved as expected. The classification rule is equivalence between actual predicate result and expected result, not inequality.

## C4 — REACHED_STATE_TOPOLOGY

The core flow is:

`DECIDE → COMMIT → WAIT_RESULT → RESULT → REVEAL → EXPLORE`

After a valid result is stored and REVEAL is closed, the normal core flow must reach EXPLORE. EXPLORE may not exist only as a side route while the core path returns to DECIDE.

## Regression constraints

Do not buy a local repair by breaking these existing properties:

- DECIDE and COMMIT do not expose prior records, prior performance, recommendations, scores, critique, or personalized patterns while new evidence is being produced.
- Committed evidence remains frozen in the normal flow.
- Missing evidence remains `NOT_MEASURED` rather than being turned into a causal or improvement claim.
- No horticultural recommendation or causal advice is added.
- Keep the static local architecture: `index.html`, `styles.css`, `app.js`, localStorage, no external services.
- Preserve valid JavaScript syntax.
