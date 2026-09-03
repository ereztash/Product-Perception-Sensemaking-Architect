# Wave 1 amendments

## 2026-09-03 23:28 +03:00 — protocol defect: authority semantics were not first-class

### Exact area affected

Cross-cutting interpretation of `research/WAVE1_PREREGISTRATION.md`, especially:

- W7's `permission/authority` distinction;
- promotion-state semantics;
- the relationship between G/C/A/O and downstream Neta action.

### Old rule / implementation

The preregistration correctly stated that G/C/A/O are separate evidence coordinates and that research promotion is not a probability of truth. `PROMOTION_PROTOCOL.md` also stated that promotion answers what Neta is allowed to do with a research claim.

However, the operational architecture did not make the following first-class for **every design finding**:

- claim reality floor;
- resolution authority;
- requested downstream use;
- explicit `ALLOW / DENY / DEFER` permission.

As a result, authority semantics risked being treated as one research topic (especially W7) rather than as constitutional structure across all capabilities.

### New rule

Neta v0.2 adds a prospective assurance overlay:

```text
Claim
→ Evidence
→ Reality
→ Resolution Authority
→ Requested Use
→ Permission
```

This overlay is defined in:

- `docs/NETA_ASSURANCE_THESIS.md`
- `docs/REALITY_AUTHORITY_PERMISSION.md`
- `research/WAVE1_ASSURANCE_REVIEW.md`

### Reason

A manual end-to-end reading of the Lessons repository showed that its re-foundation had already separated claim/evidence/reality/authority/action more deeply than Neta's initial port. The prior Neta architecture imported many Lessons mechanisms but incompletely imported this constitutional layer.

### Was relevant source/result already seen?

**Yes.** Wave 1 source collection had begun and Evidence Pass 1 results were already visible. Therefore the new rule **must not** be used to move old thresholds, rescue a favored claim, or rewrite original G/C/A/O/status assignments.

### Contamination / exclusions

- No existing Wave 1 claim is retroactively promoted or demoted by v0.2.
- `research/WAVE1_PREREGISTRATION.md` is not edited.
- `research/registers/claims.json` is not rewritten to fit the new schema.
- Evidence Pass 1 remains interpretable under the rules that existed when it was collected.
- v0.2 authority/reality/permission rules apply prospectively to clean-model evaluation, future findings and any future prompt-change decision.

### Prompt contamination protection

`prompts/SYSTEM.md` remains frozen at its v0.1 blob. The v0.2 re-foundation does not itself authorize a prompt edit.

---

## Rule for future amendments

Once `research/registers/claims.json` has `source_collection_started: true`, any substantive change to the preregistered research protocol must be logged here **before** it is used.

Each amendment must record:

- date/time;
- exact section changed;
- old rule;
- new rule;
- reason;
- whether any source/result had already been seen that bears on the change;
- which claims/runs are excluded because of contamination.

An amendment may clarify ambiguity. It may not silently move a threshold to rescue a favored result.
