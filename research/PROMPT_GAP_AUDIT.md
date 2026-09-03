# Prompt gap audit — after Wave 1 evidence pass 1

This is a **structural audit**, not a clean-model evaluation.

It asks:

> If the eight external candidate capabilities were correct, where does the current `prompts/SYSTEM.md` already express them, where is it ambiguous, and where is there a plausible blind spot worth testing?

It does **not** make any claim `PROMPT_ELIGIBLE` by itself.

## Audit table

| Candidate | Current prompt coverage | Structural status | First clean-model test |
|---|---|---|---|
| `W1-TAC-001` · moment before explanation | Rule 2 already says ask about the moment, not the term; Rule 18 teaches vocabulary after discrimination | **substantially covered** | Does Neta avoid planting an explanatory label before the owner's description contains the distinction? |
| `W1-HIE-001` · quantity vs perceptual organization | Rules 3, 5, 6 and 14 discuss hierarchy, salience, complexity compression and structural confusion | **partially covered** | Given fewer badly-ranked items vs more well-ranked items, does Neta keep quantity and hierarchy as separate hypotheses? |
| `W1-AES-001` · aesthetics ≠ usability | Rule 14 says aesthetics/perceived craft are real and not substitutes for structure; Rule 10 separates accessible from attractive | **partially covered** | Given a pure "Windows XP" complaint with unchanged task flow, does Neta preserve an aesthetic branch without laundering it into usability or dismissing it as mere taste? |
| `W1-FBK-001` · responsiveness decomposition | Rule 4 has a feedback lens; examples distinguish missing acknowledgement and weak state transition | **plausible blind spot** | Does Neta independently separate completion latency, acknowledgement, progress uncertainty and state-transition salience? |
| `W1-COG-001` · cognitive economy ≠ minimization | Rule 8 explicitly asks cost/payoff/accumulation; Rule 15 protects instrument friction; Rule 5 favors compression | **partially covered; compression wording may over-pull toward less** | When more information is task-relevant evidence, does Neta preserve it while reducing only extraneous processing? |
| `W1-NAV-001` · one-primary-action is mode-conditional | Rule 5 says default target is `ONE PRIMARY ACTION`; portfolio memory reinforces PRE-CALL/Lichess | **highest over-generalization risk** | In an explicit exploration/comparison state, does Neta wrongly suppress legitimate alternatives? |
| `W1-TRU-001` · calibrated reliance ≠ maximal trust | Rule 4 defines trust as what system knows/source/authority; Rule 11 covers authority; no explicit subjective-trust vs behavioral-reliance distinction | **plausible blind spot** | If an explanation raises trust in an incorrect AI output, does Neta call that success, or evaluate correctness-sensitive reliance? |
| `W1-INS-001` · probes have reactivity cost | Rule 9 requires hypothesis discrimination and attention cost; Rule 15 says measurement/intervention must not change together | **plausible blind spot** | Before a measured decision, does Neta explicitly ask whether the probe can alter the target behavior, not just whether it is informative? |

## Four highest-information tests

### P1 · Navigation mode boundary

Current prompt:

```text
ONE CURRENT STATE
ONE PERCEPTUAL CENTRE
ONE PRIMARY ACTION
ONE IMMEDIATE PAYOFF
```

It says "Default target", not universal law. The risk is therefore behavioral, not textual: a clean model may still over-transfer the Lichess/PRE-CALL mechanism into exploration states.

**Failure candidate:** recommends hiding peer alternatives when comparing alternatives is the user's actual task.

If observed, candidate `W1-NAV-001` becomes a strong `PROMPT_ELIGIBLE` candidate.

Neighbor behavior at risk from a repair: weakening the one-action discipline in genuine execution states.

---

### P2 · Probe reactivity

Rule 9 currently checks:

1. competing interpretations;
2. discrimination;
3. attention cost.

Rule 15 protects instrument friction and says not to change measurement and intervention together.

But neither directly forces this question at the moment a new probe is proposed:

> **Can asking this question change the behavior whose natural form we are trying to measure?**

**Failure candidate:** recommends a pre-decision chess probe solely because it is highly diagnostic.

Neighbor behavior at risk from a repair: becoming so conservative that useful post-event or low-reactivity probes are rejected.

---

### P3 · Trust vs reliance

The prompt treats `TRUST` largely as evidence/source/authority. That is valuable, but it does not explicitly separate:

- subjective trust;
- behavioral reliance;
- output correctness;
- explanation plausibility.

**Failure candidate:** interprets increased reported trust after explanation as a positive design outcome even when reliance on wrong output rises.

Neighbor behavior at risk from a repair: turning every trust question into a high-stakes automation-calibration lecture when the actual issue is ordinary product credibility.

---

### P4 · Responsiveness decomposition

The prompt can already generate latency / acknowledgement / weak transition as hypotheses. But the research suggests a stable four-way decomposition:

- completion latency;
- acknowledgement/status latency;
- progress uncertainty;
- resulting-state salience.

**Failure candidate:** closes the issue after measuring backend/client completion under a threshold, despite no visible acknowledgement or discoverable result.

Neighbor behavior at risk from a repair: over-instrumenting every interaction with progress/status UI when a fast, obvious state change is already sufficient.

## Secondary tests

`W1-HIE-001`, `W1-AES-001`, and `W1-COG-001` should also run, but their neighboring judgments are already represented substantially enough that a clean pass would be unsurprising.

`W1-TAC-001` is closest to the original raison d'être of Neta and is already strongly encoded. Its test is mainly a regression guard against vocabulary planting.

## Culture/context observation

The canonical prompt contains no explicit "country is not a mechanism" rule.

That omission is **not yet treated as a prompt gap** because Neta is currently personalized primarily to one owner and has not been asked to generate culture-specific prescriptions as a core behavior.

If a clean fixture causes Neta to infer design rules from nationality or region labels without a measured mechanism, that would create the missing failure evidence needed for a prompt rule.

## Decision

No candidate is promoted to `PROMPT_ELIGIBLE` from this audit.

Next authority: **clean-model fixture behavior**.

The first run should preserve the current `SYSTEM.md` exactly. Expected failure locations above must not be shown to the runner.
