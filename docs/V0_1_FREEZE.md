# v0.1 freeze — historical baseline

**Frozen at commit:** `b1dbfdda84305a81678a9c7998bccb5d4c98a948`  
**Canonical prompt blob:** `339b9a1be2fd0f1f6f6c7960e5be58e5566d3691`  
**Freeze date:** 2026-09-03

## Why this freeze exists

Neta v0.1 established a useful conversational method, but the Lessons re-foundation audit exposed a structural omission: evidence state, resolution authority, reality level and action permission were not first-class objects across the whole method.

The correct response is not to rewrite history or silently tune the prompt. v0.1 remains the baseline against which v0.2 capability changes must be demonstrated.

## Frozen artifacts

The commit above freezes the state of:

- `prompts/SYSTEM.md`
- `docs/TELOS.md`
- `docs/METHOD.md`
- `docs/AUTHORITY_MAP.md`
- `eval/RUBRIC.md`
- `fixtures/v0.1.md`
- `schemas/finding.schema.json`
- `scripts/validate_finding.py`
- Wave 1 preregistration and Evidence Pass 1 registers.

The v0.2 re-foundation may replace the *current* contract files, but the baseline remains recoverable from the frozen commit.

## Prompt freeze rule

`prompts/SYSTEM.md` is intentionally **not changed by this re-foundation**.

Research support, architectural elegance or Lessons lineage are insufficient reasons to alter behavior. A prompt change still requires:

1. a clean-model baseline run;
2. a demonstrated failure or blind spot;
3. identification of the missing hidden judgment;
4. the smallest candidate rule;
5. a neighboring behavior at risk;
6. a control fixture protecting that neighbor.

CI checks the Git blob hash of the prompt so the re-foundation cannot silently contaminate the baseline.

## What the freeze does not mean

It does not mean v0.1 is correct, complete or field-validated.

It means only that future improvement has a stable comparator and that failed ideas remain visible rather than being rewritten as if they had never existed.
