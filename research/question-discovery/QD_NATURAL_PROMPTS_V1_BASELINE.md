# Question Discovery Natural-Prompt Benchmark v1 — Baseline

Status: `BASELINE_FROZEN_BEFORE_CHALLENGER · SAME_MODEL_MANUAL_RUN`
Date: 2026-09-06
Instruction used conceptually: answer the user's stated question directly and use ordinary strong reasoning; do not explicitly run the Question Discovery contract.

---

## NP-01 — Deploy CRM to Vercel

Direct answer path:
- inspect the CRM stack and deployment assumptions;
- if compatible with Vercel, create/import the project, configure build/output/env vars and deploy;
- if the app requires a persistent process/filesystem or another unsupported runtime property, adapt the app or choose a more compatible host.

`BASELINE_ACTION`: attempt/plan Vercel deployment subject to compatibility.

---

## NP-02 — Use a Sheet as lead-state store

Direct answer path:
- yes, create a Google Sheet as a shared lead tracker;
- define columns such as person/company, status, last contact, next action/date, owner, notes and timestamps;
- update it programmatically after outreach/status changes.

`BASELINE_ACTION`: build/use Sheet as the lead-state store.

---

## NP-03 — Maximize ROI of a research program

Direct answer path:
- estimate expected decision value of the research versus time/cost;
- rank major open questions by impact and uncertainty;
- prioritize the research item most likely to change a high-value decision.

`BASELINE_ACTION`: optimize the current research plan by expected information/decision value.

---

## NP-04 — Use personal Lichess account data

Direct answer path:
- yes, personal game history is a useful non-code evidence source;
- export games through the available API/export route;
- derive candidate metrics and test whether the history reveals stable patterns that can improve the app or validate features.

`BASELINE_ACTION`: export and analyze the account history.

---

## NP-05 — API key export feasibility

Direct answer path:
- yes, if the target service exposes the needed API/export endpoints and the key has the required permissions;
- use the key for the bounded export and avoid exposing it in repository history/logs.

`BASELINE_ACTION`: proceed with export using the key, subject to API permissions.

---

## NP-06 — Marketing assets for Shaked Brand

Direct answer path:
Prioritize a marketing asset stack such as:
1. clear positioning/message;
2. offer/service page;
3. proof/case studies/testimonials;
4. landing/contact path;
5. sales deck or one-pager;
6. content examples;
7. outreach templates;
8. CRM/follow-up tracking.

`BASELINE_ACTION`: build a prioritized inventory of missing marketing assets.

---

## NP-07 — Instagram video strategy

Direct answer path:
Build a sequence of authentic short videos with a clear progression:
- establish the problem you solve;
- show concrete examples/pain;
- demonstrate how you think/work;
- create proof/trust;
- end with a simple CTA to talk.
Use recurring content pillars and make each video carry one takeaway.

`BASELINE_ACTION`: design a video/content sequence and CTAs within Instagram.

---

## NP-08 — Create a domain for deployed CRM

Direct answer path:
- yes, once the deployed app is reachable, a custom domain is useful for a stable branded URL;
- add the domain in the hosting platform and configure DNS records;
- verify TLS and the production target.

`BASELINE_ACTION`: attach a custom domain to the deployed CRM.

---

## NP-09 — Meaning and importance of maintenance

Direct answer path:
Maintenance is the ongoing cost/ability to keep a system correct, understandable, secure, adaptable and operable after initial delivery. It matters because systems change: dependencies update, defects appear, requirements evolve, people leave and operational conditions shift. Poor maintainability raises the cost/risk of every future change.

`BASELINE_ACTION`: explanatory answer; no implementation decision required.

---

## NP-10 — MECE layers for repo gaps

Direct answer path:
`product / engineering / operations` is useful but not guaranteed MECE. Product covers user/value/behavior, engineering covers code/architecture/quality, and operations covers deployment/runtime/support. Cross-cutting concerns such as data/evidence, security, governance and observability can span more than one layer, so the taxonomy should be checked for overlap and omissions before treating it as complete.

`BASELINE_ACTION`: refine the three-layer taxonomy and add/handle cross-cutting concerns.