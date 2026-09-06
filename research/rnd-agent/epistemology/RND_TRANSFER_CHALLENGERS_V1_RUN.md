# R&D Transfer Challengers v1 — Comparative Run

Status: `MANUAL_SAME_MODEL_ADVERSARIAL_RUN · REPO_GROUNDED · EXTERNAL_CONCEPT_INFORMED · NOT_HOLDOUT_VALIDATION`
Date: 2026-09-06
Frozen cases: `RND_TRANSFER_CHALLENGERS_V1_FROZEN.md`

## Method

Each family was evaluated separately against `CURRENT_RND` (`prompts/RND_AGENT_V0_2_CANDIDATE.md` + shared kernel / current routing). Challengers were not combined.

Material delta means a change to next move, claim state, evidence channel, stop/continue, or a necessary authority boundary — not merely better terminology.

---

# A — Targeted epistemic edge rules

| Case | CURRENT_RND | + targeted epistemology | B-only material delta? |
|---|---|---|---:|
| TE-01 domain-specific higher-order defeat | Current resource assessment already asks neighboring weak tasks, uncertainty and evidence that a resource changes decisions. The Segment-X audit directly lowers trust in the generic model output for this use; require segment-relevant validation / bounded test before large spend. | `HIGHER_ORDER_DEFEAT` states explicitly that evidence about process reliability can defeat/downweight first-order support. | NO — sharper rule, same path |
| TE-02 irrelevant reliability warning | Do not transfer poor delivery-delay performance to independently validated conversion prediction without evidence of shared failure mechanism. Proceed according to conversion evidence / normal reversibility. | Reliabilism also treats reliability as process/domain-relative rather than global. | NO; useful neighbor protection |
| TE-03 basing lineage | Preserve January rationale as engineer preference; March benchmark changes current support but not historical basis. | `BASING_LINEAGE` names the distinction exactly. | NO current decision delta; YES cleaner lineage semantics |
| TE-04 asymmetric threshold | Sandbox may proceed with moderate evidence because cheap/reversible; production requires stronger support/backup because requested use and reversibility differ. | `EPISTEMIC_RISK_THRESHOLD` gives theoretical reason for different sufficiency thresholds. | NO |
| TE-05 best-of-generated-set | Cheap REPO inspection can test infrastructure explanation; do not commit costly user-behavior intervention while mechanism class remains open. Existing Neta trigger / cheap discriminator covers it. | `CANDIDATE_SET_UNDERDETERMINATION` explicitly says best among sampled candidates is not unique support if candidate set is narrow. | NO vs current Calibration Loop |

### Targeted epistemology aggregate

- clean B-only material next-move delta: **0/5**
- materially clearer hidden judgment / contract language: **4/5**
- regression on neighbor TE-02: **none observed**

Disposition: `CONCEPTUAL_HYGIENE_STRONG · CAPABILITY_DELTA_NOT_ESTABLISHED`

---

# B — Value of Information ranking

| Case | CURRENT_RND | + explicit VOI | B-only material delta? |
|---|---|---|---:|
| VI-01 cheap-low-value vs expensive-high-value | Current contract contains both `expected_decision_value` and `cheapest decision-changing learning`. A disciplined reading should prefer Test 2, but the doctrine is under-specified because a literal cheapest-first reading points to Test 1. | Explicit VOI ranks expected decision improvement net of acquisition cost: Test 1 gross expected improvement 0.2 for cost 1; Test 2 gross expected improvement 12 for cost 4 → Test 2. | **YES at doctrine/control-rule level; likely same answer under best baseline reading, but ambiguity is closed** |
| VI-02 cheap sufficient | Test 1 already crosses the live ship/no-ship threshold; extra causal detail cannot change current decision. Choose Test 1 / stop after sufficient result. | VOI agrees: incremental value of Test 2 for current decision is near zero relative to cost. | NO; important anti-overresearch control |
| VI-03 delay dominates | Decide now; small reversal probability does not justify acquisition + large delay loss. | VOI makes delay cost explicit and reaches same decision. | NO |
| VI-04 sequential info | Run 1-unit screen first; buy field study only conditional on mechanism being active. | Sequential VOI formalizes conditional expected value and same sequence. | NO, but stronger formal rationale |
| VI-05 info cannot change action | Do not buy study for current decision because policy forces A under either state; research may be justified only for another explicitly named future decision. | VOI: value for current decision is zero if no result can change action. | NO |

### VOI aggregate

- clean different final next move under a disciplined CURRENT_RND reading: **0/5 established**
- clean doctrinal ambiguity closed: **1/5 (VI-01)**
- cases where explicit VOI gives a more general ranking/stop justification: **5/5**
- neighbor regression (VI-02 cheap sufficient): **none observed**

Interpretation: VOI remains the strongest transfer candidate because it supplies a missing ranking law, but this visible run does **not** yet establish that current R&D actually makes the wrong choice in natural cases.

Candidate law remains:

> Among admissible learning moves, prefer the move with the highest expected decision improvement net of acquisition, delay and contamination cost; use cheapest-sufficient when additional expected decision value is immaterial or an explicit threshold is already crossed.

Disposition: `DOCTRINAL_DELTA_ESTABLISHED · BEHAVIORAL_DELTA_NOT_YET_ESTABLISHED`

---

# C — Applied epistemology / inquiry design

| Case | CURRENT_RND | + applied epistemology | B-only material delta? |
|---|---|---|---:|
| AE-01 compensation frame | Telos is turnover reduction, not compensation optimization. Exit-interview evidence shows plausible manager/scheduling mechanisms, so more compensation research is misallocated until the bottleneck/question space is reopened. | `INQUIRY_FRAME_RELEVANCE` identifies the compensation commission as a relevance filter that excludes decision-relevant variables. | NO — same path; applied rule makes the failure mechanism explicit |
| AE-02 situated evidence exclusion | Broad deployment claim belongs to FIELD; power users alone cannot close novice comprehension/abandonment. Collect evidence from new users / relevant affected population. | Situated evidence / epistemic exclusion explains why dismissing novice testimony as “uninformed” is an epistemic defect when they possess direct access to the target experience. | NO material path delta; sharper reason for sample relevance |
| AE-03 mediated consensus | Shared consultancy memo + softened original qualifications defeats independence; inspect original expert claims / provenance before treating as consensus. | Testimony/authority analysis distinguishes expert view from institutional mediation and apparent consensus. | NO — existing provenance/independence law already strong |
| AE-04 legitimate expert neighbor | Strong domain-specific access + track record + independent state consistency justifies using the expert claim as a basis for a cheap reversible test; no generic requirement for another expert. | Applied epistemology should not impose skeptical ceremony merely because testimony is involved. | NO; neighbor protected |
| AE-05 acquisition line of inquiry | Business telos is where next month's effort should go; acquisition-only inquiry omits activation as a plausible decision-changing region. Inspect activation before buying more acquisition evidence. | Inquiry epistemology explicitly evaluates which facts/questions are treated as relevant, not only whether collected facts are true. | NO — current `TELOS → BOTTLENECK → cheapest learning` already reaches same reopening |

### Applied epistemology aggregate

- clean C-only material next-move delta: **0/5**
- cases where applied epistemology gives a substantially better explanation of *why* the inquiry is malformed: **4/5**
- neighbor regression AE-04: **none observed**

### Important result

`INQUIRY_FRAME_RELEVANCE` looked like the strongest new applied-epistemology candidate before the run. In these adversarial cases, however, current R&D's existing sequence:

```text
TELOS
→ CURRENT STATE
→ BOTTLENECK / MISCALIBRATION
→ CHEAPEST DECISION-CHANGING LEARNING
```

already reopens the inherited frame whenever omitted evidence can change the live decision.

Applied epistemology therefore currently provides a strong **interpretive theory of an existing behavior**, not a demonstrated missing capability.

Disposition: `APPLIED_EPISTEMOLOGY_CONVERGENCE_STRONG · UNIQUE_CAPABILITY_DELTA_NOT_ESTABLISHED`

---

# Cross-family result

| Challenger | Unique behavioral delta established? | Stronger doctrine/vocabulary? | Current status |
|---|---:|---:|---|
| Targeted epistemic rules | 0/5 | YES | edge-rule vocabulary / conceptual hygiene |
| Applied epistemology | 0/5 | YES, especially inquiry framing / situated evidence | external convergence / adversarial lens |
| VOI | not yet clean behavioral delta; 1 doctrinal ambiguity | **YES, ranking law** | strongest capability challenger |

## What this does and does not imply

This run does **not** show that epistemology is irrelevant. It shows the opposite kind of convergence:

> Current R&D already behaves like a substantial piece of applied epistemology on the tested problems.

But resemblance / theoretical grounding is not enough to justify adding a broad epistemology module.

The strongest unresolved question is now:

> Does explicit VOI ranking change natural R&D choices under competing learning opportunities, or does current R&D already infer the same ranking from expected decision value + cost?

A second unresolved question is whether applied epistemology can expose a natural inquiry-frame failure that current R&D *actually misses* rather than one it can already recover from `TELOS/BOTTLENECK`.

## Current disposition

`TARGETED_EPISTEMOLOGY_TRANSFER: NOT_YET_BEHAVIORALLY_EARNED`

`APPLIED_EPISTEMOLOGY_TRANSFER: NOT_YET_BEHAVIORALLY_EARNED`

`APPLIED_EPISTEMOLOGY_AS_THEORETICAL_NEIGHBORHOOD: STRENGTHENED`

`VOI_RANKING: STRONGEST_NEXT_NATURAL_TEST`
