# Calibration Loop Runtime v0.1

Status: `IMPLEMENTATION_CANDIDATE`

Purpose: automate the recurring collaboration pattern in which R&D diagnoses how resources should be calibrated to a live telos, selectively invokes Neta and/or an external reasoning scaffold, and then synthesizes the deltas into the next move and a durable learning record.

This runtime is **not an Orchestrator Agent**. Routing is deterministic and inspectable. The only learned/judgment-bearing components are the peer/resource adapters it invokes.

## Core flow

```text
CALIBRATION TASK
      ↓
R&D DIAGNOSE
      ↓
DETERMINISTIC ROUTING GATE
      ├── NETA      when discrimination/proxy/intervention triggers fire
      ├── SCAFFOLD  when broad/novel/architecture synthesis is requested
      └── AUTHORITY handoff when OWNER/REPO/ENVIRONMENT/FIELD owns the remainder
      ↓
R&D SYNTHESIZE
      ↓
TRACE + RESOURCE DELTAS + LEARNING RECORD
```

## Why routing is deterministic

The project does not yet have evidence that a learned orchestrator adds value. A deterministic gate provides the cheapest admissible coordination layer while preserving an auditable record of:

- why a resource was invoked;
- which resource changed the decision;
- what unique distinction it added;
- whether the invocation was worth its cost;
- which routing rule should later be challenged.

A future orchestrator must be earned by repeated routing/dependency failures under this simpler system.

## Resource roles

### R&D

R&D owns the calibration question:

> Given the telos, current state, available resources and blocked decision, what currently limits progress and what is the cheapest decision-changing learning move?

R&D runs twice: `DIAGNOSE` before routing and `SYNTHESIZE` after resource outputs are collected.

The live adapter uses `prompts/RND_AGENT_V0_2_CANDIDATE.md` plus `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`. The frozen R&D v0.1 remains a comparator and is not silently overwritten.

### Neta

Neta is invoked only when at least one Neta trigger fires:

- signal→interpretation ambiguity;
- multiple plausible mechanisms;
- proxy-substitution risk;
- research/evidence is about to become an intervention/build decision.

Neta is a peer resource, not a subordinate R&D worker and not a mandatory ceremony. The live adapter loads the canonical Neta prompt from `prompts/SYSTEM.md` and adds only a runtime return-shape bridge.

### SCAFFOLD

`SCAFFOLD` is an external broad-reasoning resource (currently represented by an OpenAI reasoning model in the provided live adapter). It is useful for architecture alternatives, novel synthesis and expert-level reasoning that is cheaper to borrow than to internalize immediately.

R&D must learn from scaffold use rather than treating scaffold output as ground truth. The scaffold prompt is `prompts/SCAFFOLD_RESOURCE_V0_1.md`.

## Command-adapter protocol

The runtime is provider-neutral. Each adapter is configured as a command that:

1. receives one JSON request on stdin;
2. writes one JSON result on stdout;
3. exits non-zero on execution failure.

Example generic config:

```json
{
  "adapters": {
    "RND": {"command": ["your-rnd-command"]},
    "NETA": {"command": ["your-neta-command"]},
    "SCAFFOLD": {"command": ["your-scaffold-command"]}
  }
}
```

This keeps API keys/provider concerns outside the repository and allows local CLIs, hosted models or future service adapters to be swapped without changing the routing law.

## Live OpenAI adapters

A working Responses-API adapter is included:

- `runtime/calibration_loop/openai_resource_adapter.py` — Neta / Scaffold live resource bridge with provider/model provenance retained in `_adapter_meta`.
- `runtime/calibration_loop/openai_rnd_adapter.py` — strict R&D bridge that preserves the exact control-flow JSON shape required by the runner.
- `runtime/calibration_loop/openai-config.example.json` — ready command configuration.

No key is stored in the repository.

Minimum setup:

```bash
export OPENAI_API_KEY="..."
export OPENAI_MODEL="gpt-5.6-sol"
export OPENAI_REASONING_EFFORT="high"
```

Optional per-resource overrides:

```bash
export CALIBRATION_RND_MODEL="gpt-5.6-sol"
export CALIBRATION_NETA_MODEL="gpt-5.6-sol"
export CALIBRATION_SCAFFOLD_MODEL="gpt-5.6-sol"

export CALIBRATION_RND_REASONING_EFFORT="high"
export CALIBRATION_NETA_REASONING_EFFORT="high"
export CALIBRATION_SCAFFOLD_REASONING_EFFORT="high"
```

External web search is **off by default**. When a calibration diagnosis genuinely requires external research, enable it for R&D only:

```bash
export CALIBRATION_RND_WEB_SEARCH=1
```

Do not enable web search merely to increase source volume. The R&D telos remains decision-changing learning, not research accumulation.

### Reference task: CAL-ARCH-001

`fixtures/calibration-valid-task.json` is the first live transfer task and is retained as the reference example:

> What is the smallest evidence-backed architecture capability and evaluation contract worth building next?

It has already been executed manually. Its trace is
`runtime/calibration_loop/traces/CAL-ARCH-001-MANUAL-2026-09-05.md`, and it produced a material
decision change: do not define an autonomous architecture agent, first test whether a distinct
architecture-specific decision capability adds value beyond R&D + Scaffold + REPO/ENVIRONMENT
evidence. Current status of that question is in `docs/CANONICAL_STATE.md`.

Run it with:

```bash
python runtime/calibration_loop/run.py \
  fixtures/calibration-valid-task.json \
  --config runtime/calibration_loop/openai-config.example.json \
  --strict \
  --output runtime/calibration_loop/traces/CAL-ARCH-001.json
```

A successful run should perform R&D diagnosis, invoke only the resources whose deterministic triggers fire, preserve each independent output and provenance, and then return to R&D for synthesis and a learning record.

If R&D, Neta and Scaffold use the same underlying model family, their agreement is **not independent empirical triangulation**. Separate invocations can still reveal useful role-conditioned deltas, but the shared model lineage must remain visible.

## Runner modes

```bash
# Validate and show required invocations. Missing adapters become PENDING_RESOURCE.
python runtime/calibration_loop/run.py fixtures/calibration-valid-task.json

# End-to-end deterministic mock run used by CI.
python runtime/calibration_loop/run.py fixtures/calibration-valid-task.json --mock

# Real command adapters.
python runtime/calibration_loop/run.py task.json --config path/to/local-config.json --strict
```

`--strict` fails if a required adapter is not wired. Without it, the runner emits pending resource requests so partial automation remains explicit rather than fabricating outputs.

## Trace contract

Every run returns a single JSON envelope containing:

- exact task;
- R&D diagnosis or pending diagnosis request;
- routing decision and fired triggers;
- each resource request/result;
- R&D synthesis or pending synthesis request;
- `resource_deltas` when synthesis exists;
- a final state of `COMPLETE`, `PENDING_RESOURCE`, `AUTHORITY_STOP`, or `FAILED_EXECUTION`.

Use `--output <path>` to persist the envelope durably.

## Learning rule

The runner itself does not rewrite routing rules.

R&D may propose a routing amendment when repeated traces show a stable pattern, for example that Neta is materially useful in a certain trigger family or that an invocation repeatedly produces no decision delta. Any routing amendment must be tested against neighboring non-fire cases before promotion.
