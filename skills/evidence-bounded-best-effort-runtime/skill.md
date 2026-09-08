# Evidence-Bounded Best-Effort Runtime

**Status:** v0.2 candidate — strengthened by self-calibration on 2026-09-08. The self-run is not validation of the skill.

## Description
Run an existing repository agent/runtime as genuinely as the environment allows, while preserving epistemic boundaries, provenance, contracts, routing, and authority. Use when the user explicitly wants the real runtime rather than a conversational simulation, especially with Neta, R&D, the Calibration Loop, or similar repository-defined agents.

## Triggers
Activate when the user asks things like:
- "בצע הרצה BEST EFFORT"
- "תריץ את הריפו באמת"
- "אל תדמה את הסוכן"
- "הפעל את R&D / Neta דרך ה-runtime"
- "אם ה-runtime חסום, תעשה הכי טוב שאפשר בלי להמציא פלט"

Do not activate for ordinary reasoning, summaries, or when the user explicitly wants a simulation.

## Core invariant
A result counts as agent/runtime output only if it was produced through the repository's actual runtime/adapters/contracts. Never read a prompt and answer "as if" you were the agent.

A successful-looking trace is not sufficient evidence that a fallback preserved the canonical decision operation.

## Best-effort ladder

### 1. Freeze the execution target
Identify and preserve:
- repository + exact ref/commit;
- task/input artifact;
- telos / decision being supported;
- canonical runtime entrypoint;
- canonical prompts/contracts;
- expected final states and trace format.

If a canonical task schema exists, validate the task before execution.

### 2. Try the canonical live path first
Use the repository's existing live adapter/provider exactly as designed when credentials and environment permit.

Do not silently change:
- agent prompts;
- routing law;
- authority boundaries;
- promotion gates;
- semantic output contracts;
- task content;
- success criteria.

### 3. On execution failure, classify the blocker
Distinguish at minimum:
- missing credential/secret;
- unavailable model/provider entitlement;
- workflow/runtime error;
- contract/schema failure;
- repository/environment mismatch;
- authority stop / missing FIELD, OWNER, REPO, ENVIRONMENT evidence.

Record the actual failure. Do not reinterpret an execution blocker as a research finding.

### 4. Adapter fallback is allowed only if protocol semantics stay fixed
A fallback adapter may be introduced only when it preserves the frozen protocol invariants:
- same runtime entrypoint;
- same task/input artifact;
- same agent prompt refs/content;
- same semantic output contract;
- same deterministic routing law;
- same authority ceilings;
- same trace/final-state semantics;
- same success criteria.

Do not claim model-level semantic equivalence. The admissible claim is narrower: the fallback preserved the frozen execution protocol while changing provider/model provenance.

Preferred fallback order:
1. canonical provider + explicit canonical model;
2. alternate provider/CLI + explicit model;
3. alternate provider/CLI + provider-selected default model;
4. stop at FAILED_EXECUTION.

Never fall through to mock output merely to obtain a successful-looking trace.

### 5. Fallback admissibility gate
Before treating a fallback result as decision-supporting, record a short equivalence record against the frozen target:

- exact repository ref/commit unchanged;
- exact task/input unchanged;
- runtime entrypoint unchanged;
- prompt refs/content unchanged;
- routing implementation unchanged;
- authority rules unchanged;
- semantic output validators/contracts unchanged;
- final-state semantics unchanged;
- fallback provider/model/adapter identified as far as the environment permits.

If any decision-relevant invariant changed, the fallback is a different experiment, not a substitute execution.

If these invariants cannot be checked, classify the result as **EXPLORATORY_FALLBACK**, even if `final_state=COMPLETE`.

### 6. Provenance persistence gate
Provider/model provenance must be persisted in a durable, inspectable artifact: preferably the execution trace, otherwise a sidecar manifest linked to the trace.

At minimum preserve when available:
- adapter/provider;
- explicit model or `provider-default`;
- reasoning/effort setting if applicable;
- repository commit;
- config used;
- fallback rung used;
- prior failed attempts and their blockers.

Console text, transient stderr, or a conversational summary alone is not sufficient provenance for a decision-supporting fallback.

If exact model lineage is unavailable, state that explicitly and downgrade the result. Unknown-lineage peer agreement is not independent triangulation.

### 7. Bounded fallback attempts
Do not provider/model-fish until something succeeds.

Default rule:
- attempt each fallback rung at most once;
- retry the same rung only when a material execution variable changed and record what changed;
- provider-selected default is the final live fallback rung;
- after that, return FAILED_EXECUTION.

A later success does not erase or reinterpret earlier failures.

### 8. Run the canonical control flow
Execute the repository's real flow. For the current Evidence-Bounded Peer-Agent System this normally means:

TASK → R&D DIAGNOSE → DETERMINISTIC ROUTING
→ optional NETA / other allowed resources
→ R&D SYNTHESIZE
→ TRACE

Do not manually choose peer invocation when the runtime owns routing.

### 9. Preserve trace and final state
Save the execution trace as a durable artifact when possible.
Report the exact runtime final state, e.g.:
- COMPLETE
- FAILED_EXECUTION
- PENDING_RESOURCE
- AUTHORITY_STOP

A workflow job completing is not equivalent to the calibration runtime returning COMPLETE.

A runtime returning COMPLETE is also not, by itself, proof that a non-canonical fallback is admissible for decision support; apply the fallback admissibility and provenance gates above.

## Interpretation discipline
When summarizing a successful run, separate:
- what the input already assumed;
- what R&D diagnosed;
- what routing actually fired;
- the unique delta contributed by Neta/other resources;
- what R&D changed in the decision;
- what remains unresolved because OWNER / REPO / FIELD / ENVIRONMENT authority was not supplied;
- whether the execution was canonical, admissible fallback, or exploratory fallback.

Never convert:
- plausibility into effectiveness;
- interpretation into FIELD evidence;
- user ownership into a proven cognitive mechanism;
- same-lineage peer agreement into independent evidence;
- a successful runtime invocation into validation of the agent itself;
- successful fallback execution into proof of semantic/model equivalence.

## Default output structure
Keep the response decision-oriented:

1. **Execution status** — what actually ran, runtime `final_state`, and execution class: canonical / admissible fallback / exploratory fallback.
2. **Provenance** — repo commit, adapter/provider, model/lineage if known, fallback rung, and prior blockers.
3. **Decision before → after** — did the run actually change the live decision?
4. **Bottleneck** — smallest material uncertainty/miscalibration identified.
5. **Unique resource delta** — especially whether Neta/R&D added something decision-relevant.
6. **Authority still missing** — OWNER / REPO / FIELD / ENVIRONMENT as applicable.
7. **Next move** — prefer smallest reversible decision-changing action over more reasoning or BUILD.
8. **Trace** — link or exact path/reference to the preserved trace plus provenance manifest if separate.

## Anti-build rule
If the central uncertainty is intervention effect or field behavior, prefer a bounded prospective test using existing capabilities over architecture work.
Only recommend BUILD when the run itself provides a decision-relevant reason that cannot be resolved more cheaply by reuse, adaptation, measurement, or field testing.

## Self-application and promotion guard
The skill may be run on itself to discover candidate improvements, but:
- self-application is not independent validation;
- one successful fallback case is not a promotion gate;
- a self-run may propose a revision, but promotion to a reusable rule should be supported by REPO evidence of the failure mode and, where the claim concerns operational reliability across cases, by bounded FIELD comparison on non-self cases.

Do not let the skill cite its own successful execution as evidence that its rules are generally valid.

## Failure behavior
If every real execution path is blocked:
- return FAILED_EXECUTION;
- identify the concrete blocker;
- preserve logs/trace if possible;
- state the smallest action that would unblock a real run;
- do not fabricate R&D/Neta output.

## Canonical example learned from the Lichess ownership run
A format hypothesis (e.g. self-question vs declarative instruction) is not yet a mechanism or architecture finding. A useful discriminator should test the target decision operation itself, not merely recall, endorsement, completion, or subjective ownership. If prospective FIELD evidence is required, stop treating further internal coherence as proof and move to the smallest matched comparison that could change the product decision.

## Self-calibration lesson — 2026-09-08
The self-run identified three distinct risks that must not be collapsed:
1. semantic-equivalence verification;
2. retry/provider-fishing control;
3. provenance-use gating.

Repository inspection then exposed a concrete provenance failure mode: a successful command adapter can discard successful-run stderr, while fallback provider/model metadata may be emitted only there and therefore never enter the durable trace. This is why provenance persistence is now an explicit gate rather than a reporting preference.
