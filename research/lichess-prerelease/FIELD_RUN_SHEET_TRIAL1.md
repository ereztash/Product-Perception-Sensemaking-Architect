# Trial 1 run sheet, first cohort

Status: `OPERATIONAL_HANDOFF, FIELD`

This sheet adds no protocol. Every rule below is already frozen in `ereztash/lichess_app`, and this
page exists only so the first cohort can be recruited without reading three documents first. Where
this sheet and a frozen document disagree, **the frozen document wins**.

| authority | document |
| --- | --- |
| what may not move during the trial | `docs/ACQUISITION_PROTOCOL_V1.md`, sections 1 to 6, frozen 2026-09-03 |
| every event, denominator and prohibited inference | `docs/ACQUISITION_EVIDENCE.md` |
| arms, thresholds, coding scheme, recruitment package | `docs/VALUE_CLARITY_FIELD_PROTOCOL.md` |

Instrument state at handoff: runnable, verified on `lichess_app main@07ccd11`. Evidence is in
`runtime/execution_traces/DEL-LICHESS-FIELD-INSTRUMENT-002.json`.

## The link

`https://lichessapp.vercel.app`

Two entry routes, and both must work for a stranger:

| route | who it is for | first screen |
| --- | --- | --- |
| username | has a Lichess or Chess.com account | a position from a game they actually played |
| shared set | has neither, or does not want to type one | a position from the anchor set |

Spread participants across both. A comprehension result from only the username route says nothing
about the half of arrivals who never type one.

## First cohort: Arm A, 5 to 8 people

Arm A is message comprehension. It is first because it costs the least and because an Arm A
participant cannot be recycled into B or C afterwards, so spending the cold contacts here is a
choice made once.

**What the recruiter does:** send the acquisition message and the link, **and stop**.

**What the recruiter does not do:** open the app with them, explain what it is, or answer any
question about what it does until after Q2. A participant who has been told the answer is spent.

**Requirement:** none of the five to eight has seen the product before.

Questions Q1 and Q2, their wording, and the coding scheme for Problem and Differentiation are in
`VALUE_CLARITY_FIELD_PROTOCOL.md`, frozen before data. Do not reword a question between participants
inside an arm. If a wording changes, everything measured before the change is retired.

## What comes after, so the first cohort is not spent wrongly

| arm | n | how it is run |
| --- | --- | --- |
| A, message comprehension | 5 to 8 cold | send the message and the link, then stop |
| B, first-reveal comprehension | 5 to 8 cold | sit them with the app, say only *"תשחקו כרגיל"*, first intervention after Reveal 1, then A, B, C in that order and the two limits-order questions. Record which reveal branch they got |
| C, natural trial | 8 to 15 | send the link, say nothing else, do not contact them again |

Arm B has a stopping rule rather than a quota: keep recruiting until at least two `process` branches
and at least one `outplayed` or silence branch have appeared. The branch is not controllable and the
coding scheme is uninterpretable without the contrast.

## How each participant is carried out

One row per person, per the protocol's per-participant reconstruction.

Arm C's row is the browser's own ledger, copied out **by hand** from the self-check drawer. The
drawer offers a clipboard copy of the report and a JSON download. The ledger is never transmitted and
is never read back by the app, so a participant who does not press the button contributes their
absence and nothing else. That is a stated limit of the collection method, not a defect.

Arms A and B are the researcher's notes. Keep the raw text verbatim and never overwrite it.

## What may not be inferred, at analysis time

Copied from the frozen list because these are the readings the data cannot carry:

- a rendered reveal is not a read one;
- a clean DOM is not comprehension;
- continuation is not satisfaction;
- a stop is not a rejection while `R-23` leaves its cause unobservable;
- the funnel is not a rate over arrivals: handover compliance is in every denominator;
- `acquisition_entry` with tags says a browser opened the app, not that a campaign converted.

## What stops the trial rather than producing a result

1. **A participant cannot reach a first decision on either route.** That is a liveness defect. The
   trial pauses and the finding moves from FIELD back to REPO. It is not a comprehension finding and
   it is the only thing in this sheet that is allowed to reopen the no-code-change decision.
2. The same question is reworded between participants inside an arm.
3. Anyone codes their own participant's answers, or an arm is reassigned after answers are seen.

Until a participant actually hits case 1, do not manufacture a product bug to explain a weak result.

## What is deliberately not here

No new instrument, no added event, no changed threshold, no product change. A change to sections 1 to
6 of the frozen protocol requires `ACQUISITION_PROTOCOL_V2.md` stating what changed and which trial-1
numbers stay comparable, not an edit to this sheet or to the frozen file.
