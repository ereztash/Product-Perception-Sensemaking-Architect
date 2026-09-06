# R&D Synthesis — Applied/Zetetic Epistemology + VOI Pass 2

Status: `MANUAL_RND_SYNTHESIS · REPO_GROUNDED · EXTERNAL_THEORY_INFORMED · NETA_REVIEWED · NOT_CANONICAL`
Date: 2026-09-06

## Decision before

Test whether adding:
1. applied/zetetic epistemology inquiry rules; or
2. explicit Value-of-Information ranking

materially strengthens current R&D's decisions about what to learn, from whom/where, how much to spend, and when to stop.

## Evidence

### Latent inquiry v0
- CURRENT_RND: 6/6 inquiry-frame failures repaired; 6/6 controls preserved.
- Applied epistemology challenger: identical 12/12 routing; 0 unique next-move deltas.

### Harder zetetic inquiry v1
- CURRENT_RND: 6/6 question/relevance/knower defects repaired; 6/6 controls preserved.
- `INQUIRY_QUESTION_AUDIT`: identical 12/12 next moves; cleaner taxonomy, 0 unique decision deltas.

### VOI ranking v0
- CURRENT_RND and explicit VOI challenger selected the same move in 10/10 cases.
- Current R&D already traded expected decision value against acquisition cost, delay, contamination, authority, reversibility and option value rather than treating cheapest as lexicographically first.

## Decision after

### Capability-addition claims

`ADD_APPLIED_EPISTEMOLOGY_MODULE`
→ **NOT EARNED**

`ADD_EXPLICIT_VOI_RANKING_MODULE`
→ **NOT EARNED AS A CAPABILITY REPAIR**

No tested case showed a correct next move available only after the added theory.

### Stronger interpretation

The repeated lack of challenger delta, together with high conceptual alignment, supports a different hypothesis:

> **Current R&D already behaves like a compact applied inquiry-epistemology + decision-value system because its functional constraints force many of the same judgments.**

This is not proof of independent rediscovery because all manual runs share the same underlying model lineage. The base model may already know the external theories.

## What external theory did add

External theory is currently more valuable as an **evaluation ontology** than as production prompt content.

Useful applied/zetetic eval labels:
- `PREMATURELY_DEFINITE`
- `WRONG_RELEVANCE_STRUCTURE`
- `MISSING_RELEVANT_KNOWER`
- `SOUND_BOUNDED`

Useful VOI eval distinctions:
- value dominance vs cheapest-sufficient;
- zero-value information;
- delay-adjusted value;
- contamination/reactivity cost;
- authority-before-value;
- sequential option value.

These labels make future failures easier to classify and can generate adversarial neighbors without automatically expanding runtime doctrine.

## Telos implication

The experiments strengthen the functional telos candidate:

> **R&D exists to calibrate inquiry/learning effort to the uncertainty that can still change a consequential decision.**

Operationally:

```text
LIVE DECISION
→ IS THE GUIDING INQUIRY SOUND ENOUGH?
→ WHAT UNCERTAINTY CAN STILL CHANGE THE DECISION?
→ WHICH ADMISSIBLE LEARNING MOVE IS WORTH BUYING?
→ WHAT DOES THE RESULT ACTUALLY JUSTIFY?
→ CONTINUE / CHANGE CHANNEL / STOP
```

Applied epistemology mainly constrains the first and fourth transitions.
VOI mainly constrains the third.
The current R&D method already approximates the whole chain.

## Strongest remaining uncertainty

Same-model manual ablations cannot tell whether:
- the R&D prompt architecture itself causes these judgments; or
- the underlying general model reconstructs applied epistemology/VOI even without explicit rules.

Therefore the cheapest next discriminating test is **natural unseen transfer**, preferably with frozen outputs from a baseline model/run or a different model lineage.

## Recommended next move

`TEST`

Do not modify the production R&D prompt yet.

Use applied/zetetic epistemology and VOI to author/classify future holdout cases. Promote only if a clean repeated CURRENT_RND failure is repaired by one targeted rule without harming neighboring non-fire cases.

## Current disposition

`APPLIED_EPISTEMOLOGY_AS_PRODUCTION_MODULE: NOT_EARNED`

`VOI_AS_PRODUCTION_MODULE: NOT_EARNED`

`APPLIED_EPISTEMOLOGY_AS_EVAL_ONTOLOGY: SUPPORTED`

`VOI_AS_EVAL_ONTOLOGY: SUPPORTED`

`EPISTEMIC_EFFORT_CALIBRATION_TELOS: STRENGTHENED_BY_THEORETICAL_AND_BEHAVIORAL_CONVERGENCE · NOT_CANONICAL`
