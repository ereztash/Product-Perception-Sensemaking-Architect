# Recursive triangulation log

This log records what each research recursion changed. Citation volume alone does not count as progress.

A pass earns continuation only by producing at least one of:

- a new design distinction;
- a new reversal condition;
- a new boundary condition;
- a refutation / split / measurement conflict that changes the candidate.

## Pass 0 — portfolio priors

**Input:** Neta v0.1 + Lessons lineage + Lichess inertial/visual laws + Erez's portfolio.

Starting priors included:

- preserve raw owner intuition before naming it;
- state should often make the next action obvious;
- one primary action;
- effort must buy payoff;
- measurement before intervention;
- instrument friction is not automatically a defect;
- aesthetics are not a substitute for structure;
- confidence should be evidence-bounded;
- extra instrumentation must buy information.

**Known contamination:** all originated in or were selected by one operator's portfolio.

**Decision:** freeze Wave 1 before external source collection.

---

## Pass 1 — external triangulation + adversarial search

**Input:** 28 registered sources across HCI, perceptual psychology, cognitive science, judgment/decision making, human factors, psychometrics, accessibility and socio-cultural HCI.

### New distinctions produced

1. **Simple description ≠ directed explanation.**
   - Changed W1 from generic reflective dialogue to a reactivity-aware elicitation rule.

2. **Information quantity ≠ perceptual organization.**
   - Strengthened W2 and prevented "too much" from collapsing into count.

3. **Aesthetic appraisal ≠ perceived usability ≠ task usability.**
   - Changed W3 from anti-decoration only to a positive aesthetic/perceived-craft branch.

4. **Completion latency ≠ acknowledgement ≠ progress uncertainty ≠ state salience.**
   - Expanded W4 beyond the initial latency/feedback pair.

5. **Cognitive economy ≠ minimization.**
   - W5 now distinguishes task-required processing, extraneous cost, expertise and information value.

6. **One primary action is mode-conditional.**
   - W6 is bounded to dominant execution states rather than exported as a universal design law.

7. **Subjective trust ≠ behavioral reliance ≠ decision performance.**
   - W7 shifts target from trust to calibrated/correctness-sensitive reliance where automation is involved.

8. **Information gain ≠ free information.**
   - W8 adds measurement reactivity and burden to adaptive-probe value.

### New cross-cultural boundary

Country/region was rejected as a default causal design mechanism.

The culture register now tracks language/script, communication context, density convention, expertise, domain/institution, accessibility and device/infrastructure where evidence exists.

### Contradictions that materially changed wording

18 rows were retained. None were deleted after synthesis.

Two apparent `SPLITS` were reclassified before merge as `MEASUREMENT_CONFLICT`:

- perceived wait vs experience/preference (`C007`);
- subjective trust vs reliance/performance (`C014`).

Reason: the registered candidate already separates the constructs. Creating child claims would falsely imply that the parent mechanism itself fragmented; the contradiction instead showed that studies were measuring different outcomes.

### State after Pass 1

All eight branches reached `CANDIDATE_CAPABILITY` under the preregistered G/C/A/O gates.

No branch reached `PROMPT_ELIGIBLE` because no clean Neta run has yet demonstrated the corresponding behavioral blind spot.

---

## Pass 2 — structural prompt challenge

**Input:** the eight pass-1 candidates compared against the unchanged canonical `prompts/SYSTEM.md`.

This is not a model run and therefore cannot close a prompt-behavior question.

### New boundary conditions produced

The audit identified four places where the current prompt can plausibly over- or under-generalize:

- `ONE PRIMARY ACTION` may over-transfer from execution to exploration;
- probe information-gain rule does not explicitly force measurement-reactivity analysis;
- trust lens does not explicitly separate subjective trust from behavioral reliance;
- feedback lens does not explicitly force completion/acknowledgement/progress/state-salience separation.

Three other candidates are partially covered, and moment-first elicitation is substantially covered.

**New artifact:** `research/PROMPT_GAP_AUDIT.md`.

### Did Pass 2 produce a new distinction/boundary/reversal?

**Yes.** It produced a product-specific boundary between:

- research evidence that supports a candidate;
- structural prompt coverage;
- actual model failure.

Therefore the recursive stopping condition has **not** fired. This is not a second no-new-information pass.

---

## Next pass — clean-model fixture evaluation

Run the unchanged `prompts/SYSTEM.md` in a clean context against `fixtures/research-wave1-pass1.md`.

Do not give the runner:

- `WAVE1_RESULTS_PASS1.md`;
- `PROMPT_GAP_AUDIT.md`;
- expected failure locations;
- candidate claim states;
- previous outputs.

The run should answer whether any candidate capability is actually missing from Neta's behavior.

A clean green fixture may show that research knowledge does **not** need to enter the prompt.

That is a valid success outcome.

## Recursive stop

Not reached yet.

To claim a branch has exhausted internal research under Wave 1, either:

- two consecutive subsequent passes must produce no new distinction/reversal/boundary; or
- the remaining authority must become external field/community evidence.
