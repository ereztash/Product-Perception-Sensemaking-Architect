# R&D Telos Self-Calibration — 2026-09-06

Status: `MANUAL_RND_CONTRACT_RUN · REPO_GROUNDED · CANDIDATE_TELOS · NOT_RUNTIME_EXECUTION · NOT_CANONICAL`

## Question

What is the narrowest R&D telos that preserves the cases where R&D produces material decision-path delta, while excluding work better handled by direct response policy, Neta, OWNER, REPO/ENVIRONMENT/FIELD, or generic orchestration?

## Runtime note

The repository's live Calibration Loop requires an external `OPENAI_API_KEY`. The present execution environment does not expose one, so this is a manual application of `prompts/RND_AGENT_V0_2_CANDIDATE.md` to repository evidence, not a live `runtime/calibration_loop/run.py --strict` trace.

## Recovered state

### Canonical ecosystem telos

The ecosystem as a whole exists to remove material uncertainty from consequential decisions while preserving lineage. Therefore this cannot itself be the unique telos of R&D.

### Canonical R&D boundary

`docs/AGENT_AUTHORITY_BOUNDARIES.md` still names R&D as the Research & Evidence Sensemaking peer. Its canonical strengths are claim targeting, evidence-family selection, research/instrument recovery, reuse/adapt/build decisions, falsification, execution-state fidelity, provenance, deposition, and research closure.

### v0.2 candidate expansion

`research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md` broadens R&D to:

> improve the fit between the system's resources and its telos, given the state from which the system is actually starting.

Operationally, however, the same document contains a narrower question:

> What is the cheapest admissible information that can change how resources should be allocated toward the telos?

That narrower sentence is closer to the observed useful behavior.

### Observed material-delta surface

The mechanically selected Yishumi historical holdout found full R&D materially changed the work path in 8/20 cases and added no material calibration delta in 12/20.

The 8 material cases shared a recurring structure:

- a reusable analysis protocol hard-coded decomposition/scoring before evidence;
- a source-selection protocol committed research volume/hierarchy before decision relevance;
- sparse evidence was converted into durable avatar/psychographic control policy;
- nested prompt/agent orchestration was adopted before simpler coordination was compared;
- a reusable prompt-improvement method contained untested ceremony;
- an image workflow purchased broad research and causal inference before the visual decision was bounded;
- inferred cognitive rules were about to be internalized as reusable policy;
- a weakly grounded composite score was about to drive a roadmap.

The 12 non-material cases were mostly direct/domain tasks, fixed owner constraints, bounded critique, factual product questions, or cheap reversible probes.

The earlier `QD_VS_RND_V0_RUN.md` also showed that a compact front-door gate can often avoid paying for the full loop, while R&D remains useful when the work path itself requires calibration.

## DIAGNOSE

### Material question

What exactly does R&D own that is neither generic reasoning nor generic resource management?

### Bottleneck

The phrase `improve the fit between the system's resources and its telos` is too broad. It can absorb:

- OWNER tradeoff decisions;
- orchestrator routing;
- production resource management;
- product prioritization;
- direct local reasoning.

This creates authority leakage and makes the agent expensive to invoke on tasks where local response policy or a domain authority is sufficient.

At the same time, reverting fully to `research continuity` is too narrow because observed useful R&D behavior includes choosing among research, recovery, tests, REPO/ENV/FIELD evidence, external scaffold, waiting, stopping, and sometimes a bounded build-as-test.

### Candidate teloi

#### A — Broad resource↔telos fit

> Improve the fit between all available resources and the system telos.

Strength: broad coverage.
Failure: weak ownership boundary; drifts toward orchestrator/general manager.

#### B — Research continuity only

> Remove research uncertainty while preserving claim→evidence→run→deposit→disposition continuity.

Strength: precise and canonically grounded.
Failure: misses the real choice that often occurs *before* research: whether research is the right uncertainty-reduction resource at all.

#### C — Consequential commitment uncertainty calibration

> Reduce decision-controlling uncertainty enough to justify or reject the next consequential resource commitment, using the cheapest admissible learning move.

Strength: captures the common mechanism across observed material cases while preserving bounded authority.

#### D — Reusable decision-machinery validation

> Prevent unvalidated reusable methods, rubrics and workflows from becoming durable control policy.

Strength: extremely sharp fit to many Yishumi positives.
Failure: too narrow; misses one-off but consequential cases where research/test/inspection allocation itself is the live problem.

## Cheapest decision-changing learning

Do not buy external research yet. The repository already contains positive and negative historical cases sufficient to discriminate the four candidate teloi at the conceptual-boundary level.

Compare candidates against:

1. observed material R&D cases;
2. observed no-delta cases;
3. canonical authority boundaries;
4. overlap with ecosystem telos;
5. overlap with Neta / OWNER / Orchestrator;
6. availability of a crisp fire/no-fire rule and stop condition.

## Observed delta

Candidate C provides the strongest current fit.

It preserves the useful v0.2 mechanism — choosing `RECOVER / RESEARCH / TEST / REPO / ENVIRONMENT / FIELD / SCAFFOLD / WAIT / STOP` based on decision value and cost — without granting R&D ownership over arbitrary project resources.

It also explains why many prompts should bypass R&D entirely: if there is no consequential resource commitment whose allocation can change after learning, the R&D telos is not active.

## Candidate telos

### Formal

> **R&D exists to reduce decision-controlling uncertainty enough to justify or reject the next consequential resource commitment, using the cheapest admissible learning move.**

### Operational

```text
ACCEPTED TELOS / OWNER INTENT
+ CURRENT STATE
+ PROPOSED OR PENDING CONSEQUENTIAL COMMITMENT
+ UNRESOLVED UNCERTAINTY THAT COULD CHANGE THAT COMMITMENT
→ CANDIDATE LEARNING / EVIDENCE MOVES
→ CHEAPEST ADMISSIBLE DECISION-CHANGING MOVE
→ OBSERVED DELTA
→ JUSTIFY / REJECT / RESCOPE / HANDOFF / WAIT / STOP
→ LEARN WHETHER THE RESOURCE DESERVES FUTURE REUSE
```

### Plain-language version

> **R&D decides what uncertainty is worth paying to remove before the system spends meaningful resources.**

## Unit of work

One live consequential resource commitment under unresolved decision-controlling uncertainty.

Examples of `resource commitment`:

- buying research;
- building/adapting a capability;
- institutionalizing a reusable protocol/rubric/template;
- adopting a data/evidence source as decision authority;
- invoking expensive expert/scaffold/agent work;
- committing meaningful engineering/content/analysis effort to a path;
- retaining or retiring a recurring method.

The word `resource` here does **not** mean R&D owns all project allocation. R&D owns only the uncertainty-reduction question that must be resolved before the commitment is epistemically justified.

## Fire condition

R&D should fire when all are true:

1. a consequential commitment of time, money, build effort, research effort, attention, authority or reusable process is pending;
2. at least one unresolved uncertainty could materially change whether, where, how much, or in what form that commitment should occur;
3. resolving that uncertainty requires choosing among non-equivalent learning/evidence moves, or the currently proposed move is itself materially costly;
4. a cheaper admissible observation may exist before full commitment.

Compactly:

```text
MATERIAL COMMITMENT
+ DECISION-CONTROLLING UNCERTAINTY
+ NONTRIVIAL CHOICE OF HOW TO LEARN
+ CHEAPER DISCRIMINATION MAY EXIST
→ R&D
```

## No-fire boundary

Prefer bypass/handoff when:

- the question is a bounded fact, calculation, explanation or creative generation task;
- a local response-policy move such as premise correction, clarification, refusal/redirect or balanced analysis resolves the issue;
- OWNER has fixed the relevant goal/constraint and no open allocation axis remains;
- a cheap reversible action is already the obvious discriminator and no calibration is needed first;
- the remaining uncertainty is directly owned by REPO, ENVIRONMENT or FIELD;
- the core problem is product signal→mechanism→intervention discrimination owned by Neta;
- the work path is already justified and the remaining task is execution.

## Stop condition

> **If no unresolved uncertainty can still change the next consequential resource commitment, R&D stops or hands off.**

This is stricter than `more research would be interesting` and stricter than `the system could still be improved`.

## Boundary to neighboring roles

### OWNER
Sets telos, accepted tradeoffs and risk. R&D cannot invent the objective to optimize.

### Neta
Determines what a product/design signal may mean, which mechanisms compete, and which intervention is justified. R&D may determine what evidence is worth buying before that intervention decision, but does not own the product meaning.

### REPO / ENVIRONMENT / FIELD
Resolve state/reality claims. R&D may choose to request that evidence; it does not inherit the authority of the source.

### Front-door gate
Decides whether the full calibration machinery is worth invoking at all. It is an efficiency/routing layer, not the R&D telos.

### Orchestrator
Coordinates compound work and dependencies. R&D may discover that coordination is costly, but does not become the generic router.

## Recalibration recommendation

`USE_DIFFERENTLY`

Do not promote this directly to canonical prompt wording yet.

Recommended interpretation:

- keep v0.2 as the current implementation candidate for comparison;
- treat `consequential commitment uncertainty calibration` as the narrowed telos hypothesis;
- build a fire/no-fire benchmark around this exact boundary;
- compare it prospectively against broad v0.2 on both material-delta recall and unnecessary-invocation burden.

## Falsifier

Reject or widen this telos if unseen cases repeatedly show material R&D decision delta when **no consequential resource commitment is pending**, or if the narrowed telos misses legitimate R&D-owned research/evidence work whose result matters materially but cannot be represented as justification of a commitment.

Reject or narrow it further if most apparent wins are already fully produced by Neta, local response policy, or direct authority lookup without a distinct R&D resource-learning decision.

## Current disposition

`CANDIDATE_TELOS_SUPPORTED_BY_RETROSPECTIVE_REPO_EVIDENCE`

Not yet:

`CANONICAL_RND_TELOS`
