# Applied Epistemology Transfer Map v0

Status: `EXTERNAL_CONCEPT_MAPPING · CANDIDATE_TRANSFER_ONLY · NOT_PROMOTION_EVIDENCE`
Date: 2026-09-06

## Question

Does applied epistemology add decision-changing distinctions to the current R&D Agent beyond the targeted epistemology concepts and VOI challenger already under test?

## Why separate applied epistemology

Applied epistemology does not merely ask abstractly what knowledge or justification is. It applies epistemic norms to real inquiry practices, testimony, expertise, institutions, collective deliberation, framing and high-stakes contexts.

The live R&D hypothesis is therefore not `add philosophy knowledge`, but:

> Does applied epistemology improve how R&D structures inquiry before, during and after evidence acquisition?

## External concepts with plausible transfer value

### AE-1 — INQUIRY_FRAME_RELEVANCE

Recent work on lines of inquiry treats the practice of deciding what is relevant to a question as itself normatively evaluable. A research process can contain true facts yet still be epistemically poor because its frame makes the wrong facts/questions salient.

Candidate R&D delta:
- distinguish `evidence quality` from `inquiry-frame quality`;
- ask whether the current line of inquiry excludes plausible decision-relevant variables before buying more evidence inside the frame;
- detect research that is rigorous conditional on a prematurely narrowed question.

Current repo coverage: `PARTIAL`.
- R&D has `material_question`, `bottleneck`, candidate moves and cheapest decision-changing learning;
- Question Discovery / front-door work challenges premature objects;
- no generic R&D rule explicitly evaluates whether the *set of facts/questions treated as relevant* is itself biasing the inquiry.

### AE-2 — TESTIMONY_AND_EXPERT_DEFERENCE

Applied/social epistemology treats expert testimony as a distinct justification problem. Expertise is domain-relative and rational deference depends on access, track record, bias, independence and what kind of authority the expert actually has.

Candidate R&D delta:
- expert status should not automatically close a claim;
- distinguish expertise from first-hand access and from decision authority;
- disagreement with a relevant peer/expert may be higher-order evidence about the current inference;
- institutional communication may mediate or distort expert evidence.

Current repo coverage: `PARTIAL_TO_STRONG`.
- claim-specific authority and lineage independence already exist;
- resource assessment tracks neighboring weakness and prior usefulness;
- residual: explicit `expertise ≠ authority ≠ access ≠ independence` decomposition is not strongly encoded.

### AE-3 — COLLECTIVE_INQUIRY_DESIGN

Applied epistemology evaluates whether groups/institutions are structured in ways that tend to produce reliable justified beliefs, not merely whether individual pieces of evidence are good.

Candidate R&D delta:
- evaluate whether a research process systematically suppresses dissent, duplicates the same error path, or lacks epistemically relevant diversity;
- treat the design of inquiry itself as a reliability object.

Current repo coverage: `PARTIAL`.
- agreement ≠ independent triangulation;
- provenance and shared ancestry are tracked;
- peer disagreement is preserved;
- residual: independence of sources is represented better than the *structure of collective inquiry* that determines which sources become visible.

### AE-4 — SITUATED_EVIDENCE / EPISTEMIC EXCLUSION

Applied epistemology and epistemic-injustice work emphasize that credibility allocation and standpoint can cause relevant evidence to be systematically ignored or discounted.

Candidate R&D delta:
- when the claim concerns experience, implementation or harm, ask whether the evidence set systematically omits the people with direct situated access;
- distinguish low-status testimony from low-quality testimony;
- detect sampling/voice exclusion as an epistemic defect, not only a fairness concern.

Current repo coverage: `PARTIAL`.
- FIELD authority exists for external human perception/value/behavior;
- no generic R&D rule checks whether the chosen FIELD sample or testimony structure excludes materially situated evidence.

### AE-5 — PRACTICAL / MORAL ENCROACHMENT ON EVIDENCE THRESHOLDS

Applied epistemology examines whether practical or moral stakes can affect how much evidence is required before belief/action is justified.

Candidate R&D delta:
- requested use and asymmetric error consequences may alter evidence sufficiency;
- do not collapse this into truth-confidence: the same evidence may support a hypothesis while not licensing a high-stakes action.

Current repo coverage: `STRONG_PARTIAL`.
- permission is separate from confidence;
- reversibility and requested use already matter;
- this overlaps the existing `EPISTEMIC_RISK_THRESHOLD` challenger and should not be counted twice.

## Strongest applied-epistemology challenger

The most distinctive residual is currently:

> **INQUIRY_FRAME_RELEVANCE**

Reason:

Current R&D explicitly asks which uncertainty to reduce and which evidence channel to use, but it can still perform excellent evidence selection *inside a badly framed line of inquiry*.

Potential failure chain:

```text
DECISION
→ PREMATURELY FRAMED QUESTION
→ RELEVANCE FILTER
→ HIGH-QUALITY EVIDENCE INSIDE THAT FILTER
→ WELL-JUSTIFIED ANSWER TO THE WRONG/NARROW QUESTION
→ LITTLE DECISION IMPROVEMENT
```

Candidate guard:

> Before allocating epistemic effort, test whether the current line of inquiry treats all plausibly decision-changing factors as eligible for relevance, rather than merely optimizing evidence inside the inherited frame.

## Boundary to Neta / Question Discovery

This must not silently recreate a separate Question Discovery engine.

- Neta owns product/design signal → mechanism discrimination.
- Front-door gate owns whether full calibration should run.
- R&D would own inquiry-frame relevance only when the *epistemic investment* depends on what is being treated as relevant evidence/question-space.

If the distinction can be fully handled by the existing `material_question + bottleneck` fields with no decision delta, do not add it.

## Sources

- Alex Worsnip, “Applied Epistemology: What Is It? Why Do It?”, Oxford Studies in Epistemology 8, 2026.
- Susanna Siegel, “How Do Lines of Inquiry Unfold? Insights from Journalism”, Oxford Studies in Epistemology 8, 2026.
- Jennifer Lackey (ed.), Applied Epistemology, Oxford University Press, 2021.
- OpenStax, Introduction to Philosophy, section 7.5 Applied Epistemology.
- Tony Ward, “Expert Testimony, Law and Epistemic Authority”, Journal of Applied Philosophy 34(2), 2017.

## Current disposition

`APPLIED_EPISTEMOLOGY_BROAD_LAYER: NOT_JUSTIFIED`

`INQUIRY_FRAME_RELEVANCE: STRONGEST_NEW_TRANSFER_CANDIDATE`

`EXPERTISE / COLLECTIVE / SITUATED_EVIDENCE: EDGE_RULE_CANDIDATES`
