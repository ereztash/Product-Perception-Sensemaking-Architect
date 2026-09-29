# Calibration Loop gate-yield audit — 2026-09-29

Status: `INCONCLUSIVE` — the routing gate never received discriminating input, so it could neither save nor fail to save model calls.

Raw evidence: `runtime/calibration_loop/traces/preflight-2026-09/` (13 traces copied verbatim from GitHub Actions artifacts `rnd-trace-<sha>`, which expire 2026-12-15 … 2026-12-19).

## Question and claim identity

Material question:

> Can the deterministic gates in the Calibration Loop reduce model invocations per calibration decision without losing decision state?

Claim `C-GATE-AI-REDUCTION` is a **new claim**, not a narrowing of an earlier one.

Lineage: the mechanism-transfer experiments ended in `STOP_*_UNIQUE_DELTA_UNSHOWN` (structured / executable contracts did not beat an information-matched strong baseline on output quality). That result stays as recorded. The present claim measures a different construct (model-call cost at matched decision state), carries its own evidence burden under A2 of `research/RND_AGENT_AMENDMENT_V0_2_1.md`, and cannot be cited as support for the parent quality claim.

The executable-contract result explicitly left "repeated unattended verification" open as a separate regime (`research/mechanism-transfer/executable-contract/RESULT_STAGE1_2026-09-09.md`). This audit is the first observation in that regime.

Resolution authority for what happened in the runs: `REPO` (traces). Whether gating can reduce model use: `RESEARCH`.

## Inventory — all 22 runs of `rnd-deep-research-preflight.yml`

| Runs | Outcome | Model output produced? | Evidence |
|---|---|---|---|
| 1–10 | `FAILED` before any model output | No | Run 3 log: `OPENAI_API_KEY` empty, exit before trace. Run 10 trace: GitHub Models HTTP 410 retirement brownout. Runs 1–2, 4–9 not inspected individually; all ≤ 12 s wall-clock. |
| 11 | `FAILED_EXECUTION` | Yes, rejected | R&D adapter timed out |
| 12 | `FAILED_EXECUTION` | Yes, rejected | `candidate_moves[0] values must be non-empty strings` |
| 13 | `FAILED_EXECUTION` | Yes, rejected | DIAGNOSE returned non-JSON |
| 14 | `FAILED_EXECUTION` | Yes, rejected | NETA semantic fields drift |
| 15, 16 | `FAILED_EXECUTION` | Yes, rejected | SYNTHESIZE returned non-JSON (DIAGNOSE and peers had already run) |
| 17–21 (+ run 20 attempt 1) | `COMPLETE` | Yes | 6 traces |
| 22 | `AUTHORITY_STOP` | Yes | 1 trace |

Model identity: every trace that records it shows `ollama-local` with `qwen2.5:3b-instruct` (run 17: `qwen2.5:1.5b-instruct`). R&D DIAGNOSE / SYNTHESIZE calls carry no `_adapter_meta` in the trace, so their model identity is inferred from the workflow config at each commit, not recorded. The configured strong model (`gpt-5.6-sol`) never ran: no OpenAI key was present.

## Findings on the 7 successful traces

26 model calls in total (7 × DIAGNOSE, 12 peer calls, 7 × SYNTHESIZE). Peer calls consumed 39,038 prompt tokens and 3,448 output tokens; R&D token counts were not recorded.

### F1 — routing input saturated

In 7/7 traces DIAGNOSE set **all 12** `needs` flags to `true`.

`routing.py` is deterministic, but with saturated input its output is constant: invoke every allowed peer and hand off to every authority. The gate therefore carried zero bits from the diagnosis and saved zero peer calls.

This is the same failure class recorded in `research/GATE_RELIABILITY.md`: a gate that exists but cannot observe the state it claims to act on.

The only zero-peer run (22) came from the task file (`allowed_resources: ["RND"]`), not from the diagnosis; SYNTHESIZE still ran.

### F2 — materiality check measures non-emptiness, not change

- 10/12 peer calls were labelled `material=true`.
- In 8 of those 10, the same sentence was copied into several delta dimensions (e.g. identical `decision` and `action` text; in run 17 one sentence fills five dimensions).
- 6/12 peer calls had an all-false `expected_delta`; 5 of those 6 were still labelled material. Nothing flagged the mismatch.
- In 2 runs NETA and SCAFFOLD returned an identical `decision` sentence.

`run.py` derives `material` from "at least one non-null field". Under these outputs `Neta Yield` would be inflated and cannot be computed from these traces.

### F3 — where the deterministic gates did work

- Runs 1–10 stopped before any model output (no key / provider unavailable).
- Runs 11–16 spent model calls, and deterministic validators rejected the malformed output (timeout, non-JSON ×3, empty field, schema drift). Nothing malformed was deposited and no second model was needed to judge it. The calls were already spent.

## Disposition

`C-GATE-AI-REDUCTION`: `INCONCLUSIVE`.

This is not a refutation. The routing gate was never given input that allowed a decision, so its capacity to reduce calls is untested.

## Next discriminating step (authorized by owner 2026-09-29)

Deterministic validator changes only, no new capability:

1. Reject a diagnosis whose `needs` are saturated (every flag `true`).
2. Reject an `observed_delta` that repeats identical text across dimensions, and mark in the trace every peer invocation whose ex-ante `expected_delta` was all-false but whose observed result is material.

Counterfactual on the archived traces: all 7 successful runs would stop after DIAGNOSE, i.e. 7 model calls instead of 26.

Implemented 2026-09-29 in `runtime/calibration_loop/run.py`, with synthetic and archived-trace positive controls in `scripts/check_calibration_loop.py`. The DIAGNOSE instruction sent to the model was deliberately **not** changed in the same step, so the re-run measures the gate alone; telling the model about the saturation rule is a separate, later intervention.

Then re-run 2 existing tasks on the same model.

## Reversal conditions

- If, after the validators are enforced, DIAGNOSE still cannot produce non-saturated `needs` on this model (runs simply fail at DIAGNOSE), routing-based reduction is not reachable with this model: stop, and do not add further routing machinery.
- If `needs` become discriminating across tasks, measure peer calls saved per task at unchanged `decision_after` / `next_move`.
- If a strong model on a well-scoped task legitimately needs all 12 flags and an independent adjudicator agrees, the saturation rule must be revisited rather than bypassed.
- All findings above are bounded to 1.5B/3B local models. A strong-model run that produces discriminating `needs` without the new validators would re-attribute F1 to model capacity rather than gate design.
