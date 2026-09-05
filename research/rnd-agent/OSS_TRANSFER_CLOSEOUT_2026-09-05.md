# R&D Agent OSS Transfer Closeout — 2026-09-05

Status: `CLOSED_AT_ARCHITECTURE_SATURATION`

Inputs:
- `OSS_TARGETED_TRANSFER_2026-09-05.md`
- external surfaces from R&D-Agent, AI Scientist v2, Agent Laboratory, PaperQA2, OpenHands Benchmarks, MLE-bench, DeepResearch Bench, MLEvolve, Sibyl;
- final saturation probe: LoongFlow;
- current research triangulation: verification-gap survey, EviGraph, scientific-agent trace/scaffolding benchmark, ResearchClawBench.

## Stop decision

Routine OSS expansion stops here.

The final LoongFlow probe primarily repeated patterns already represented in the sample:

- structured Plan/Execute/Summary loops;
- explicit reflection on failure;
- structured experience memory;
- iterative learning/evolution.

It did not expose a new decision-relevant architecture axis that changes the current challenger queue.

Therefore another generic agent repository is unlikely to buy enough new information to justify continued source accumulation.

Reopen OSS discovery only when a named baseline failure requires an architecture family not represented here.

## What survived as high-value challengers

### Priority 1 — provenance/verification residuals

1. attempt set + result-selection policy when multiple attempts can alter the claim;
2. stochastic stability / repeated trajectories when variance is material;
3. execution environment/model/tool identity when comparability or runnability depends on them;
4. trace-level integrity when a final output can hide protocol violations or failed paths.

These are stronger than a generic demand for 'more logging' because each has a specific failure it prevents.

### Priority 2 — state representation residuals

5. dependency-safe claim/experiment/finding links;
6. checkpoint/rollback so failed downstream repairs do not corrupt validated upstream evidence.

The main unresolved representation question is now:

> Is the current linear `rnd-research-task` contract sufficient when several claims/experiments share dependencies, or does a typed evidence graph buy a distinction the linear form loses?

This is a fixture question, not permission to build a graph.

### Priority 3 — architecture interventions requiring comparative evidence

7. structured experience retrieval from previous attempts;
8. branching/tree/graph search after stagnation;
9. specialized research/development or phase-agent decomposition;
10. scientific retrieval subsystem/index.

These may be useful, but none is prerequisite to a valid R&D Agent v0.1.

## What was rejected as a default

- multi-agent by default;
- tree search by default;
- automatic self-modification;
- vector memory because memory is available;
- report-writing as a core R&D objective;
- unrestricted execution;
- one universal research lifecycle;
- copying the architecture of the highest leaderboard system.

## Strongest external counterexample to complexity

AI Scientist v2 explicitly reports that its more general/open-ended exploratory approach does not necessarily outperform the more structured v1 when a strong task template exists.

Independent scientific-agent benchmark evidence also reports a setting where richer scaffolding increased exploration while reducing task performance.

Together these establish a practical burden of proof:

> added agent architecture must beat the simpler baseline under matched decision and resource conditions; complexity is not presumed beneficial.

## Strongest external support for research continuity

The most direct convergence is not on multi-agent design but on **verification-state continuity**:

- verification-gap survey: runnable code is much more common than reproducibility/claim-verification artifacts;
- EviGraph: explicit claim-evidence dependency state improves claim support/data consistency in reported experiments;
- MLEvolve/Sibyl/LoongFlow: prior attempt outcomes are retained as reusable experience rather than discarded terminal outputs;
- OpenHands/MLE-bench: versions, environments, traces, seeds and budgets materially affect agent-evaluation interpretation.

This narrows the thesis:

> The next R&D-agent gains should first be sought in making research attempts verifiable, comparable, recoverable and correctly linked to claims — before adding search breadth or more agents.

## Next authorized sequence

1. Keep `prompts/RND_AGENT_V0_1.md` frozen at blob `bc0e725d0449478d53b93bb6643d24404c22708c`.
2. Validate the runtime/validator against controlled task objects.
3. Run the 8 original TRAIN controls against the frozen baseline.
4. Run Priority-A OSS challengers as visible/adversarial tests; they cannot count as HOLDOUT.
5. Freeze exact model/tool/evaluator/resource boundary.
6. Author unseen HOLDOUT cases only after the execution baseline is frozen.
7. Promote only the smallest repair earned by a clean failure.
8. Compare branching/memory/multi-agent challengers only if the simpler baseline exposes a failure those architectures plausibly address.

## Reopen conditions

Targeted OSS research may resume if:
- a new clean failure has no represented architecture candidate;
- an existing candidate is contradicted by a materially newer system/benchmark;
- the R&D Agent reaches a field where the current OSS sample's computational-ML assumptions are no longer transferable.
