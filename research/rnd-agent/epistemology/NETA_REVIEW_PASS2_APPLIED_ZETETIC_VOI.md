# Neta Review — Applied/Zetetic Epistemology + VOI Pass 2

Status: `ROLE_CONDITIONED_MANUAL_NETA_REVIEW · NOT_RUNTIME_EXECUTION · NOT_CANONICAL`
Date: 2026-09-06

## Raw signal under review

Repeated result:
- current R&D matches applied/zetetic inquiry challenger on 12/12 harder cases;
- current R&D matches explicit VOI challenger on 10/10 controlled ranking cases;
- external theory gives cleaner names/decompositions but not yet a unique next move.

## Competing interpretations

### H1 — external expertise is unnecessary
R&D already contains everything relevant; epistemology/VOI add no capability.

### H2 — external expertise is already latent in the base model
The prompt does not contain the theory explicitly, but the same underlying model can reconstruct it from general knowledge, masking prompt-level capability differences.

### H3 — the telos has independently compressed the same problem structure
Because R&D is forced to reason from telos, current state, authority, bottleneck, expected decision value, reversibility and stop conditions, it converges behaviorally on norms that applied/zetetic epistemology and VOI formalize academically.

## Neta discrimination

The observed data supports H3 as a **strong architectural hypothesis**, but cannot distinguish H3 cleanly from H2 in same-model manual runs.

Key non-collapse:

```text
SAME NEXT MOVE UNDER SAME MODEL
≠
PROMPT CONTAINS THE CAPABILITY
≠
EXTERNAL THEORY IS USELESS
```

However another non-collapse is equally important:

```text
EXTERNAL THEORY NAMES THE SAME DISTINCTION
≠
EXTERNAL THEORY IMPROVES THE AGENT
```

Therefore do not add epistemology/VOI modules merely because the conceptual fit is elegant.

## What the experiments do establish

1. Current R&D behavior is strongly compatible with **inquiry-level epistemic discipline**:
   - it challenges premature candidate sets;
   - notices source/requested-use mismatches;
   - identifies missing actors with distinctive evidence access;
   - preserves bounded direct-authority questions;
   - reopens a question when its answer space is not earned.

2. Current R&D behavior is strongly compatible with **Value-of-Information reasoning**:
   - it does not choose cheapest lexicographically;
   - it trades information value against cost/delay/reactivity;
   - preserves option value;
   - stops when information cannot alter the decision;
   - respects validity/authority before value ranking.

3. The external theories add **better observables for evaluation** even where they add no action:
   - `PREMATURELY_DEFINITE`
   - `WRONG_RELEVANCE_STRUCTURE`
   - `MISSING_RELEVANT_KNOWER`
   - `SOUND_BOUNDED`
   - explicit VOI dominance / option-value / zero-value cases.

## Neta's main challenge to the emerging telos

Do not conclude that the telos is "epistemology".

The observed invariant is still better stated functionally:

> calibrate learning/inquiry effort to what can change a consequential decision.

Applied/zetetic epistemology appears to describe **quality constraints on the inquiry**.
VOI appears to describe **allocation logic among learning moves**.
Neither alone equals the telos.

A more coherent decomposition is:

```text
LIVE DECISION
→ IS THE GUIDING INQUIRY SOUND / RELEVANT?
→ WHAT UNCERTAINTY CAN STILL CHANGE THE DECISION?
→ WHICH ADMISSIBLE LEARNING MOVE HAS THE BEST DECISION VALUE?
→ WHAT DOES THE OBSERVED EVIDENCE JUSTIFY?
→ CONTINUE / CHANGE CHANNEL / STOP
```

Current R&D already approximates this chain through broader primitives.

## What would falsify the "already latent capability" interpretation

Find natural unseen cases where:
- current R&D repeatedly selects the wrong question/evidence channel/stop point;
- an externally specified applied-epistemology or VOI rule repairs those failures without harming neighbors;
- the repair persists across a different model/runtime or frozen prospective traffic.

Without that, external theory should be used as an **evaluation ontology / adversarial case generator**, not automatically promoted into the production prompt.

## Neta disposition

- `ADD_APPLIED_EPISTEMOLOGY_MODULE`: NOT EARNED
- `ADD_EXPLICIT_VOI_FORMULA`: NOT EARNED
- `USE_APPLIED_EPISTEMOLOGY_AS_EVAL_ONTOLOGY`: EARNED AS RESEARCH TOOL
- `USE_VOI_AS_EVAL_ONTOLOGY`: EARNED AS RESEARCH TOOL
- `EPISTEMIC_EFFORT_CALIBRATION_TELOS`: STRENGTHENED BY CROSS-DOMAIN CONVERGENCE, STILL NOT CANONICAL
