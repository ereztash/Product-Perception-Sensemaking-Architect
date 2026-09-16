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

## Addendum 2026-09-08: a second adapter, built independently

A parallel session added `runtime/calibration_loop/copilot_resource_adapter_v02.py`
(commit `a6aec47`) and drove it from
`.github/workflows/rnd-self-triangulation-anti-challenges.yml` (`3b51465`) on branch
`research/rnd-self-triangulation-anti-challenges-2026-09-08`. Four `--strict` cases ran in
parallel in run [34224341388]; all reached `final_state: COMPLETE` with `failure: null`.
Neither the adapter nor `copilot-config-v02.best-effort.json` is on `main`.

It imports `prompt_for` and `validate_semantic_shape` from `openai_resource_adapter`, the same
two canonical entry points this branch's adapter uses. Two adapters, three providers, written by
sessions that did not coordinate, against one unchanged routing law.

**What that is evidence for, and what it is not.**

It is evidence that the provider-neutral command-adapter protocol is implementable by someone who
did not write it. That is a different property from the one claimed above. The claim above is that
a transport-only adapter survives a contract change without edits; the Copilot adapter was written
*after* v0.2 and has never crossed a contract change, so it cannot be evidence for it. The two
should not be pooled.

It is not independent triangulation and adds nothing to `CONFIRMATORY_N`, which stays 0. The
adapter's own provenance block records `model: "provider-default"` and
`exact_model_lineage: "unknown"`, and states that its runs are developmental evidence only until
adjudicated by a known different lineage. That limit is correctly stated at the source and is
carried here unchanged rather than relaxed.

The two adapters also differ in transport-purity, which matters to the property being claimed. The
Copilot adapter defines `exact_runtime_bridge()`, appending a runner invariant to the RND
`SYNTHESIZE` prompt that constrains `resource_deltas` to the routed resources in routed order. Its
prompt is therefore canonical-plus-one-injection, not canonical alone. This branch's adapter
required no such injection. Whether that injection is compensating for a prompt-following weakness
in the provider or for an under-specification in the bridge contract is undetermined here, and is
the parallel session's question, not this branch's.

**Effect on the credential blocker.** This route used no stored secret: `permissions:
copilot-requests: write` plus the runner's own ephemeral `github.token`. That removes the reason
five R&D tasks sat unexecuted, and it means the two remedies this branch offered the owner — add
`OPENAI_API_KEY`, or run them through `claude_cli_adapter.py` — were not the only two.

It does **not** answer `O5`. `O5` asks whether a non-Anthropic credential is inside existing
authorization or is an OWNER spend. Copilot requests draw on the owner's Copilot entitlement, so
the route substitutes one spend class for another rather than eliminating spend. It is answered for
*secret handling* and open for *spend authority*. `O5` stays OWNER-held.

No status, prompt, telos, routing rule, schema or agent boundary changed by recording this.
