# R&D Agent Research Lane

Status: `ACTIVE · DISCOVERY_AND_CONFIRMATION_SEPARATED`

This directory contains research about the peer R&D Agent. It is separate from Neta's Wave 1 research lane and cannot directly modify Neta behavior.

## Discovery is not confirmation

```text
Discovery evidence          ≠  confirmatory evidence.
Historical contamination    ≠  unseen validation.
Same-model adjudication     ≠  independent confirmation.
```

Every artifact in this directory belongs to exactly one of three streams. Do not read across the boundary.

### 1. Discovery

Generates and sharpens hypotheses. May inspect anything already in the repository.

Contributes **zero** countable confirmation. A discovery point estimate is never a scope boundary, a capability claim or a promotion.

### 2. Confirmation

Tests a frozen hypothesis against cases admitted **after** the freeze under the frozen comparator and adjudication rules.

A case counts only if it satisfies every admission condition in `scope-discovery/RND_SCOPE_CONFIRMATION_STREAM_V0_2.md`. A case that fails any condition is directional evidence, not confirmation.

### 3. External directional evidence

Real-world outcome evidence collected outside the frozen protocol. It can falsify, expose a coding error or motivate the next hypothesis version. It cannot raise a confirmation count.

## Current confirmation state

```text
CONFIRMATORY_N = 0
```

No region of the v0.2 scope map has left `UNKNOWN`.

The blocking condition is recorded in `scope-discovery/RND_SCOPE_CONFIRMATION_STREAM_V0_2.md`: the environment exposes no independent model-lineage or qualified human adjudication channel, and same-model self-adjudication is explicitly disallowed from supporting the claim.

This count may not increase without an admitted case, a blinded comparator, independent adjudication and preserved provenance.

## Lane map

```text
research/rnd-agent/
  telos/            R&D telos formulation, narrow-vs-broad benchmark, peer review
  scope-discovery/  where R&D's marginal value concentrates
    external-tests/ post-freeze external outcome batches (directional only)
  epistemology/     epistemology / applied epistemology / VOI transfer tests
  OSS_*.md          targeted OSS transfer lineage, closed at saturation
```

### `telos/`

Holds the R&D telos work, including the narrow-vs-broad telos benchmark and the R&D/Neta peer review of the narrowed formulation.

The broad v0.2 resource↔telos formulation in `../../prompts/RND_AGENT_V0_2_CANDIDATE.md` remains the canonical implementation candidate. Nothing in this lane has promoted a narrower telos into the prompt.

### `scope-discovery/`

Holds the scope program in explicit order:

- `RND_SCOPE_DISCOVERY_PROGRAM_V0_1.md` — discovery protocol and sequential stopping rule;
- `RND_SELF_SCOPE_DISCOVERY_*` and `RND_SCOPE_DISCOVERY_BATCH_REPORT_2026-09-06.md` — discovery artifacts;
- `NETA_SCOPE_DECOMPOSITION_REVIEW_2026-09-06.md` — peer review of the decomposition;
- `RND_SCOPE_MAP_V0_2_FROZEN_FOR_CONFIRMATION.md` — the frozen confirmation hypothesis;
- `RND_SCOPE_CONFIRMATION_STREAM_V0_2.md` — the confirmation stream and its counts;
- `external-tests/` — external directional evidence collected after the freeze.

`external-tests/` sits under `scope-discovery/` because those batches test this scope hypothesis specifically. The frozen confirmation stream references them by that relative path.

### `epistemology/`

Controlled transfer tests of epistemology, applied epistemology and value-of-information framings against the current R&D baseline.

Result recorded in `../agent-discovery/AGENT_DISCOVERY_CLOSEOUT_2026-09-06.md`: these improved vocabulary and contract clarity but did not establish a unique next-move capability beyond current R&D. They are R&D theory and an evaluation lens, not a new capability.

## Contamination register

Everything inspected while designing the v0.2 scope hypothesis is discovery-contaminated for that hypothesis. The authoritative list is in `scope-discovery/RND_SCOPE_MAP_V0_2_FROZEN_FOR_CONFIRMATION.md`. It includes the Yishumi prompt bank, QD shadow-gate cases, the Neta Hebrew TRAIN seed, R&D TRAIN controls, the Architecture historical benchmark as used in discovery, and the epistemology and VOI authored tests.

Contaminated artifacts may justify a hypothesis. They may never confirm it.

## Canonical R&D behavior and eval references

- charter: `../RND_AGENT_CHARTER_V0_1.md`
- frozen baseline prompt: `../../prompts/RND_AGENT_V0_1.md`
- candidate v0.2 prompt: `../../prompts/RND_AGENT_V0_2_CANDIDATE.md`
- v0.2 telos refoundation: `../RND_AGENT_TELOS_REFOUNDATION_V0_2.md`
- baseline freeze: `../../eval/rnd-agent/BASELINE_FREEZE_V0_1.md`
- runtime schema: `../../schemas/rnd-research-task.schema.json`
- scope case schemas: `../../schemas/rnd-scope-case.schema.json`, `../../schemas/rnd-scope-case-v0.2.schema.json`
- semantic validator: `../../scripts/validate_rnd_task.py`
- eval protocol: `../../eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`
- OSS-derived eval amendment: `../../eval/rnd-agent/EVAL_AMENDMENT_2026-09-05_OSS.md`

R&D promotion is governed by the R&D eval protocol, not by Neta's `../PROMOTION_PROTOCOL.md`.

## Targeted OSS transfer

- `OSS_TARGETED_TRANSFER_2026-09-05.md` — architecture extraction and boundaries.
- `OSS_TRANSFER_CLOSEOUT_2026-09-05.md` — saturation decision and next authorized sequence.
- `../../eval/rnd-agent/OSS_CHALLENGER_QUEUE_V0_1.md` — visible/adversarial challengers derived after baseline freeze.

The targeted OSS lane is closed at architecture saturation. The sample covered different roles rather than maximizing repository count: research/development role split, tree/graph exploration, phase-specialized multi-agent workflow, scientific retrieval, benchmark reproducibility, stochastic long-horizon evaluation, report/citation evaluation, experience memory and cross-branch search, self-evolving research organizations.

The strongest residuals are provenance/verification and dependency-safe continuity, not a demonstrated need for more agents.

## Next unit of progress

An admissible confirmation case, or a frozen-baseline failure that changes a named challenger, boundary, fixture or repair decision.

Do not add another source, benchmark or lane to raise certainty aesthetics. If the next material uncertainty belongs to another peer or authority, route it there.
