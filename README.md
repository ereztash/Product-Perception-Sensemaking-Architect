# Neta — Product Perception & Sensemaking Architect

Neta helps an owner-builder turn a raw product intuition into a defensible design decision **without letting the claim or the action outrun the evidence, reality level and authority that actually exist**.

The presenting state can be as vague as:

> "זה מרגיש כמו Windows XP"
>
> "הכפתור לא מגיב"
>
> "אני משקיע בהחלטה ולא מקבל מספיק בחזרה"

Neta first preserves that language, then discriminates among neighboring mechanisms. v0.2 adds a deeper assurance layer learned from the Lessons re-foundation.

## Canonical state

The repository now separates the **method version**, the **frozen prompt baseline**, and the **evaluation evidence**.

- canonical method: **v0.2 assurance re-foundation**;
- canonical prompt comparator: **v0.1 frozen baseline**;
- GitHub Benchmark Wave 1: **closed at BATCH-016 due saturation under the current broad sampling distribution**;
- prompt updates earned by that wave: **none**;
- next empirical frontier: **Hebrew falsification**, with Signal Fidelity and Reader Effect kept as separate evaluation tracks.

See `docs/CANONICAL_STATE.md` and `eval/github-benchmark/WAVE1_CLOSEOUT.json`.

## Two nested loops

### Sensemaking

```text
RAW SIGNAL
→ CONCRETE MOMENT
→ OBSERVABLE
→ COMPETING MECHANISMS
→ CHEAP DISCRIMINATOR
→ DESIGN DISTINCTION
```

### Assurance

```text
CLAIM
→ EVIDENCE
→ REALITY LEVEL
→ RESOLUTION AUTHORITY
→ REQUESTED USE
→ PERMISSION
→ INTERVENTION
→ GATE / REVERSAL
→ AUTHORITY CEILING / STOP
```

The first loop helps name what is happening. The second prevents a good explanation from becoming an unauthorized conclusion.

## v0.2 re-foundation

A finding is now a **claim/evidence ledger**, not one confidence label.

The same finding may legitimately contain:

- a repository observation that is established;
- a design mechanism that has external research support;
- a reversible intervention that the owner is allowed to try;
- a predicted external-user outcome that remains unresolved and denied until FIELD evidence exists.

This is not indecision. It is epistemic separation.

See:

- `docs/NETA_ASSURANCE_THESIS.md`
- `docs/REALITY_AUTHORITY_PERMISSION.md`
- `docs/LESSONS_COVERAGE_AUDIT.md`
- `docs/FAILURE_LINEAGE.md`

## v0.1 baseline is frozen

The v0.1 prompt remains unchanged as a clean-model comparator. CI checks its Git blob hash.

The re-foundation does **not** earn a prompt edit by being conceptually better. A prompt change still requires a demonstrated clean-model failure, the missing hidden judgment, a smallest repair and a neighboring control.

See `docs/V0_1_FREEZE.md`.

## Research quarantine

Wave 1 already collected external evidence under a frozen preregistration. Its original G/C/A/O vectors and promotion states remain historical truth.

v0.2 does not rewrite them. It adds a prospective question:

> Given this research state, what concrete use is actually permitted in a Neta finding?

External research still cannot edit the prompt directly.

See `research/WAVE1_ASSURANCE_REVIEW.md` and `research/AMENDMENTS.md`.

## Core working lenses

Neta silently checks:

| Lens | Question |
|---|---|
| **Perception** | What does the eye rank first? |
| **Orientation** | Is the current state legible? |
| **Action** | Does the current mode make the next move discoverable? |
| **Feedback** | Did the system acknowledge the action and make the transition perceptible? |
| **Payoff** | Does cognitive reward justify cognitive cost? |
| **Accumulation** | Does the interaction leave useful evidence/progress behind? |
| **Trust** | What is known, from what evidence/reality, and what does it authorize? |

These are working lenses, not a validated exhaustive taxonomy.

## Non-goals

- no generic heuristic checklist as the default response;
- no automatic redesign from a metaphor;
- no fake confidence percentages;
- no treating taste as usability or owner taste as market preference;
- no field claims from repo/research evidence alone;
- no adding probes merely because they are measurable;
- no removing instrument friction without a validity decision;
- no SaaS/UI/dashboard until a measured failure earns it;
- no source 29 merely to increase citation count;
- no feature justified only by encodability.

## Repository structure

```text
prompts/       frozen v0.1 baseline until clean-model failure earns change
schemas/       v0.2 claim/evidence finding contract + research claim contract
memory/        owner-language priors, never ground truth
fixtures/      conversational/research/assurance cases
eval/          behavior rubric and empirical observatories
docs/          telos, method, assurance, authority, lineage, canonical state
research/      frozen research quarantine + prospective evidence layers
scripts/       executable gates and deliberate positive controls
```

## Current status

**v0.2 ASSURANCE RE-FOUNDATION · PROMPT FROZEN · GITHUB WAVE 1 CLOSED AT SATURATION · HEBREW FALSIFICATION NEXT · NO UI.**

The next legitimate unit of progress is a clean Hebrew judgment failure or a surviving Neta-vs-baseline Hebrew decision delta — not additional broad GitHub sampling and not a prompt edit by intuition.
