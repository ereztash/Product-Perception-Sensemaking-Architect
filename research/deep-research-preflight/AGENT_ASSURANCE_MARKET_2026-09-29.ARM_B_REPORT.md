# Disconfirmation check: assurance layer over agent output

Compiled 2026-09-29 from web sources only. Pricing pages carry no publication date, so they are marked "accessed 2026-09-29". Analyst sizing, vendor category claims, projections past 2027 and unnamed commentary were excluded.

---

## K1 — PLATFORM ABSORPTION: CONFIRMED

- **Source 1:** AWS, [Amazon Bedrock AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/) (accessed 2026-09-29), together with [AgentCore Evaluations GA](https://aws.amazon.com/about-aws/whats-new/2026/03/agentcore-evaluations-generally-available) (2026-03-31) and [AgentCore Policy GA](https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/) (2026-03-03).
  - Evaluations include 13 built-in evaluators with online scoring of live traces. They cost $0.0024 per 1K input tokens and $0.012 per 1K output tokens, and custom evaluators cost $1.50 per 1K evaluations.
  - Policy is enforced outside the agent code at $0.000025 per authorization request.
  - Tracing is billed at standard CloudWatch rates.
  - Guardrails cost $0.15 per 1K text units, a rate set on [2024-12-01](https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-bedrock-guardrails-reduces-pricing-85-percent/).
- **Source 2:** Anthropic, [Claude Managed Agents: Define outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes) (beta header `managed-agents-2026-04-01`; public beta 2026-05-06), together with the [Claude pricing page](https://platform.claude.com/docs/en/about-claude/pricing) (accessed 2026-09-29).
  - A separate-context grader is provisioned automatically. It scores the agent's output against a rubric you supply and loops until the output passes.
  - The pricing page lists only tokens plus $0.08 per session-hour, so there is no separate charge for grading.
- **Why:** Every major platform now ships evaluation, guardrails, tracing and policy natively, and each either meters them at token-level cents or includes them at no separate charge:
  - **AWS and Anthropic:** as in the two sources above.
  - **Google:** [Gemini Enterprise Agent Platform](https://cloud.google.com/blog/products/ai-machine-learning/introducing-gemini-enterprise-agent-platform), GA 2026-04-22, adds Agent Evaluation, Observability, Gateway and LLM-judge anomaly detection. [Model Armor](https://cloud.google.com/security/products/model-armor) is free for 2M tokens a month and then $0.10 per 1M tokens.
  - **Microsoft:** [Agent 365](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) went GA on 2026-05-01 at $15 per user per month.
  - **OpenAI:** its one retreat, the [Evals platform shutdown](https://developers.openai.com/api/docs/deprecations) (announced 2026-06-03, shutdown 2026-11-30), sends users to Promptfoo. OpenAI [acquired Promptfoo](https://techcrunch.com/2026/03/09/openai-acquires-promptfoo-to-secure-its-ai-agents/) on 2026-03-09 and is folding it into Frontier.

  So the layer made of these four functions is commoditized. What this does not settle is whether a buyer-facing attestation product for a non-technical owner is something different from these building blocks.

---

## K2 — BUNDLED FEATURE, NOT PRODUCT: NOT_CONFIRMED

- **Source 1:** [Patronus AI pricing](https://www.patronus.ai/pricing) (accessed 2026-09-29).
  - This is assurance-only pricing: $10 per 1K small-evaluator API calls, $20 per 1K large-evaluator calls, $10 per 1K eval explanations, and a $25/month base plan.
- **Source 2:** [Braintrust pricing](https://www.braintrust.dev/pricing) (accessed 2026-09-29).
  - Scores are their own metered line: $2.50 per 1K on Starter and $1.50 per 1K on Pro, with Pro at $249/month.
  - Braintrust stayed independent after an [$80M Series B at an $800M valuation on 2026-02-17](https://siliconangle.com/2026/02/17/braintrust-lands-80m-series-b-funding-round-become-observability-layer-ai/).
- **Why:** Assurance does carry its own price line in several places (Patronus per evaluator call, Braintrust per score, [LangSmith](https://www.langchain.com/pricing) per evaluator run), so the kill as written fails. The case against a standalone product is still strong:
  - Every line item found is a developer-metered API or seat price sold to engineering.
  - Independent vendors were absorbed into observability, security and model suites during 2025–26:
    - Galileo to Cisco, [closed 2026-05-22](https://blogs.cisco.com/news/cisco-announces-the-intent-to-acquire-galileo) and [renamed Splunk Agent Observability on 2026-08-07](https://befailproof.ai/answers/galileo-cisco-acquisition/).
    - Arize to Dynatrace for [$915M, announced 2026-08-13](https://ir.dynatrace.com/news-events/press-releases/detail/435/dynatrace-to-acquire-ai-observability-leader-arize).
    - Promptfoo to OpenAI Frontier.
    - Lakera to [Check Point (2025-09)](https://www.checkpoint.com/press-releases/check-point-acquires-lakera-to-deliver-end-to-end-ai-security-for-enterprises/).
  - No public contract value for a standalone assurance purchase was found. Credo AI publishes no price and shows only "awardable" marketplace and reseller listings.

---

## K3 — BUYER SIZE MISMATCH: NOT_CONFIRMED

- **Source 1:** Microsoft, [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) (updated 2026-07-28).
  - Agent 365 "is available as an add-on to Microsoft E5/A5/Business Premium."
  - Business-family plans are capped at 300 seats ([Business Premium FAQ](https://learn.microsoft.com/en-us/microsoft-365/business-premium/microsoft-365-business-faqs?view=o365-worldwide)).
  - So agent governance is sold into the 50–300 band, but through the IT/security licensing budget.
- **Source 2:** IAPP, [AI Governance Profession Report 2025](https://iapp.org/resources/article/ai-governance-profession-report) (2025-04-16; 671 respondents).
  - The primary owner of AI governance is privacy (22%), legal/compliance (22%), IT (17%), data governance (10%), ethics/compliance (6%) or security (5%).
  - No COO, finance or HR owner category appears.
- **Why:** The condition that every buyer is above 5,000 employees is refuted:
  - Microsoft sells agent governance as an add-on to a SKU capped at 300 seats.
  - Small builder teams adopt assurance tooling. In [LangChain's Nov–Dec 2025 sample](https://www.langchain.com/state-of-agent-engineering), 49% of respondents were under 100 employees and about 52% run offline evals.

  But every budget owner I observed is IT/security, engineering, privacy/legal or risk:
  - At fintech Mercury, the [Data & AI Governance lead reports to the Chief Risk Officer](https://job-boards.greenhouse.io/mercury/jobs/6142625004).
  - [AIUC-1 agent certification is bought by agent vendors such as UiPath](https://www.uipath.com/blog/product-and-updates/aiuc-1-certification-next-chapter-trusted-agentic-automation) (2026-03-10), not by the companies deploying agents.
  - Among firms of 500 or fewer employees, only 9% monitor AI for accuracy and drift ([Pacific AI/Gradient Flow, fielded Feb–May 2025](https://gradientflow.com/2025-ai-governance-survey/)).

  The regulations that could force your band to buy were cut or pushed back:
  - Colorado's [SB 26-189](https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/) (signed 2026-05-14) drops deployer impact assessments; it takes effect 2027-01-01.
  - The EU's Annex III high-risk duties were [deferred to 2027-12-02](https://www.orrick.com/en/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes).
  - Under NYC LL144, only [18 of 391 employers posted a bias audit](https://arxiv.org/abs/2406.01399).

  So the size kill fails, but nothing I found shows a COO, CFO or VP People as the budget owner.

---

## K4 — THE BLOCKER IS SOMETHING ELSE: NOT_CONFIRMED

- **Source 1:** [PwC AI Agent Survey](https://www.pwc.com/us/en/tech-effect/ai-analytics/ai-agent-survey.html), fielded 2025-04-22 to 2025-04-28 with 308 US executives; figures via [Techstrong.ai](https://techstrong.ai/agentic-ai/ai-agents-are-gaining-traction-in-enterprises-but-with-some-hiccups-pwc-survey/).
  - Share naming each item as a top-three challenge: "lack of trust in AI agents" 28%, cybersecurity 34%, implementation cost 34%, data issues 24%.
- **Source 2:** [RSM Middle Market AI Survey 2026](https://rsmus.com/newsroom/2026/rsm-survey-middle-market-embraced-ai-now-comes-hard-part.html), fielded 2026-03-05 to 2026-03-16 and published 2026-07-21; 1,030 respondents at companies with $30M–$10B revenue.
  - Top inhibitors to deployment: data quality 34%, security/privacy 30%, legacy integration 28%, talent 28%.
  - Trust in, or accuracy of, AI output is not among the items reported.
- **Why:** Trust is not a marginal item:
  - In PwC it ties roughly with cost.
  - In [KPMG's Q1 2025 sample of $1B+ companies](https://kpmg.com/us/en/media/news/q1-ai-pulse-2025.html), "personal trust in the technology" is 35%, behind risk management (82%) and data quality (64%).
  - Output quality (accuracy, consistency, hallucination) is the number-one barrier for builders, at 32% in [LangChain's 1,340-respondent survey](https://www.langchain.com/state-of-agent-engineering).

  It still does not settle the question for your buyer:
  - In the one mid-market survey (RSM), the top four inhibitors are data, security, integration and talent.
  - The closest sample to your buyer is [100 CFOs at $50–500M-revenue firms](https://www.journalofaccountancy.com/news/2026/feb/agentic-ai-is-handling-more-finance-work-but-can-cfos-trust-it/) (Wakefield for the vendor Maximor, fielded Sept 2025). There, 86% had hit hallucinated AI data, yet [88% already use agentic tools, with human review](https://www.cfodive.com/news/massive-trust-gap-hinders-cfo-ai-ambitions-study-finds/810786/).
  - I could not retrieve the full question wording for PwC, KPMG or RSM.
  - No survey isolates a COO, CFO or VP People at 50–300 employees.

  So the kill is not confirmed, but it is not ruled out for your specific buyer.

---

**CONFIRMED: 1 of 4 (K1).**

**Cheapest single observation that would flip a NOT_CONFIRMED to CONFIRMED:** Download RSM's full 2026 report (the `ai_survey_report.pdf` link on the [survey page](https://rsmus.com/insights/services/digital-transformation/rsm-middle-market-ai-survey.html)) and read the complete answer options for "top inhibitors to deployment", using the smallest revenue band it reports.
- If an option about accuracy, reliability or trust in AI output was offered and ranks below data, security, integration and cost there, K4 flips to CONFIRMED for the mid-market.
- That takes one document read and no field contact.
