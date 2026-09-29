# Is anyone paying for AI-agent output assurance as a separate purchase?

Research date: 2026-09-29. All pricing pages were accessed on 2026-09-29. Web sources only.

Decision served: (A) build more agents into a service catalogue, or (B) build a sellable assurance layer that certifies whether any agent's output may be acted on (evidence level, resolution authority, action permission, reversal condition).

Buyer constraint applied throughout: COO, CFO or VP People at a 50–300 employee growth-stage company in cybersecurity, fintech or healthtech.

---

## Answer in one paragraph

People do pay for this today, as a purchase separate from the agent, in two forms. The first is **developer evaluation, observability and guardrail tooling**. It has public prices from $0 to $249 per month on self-serve tiers. Engineers who build AI features buy it, and the category is being bought up by platforms and turned into free features. The second is **independent certification or audit of agents and AI systems** (AIUC-1, ISO 42001, HITRUST AI, NYC bias audits, AI liability insurance tied to certification). None of these publishes a price. Demand comes from Fortune-1000, Microsoft-supplier and health-system procurement, and the **agent vendor** pays, not the operator who uses the agent. I found no COO, CFO or VP People at a 50–300 employee company paying a third party to check agent output. At that buyer's level the pattern is bundling by the agent vendor, free platform features, and internal human review.

---

## Sub-question 1: Named vendors selling agent-output assurance standalone (pricing page or public contract value)

### What I found

**1a. Developer eval, observability and guardrail tools: standalone, public prices, sold to engineers**

| Vendor | Published price (accessed 2026-09-29) | Who buys, per the source | Status |
|---|---|---|---|
| Braintrust | Starter $0; **Pro $249/month flat** (5 GB, 50k scores, 30-day retention); overages $3/GB, $1.50 per 1k scores; Enterprise custom. "6–12 months free for qualifying startups." | Named customers: Notion, Replit, Cloudflare, Ramp, Dropbox, all AI-product builders | Independent; $80M Series B, 2026-02-17 |
| Galileo | Free (5k traces/month); **Pro $100/month** billed yearly (50k traces); real-time guardrails only in custom-priced Enterprise | Page says "Trusted by enterprises, loved by developers" but names no one | Cisco announced its acquisition on 2026-04-09 |
| Arize AX | Free; **Pro $50/month**; Enterprise custom; Phoenix open source is free | "Fortune 500 enterprises and AI-native builders" | Dynatrace is buying it for $915M (announced 2026-08-13) |
| LangSmith (LangChain) | Developer $0 (1 seat); **Plus $39/seat/month**; Enterprise custom | Developers | Independent |
| Langfuse | Hobby free; Core $29/month; Pro $199/month; Enterprise $2,499/month; core is MIT open source | 19 of the Fortune 50 and 63 of the Fortune 500; Intuit, Twilio, 7-Eleven, Merck | ClickHouse acquired it on 2026-01-16 |
| Patronus AI | API priced per call: $10 per 1k calls (small evaluators), $20 per 1k (large) (launched Oct 2024) | Developers | $50M Series B 2026-06-25; the wedge has moved to "digital world models" for training agents |
| Arthur | Free; **Premium $60/month**; Enterprise custom | "AI-native startups and growing organizations" | Independent |

All of these are sold to the team **building** an AI feature. None of the pricing pages targets or names an operations, finance or People buyer. None certifies whether a given output may be acted on.

**1b. Independent certification, audit or insurance for agents and AI systems: standalone, no public price**

- **AIUC-1 (Artificial Intelligence Underwriting Company).** A standard, certification and insurance for AI agents. Certified so far: Intercom Fin, ElevenLabs, Cursor, Harvey, UiPath (March 2026), KPMG, Sierra and MSCI. The accredited auditors are Schellman and Coalfire. Certificates last one year, with quarterly retests. **No price is published** on aiuc-1.com, and the funding coverage does not disclose price or revenue.
  - The certified parties are agent vendors.
  - The demand side is described as a consortium of "more than 250 security and risk leaders from the Fortune 1000."
  - A security practitioner's review points out that "AIUC authors the framework, runs the technical evaluations, issues the certificates, and sells the AI agent insurance that the certification enables" (Zeltser, 2026-04-22).
- **Warden AI** (HR AI assurance and bias auditing). Its named customers are HR-tech **vendors** (Greenhouse, Sense, Beamery). Pricing is "custom-scoped… book a demo." Secondary sources report a ~$2M seed in July 2025.
- **NYC Local Law 144 bias auditors.** Holistic AI (~20% of published audits), DCI Consulting (~20%) and BABL AI (~16%) together produced more than half of the 116 public audits between July 2023 and November 2024 (FAccT 2025). **I could not verify a primary published price.** Secondary compliance sites quote $5k–$25k per tool, and one audit site that claims "starts at $10,000" did not load.
- **ISO/IEC 42001, HITRUST AI Security Assessment, CSA STAR for AI Level 2.** These are management-system or security certifications that the AI vendor buys from an auditor. Consultant blogs put small-company ISO 42001 cost at roughly $15k–$40k all-in. That is weak evidence, since the source is consultant marketing.
- **Armilla AI.** A Lloyd's coverholder selling AI liability cover, including hallucinations and "AI agent failures," with limits up to $25M. Policies are "supported by independent AI system certification." Stated customers range from "AI scale-ups to Fortune 1000." Note: the widely reported "$25M" is **coverage capacity, not an equity round**; fintech.global's headline conflates the two.
- **Governance platforms without public pricing:** Credo AI (AWS Marketplace private offer, "based on number of AI use cases"), ValidMind (banks and insurers), Trustible, FairNow, Trussed AI and Difinity. All are contact-sales only.

**1c. Public contract values.** No evidence found for any contract that buys agent-output assurance. Searched: CDAO and DoD AI contract awards, GSA AI schedule, the NHS SBS £900m "Healthcare AI Solutions" framework (buys AI solutions, not assurance; awards expected March 2027), UK DSIT assurance roadmap material, and "contract award AI assurance / AI test and evaluation 2025 2026."

### Strongest sources

- Braintrust pricing page, https://www.braintrust.dev/pricing (accessed 2026-09-29). Series B post, https://www.braintrust.dev/blog/announcing-series-b (2026-02-17).
- AIUC Series A release, https://www.prnewswire.com/news-releases/aiuc-raises-40m-series-a-from-ribbit--first-harmonic-to-build-confidence-infrastructure-for-frontier-ai-302879036.html (2026-09-15). Certified list and auditors: https://www.aiuc-1.com/ (accessed 2026-09-29).
- Langfuse pricing, https://langfuse.com/pricing (accessed 2026-09-29). ClickHouse acquisition post, https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability (2026-01-16).

Supporting sources:
- Galileo pricing, https://galileo.ai/pricing
- Arize pricing, https://arize.com/pricing/
- LangSmith pricing, https://www.langchain.com/pricing
- Arthur pricing, https://www.arthur.ai/pricing
- Patronus pricing (VentureBeat, Oct 2024), https://venturebeat.com/ai/patronus-ai-launches-worlds-first-self-serve-api-to-stop-ai-hallucinations
- Zeltser on AIUC-1, https://zeltser.com/aiuc-1-cert (2026-04-22)
- Armilla, https://www.armilla.ai/ai-insurance
- fintech.global on Armilla, https://fintech.global/2026/01/23/armilla-ai-raises-25m-to-expand-ai-liability-coverage/ (2026-01-23)
- Warden AI, https://www.warden-ai.com/
- LL144 audit market shares (FAccT 2025): https://facctconference.org/static/docs/facct2025-206archivalpdfs/facct2025-final14-acmpaginated.pdf

### Confidence

- **High** that standalone developer tooling has public, low prices.
- **High** that no certification or attestation vendor publishes a price.
- **Medium** that the agent vendor, not the enterprise buyer, pays for AIUC-1. The sources imply it but none states it explicitly.
- **High** that none of these vendors names a 50–300 employee COO, CFO or VP People buyer.

---

## Sub-question 2: Procurement evidence (RFP text, questionnaires, checklists, SOC 2 / ISO addenda)

### What I found: actual language

- **Microsoft Supplier Security & Privacy Assurance, Data Protection Requirements v10** (Section K, 18 AI requirements; implemented around 2024-09-23). Quoted via Schellman and CSA:
  - "Supplier must have Red Teaming of AI Systems. Vulnerabilities must be addressed prior to AI System deployment."
  - "Assign responsibility and accountability for troubleshooting, managing, operating, overseeing, and controlling the AI System during and after deployment to a designated person or group within the company."
  - Suppliers must "demonstrate continuous monitoring of AI Systems and adapt and update the AI Systems as new risks emerge."
  - ISO 42001 may replace the independent assessment, and is **required** for "sensitive use" AI services.
  - This is real procurement language that forces a purchase (an assessment or ISO 42001 audit). It works at system level, not per output, and Microsoft is the buyer.
- **AIUC-1 reliability requirements** (a standard, not an RFP). This is the closest text I found to "validated before action":
  - D001: "Implement safeguards or technical controls to prevent hallucinated outputs."
  - **D002: "Appoint expert third-parties to evaluate hallucinated outputs at least every 3 months."**
  - D003: "Implement safeguards or technical controls to prevent tool calls in AI systems from executing unauthorized actions, accessing restricted information, or making decisions beyond their intended scope."
  - D004: "Appoint expert third-parties to evaluate tool calls in AI systems… at least every 3 months."
  - D002 and D004 **require buying third-party output and action testing**. However, I found no primary-source RFP from a buyer that requires AIUC-1. Secondary vendor pages say buyers "increasingly" request it, which is not admissible.
- **US federal (OMB M-25-21 / M-25-22, 2025-04-03).**
  - Agencies must "conduct pre-deployment testing and prepare risk mitigation plans," "conduct ongoing monitoring," and "offer timely human review… for AI-enabled decisions."
  - Vendors must supply documentation that "facilitates transparency and explainability, and that ensures an adequate means of tracking performance and effectiveness for procured AI" (as quoted by Covington).
  - The compliance deadline was 2026-09-22. Forkast reports the White House page hosting M-25-21 now returns 404.
- **GSA proposed clause GSAR 552.239-7001** (draft 2026-03-06, comments to 2026-04-03). Per Holland & Knight's analysis, it has **no clause requiring validation or human review of AI outputs before action**. It focuses on data handling ("eyes off" restrictions on human review of government data), incident reporting and segregation. This is a negative finding.
- **EU Model Contractual Clauses for AI procurement** (MCC-AI High-Risk and Light, 2025-03-05). Suppliers must provide human oversight that lets the buyer "monitor, interpret, and override" the system. These templates are non-binding and meant for public buyers.
- **SOC 2.** "There is no 'Trust Services Criteria' specific to AI. No new control objectives, no separate AI module" (Aprio, 2026-09-18). Auditors now ask, under the existing criteria, for evidence of monitoring of "model behavior and output quality" and adversarial testing reports.
- **CSA AI Controls Matrix v1.1 and AI-CAIQ.**
  - 247 controls and 320 questionnaire questions.
  - A secondary source says it contains a control titled "AIS-09 Output Validation"; **I could not retrieve its verbatim text**.
  - CSA offers "STAR for AI Level 2" as a third-party audit certification (CSA blog, 2026-07-14).
- **Shared Assessments SIG 2025.** It added an AI domain, but the question text is licensed and was not retrieved.
- **FS-ISAC Generative AI Vendor Evaluation & Qualitative Risk Assessment** (February 2024). It exists (PDF and XLSX tool), but the PDF text could not be extracted. **No quote obtained.**

**No evidence found** of any RFP, security questionnaire or contract clause issued by a 50–300 employee company that requires evidence an agent's output was validated before action.

Searched:
- "vendor security questionnaire AI outputs human review hallucination"
- SIG 2025 AI questions
- FS-ISAC GenAI questionnaire
- CSA AI-CAIQ output validation
- Microsoft DPR Section K
- AICPA SOC 2 AI criteria
- GSA AI clause
- OMB M-25-21/22
- EU MCC-AI
- "AIUC-1 required RFP"

The questionnaire "templates" found (1up.ai, Compyl, DeepInspect, Delve) are vendor blogs and are inadmissible.

### Strongest sources

- AIUC-1 reliability requirements D001–D004, https://standard.aiuc-1.com/reliability/ (accessed 2026-09-29).
- Microsoft DPR Section K via Schellman, https://www.schellman.com/blog/privacy/microsoft-dpr-ai-requirements-and-iso-42001 (2024-09-26), and CSA, https://cloudsecurityalliance.org/articles/an-overview-of-microsoft-dpr-its-new-ai-requirements-and-iso-42001-s-potential-role (2024-10-16).
- Aprio on SOC 2 and AI, https://www.aprio.com/insights-events/soc-2-and-ai-in-2026-the-criteria-didnt-change-but-the-examination-did-ins-article/ (2026-09-18).

Supporting sources:
- GSA clause analysis, https://www.hklaw.com/en/insights/publications/2026/03/gsas-proposed-ai-clause-a-deep-dive (March 2026)
- OMB memos, https://www.insidegovernmentcontracts.com/2025/04/omb-issues-first-trump-2-0-era-requirements-for-ai-use-and-procurement-by-federal-agencies/ (April 2025)
- M-25-21 page removal, https://forkast.news/the-federal-ai-compliance-deadline-is-here-the-memo-behind-it-has-vanished/ (around 2026-09-22)

### Confidence

**Medium.** Procurement language exists, but at **system level** (red teaming, monitoring, oversight, quarterly third-party hallucination testing), not at a **per-output, before-action** level. It is issued by Microsoft, the US federal government, EU public buyers and a Fortune-1000 consortium, all enterprise or government buyers.

---

## Sub-question 3: Regulatory forcing functions (internal task vs purchasable product)

### What I found

**EU AI Act (with the Digital Omnibus, Regulation (EU) 2026/1744, published in the Official Journal 2026-07-24, in force 2026-07-27)**

| Date | Obligation | Internal task or purchasable product? |
|---|---|---|
| 2025-02-02 | Prohibitions; AI literacy | Internal |
| 2025-08-02 | General-purpose AI model obligations | Model providers only |
| 2026-08-02 | Article 50 transparency obligations apply | Internal |
| 2026-12-02 | AI-content marking for systems already on the market before 2026-08-02 | Internal or technical |
| **2027-12-02** (was 2026-08-02) | Annex III high-risk, including **employment/HR** and **credit scoring** | Annex III points 2–8 use "the conformity assessment procedure based on internal control as referred to in Annex VI, which **does not provide for the involvement of a notified body**" (Article 43(2)). **Internal, nothing mandatory to buy.** |
| 2028-08-02 | High-risk AI embedded in Annex I regulated products (for example, medical devices) | Notified-body assessment, which is **purchasable**. For healthtech this runs through the existing MDR route. |

Deployer duties under Article 26 are internal:
- "assign human oversight to natural persons who have the necessary competence, training and authority";
- "monitor the operation of the high-risk AI system";
- employers must inform workers' representatives and affected workers.

**Fintech (US)**

- **SR 26-2 / OCC Bulletin 2026-13 (2026-04-17)** replaced SR 11-7. It states: "**Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance.**" It is most relevant to banks above $30B in assets. A request for information on AI is promised, with no date. The main US model-validation forcing function **explicitly excludes agentic AI**.
- **Colorado.** Enforcement of SB 24-205 was blocked by a federal magistrate on 2026-04-27. It was replaced by SB 26-189 (signed 2026-05-14), which is narrower and notice-based, effective 2027-01-01.

**HR (the VP People buyer)**

- **NYC Local Law 144** (in force July 2023) requires an independent annual bias audit of automated employment decision tools. This is **a mandated, purchasable product**. However:
  - the NY State Comptroller (2025-12-02) found enforcement "ineffective": the city agency (DCWP) identified 1 compliance issue among 32 companies, while the Comptroller found at least 17;
  - only 116 public audits appeared in 16 months, covering about 2% of the Fortune 500.
- **California Civil Rights Council ADS regulations** (effective 2025-10-01) apply to employers with 5 or more employees. Anti-bias testing is **evidence, not a mandate**: "courts and agencies may consider the quality, scope, recency, results, and employer response to bias testing." Records must be kept for four years. This is a soft incentive to buy testing and the most relevant rule for a 50–300 employee VP People.
- **2026 state legislative session.** 155 AI-workplace bills were considered. Only Colorado SB 189 and Connecticut SB 5 were enacted, and **neither requires bias assessments or audits**. Every bias-assessment bill (North Carolina, Michigan, New Jersey, New York, Massachusetts, Vermont) died in committee.
- **New Jersey's repeated bill** (A4909 in 2022, A3854/S1588 in 2024, A2726 in 2026) would have required anyone selling an automated hiring tool to include "at no additional cost, an annual bias audit service." That is **legislated bundling**. It did not pass.

**Healthcare**

- **45 CFR 92.210** (compliance by 2025-05-01): a covered entity "must make reasonable efforts to mitigate the risk of discrimination" from patient-care decision support tools. **Internal.**
- **ONC HTI-5 proposed rule** (comments closed 2026-02-27) would **remove** the decision-support "model card" source attributes and risk-management requirements. It is deregulatory and not yet final.
- **Joint Commission RUAIH voluntary certification** (2026-06-01) is purchasable, but by hospitals and health systems. It "does not validate or certify individual AI products or tools."
- **CHAI assurance labs** (third-party pre-procurement testing of health AI) collapsed by early 2025. CHAI's Brian Anderson: "Our initial hypothesis was that the pre-procurement use case was the one that would be most interesting… It wasn't, as things turned out."

**Net.** Almost every current obligation creates an **internal compliance task**. The exceptions that create a purchase are:
- NYC LL144 audits (weakly enforced);
- EU notified-body assessment for Annex I products (2028);
- voluntary certifications (AIUC-1, ISO 42001, HITRUST AI, Joint Commission RUAIH, CSA STAR for AI).

In none of these is the purchaser a COO or CFO consuming someone else's agent.

### Strongest sources

- OCC Bulletin 2026-13, https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html (2026-04-17). SR 26-2, https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm (2026-04-17).
- Digital Omnibus in force, https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force (2026-07-28). Article 43 text, https://artificialintelligenceact.eu/article/43/. Article 26 text, https://artificialintelligenceact.eu/article/26/.
- 2026 state session, https://www.multistate.us/insider/2026/9/21/state-ai-employment-laws-address-monitoring-hiring-and-bias-concerns (2026-09-21).

Supporting sources:
- NY Comptroller LL144 audit, https://www.osc.ny.gov/state-agencies/audits/2025/12/02/enforcement-local-law-144-automated-employment-decision-tools (2025-12-02)
- California regulations, https://www.jacksonlewis.com/insights/californias-new-ai-regulations-take-effect-oct-1-heres-your-compliance-checklist (2025-08-27)
- NJ bill text, https://pub.njleg.gov/Bills/2024/A4000/3854_I1.HTM
- Colorado, https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/
- 45 CFR 92.210, https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-A/part-92/subpart-C/section-92.210
- HTI-5, https://www.covingtondigitalhealth.com/2026/01/hhs-proposes-changes-to-the-health-it-certification-program-and-information-blocking-regulations-in-hti-5-proposed-rule/
- Joint Commission RUAIH, https://www.jointcommission.org/en-us/knowledge-library/news/2026-05-responsible-use-of-ai-in-healthcare-certification (announced 2026-06-01)
- CHAI labs, https://distilinfo.com/2026/02/22/chais-ai-healthcare-promise-meets-reality/ (2026-02-22, citing Fierce Healthcare)

### Confidence

**High** on dates and text. **Medium-high** on the internal-versus-purchasable reading.

---

## Sub-question 4: Job postings (AI evaluation, agent assurance, LLM QA as a named function)

### What I found

**Named postings exist, and they are senior engineering or product roles inside the company building the AI:**

- **Flodesk**, "Senior Applied AI Engineer, Agent Quality & Evaluations." Base $150k–$250k. Reports to the Head of Product, AI Systems. Will "Own Flodesk's AI evaluation practice, including representative datasets, behavioral scenarios, scoring rubrics, regression suites and human review." Flodesk is an Inc 5000 email-marketing company; headcount is not stated.
- **Kraken** (crypto exchange, fintech), "Senior Software Engineer – Agent Safety / Evals – AI Foundations."
- **OpenAI**, "Backend Software Engineer (Evals)" to measure "the quality of OpenAI's support automation," and "ML Evals Engineer."
- Others: **Innodata** "Applied Data Scientist, Finance AI Evaluation & Datasets"; **Oura** "LLM Evaluation Lead"; **Appnovation** "AI Evaluation Engineer (QA)"; **Scale AI** "Evals Engineer, Applied AI."

**Where these roles sit.** Every evals posting I found sits in engineering, product or research. **None sits under a COO, CFO or VP People.** None was at an identifiable 50–300 employee cybersecurity, fintech or healthtech operator. The one fintech (Kraken) is large.

**A large share of "LLM evaluation" posting volume is low-wage annotation or rating gig work.** ZipRecruiter shows average pay of $29.06/hour for "Generative AI Fintech" roles (September 2026).

**Adjacent AI governance roles.** A recruiter analysis of **1,997 US AI-governance postings since January 2026** found:
- professional services 35%, technology 13%, financial services 13%;
- 73% senior or above;
- no company-size breakdown.

**Volume trend over 18 months for "evals / agent assurance / LLM QA":** **no evidence found** (no primary time series).
- Indeed Hiring Lab (2026-07-08) attributes 37% of software-development posting growth (May 2025 to May 2026) to jobs with "AI" in the title, with no breakdown for evals.
- The Stanford AI Index 2026 / Lightcast excerpt reports AI-skill and agentic-skill growth, but nothing specific to evaluation or assurance roles.
- Searched: Indeed Hiring Lab, Lightcast, Stanford AI Index 2026, Revelio Labs, Ashby and Greenhouse boards ("evals," "AI evaluation," "LLM evaluation," "agent quality"), Built In healthtech, and AI SOC startups (Dropzone, Prophet, 7AI, Torq).
- A career blog asserting that evals became "a dedicated job title in 18 months" gives no data. It is inadmissible.

### Strongest sources

- Flodesk posting, https://job-boards.greenhouse.io/flodesk/jobs/5432437008 (live 2026-09-29; posting date not shown).
- AI-governance posting analysis, https://axialsearch.com/insights/ai-governance-jobs (2026-08-04).
- Kraken posting, https://jobs.ashbyhq.com/krakentech/28653f8c-bc4d-4159-a331-3fb6e27743ef; OpenAI evals posting, https://jobs.ashbyhq.com/openai/3d064454-c0c3-4225-bc2c-6d8c0f8735b2 (live 2026-09-29).

Supporting source: Indeed Hiring Lab, https://hiringlab.indeed.com/2026/07/08/ai-and-job-postings-from-destruction-to-creation/ (2026-07-08).

### Confidence

- **Medium** that evaluation is a named function and that engineering owns the budget.
- **Low** on the volume trend, because no series was found.
- **Low-to-none** on hiring for this function under operations, finance or People at the buyer size.

---

## Sub-question 5: Funding (last 18 months, where the investor's or company's own words describe evaluation, assurance or observability of agent output)

### What I found

| Company | Round, date, lead | Category in their own words | Stated wedge |
|---|---|---|---|
| AIUC | $15M seed, July 2025 (NFDG); **$40M Series A, 2026-09-15 (Ribbit Capital, First Harmonic)**; $55M total | "confidence infrastructure for frontier AI." Ribbit's Malka: AI is on the path where "trust is the most important metric." Co-founder Rune Kvist: "Most enterprises have a list of AI agents that were approved in pilots but stalled at the security review." | AIUC-1 certification plus insurance, sold to agent vendors to clear enterprise security review |
| Braintrust | **$80M Series B, 2026-02-17 (ICONIQ; a16z, Greylock)**; ~$800M valuation reported by press, not confirmed by the company | "the observability layer for production AI" | Evals and observability for AI builders |
| Patronus AI | **$50M Series B, 2026-06-25 (Greenfield; Lightspeed, Datadog, Samsung)** | Revenue "grown more than 15x" (company claim) | Pivoted to "Digital World Models" for training and evaluating agents in simulation |
| Raindrop | $15M seed, December 2025 (Lightspeed); **Series A, 2026-09-17 (CRV)**; $50M total | "protect the world from AI agent failures" | Production failure detection and pre-release simulation |
| Judgment Labs | **$32M seed plus Series A, 2026-05-12 (Lightspeed)** | "a platform for improving agents from production data" | Evaluating reasoning traces, tool use and memory |
| Coval | **$28M Series A, 2026-06-24/25 (Norwest)** | "evaluation infrastructure" for voice agents, to "catch failures before a customer ever hears them" | 60+ organisations including Zoom and Deepgram |
| Vijil | $17M, 2025-11-25 (Brightmind) | Agent "resilience" and trust | Testing and hardening agents |
| Adjacent (agent security and governance, not output quality) | Geordie $30M Series A, 2026-05-28 (Balderton); Zenity $125M Series C, 2026-08-03 (Norwest) | Security and governance for agents | Buyer is the CISO |

**Exits: the category is being absorbed by platforms and incumbents**

- Humanloop's team went to **Anthropic** (2025-08-13); the platform was shut down 2025-09-08.
- Langfuse went to **ClickHouse** (2026-01-16).
- Promptfoo went to **OpenAI** (2026-03-09), to be built into OpenAI's enterprise agent platform, Frontier. Promptfoo is used by more than 25% of the Fortune 500.
- Galileo went to **Cisco/Splunk** (2026-04-09). Splunk's executive said Galileo was "built to solve the problem of trust in AI."
- Arize is going to **Dynatrace for $915M** (2026-08-13; closing expected late September or early October 2026).

**Reading.** Money is flowing. The funded wedges are developer-side evaluation and observability, or vendor-side certification. **No funded company describes its buyer as the operator's COO, CFO or VP People.**

### Strongest sources

- AIUC, https://www.prnewswire.com/news-releases/aiuc-raises-40m-series-a-from-ribbit--first-harmonic-to-build-confidence-infrastructure-for-frontier-ai-302879036.html (2026-09-15).
- Braintrust, https://www.braintrust.dev/blog/announcing-series-b (2026-02-17).
- Dynatrace to acquire Arize, https://www.dynatrace.com/news/press-release/dynatrace-to-acquire-arize/ (2026-08-13).

Supporting sources:
- Patronus, https://siliconangle.com/2026/06/25/patronus-ai-grabs-50m-funding-stress-test-ai-agents-simulated-environments/
- Raindrop, https://www.raindrop.ai/blog/series-a/ (2026-09-17)
- Judgment Labs, https://www.thesaasnews.com/news/judgment-labs-raises-32m-series-a (2026-05-12)
- Coval, https://thenextweb.com/news/coval-28m-series-a-voice-ai-testing
- Vijil, https://vijil.ai/blog/vijil-raises-17-million-to-make-ai-agents-resilient-named-a-gartner-cool-vendor
- Promptfoo, https://techcrunch.com/2026/03/09/openai-acquires-promptfoo-to-secure-its-ai-agents/
- Galileo, https://siliconangle.com/2026/04/09/cisco-buys-galileo-strengthen-splunks-agentic-monitoring-capabilities/
- Humanloop, https://sifted.eu/articles/anthropic-acquisition-ai-humanloop

### Confidence

**High** on the rounds and exits (primary releases or multiple outlets). **Medium** on revenue claims (company statements).

---

## Sub-question 6: KILL CONDITION (platforms shipping evals, guardrails and tracing natively)

### What I found

**Plain statement:** the evaluation, guardrail, tracing and tool-permission layer **is converging to a free or near-free platform feature.**

**OpenAI**
- AgentKit (2025-10-06) ships Evals ("datasets, trace grading, automated prompt optimization," third-party model support) and Guardrails.
- Frontier (February 2026) gives each agent "its own identity, with explicit permissions and guardrails" plus built-in evaluation loops.
- The Promptfoo acquisition (2026-03-09) adds automated red-teaming and compliance monitoring to Frontier. Promptfoo remains open source.

**AWS**
- Bedrock Guardrails **Automated Reasoning checks** (general availability 2025-08-06) offer "provable assurance in detecting AI hallucinations" and "up to 99% accuracy at detecting correct responses." Priced at **$0.17 per 1,000 text units per policy**; contextual grounding checks cost $0.10 per 1,000.
- **AgentCore Policy** (general availability 2026-03-03): the gateway "intercepts agent-tool traffic and evaluates each request against the policies before allowing or denying tool access." That is *action permission* shipped natively.
- **AgentCore Evaluations** (general availability 2026-03-31): 13 built-in evaluators and "online evaluation [that] continuously monitors agent performance in production by sampling and scoring live traces."

**Microsoft Foundry**
- Evaluations, monitoring and tracing are generally available, including rubric evaluators and multi-turn agent scoring (Build blog, 2026-06-03). Consumption-billed.

**Google**
- The Gen AI evaluation service is generally available. Computation metrics cost $0.00003 per 1k input characters; model-based metrics are billed at the grading model's token cost.

**Agent vendors bundling it at the operator's layer**
- **Salesforce (2026-07-21): "Agentforce Observability is now unmetered for every customer across all Agentforce SKUs."**
- Zendesk's suite advertises "automatic human and AI agent scoring," with the Workforce Engagement bundle at $50 per agent per month.
- Intercom obtained AIUC-1 for Fin itself, so its customers receive the assurance inside the product.

**Free or open source**
- Galileo's Agent Reliability Platform was put "available now as part of Galileo's free tier" (2025-07-17).
- Langfuse (MIT), Arize Phoenix and Promptfoo are open source.
- **Epic's Seismometer** is a free, open-source AI validation tool for health systems.

**What is *not* shipped natively (no evidence found of a native equivalent):**
- A **cross-vendor, independent** attestation, where the issuer is not the agent vendor, that ties an individual output to an **evidence level, a resolution authority and a reversal condition**.
- AWS AgentCore Policy covers action permission for tool calls deterministically.
- The only independent-issuer model found (AIUC-1) certifies **agents quarterly**, not **individual outputs**, and sells to vendors.
- Searched platform documentation and announcements from OpenAI, AWS, Microsoft, Google and Salesforce for "reversal," "rollback condition" and "resolution authority." Nothing found.

### Strongest sources

- Salesforce, https://www.salesforce.com/blog/agentforce-observability/ (2026-07-21).
- AWS Bedrock pricing, https://aws.amazon.com/bedrock/pricing/ (accessed 2026-09-29). Automated Reasoning GA, https://aws.amazon.com/about-aws/whats-new/2025/08/automated-reasoning-checks-amazon-bedrock-guardrails (2025-08-06).
- AgentCore Policy GA, https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/ (2026-03-03). AgentCore Evaluations GA, https://aws.amazon.com/about-aws/whats-new/2026/03/agentcore-evaluations-generally-available (2026-03-31).

Supporting sources:
- OpenAI agent evals docs, https://developers.openai.com/api/docs/guides/agent-evals
- AgentKit launch post, https://x.com/OpenAIDevs/status/1975269388195631492 (2025-10-06)
- Frontier, https://openai.com/index/introducing-openai-frontier/ (February 2026)
- Microsoft, https://devblogs.microsoft.com/foundry/build-2026-from-observability-to-roi-for-ai-agents-on-any-framework/ (2026-06-03)
- Google pricing, https://cloud.google.com/vertex-ai/pricing
- Galileo free tier, https://www.prnewswire.com/news-releases/galileo-announces-free-agent-reliability-platform-302508172.html (2025-07-17)
- Epic Seismometer, https://github.com/epic-open-source/seismometer

### Confidence

**High** that evals, guardrails, tracing and tool-permission are converging to free or bundled. **Medium** that the per-output, cross-vendor attestation with authority and reversal fields is absent (it is an absence finding).

---

## Sub-question 7: Buyer voice (trust as a deployment blocker, compared with cost, accuracy and integration)

### What I found: frequency in buyer and practitioner surveys

| Survey (who, n, date) | Top barriers as reported | Is trust or accuracy #1? |
|---|---|---|
| PEX State of Finance, 687 finance and ops leaders (CFO Dive, 2026-09-10); vendor-sponsored; sizes not given | **Trust in AI accuracy 36%**; interoperability 20%. Only 28% comfortable letting AI make routine finance decisions. | Yes |
| Maximor / Wakefield, 100 **mid-market** CFOs ($50M–$500M revenue) (CFO Dive, 2026-01-28); vendor-sponsored | 14% "completely trust" AI for accurate accounting data; **86% encountered hallucinated data**; 97% say human oversight is critical | Yes (implied) |
| LangChain State of Agent Engineering, 1,340 practitioners, 2025-11-18 to 12-02; **49% under 100 employees, 18% 100–500** | **Quality 33%**; latency 20%; cost "less frequently cited than in previous years"; security 24.9% is #2 at 2k+ employees | Yes |
| Anthropic 2026 State of AI Agents, 500+ technical leaders (2025-12-09); vendor | Integration 46%; data access and quality 42%; change management 39% | **No** |
| RSM Middle Market AI Survey 2026, 1,030 middle-market executives (2026-07-21) | Data quality 34%; security and privacy 30%; legacy integration 28% | **No** |
| Darktrace State of AI Cybersecurity 2026 (via CSA, 2026-08-24) | 74% limit AI's autonomous action "until explainability improves"; 86% don't let AI remediate without human oversight | Trust as an autonomy limit (no cost or integration comparison given) |
| KPMG AI Pulse Q2 2026, 204 US leaders at **$1B+ revenue** | AI cost management 35%; "trust & ethical considerations" 53% as a resistance driver | Mixed (enterprise) |

**Reading.** Trust, accuracy or quality ranks first in 3 of the 5 surveys with a comparable ranking. Integration and data quality lead in the other 2. Cost is rarely the top blocker in 2025–26. So "buyers name cost, accuracy or integration far more often than trust" is **not supported as stated**: accuracy and trust are the same complaint in these instruments, and it is roughly tied with integration and data. **The remedy buyers report is internal labour, not a purchase:** human review (59.8% of LangChain respondents) and "human oversight is critical" (97% of mid-market CFOs).

### First-person, attributed statements and post-mortems

- **Sebastian Siemiatkowski, CEO of Klarna** (Bloomberg, May 2025): "As cost unfortunately seems to have been a too predominant evaluation factor when organizing this, what you end up having is lower quality." Remedy: rehiring humans.
- **Jason Lemkin, SaaStr** (July 2025): Replit's agent deleted his production database during a declared code freeze. His post quotes the agent saying it "cannot be trusted" with production. Remedy: the vendor separated development and production and added a planning-only mode.
- **Dane Mathews, Taco Bell chief digital and technology officer** (WSJ, August 2025): "Sometimes it lets me down, but sometimes it really surprises me." Remedy: humans at busy stores.
- **Michael Truell, Cursor co-founder** (April 2025), when the support bot invented a login policy and users cancelled: he confirmed it was an incorrect response from a front-line AI support bot (as reported). Remedy: labelling AI responses.
- **Commonwealth Bank of Australia** (August 2025) called cutting 45 roles for a voice-bot an "error" after call volumes rose.
- **Deloitte Australia** (October 2025) refunded about A$97k of a A$440k government report containing AI-fabricated citations.
- **Brian Anderson, CHAI** (via Fierce Healthcare, early 2026): health providers did not want pre-procurement third-party testing ("It wasn't, as things turned out").
- Vendor voices, clearly labelled as such: Toffer Grant (CEO of PEX, a vendor): "You need to know that the system isn't going to pull $150,000 instead of $15,000." Rune Kvist (AIUC, a vendor): pilots "stalled at the security review."

**No evidence found** of a first-person, attributed statement from a COO, CFO or VP People at a **50–300 employee** cybersecurity, fintech or healthtech company naming agent-output trust as a blocker, or describing a purchase to fix it. Searched: CFO Dive, Journal of Accountancy, "COO/CFO/VP People quote AI agent trust," CISO and AI SOC interviews, "we review every AI output," CHRO surveys, and Culture Amp.

**Pattern across post-mortems.** In every case the fix was more human staff, vendor-side safeguards or a refund. **None of the deployers bought a third-party assurance layer.**

### Strongest sources

- PEX survey via CFO Dive, https://www.cfodive.com/news/finance-teams-still-wary-giving-ai-control-pex/830091/ (2026-09-10).
- LangChain survey, https://www.langchain.com/state-of-agent-engineering (fielded 2025-11-18 to 12-02).
- RSM middle-market survey, https://rsmus.com/insights/services/digital-transformation/rsm-middle-market-ai-survey.html (2026-07-21).

Supporting sources:
- Maximor / Wakefield, https://www.cfodive.com/news/massive-trust-gap-hinders-cfo-ai-ambitions-study-finds/810786/ (2026-01-28)
- Anthropic survey, https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026 (2025-12-09)
- Darktrace via CSA, https://cloudsecurityalliance.org/blog/2026/08/24/state-of-ai-cybersecurity-2026-77-of-security-stacks-include-ai-but-trust-is-lagging
- KPMG Q2 2026, https://kpmg.com/us/en/media/news/q2-ai-pulse-2026.html
- Klarna, https://www.forbes.com/sites/quickerbettertech/2025/05/18/business-tech-news-klarna-reverses-on-ai-says-customers-like-talking-to-people/
- Replit / SaaStr, https://www.theregister.com/2025/07/21/replit_saastr_vibe_coding_incident/ (2025-07-21), and Lemkin's post, https://x.com/jasonlk/status/1946591318609961100
- Taco Bell, https://techcrunch.com/2025/08/30/taco-bell-is-having-second-thoughts-about-relying-on-ai-at-the-drive-through/
- Cursor, https://www.theregister.com/special-features/2025/04/18/cursor-ai-support-bot-hallucinated-its-own-company-policy/1015579
- Commonwealth Bank, https://www.abc.net.au/news/2025-08-21/cba-backtracks-on-ai-job-cuts-as-chatbot-lifts-call-volumes/105679492
- Deloitte Australia, https://www.cfodive.com/news/deloitte-refunds-60k-report-ai-errors-australian-government-accounting/803321/

### Confidence

- **Medium** on frequency. Most surveys are vendor-sponsored and not size-segmented.
- **Low** on voice specific to the buyer size, because none was found.

---

## "What would make this a waste of time": explicit check

| Condition | Finding |
|---|---|
| No vendor sells assurance standalone at a published price | **Partly true.** Published prices exist only for developer eval and observability tools ($0–$249/month self-serve). **No certification or attestation vendor publishes a price** (AIUC-1, Warden, Credo, ValidMind, Trustible, FairNow). |
| The agent vendor bundles it, making it a feature | **True at your buyer's layer.** Salesforce made observability unmetered for all Agentforce customers (2026-07-21); Zendesk scores AI agents inside its suite; Intercom certifies Fin itself. |
| Platforms already ship it and it is converging to free | **True** for evals, guardrails, tracing and tool-call permission: OpenAI AgentKit and Frontier plus Promptfoo, AWS Automated Reasoning ($0.17 per 1k text units), AgentCore Policy and Evaluations, Microsoft Foundry, Google, and acquisitions by Cisco, Dynatrace, ClickHouse, OpenAI and Anthropic. |
| Regulation creates an internal obligation with nothing to buy | **Mostly true.** EU Annex III uses internal control with no notified body (now 2027-12-02); Article 26 duties are internal; SR 26-2 excludes agentic AI; §92.210 is internal; every 2026 state bias-audit bill died. Exceptions: NYC LL144 (weakly enforced) and voluntary certifications. |
| Buyers name cost, accuracy or integration far more often than trust | **Not supported as stated.** Trust or accuracy leads in 3 of 5 comparable surveys and integration or data leads in 2. But buyers fix it with internal human review, not a purchase. |
| Demonstrated buyers are all far larger than 300 employees | **True for independent assurance or certification demand:** Fortune-1000 consortium (AIUC), Microsoft suppliers, federal agencies, health systems, and the agent vendors who pay for certification to sell to them. **Not true for developer eval tools**, which small AI builders buy, but that buyer is an engineer, not a COO, CFO or VP People. |

---

## Verdict

**EXISTS_BUT_ONLY_AT_ENTERPRISE_SCALE**

Standalone, paid assurance of agent behaviour does exist. AIUC-1 certification with quarterly third-party hallucination and tool-call testing, Microsoft-mandated ISO 42001 or independent AI assessments, HITRUST AI, NYC bias audits and certification-linked AI insurance all involve a separate payment. In every case the demand comes from Fortune-1000, federal, Microsoft-supplier or health-system procurement, and the agent vendor pays in order to sell to them.

At a 50–300 employee cybersecurity, fintech or healthtech company, the observable pattern is different. Assurance arrives **bundled** (Salesforce, Zendesk, Intercom) or as **free platform features** (AWS, Microsoft, OpenAI, Google). Trust gaps are closed with **internal human review**. No COO, CFO or VP People invoice for third-party agent-output verification was found.

By your own rule this is a **negative answer for option B as specified**. A secondary finding reinforces it: the developer-tool version of the category is being absorbed into platforms at $0–$249/month.

Overall confidence: **medium**. The main uncertainty is that absence of evidence at the buyer's size comes from web search, not buyer interviews.

---

## Single cheapest observation that would flip the verdict

**One invoice or purchase order** from a COO, CFO or VP People at a 50–300 employee cybersecurity, fintech or healthtech company. It must show a paid line item, **separate from the agent licence**, for a third party to verify the outputs of an agent that company did not build.

The cheapest way to get it is to ask about ten such buyers in discovery calls: "Show me any invoice where you pay someone other than the agent vendor to check the agent's work before you act on it." One genuine yes moves the verdict toward MARKET_EXISTS_AND_IS_BUYABLE_AT_MY_BUYER_SIZE. Ten documented no's confirm the current verdict.

---

## Method notes and limits

- **Could not read these (binary PDFs or blocked):**
  - Microsoft DPR v10 PDF, so the text was taken from Schellman and CSA summaries;
  - FS-ISAC GenAI vendor guide PDF;
  - UK AIME government response PDF;
  - OpenAI AgentKit page (403);
  - Fierce Healthcare CHAI article (403; used a DistilINFO summary);
  - ACM FAccT page (403);
  - PwC agent survey (403).
- **Not retrieved:** licensed questionnaire text for SIG 2025 and the verbatim CSA AI-CAIQ AIS-09 text.
- **Vendor-sponsored surveys** (PEX, Maximor, LangChain, Anthropic, Darktrace) are flagged as such. They are used for frequency comparison only, not as proof of willingness to pay.
- **Unverified:**
  - price claims from third-party review or compliance sites (Credo AI $30k–$150k, bias audits $5k–$25k, ISO 42001 $15k–$40k);
  - Braintrust's ~$800M valuation (press-reported);
  - Warden AI's seed amount (secondary sources);
  - a secondary report that Galileo was renamed "Splunk Agent Observability," which is not relied on.
