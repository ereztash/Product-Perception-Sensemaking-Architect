# Applied Epistemology — Latent Inquiry Discovery v0

Status: `FROZEN_BEFORE_BASELINE · CONTROLLED_ADVERSARIAL · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06

## Capability under test

Does an explicit applied-epistemology inquiry rule add a material distinction beyond current R&D v0.2 by detecting that the current line of inquiry excludes a relevant evidence/mechanism/source class **without the prompt explicitly naming the missing class as the problem**?

Candidate challenger rule, frozen before baseline:

> **EXCLUDED_RELEVANCE_CHECK** — Before selecting a learning/evidence move, inspect whether the current inquiry frame has made some plausible evidence source, mechanism family, stakeholder, reality level, or alternative explanation effectively irrelevant. Expand the inquiry only when concrete cues in the current state make an excluded class capable of materially changing the decision. Do not broaden merely because other perspectives exist.

## Output contract per case

Return exactly:
- `route`: `PRESERVE_FRAME` or `EXPAND_INQUIRY`
- `controlling_uncertainty`
- `excluded_class`: null unless expanding
- `next_learning_move`
- `why`

## Cases

### LI-01 — compensation frame
A company wants to reduce first-year employee attrition. The working question is: “What salary increase would most reduce attrition?” Compensation bands are identical across five sites. Attrition is 8–11% in three sites and 31–35% in two sites. The two high-attrition sites also have much higher variation in shift changes and supervisor reassignment, but those variables have not been included in the planned salary study. The planned next step is a broad market-pay benchmark.

### LI-02 — UX engagement frame
A mobile product team wants to increase session depth. The working question is: “Which navigation redesign will make users explore more?” Session depth fell after the last release. The decline is concentrated on Android sessions that terminate within 30 seconds; iOS behavior is nearly unchanged. Crash/timeout telemetry exists but is not part of the UX review. The planned next step is a navigation concept test.

### LI-03 — content conversion frame
A B2B founder wants more booked calls from LinkedIn. The working question is: “Which content hook will produce higher-converting leads?” Profile visits and inbound messages are stable. Leads contacted within two hours book at 28%; leads first answered after 24 hours book at 4%. The content study excludes response-time and sales-process variables. The planned next step is to research viral hook patterns.

### LI-04 — training/adoption frame
An organization wants to increase use of an internal AI assistant. The working question is: “What training curriculum will increase adoption?” Team-level usage differs by more than 5x. Several low-use teams require manager approval for access and have many unactivated seats. The training plan does not include access/governance variables. The planned next step is to commission a training-needs survey.

### LI-05 — model-quality frame
A forecasting system’s benchmark accuracy has fallen. The working question is: “Which model/hyperparameter family should we try next?” Most new errors are concentrated in records created after a schema migration, and two important features have much higher missingness in the new data. The model-comparison plan assumes the dataset is comparable to the old benchmark. The planned next step is a larger model sweep.

### LI-06 — employer-brand frame
A nonprofit has trouble filling frontline roles. The working question is: “How should we improve employer branding to attract more candidates?” Application volume is already above target, but 63% of candidates abandon during a multi-step assessment and scheduling process before an interview. The planned research focuses on employer-brand messaging and candidate personas.

### LI-07 — bounded field preference control
Two onboarding screens implement the same already-validated flow and differ only in tone and visual treatment. The owner accepts either variant. The remaining decision is which one new users prefer and understand better. A five-user comparative field check can directly observe preference and comprehension.

### LI-08 — repo-state control
A production function now returns `None` for one input family. A reproducible unit test and stack trace identify the failing branch, and the live decision is whether the deployed code contains a particular guard condition. Repository/runtime inspection can close the claim directly.

### LI-09 — fixed artifact control
The owner has explicitly fixed the output as a single-file RTL HTML learning presentation. The unresolved question is which of two already-supported interaction patterns best fits the specified lesson. Both can be prototyped cheaply inside the fixed artifact constraint.

### LI-10 — bounded pricing evidence control
A SaaS company must choose between keeping the current price or rolling back a recent 15% increase. A randomized rollout already produced comparable cohorts with enough observation time; the relevant metrics are conversion, churn, and contribution margin, and the decision rule was frozen before the rollout. The next move is to read the completed experiment.

### LI-11 — direct authority control
The question is whether a feature flag is enabled in the currently deployed environment. The deployment platform exposes the flag state directly. No user-behavior or causal claim is being made.

### LI-12 — cheap discriminator control
A team is unsure whether users fail a workflow because the primary button is not noticed or because the label is misunderstood. A five-minute replay review can show whether eyes/cursors reach the button before abandonment. If they do, a second tiny label-comprehension probe becomes relevant; if not, it does not.

## Preregistered adjudication logic

A case counts as `EXPAND_INQUIRY` only if the current frame excludes a class whose inclusion can materially change the next decision/learning investment. Generic “consider other factors” does not count.

A case counts as `PRESERVE_FRAME` when the current claim is already bounded to the correct authority/mechanism/evidence family and expansion would add ceremony or broaden the hypothesis space without decision value.

Promotion signal requires both:
1. challenger catches latent inquiry exclusions missed by current R&D; and
2. challenger preserves the bounded controls instead of turning every task into frame expansion.

No retroactive repair to cases or rule is allowed after baseline begins.