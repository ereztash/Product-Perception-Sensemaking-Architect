# External GitHub Scope Test — Batch 01 Frozen Outputs

Status: `EXTERNAL_OUTCOME_TEST · CASES_AND_OUTPUTS_FROZEN_BEFORE_RESOLUTION_READ · SAME_MODEL_ROLE_CONDITIONED_OUTPUTS · NOT_95PCT_CONFIRMATION`
Date: 2026-09-06
Scope map: `RND_SCOPE_MAP_V0_2_FROZEN_FOR_CONFIRMATION.md`

Purpose: test the frozen R&D scope boundary against external natural engineering issues whose eventual maintainer resolution has not yet been read in this run.

Important limits:
- Issue bodies are external/natural.
- Baseline and R&D outputs below are same-model role-conditioned, not independent model executions.
- External maintainer outcome may adjudicate directional fit, but this batch does not satisfy the frozen 95% confirmation requirement by itself.

## Frozen cases and predictions

### EXT-01 — microsoft/vscode#325111
Issue: performance regression after 1.127 -> 1.128; extensions disabled; rollback restores performance.
Pre-outcome region: `R2_OBVIOUS_LEARNING_NEIGHBOR`.

**Strong baseline output (frozen):**
Treat as a version regression. First search/merge duplicates and collect a VS Code performance profile on 1.128 vs 1.127 or a nearby Insiders build; if reproducible, bisect/narrow the build/commit range before proposing a fix.

**R&D output (frozen):**
Full R&D should bypass. A cheap legitimate discriminator already dominates: known-issue/duplicate recovery plus controlled profile/bisect across versions. Do that first; escalate to broader learning only if the regression cannot be localized.

Predicted material delta: `TIE / no full-R&D value`.

### EXT-02 — Z3Prover/z3#10645
Issue: one benchmark goes from ~1.25s to ~47s between adjacent commits, later times out.
Pre-outcome region: `R2_OBVIOUS_LEARNING_NEIGHBOR`.

**Strong baseline output (frozen):**
Reproduce the attached SMT case on the two adjacent commits, profile the regression, and inspect/bisect around `c56b2cb`, which is already the first known bad commit. Minimize the SMT case if needed before changing solver heuristics.

**R&D output (frozen):**
Bypass full R&D. The issue already supplies a high-value discriminator: adjacent good/bad commits plus a reproducible artifact. The next move is direct repo/performance diagnosis, not research allocation.

Predicted material delta: `TIE / no full-R&D value`.

### EXT-03 — microsoft/winappCli#729
Issue: flaky cancellation/process-tree test on unrelated PRs; likely fixed-delay/timeout sensitivity under CI load.
Pre-outcome region: `R2_OBVIOUS_LEARNING_NEIGHBOR`.

**Strong baseline output (frozen):**
Inspect the test's fixed wait/timeout and child-process lifecycle; reproduce under loaded/slow conditions and replace timing assumptions with deterministic waiting on process exit/PID disappearance if confirmed.

**R&D output (frozen):**
Full R&D should bypass. There is one cheap direct discriminator: instrument/wait on child-process lifetime under CI-like load. If that confirms timeout sensitivity, make teardown synchronization deterministic.

Predicted material delta: `TIE / no full-R&D value`.

### EXT-04 — github/gh-aw#53729
Issue: five unrelated benchmarks regress simultaneously, no relevant code change, tiny iteration count, long history gap; environment noise suspected.
Pre-outcome region: `R2_OBVIOUS_LEARNING_NEIGHBOR`.

**Strong baseline output (frozen):**
Re-run on a quieter/dedicated runner before investigating code. If the slowdown disappears, treat it as runner noise; then harden the benchmark by increasing sampling/benchtime and verify the missing daily-history runs separately.

**R&D output (frozen):**
Bypass full R&D. The issue already names the cheapest decision-changing test: controlled rerun on a quieter/dedicated runner. Do not spend code-investigation effort until that discriminator fails.

Predicted material delta: `TIE / no full-R&D value`.

### EXT-05 — apache/beam#39010
Issue: automated performance alert with one anomalous runtime point amid a noisy recent series and a documented triage procedure.
Pre-outcome region: `R3_DIRECT_AUTHORITY_OR_EXECUTION` (documented performance-alert triage owns next step).

**Strong baseline output (frozen):**
Follow the repository's performance-alert triage procedure, inspect subsequent runs/dashboard and relevant changes around the anomaly; do not infer a code regression from a single point without reproduction.

**R&D output (frozen):**
Route to the existing performance-alert procedure/maintainer authority. There is no separate nontrivial learning-allocation problem yet; full R&D adds ceremony unless triage produces competing evidence paths.

Predicted material delta: `TIE / no full-R&D value`.

### EXT-06 — checkstyle/checkstyle#20818
Issue: performance-regression CI fails frequently; options include manual trigger, changing threshold/sampling, or making testing more stable.
Pre-outcome region: `R1_EPISTEMIC_ALLOCATION_CORE`.

**Strong baseline output (frozen):**
Likely reduce false positives by either making the workflow manual/conditional for performance-sensitive changes or increasing repetitions and loosening/stabilizing the threshold. Review recent failures before choosing.

**R&D output (frozen):**
Do not choose manual-trigger vs threshold vs more repetitions yet. First define the decision the check protects (catching real regressions before merge) and estimate two quantities from recent history: false-positive frequency and known/estimated miss risk. Then compare at least three learning/intervention paths: (1) stabilize execution environment/statistics, (2) scope/conditional trigger by change type, (3) manual mentor trigger. Choose the cheapest design that preserves required detection sensitivity. A manual-only switch may remove noise by removing measurement rather than improving it.

Predicted material delta: `MATERIAL_RND_WIN candidate`.

### EXT-07 — paperclipai/paperclip#4328
Issue: intermittent blocked-state/comment inconsistency; swallowed errors hide whether failure is upstream state/race vs post-transaction comment failure; proposed fixes differ materially.
Pre-outcome region: `R1_EPISTEMIC_ALLOCATION_CORE`.

**Strong baseline output (frozen):**
Add logging around swallowed `releaseIssueExecutionAndPromote` errors, reproduce under CI-like concurrency, and likely make blocked status + comment atomic in one transaction; avoid merely waiting longer in the test unless production semantics are intentionally asynchronous.

**R&D output (frozen):**
Do not commit first to transactional rewrite or test polling because the two candidate mechanisms imply different fixes. Buy the cheapest discriminator first: narrow the swallowed-error surface and log the exact branch/exception plus retryReason/comment outcome in a stress/CI-like reproduction. If status commits and `addComment` fails, transactionality is earned; if the blocked branch was never legitimately selected, fix upstream state/classification instead. Test polling is only justified if production semantics explicitly permit status-before-comment visibility.

Predicted material delta: `MATERIAL_RND_WIN candidate`, mainly by preserving mechanism-dependent branching before production change.

### EXT-08 — apache/pulsar#24628
Issue: flaky load-manager close test with concrete stack trace in TableView/load-data store during shutdown lifecycle.
Pre-outcome region: `R4_DOMAIN_METHOD_PRIMARY` / direct engineering diagnosis.

**Strong baseline output (frozen):**
Reproduce the close/load ordering race, inspect the TableView/load-data-store lifecycle around shutdown, and make the test/implementation synchronize on closure or guard the lookup against the closed/null state based on intended semantics.

**R&D output (frozen):**
Engineering/domain debugging is primary. R&D should not replace it. Invoke full R&D only if several materially different diagnostic routes compete and the team cannot tell which evidence is worth acquiring first.

Predicted material delta: `TIE / domain-method primary`.

## Frozen aggregate prediction

- R1 candidates: EXT-06, EXT-07 (2)
- R2: EXT-01, EXT-02, EXT-03, EXT-04 (4)
- R3: EXT-05 (1)
- R4: EXT-08 (1)
- R5: none

Expected scope behavior:
- R1: R&D should outperform a strong direct baseline on decision-path quality.
- R2/R3/R4: R&D should mostly bypass/handoff and not claim a material reasoning advantage.

Next step after this commit: read external maintainer comments / linked PR resolution and score directional fit without changing any frozen output above.