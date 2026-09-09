# Autonomous Mechanism Extraction — Stage 1 result

Status: `ADVANCE_TO_REPLICATION`
Date: 2026-09-09
Execution commit: `e9577055de06f3cf0e99d35351a546bab615801e`
GitHub Actions run: `34336648350`
Source: `ereztash/lichess_app@06828afbc1405a839dfc983a065bcb10109c5e02`

## Frozen decision rule

Advance if the structured arm exceeds the strong conventional baseline by at least 2.0 GOLD_RECALL_POINTS, has no source-isolation violation, and does not add more than one unsupported mechanism.

## Blind score before mapping

| Candidate | Gold recall | Unsupported | Invalid evidence paths | Leakage |
|---|---:|---:|---:|---:|
| candidate-1 | 3.0 / 8 | 0 median | 0 | 0 |
| candidate-2 | 6.5 / 8 | 0 median | 0 | 0 |

Per-target medians:

- candidate-1: G1=1, G2=0, G3=0, G4=0, G5=1, G6=.5, G7=.5, G8=0.
- candidate-2: G1=.5, G2=1, G3=1, G4=1, G5=1, G6=.5, G7=.5, G8=1.

## Mapping

- candidate-1 = Arm B, strong conventional reverse-engineering baseline.
- candidate-2 = Arm S, structured mechanism-extraction protocol.

Observed advantage: **+3.5 GOLD_RECALL_POINTS** for Arm S.

Both outputs were valid JSON, within the 12-item cap, cited only existing sanitized production-code paths, and contained no README/docs/tests/research path leakage.

## Decision

`ADVANCE_TO_REPLICATION`

Stage 1 does **not** authorize BUILD.

## Important validity threat

The structured protocol was designed after prior work on `lichess_app`. Its decomposition explicitly asks about state, authority, evidence boundaries, action derivation and persistence — categories that overlap the independently documented gold of this source. Therefore Stage 1 may measure protocol fit to a familiar source rather than general reverse-engineering value.

The next discriminating test is out-of-sample replication with the structured prompt frozen unchanged on source systems that did not contribute to its design. A failure there should reverse any temptation to build an extractor from this result alone.
