# Mechanism Transfer Stage 1 — results

Date: 2026-09-09
Status: `STOP_UNIQUE_DELTA_UNSHOWN`
Preregistration: `research/mechanism-transfer/PREREGISTRATION_2026-09-09.md`
Builder deviation: `research/mechanism-transfer/EXECUTION_DEVIATION_01_2026-09-09.md`

## Decision

Stage 1 does **not** show a unique implementation advantage for the current mechanism-bearing `SYSTEM_IR` over an information-matched conventional specification.

Do not advance to Stage 2 replication under the frozen protocol. Do not build a general mechanism-transfer compiler from this evidence.

This is not a refutation of mechanism transfer in general. It is a failure to show the current representation's unique delta under this target, builder and single paired run.

## R&D provenance

The canonical `main` OpenAI-backed workflow was attempted first from frozen task `CAL-MECHANISM-TRANSFER-2026-09-09` and stopped at the missing live adapter credential before semantic R&D execution. That run is `FAILED_EXECUTION`, not an R&D result.

A second, explicitly best-effort execution used the repository's existing Calibration Loop v0.2 with the GitHub Copilot CLI execution adapter on branch `research/rnd-self-triangulation-2026-09-08`.

- R&D workflow run: `34330244340`
- runtime: Calibration Loop v0.2
- adapter: `runtime/calibration_loop/copilot_resource_adapter_v02.py`
- provider: GitHub Copilot CLI
- CLI version: `1.0.83`
- model: provider-default
- exact model lineage: unknown
- authority: `BEST_EFFORT_EXECUTION_ONLY_NOT_CANONICAL_EVIDENCE`

The R&D output retained the no-build default and recommended the information-matched paired discriminator used here. It also required exact-substrate positive controls and deferred a second target domain until a reproducible first-domain advantage exists.

## Execution deviation

Lovable was preregistered as the common builder. The first Arm A project creation was rejected before project creation because the user-owned workspace had no credits. No successful artifact was generated before the deviation was recorded.

Stage 1 therefore substituted GitHub Copilot CLI for both arms, under the controls recorded in `EXECUTION_DEVIATION_01_2026-09-09.md`.

Interpretation is limited to this builder setting.

## Frozen inputs

- Arm A: `ARM_A_SYSTEM_IR_2026-09-09.txt`
- Arm B: `ARM_B_MATCHED_SPEC_2026-09-09.txt`
- Target: household plant-care decision journal
- Arm A prompt at freeze: ~5,312 characters / 769 whitespace tokens
- Arm B prompt at freeze: ~5,068 characters / 738 whitespace tokens

Both arms received the same target-domain facts, fields, workflow, prohibitions, epistemic vocabulary, validation requirement and implementation boundary. Arm A expressed them as a mechanism-bearing IR; Arm B expressed them as conventional product requirements.

## Generation provenance

GitHub Actions run: `34331181765`
Commit: `bf346508d2491bfc9cd5666c43d30eeedadbad20`
Builder: GitHub Copilot CLI, provider-default model
Format: static `index.html` + `styles.css` + `app.js`, vanilla JavaScript + localStorage
Generation turns per candidate: 1
Repair turns before scoring: 0

Candidate artifact:
- artifact id: `10095908088`
- digest: `sha256:eceea51f43cedc86506ad5c9c08e9244e125cc3488cc289e460ed86a11e76655`

Separate randomized mapping artifact:
- artifact id: `10095908617`
- digest: `sha256:560530ce90b217295213e4f14f3bb391344494dd38adc41fe5c4bbc8e51811ac`

Both generated `app.js` files passed `node --check` before scoring.

### Candidate file hashes

Candidate 1:
- `index.html`: `1d5238c5f395d27c6670c3312bcb5a89e01e4b7067e5e0b29eda7436cb802b36`
- `app.js`: `e0969e4aa6ff98a6ad09ac621c20980502fc072b406a2bf5ef9aea94797af521`
- `styles.css`: `b208a39ea8efe545aed6c5f5f5139a1620fd3b0dd4cf233bf0eb2c538e02c9e5`

Candidate 2:
- `index.html`: `cad4364d7c3567180fbe4974531224d12264901ffe56f479d847dbeadc4245d5`
- `app.js`: `12cb2b8cefcaf2098ab0660dde3a9c0494450c61d4f6e413d897d033f295bfd3`
- `styles.css`: `207ad494508bf39684f84d04df6a0ed9f837260978a0cad114f0bace83484d3a`

## Blind scoring

The mapping was not opened until after both candidates were scored against the eight preregistered critical gates.

| Critical gate | Candidate 1 | Candidate 2 |
|---|---|---|
| G1 Capture contamination | PASS | **FAIL** |
| G2 Reached-state topology | PASS | PASS |
| G3 Draft roundtrip | PASS | PASS |
| G4 Actual temporal substrate | PASS | PASS |
| G5 Validator discrimination | **FAIL** | PASS |
| G6 Committed evidence immutable | PASS | PASS |
| G7 Epistemic ceiling | PASS | PASS |
| G8 Claim-record integrity | PASS | PASS |
| **Critical violations** | **1** | **1** |

The primary endpoint was therefore tied before unblinding.

Under the preregistration, `ADVANCE_TO_REPLICATION` required Arm A to have at least two fewer critical violations than Arm B and no G5 false-green. This condition was already impossible before the mapping was opened.

## Unblinding

Randomized mapping:
- Candidate 1 = **Arm A — SYSTEM_IR**
- Candidate 2 = **Arm B — information-matched conventional specification**

Therefore:

| Arm | Critical violations | Critical failure |
|---|---:|---|
| A — SYSTEM_IR | 1 | G5 validator discrimination |
| B — matched conventional spec | 1 | G1 capture contamination |

The primary endpoint is a tie.

On the preregistered secondary endpoint, Arm A also omitted several required claim-object fields in its concrete claim objects, while Arm B represented the required claim fields more completely. Secondary criteria cannot rescue or reverse the primary result.

## Failure analysis

### Arm A failure — G5 validator discrimination

Arm A created both malformed and valid examples on the correct `observationDate` versus `committedAt` concept, but its validation-screen qualification logic inverted the expected-result comparison:

- malformed case: actual `false`, expected `false` -> displayed as not passing the control;
- valid case: actual `true`, expected `true` -> also displayed as not passing the control.

Thus it failed to demonstrate the required combination: seeded defect red + valid negative control green.

This is especially decision-relevant because validator discrimination was one of the purported mechanism-bearing advantages inherited from the source/assurance architecture.

### Arm B failure — G1 capture contamination

Arm B exposed a direct clickable longitudinal-record navigation item during decision capture. The route allowed access to prior records while evidence was being produced, violating capture isolation.

Thus the conventional specification preserved the validation mechanism better in this run, while losing the state-boundary isolation mechanism.

## Environment limitation

A live browser runtime pass was attempted in the analysis environment, but localhost/file URL browser access was blocked by the environment. Therefore the Stage 1 score is based on:

- generated source-code execution-path audit against preregistered binary gates;
- JavaScript syntax validation via `node --check`;
- preserved generation artifacts and hashes.

It is **not** a claim that every path was exercised in a real browser. This limitation does not change the frozen Stage-1 decision because the primary result is a tie, but it lowers the strength of any individual PASS assertion that depends on runtime behavior.

## Frozen decision rule applied

Preregistered rule:
- advance only if Arm A has >=2 fewer critical violations than Arm B and no G5 false-green;
- adapt only if Arm A shows a localized advantage but retains critical failures attributable to IR ambiguity;
- otherwise `STOP_UNIQUE_DELTA_UNSHOWN`.

Observed:
- Arm A: 1 critical violation;
- Arm B: 1 critical violation;
- Arm A did not show a primary advantage;
- Arm A itself failed G5.

Decision: **`STOP_UNIQUE_DELTA_UNSHOWN`**.

## Permitted conclusion

Supported for this run:

> A mechanism-bearing SYSTEM_IR and an information-matched conventional specification produced equal critical contract-conformance scores in one blinded paired generation under GitHub Copilot CLI. The current SYSTEM_IR's unique implementation delta is therefore not shown.

Not supported:
- mechanism transfer is impossible;
- conventional specifications are universally equivalent to mechanism IRs;
- the result generalizes across builders or domains;
- the first Lovable outreach transfer was meaningless;
- a future revised IR cannot earn a measurable advantage.

## Next decision boundary

Do not run Stage 2 under this preregistration.

A new experiment is justified only if it tests a *new, narrower hypothesis* that explains why the current representation should outperform a matched spec, rather than merely rerunning the same broad claim. Candidate follow-up questions include whether executable/generated contracts, rather than prose invariants, are the actual missing representation layer; or whether the differentiating value lives in automated reverse extraction + verification rather than in the IR prose format itself.
