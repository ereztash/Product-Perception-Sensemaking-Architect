# VENDOR disconfirmation report: third-party agent evaluation sold to agent vendors

Research date: 2026-09-29. Sources: open web only. Where a page has no date of its own, it is marked "undated, accessed 2026-09-29".

---

## V1: CLOSED ROLE — CONFIRMED

**Source 1.** AIUC-1 auditor guide, "Evals" page (undated, accessed 2026-09-29): https://standard.aiuc-1.com/auditors/deliver-and-certify/evals
> "AIUC runs evals today. Auditor-led evals are in development." / "The auditor does not run or design the evals. The auditor's role is to validate that testing took place, that procedures followed the documented methodology, and that results met the AIUC-1 pass bar." / "Guidance for auditors who want to run evals themselves is coming soon."

**Source 2.** AIUC-1 "Accredited auditors" page, April 2026 version (archived site aiuc-1-042026.com, accessed 2026-09-29): https://www.aiuc-1-042026.com/accredited-auditors
> "Currently, only the Artificial Intelligence Underwriting Company can carry out the quarterly technical testing required as part of AIUC-1."
>
> The current page (https://standard.aiuc-1.com/accredited-auditors) says: "Only the Artificial Intelligence Underwriting Company can accredit AIUC-1 auditors". It lists Schellman (full accreditation, from 2025-11-01), plus Coalfire, BDO, Grant Thornton, Mastermind, Sensiba and A-LIGN (all provisional, May–Aug 2026).

**Why this settles it.** The wording of D002 and D004 sounds open ("Appoint expert third-parties to evaluate hallucinated outputs / tool calls at least every 3 months": https://standard.aiuc-1.com/reliability/3rd-party-testing-for-hallucinations, https://standard.aiuc-1.com/reliability/3rd-party-testing-of-tool-calls). But the certification process sends that evaluation only to AIUC, the certification body. The only opening announced so far is for AIUC-accredited auditors ("auditor-led evals"). AIUC's CEO confirmed this on 2026-09-16 ("Is it you testing or the auditor?" / "We test them.": https://www.latent.space/p/aiuc). The closest comparable scheme, CSA's STAR for AI Agentic scheme (draft, 2026-03-27), is also limited to auditors who "hold STAR for AI audit qualification from an accredited CSA audit partner program" (https://labs.cloudsecurityalliance.org/agentic/agentic-star-ai-certification-scheme-v1/).

---

## V2: BUYER OUT OF REACH — CONFIRMED

**Source 1.** AIUC-1 research index of dated certification announcements (accessed 2026-09-29): https://www.aiuc-1.com/research
> ElevenLabs (2026-02-18), Harvey (2026-07-30), Cursor (2026-08-12), KPMG (2026-08-27), Sierra (2026-09-17), and a case study on MSCI's internal SecOps agent (2026-09-24). Separate announcements add Intercom/Fin (2025-12-08, https://www.intercom.com/blog/intercom-achieves-aiuc-1-certification/), UiPath (2026-03-09, https://ir.uipath.com/news/detail/430/uipath-achieves-aiuc-1-certification-setting-new-standard-for-ai-agent-security-and-reliability) and Lovable (2026-07-22, https://lovable.dev/blog/aiuc-1).

**Source 2.** AIUC job posting, "Forward-Deployed Engineer" (published 2026-08-28): https://jobs.ashbyhq.com/aiuc/84ae5a63-7a10-45ae-940f-3733ffaefd49
> "We've now certified the category leaders in every major AI vertical: ElevenLabs (voice), Intercom (customer service), UiPath (workflow automation), Lovable (coding), and more we'll announce soon."

**Why this settles it.** Three of the prompt's kill triggers are met at once:
- **All named buyers are large or heavily funded.** ElevenLabs was valued at $11B in Feb 2026 (https://elevenlabs.io/blog/series-d). Sierra was valued at $15.8B on 2026-05-04 (https://techcrunch.com/2026/05/04/sierra-raises-950m-as-the-race-to-own-enterprise-ai-gets-serious/). Lovable was valued at $13.3B on 2026-08-12 (https://www.bloomberg.com/news/articles/2026-08-12/ai-coding-startup-lovable-raises-400-million-at-13-3-billion-valuation). Harvey was valued at $15.5B on 2026-09-09 (https://techcrunch.com/2026/09/09/harvey-hits-15-5b-valuation-months-after-reaching-11b/). The rest are UiPath and MSCI (both publicly listed), KPMG (Big Four), Intercom and Cursor.
- **None is a cybersecurity, fintech or healthtech vendor.** MSCI certified an internal agent, not a product it sells.
- **None is Israeli or sells from Israel.** Searches for AIUC-1 with Israel or Tel Aviv returned nothing.

---

## V3: AUTOMATED SUBSTITUTE — CONFIRMED

**Source 1.** TechCrunch, "Early Anthropic hire, former METR COO have found a way to rein in rogue AI agents" (2026-09-15): https://techcrunch.com/2026/09/15/early-anthropic-hire-former-metr-coo-have-found-a-way-to-rein-in-rogue-ai-agents/
> "The startup then runs an agent through a suite of some 5,000 tests … AIUC uses AI agents to run the tests and AI to analyze the data. Humans, however, verify the final audit."

**Source 2.** AIUC job posting, "Forward-Deployed Engineer" (published 2026-08-28): https://jobs.ashbyhq.com/aiuc/84ae5a63-7a10-45ae-940f-3733ffaefd49
> "Getting there means running thousands of evaluations against their live system … get it wired into our evaluation system … We're building toward a product that runs evaluations end to end without an engineer in the loop."
>
> Supporting source: AIUC's own technical docs (2026-08-15, https://www.aiuc-1.com/research/technical-docs-evaluating-coding-agents) describe grading by a "primary LLM-as-a-judge" plus "adversarial debate" between two LLMs.

**Why this settles it.** For D002 and D004, what the auditor accepts as the "third-party evaluation" is the certification body's own run: AI agents execute the tests and LLMs grade them. The auditor only checks that the run happened, followed the documented method and met the pass bar (V1 Source 1). AIUC is also openly working to remove the human engineer from that loop. So expert human evaluation is not a priced input to this requirement.

---

## V4: NO BUYER-SIDE PULL — CONFIRMED

**Source 1.** Latent Space podcast, interview with AIUC CEO Rune Kvist (2026-09-16): https://www.latent.space/p/aiuc
> "if you want to do a wall-to-wall rollout at a bank or a hospital, you have to go through the risk process. These banks have no idea even which questions to ask"

**Source 2.** AIUC-1 homepage (undated, accessed 2026-09-29): https://www.aiuc-1.com/
> Brad Arkin (LeverSec; formerly Chief Trust Officer at Salesforce): "We've integrated AIUC-1 into vendor assessments because it compresses timelines while raising the standard."

**Why this settles it.** The strongest attributed pull statement found fails on three counts. It comes from a consortium member who runs an advisory firm, not from an enterprise buyer. It says "integrated", not "required". And it is published on the certification body's own site. Meanwhile the certification body's CEO says banks do not yet know what to ask. Every other "buyers are asking" claim traces to AIUC, CSA, certified vendors or auditors. By the prompt's own rule, that means supply-side push. Caveat: real RFPs and security questionnaires are mostly private, so the public web can only show that no attributed pull is visible. It cannot prove that no pull exists.

**What was searched.**
- AIUC-1 with RFP, solicitation, statement of work, security questionnaire, vendor requirements PDFs, "require/requires/requiring AIUC-1", job postings, and university, health-system and bank third-party-risk policies.
- Named consortium buyers (JPMorgan, Capital One, Fidelity, Goldman) with AIUC-1.
- All certification announcements (Intercom, UiPath, ElevenLabs, Lovable, Harvey, Cursor, KPMG, Sierra) for statements that a customer required the certification. None found.
- The CSA STAR registry press release (2026-06-30) and the CRI collaboration post (2026-08-07). Neither contains a buyer-attributed requirement.
- Found and excluded: MSCI's CISO statement (2026-09-24). It concerns MSCI's own internal agent for SOX, not procurement of vendors.

---

## Count

4 of 4 (V1–V4) are CONFIRMED, and V1 is one of them.

## Cheapest single observation that would flip a NOT_CONFIRMED to CONFIRMED

Not applicable: no kill condition came back NOT_CONFIRMED.

The cheapest observation that could *reverse* the controlling kill (V1) would be a written reply from AIUC (contact@aiuc.com) or from one accredited auditor (e.g., Schellman). It would have to say that a D002/D004 report from a vendor-appointed independent expert counts as certification evidence, or that the promised auditor-led evals guidance lets auditors subcontract expert evaluators.
