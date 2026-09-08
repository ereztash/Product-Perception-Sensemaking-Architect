# Calibration Loop Runtime v0.2

Status: `IMPLEMENTATION_CANDIDATE`

Purpose: automate the recurring collaboration pattern in which R&D diagnoses how resources should be calibrated to a live telos, selectively invokes Neta and/or an external reasoning scaffold, and then synthesizes the deltas into the next move and a durable learning record.

This runtime is **not an Orchestrator Agent**. Routing is deterministic and inspectable. The only learned/judgment-bearing components are the peer/resource adapters it invokes.

## Core flow

```text
CALIBRATION TASK
      ↓
R&D DIAGNOSE
      ↓
EX-ANTE EXPECTED DELTA
      ↓
DETERMINISTIC ROUTING GATE
      ├── NETA      when discrimination/proxy/intervention triggers fire
      ├── SCAFFOLD  when broad/novel/architecture synthesis is requested
      └── AUTHORITY handoff when OWNER/REPO/ENVIRONMENT/FIELD owns the remainder
      ↓
PEER ANALYSIS (blind to expected_delta)
      ↓
R&D SYNTHESIZE
      ↓
OBSERVED DELTA + MATERIALITY CHECK
      ↓
TRACE + LEARNING RECORD
```

## Why routing is deterministic

The project does not yet have evidence that a learned orchestrator adds value. A deterministic gate provides the cheapest admissible coordination layer while preserving an auditable record of:

- why a resource was invoked;
- what R&D expected it could still change before invocation;
- what actually changed after invocation;
- whether the invocation was worth its cost;
- which routing rule should later be challenged.

A future orchestrator must be earned by repeated routing/dependency failures under this simpler system.

## Resource-delta accounting

v0.2 adds prospective resource accounting. The purpose is to distinguish a valid trigger from a useful invocation.

A resource can be correctly routed because its trigger family is present and still produce no material state change. Therefore `material=true/false` is not accepted as an unconstrained model judgment.

For every assessed resource, R&D must commit **before routing** to an `expected_delta` over six decision-state dimensions:

```json
{
  "decision": false,
  "action": false,
  "reversal": false,
  "evidence": false,
  "allocation": false,
  "distinction": false
}
```

The booleans mean only that the resource could still change that dimension if invoked now. They do not predict that it will.

After the peer returns, R&D must report `observed_delta` over the same six dimensions. Each value is either `null` or a concrete description of the state change attributable to that resource.

```json
{
  "decision": null,
  "action": "Changed the next move from BUILD to TEST.",
  "reversal": null,
  "evidence": null,
  "allocation": "Restricted Neta to two bounded passes instead of a standing workstream.",
  "distinction": "Separated proxy completion from position-specific judgment."
}
```

`material` is valid only when it equals whether at least one `observed_delta` field is non-null. The runtime rejects inconsistent labels.

This produces a reusable delta vocabulary:

- `ΔDecision`
- `ΔAction`
- `ΔReversal`
- `ΔEvidence`
- `ΔAllocation`
- `ΔDistinction`
- `Δ0` when all six are null

A distinction may therefore be material without changing the top-level decision, but only if it changes the reusable decision state rather than merely restating or elaborating an existing point.

### Independence guardrail

`expected_delta` is stored in the trace and in the R&D diagnosis, but it is **not sent to Neta or Scaffold**. The peer receives the task and fired focus only. This keeps the ex-ante expectation from becoming a self-fulfilling evaluation target.

R&D sees the expected delta again during synthesis and performs the expected-versus-observed comparison there.

### What this enables

Repeated real traces can support empirical routing metrics such as:

```text
Neta Yield = material Neta invocations / total Neta invocations
```

The same yield can later be decomposed by trigger family and delta type. Routing rules should not be changed from one case; repeated traces must show a stable pattern and neighboring non-fire cases must still be checked.

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

The v0.2 accounting layer does **not** change Neta's routing law. It makes the value of each invocation measurable before any future routing amendment is considered.

### SCAFFOLD

`SCAFFOLD` is an external broad-reasoning resource. It is useful for architecture alternatives, novel synthesis and expert-level reasoning that is cheaper to borrow than to internalize immediately.

R&D must learn from scaffold use rather than treating scaffold output as ground truth.

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
- `runtime/calibration_loop/openai_rnd_adapter.py` — strict R&D bridge that preserves the control-flow JSON shape required by the runner.
- `runtime/calibration_loop/openai-config.example.json` — ready command configuration.

No key is stored in the repository.

Minimum setup:

```bash
export OPENAI_API_KEY="..."
export OPENAI_MODEL="gpt-5.6-sol"
export OPENAI_REASONING_EFFORT="high"
```

External web search is **off by default**. When a calibration diagnosis genuinely requires external research, enable it for R&D only:

```bash
export CALIBRATION_RND_WEB_SEARCH=1
```

Do not enable web search merely to increase source volume. The R&D telos remains decision-changing learning, not research accumulation.

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

Every v0.2 run returns a single JSON envelope containing:

- exact task;
- R&D diagnosis or pending diagnosis request;
- routing decision and fired triggers;
- each peer request/result;
- `expected_delta` on every routed peer invocation;
- `observed_delta` and derived-compatible `material` after synthesis;
- R&D synthesis or pending synthesis request;
- `resource_deltas` when synthesis exists;
- a final state of `COMPLETE`, `PENDING_RESOURCE`, `AUTHORITY_STOP`, or `FAILED_EXECUTION`.

Use `--output <path>` to persist the envelope durably.

Existing v0.1 traces remain historical records; v0.2 does not retroactively infer deltas that were not prospectively captured.

## Learning rule

The runner itself does not rewrite routing rules.

R&D may propose a routing amendment when repeated traces show a stable pattern, for example that Neta is materially useful in a certain trigger family or that an invocation repeatedly produces `Δ0`. Any routing amendment must be tested against neighboring non-fire cases before promotion.
