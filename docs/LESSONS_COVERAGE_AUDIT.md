# LESSONS COVERAGE AUDIT — Neta re-foundation

This audit asks whether the load-bearing objects/principles from the Lessons re-foundation are actually represented in Neta's architecture. It is not a claim that every historical artifact in `lessons` should be copied.

Status meanings:

- `PRESENT` — first-class and operational in Neta v0.2.
- `PARTIAL` — represented but not yet strong enough to inherit the Lessons meaning.
- `MISSING` — absent before this re-foundation.
- `N/A` — intentionally not transferred.

## Object-model coverage

| Lessons object | Before | v0.2 | Neta implementation |
|---|---|---|---|
| Claim | PARTIAL | PRESENT | typed claim ledger in finding contract |
| Evidence | PARTIAL | PRESENT | evidence objects with provenance/type/reality |
| Reality level | MISSING | PRESENT | R0–R6 ladder + claim reality floor |
| Gate / falsifier | PRESENT | PRESENT | finding gate + CI controls |
| Positive control | PRESENT | PRESENT | deliberate invalid findings must go red |
| Resolution authority | PARTIAL | PRESENT | OWNER / REPO / ENVIRONMENT / RESEARCH / FIELD |
| Action permission | PARTIAL | PRESENT | requested use separated from ALLOW/DENY/DEFER |
| Reversal condition | PRESENT | PRESENT | required for build-ready work |
| Waiver | MISSING | PRESENT | explicit OWNER risk acceptance; cannot upgrade evidence |
| Field requirement | PARTIAL | PRESENT | required on FIELD_STOP |
| Failure lineage | PARTIAL | PRESENT | `docs/FAILURE_LINEAGE.md` |
| Policy | PARTIAL | PRESENT | assurance laws in thesis + RAP document |
| Lineage | PRESENT | PRESENT | portfolio lineage retained without universality claim |

## Method-principle coverage

| Principle | Before | v0.2 treatment |
|---|---|---|
| Evidence-or-defer | PRESENT | retained |
| Observation strength ≠ claim strength | PARTIAL | claim ledger makes this explicit |
| Evidence quality ≠ action authority | PARTIAL | permission is now separate object |
| Test reality must match claim reality | MISSING | reality floor is executable |
| User-facing claim cannot outrun measurement | PARTIAL | outcome/field claims blocked below R6 |
| Causal/outcome claims require higher authority | PARTIAL | OUTCOME → FIELD/R6 rule |
| Not measured ≠ zero | PRESENT | retained; insufficient reality is explicit |
| Gate must be demonstrated red | PRESENT | expanded from schema defects to epistemic defects |
| Fix should leave a gate | PARTIAL | failure-lineage contract now asks for one where recurrence matters |
| Ground truth must not reuse predictor | PARTIAL | retained as research/eval design law; still needs prospective Neta outcome study |
| Field outcome cannot be replaced by engineering | PRESENT | authority ceiling makes this central |
| Committed artifact ≠ current reality | PARTIAL | artifact authority map remains; environment claims require current environment evidence |
| Preregistration protects thresholds from rescue | PRESENT | Wave 1 freeze preserved; amendment logged |
| Contradictions are retained and may split concepts | PRESENT | research quarantine retained |
| External replication is different from literature support | PRESENT | G7 remains external use replication, not citation breadth |
| Stop when next uncertainty belongs to another authority | PARTIAL | promoted to Authority Ceiling |
| Encodability does not justify construction | MISSING | new encodability-bias gate |
| Unit of progress = uncertainty removed, not artifacts produced | PARTIAL | promoted to thesis |

## What is deliberately not inherited as a universal law

The following historical Lessons artifacts remain lineage/evidence, not Neta laws:

- Four-Feature repo-health classification;
- publish-button scoring;
- RepoHealth SaaS market assumptions;
- Genesis constraints as causal guarantees;
- any portfolio-specific tool cadence presented as universal;
- historical pricing/TAM/retention claims.

Their value is partly negative-control value: they show how a plausible signal can acquire more claim/action authority than the evidence earned.

## Remaining partials that require future evidence

### Ground-truth independence for Neta effectiveness
We do not yet have a prospective measure of “Neta improves design discrimination” that is independent of the rubric used to train Neta. That remains unresolved.

### External operator replication
No second owner-builder has yet demonstrated the method. No amount of research literature grants G7.

### Seven-lens completeness
The lens set remains a working decomposition, not an exhaustive taxonomy.

### Failure-to-gate yield
We have gate discipline, but we do not yet know what fraction of real Neta failures produce reusable, non-overfitted gates. That must be learned prospectively.

## Audit conclusion

The largest pre-v0.2 omission was not lack of UX knowledge. It was that **Reality, Authority and Permission were not first-class across every finding**.

That omission is now architecturally addressed. The next legitimate test is not more reading. It is whether the new assurance contract catches judgment errors that v0.1 allowed, while preserving useful v0.1 behavior.
