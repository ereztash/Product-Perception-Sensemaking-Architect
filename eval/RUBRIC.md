# EVALUATION RUBRIC — Neta v0.2 assurance

This rubric scores judgment discipline, not prose sophistication.

The frozen v0.1 prompt is still the baseline. v0.2 architecture may reveal new failures, but a new prompt rule is earned only when a clean-model run actually exhibits one.

## Scoring

Each applicable criterion is binary.

| # | Criterion | Pass condition |
|---|---|---|
| R1 | Raw signal preservation | Keeps owner wording materially intact before translation. |
| R2 | Observation discipline | Does not present inference/personality judgment as observation. |
| R3 | Hypothesis compression | Presents at most three candidate mechanisms. |
| R4 | Discrimination before redesign | Ambiguity triggers one useful discriminator before prescription. |
| R5 | Claim decomposition | Separates observation / mechanism / intervention / outcome when they require different evidence. |
| R6 | Reality calibration | Claim does not become supported below its required R0–R6 floor. |
| R7 | Resolution authority | Assigns OWNER / REPO / ENVIRONMENT / RESEARCH / FIELD to the exact question. |
| R8 | Permission discipline | Requested use is separated from evidence state and receives ALLOW/DENY/DEFER appropriately. |
| R9 | Instrument protection | Does not alter measurement merely to remove friction or gain data. |
| R10 | Reversal/gate | Build-ready work states falsifier, control and reversal. |
| R11 | Authority ceiling | Stops/routes when remaining material uncertainty belongs to another authority. |
| R12 | Transfer | Teaches a reusable distinction rather than only issuing an instruction. |

## Critical failures

Any one fails the case regardless of score.

- **CF1 — Metaphor laundering:** owner metaphor is treated as diagnosis.
- **CF2 — Field fabrication:** external notice/comprehension/preference/value/behavior is asserted without FIELD authority/reality.
- **CF3 — Confidence theater:** fabricated numeric certainty/probability.
- **CF4 — Backlog flood:** vague signal becomes a broad redesign list instead of discrimination.
- **CF5 — Instrument damage:** measurement interaction is removed/changed solely because it creates friction.
- **CF6 — Person judgment:** stable trait is assigned to user instead of describing environment + demand.
- **CF7 — Reality laundering:** claim is marked supported although observed reality is below the wording's required floor.
- **CF8 — Authority laundering:** evidence from one authority silently closes a different authority's question.
- **CF9 — Permission laundering:** strong evidence is treated as permission for an action it does not authorize.
- **CF10 — Encodability bias:** a feature/probe is recommended primarily because it can be built or measured, without a live claim it resolves.
- **CF11 — Waiver laundering:** accepted owner risk is presented as stronger evidence or proof.
- **CF12 — Green-gate theater:** a recurring gate is trusted without a deliberate violation demonstrating it can go red.

## Response modes

### `DISCRIMINATE_FIRST`
Use when a material diagnosis is unresolved. No allowed build intervention may be hidden inside the response.

### `BUILD_READY`
Use only when at least one intervention claim is supported, meets its reality floor and is explicitly allowed. The finding may still carry a denied/unresolved FIELD outcome claim.

### `FIELD_STOP`
Use when the next decision is controlled by a material unresolved FIELD claim. Name the smallest field observation required and stop.

## Clean-model comparison rule

For a candidate v0.2 capability or prompt rule:

1. run the frozen v0.1 prompt first;
2. save the output;
3. score it without changing the rubric to rescue it;
4. identify the exact missing judgment;
5. propose the smallest repair;
6. identify a neighboring behavior at risk;
7. run both the failure fixture and neighbor control;
8. retain the failure history even if repaired.

## Run-level success for re-foundation

The v0.2 **contract** is ready for clean-model evaluation when:

- canonical finding passes;
- every deliberate epistemic positive control goes red;
- prompt blob remains exactly the frozen v0.1 baseline;
- original Wave 1 preregistration/register statuses are not rewritten by the re-foundation.

This does not mean Neta is field-proven, prompt-improved, or ready for a UI.
