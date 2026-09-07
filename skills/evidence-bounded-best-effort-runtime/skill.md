# Evidence-Bounded Best-Effort Runtime

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

### 4. Adapter fallback is allowed only if semantics stay fixed
A fallback adapter may be introduced when it preserves:
- the same runtime entrypoint;
- the same agent prompts;
- the same bridge/semantic contract;
- the same deterministic routing;
- the same authority ceilings;
- the same trace shape;
- the same stop/failure semantics.

The adapter change must be explicit in provenance.

Preferred fallback order:
1. canonical provider + explicit canonical model;
2. alternate provider/CLI + explicit model;
3. alternate provider/CLI + provider-selected default model;
4. stop at FAILED_EXECUTION.

Never fall through to mock output merely to obtain a successful-looking trace.

### 5. Provenance downgrade rule
If the fallback provider or model differs from the canonical adapter, label it clearly.
If provider-selected model routing is used and exact lineage is unavailable, say so.
Never treat agreement between two resources executed through the same unknown/same model lineage as independent triangulation.

### 6. Run the canonical control flow
Execute the repository's real flow. For the current Evidence-Bounded Peer-Agent System this normally means:

TASK → R&D DIAGNOSE → DETERMINISTIC ROUTING
→ optional NETA / other allowed resources
→ R&D SYNTHESIZE
→ TRACE

Do not manually choose peer invocation when the runtime owns routing.

### 7. Preserve trace and final state
Save the execution trace as a durable artifact when possible.
Report the exact final state, e.g.:
- COMPLETE
- FAILED_EXECUTION
- PENDING_RESOURCE
- AUTHORITY_STOP

A workflow job completing is not equivalent to the calibration runtime returning COMPLETE.

## Interpretation discipline
When summarizing a successful run, separate:
- what the input already assumed;
- what R&D diagnosed;
- what routing actually fired;
- the unique delta contributed by Neta/other resources;
- what R&D changed in the decision;
- what remains unresolved because OWNER / REPO / FIELD / ENVIRONMENT authority was not supplied.

Never convert:
- plausibility into effectiveness;
- interpretation into FIELD evidence;
- user ownership into a proven cognitive mechanism;
- same-lineage peer agreement into independent evidence;
- a successful runtime invocation into validation of the agent itself.

## Default output structure
Keep the response decision-oriented:

1. **Execution status** — what actually ran, final_state, provider/model provenance, and any downgrade.
2. **Decision before → after** — did the run actually change the live decision?
3. **Bottleneck** — smallest material uncertainty/miscalibration identified.
4. **Unique resource delta** — especially whether Neta/R&D added something decision-relevant.
5. **Authority still missing** — OWNER / REPO / FIELD / ENVIRONMENT as applicable.
6. **Next move** — prefer smallest reversible decision-changing action over more reasoning or BUILD.
7. **Trace** — link or exact path/reference to the preserved artifact.

## Anti-build rule
If the central uncertainty is intervention effect or field behavior, prefer a bounded prospective test using existing capabilities over architecture work.
Only recommend BUILD when the run itself provides a decision-relevant reason that cannot be resolved more cheaply by reuse, adaptation, measurement, or field testing.

## Failure behavior
If every real execution path is blocked:
- return FAILED_EXECUTION;
- identify the concrete blocker;
- preserve logs/trace if possible;
- state the smallest action that would unblock a real run;
- do not fabricate R&D/Neta output.

## Canonical example learned from the Lichess ownership run
A format hypothesis (e.g. self-question vs declarative instruction) is not yet a mechanism or architecture finding. A useful discriminator should test the target decision operation itself, not merely recall, endorsement, completion, or subjective ownership. If prospective FIELD evidence is required, stop treating further internal coherence as proof and move to the smallest matched comparison that could change the product decision.
