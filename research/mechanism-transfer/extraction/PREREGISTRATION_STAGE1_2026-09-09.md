# Autonomous Mechanism Extraction — Stage 1 preregistration

Status: `PREREGISTERED_NOT_RUN`
Date: 2026-09-09
Source: `ereztash/lichess_app@06828afbc1405a839dfc983a065bcb10109c5e02`
Prior decisions: prose SYSTEM_IR generation advantage = unshown; executable-contract repair advantage = unshown.

## Decision

Determine whether a structured reverse-engineering protocol can discover preservation-worthy product mechanisms from code alone better than a strong conventional reverse-engineering prompt, before building an extraction/compiler layer.

Current default: **do not build an autonomous mechanism extractor**.

## Hypotheses

- H1 — structured mechanism extraction yields materially higher recovery of independently documented preservation targets from a code-only snapshot.
- H0 — a capable model with a strong ordinary reverse-engineering request recovers the same targets; structured extraction adds no material delta.

## Source isolation

Both arms receive the same frozen production-code snapshot copied only from existing paths among `client/`, `shared/`, `server/`, `api/`, plus package/config files needed to understand structure. Before extraction, all `.git`, Markdown, docs, tests/specs, research material and repository instructions are removed. README and `docs/INERTIAL_UX_LAWS.md` are used only to freeze hidden gold and are not present in either extraction directory.

No source-domain documentation or git history may be read by either arm.

## Hidden gold

Eight preservation targets were frozen from product documentation that predates this experiment. Gold is limited to mechanisms that should leave discoverable traces in production code. The hidden gold file is not supplied to either extractor.

Targets cover:
1. measurement-before-intervention / no prior-record or engine exposure while producing evidence;
2. one primary action per interaction state;
3. interaction mode/state as the central permission contract for what may be shown or executed;
4. centrally derived next action from product/record state, with `none`/wait as legitimate outcomes rather than forced advice;
5. explicit board authority by stage/mode, with no undeclared interaction authority;
6. persisted record as source of truth rather than screen-local copies;
7. explicit representation of blind/unknown inputs rather than silently treating missing context as a wrong recommendation;
8. action selection based on what the record is missing, not player-specific inferred weakness that would contaminate later measurement.

## Arms

### Arm S — structured mechanism extraction

Receives a structured reverse-engineering protocol: establish the problem frame from code; map actors/states/authority/evidence boundaries; search for repeated constraints and conservative defaults; distinguish mechanisms from implementation details using a cross-domain counterfactual; identify the failure caused by removal; rank only preservation-worthy invariants; mark uncertainty instead of filling gaps.

### Arm B — strong conventional baseline

Receives the same task, output schema, maximum item count, definition of preservation-worthy mechanism, evidence requirements and source isolation. It is instructed as a senior architect to reverse engineer the codebase for reimplementation, but without the structured decomposition/protocol above.

## Shared output contract

Each arm returns one JSON object with:
- `telos_hypothesis`;
- up to 12 `items`, each with `mechanism`, `type`, `why_preserve`, `failure_if_removed`, at least one code `evidence` path/symbol/reason, and confidence;
- `uncertainties`.

Allowed `type`: `measurement_boundary`, `state_authority`, `action_selection`, `interaction_permission`, `persistence`, `epistemic_boundary`, `other`.

## Primary endpoint

`GOLD_RECALL_POINTS` from 0 to 8.

Three blinded judge runs receive both candidate outputs, the hidden gold, and the sanitized source snapshot. For each gold target a judge assigns:
- 1.0 = mechanism is substantively recovered with code evidence;
- 0.5 = partial recovery missing a load-bearing element;
- 0 = absent, contradicted, or only a surface implementation detail.

Per-target score is the median of the three blinded judges. Primary score is the sum of the eight medians.

## Integrity and secondary endpoints

Deterministic pre-judge checks:
- output parses as required JSON;
- no more than 12 items;
- every cited evidence path exists in sanitized source;
- no docs/README/test/research path leakage.

Judges also report unsupported mechanism count. This is secondary and cannot rescue lower gold recall.

## Stage 1 decision rule

- `ADVANCE_TO_REPLICATION`: Arm S exceeds Arm B by at least **2.0 GOLD_RECALL_POINTS**, has no source-isolation violation, and does not have more than one additional unsupported mechanism.
- `ADAPT`: Arm S exceeds Arm B by 0.5–1.5 points and the advantage/localized miss identifies a specific protocol ambiguity worth changing.
- `STOP_EXTRACTION_UNIQUE_DELTA_UNSHOWN`: Arm S ties, loses, or any apparent advantage depends on leakage, invalid evidence paths, output-format failure, or non-gold stylistic/detail differences.

Stage 1 cannot authorize BUILD.

## Stage 2 — only if Stage 1 advances

Repeat on at least two additional source systems with independently frozen gold created before extraction, plus repeated stochastic runs. Only replicated advantage can justify a bounded `BUILD_REVERSIBLE` extractor prototype.

## Stopping rule

Do not expand the experiment if Stage 1 resolves the build decision. A result that a generic strong baseline recovers the same mechanisms is an anti-build finding, not a reason to add more prompt structure.
