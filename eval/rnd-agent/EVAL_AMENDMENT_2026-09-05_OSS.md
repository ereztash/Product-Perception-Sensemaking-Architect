# R&D Agent Eval Amendment — OSS Transfer, 2026-09-05

Status: `PROSPECTIVE_EVAL_INTEGRITY_AMENDMENT`

This amendment changes **evaluation provenance requirements**, not the frozen R&D Agent v0.1 behavior.

Original protocol remains `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`.

Reason for amendment:
Targeted OSS/benchmark review exposed evaluation-integrity variables that can materially change conclusions about long-horizon stochastic agents and were not explicit enough in the original protocol.

## Added requirements for future comparative/HOLDOUT runs

### 1. Agent/model/tool freeze
Record:
- agent prompt/implementation version;
- foundation model and relevant inference configuration;
- tool/runtime boundary;
- source commit/blob references where applicable.

### 2. Evaluator freeze
Record:
- evaluator implementation/model/version;
- rubric/criteria version;
- any change that makes old/new scores not directly comparable.

If evaluator semantics change, retain old results and create a new evaluation lineage rather than silently overwriting/mixing scores.

### 3. Resource budget
Record material constraints such as:
- wall-clock budget;
- token/API budget where measurable;
- compute/environment limits;
- search/tool-call limits where material.

Comparative claims require matched or explicitly normalized budgets.

### 4. Repeated runs / seeds
When agent or experimental stochasticity can plausibly reverse the capability judgment:
- run at least 3 independent seeds/trajectories where feasible;
- report distribution/mean and uncertainty rather than the best trajectory alone;
- if repeated runs are infeasible, narrow the claim to the observed trajectory and record the limitation.

This is not a universal requirement for deterministic instruments.

### 5. Attempt-selection provenance
If multiple attempts/branches are generated and a subset is reported:
- preserve the attempt set or a sufficient manifest;
- preserve the selection rule/policy;
- distinguish preregistered selection from post-hoc selection.

### 6. Execution traces
Preserve trace-level artifacts when process integrity can change the interpretation of the final result, including:
- leakage/unauthorized evidence access;
- tool/environment errors;
- protocol deviations;
- failed attempts hidden by a final successful artifact;
- human interventions.

Final-output success alone does not certify process validity.

## Source lineage for this amendment

- OpenAI MLE-bench: repeated seeds and resource-budget comparability for stochastic agents.
- OpenHands Benchmarks: exact SDK/runtime versioning, isolated workspaces and run logs.
- DeepResearch Bench: evaluator-version migration and separation of report quality from citation/factual support.
- Autonomous Research Agents verification-gap survey (2026): execution traces/seeds, novelty verification and result-selection disclosure are substantially less common than code release.
- Scientific-agent benchmark evidence that additional scaffolding can alter traces and reduce performance even when it appears to add capability.

## Contamination rule

These requirements may improve how v0.1 is **measured**. They may not be used to edit `prompts/RND_AGENT_V0_1.md` before a qualifying R&D capability failure.
