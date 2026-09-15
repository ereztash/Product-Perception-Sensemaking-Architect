# R&D Agent Amendment v0.2.1 — composed baseline + claim lineage

Status: `CANDIDATE_AMENDMENT_NOT_PROMOTED`

Pre-change baseline: `prompts/RND_AGENT_V0_2_PRE_AMENDMENT_BASELINE.md`.
Runtime compatibility path: `prompts/RND_AGENT_V0_2_CANDIDATE.md`.
Candidate implementation: `prompts/RND_AGENT_V0_2_1_CANDIDATE.md`.

## Why this amendment exists

Recent discovery work repeatedly produced the same failure risk:

1. a candidate capability appears unique relative to one obvious alternative;
2. broader recovery reveals that several existing methods/resources can be composed to supply most or all of the claimed function;
3. the original claim is narrowed into a residual hypothesis;
4. without explicit lineage, the residual can be mistaken for confirmation of the parent claim.

The observed sequence motivating this amendment was discovery-only reasoning around human/AI work allocation and related process/decision architecture. It is **not** confirmatory evidence for this amendment.

## Hidden judgments proposed

### A1 — strongest composed baseline

When a build/adapt/internalize decision depends on unique functional value, the relevant comparator is the strongest plausible composition of already available resources/capabilities, not merely the nearest single competitor.

Failure prevented:

> `NEW_CAPABILITY > SINGLE_BASELINE` is treated as evidence of uniqueness even though `COMPOSED_EXISTING_BASELINE` already supplies the function.

Neighbor where A1 must not overfire:

> Composition itself creates material cost, latency, coordination failure, UX burden, reliability loss or authority fragmentation. In that case an integrated capability may still add value, but the live claim is integration value rather than primitive uniqueness.

### A2 — claim mutation creates a new claim

When a parent claim is falsified, absorbed by baseline or materially narrowed, a surviving residual must receive a new claim identity and new evidence burden.

Failure prevented:

> Repeated narrowing lets a moving claim appear continuously supported even though each stronger parent claim failed.

Neighbor where A2 must not overfire:

> A wording change that does not alter construct, scope, requested use, decision implication or falsifier remains the same claim and may be edited without creating artificial lineage noise.

## Evidence boundary

Current support for adding these as candidate behaviors is:

- `DISCOVERY_ONLY`;
- same-conversation reasoning;
- no frozen baseline-vs-challenger run;
- no unseen HOLDOUT;
- no independent adjudication.

Therefore this amendment does **not** claim promotion under `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`.

## Required evaluation before promotion

A promotion attempt should include at minimum:

1. frozen `v0.2` baseline vs `v0.2.1` challenger;
2. natural cases where capability/uniqueness claims matter to BUILD/ADAPT/INTERNALIZE decisions;
3. at least one case where a composed baseline defeats apparent uniqueness;
4. at least one neighbor where composition cost makes integration genuinely valuable;
5. at least one case where falsification yields a narrower residual claim;
6. at least one wording-only revision that should **not** create a new claim;
7. blinded adjudication of whether the amendment changed `ΔDecision`, `ΔAction`, `ΔEvidence`, `ΔAllocation` or `ΔDistinction` without regressions in cost discipline or authority routing;
8. unseen HOLDOUT after the repair is frozen.

Passing discovery examples used to design this amendment cannot count as HOLDOUT evidence.

## Promotion criterion

Promote only if v0.2.1 shows a repeated surviving advantage on the relevant failure family and no material regression across the existing R&D dimensions.

Until then:

- v0.2 remains the retained comparator;
- v0.2.1 is an implementation candidate for explicit testing only;
- no shared-kernel rule changes are implied;
- no Neta rule changes are implied.
