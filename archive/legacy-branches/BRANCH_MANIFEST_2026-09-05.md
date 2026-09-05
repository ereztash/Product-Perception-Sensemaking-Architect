# Legacy Branch Manifest — 2026-09-05

Status: `HISTORICAL_LINEAGE_ONLY`

`main` is the only canonical branch. This manifest records the branch tips that existed before consolidation so historical derivation remains inspectable without treating those branches as current truth.

| Branch | Pre-cleanup tip | Audit disposition |
|---|---|---|
| `neta/design-research-spine-v0.1` | `5ed5f2222a6c31b56756c223cb54c57d9b33e0d7` | strict ancestor of main; no unique commits |
| `neta/github-benchmark-v1` | `f5c8a17320864b310fd202f9f29768f6e3ceb60a` | strict ancestor of main; no unique commits |
| `neta/hebrew-observatory` | `c91275e655f7d24c178a7ef6187dca2b96d6901c` | strict ancestor of main; no unique commits |
| `neta/hebrew-signal-fidelity` | `687cff56e8e15efa5bc28e450850b2e7c44888b6` | strict ancestor of main; no unique commits |
| `neta/oss-observatory` | `b0d94d8ba15a63d3396ee14666e5a6549c6df75e` | strict ancestor of main; no unique commits |
| `refoundation/neta-assurance-v0.2` | `e050cded5baac5313a44ab0dd60345c1b6e36132` | strict ancestor of main; no unique commits |
| `research/wave1-triangulation` | `873f2abc2fb4084b172278bb91a117b3e69417a5` | strict ancestor of main; no unique commits |
| `neta/v0.1-agent-contract` | `5b27dd6b82aa323f595640e1baf21f5cd7032553` | historically diverged; core files exist in later/superseding forms on main; retain SHA as lineage, not authority |
| `research/wave1-evidence-pass1` | `27ffa95066b015424a48093a007f364388c82748` | historically diverged; three unique research docs copied into this archive before normalization; old validator not promoted |
| `rnd/calibration-loop-v0.1` | `f658f416918c239dfdf7290d06890b24d1b03333` | fast-forward merged to main; historical work ref only |

## Temporary refs created during repository cleanup

The connected GitHub tool available during this pass could create and move branch refs but could not delete them. A few temporary organization/archive refs were therefore created while determining the safest cleanup path. They carry **no independent authority** and should be considered deletable UI clutter once their tip equals `main`:

- `repo/organization-pass`
- `archive/legacy-snapshots`
- `repo/organization-pass-2`
- `archive/legacy-docs-2026-09-05`
- `repo/organization-final`
- `repo/organization-canonical`
- `repo/organization-canonical-v2`
- `repo/organization-work`
- `repo/organization-single-source`

No future workflow should depend on any of these names.

## What was preserved from `research/wave1-evidence-pass1`

Exact historical content is copied under:

- `archive/legacy-branches/research-wave1-evidence-pass1/PROMPT_GAP_AUDIT.md`
- `archive/legacy-branches/research-wave1-evidence-pass1/RECURSION_LOG.md`
- `archive/legacy-branches/research-wave1-evidence-pass1/WAVE1_RESULTS_PASS1.md`

The branch-specific version of `scripts/check_research_contract.py` was not promoted because current `main` contains a later contract architecture. Its historical behavior remains attributable to the branch tip SHA above.

## Authority rule

A historical branch or archived document may explain lineage. It may not override a current canonical contract, prompt, evaluation gate or runtime on `main`.
