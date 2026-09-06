# R&D Self-Scope Discovery Task — 2026-09-06

Status: `FROZEN_SELF_CALIBRATION_TASK · NOT_CANONICAL`

## Owner goal

Design a research program that identifies the boundaries within which the R&D Agent produces the highest material decision value.

The program must not stop because the agent feels confident. It may stop only when a prespecified evidential criterion supports the boundary claims with at least 95% statistical confidence / anytime-valid coverage.

## Live decision

What is the narrowest defensible operating scope for R&D such that:

1. inside the scope, invoking R&D repeatedly adds material decision value over a strong baseline;
2. outside the scope, R&D is bypassed or routed to the correct peer/authority with low false-invocation burden;
3. the scope does not absorb OWNER, Neta, Orchestrator, REPO, ENVIRONMENT or FIELD authority;
4. the scope generalizes across domains and across pre-learning, mid-learning and post-learning phases;
5. the result is supported by independent evidence, not same-model agreement.

## Current candidate telos

> **R&D exists to calibrate inquiry/learning effort to the uncertainty that can still change a consequential decision.**

This is a hypothesis, not a canonical truth.

## Known evidence / constraints

- Current v0.2 telos is broader: resource↔telos calibration.
- Narrow commitment-only telos was directionally useful but missed a reusable epistemic-policy case.
- Peer review with Neta separated FIRE condition from invariant telos.
- Applied/zetetic epistemology and VOI challengers produced theoretical convergence but no unique next-move delta in same-model manual ablations.
- Existing eval protocol forbids same-model self-critique from counting as independent corroboration and forbids a single subjective score.
- Current runtime cannot execute live OpenAI adapters in this environment because `OPENAI_API_KEY` is absent.

## Required output from R&D

Design the smallest sequential research program capable of discovering and validating a scope boundary.

The program must specify:

### A. Scope representation
Define an orthogonal-enough feature space / taxonomy for classifying tasks before outcome is known. Avoid a list of examples masquerading as a boundary.

At minimum consider whether the following are true dimensions, derived features, or should be rejected:
- consequentiality of the live decision;
- whether uncertainty can materially change the decision;
- whether choosing **whether / how / how much** to learn is nontrivial;
- evidence/authority ambiguity;
- inquiry-frame quality;
- pre-learning / mid-learning / post-learning phase;
- one-off vs reusable epistemic policy;
- reversibility / cost / delay / contamination;
- product-signal discrimination (Neta boundary);
- direct state/reality authority (REPO / ENVIRONMENT / FIELD);
- settled OWNER intent;
- pure execution / coordination.

### B. Baselines and comparators
At least:
1. strong direct general model / local response policy without R&D doctrine;
2. current R&D;
3. any narrower candidate gate/telos that emerges;
4. Neta or direct authority only where that is the legitimate alternative.

### C. Outcome unit
Define `MATERIAL_RND_DELTA` at case level. Agreement, verbosity, better terminology or a nicer explanation do not count.

Candidate definition to challenge:
> R&D materially changes the next justified decision path by changing what uncertainty is pursued, which evidence/authority is used, how much learning is bought, the claim state, or whether the system continues/stops — and the change survives independent adjudication.

Track harm / delay / authority violation separately.

### D. Discovery vs confirmation
Separate adaptive discovery from confirmatory holdout. Cases used to invent a boundary cannot validate it.

### E. Corpus lanes
Use multiple natural domains and include adversarial neighbors. Include historical natural tasks only as discovery unless they were genuinely unseen at freeze time. Require prospective / independently frozen transfer before promotion.

### F. 95% stopping rule
The owner requests >95% certainty. Operationalize this without fake precision.

The program should use a sequentially valid method because sampling continues until the criterion is reached. Confidence sequences / sequential tests are admissible. Ordinary fixed-N intervals cannot be repeatedly peeked at and treated as valid stopping evidence.

At minimum define:
- which scalar or vector claims receive 95% coverage;
- minimum effect / quality thresholds, not merely `p > 0`;
- minimum independent sample counts per critical boundary family;
- what happens when evidence remains inconclusive indefinitely;
- multiplicity / familywise risk across multiple scope cells;
- independence requirements for adjudication and model lineage.

### G. Boundary output
The final artifact must classify at least:
- HIGH-VALUE CORE;
- CONDITIONAL / ROUTE-DEPENDENT;
- LOW/NO-VALUE — BYPASS;
- WRONG AUTHORITY — HANDOFF;
- UNKNOWN / INSUFFICIENT EVIDENCE.

### H. Anti-self-confirmation controls
The program must actively try to falsify the candidate telos and discover cases where:
- R&D fires but adds nothing;
- R&D delays an obvious cheap action;
- R&D opens a sound bounded inquiry unnecessarily;
- R&D duplicates Neta or an authority;
- R&D misses a material learning-allocation decision;
- R&D's own taxonomy causes the apparent win.

## Statistical references allowed as methodology scaffolds

- Howard, Ramdas, McAuliffe & Sekhon (2021), time-uniform confidence sequences: sequential intervals valid over an unbounded time horizon.
- NIST binomial proportion confidence interval guidance (Wilson / related methods) for fixed summaries and sanity checks.
- Wald-style sequential testing as a conceptual reference, but do not force simple i.i.d. assumptions onto heterogeneous task families without justification.

## Current execution label

Any output generated in this environment is:
`ROLE_CONDITIONED_MANUAL_RND_RUN · REPO_GROUNDED · NOT_RUNTIME_EXECUTION`

## Stop rule for this design task

Do not stop merely with a verbal telos. Stop only when a concrete executable protocol exists that, if run with independent cases/judges, can either:
1. establish a bounded >95%-supported scope claim; or
2. remain explicitly `INCONCLUSIVE` because the required independent evidence is not currently obtainable.
