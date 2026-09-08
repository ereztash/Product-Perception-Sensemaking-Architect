# Neta Yield Batch 001 — Calibration Loop v0.2

Status: `EXPERIMENTAL_EVIDENCE`
Date: 2026-09-08

## Decision

**KEEP the current deterministic routing unchanged.** The first v0.2 batch supports the new resource-delta accounting, but it does not yet justify a routing amendment.

## Sample

- Real calibration tasks: **6**
- Final `FAILED_EXECUTION`: **0**
- Final states: **3 COMPLETE, 3 AUTHORITY_STOP**
- Neta trigger fired in: **6/6** cases
- Neta actually routed in: **3/6** cases
- Material Neta invocations: **3/3**
- Raw Neta Yield: **100% (n=3)**

This 100% is **not** a routing-quality estimate. The routed sample is only three cases and every routed case fired the same four-trigger bundle.

## Observed Neta delta by dimension

| Dimension | Material cases |
|---|---:|
| ΔDecision | 2/3 |
| ΔAction | 2/3 |
| ΔReversal | 0/3 |
| ΔEvidence | 1/3 |
| ΔAllocation | 1/3 |
| ΔDistinction | 3/3 |

The strongest repeated Neta contribution in this batch is **ΔDistinction (3/3)**. Decision/action changes appeared in 2/3; no reversal-condition delta was observed.

## Case-level accounting

| Task | Final state | Neta |
|---|---|---|
| `CAL-ARCH-SOLARCH-001` | `COMPLETE` | ROUTED; material=true; ΔDecision + ΔDistinction |
| `CAL-ARCH-SYSDESIGN-001` | `COMPLETE` | ROUTED; material=true; ΔDecision + ΔAction + ΔEvidence + ΔAllocation + ΔDistinction |
| `CAL-LICHESS-PREMOVE-OWNERSHIP-2026-09-07` | `COMPLETE` | ROUTED; material=true; ΔAction + ΔDistinction |
| `DR-PREFLIGHT-WHITEPAPER-001` | `AUTHORITY_STOP` | TRIGGERED, NOT ROUTED — task allows RND only |
| `RND-LICHESS-WTP-BELIEF-001` | `AUTHORITY_STOP` | TRIGGERED, NOT ROUTED — task allows RND only |
| `RND-SHAKED-CLOSE-OS-2026-09-07` | `AUTHORITY_STOP` | TRIGGERED, NOT ROUTED — task allows RND only |

## Important control

Three cases fired one or more Neta triggers but did not route Neta because their task resource boundary did not allow Neta. They are **not Δ0 cases** and do not belong in the Neta Yield denominator.

This is evidence that `trigger fired` and `resource invoked` are distinct states in the runtime.

## Execution provenance

- Canonical v0.2 runtime base: `74fc4af509965497a7440d9521fc3717b2809f50`
- Initial batch run: `34219245290` at `54c7f4877c4564825ffa0059ad72b14c768e61e5`
- Zero-peer retry run: `34219483110` at `9ef5c8b4332db689d699988664cd70043b2b883d`
- Execution adapter: GitHub Copilot CLI best-effort bridge
- Model: provider-default; exact lineage unknown
- Same-provider role-conditioned agreement is **not independent triangulation**.

Two zero-peer cases initially failed because Copilot emitted an illegal `RND` entry in `resource_deltas` when `routing.resources=[]`. The canonical runtime rejected both. A single retry followed after tightening only the fallback bridge to enforce the already-existing v0.2 invariant. No task, routing rule, canonical prompt or canonical runtime contract was changed. Both retries completed with `AUTHORITY_STOP` and `resource_deltas=[]`.

## What this batch can and cannot tell us

Supported:

- v0.2 can distinguish trigger firing, actual invocation, and observed material delta.
- In the three Neta invocations sampled, Neta produced a non-null material delta every time.
- Neta's repeated contribution was primarily discrimination/refinement, not reversal.

Not supported yet:

- that Neta has 100% yield generally;
- that any individual Neta trigger predicts value;
- that the four-trigger bundle is necessary;
- that routing should be narrowed or expanded;
- that same-provider outputs validate the underlying claims.

## Next discriminator

Run a second, deliberately orthogonal batch containing:

1. single-trigger or two-trigger Neta cases;
2. neighboring cases where Neta is allowed but expected to produce `Δ0`;
3. cases where only `proxy_substitution_risk` fires;
4. cases where only `signal_interpretation_ambiguity` / `multiple_plausible_mechanisms` fires;
5. at least one case where R&D predicts Neta can only add `ΔDistinction`, not `ΔDecision`.

Only after those cases should trigger-level yield or a routing amendment be considered.
