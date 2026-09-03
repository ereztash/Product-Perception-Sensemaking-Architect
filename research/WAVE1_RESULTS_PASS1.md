# Wave 1 results — external triangulation, pass 1

## Bottom line

Wave 1 pass 1 produced **eight `CANDIDATE_CAPABILITY` distinctions and zero prompt changes**.

That is intentional.

The first external pass did not tell us that Neta needs more UX rules. It mostly told us that several useful portfolio rules were too broad when stated outside the situations that produced them.

The biggest result is therefore **better boundaries**.

## Corpus

Registered in `research/registers/sources.tsv`:

- **28 sources**
- primary experiments / comparative studies
- meta-analyses and systematic reviews
- perceptual psychology
- HCI / aesthetics
- cognitive load and information seeking
- judgment and decision making
- human factors / automation trust
- psychometrics / adaptive testing
- accessibility standards used only for normative/mechanism support, not preference claims
- explicit cross-cultural and socio-cultural evidence

Registered separately:

- **18 contradiction / boundary rows**
- **28 culture/context scope rows**
- **8 discriminating research fixtures**

Citation count is not a score. Sources sharing one lineage are recorded as one `independence_family` for triangulation purposes.

## What changed in Neta's model

### 1. Elicitation is not neutral by default

The portfolio prior was already: preserve the owner's words and ask about the moment before naming the mechanism.

External evidence sharpened it:

> **simple description and directed explanation are not the same intervention.**

Verbal-report meta-analysis indicates that simple concurrent think-aloud can have little effect on accuracy in many tasks, while directed explaining/describing is materially more reactive; all verbal procedures can add time. Cross-cultural usability work also warns that instructions, verbalization and evaluator-participant relationship are context sensitive.

So Neta should not celebrate a distinction merely because it appears after she supplied the vocabulary.

Candidate: `W1-TAC-001`.

---

### 2. "Too much" is not one variable

The portfolio had already learned that a screen can contain many useful things and still fail because nothing is ranked.

The external pass split two questions that are easy to collapse:

1. **How much information exists?**
2. **How is the information perceptually organized?**

Perceptual grouping evidence supports strong effects of common region. Large-scale international visual-preference evidence simultaneously shows that preferred complexity/colorfulness varies substantially across people and contexts.

So Neta may diagnose weak grouping/hierarchy structurally without claiming a universal preferred density.

Candidate: `W1-HIE-001`.

---

### 3. "Windows XP" earns an aesthetic branch, not a usability verdict

The external literature makes the portfolio's anti-decoration rule more precise, not weaker.

Aesthetic appraisal itself contains separable dimensions such as order/clarity and expressive originality. Studies disagree about the causal direction between aesthetics and perceived usability, and international preference data shows substantial variation in preferred visual complexity/colorfulness.

Therefore:

> **an aesthetic complaint is real evidence about perceived craft/appearance, but it does not by itself establish a task-usability defect.**

This prevents both errors:

- laundering "ugly" into "unusable";
- dismissing "ugly/old/cheap" as meaningless taste.

Candidate: `W1-AES-001`.

---

### 4. Responsiveness is not backend speed

The portfolio prior "the button doesn't respond" had three candidates: actual latency, missing acknowledgement, weak state transition.

External evidence expands and stabilizes the decomposition:

- actual completion latency;
- action acknowledgement / success status;
- progress / wait uncertainty;
- perceived duration;
- state-transition salience.

Feedback can change perceived waiting without changing actual latency, and more feedback is not automatically better: accessibility guidance explicitly warns against overly chatty status updates.

Candidate: `W1-FBK-001`.

---

### 5. Cognitive economy is not minimization

This is one of the strongest corrections to a generic UX instinct.

The right target is not:

> less text + fewer choices + fewer steps.

The better distinction is:

> **reduce processing imposed by the interface that does not buy task value, while preserving information that improves comprehension, calibration or the task itself.**

Cognitive-load work distinguishes task/intrinsic difficulty from extraneous processing and emphasizes expertise. Information-foraging theory adds value-rate rather than raw quantity. Choice-overload meta-analysis finds no universal benefit from fewer options.

This supports your earlier phrase **effort must buy payoff**, but makes the denominator and numerator more explicit.

Candidate: `W1-COG-001`.

---

### 6. "One primary action" is a mode rule, not a universal UX law

This is the clearest place where external triangulation narrows a Lichess-derived law.

In an execution state with one already-selected goal, peer-weight controls can create search and competition. That remains a strong local mechanism.

But choice research shows that the effect of more alternatives is conditional on factors such as:

- comparison complexity;
- task difficulty;
- preference uncertainty;
- decision goal.

If the user's task **is to explore and compare alternatives**, suppressing legitimate alternatives can itself damage the task.

So Neta should distinguish:

**EXECUTION:** alternatives compete with the task.  
**EXPLORATION:** alternatives may be the task.

Candidate: `W1-NAV-001`.

This does **not** refute Lichess's one-primary-action law inside its measured decision states. It bounds the transfer of that law to other products.

---

### 7. Trust is not the goal

Human-factors research strongly supports a shift from "increase trust" to **appropriate / calibrated reliance**.

The most important adversarial finding in this pass: one 2026 experiment found that explanations could increase trusting behavior when AI outputs were inaccurate.

Other work distinguishes self-reported trust from behavioral reliance and decision performance, and trust varies with situational, dispositional and learned factors.

So Neta must keep separate:

- subjective trust;
- behavioral reliance;
- system accuracy;
- evidence quality;
- explanation plausibility;
- decision authority.

Candidate: `W1-TRU-001`.

---

### 8. A diagnostic question can become the intervention

This is the most important capability for the Lichess evidence-dashboard direction.

Adaptive testing demonstrates that selecting an informative next item can improve measurement precision. But question-behavior-effect research demonstrates the other side: **asking can change later behavior**. Adaptive precision also does not automatically reduce subjective effort or improve experience.

Therefore a probe is justified only after three ledgers are explicit:

1. **information gain** — which live hypotheses can it separate?
2. **burden** — what does answering cost?
3. **reactivity** — can asking change the behavior we are trying to measure?

Candidate: `W1-INS-001`.

For chess, a question such as "which second move were you considering?" may be highly diagnostic and still be invalid *before* the natural search is finished if it changes candidate generation itself.

---

## Cross-cultural result

The research did **not** produce country-specific design rules. That is a success condition, not a missing deliverable.

The strongest cross-cultural finding is methodological:

> **Country is a sampling context. It is not automatically the causal design mechanism.**

The culture register therefore records axes such as:

- language / register;
- RTL/LTR/script;
- visual-density convention;
- evaluator-user communication context;
- expertise / digital fluency;
- domain and institutional culture;
- accessibility / cognitive context;
- device/infrastructure.

Direct evidence includes a very large international visual-preference study, Arabic government interfaces across ten countries, socio-cultural HCI review evidence and US/China automation-trust evidence. Each also exposes limits to simplistic national prediction.

The largest missing contexts for Neta remain the ones that matter most operationally:

- independent Hebrew/Israeli owner-builder replication;
- dense expert tools;
- CJK product contexts;
- live chess measurement;
- longitudinal real-product use.

Those are recorded as missing, not silently generalized over.

## G/C/A/O state after pass 1

No scalar confidence score is computed.

| Claim | Capability | G | C | A | O | State |
|---|---|---:|---:|---:|---:|---|
| `W1-TAC-001` | tacit → explicit | 3 | 2 | 2 | 3 | CANDIDATE_CAPABILITY |
| `W1-HIE-001` | hierarchy / quantity | 3 | 3 | 2 | 3 | CANDIDATE_CAPABILITY |
| `W1-AES-001` | aesthetics / craft | 3 | 3 | 2 | 3 | CANDIDATE_CAPABILITY |
| `W1-FBK-001` | interaction feedback | 3 | 1 | 2 | 3 | CANDIDATE_CAPABILITY |
| `W1-COG-001` | cognitive economy | 3 | 1 | 2 | 3 | CANDIDATE_CAPABILITY |
| `W1-NAV-001` | orientation / action choice | 3 | 1 | 2 | 3 | CANDIDATE_CAPABILITY |
| `W1-TRU-001` | trust / reliance | 3 | 2 | 2 | 3 | CANDIDATE_CAPABILITY |
| `W1-INS-001` | adaptive instrumentation | 3 | 1 | 2 | 3 | CANDIDATE_CAPABILITY |

Interpretation:

- `G3`: externally researched, but the **Neta mechanism itself** has not been replicated by another operator; literature does not grant G7.
- `C`: varies honestly by represented context instead of being maximized.
- `A2`: every candidate underwent explicit contrary/boundary search.
- `O3`: each has a concrete discriminator and fixture.

## Why zero prompt changes

The quarantine requires more than literature support.

A candidate becomes `PROMPT_ELIGIBLE` only when a Neta evaluation exposes a failure/blind spot that the candidate can repair, and the smallest prompt rule plus a neighboring behavior-at-risk and control are specified.

Pass 1 produced **structural reasons to test four prompt areas first**:

1. one-primary-action may be over-broad outside execution mode;
2. instrumentation rule omits explicit measurement-reactivity risk;
3. trust lens does not yet distinguish trust from calibrated reliance;
4. feedback lens does not yet explicitly separate completion latency, acknowledgement, progress and state salience.

These are documented in `research/PROMPT_GAP_AUDIT.md`.

They are **not yet prompt failures** because a clean-model fixture run has not demonstrated them.

## Decision

**PASS 1 COMPLETE. DO NOT EDIT THE SYSTEM PROMPT YET.**

The highest-information next move is not another broad literature sweep. It is a clean-context evaluation of the canonical prompt against the eight new fixtures, with the four structural gaps above treated as preregistered failure candidates rather than expected answers.
