# Executable Contract Repair Experiment — Stage 1 preregistration

Status: `PREREGISTERED_NOT_RUN`
Date: 2026-09-09
Prior decision: `STOP_UNIQUE_DELTA_UNSHOWN` for prose SYSTEM_IR generation advantage.

## Decision

Determine whether an executable contract adds unique repair value beyond an information-matched prose contract when both are applied to the same mechanism-broken software artifact.

Current default: **do not build a mechanism-transfer compiler/verifier**.

## Hypotheses

- H1 — executable contracts materially improve detection and repair of mechanism loss because red/green execution closes ambiguity that prose requirements leave open.
- H0 — a capable builder given the same contract semantics in prose repairs the artifact equally well; executable form adds no material repair delta in this setting.

This experiment tests repair fidelity only. It does not test user outcomes, cross-domain generality, commercial value, or autonomous mechanism extraction.

## Starting artifact

Use `candidate-1` from GitHub Actions run `34331181765`, artifact `mechanism-transfer-stage1-candidates-bf346508d2491bfc9cd5666c43d30eeedadbad20`.

That artifact was the prior SYSTEM_IR arm and already contains one known contract defect: its internal validator classifies `actual !== expected` as pass rather than `actual === expected`.

Before either repair arm is created, the execution harness deterministically seeds three additional mechanism defects into the same artifact:

1. back-to-edit from COMMIT discards the staged decision draft;
2. result chronology checks a surrogate/current-date condition rather than the user-entered `observationDate` against `committedAt`;
3. closing REVEAL routes to DECIDE rather than reaching EXPLORE.

The seed transform occurs before arm randomization. Both arms receive byte-identical broken application files.

## Contract families under test

C1 `DRAFT_ROUNDTRIP` — returning from COMMIT to DECIDE preserves every staged draft value.

C2 `ACTUAL_TEMPORAL_SUBSTRATE` — the user-entered observation date may not precede commitment; same-day chronology is valid. The actual field must be checked, not a surrogate timestamp.

C3 `VALIDATOR_DISCRIMINATION` — a deliberately malformed case on the actual temporal substrate must be classified correctly and a valid control must also be classified correctly. A permanently green or inverted validator is not a gate.

C4 `REACHED_STATE_TOPOLOGY` — after a valid result and REVEAL close, the core state machine reaches EXPLORE; EXPLORE is not merely declared or reachable through an unrelated side route.

Unseeded regression gates remain binding: evidence-production screens must not expose prior records/history, committed evidence must not become casually editable, syntax must remain valid, and no causal/improvement recommendation may be introduced.

## Arms

### Arm E — executable contract

Receives:
- the broken app;
- the same prose contract semantics as Arm P;
- an executable black-box contract suite encoding C1–C4;
- one repair session in which the builder may run the suite repeatedly until it decides it is done.

The executable suite is immutable. Editing it invalidates the arm.

### Arm P — prose contract

Receives:
- the identical broken app;
- the same prose contract semantics;
- an information-matched prose description of the exact public test cases used in Arm E;
- one repair session.

It receives no executable contract tests.

## Information matching

Both arms know the same four contract families and the same public examples/cases. Arm E differs only in that those cases can produce machine-observed red/green execution. No hidden evaluator cases are included in either arm.

## Builder controls

- builder: GitHub Copilot CLI, provider-default model;
- two fresh isolated temp directories;
- randomized arm order;
- identical starting application bytes;
- same runtime and tool permissions;
- one independent CLI repair session per arm;
- no human/evaluator feedback before scoring;
- builder instructed to read/work only in its current directory;
- hidden evaluator is not copied into either repair directory until both repair sessions finish.

## Primary endpoint

`HIDDEN_CRITICAL_FAILURES` — number of hidden behavioral gate families failed after repair. Lower is better.

Hidden gate families:

- H1 `DRAFT_ROUNDTRIP_VARIATION`: core and optional draft fields survive COMMIT → edit → DECIDE with unseen values.
- H2 `TEMPORAL_BOUNDARY`: a past observation date is rejected and a same-day observation date is accepted on the actual user field.
- H3 `VALIDATOR_DISCRIMINATION_VARIATION`: malformed and valid chronology controls are both classified correctly.
- H4 `STATE_TOPOLOGY`: valid flow reaches EXPLORE after REVEAL close.
- H5 `CAPTURE_REGRESSION`: DECIDE and COMMIT do not expose prior record/history content.
- H6 `SYNTAX_AND_TEST_INTEGRITY`: application syntax remains valid; Arm E's public executable contract file remains byte-identical.

H1–H4 are the seeded mechanism-repair target. H5–H6 prevent a nominal repair from buying success through regression or test tampering.

## Secondary endpoint

`DETECTION_RECALL` from `repair-report.json`: how many of the four seeded mechanism defects the builder explicitly identified. This is descriptive only; repair behavior outranks self-report.

Patch size and generic aesthetics are recorded but cannot change the decision.

## Stage 1 decision rule

After blind hidden scoring and before opening arm mapping:

- `ADVANCE_TO_REPLICATION`: executable arm has at least **2 fewer hidden critical failures** than prose arm, with no test-integrity failure and no new capture regression.
- `ADAPT`: executable arm has exactly 1 fewer hidden critical failure, or shows a clear localized executable-test benefit but also an architecture/test-design defect that prevents the stronger threshold.
- `STOP_EXECUTABLE_UNIQUE_DELTA_UNSHOWN`: tie or executable loss, or any apparent advantage is explained by test tampering / unequal information / regression.

Stage 1 cannot authorize BUILD.

## Stage 2 — only if Stage 1 advances

Run three additional independently randomized repair pairs from the exact same frozen broken base and contracts.

A bounded verifier prototype becomes worth building only if across four total pairs:

- executable wins on hidden critical failures in at least 3 of 4 pairs;
- median paired advantage is at least 2 hidden critical failures;
- zero executable runs modify the public contract tests;
- no advantage depends on information unavailable to prose arm.

Mixed/localized result => `ADAPT`.
Non-replication/equivalence => `STOP_EXECUTABLE_UNIQUE_DELTA_UNSHOWN`.

Even a Stage 2 win supports only a bounded executable-contract verifier/repair loop for this representation/runtime setting. It does not establish general software synthesis.

## Contamination and stopping rules

- Freeze this preregistration, public contract semantics, public test cases, hidden evaluator, seed transform and thresholds before repair generation.
- Do not change hidden gates after seeing repaired artifacts.
- Score repaired code behavior, not builder explanation.
- Open arm mapping only after blind hidden scores are frozen.
- Stop expanding this experiment once the current BUILD/ADAPT/STOP decision is resolved.
