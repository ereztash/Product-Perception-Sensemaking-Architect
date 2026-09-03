# AUTHORITY MAP — canonical artifacts and resolution authorities

This file answers two different questions and keeps them separate:

1. **Artifact authority** — which repository artifact is canonical for a question about Neta itself?
2. **Resolution authority** — which source can legitimately close a design/product claim?

## A. Artifact authority

| Question | Canonical authority | Not the authority |
|---|---|---|
| Why does Neta exist? | `docs/TELOS.md` | README slogans |
| What is the v0.2 assurance thesis? | `docs/NETA_ASSURANCE_THESIS.md` | chat history |
| How does Neta reason? | `docs/METHOD.md` | examples in fixtures |
| What do R0–R6, authorities and permissions mean? | `docs/REALITY_AUTHORITY_PERMISSION.md` | ad-hoc prose elsewhere |
| What was frozen as v0.1? | `docs/V0_1_FREEZE.md` + commit `b1dbfdda...` | current files rewritten later |
| What behavior does the frozen clean-model baseline prompt contain? | `prompts/SYSTEM.md` at the frozen blob hash | v0.2 docs pretending the prompt already changed |
| What finding shape is valid in v0.2? | `schemas/finding.schema.json` + `scripts/validate_finding.py` | prose examples |
| Does the finding gate actually reject epistemic violations? | CI + `scripts/check_contract.py` | presence of validator code |
| How is Neta evaluated? | `eval/RUBRIC.md` | prompt self-description |
| Which historical failures created current gates? | `docs/FAILURE_LINEAGE.md` | memory of prior chats |
| How completely was Lessons re-foundation transferred? | `docs/LESSONS_COVERAGE_AUDIT.md` | one lineage table |
| Where did design principles originate? | `docs/LINEAGE.md` | claims of universality |
| What has Neta learned about owner language? | `memory/owner-language.yaml` | permanent phrase→diagnosis mapping |
| Which Wave 1 questions/thresholds were preregistered? | `research/WAVE1_PREREGISTRATION.md` | v0.2 overlay |
| What candidate claims and original G/C/A/O/status exist? | `research/registers/claims.json` | `WAVE1_ASSURANCE_REVIEW.md` |
| How may research progress toward prompt eligibility? | `research/PROMOTION_PROTOCOL.md` | citation count |
| What did v0.2 change after source collection began? | `research/AMENDMENTS.md` | silent edits |
| How may Wave 1 be used under v0.2 without rewriting history? | `research/WAVE1_ASSURANCE_REVIEW.md` | retroactive threshold changes |
| Does research quarantine reject invalid promotion? | CI + `scripts/check_research_contract.py` | prose policy |

If two artifacts answer the same repository-governance question differently, the canonical artifact above wins and the disagreement is a defect.

## B. Resolution authority

Resolution authority belongs to a **claim**, not an entire conversation.

| Authority | May close | May not close merely by being strong |
|---|---|---|
| `OWNER` | intent, taste, strategic tradeoff, accepted risk | stranger behavior/value |
| `REPO` | code, geometry, integrated state, recorded instrumentation | production reality or human interpretation |
| `ENVIRONMENT` | deployed/runtime/config reality | user value/comprehension |
| `RESEARCH` | external mechanism/support within actual constructs and samples | whether mechanism is active here; product-specific value |
| `FIELD` | external notice, comprehension, preference, value, behavior actually observed | owner's strategic intent; unmeasured causality |

See `docs/REALITY_AUTHORITY_PERMISSION.md` for the full contract.

## Questions deliberately unresolved

| Question | Why unresolved | What would create authority |
|---|---|---|
| Does Neta improve Erez's design discrimination over time? | no prospective independent outcome measure | preregistered transfer checks over repeated sessions |
| Does the method work for another owner-builder? | no external operator replication | second-operator use under frozen method |
| Are the seven lenses complete? | working decomposition only | failure coverage showing stability or forcing revision |
| Which model/provider is best? | no controlled comparative runs | same fixtures across clean model surfaces |
| Should Neta have a UI? | no UI-specific need has earned build permission | repeated conversational failures whose cheapest repair is UI-specific |
| Which Wave 1 candidates should enter the prompt? | research candidates exist, but clean-model failures have not yet authorized prompt edits | baseline fixture runs + smallest-rule repair + neighbor controls |

## Research quarantine boundary

External literature, standards, examples and culture/context observations do not directly modify `prompts/SYSTEM.md`.

Wave 1 source collection has already begun and Evidence Pass 1 is merged. Therefore the v0.2 assurance re-foundation is a **prospective overlay**, not a retroactive rewrite of the preregistration or original research statuses.

## Non-collapse rules

- remembered phrase ≠ evidence by itself;
- fixture ≠ field behavior;
- deployment ≠ value;
- paper ≠ product-specific mechanism;
- promotion state ≠ probability of truth;
- G/C/A/O ≠ action permission;
- supported claim ≠ permission for every requested use;
- waiver ≠ upgraded evidence;
- executable feature ≠ justified feature;
- green gate never challenged ≠ demonstrated gate.
