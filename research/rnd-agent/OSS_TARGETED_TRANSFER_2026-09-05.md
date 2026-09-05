# R&D Agent — Targeted OSS Transfer, 2026-09-05

Status: `QUARANTINED_TARGETED_TRANSFER`

Purpose: compare materially different open-source/autonomous-research architectures against the already-frozen R&D Agent v0.1 baseline without allowing external patterns to leak into that baseline.

Frozen comparator:
- `prompts/RND_AGENT_V0_1.md`
- blob SHA `bc0e725d0449478d53b93bb6643d24404c22708c`
- freeze record `eval/rnd-agent/BASELINE_FREEZE_V0_1.md`

This study asks a bounded question:

> Which external architecture patterns could remove a named R&D-agent failure better than the current linear continuity loop, and under what boundaries/costs?

It does **not** ask which agent is most impressive or which framework should be copied.

---

## 1. Evidence set

### O1 — Microsoft R&D-Agent
Observed surface: `microsoft/RD-Agent` README and scenario/search excerpts, current main surface inspected 2026-09-05.

Key observed patterns:
- explicit `R`/Research and `D`/Development role separation;
- iterative hypothesis → experiment design → implementation → feedback/refinement loops;
- detailed run surfaces and experiment feedback;
- evaluation on MLE-bench with multiple independent seeds;
- scenario-specific specialization rather than one universal scientific workflow.

Potential transfer:
- separate hypothesis/experiment judgment from implementation only if coupled work repeatedly contaminates either function;
- persist experiment feedback as state rather than prose-only history.

Boundary/counterevidence:
- role split creates coordination overhead;
- MLE tasks provide relatively crisp executable objectives and cannot establish value for general research questions;
- peer R&D v0.1 should not become multi-agent merely because R&D-Agent is.

Primary R&D dimensions touched:
`FALSIFICATION_QUALITY`, `CLOSURE_CONTINUITY`, `COST_DISCIPLINE`.

### O2 — AI Scientist v2
Observed surface: `SakanaAI/AI-Scientist-v2` README, blob `3bb62d43ab4632b3bbffc2642f12beafe869d3a4`.

Key observed patterns:
- autonomous hypothesis → experiment → analysis → manuscript pipeline;
- experiment-manager-guided progressive tree search;
- multiple root drafts/workers and bounded debug depth;
- timestamped experiment logs and tree visualization;
- explicit sandbox warning for LLM-authored code.

Most important counterevidence:
- the project explicitly states v2's broader/open-ended tree approach does **not necessarily outperform v1**, especially where a strong template exists; broader exploration can lower success.

Potential transfer:
- branching/tree exploration should be an earned escalation for open-ended search or stagnation, not the default R&D control flow;
- autonomous code execution requires a controlled sandbox.

Primary R&D dimensions touched:
`COST_DISCIPLINE`, `FALSIFICATION_QUALITY`, `CLOSURE_CONTINUITY`.

### O3 — Agent Laboratory
Observed surface: `Point-Zheng/AgentLaboratory` README, blob `11710d7e9d9961684d4d379c18e7f52ebbea026b`.

Key observed patterns:
- phase decomposition: Literature Review → Experimentation → Report Writing;
- specialized agents per phase;
- explicit compute/resource notes supplied to agents;
- checkpoint/state saves and resume support;
- copilot mode allows bounded human participation.

Potential transfer:
- durable checkpoints are useful for long-horizon recovery;
- resource constraints should be explicit inputs to research planning;
- human intervention should be recorded rather than hidden.

Boundary:
- phase decomposition is task/workflow structure, not evidence that specialized agents improve our R&D judgment;
- report writing is downstream and is not currently part of the core R&D Agent telos.

Primary dimensions:
`CLOSURE_CONTINUITY`, `COST_DISCIPLINE`, `PEER_HANDOFF_QUALITY`.

### O4 — PaperQA2
Observed surface: `Future-House/paper-qa` README, blob `0b5639921586f03bd1f9d93445af9e0d17f37c48`.

Key observed patterns:
- literature retrieval as a dedicated tool/system rather than generic web browsing;
- metadata-aware retrieval and re-ranking;
- redundant metadata fetching, citation/journal metadata and retraction checks;
- reusable local full-text index;
- explicit Paper Search → Gather Evidence → Generate Answer stages;
- agent may adaptively re-query/rephrase rather than rely on one search.

Potential transfer:
- `RECOVER` may eventually benefit from a provenance-aware retrieval tool with reusable indexes and source metadata;
- retrieval quality and source support should remain separable from downstream claim disposition.

Boundary:
- PaperQA2 is primarily a scientific-literature retrieval/QA system, not a general experiment-selection or claim-authority agent;
- it should be a callable evidence-recovery capability, not the R&D Agent's constitution.

Primary dimensions:
`RECOVERY`, `LINEAGE_INDEPENDENCE`.

### O5 — OpenHands Benchmarks
Observed surface: `OpenHands/benchmarks` README, blob `f7998d10d8743d94e7dfc97f5e07552da7592420`.

Key observed patterns:
- SDK is pinned as a git submodule to an exact commit;
- benchmark/runtime compatibility is treated as versioned state;
- isolated Docker workspaces for reproducible execution;
- logs preserve tool calls, messages, error counts and run summaries;
- remote and local execution paths are explicit.

Potential transfer:
- R&D runs should preserve an environment/runtime fingerprint where execution reproducibility is material;
- exact tool/SDK/model boundary belongs in HOLDOUT/eval provenance;
- trace-level evaluation may expose failures hidden by final output.

Boundary:
- not every research task needs container-level reproducibility; require it when the run's conclusion depends on executable environment state.

Primary dimensions:
`CLOSURE_CONTINUITY`, `FALSE_REUSE_AVOIDANCE`, `FALSIFICATION_QUALITY`.

### O6 — MLE-bench
Observed surface: `openai/mle-bench` README/current leaderboard, inspected 2026-09-05.

Key observed patterns:
- long-horizon executable tasks with deterministic grading but stochastic agents;
- benchmark recommends at least 3 seeds and reporting mean ± SEM because agent/LLM variance is material;
- compute/time budgets are part of benchmark comparability;
- current leaderboard distinguishes source availability and grading-report availability.

Potential transfer:
- R&D Agent evaluation should treat repeated runs/seeds and resource budgets as first-class whenever stochastic variance can change a capability judgment;
- one successful trajectory is not automatically stable capability evidence.

Boundary:
- repeated seeds are an eval requirement when stochasticity is material; not every deterministic research instrument needs multi-seed repetition.

Primary dimensions:
`FALSIFICATION_QUALITY`, `COST_DISCIPLINE`, `CLOSURE_CONTINUITY`.

### O7 — DeepResearch Bench
Observed surface: `Ayanami0730/deep_research_bench` README, blob `2b96b70617f236e77555c8d1fa40c8942950b8c4`.

Key observed patterns:
- separates report-quality evaluation (RACE) from factual/citation support evaluation (FACT);
- dynamic task-specific evaluation criteria;
- citation support is checked at statement/source level;
- evaluator migration in 2026 preserves legacy results separately instead of silently mixing versions.

Potential transfer:
- evaluator/version identity is provenance and must be frozen for comparable HOLDOUT claims;
- final-report quality and claim-support quality should not collapse into one score;
- if evaluator semantics change, old/new results require explicit compatibility treatment.

Boundary:
- R&D Agent v0.1 is not a report-writing agent, so readability/comprehensiveness dimensions are not core promotion targets.

Primary dimensions:
`FALSIFICATION_QUALITY`, `CLOSURE_CONTINUITY`, `LINEAGE_INDEPENDENCE`.

### O8 — MLEvolve
Observed surface: `InternScience/MLEvolve` README, blob `5ca90e490d0053ee60265c4859af56d5c86ac056`.

Key observed patterns:
- Monte Carlo Graph Search rather than a single linear trajectory;
- global memory records plan, code, metrics and success/failure labels for every node;
- hybrid BM25 + FAISS retrieval from prior attempts;
- adaptive planning/code-generation modes based on search state;
- stagnation detection and cross-branch fusion;
- full run directories include search tree logs, best solution and top-K candidates;
- reports 3-seed benchmark results.

Potential transfer:
- prior attempts should be recoverable as structured experience, including failures, not only textual lessons;
- branching/fusion may help when a task has a reliable objective and linear local improvement stagnates;
- retrieval from prior attempts is a concrete architecture for `RECOVER` beyond source/document retrieval.

Strong boundary:
- MLEvolve's search is calibrated by machine-readable task metrics. General research often lacks a scalar oracle; graph search can optimize the wrong proxy while appearing productive.

Primary dimensions:
`RECOVERY`, `NULL_STATE_FIDELITY`, `COST_DISCIPLINE`, `CLOSURE_CONTINUITY`.

### O9 — Sibyl Research System
Observed surface: `Sibyl-Research-Team/AutoResearch-SibylSystem` README, inspected 2026-09-05.

Key observed patterns:
- inner research-iteration loop plus outer system self-evolution loop;
- persistent workspace/project memory;
- issue classification and reusable lessons;
- quality gates, failed-task exclusion, stuck-task detection and retry;
- explicit authoritative experiment state file;
- long-running session recovery/watchdog;
- system-level learning changes prompts/scheduling/architecture across projects.

Potential transfer:
- distinguish research-task learning from agent-capability learning;
- durable authoritative state and recoverable failure classes are directly relevant to research continuity;
- self-update requires a much stronger gate than ordinary run learning.

Critical boundary:
- automatic self-modification of prompts/architecture conflicts with our current promotion constitution unless a clean failure, neighbor, holdout and versioned repair have earned it;
- unrestricted execution is explicitly high-risk and is outside R&D v0.1 autonomy.

Primary dimensions:
`NULL_STATE_FIDELITY`, `CLOSURE_CONTINUITY`, `FALSIFICATION_QUALITY`.

---

## 2. Current external research triangulation

### T1 — verification gap
`Autonomous Research Agents: A Survey of AI Scientists and the Verification Gap` (2026, arXiv 2608.05179) reports a broad audit where code release is substantially more common than execution traces/seeds and explicit novelty-verification methods.

Transfer implication:
- artifact presence must not substitute for reproducible/claim-verifiable provenance;
- execution traces, attempt-selection policy and human-intervention disclosure are candidate missing fields in our current runtime/eval contracts.

### T2 — evidence graph as operational state
`EviGraph: Evidence-Guided Autonomous Research Agents` (2026, arXiv 2608.04738) represents Problem, Gap, Hypothesis, Experiment, Finding and Claim as a typed evidence graph used during execution, not only after the fact. It reports improvements in claim support/data consistency against compared research-agent baselines.

Transfer implication:
- this directly challenges whether one linear `rnd-research-task` object is sufficient for multi-claim/multi-experiment dependency structure;
- do not adopt a graph yet: create a fixture where linear state may lose or mis-bind dependencies and compare representations.

### T3 — scaffolding can hurt
`Mind the alignment gap: a spatial transcriptomics benchmark for scientific coding agents` (2026 preprint) reports that richer package/environment scaffolding increased tool exploration but reduced mean task performance in its evaluated setting; trace inspection exposed unnecessary transformations and fragile package-first behavior.

Transfer implication:
- more tools/context/architecture are not monotonic improvements;
- every OSS-derived capability needs a neighboring case where the simpler baseline should win.

### T4 — end-to-end research is still weak
`ResearchClawBench` (2026, arXiv 2606.07591) evaluates end-to-end autonomous scientific research across 40 tasks/10 domains and reports low absolute performance, with failures concentrated in experimental-protocol mismatch, evidence mismatch and missing scientific core.

Transfer implication:
- our eval should target protocol/evidence alignment, not only task completion;
- broad autonomous execution should remain downstream of clean bounded-judgment evidence.

---

## 3. Cross-system synthesis — what appears genuinely additive

The external systems do **not** justify replacing the frozen linear v0.1 with a multi-agent/tree/graph system.

They expose six candidate residuals not fully first-class in the current contracts:

1. **Attempt/selection provenance**
   - when multiple runs/branches are tried, preserve what was attempted and the policy selecting the reported result.

2. **Stochastic stability**
   - when agent/run variance can alter the conclusion, use repeated seeds/runs and report the distribution rather than one trajectory.

3. **Execution environment identity**
   - preserve environment/tool/model/runtime version when it can change runnability or result semantics.

4. **Checkpoint/rollback semantics**
   - long research work needs a recoverable last-known-good state so failed repair/execution cannot silently corrupt validated upstream evidence.

5. **Dependency-aware evidence state**
   - a linear task object may be insufficient when multiple hypotheses/experiments/findings share dependencies; this needs a discriminating fixture before any graph is built.

6. **Experience retrieval from prior attempts**
   - `RECOVER` currently names prior runs/nulls but does not specify a structured experience-memory mechanism. MLEvolve/Sibyl provide plausible implementations; value must be tested against retrieval cost, stale-memory risk and correlated-error reinforcement.

---

## 4. Patterns that should NOT enter v0.1 by default

- multi-agent specialization;
- tree/graph search;
- automatic self-modification;
- report/paper generation pipeline;
- global vector memory;
- critic/reviewer swarms;
- unrestricted shell/GPU autonomy;
- one universal research lifecycle.

Each is an intervention candidate, not a capability prerequisite.

---

## 5. Strongest architecture-level finding

The OSS landscape supports the same high-level direction as the portfolio synthesis but adds a stricter requirement:

> Research continuity is not only `claim → instrument → run → deposit → disposition`; for autonomous systems it also needs **attempt selection, stochastic/runtime provenance, and dependency-safe recovery** when those factors can change the claim.

The frozen baseline remains intentionally smaller so these residuals can be tested rather than assumed.
