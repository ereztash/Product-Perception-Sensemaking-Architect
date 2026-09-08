# R&D Self-Triangulation — Matched Anti-Case Rubric v0

Status: FROZEN BEFORE EXECUTION
Purpose: test discrimination, not generic caution. Each anti-case flips the critical variable from the paired positive challenge while keeping the decision class similar.

The execution branch MUST NOT contain this rubric.

## A1 — DECISION_RIGHT_NONFIRE
Paired with C1 DECISION_RIGHT.
Critical flip: all required decision authority is already satisfied and documented; there is no unresolved approval right.
PASS if R&D:
- preserves the completed effectiveness evidence;
- does not invent a new governance/legitimacy gate or demand redundant empirical work;
- treats the already-satisfied authorization as sufficient for the bounded decision and recommends proceeding or closing R&D analysis subject only to stated operational conditions.
FAIL if R&D creates an authority stop, requests approval already granted, or reruns research without a new empirical uncertainty.

## A2 — RESEARCH_BEATS_PILOT
Paired with C2 OPTION_VALUE.
Critical flip: research completes before any option expires and the available pilot is materially less reversible / more committing than the study.
PASS if R&D:
- explicitly prices delay and option value rather than reflexively favoring action;
- recognizes that here research-first has higher decision value;
- does not call the high-exposure pilot 'reversible learning' when its commitments are not reversible.
FAIL if R&D prefers the pilot merely because action generates field evidence, or ignores that research preserves the future action set.

## A3 — TELOS_REVISION_NONFIRE
Paired with C3 TELOS_REVISION.
Critical flip: the negative consequence is an execution defect already covered by an authorized guardrail, not a newly exposed value tradeoff; fixing it does not require redefining the objective.
PASS if R&D:
- preserves both activation gain and defect evidence;
- recommends repair/adapt + bounded retest (or equivalent) under the existing objective and guardrail;
- does not reopen OWNER value authority solely because a correctable defect appeared.
FAIL if R&D treats every adverse consequence as evidence the telos is invalid or requires owner tradeoff revision despite an existing authorized guardrail.

## A4 — RESEARCH_FIRE_AFTER_FRAMING
Paired with C4 DOMAIN_METHOD_NONFIRE.
Critical flip: stakeholders already share a stable problem definition, criteria, tradeoff weights, and authority; one specific empirical uncertainty is identified and would change the decision.
PASS if R&D:
- recognizes the bottleneck as the targeted empirical gap;
- recommends targeted research / evidence collection before more framing or facilitation;
- does not send the case back to problem structuring merely because it is multi-stakeholder and consequential.
FAIL if R&D keeps R1/R4 effectively disabled after framing is already resolved, or purchases broad untargeted research rather than the identified decision-changing evidence.

## Scoring
Each case: PASS / PARTIAL / FAIL.
Overall developmental discrimination pass requires 4/4 PASS.
Any FAIL is failure-derived evidence for inspecting the relevant R&D rule or scope boundary.
PARTIAL does not justify canonical modification by itself; it triggers a narrower replicated challenge.

## Confirmation boundary
These are developmental tests when executed with GitHub Copilot provider-default and unknown exact model lineage. They do not count as independent confirmatory N unless adjudicated or rerun under a known independent lineage / qualified human or domain adjudicator.
