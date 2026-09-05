# CAL-CHESS-ERROR-001 — Research task

Status: `LIVE_RESEARCH_TASK`

## Owner telos

Build the knowledge base required to design a system that adapts chess-error diagnosis and learning guidance to the player's actual skill/rating context, rather than applying one universal engine-error interpretation to everyone.

## Starting state

- Neta exists as a product/design sensemaking peer.
- R&D v0.2 candidate exists as a resource↔telos calibration peer.
- The Calibration Loop exists, but live model adapters are not being used in this run.
- This run is manual role-separated execution using the canonical prompts/roles.
- The current system does not yet have a validated cross-lingual, cross-source knowledge spine for rating-conditioned chess errors.

## Decision blocked

What research program should be run, and what evidence should be collected, before we can responsibly design rating-conditioned chess error classification/adaptation?

## Constraints

- Do not assume centipawn loss alone defines a useful error.
- Do not assume rating alone defines a player.
- Do not treat language/country as an evidence family by itself.
- Preserve source lineage and distinguish books, coaching doctrine, empirical studies, datasets, OSS, engines, and field evidence.
- Research must be allowed to conclude that some categories or source families are not useful.

## Authority

- OWNER: product telos/tradeoffs.
- RESEARCH: external evidence, construct validity, prior methods.
- REPO: what the current chess product/code actually does.
- ENVIRONMENT: runtime/model/engine behavior.
- FIELD: what players actually learn/change from feedback.

## Required process

1. R&D DIAGNOSE independently.
2. Neta challenge independently from the same task.
3. R&D SYNTHESIZE a research plan from the deltas.
4. Execute only the plan R&D earns.
5. Persist sources, claims, contradictions, scope, and next uncertainty.

Agreement between manual role passes is not independent triangulation because they share one model/session lineage.
