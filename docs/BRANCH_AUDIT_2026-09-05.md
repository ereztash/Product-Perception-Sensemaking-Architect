# Branch Audit — 2026-09-05

This audit classifies every current branch against `main` after canonical consolidation.

## Canonical rule

`main` is the only released source of truth. A branch may remain only when it preserves unique historical evidence that has not yet been migrated safely.

## Disposition

| Branch | Disposition | Reason |
|---|---|---|
| `main` | KEEP_CANONICAL | Current source of truth. |
| `neta/design-research-spine-v0.1` | MERGED_SAFE_TO_DELETE | PR #8 merged into `main`; no unique released content should remain authoritative on the branch. |
| `neta/github-benchmark-v1` | MERGED_SAFE_TO_DELETE | Benchmark protocol already merged; branch is fully behind `main`. |
| `neta/hebrew-observatory` | MERGED_SAFE_TO_DELETE | H2 Reader Effect observatory merged into `main`; branch is fully behind. |
| `neta/hebrew-signal-fidelity` | MERGED_SAFE_TO_DELETE | H1 Signal Fidelity benchmark merged into `main`; branch is fully behind. |
| `neta/oss-observatory` | MERGED_ARCHIVE_OPTIONAL | BATCH-001..016, closeout and canonical state are now in `main`; retain only if branch-level execution history is operationally useful. |
| `neta/v0.1-agent-contract` | MERGED_SAFE_TO_DELETE | PR #1 merged. The frozen `prompts/SYSTEM.md` blob is identical to `main` (`339b9a1be2fd0f1f6f6c7960e5be58e5566d3691`). Git history preserves lineage without requiring the branch. |
| `refoundation/neta-assurance-v0.2` | MERGED_SAFE_TO_DELETE | Assurance re-foundation merged; branch is fully behind. |
| `research/wave1-triangulation` | MERGED_SAFE_TO_DELETE | Preregistered research-wave material merged; branch is fully behind. |
| `research/wave1-evidence-pass1` | KEEP_ARCHIVE_UNTIL_MIGRATED | Contains four post-merge historical commits absent from `main`: `PROMPT_GAP_AUDIT.md`, `RECURSION_LOG.md`, `WAVE1_RESULTS_PASS1.md`, and a stronger historical research-contract gate. PR #11 was intentionally closed rather than forcing an unsafe old-branch merge. |

## Cleanup target

The minimal branch set after deletion should be:

1. `main`
2. `research/wave1-evidence-pass1` temporarily, until its unique historical tail is migrated or deliberately retired.
3. Optionally `neta/oss-observatory` only if preserving the execution branch itself has operational value; its evidence is already canonical in `main`.

## Safety rule

Never delete a branch merely because its PR is closed or merged. First verify either:

- `ahead_by = 0` against `main`, or
- all unique content has been explicitly migrated and lineage recorded.

Branch deletion itself is repository hygiene, not evidence deletion: merged commits remain in Git history.