# AUTHORITY MAP — one authority per question

This file is the authority for **which artifact answers which question** in Neta v0.1.

| Question | Authority | What is not the authority |
|---|---|---|
| Why does Neta exist? | `docs/TELOS.md` | README slogans |
| How does Neta reason from a raw feeling? | `docs/METHOD.md` | examples in fixtures |
| What behavior must a clean model follow? | `prompts/SYSTEM.md` | this map or README |
| What shape is a build-ready finding allowed to have? | `schemas/finding.schema.json` + `scripts/validate_finding.py` | prose examples |
| How is Neta evaluated? | `eval/RUBRIC.md` | self-description in the prompt |
| Which cases currently exercise the method? | `fixtures/v0.1.md` | anecdotes outside the repo |
| What has Neta learned about Erez's private design vocabulary? | `memory/owner-language.yaml` | a permanent definition of his phrases |
| Where did the method's principles come from? | `docs/LINEAGE.md` | claims that they are universal laws |
| Does the contract actually reject bad output? | CI + `scripts/check_contract.py` | presence of a validator file |

## Questions with deliberately no authority yet

| Question | Why unresolved | What would create authority |
|---|---|---|
| Does Neta improve Erez's design discrimination over time? | no prospective before/after evidence | repeated sessions with blinded or preregistered transfer checks |
| Does the method work for another owner-builder? | current design is personalized to one operator | external replication with a second operator |
| Are the seven lenses complete? | they are a useful decomposition, not a validated exhaustive taxonomy | repeated failure analysis showing stable coverage or a revised taxonomy |
| Which model/provider is best for Neta? | no comparative runs | same fixtures across clean model surfaces |
| Should Neta have a UI? | method has not earned one | conversational method passes fixtures and real sessions reveal a UI-specific need |

## Rule

If two artifacts answer the same question differently, the file named here wins and the disagreement is a defect.

A remembered phrase is never evidence by itself. A fixture is never proof of field behavior. A passing check is never proof that a human will understand the result.
