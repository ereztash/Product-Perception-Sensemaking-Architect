# Mechanism Transfer Paired Experiment — preregistration v0.1

Status: `PREREGISTERED_NOT_RUN`
Date: 2026-09-09
R&D task: `CAL-MECHANISM-TRANSFER-2026-09-09`
R&D best-effort trace source: GitHub Actions run 34330244340. This trace was produced by the real Calibration Loop v0.2 through the stranded Copilot best-effort execution adapter; it is execution guidance, not canonical evidence and not independent triangulation.

## Decision

Determine whether a mechanism-bearing `SYSTEM_IR` yields more faithful implementation of source-independent mechanisms than an information-matched conventional product specification.

Current default: **do not build a general compiler**.

## Competing explanations

- H1 — `SYSTEM_IR` carries transferable mechanism structure that materially reduces implementation-level mechanism loss.
- H0 — any apparent advantage is adequately explained by detailed specification quality / informational richness / builder competence.

This experiment does not test user behavior, plant outcomes, commercial value, or cross-domain generality.

## Target domain

`Plant Care Decision Trace`: a low-stakes household-plant decision journal. Before a meaningful care action, the user records observation, intended action, expected observable response, confidence, optional alternatives and rationale; later records an observed result. The app must not give horticultural advice or claim causal improvement.

This target is new relative to both the chess source and the earlier outreach exploratory transfer.

## Arms

### Arm A — mechanism-bearing representation

Receives the target facts organized as:
- telos;
- explicit state machine;
- named invariants;
- epistemic claim object;
- authority/reality/permission boundaries;
- anti-patterns;
- interaction contract.

No source-domain chess nouns or implementation details are permitted.

### Arm B — information-matched conventional specification

Receives the same target-domain facts, fields, workflow requirements, prohibitions, epistemic claim fields, validation requirements and UI boundary, written as a conventional product/requirements specification rather than a mechanism representation.

Matching constraints:
- same target domain and user task;
- same required fields and stages;
- same behavioral prohibitions;
- same claim/status vocabulary;
- same validation examples;
- same implementation boundary;
- prompt length within 10% where practical;
- no extra examples, source-domain knowledge, or implementation hints in either arm.

Prompt length at freeze: Arm A ~5,312 characters / 769 whitespace tokens; Arm B ~5,068 characters / 738 whitespace tokens.

## Builder controls

- Same builder family: Lovable.
- Fresh project per arm.
- No template or design system.
- Same workspace where feasible.
- Default builder settings in both arms.
- No repair prompt before scoring.
- No evaluator feedback sent into either build.
- Same generation opportunity: one initial build turn.

## Primary endpoint

`CRITICAL_CONTRACT_VIOLATIONS` — count of failed critical gates below. Lower is better. No aesthetic, perceived usefulness, generic code quality, or build-success score may substitute for this endpoint.

### Critical gates

- `G1_CAPTURE_CONTAMINATION`: DECIDE and COMMIT expose no history, prior performance, recommendation, score, critique, or personalized pattern.
- `G2_REACHED_STATE_TOPOLOGY`: after result and REVEAL close, the core state machine reaches EXPLORE; EXPLORE is not merely a side route declared as a state.
- `G3_DRAFT_ROUNDTRIP`: quiet back-to-edit from COMMIT preserves every staged draft value.
- `G4_ACTUAL_TEMPORAL_SUBSTRATE`: the user-entered observation/result date cannot precede `committed_at`; the check operates on that actual field, not a surrogate timestamp.
- `G5_VALIDATOR_DISCRIMINATION`: a deliberately malformed fixture on the same actual field/substrate fails, and a valid negative control passes.
- `G6_COMMITTED_EVIDENCE_IMMUTABLE`: committed decision evidence cannot be silently edited by the normal flow.
- `G7_EPISTEMIC_CEILING`: retrospective history does not become a causal/personal mechanism or improvement claim; insufficient evidence remains `NOT_MEASURED`; no recommendation is a valid state.
- `G8_CLAIM_RECORD_INTEGRITY`: any factual `SUPPORTED` APP_RECORD claim is derived from or guaranteed consistent with actual seeded/runtime data rather than drifting hard-coded counts.

A gate is PASS only when the implementation path supports it. Presence of text asserting the rule is insufficient.

## Secondary endpoint

`SECONDARY_CONTRACT_VIOLATIONS`:
- more than one visually primary action in a workflow state;
- source-domain leakage;
- user must understand app architecture to find next action;
- required claim fields absent;
- invalid/missing result chronology handling outside G4/G5;
- generated recommendation where evidence state is insufficient.

Secondary endpoint breaks ties only. It cannot rescue a loss on critical gates.

## Validator qualification rule

Before a validator contributes evidence, it must demonstrate:
1. a seeded defect on the exact claimed rule/substrate produces red;
2. a valid control produces green.

A permanently green check, or a check against a surrogate field, is `NOT_A_DISCRIMINATING_GATE`.

## Stage 1 — screening pair

Generate exactly one fresh Arm A build and one fresh Arm B build.

Score both before any repair.

Decision after Stage 1:
- `ADVANCE_TO_REPLICATION`: Arm A has at least 2 fewer critical violations than Arm B **and** Arm A has no false-green validator failure under G5.
- `ADAPT`: Arm A shows a localized advantage but fails one or more critical gates in a way attributable to ambiguous/underspecified IR representation; freeze the failure before modifying the IR.
- `STOP_UNIQUE_DELTA_UNSHOWN`: Arm A ties or loses on critical violations, its apparent advantage exists only on secondary/aesthetic criteria, or any advantage depends on extra information rather than representation.

Stage 1 cannot authorize BUILD.

## Stage 2 — only if Stage 1 advances

Add three fresh runs per arm (4 total per arm), randomized in order.

A bounded `BUILD_REVERSIBLE` case is earned only if:
- Arm A has fewer critical violations in at least 3 of 4 paired comparisons;
- median paired advantage is at least 2 critical violations;
- no Arm A run contains a G5 false-green validator;
- the advantage cannot be attributed to unequal target facts or implementation hints.

Mixed/localized results => `ADAPT`.
Equivalence/non-replication => `STOP_UNIQUE_DELTA_UNSHOWN`.

Even a Stage 2 win supports only a bounded compiler/verifier prototype for the tested representation and builder setting, not general-purpose software synthesis.

## Contamination controls

- Freeze prompts before generation.
- Do not edit scoring gates after seeing outputs.
- Do not use source product terms in either prompt.
- No repair turn before score.
- Evaluate code/behavior against gates; do not infer mechanism preservation from visual similarity.
- Project/arm identity should not affect gate scoring; gates are predeclared binary execution-path claims.

## Stopping rule

Stop research expansion when the current build decision is resolved. A second target domain is deferred until a material, reproducible Stage 2 advantage exists.
