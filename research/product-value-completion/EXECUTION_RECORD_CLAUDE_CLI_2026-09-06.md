# CAL-PRODUCT-VALUE-001 — live execution record, Claude CLI transport

Status: `COMPLETE`
Report class: **WORK QA / EXECUTION NOTES**. No Neta, R&D or Scaffold conclusion is authored in this file. The repository output lives in the trace.
Date: 2026-09-06

Preserved alongside, not replacing:

- `EXECUTION_CHECKPOINT_2026-09-06.md` — pass 1, `FAILED_EXECUTION`
- `EXECUTION_CHECKPOINT_PASS2_2026-09-06.md` — pass 2, `FAILED_EXECUTION`

## Why the transport changed

Passes 1 and 2 both stopped at `FAILED_EXECUTION` because `OPENAI_API_KEY` is absent from the Actions environment and from this execution environment. The owner directed that the run proceed directly rather than through the GitHub Actions/OpenAI secret path.

`runtime/calibration_loop/README.md` specifies a provider-neutral command-adapter protocol: an adapter is any command that reads one JSON request on stdin, writes one JSON result on stdout, and exits non-zero on failure, so that providers can be swapped **without changing the routing law**. This pass exercises exactly that affordance.

## What actually executed

`runtime/calibration_loop/run.py` drove the run in `--strict` mode. Nothing was authored by hand.

```text
R&D DIAGNOSE  →  routing.py  →  NETA + SCAFFOLD (parallel)  →  R&D SYNTHESIZE  →  COMPLETE
```

| Phase | Resource | State |
|---|---|---|
| DIAGNOSE | RND | COMPLETE |
| ANALYZE | NETA | COMPLETE |
| ANALYZE | SCAFFOLD | COMPLETE |
| SYNTHESIZE | RND | COMPLETE |

- Trace: `runtime/calibration_loop/traces/CAL-PRODUCT-VALUE-001-claude-cli.json`
- Provenance sidecar: `runtime/calibration_loop/traces/CAL-PRODUCT-VALUE-001-claude-cli-provenance.jsonl`
- Task: `fixtures/calibration-product-value-completion-2026-09-06.json`
- Config: `runtime/calibration_loop/claude-cli-config.json`
- Adapter: `runtime/calibration_loop/claude_cli_adapter.py`
- Executed at commit: `a108743` working tree, plus the adapter added in this pass.

### Routing verdict, produced by `routing.py` from the live diagnosis

```text
resources           = NETA, SCAFFOLD
NETA fired on       = signal_interpretation_ambiguity, multiple_plausible_mechanisms,
                      proxy_substitution_risk, research_to_intervention_transition
SCAFFOLD fired on   = broad_reasoning_needed, novel_synthesis_needed
authority handoffs  = OWNER, REPO, ENVIRONMENT, FIELD
needs FALSE         = architecture_alternatives_needed, external_research_needed
```

Neta was **not** forced. The diagnosis set four Neta triggers true on its own and the deterministic gate routed accordingly. `architecture_alternatives_needed` and `external_research_needed` came back false, so no architecture lane and no further external research were opened.

The four authority handoffs are **recorded routing outputs**, not executed handoffs. This runtime records them; it does not perform them. `COMPLETE` coexists with four unresolved authorities, and none of them may be read as an OWNER decision or a FIELD outcome.

## Provenance, stated plainly

| Call | Served model | Turns | Stop reason | Cost USD |
|---|---|---|---|---|
| RND DIAGNOSE | `claude-opus-5` | 1 | end_turn | 0.1511 |
| SCAFFOLD ANALYZE | `claude-opus-5` | 1 | end_turn | 0.4471 |
| NETA ANALYZE | `claude-opus-5` | 1 | end_turn | 0.5209 |
| RND SYNTHESIZE | `claude-opus-5` | 1 | end_turn | 0.9983 |
| | | | **total** | **2.1174** |

**Material deviation from the prepared configuration.** The prepared run specified `gpt-5.6-sol` through the OpenAI adapter. This run reached `claude-opus-5` through the Claude CLI. The routing law, the frozen prompts, the bridge contracts, the semantic validators and the trace contract are byte-identical to the canonical ones; only the transport differs. The deviation is recorded here rather than smoothed over, because model identity is part of the evidence.

**Independence.** All four calls share one model lineage. Convergence between R&D, Neta and Scaffold is role-conditioned execution, not independent triangulation, and contributes zero confirmatory N. The synthesis states this itself and does not claim otherwise.

**Second-order caveat, specific to this pass.** The session that operated the runtime is of the same lineage as the resources it invoked. Work QA performed here is therefore not an independent check of the resource outputs either. It is a check that the runtime executed as specified.

## Contamination controls on the adapter

- System prompt is loaded by the canonical `prompt_for()` from `openai_resource_adapter`, so `prompts/SYSTEM.md`, `prompts/RND_AGENT_V0_2_CANDIDATE.md` and `prompts/SCAFFOLD_RESOURCE_V0_1.md` are used verbatim with the same bridge contract.
- Input is the runner's serialized request and nothing else. No conversation context was passed.
- Each call runs in a fresh subprocess in a temporary working directory, so the repository `CLAUDE.md` and any project context are not loaded.
- `--restricted`, `--strict-mcp-config` and an explicit deny list remove tool access, so no resource could read the repository or the network out of band.
- Output is parsed by the canonical `parse_json_object()` and checked by the canonical `validate_semantic_shape()`. R&D `DIAGNOSE` is additionally checked by `run.py::validate_diagnosis`, which enforces exact keys.

Because `validate_diagnosis` forbids extra keys, R&D provenance cannot ride inside the semantic object. It is written to the sidecar instead. This is the same asymmetry pass 1 flagged, handled without weakening the strict shape. Neta and Scaffold retain `_adapter_meta` inline.

## What this pass does not establish

- No competitor was trialled.
- No external person read anything.
- No FIELD claim was closed.
- `CONFIRMATORY_N` remains 0.
- No status, prompt, telos, routing rule, schema or agent boundary was changed.
- Nothing was promoted. The roadmap in the trace is R&D synthesis output under the shared kernel, not an earned finding.

The synthesis returned `CONTINUE`, `routing_amendment_proposed: null`, and five routing-learning records each marked `sufficient_to_amend_routing: false`. The runtime did not self-modify its routing law, which is the behaviour the contract requires.
