# R&D Synthesis — Does epistemology expertise strengthen R&D?

Status: `MANUAL_RND_SYNTHESIS · REPO_GROUNDED · EXTERNAL_RESEARCH_INFORMED · NETA_REVIEWED · NOT_CANONICAL`
Date: 2026-09-06

## decision_before

Hypothesis under test:

> If explicit expertise in epistemology materially strengthens R&D's ability to decide what is worth learning, then the emerging `epistemic effort calibration` telos is probably identifying a real capability rather than a locally convenient metaphor.

Possible outcomes were frozen as:
- H0 vocabulary-only;
- H1 broad epistemology upgrade;
- H2 targeted subdomain transfer.

## evidence recovered

### Strong external convergence

Academic epistemology contains mature distinctions closely matching current repo concerns:
- evidence and justification;
- evidence actually grounding a belief vs merely being available;
- higher-order evidence about one's evidence/reliability;
- process reliabilism;
- testimony/expert disagreement;
- underdetermination;
- abduction / inference to best explanation;
- Bayesian credence updating;
- epistemic/inductive risk;
- epistemic utility and value of knowledge.

### Stronger adjacent convergence

Decision analysis / Value of Information asks an especially close version of the live R&D question:
- what decision should be made now under uncertainty;
- whether more evidence is worth acquiring;
- which uncertainty/study is worth buying;
- whether the expected improvement from information exceeds research and delay cost.

This is structurally very close to `epistemic effort calibration`.

### Repo overlap

The Shared Epistemic Kernel and R&D already independently implement many applied epistemic constraints:
- evidence is not represented reality;
- authority belongs to the claim;
- permission is not confidence;
- agreement is not independent triangulation;
- null is not refuted;
- provenance and reversal matter;
- research support is not product-specific field effect;
- stale existence is not current runnability;
- falsification and neighboring alternatives matter;
- more learning is not automatically progress;
- stop when remaining uncertainty cannot change the decision.

## comparative test result

Eight controlled boundary cases compared current R&D against an epistemology-augmented challenger.

### Epistemology proper

Across seven epistemology cases:
- clean B-only next-move delta: **0/7 established**;
- sharper hidden judgment / explanation: **4/7**;
- broad-layer justification: **not supported**.

This means the current agent is already behaviorally close to applied epistemology in the tested dimensions.

### Value of Information

One case exposed a live ambiguity:

```text
CHEAPEST ADMISSIBLE LEARNING THAT CAN CHANGE A DECISION
vs
HIGHEST EXPECTED DECISION IMPROVEMENT NET OF LEARNING COST
```

When two learning moves can both change the decision, literal cheapest-first can be dominated by a more expensive but much more decision-valuable observation.

Current R&D partially contains the right answer through `expected_decision_value`, but the doctrine lacks a crisp ranking law.

## Neta delta

Neta materially changed the interpretation by separating:

```text
CONCEPTUAL RESEMBLANCE
≠
MISSING CAPABILITY
```

and:

```text
EPISTEMOLOGY
— what counts as justified/reliable support?

VALUE OF INFORMATION / DECISION ANALYSIS
— which uncertainty is worth paying to reduce?
```

Therefore the research must not attribute a VOI gain to epistemology merely because both concern knowledge under uncertainty.

## decision_after

### Broad claim

> `ADD_GENERAL_EPISTEMOLOGY_EXPERTISE_TO_RND`

**NOT EARNED.**

### Narrow claim

> `R&D's current architecture has independently converged on a substantial subset of applied epistemic principles, and targeted epistemology may strengthen edge judgments.`

**SUPPORTED AS A RESEARCH SIGNAL.**

### Strongest capability hypothesis

The most accurate external intellectual neighborhood is currently hybrid:

```text
EPISTEMOLOGY
  evidence / justification / reliability / defeat / disagreement
        +
PHILOSOPHY OF SCIENCE & METHODS
  hypothesis discrimination / underdetermination / falsification
        +
DECISION ANALYSIS / VALUE OF INFORMATION
  what uncertainty is worth paying to reduce / when enough is enough
        +
AUTHORITY / REALITY CONTRACT
  what source can legitimately close which claim
```

This hybrid maps more closely to the observed R&D telos than `research agent` or `general resource manager`.

## Targeted transfer candidates

Do not add broad field knowledge to the prompt. Test small rules:

1. `HIGHER_ORDER_DEFEAT`
   - Question: does evidence about the reliability of the inference/process materially alter the first-order claim state?

2. `EPISTEMIC_RISK_THRESHOLD`
   - Question: should the requested use and asymmetric false-positive/false-negative cost alter the evidence sufficiency threshold?

3. `CANDIDATE_SET_UNDERDETERMINATION`
   - Question: is the preferred explanation discriminated against plausible alternatives, or only best among a narrow generated set?

4. `BASING_LINEAGE`
   - Question: was the decision actually grounded in this evidence at the relevant time, or is the evidence only current/post-hoc support?

5. `VOI_RANKING`
   - Question: among admissible learning moves, which has the highest expected decision improvement net of acquisition/delay/contamination cost?

## Recalibration recommendation

`USE_DIFFERENTLY`

- Keep `EPISTEMIC_EFFORT_CALIBRATION` as the strongest current telos candidate.
- Do **not** rename R&D an epistemologist or add a broad epistemology module.
- Treat external epistemology as a source of adversarial distinctions and conceptual hygiene.
- Prioritize a separate VOI challenger because it is the strongest candidate to improve the core allocation rule.
- Test targeted epistemic edge rules only where they predict a different next move from current R&D.

## What would make the user's hypothesis materially true

The hypothesis becomes strong if unseen cases show either:

A. one or more targeted epistemology rules repeatedly change the correct next move/claim state while current R&D fails; or

B. a VOI-style ranking rule repeatedly improves which uncertainty R&D chooses to investigate and when it stops.

If neither occurs, the important discovery is still theoretical convergence: R&D has independently rediscovered many applied epistemic norms, but external expertise is not itself a capability upgrade.

## stop_or_continue

`CONTINUE`

Next cheapest discriminating experiment:

Run two independent challengers on unseen neighbor-balanced cases:
1. `CURRENT_RND` vs `CURRENT_RND + TARGETED_EPISTEMIC_EDGE_RULES`;
2. `CURRENT_RND` vs `CURRENT_RND + VOI_RANKING`.

Do not combine them in one challenger, or attribution becomes impossible.

## current disposition

`GENERAL_EPISTEMOLOGY_LAYER: NOT_SUPPORTED`

`TARGETED_EPISTEMOLOGY_TRANSFER: PLAUSIBLE_NOT_YET_PROVEN`

`VOI_DECISION_ANALYSIS_TRANSFER: STRONGEST_CURRENT_CAPABILITY_CHALLENGER`

`EPISTEMIC_EFFORT_CALIBRATION_TELOS: EXTERNALLY_CONVERGENT_AND_STRENGTHENED_AS A HYPOTHESIS`
