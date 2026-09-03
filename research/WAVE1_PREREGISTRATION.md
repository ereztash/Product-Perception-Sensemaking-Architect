# Wave 1 preregistration — recursive triangulation

**Status: FROZEN BEFORE SOURCE COLLECTION**

This file fixes the questions, promotion rules and stopping rules for Wave 1 before the corpus is collected. Once the first source row is added to `registers/sources.tsv`, substantive edits here require an entry in `AMENDMENTS.md` and may not be used to rescue a failing candidate retroactively.

## Purpose

Deepen Neta's capabilities without converting one operator's portfolio conventions into universal design laws.

Wave 1 asks:

> Which distinctions in Neta survive triangulation across independent research traditions, adversarial evidence, and materially different cultural/contextual conditions — and which need to be narrowed, split, or rejected?

The target is **better discrimination**, not more rules.

## Eight capability families

### W1. Tacit → explicit design knowledge

Question: How can Neta help an owner make an implicit design perception explicit without planting the answer?

Neighboring mechanisms to keep separate:
- elicitation;
- suggestion / demand characteristics;
- reflective conversation;
- recognition vs recall;
- vocabulary teaching;
- retrospective rationalization.

### W2. Perceptual hierarchy

Question: Which properties reliably affect what is perceived as primary, and which effects are context-, task-, expertise-, or culture-dependent?

Keep separate:
- salience;
- visual hierarchy;
- reading order;
- grouping;
- information quantity;
- task relevance.

### W3. Aesthetic judgment / perceived craft

Question: When is language such as "old", "cheap", "Windows XP", "messy" a useful signal about structural design, and when is it preference or cultural convention?

Keep separate:
- classical/order aesthetics;
- expressive aesthetics;
- familiarity;
- perceived modernity;
- coherence;
- usability inference from appearance.

### W4. Interaction feedback

Question: How should Neta distinguish actual latency from missing acknowledgement, weak state transition, progress uncertainty, and action-state ambiguity?

Keep separate:
- system response time;
- acknowledgement latency;
- progress feedback;
- state salience;
- success/error visibility;
- perceived responsiveness.

### W5. Cognitive economy

Question: How should Neta reason about effort, cognitive load, payoff and accumulation without assuming that less information or less friction is always better?

Keep separate:
- intrinsic task effort;
- extraneous interaction cost;
- instrument friction;
- information value;
- immediate payoff;
- accumulated payoff;
- trust/completeness tradeoffs.

### W6. Orientation & navigation

Question: Under what conditions should product state nearly dictate the next action, and when is visible choice valuable rather than harmful?

Keep separate:
- information scent;
- wayfinding;
- state clarity;
- primary-action competition;
- exploration vs execution mode;
- expert shortcuts vs novice guidance.

### W7. Trust & uncertainty communication

Question: How should Neta express evidence, uncertainty, limits and reversibility without fake precision or false reassurance?

Keep separate:
- confidence;
- evidence quantity;
- evidence quality;
- provenance;
- calibration;
- permission/authority;
- user trust.

### W8. Adaptive instrumentation

Question: When does an additional question/probe create enough expected information gain to justify the cognitive cost and risk of contaminating the behavior being measured?

Keep separate:
- information gain;
- measurement reactivity;
- question burden;
- adaptive testing;
- selection bias;
- intervention contamination.

## Source sampling rule

A candidate may not reach `PROMPT_ELIGIBLE` from citation volume alone.

For any candidate seeking promotion:

1. **Independent empirical surface** — at least one primary empirical source or dataset directly relevant to the mechanism.
2. **Independent second surface** — at least one review, replication, standard, or adjacent-discipline result not merely restating the first source.
3. **Adversarial surface** — an explicit search for null results, contrary findings, boundary conditions, or a competing explanation.
4. **Culture/context surface** — if culture relevance is `material` or `plausible`, include either a direct cross-cultural design or at least two materially different cultural/contextual samples. If relevance is `low`, record why.
5. **Independence check** — sources sharing the same dataset, lab, benchmark, or review lineage are marked as one evidence family for triangulation purposes.

These are eligibility conditions, not a claim that three sources prove truth.

## Culture sampling policy

Wave 1 must not reduce culture to nationality. For every capability where culture relevance is `material` or `plausible`, record whichever axes are actually evidenced:

- script / writing direction;
- language / register;
- visual-density convention;
- communication context;
- expertise / digital fluency;
- domain culture;
- institutional context;
- accessibility / cognitive constraints;
- device / infrastructure context.

Geographic samples should, where the literature permits, include evidence beyond North American / Western-European English-language contexts. Absence of such evidence is recorded as a boundary, never silently generalized over.

## Recursive contradiction protocol

For each candidate:

```text
claim vN
→ supporting evidence
→ contradiction search
→ classify contradiction
```

Contradictions are classified as:

- `REFUTES` — central mechanism does not survive.
- `NARROWS` — survives only under smaller scope.
- `SPLITS` — one concept contains multiple mechanisms and must branch.
- `CONTEXTUALIZES` — effect differs by task/culture/expertise/etc.
- `MEASUREMENT_CONFLICT` — studies operationalize different constructs.
- `NO_MATERIAL_EFFECT` — source looked contrary but does not change the claim.

If `SPLITS`, child claims receive new IDs and `recursive_parent_id`; the parent may not be promoted unchanged.

If `MEASUREMENT_CONFLICT`, do not average results until the operationalizations are reconciled.

## Promotion vector

No scalar confidence score.

### G — Generalization, Lessons ladder

1. personal preference
2. portfolio convention
3. repeated cross-domain mechanism
4. explicit transferred method
5. executable assurance mechanism
6. candidate general methodological principle
7. externally replicated by another operator/portfolio

Wave 1 research may add external research breadth, but it **does not automatically grant G7**. G7 requires external replication of Neta's mechanism in use, not merely literature support.

### C — Cultural breadth

- `0` no culture/context analysis
- `1` one context only; scope named
- `2` two materially different contexts or one direct cross-cultural comparison
- `3` multiple context families with at least one non-Western/non-English context where relevant
- `4` repeated cross-context evidence plus explicit boundary conditions / local exceptions

### A — Adversarial survival

- `0` no falsification search
- `1` neighboring explanations named
- `2` explicit counterevidence search completed
- `3` material contradictions adjudicated by narrowing/splitting/rejection
- `4` candidate survives a preregistered discriminating test or external replication

### O — Operationalization

- `0` prose intuition
- `1` observable distinction defined
- `2` discriminator specified
- `3` fixture or measurement procedure exists
- `4` gate/positive control or blinded comparison exists
- `5` field observation or replicated operational test exists

No arithmetic combination of G/C/A/O is permitted.

## Promotion gates

### To `TRIANGULATED`

- at least two independent evidence families;
- source provenance recorded;
- claim wording narrower than the strongest evidence.

### To `ADVERSARIAL`

- explicit counterevidence search recorded;
- at least one neighboring explanation named;
- null/contrary evidence is retained, not omitted.

### To `BOUNDED`

- culture relevance recorded;
- context limits recorded;
- material contradictions are disposed as refute/narrow/split/contextualize/measurement-conflict.

### To `FIXTURE_READY`

- one concrete observable;
- one discriminator that could change the diagnosis;
- one reversal condition.

### To `CANDIDATE_CAPABILITY`

- reaches at least `G3`, `A2`, `O3`;
- `C` is appropriate to stated culture relevance rather than maximized performatively;
- no unresolved material contradiction.

### To `PROMPT_ELIGIBLE`

- `CANDIDATE_CAPABILITY` conditions hold;
- a Neta fixture fails without the capability or a new fixture demonstrates a blind spot;
- the proposed prompt rule is the smallest rule that repairs that failure;
- neighboring behavior at risk is named;
- a negative or positive control protects against over-generalization.

A literature-supported capability that has not caused or explained a Neta failure remains research knowledge, not prompt behavior.

## Wave 1 output

For each of the eight families, produce one of:

- promoted candidate distinctions;
- split candidate tree;
- bounded/context-specific mechanism;
- rejected mechanism;
- `DEFER_FIELD` with the smallest external observation needed.

The wave is successful even if several families produce no prompt changes.

## Stopping rule

For one recursive claim branch, stop when either:

1. **two consecutive recursion passes** produce no new design distinction, reversal condition, or boundary condition; or
2. the remaining unresolved question requires external/community behavior or preference evidence.

At wave level, stop when all eight capability families have reached a terminal state for this preregistration (`CANDIDATE_CAPABILITY`, `PROMPT_ELIGIBLE`, `REJECTED`, or `DEFER_FIELD`) or are explicitly carried forward with a recorded unresolved authority.

Do not continue searching merely to increase citation count.

## Contamination rules

- Do not edit this preregistration after source collection begins without an amendment entry.
- Do not change promotion thresholds to rescue a favored claim.
- Do not delete failed claims or contrary sources.
- Do not update `prompts/SYSTEM.md` directly from a paper.
- Do not treat country as causal mechanism without evidence.
- Do not treat a standard as empirical proof of user preference.
- Do not treat an empirical average as a universal design prescription.
- Do not change measurement and intervention together when evaluating adaptive instrumentation.
