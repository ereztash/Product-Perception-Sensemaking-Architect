# Public Release Readiness

Status: **PUBLIC SOURCE / OSS LICENSE NOT YET VERIFIED**

This document separates repository visibility from an open-source grant. The repository is public, but a root open-source license was not found during the 2026-09-29 portfolio audit. Do not describe this repository as open source until that boundary is resolved.

## Public value

This repository is useful to people building AI-assisted decision systems that need to preserve uncertainty rather than turn plausible model output into product truth.

The reusable core is not "two agents." It is the contract around them:

- raw signal -> competing mechanisms -> cheap discriminator -> intervention / defer / field;
- telos -> current state -> resource map -> bottleneck -> cheapest decision-changing learning;
- explicit resolution authorities;
- deterministic routing and stop states;
- claim lineage after falsification or narrowing;
- a strongest-composed-baseline gate before BUILD / ADAPT / INTERNALIZE.

## Evidence boundary

The repository already distinguishes discovery, executed traces, durable evidence, confirmatory evidence, and decision effect. Several active hypotheses remain unconfirmed. That boundary is part of the value and must remain visible in public descriptions.

## Stranger path

A new reader should be able to answer, in order:

1. What decision problem does this solve?
2. What is Neta responsible for?
3. What is R&D responsible for?
4. What is deterministic rather than agentic?
5. What would force the system to stop?
6. How can I run one trace and inspect the result?

Suggested path:
`README.md` -> `docs/CANONICAL_STATE.md` -> `docs/SHARED_EPISTEMIC_KERNEL.md` -> `runtime/calibration_loop/`.

## Before OSS spotlight

1. **License decision** — choose and add an explicit root license, or keep the repository source-visible and say so.
2. **One reproducible example** — one command, one fixture, one trace, one expected stop/success state.
3. **Contribution boundary** — state what kinds of changes are welcome and which epistemic/kernel rules require owner review.

## Public one-liner

> An evidence-bounded peer-agent system for turning uncertain signals into decision-relevant tests without letting agents manufacture authority.

## Do not claim

- that the architecture is universally validated;
- that Neta or R&D is independently proven to improve decisions;
- that more agents are better;
- that an executed trace is field evidence.
