# Epistemology capability gap map — Pass 1

Status: `REPO_VS_EXTERNAL_CONCEPT_MAPPING · NOT_PROMOTION_EVIDENCE`
Date: 2026-09-06

Legend:
- `ALREADY_PRESENT` — current repo already contains the decision distinction strongly enough that terminology transfer alone is not a capability gain.
- `PARTIAL` — neighboring mechanism exists but an explicit hidden judgment may still be missing.
- `ABSENT` — no clear current representation found; still requires decision-delta testing before transfer.

| Capability family | Status | Current repo coverage | Residual question |
|---|---|---|---|
| Evidence ↔ justification | PARTIAL | Evidence objects support/challenge/bound claims; authority/requested-use/permission/reversal are explicit. | Does R&D distinguish `evidence available` from `claim actually justified by / based on this evidence` strongly enough to prevent post-hoc support? |
| Epistemic basing | ABSENT/PARTIAL | Provenance and decision-before/after exist, but no explicit rule that evidence cited after a conclusion need not be the basis that justified it. | Would a `BASING_LINEAGE` distinction materially change claim disposition? |
| Higher-order evidence | PARTIAL | Runnability, provenance, shared lineage and resource-delta learning exist; same-model agreement is not independent triangulation. | Is evidence about the *reliability of the inferential process itself* allowed to defeat/downweight first-order support generically? |
| Reliabilism / process reliability | PARTIAL | Resource assessment asks whether invoking a resource has helped before; repeated deltas can change future routing. | Should historical process reliability alter evidential weight, not merely routing choice? |
| Testimony / expert disagreement | PARTIAL | Authority map and peer-conflict classes exist; independent lineage protected. | No explicit `peer-ness / expertise / access / disagreement-as-higher-order-evidence` rule. |
| Underdetermination | ALREADY_PRESENT/PARTIAL | Neta explicitly carries competing mechanisms and discriminators; R&D carries falsification and controls. | R&D may still need a generic guard against treating one supported explanation as uniquely determined. |
| Abduction / IBE candidate-set completeness | PARTIAL | Competing alternatives exist in neighboring methods, but no explicit `best among considered ≠ likely true if candidate set is poor` rule. | Does candidate-set incompleteness cause a clean R&D failure? |
| Epistemic / inductive risk | PARTIAL | Reversibility, requested use, permission, owner risk/authority and cost discipline exist. | Evidence threshold is not explicitly conditioned on asymmetric error consequences. |
| Bayesian epistemology / credence updating | ABSENT as a formal mechanism | Repo intentionally avoids fake precision and uses bounded evidence states. | Can legitimate probabilistic updating improve decisions without importing pseudo-precision? |
| Epistemic utility / value of knowledge | ALREADY_PRESENT at operational level | Shared unit is material uncertainty removed from a live decision; R&D stops when more learning cannot change decision. | Formal epistemic utility may optimize accuracy rather than practical decision value, so transfer could misalign. |
| Decision-analysis Value of Information | PARTIAL but highly aligned | `cheapest decision-changing learning` is already core, but no explicit EVPI/EVSI-style comparison across uncertain learning opportunities. | Could VOI formalization improve ranking of which uncertainty to investigate first and when to stop? |

## Preliminary interpretation

`GENERAL_EPISTEMOLOGY_LAYER` is not yet justified.

The strongest residual candidates for controlled testing are:

1. `BASING_LINEAGE` — evidence present vs evidence that actually grounds the claim;
2. `HIGHER_ORDER_DEFEAT` — evidence about method/agent/inference reliability changes first-order confidence;
3. `TESTIMONY_DISAGREEMENT` — peer/expert disagreement treated as evidence about one's inference, with source-access/reliability distinctions;
4. `CANDIDATE_SET_UNDERDETERMINATION` — best explanation among considered candidates is not unique support if the candidate set is weak;
5. `EPISTEMIC_RISK_THRESHOLD` — requested use/error asymmetry changes how much evidence is sufficient;
6. `VOI_RANKING` — compare learning opportunities by expected decision improvement net of acquisition/delay cost.

Bayesian credence machinery remains a secondary candidate because current qualitative state discipline may already be safer where priors/likelihoods are not grounded.
