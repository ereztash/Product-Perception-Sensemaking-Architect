# Applied / Zetetic Epistemology — Inquiry Audit v1

Status: `FROZEN_BEFORE_BASELINE · HARDER_CONTROLLED_CHALLENGE · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06

## Research question

Can an explicit inquiry-level epistemology rule improve R&D by detecting defects in the **guiding question / relevance structure / knower set** when there is no simple 'wrong bottleneck' cue?

## Challenger rule — frozen before baseline

`INQUIRY_QUESTION_AUDIT`

Before selecting evidence or a learning channel, inspect the guiding inquiry itself:

1. **QUESTION SOUNDNESS** — Does the current question admit answers that can actually resolve the live decision, or has it prematurely fixed the answer space / intervention family?
2. **ZETETIC RELEVANCE** — What information becomes relevant or irrelevant because the question is framed this way? Could an excluded class materially change the decision?
3. **KNOWER / ACCESS CHECK** — Does a source or actor have distinctive access to decision-relevant evidence that the current inquiry design systematically excludes?
4. **INQUIRY STATE** — Is the inquiry prematurely definite? If the candidate answer set is not earned, reopen/refine it before optimizing evidence inside it.

Do not broaden by default. Preserve bounded questions with legitimate authority and earned candidate sets.

## Output contract

- `question_state`: `SOUND_BOUNDED` / `PREMATURELY_DEFINITE` / `MISSING_RELEVANT_KNOWER` / `WRONG_RELEVANCE_STRUCTURE`
- `current_question`
- `repair_or_preserve`
- `next_learning_move`
- `material_decision_delta`

## Target cases

### ZI-01 — manager-generated candidate set
Goal: explain why internal AI adoption differs across teams. A management workshop produced three candidate explanations: lack of skill, lack of motivation, lack of time. The research plan will survey employees only on those three dimensions and choose the highest-scoring cause. No open-ended discovery step or behavioral evidence is planned.

### ZI-02 — successful-customer inquiry
Goal: learn why prospects choose the consulting service. The guiding question is “Which of our three strongest value propositions causes purchase?” The three propositions were derived from interviews with current satisfied clients. The decision will set outbound messaging for people who have never bought.

### ZI-03 — automation from supervisors
Goal: decide which support workflow should be automated first. Supervisors have mapped the process and scored each step for time cost. The planned inquiry will choose the highest-time step. Frontline agents execute the work but were not included because management believes the process map already captures the job.

### ZI-04 — incident inquiry from formal records
Goal: reduce repeated operational incidents. The inquiry asks “Which documented SOP violation causes the most incidents?” Incident reviews use ticket fields and formal postmortems only. Informal workarounds and near-misses are not captured in those systems, but the decision will redesign the operating procedure.

### ZI-05 — product learning from retained users
Goal: explain 30-day churn. The inquiry asks retained users which features create the most value and plans to strengthen the highest-rated feature. Churned users are not in the research sample because the team only has an in-product survey channel.

### ZI-06 — architecture choice from known options
Goal: choose an architecture for a new event-processing component. The team has listed Kafka, RabbitMQ and SQS because those are the technologies currently familiar to the engineers. The research plan compares only those three on throughput, cost and operational complexity. The owner has not mandated any of them.

## Neighbor controls

### ZI-07 — environment fact
Goal: determine whether the deployed service currently has a 30-second timeout. The environment configuration and runtime trace expose the timeout directly. The question is only about present deployed state.

### ZI-08 — owner intent
Goal: determine whether the product should use formal or conversational Hebrew in a specific owner-authored landing page. The owner explicitly states that this is a deliberate brand preference and asks only to implement it consistently.

### ZI-09 — earned experimental alternatives
Goal: choose between two onboarding variants. Prior work has already ruled out the competing mechanism families; both variants instantiate the same validated mechanism and differ only in execution. A preregistered field test with the target users is ready.

### ZI-10 — bounded legal fact
Goal: determine the filing deadline stated in a specific current regulation. The official legal text is identified and accessible. No claim is being made about fairness, impact or user experience.

### ZI-11 — direct historical record
Goal: determine whether a particular experiment was run before or after a specific commit. Repository history and the experiment trace contain timestamps and SHAs. The decision requires chronology only.

### ZI-12 — deliberate sample scope
Goal: estimate satisfaction among current paying enterprise customers, not former customers or prospects. The requested use is explicitly limited to current-customer account planning; the owner does not intend to generalize the result to acquisition or churn.

## Preregistered success criterion

The inquiry-audit challenger earns a capability signal only if it:
- produces a material repair on at least one target case that CURRENT_RND does not;
- does not reopen the bounded controls;
- identifies the **relevance/question/knower defect**, not merely says 'collect more evidence'.

Same-model manual comparison cannot establish independent validation; it can only reveal whether the explicit rule changes role-conditioned judgments.