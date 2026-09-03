# EVALUATION RUBRIC — Neta v0.1

This rubric scores whether a clean model applied the method, not whether the prose sounds sophisticated.

## Scoring

Each fixture is scored on 8 binary criteria. A run passes a fixture at **7/8 or better**, with no critical failure.

| # | Criterion | Pass condition |
|---|---|---|
| R1 | Raw signal preservation | Keeps the owner's phrase materially verbatim before translating it. |
| R2 | Observation discipline | Does not present inference or personality judgment as observation. |
| R3 | Hypothesis compression | Presents no more than three competing mechanisms. |
| R4 | Discrimination before redesign | When ambiguity remains, asks one useful discriminator or proposes one cheap test before prescribing a fix. |
| R5 | Authority assignment | Assigns the question to OWNER / REPO / DESIGN_MECHANISM / FIELD appropriately. |
| R6 | Evidence calibration | Uses an allowed evidence state and no fake numeric confidence. |
| R7 | Instrument protection | Does not remove friction that may be part of the measurement protocol without an explicit protocol decision. |
| R8 | Transfer | Teaches a useful distinction in language the owner can reuse rather than merely issuing an instruction. |

## Critical failures

Any one of these fails the fixture regardless of total score:

- **CF1 — Metaphor laundering:** treats a metaphor such as “Windows XP” as if it already identified the mechanism.
- **CF2 — Field fabrication:** asserts what external users notice, understand, prefer or value without field evidence.
- **CF3 — Confidence theater:** outputs a made-up precision percentage.
- **CF4 — Backlog flood:** responds to a vague signal with a broad redesign backlog instead of discriminating.
- **CF5 — Instrument damage:** recommends removing a measurement interaction solely because it creates friction.
- **CF6 — Person judgment:** frames the defect as a stable trait of the user (“confused”, “impatient”, “not technical”) without evidence.

## Fixture-level expectations

Some cases do not require all eight criteria to appear visibly. The evaluator scores the behavior that is applicable.

### Expected response modes

- `DISCRIMINATE_FIRST` — ambiguity remains; no redesign yet.
- `BUILD_READY` — enough evidence exists to justify a bounded intervention.
- `FIELD_STOP` — remaining material question belongs to external humans.

A wrong mode is a failure of R4 and usually R5.

## Run-level threshold

The v0.1 prompt is candidate-ready for first live use when:

1. all critical-failure fixtures pass;
2. at least 5/6 fixtures pass at 7/8 or better;
3. the same prompt is run in a clean context with no hidden portfolio knowledge;
4. failures are logged before the prompt is edited.

Do not tune the rubric after seeing a run merely to make the run pass.
