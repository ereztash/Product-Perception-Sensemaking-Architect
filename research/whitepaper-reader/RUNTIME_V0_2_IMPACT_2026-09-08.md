# Calibration Loop v0.2 impact on this branch

Report class: **WORK QA / EXECUTION NOTES**.
Date: 2026-09-08
Merged: `origin/main` at `74fc4af`, "Add prospective resource-delta accounting to Calibration Loop".

## What changed on main

The runtime moved from v0.1 to v0.2. `run.py` now:

- requires `expected_delta` on every `resource_assessment` entry — an ex-ante boolean commitment across `decision`, `action`, `reversal`, `evidence`, `allocation`, `distinction`;
- adds `validate_synthesis`, which enforces exact synthesis fields, one `observed_delta` per routed resource in routed order, and that `material` equals whether any `observed_delta` dimension is non-null;
- annotates each peer invocation in the trace with its expected and observed delta;
- stamps traces `runtime_version: "0.2"`.

The bridge contracts in `openai_resource_adapter.py` were rewritten to match, and they explicitly withhold R&D's ex-ante `expected_delta` from the peers so the later materiality comparison stays prospective rather than self-fulfilling.

## Impact on the adapter this branch added

**None required.** `claude_cli_adapter.py` is transport-only: it calls the canonical `prompt_for()`, which calls the canonical `bridge_contract()`, and it validates with the canonical `validate_semantic_shape()`. It therefore picked up the v0.2 contract without a line of change. That was the design property the transport-only split was for, and this is the first evidence it holds under a real contract change.

Verified on the merge commit:

| Check | Result |
|---|---|
| `check_contract`, `check_research_contract`, `check_rnd_contract` | PASS |
| `check_canonical_state`, `check_calibration_loop`, `check_live_adapters` | PASS |
| `claude_cli_adapter.py` compiles | PASS |
| `bridge_contract('RND','DIAGNOSE')` carries `expected_delta` | PASS |
| `bridge_contract('RND','SYNTHESIZE')` carries `observed_delta` | PASS |
| `--mock` end to end on all three branch tasks | PASS |

## The caveat that must travel with the three traces

`CAL-PRODUCT-VALUE-001`, `CAL-RESEARCH-ALLOCATION-001` and `CAL-WHITEPAPER-READER-001` were executed on **2026-09-06 under v0.1**. They carry `runtime_version: "0.1"` and contain no `expected_delta` and no `observed_delta`.

They are historical records under the superseded contract. They are **not** v0.2-conforming output and must not be read as if they were. Their `resource_deltas` carry `material` as a judgement stated in prose, without the six-dimension derivation v0.2 now requires and machine-checks.

They are retained unchanged rather than re-run or back-filled. Back-filling `observed_delta` onto a synthesis produced before the dimensions existed would be constructing evidence after the fact, which is the failure the freeze discipline exists to prevent.

## What would change that

Re-running any of the three tasks on v0.2 would produce a genuinely v0.2-conforming trace with ex-ante commitments and machine-checked materiality. That is a fresh run, not a repair of the old one, and both would be retained. It is not done here because no one asked for it and it costs a paid run.
