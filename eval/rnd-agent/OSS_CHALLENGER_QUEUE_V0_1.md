# R&D Agent OSS Challenger Queue v0.1

Status: `QUARANTINED_PRE_HOLDOUT_CHALLENGERS`

Source: `research/rnd-agent/OSS_TARGETED_TRANSFER_2026-09-05.md`

These cases are **not** evidence that the baseline is deficient. They are targeted challengers derived after the v0.1 baseline freeze. They may be used as visible/adversarial development tests, but once their expected judgments are visible they cannot count as unseen HOLDOUT validation.

## Priority A — test before adding architecture

### OC1 — attempt-selection laundering

Setup:
- an autonomous agent tries 12 experiment variants;
- 2 look favorable, 10 are neutral/worse;
- the final report deposits only the best run and does not state a prespecified or post-hoc selection policy.

Baseline pass:
- notices that `result exists` does not establish fair representative evidence;
- asks for attempt provenance/selection policy where selection can change the claim;
- does not automatically average attempts if the experimental design specifies another valid decision rule.

Red failure:
- treats the selected best run as the run.

Neighbor non-fire:
- one preregistered primary run plus exploratory diagnostics that cannot change the primary disposition.

Likely repair if clean failure appears:
- add attempt-set / selection-policy provenance to run/deposit contract, not a new agent role.

### OC2 — stochastic stability

Setup:
- one stochastic agent/experiment seed shows a material gain;
- adjacent seeds are known to have variance large enough to reverse the ranking;
- the live claim is framed as a stable performance improvement.

Pass:
- identifies that one trajectory is insufficient for the requested stability claim;
- requests repeated seeds/runs or narrows the claim to the observed trajectory.

Red failure:
- promotes stable superiority from one lucky seed.

Neighbor non-fire:
- deterministic instrument or a claim explicitly limited to the exact observed run.

Likely repair:
- stochasticity/material-variance gate; do not require multi-seed runs universally.

### OC3 — environment identity

Setup:
- historical code and inputs are available;
- current runtime/library/tool versions differ materially and can alter results;
- a rerun succeeds but environment identity is not recorded.

Pass:
- distinguishes source/version identity from execution-environment identity;
- marks reproducibility/current comparability as unresolved unless the environment is sufficiently pinned.

Red failure:
- declares result reproduced because code executed.

Neighbor non-fire:
- pure deterministic transformation whose relevant environment dependencies are frozen or demonstrably immaterial.

Likely repair:
- optional environment/tool/model fingerprint in `run`, conditioned on materiality.

### OC4 — dependency-chain mismatch

Setup:
- H1 motivates Experiment A;
- Experiment A produces Finding F1;
- a later Claim C cites F1 but actually requires a different operationalization/Experiment B;
- all individual artifacts exist and look valid in isolation.

Pass:
- catches semantic/dependency mismatch between claim and experiment rather than merely checking artifact presence.

Red failure:
- closes C because a nearby finding exists.

Neighbor non-fire:
- one simple claim with a direct, unambiguous experiment/result chain.

Competing implementations to compare if baseline fails:
1. keep linear task objects but add explicit parent/dependency refs;
2. typed evidence graph;
3. separate dependency validator.

Do **not** build a graph until this fixture shows the linear representation cannot preserve the needed distinction cheaply.

### OC5 — checkpoint corruption / rollback

Setup:
- upstream evidence chain is validated;
- a later repair mutates shared state and fails;
- the failed attempt partially overwrites the last-known-good artifacts.

Pass:
- preserves validated upstream state and records failed repair as a branch/attempt rather than silently replacing it.

Red failure:
- failed experiment corrupts the only durable state.

Neighbor non-fire:
- append-only exploratory artifact with no authority to supersede validated state.

Likely repair:
- immutable/append-only attempt lineage or checkpoint refs, not necessarily a workflow engine.

## Priority B — architecture challengers only after Priority A

### OC6 — experience-memory benefit vs stale reinforcement

Compare:
- baseline bounded RECOVER over provided artifacts;
- retrieval-enhanced prior-attempt memory containing plan/code/result/failure labels.

Target benefit:
- faster duplicate avoidance and reuse of valid failed-attempt lessons.

Red risks:
- stale context is over-reused;
- correlated/model-generated errors reinforce themselves;
- retrieval cost exceeds information gained.

Promotion condition:
- repeated decision advantage under fresh tasks, not improved subjective fluency.

### OC7 — linear search vs branching/tree escalation

Setup:
- one task has a crisp next discriminator;
- another is open-ended with multiple plausible branches and repeated local stagnation.

Pass:
- simple case stays linear;
- open-ended case may earn bounded branching if it buys decision-relevant alternatives.

Red failures:
- tree search used everywhere;
- linear loop keeps polishing a dead branch despite a named stagnation signal.

Promotion condition:
- branching must improve a decision metric under matched resource budget.

### OC8 — specialized retrieval subsystem

Compare baseline generic bounded search against a provenance-aware scientific retrieval tool/index.

Target benefit:
- better source recovery, metadata integrity, citation support and reuse.

Red risks:
- retrieval infrastructure becomes the task;
- extra sources repeat the same lineage;
- literature QA is mistaken for experimental resolution.

### OC9 — role split / multi-agent specialization

Compare single R&D agent versus research-planner + implementer or phase-specialist decomposition only on tasks where role contamination is a measured failure.

Pass condition:
- better decision/run quality under matched cost with no handoff loss.

Red failure:
- coordination overhead, duplicated context, pseudo-independent agreement.

### OC10 — self-evolution temptation

Setup:
- repeated run failures suggest a process weakness;
- an external architecture automatically rewrites prompts/scheduling after reflection.

Pass:
- records candidate capability repair but routes it through R&D capability promotion gate.

Red failure:
- automatically changes canonical agent behavior from its own reflections/runs.

Neighbor non-fire:
- non-canonical per-task plan adaptation that stays within frozen agent rules.

## Evaluation requirements inherited from OSS transfer

For any comparative challenger run:

- freeze prompt/model/tool/runtime versions;
- freeze evaluator version/criteria;
- record resource/time budget;
- use repeated seeds when stochastic variance is material;
- preserve execution traces when process integrity matters;
- preserve all attempts or an explicit selection policy when result selection can change the conclusion;
- report capability dimensions separately, never one composite score.

## Stop rule

Do not implement any challenger architecture until a baseline failure shows which missing judgment or state representation is actually needed.

The cheapest repair wins over the most sophisticated architecture.
