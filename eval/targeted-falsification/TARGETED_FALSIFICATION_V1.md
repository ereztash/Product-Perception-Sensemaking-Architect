# Neta Targeted Falsification v1

Status: `PREREGISTERED_BEFORE_EXECUTION`

Purpose: search specifically for Neta failure modes that broad GitHub sampling was unlikely to expose. This protocol does **not** reopen GitHub Benchmark Wave 1 and does not reuse its HOLDOUT as unseen evidence.

## Tested Neta

- canonical method: v0.2 assurance re-foundation
- prompt: frozen v0.1 `prompts/SYSTEM.md`
- no prompt edit during this program

## Why targeted falsification

GitHub Wave 1 produced 14 fully surviving Neta-vs-baseline decision deltas but only 1 clean Neta failure. That evidence is asymmetric: strong for showing restraint wins, weak for locating Neta's own failure boundary.

The next sampling distribution therefore targets suspected **false-build, false-defer, and category-collapse** errors rather than broad repository diversity.

## Four preregistered targets

### TF1 — Execution vs Exploration

Suspected failure: Neta over-transfers `ONE PRIMARY ACTION` into a comparison/exploration state where peer alternatives are the task.

Hidden judgment under test:
> action competition is harmful only when the user already has a dominant execution goal; alternatives may be necessary evidence in exploration.

Red positive control:
- explicit comparison task;
- Neta recommends hiding/suppressing legitimate alternatives or forcing one primary action before comparison is complete.

Neighbor where rule must not fire:
- execution state with one selected goal and several peer-weight controls competing with it.

Falsifiable gate:
- classify state as `EXECUTION | EXPLORATION | MIXED` from provided evidence before any recommendation;
- recommendation must preserve task-essential alternatives in EXPLORATION while allowing stronger compression in EXECUTION.

### TF2 — Probe Reactivity

Suspected failure: Neta chooses a highly informative probe without checking whether asking it changes the behavior being measured.

Hidden judgment under test:
> information gain is insufficient when the probe is itself an intervention on the target behavior.

Red positive control:
- pre-decision probe that names candidate strategies/options before natural search completes;
- Neta recommends it solely because it separates hypotheses.

Neighbor where rule must not fire:
- post-event retrospective probe or low-reactivity telemetry that cannot plausibly alter the target decision.

Falsifiable gate:
- every proposed probe must be classified `LOW | MATERIAL | UNKNOWN` reactivity;
- `MATERIAL` pre-event probes require an explicit protocol tradeoff or alternative measure.

### TF3 — Trust vs Calibrated Reliance

Suspected failure: Neta treats increased subjective trust or explanation plausibility as a positive outcome even when reliance becomes less correctness-sensitive.

Hidden judgment under test:
> subjective trust, behavioral reliance, output correctness, and explanation plausibility are separate outcomes.

Red positive control:
- explanation increases willingness to follow an inaccurate model output;
- Neta calls the explanation a trust/success improvement without considering correctness-sensitive reliance.

Neighbor where rule must not fire:
- ordinary low-stakes credibility/legibility question where no automation-decision reliance claim is being made.

Falsifiable gate:
- when automated advice affects a decision, Neta must keep subjective trust and correctness-sensitive reliance separate.

### TF4 — Responsiveness Decomposition

Suspected failure: Neta closes a responsiveness complaint after measuring one latency dimension while ignoring acknowledgement/progress/state-salience.

Hidden judgment under test:
> completion latency, acknowledgement/status latency, progress uncertainty, and resulting-state salience are neighboring mechanisms.

Red positive control:
- backend completes quickly but user receives no perceptible acknowledgement/result state;
- Neta concludes the interaction is responsive because completion latency is low.

Neighbor where rule must not fire:
- fast interaction with immediate obvious state change and no meaningful wait interval.

Falsifiable gate:
- only measure dimensions needed to discriminate the live mechanisms; do not require progress UI universally.

## Corpus lanes

- `TRAIN_CONTROL`: visible deliberate red/green controls used only to verify the evaluator can detect the target distinction.
- `HOLDOUT`: unseen cases authored/sampled after this protocol and exact tested prompt are frozen.
- `ADVERSARIAL`: cases deliberately designed to make the neighboring rule attractive but wrong.

TRAIN/ADVERSARIAL cases cannot count as unseen validation after their expected judgment is visible.

## Required case structure

For every case:
- case_id
- lane
- product/domain
- evidence boundary
- task state
- raw signal
- material claim
- expected authority
- expected action
- target failure family
- red condition
- neighboring non-fire condition
- Neta output frozen before gold reveal
- baseline output frozen before gold reveal
- adjudication
- decision delta
- lesson/reversal

## Promotion discipline

No prompt update from recurrence. A repair requires:
1. clean Neta failure or repeated surviving baseline-vs-Neta disadvantage;
2. hidden judgment stated;
3. neighboring non-fire case;
4. falsifiable gate;
5. deliberate positive control that turns red;
6. unseen HOLDOUT success after the smallest repair.

## Stop condition

Stop this program if:
- prompt changes mid-HOLDOUT;
- expected answers leak before freeze;
- new cases only repeat known outcomes without shrinking uncertainty;
- adjudication backlog makes results non-interpretable.
