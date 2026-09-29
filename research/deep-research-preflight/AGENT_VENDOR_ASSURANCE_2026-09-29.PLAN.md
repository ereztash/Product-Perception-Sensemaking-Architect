# Agent-Vendor Assurance: Frozen Disconfirmation Plan

Status: `FROZEN_BEFORE_RUN · DISCONFIRMATION_INSTRUMENT · NOT_CANONICAL`
Frozen: 2026-09-29, committed and pushed before the run
Claim: `C-VENDOR-ASSURANCE` (new claim; see Lineage)
Parent result: `AGENT_ASSURANCE_MARKET_2026-09-29.RESULT.md`

## Gate 0

| # | Item | Value |
|---|---|---|
| 1 | Material question | Is there a paid role an independent practitioner can sell into when agent vendors seek third-party evaluation of agent outputs and tool calls (AIUC-1 D002/D004 and equivalents)? |
| 2 | Claim | Agent vendors in cybersecurity, fintech or healthtech, reachable from Israel, buy third-party output and tool-call evaluation from parties other than the certification body and its accredited auditors. |
| 3 | Decision that could change | Whether to spend up to five field contacts on agent vendors, or keep the capability only as an internal consulting asset. |
| 4 | Minimum reality | Public standard text, auditor and accreditation pages, dated certification announcements, procurement text. |
| 5 | Resolution authority | `RESEARCH` for the kill conditions; `FIELD` for willingness to pay. |
| 6 | Peer | R&D. |
| 7 | Requested use | Kill or authorize bounded field contact. Nothing is built from this result. |
| 8 | Current permission | `DEFER`. |
| 9 | Reversal | The stop rule below. |

## Buyer change, stated

This names a different buyer from the owner's ICP (COO, CFO or VP People at operators). Whether a vendor-side buyer is acceptable is an `OWNER` decision. This instrument informs that decision; it does not make it.

## The frozen prompt

Run verbatim. A reworded question retires everything measured before the change.

```text
DECISION THIS RESEARCH SERVES

Whether to spend field contacts offering independent third-party evaluation
of AI agent outputs and tool calls to agent vendors, meaning the companies
that build agents and sell them to enterprises, instead of keeping that
capability only as an internal consulting asset.

A previous disconfirmation pass found that operating companies of 50 to 300
employees do not pay a third party to verify agent output; they rely on
platform features and internal human review. The one place a purchase
appeared was on the vendor side: agent vendors buying certification
(AIUC-1 and similar) to pass enterprise security review, where the standard
requires third-party evaluation of hallucinated outputs and tool calls at
least every three months.

This research is a DISCONFIRMATION instrument. It cannot establish that a
vendor will pay me; that resolves to field contact and is out of scope here.
Its entire job is to tell me cheaply if this direction is already dead.
Do not pad a weak answer to look balanced.

WHO I AM, FOR SCOPE

An independent practitioner based in Israel, not an accredited audit firm,
with a behavioural-science and agent-evaluation method, and no existing
relationship with any certification body.

THE FOUR KILL CONDITIONS

Answer each one separately.

V1: CLOSED ROLE
Under AIUC-1 (requirements such as D002 and D004) and any comparable agent
standard or certification, who may perform the required third-party
evaluations: only the certification body, only accredited auditors, or any
qualified independent party the vendor chooses. If the role is closed to
accredited or in-house parties, an independent practitioner cannot sell
into it.
Look at: the standard's own text, accreditation or auditor-programme pages,
certification announcements naming who performed the testing.

V2: BUYER OUT OF REACH
Which agent vendors have pursued AIUC-1 or comparable third-party agent
testing, at what size, in which sectors and countries. If every one is a
large or heavily funded vendor, or none is in cybersecurity, fintech or
healthtech, or none is Israeli or sells from Israel, that is a negative
answer for me.
Look at: certification announcements with dates, vendor trust pages,
headcount and funding of the certified vendors.

V3: AUTOMATED SUBSTITUTE
Can the required evaluations be satisfied by automated red-teaming or
evaluation tools that auditors accept as evidence. If a tool run is accepted
as the third-party evaluation, expert human evaluation is a commodity input
with no price floor.
Look at: the standard's evidence requirements, auditor guidance,
partnerships between the certification body and tooling vendors.

V4: NO BUYER-SIDE PULL
Is there primary evidence that enterprise buyers require AIUC-1 or
equivalent third-party agent testing in procurement, as opposed to the
certification body or vendors saying that buyers "increasingly" ask. If the
only evidence is supply-side claims, the certification is being pushed,
not pulled.
Look at: procurement or RFP text, security questionnaire language,
first-person statements from enterprise buyers with attribution.

ADMISSIBLE

The standard's text. Auditor and accreditation pages. Certification
announcements with dates. Pricing pages. Procurement, RFP and questionnaire
text. Job postings. First-person statements with attribution.

INADMISSIBLE

Analyst market sizing. Vendor or certification-body claims about demand
for their own category. Anything projecting past 2027. Commentary without
a named source.

OUTPUT

Per kill condition: CONFIRMED / NOT_CONFIRMED / NO_EVIDENCE, the two
strongest sources with links and dates, and one sentence on why that
evidence settles or fails to settle it.

Then one line: how many of V1 to V4 are CONFIRMED, and whether V1 is one
of them.

Then the cheapest single observation that would flip any NOT_CONFIRMED
to CONFIRMED.

If a kill condition has no evidence, write NO_EVIDENCE and list what you
searched. Absence is a finding. Do not fill the gap with adjacent material.
```

## Preregistered stop rule

Frozen before any result is read.

| Result | Disposition |
|---|---|
| V1 `CONFIRMED` | `STOP`, regardless of the others. There is no role to sell into. The capability stays `INTERNAL_ASSET`. |
| 2 or more confirmed | `STOP`. The capability stays `INTERNAL_ASSET`. |
| exactly 1, not V1 | `INTERNAL_ASSET` stays. Record the gap. No field contact. |
| 0 | `FIELD_AUTHORIZED`: at most five contacts with agent vendors in cybersecurity, fintech or healthtech, each asked one question: whether they have bought or budgeted third-party output or tool-call evaluation, and from whom. |

`NO_EVIDENCE` counts as `NOT_CONFIRMED` for the tally and is recorded separately as a coverage gap.

`0` does not mean a market exists. It means no cheap reason to abandon was found.

## Execution plan and known contamination

Executed by one general-purpose Claude agent with web search and fetch, using the same wrapper as the 2026-09-29 run of the parent instrument (web only, no repository access, report to a file). The prompt was written by the same session and model lineage that will execute it and score it. Zero confirmatory N. The adjudicator scores strictly against the table above.

## Lineage

Parent: `AGENT_ASSURANCE_MARKET_2026-09-08` → `INTERNAL_ASSET` (sensitivity `STOP`) for operator buyers. This claim changes the buyer, so under A2 of `research/RND_AGENT_AMENDMENT_V0_2_1.md` it is a new claim with its own evidence burden. A positive result here is not evidence for the parent claim.
