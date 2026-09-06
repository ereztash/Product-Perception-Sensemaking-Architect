# Front-Door Gate Shadow Test v0 — Shadow R&D Reference

Status: `SHADOW_RND_FROZEN_BEFORE_ADJUDICATION · MANUAL_CONTRACT_RUN · NOT_RUNTIME_EXECUTION`
Date: 2026-09-06

Important: this applies the repository R&D v0.2 / Calibration Loop contracts manually. It is not a live `run.py` adapter execution.

## Shadow reference decisions

| Case | R&D material question / bottleneck | R&D next move | Material calibration delta? |
|---|---|---|---|
| SG-01 Product value of test | Which product/value claim does the new test strengthen, and what downstream decision does that evidence change? | Compare evidence-before/evidence-after and map to product/engineering/market claim; avoid treating “more data” as generic value | **YES** |
| SG-02 Run 2,533 games | Owner has chosen a full run after a successful pilot; no unresolved resource-choice question is necessary unless cost/contamination emerges | Execute full batch, preserve runtime/failure/evidence delta | **NO** beyond execution discipline |
| SG-03 Progress % feature | The batch is already chosen; progress visibility is a bounded operability/user-feedback need | Implement the smallest reliable progress indicator | **NO** |
| SG-04 Full Gemini teaching app | Owner has fixed deliverable; curriculum completeness is the active dependency | Recover curriculum, then generate complete app specification/prompt | **NO** |
| SG-05 Similar sold products to Neta | Which external products share the relevant capability/problem set strongly enough to inform positioning/comparison? | `RESEARCH`; define comparison dimensions during the research and collect market/product evidence | **NO** extra calibration before research; research is the correct resource |
| SG-06 Neta as startup team | What orthogonal functions would complement Neta in a company-building system? | Direct functional decomposition; do not infer new agents from job titles | **NO** need for full calibration loop |
| SG-07 Reduce effort via PM/templates | Where in the current workflow does user effort materially block adoption/value, and which intervention family owns that friction? | Recover current-state evidence; locate friction; compare templates/integration/automation/onboarding moves | **YES** |
| SG-08 Filming behavior | Owner already chose filming; task is bounded execution guidance | Give concrete recording instructions | **NO** |
| SG-09 Learn from conversation / export MD | What knowledge/decision state must survive the session, who must reuse it, and what representation is cheapest/durable enough? | Compare MD deposit vs repo trace/memory/workflow artifact; choose minimal durable representation | **YES** |
| SG-10 Simply not reply? | Given the live thread and outreach telos, does another message have expected decision value or create unnecessary pressure/noise? | Route to DM/outreach method using thread evidence; choose HOLD/reply | **NO** need for broader R&D calibration |
| SG-11 Current Neta/Lichess repo state | Current state is a REPO-truth question | `COLLECT_REPO`; inspect both repos and report observed deltas | **NO** |
| SG-12 Proven objection methods? | What evidence-backed methods exist and under what conditions do they work? | `RESEARCH` domain evidence; preserve evidence strength/context | **NO** resource-choice ambiguity |
| SG-13 Algorithm matching method to situation? | Does validated conditional matching exist, or only heuristics/frameworks? | `RESEARCH`; compare algorithms, empirical decision rules and practitioner heuristics | **NO** |
| SG-14 Record message sent | Owner reports completed field action; state needs synchronization | Update canonical lead state | **NO** |
| SG-15 Opinion on CRM repo | What is the repo’s actual product/engineering/operational state after recent changes? | `COLLECT_REPO`, then assess | **NO** |
| SG-16 Run/inspect CRM UI | The unresolved truth is ENVIRONMENT behavior, not more reasoning | `COLLECT_ENVIRONMENT`; run/test UI and record failures | **NO** |
| SG-17 Maintainability as gap category | The immediate classification hides a larger decomposition question: if this taxonomy will score repo gaps, what single axis makes categories orthogonal and complete? | Before assigning maintainability, test the decomposition axis against known gaps; treat maintainability as a quality/cross-cutting property unless the axis earns another placement | **YES** — changes object from classification to taxonomy validity |
| SG-18 Neta startup-team roles variant | Same as SG-06: map orthogonal functions first, then role labels if useful | Direct functional decomposition | **NO** |
| SG-19 Personal Lichess account data | Which unresolved claim can one-user game history legitimately change, and what minimum sample/analysis is sufficient? | Calibrate evidence need before export/full analysis | **YES** |
| SG-20 Meaning/importance of maintenance | Direct conceptual learning question | Explain directly | **NO** |

## Shadow aggregate before gate comparison

Cases where full R&D produces a material calibration delta beyond ordinary direct/domain execution:
- SG-01
- SG-07
- SG-09
- SG-17
- SG-19

Total: **5/20**.

All other cases resolve to direct execution, direct explanation, REPO/ENVIRONMENT collection, or domain research/handoff without needing the full calibration loop.