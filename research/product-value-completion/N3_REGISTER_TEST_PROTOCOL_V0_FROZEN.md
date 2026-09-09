# N3 Register Test — protocol v0, FROZEN

Status: `FROZEN_BEFORE_RUN`
Frozen: 2026-09-06, before any reader saw any artifact.
Origin: `CAL-PRODUCT-VALUE-001` R&D synthesis, roadmap row `N3-REGISTER-TEST`, in `runtime/calibration_loop/traces/CAL-PRODUCT-VALUE-001-claude-cli.json`.

This protocol is written by the operator, not by a peer. It implements a row the runtime produced; it does not add to it.

## 1. Authorization

`O4-FIRST-EXTERNAL-CONTACT-AUTHORIZATION` was recorded as `NOT_DECIDED` by the synthesis and is **closed** by the OWNER on 2026-09-06: external contact with one artifact is authorized.

`O1-TARGET-WORKFLOW` remains `NOT_DECIDED` and is **not** required by this row. This probe deliberately asks nothing about buyers, workflows, pricing or preference.

## 2. What this test is for

It discriminates one of the three competing mechanisms Neta named for the absence of external value:

| Mechanism | Claim |
|---|---|
| M-A ACCESS | nothing external can reach the system at all |
| M-B LEGIBILITY / REGISTER | the artifacts demand that the reader already hold the vocabulary the product exists to help them discover |
| M-C JOB ABSENCE | there is no recurring external decision of this shape |

**Scope honesty.** This probe tests **M-B directly**. It bears on M-A only trivially, since handing over a file proves a file can be handed over. It says **nothing** about M-C, which is FIELD-owned and cannot be reached by a reading task. Any report claiming this probe settled M-C is void.

## 3. The reader

Admissible only if **all** hold:

1. not the OWNER;
2. not of the model lineage that produced or operated the artifacts, which for every artifact in this repository to date means not Anthropic Claude;
3. has not read this repository;
4. receives no orientation, glossary, framing or follow-up help.

A reader failing any of these produces an **instrument observation**, never a discrimination result. This is stated here, before the run, so a later pass cannot relabel one as the other.

## 4. Artifacts

Exactly one artifact per reader. Never both.

- **Artifact A** — `runtime/execution_traces/DEL-LICHESS-FIELD-INSTRUMENT-002.json`
- **Artifact B** — `runtime/calibration_loop/traces/CAL-ARCH-001-MANUAL-2026-09-05.md`

Both were verified before freezing to contain a decision and a reversal condition, so a failure cannot be attributed to an artifact that had nothing to find.

A is JSON with literal `statement` and `reversal_condition` keys. B is prose carrying the repository's idiom. A therefore permits a **key-scan confound**: a reader can quote the right strings without holding the meaning. Scoring records that confound separately rather than treating a quotation as comprehension.

Order: A first. B only under the repeat rule in section 8.

## 5. The question

Handed verbatim, with the artifact and nothing else:

> Read this document. In your own words: what decision was made, and what would reverse it?

No preamble, no glossary, no second question, no clarification if asked. It is not a preference survey, a usability interview or a satisfaction rating.

## 6. Scoring

Scored from the reader's answer alone.

| Item | STATED | PARTIAL | NOT_STATED |
|---|---|---|---|
| `DECISION` | restates what was decided, in the reader's own words | names the topic without the decision | absent or wrong |
| `REVERSAL` | states what would undo it | gestures at change without the condition | absent or wrong |
| `AUTHORITY` (secondary) | says who settles it | implies it | absent |

Flags recorded alongside:

- `KEY_SCAN` — the answer reproduces labelled field values without restatement;
- `VOCAB_IMPORT` — the answer uses repository idiom the document did not define;
- `OVERREACH` — the reader asserts facts the document does not contain.

**PASS** = `DECISION` STATED **and** `REVERSAL` STATED, with `KEY_SCAN` not set.
`AUTHORITY` is recorded but does not gate the result.

## 7. Pre-registered interpretation

Fixed before the run so the outcome cannot be reinterpreted after it is seen.

- **PASS** → weakens M-B. Supports Scaffold's `PACKAGE` alternative, that the durable record is itself the externally usable unit and needs no surface build. Roadmap effect: `X3-PACKAGE-THE-DURABLE-RECORD` is entered.
- **FAIL** → supports M-B. Legibility becomes the first product row, ahead of any surface, integration or capability work.
- **PASS with `KEY_SCAN` set** → inconclusive on M-B. Repeat on Artifact B, which has no scannable keys.

n = 1 in either direction. **No FIELD claim follows from this probe.** It changes which row the roadmap is ordered against; it does not establish comprehension, comparative improvement, repeat use or willingness to pay.

## 8. Repeat and void rules

Repeat **once**, on Artifact B, only if the failure is plausibly attributable to artifact selection rather than register, per the synthesis stop condition. Do not repeat to obtain a preferred outcome.

The run is **void** if the reader is coached past a failure, is asked follow-up questions, is shown the repository or the runtime, is shown both artifacts, or is told what the test is for.

## 9. What this can never establish

Comprehension by any population, comparative decision improvement, repeat use, willingness to pay, or that the claim contract differentiates this system from any competitor. It also cannot move `CONFIRMATORY_N`, which stays 0.
