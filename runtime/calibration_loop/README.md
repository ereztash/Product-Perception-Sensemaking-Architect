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

### Neta

Neta is invoked only when at least one Neta trigger fires:

- signal→interpretation ambiguity;
- multiple plausible mechanisms;
- proxy-substitution risk;
- research/evidence is about to become an intervention/build decision.

Neta is a peer resource, not a subordinate R&D worker and not a mandatory ceremony.

### SCAFFOLD

`SCAFFOLD` is an external broad-reasoning resource (currently represented by ChatGPT in the development process). It is useful for architecture alternatives, novel synthesis and expert-level reasoning that is cheaper to borrow than to internalize immediately.

R&D must learn from scaffold use rather than treating scaffold output as ground truth.

## Command-adapter protocol

The runtime is provider-neutral. Each adapter is configured as a command that:

1. receives one JSON request on stdin;
2. writes one JSON result on stdout;
3. exits non-zero on execution failure.

Example config:

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
