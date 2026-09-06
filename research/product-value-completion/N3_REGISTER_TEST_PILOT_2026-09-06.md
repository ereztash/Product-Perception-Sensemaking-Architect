# N3 Register Test — instrument pilot

Status: `INSTRUMENT_RUNNABLE / AWAITING_ADMISSIBLE_READER`
Discrimination result: **NONE PRODUCED**
Date: 2026-09-06
Protocol: `N3_REGISTER_TEST_PROTOCOL_V0_FROZEN.md`, frozen before any reader saw any artifact.

## 1. Why this is a pilot and not the test

`O4-FIRST-EXTERNAL-CONTACT-AUTHORIZATION` was closed by the OWNER, so authorization is no longer the blocker. A second requirement remains open, and it is the one that decides admissibility.

Protocol section 3 requires a reader who is **not of the model lineage that produced and operated the artifacts**. Neta stated the same constraint in its own limitations: run by the owner or by a same-lineage pass, the discriminator "yields nothing admissible".

This environment has one model CLI, Anthropic Claude, and no credential for any other provider. The owner is excluded by construction as the owner. So no admissible reader was reachable.

What was run instead is a **pilot of the instrument**: does the question get answered at all, does the rubric discriminate, and is either candidate artifact defective as a test item. That is the same state the repository already recognises elsewhere — `DEL-LICHESS-FIELD-INSTRUMENT-002` sits at "instrument runnable, awaiting participants".

**Nothing below discriminates M-A, M-B or M-C.** The roadmap is not reordered by it.

## 2. What ran

Two readers, one artifact each, fresh subprocess per reader, neutral working directory, all tools disabled, no repository access, no glossary, no follow-up. Each received the frozen question and one document, and nothing else.

Verbatim answers: `n3-register-test-pilot/READER_A.json`, `n3-register-test-pilot/READER_B.json`.

## 3. Scoring against the frozen rubric

| | Reader A — Artifact A (JSON) | Reader B — Artifact B (prose) |
|---|---|---|
| `DECISION` | STATED | STATED |
| `REVERSAL` | STATED | STATED |
| `AUTHORITY` (secondary) | STATED, named FIELD and the handback to REPO | PARTIAL, named no settling authority |
| `KEY_SCAN` | **SET** | not set |
| `VOCAB_IMPORT` | not set | not set |
| `OVERREACH` | not set | not set |
| Rubric result | **INCONCLUSIVE** — pass blocked by `KEY_SCAN` | PASS |

Reader A's reversal answer is a light paraphrase of the artifact's own `reversal_condition` string. Under the rule written before the run, that is the key-scan confound and not comprehension.

Reader B synthesised the decision across sections rather than from one field, generalised the reversal condition beyond its literal text, and volunteered the shared-model-lineage caveat unprompted.

Both answered in a single turn. Neither asked for clarification.

## 4. The instrument defect this pilot found

**Both candidate artifacts label the answer.** Artifact A carries a `reversal_condition` JSON key at line 13. Artifact B carries a `## Reversal condition` heading at line 233.

So the frozen question can be satisfied by locating a labelled field. Against a genuinely external reader the current instrument would therefore under-detect M-B: a reader who holds none of the vocabulary can still return a scoring answer by finding the label. The rubric's `KEY_SCAN` flag catches the crudest version of this and caught it on Reader A, but a fluent paraphraser would slip past it.

This is a defect in the test item, found before an admissible reader was spent on it. That is what a pilot is for.

## 5. Proposed amendment to v1 — a proposal, not applied

Protocol v0 stays frozen. Proposed for the next pass, for OWNER or the next runtime iteration to accept or reject:

1. Add a second question that no label answers: **"What would you need to know, that this document does not tell you, before acting on it?"** A reader holding the register can name the missing authority or the missing observation. A label-scanner cannot.
2. Prefer Artifact B as the primary item. Prose without a JSON key is the harder register test, and the pilot showed it produces the richer answer.
3. Keep `KEY_SCAN`, and add `LABEL_ADJACENT` for an answer that restates a labelled field without using anything else in the document.

Not self-applied. Amending a frozen protocol after seeing pilot output, without recording it as a proposal, is the failure this repository's freeze discipline exists to prevent.

## 6. What is still required

One reader who is not the OWNER, not Anthropic Claude, and has not read this repository. Handoff: `runtime/handoffs/HANDOFF-REGISTER-TEST-FIELD-001.json`. Execution record: `runtime/execution_traces/DEL-REGISTER-TEST-001.json`.

Two ways to reach one, both open to the OWNER and neither available from inside this session:

- hand the artifact and the one question to a person who fits the criteria, which is a ten-minute task;
- provision a credential for a non-Anthropic model, which would also restore the second lineage that `X1-INDEPENDENT-ADJUDICATION-CHANNEL` needs for four other blocked lanes.

`CONFIRMATORY_N` remains 0. No FIELD claim was established or advanced.
