# Front-Door Gate Shadow Test v0 — Gate Outputs

Status: `GATE_FROZEN_BEFORE_SHADOW_RND · MANUAL_SAME_MODEL`
Date: 2026-09-06
Frozen prompts: `QD_SHADOW_GATE_V0_FROZEN.md`

## Gate decisions

| Case | Gate class | Compact rationale | Gate next move |
|---|---|---|---|
| SG-01 Product value of test | `NEEDS_CALIBRATION` | “Raises product value” depends on which uncertainty/claim/value dimension the test changes; not a bounded factual property | Identify the live product/value claim, evidence delta and what decision the test changes |
| SG-02 Run 2,533 games | `DIRECT_EARNED` | Owner explicitly chose the full run after a smaller successful experiment; execution intent is settled | Run the batch; observe outputs/cost/failures; do not reopen whether to run unless a new constraint appears |
| SG-03 Progress % feature | `DIRECT_EARNED` | The long-running batch is already chosen and progress visibility is a bounded usability/operability requirement | Implement progress reporting |
| SG-04 Full Gemini teaching app | `DIRECT_EARNED` | Owner explicitly fixed the desired deliverable after curriculum recovery; question is execution, not resource selection | Gather curriculum, then produce the requested complete app-generation prompt/spec |
| SG-05 Similar sold products to Neta | `DOMAIN_HANDOFF` | Concrete market/competitive research request; first need external/product evidence, not resource calibration | Research comparable sold products and compare capabilities/problem framing |
| SG-06 Neta as startup team | `DIRECT_EARNED` | Conceptual decomposition/exploration with no immediate costly commitment embedded | Answer by mapping orthogonal functions/roles around Neta |
| SG-07 Reduce user effort through PM integration/templates | `NEEDS_CALIBRATION` | A product-direction hypothesis bundles several interventions before locating the material friction/bottleneck | Identify where user effort currently blocks value and which integration/template intervention can change it |
| SG-08 What to do while filming | `DIRECT_EARNED` | Recording decision is already made; request is bounded execution guidance | Give concrete filming behavior/instructions |
| SG-09 Learn from conversation / export MD | `NEEDS_CALIBRATION` | `export to MD` is a candidate artifact before the learning/reuse need is specified | Identify what must survive the conversation and choose the cheapest durable representation/workflow |
| SG-10 Simply not reply? | `DOMAIN_HANDOFF` | Tactical sales/DM decision belongs to the conversation/outreach method and current thread evidence, not general resource calibration | Evaluate the thread under the DM decision method and choose reply/hold |
| SG-11 Current state of Neta and Lichess repos | `DOMAIN_HANDOFF` | Requires repository/current-state inspection; REPO is the relevant truth authority | Inspect current repositories and report state/delta |
| SG-12 Proven objection-handling methods? | `DOMAIN_HANDOFF` | Direct evidence/research question in a domain | Search authoritative/empirical sources on objection handling |
| SG-13 Algorithm matching method to situation? | `DOMAIN_HANDOFF` | Direct research/feasibility question about existing methods/decision systems | Investigate literature/products and distinguish validated algorithms from heuristics |
| SG-14 Record that message was sent | `DIRECT_EARNED` | User reports completed action and requests state update | Update the lead record/status |
| SG-15 Opinion on CRM repo | `DOMAIN_HANDOFF` | Requires repo evidence before judgment; no need to calibrate resources merely to inspect | Inspect repository and assess product/engineering/operational state |
| SG-16 Run and inspect CRM UI | `DOMAIN_HANDOFF` | Requires environment/runtime execution and visual inspection | Run/deploy locally or inspect available environment, then test UI |
| SG-17 Is maintainability part of gap group? | `DIRECT_EARNED` | Conceptual classification question; no costly action/resource embedded | Explain maintainability’s relation to the decomposition |
| SG-18 Neta startup-team roles (variant) | `DIRECT_EARNED` | Same conceptual exploration class as SG-06 | Map complementary orthogonal roles/functions |
| SG-19 Use personal Lichess account data | `NEEDS_CALIBRATION` | Availability of data is not yet evidence that analyzing it is the best resource move | Name the unresolved claim/decision and smallest account-data sample that could change it |
| SG-20 Meaning/importance of maintenance | `DIRECT_EARNED` | Direct conceptual learning question | Explain directly |

## Gate aggregate before shadow reference

- `DIRECT_EARNED`: **8/20**
- `CHEAP_TEST`: **0/20**
- `FIXED_CONSTRAINT`: **0/20**
- `DOMAIN_HANDOFF`: **8/20**
- `NEEDS_CALIBRATION`: **4/20**

Provisional bypass proposed by gate: **16/20 = 80%**.

No quality claim is made yet. The next step is to shadow-run the full R&D contract on all 20 cases and inspect whether any of these 16 bypasses were unsafe.