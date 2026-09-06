# Commitment Qualification vs R&D v0.2 — Comparative Run

Status: `MANUAL_CONTRACT_RUN · REPO-GROUNDED · NOT_RUNTIME_EXECUTION · NOT_PROSPECTIVE_VALIDATION`
Date: 2026-09-06
Frozen benchmark: `QD_VS_RND_V0_FROZEN.md`

Important: this is a manual application of the repository's frozen/candidate contracts. It is **not** an execution of `runtime/calibration_loop/run.py` with live adapters.

## Contract facts recovered from the repository

R&D v0.2 already owns:

```text
TELOS
→ CURRENT STATE
→ RESOURCE MAP
→ BOTTLENECK / MISCALIBRATION
→ CANDIDATE RESOURCE MOVES
→ CHEAPEST DECISION-CHANGING LEARNING
→ RECALIBRATE
```

Its DIAGNOSE output explicitly includes:
- `material_question`;
- `bottleneck`;
- resource expected contribution / authority ceiling / uncertainty;
- candidate moves with expected decision value and reversibility.

The Calibration Loop already routes to Neta when:
- signal→interpretation ambiguity matters;
- multiple mechanisms are plausible;
- proxy substitution is likely;
- evidence is about to become an intervention/build decision.

Therefore `commitment qualification` can be unique only if it repeatedly adds a distinction not already produced by those contracts.

---

## Comparative matrix

| Case | A — R&D SOLO | B — Existing Calibration Loop | C — Compact commitment gate | Unique C decision? | Burden implication |
|---|---|---|---|---|---|
| OR-01 Sheet | Frames telos as reliable lead state; treats Sheet as resource; asks what state/authority properties must be preserved before choosing it | Same; may route broad architecture reasoning if source-of-truth semantics exceed R&D method | `NOT_YET_EARNED`; specify authority/state requirements, then Sheet may be authority or projection | **NO** | C reaches the same precondition with lower ceremony; domain architecture may still require handoff |
| OR-02 Research ROI | **Directly owns this case**: research must compete with repo/field/test/wait/stop on expected decision value per cost | Same, with selective resources only if needed | `NOT_YET_EARNED`; identify controlling uncertainty and cheapest evidence move before buying research | **NO** | C is essentially a compressed R&D diagnosis here |
| OR-03 Lichess history | Treats account history as one evidence resource; asks which live claim it can change and the cheapest sufficient sample | Same; authority ceiling keeps one-user history from becoming field/generalization evidence | `NOT_YET_EARNED`; name claim before export/analysis | **NO** | C compresses a standard R&D resource-fit check |
| OR-04 Marketing assets | Telos→next acquisition/customer decision; asset inventory is a candidate resource set; locate bottleneck before building | Neta may help if buyer signal/interpretation or intervention ownership is ambiguous | `NOT_YET_EARNED`; build only the asset justified by the next blocked decision | **NO** | Same decision; C may avoid full resource mapping when the embedded commitment is obvious |
| OR-05 Findings→UX/UI | R&D alone can flag uncertainty over whether UI is the right resource/intervention, but its own contract says this is a Neta-valuable trigger | **Strong existing coverage**: Neta is explicitly invoked when evidence is about to become intervention/build and when mechanisms/proxies compete | `NOT_YET_EARNED`; establish failure/mechanism/intervention ownership before UI work | **NO versus B**; at most partial versus A | C duplicates a deterministic Neta-routing trigger rather than adding a new epistemic distinction |
| OR-06 Engineering debt→adaptation sequence | Bottleneck/miscalibration + candidate moves naturally challenges a fixed sequence; choose order by dependency, expected value, reversibility | Same; Neta only if interpretation/proxy ambiguity matters | `NOT_YET_EARNED`; sequence must be justified by dependency/bottleneck evidence | **NO** | Compact gate gives a faster surface test, not a different conclusion |
| OR-07 30-min CRM sandbox test | Cheapest decision-changing learning is the proposed bounded test; R&D should choose `TEST` rather than research/migration | Same | `CHEAP_TEST → ACT/LEARN` | **NO** | C can close the gating decision without invoking full loop machinery |
| OR-08 Fixed Vercel constraint | TELOS/CURRENT STATE includes company policy as constraint/authority; optimize resource use inside it or escalate infeasibility | Same; no Neta needed unless another ambiguity appears | `FIXED_CONSTRAINT → OPTIMIZE_WITHIN` | **NO** | Same authority behavior already required by R&D/kernel |
| OR-09 Empathimetry factual existence | If R&D is invoked, it must decide whether RESEARCH is needed; this is unnecessary machinery for a simple factual verification | Existing loop is also overkill unless routing bypasses it upstream | `NO_REFRAME / BYPASS`; answer/verify directly | **NO epistemic delta** | **YES efficiency opportunity**: gate can prevent invoking R&D at all |
| OR-10 “Where is my system losing people?” | This is already a bottleneck question; R&D is a plausible direct owner if resource allocation follows | Same, with Neta only if signal interpretation becomes ambiguous | `ALREADY_DECISION-GRADE`; do not reframe | **NO** | C can act as a cheap no-fire classifier, but may not reduce work if R&D is the correct owner anyway |

---

# Aggregate result

## Unique decision value

Across 10 cases:

- cases where C produced a material decision unavailable to R&D + existing Calibration Loop: **0/10**
- cases where C was partially sharper than R&D SOLO but already covered by Calibration Loop/Neta routing: **1/10** (`OR-05`)
- cases where C and R&D reached materially the same decision: **9/10**

Result:

> `NO_EVIDENCE_FOR_SEPARATE_EPISTEMIC_CAPABILITY`

The strongest previously observed behaviors—challenge an unearned tool/resource/sequence, prefer cheap reversible tests, preserve fixed constraints, ask what evidence can change the move—are already entailed by R&D v0.2 and the existing R&D→Neta routing contract.

## Where C still appears useful

The comparison does reveal a different potential value:

> **C may be a cheap front-door gate that decides whether the full Calibration Loop needs to run at all.**

The compact gate can often classify a prompt into one of:

```text
DIRECT / ALREADY EARNED
CHEAP_TEST
NEEDS_CALIBRATION
FIXED_CONSTRAINT
DOMAIN_HANDOFF
```

before paying for:
- full TELOS/CURRENT STATE/RESOURCE MAP elaboration;
- R&D DIAGNOSE;
- deterministic resource routing;
- Neta or Scaffold invocation;
- R&D SYNTHESIZE;
- durable resource-learning trace.

This is a **coordination/efficiency hypothesis**, not a new reasoning capability.

## Minimal architectural interpretation

The evidence currently supports:

```text
USER QUESTION / PROPOSED MOVE
        ↓
COMPACT COMMITMENT GATE
        ├─ DIRECT / EARNED → answer or act
        ├─ CHEAP_TEST → test and observe
        ├─ FIXED_CONSTRAINT → optimize within
        ├─ DOMAIN_HANDOFF → route authority/capability
        └─ NEEDS_CALIBRATION → existing R&D Calibration Loop
```

rather than:

```text
USER
→ NEW QUESTION-DISCOVERY PRODUCT/PEER
→ R&D
```

## What would justify the gate internally

A front-door gate would be earned if prospective traces show that it:

1. avoids a material number of unnecessary R&D/peer invocations;
2. does not miss cases where the full loop would change the decision;
3. respects authority and cheap reversible action;
4. costs meaningfully less in latency/tokens/operator burden;
5. does not become a second competing source of resource-allocation doctrine.

Required metrics should therefore be routing metrics, not “question quality”:

- `BYPASS_RATE`
- `FALSE_BYPASS_RATE` — gate says direct, but R&D would materially change decision
- `UNNECESSARY_ESCALATION_RATE`
- `DECISION_AGREEMENT_ON_BYPASSED_CASES`
- `LATENCY/TOKEN/COST_DELTA`
- `AUTHORITY_VIOLATION_RATE`

## Product implication

Current repo evidence does **not** support a standalone product claim based on unique reasoning versus R&D.

A standalone user-facing product may still exist commercially if it packages this narrow pre-commitment interaction better than a general decision system, but that would be a **surface/workflow/productization thesis**, not evidence of a distinct epistemic engine.

The internal name should therefore not become a new peer/capability ontology yet.

Candidate internal status:

`FRONT_DOOR_ROUTING_GATE_HYPOTHESIS`

not:

`SEPARATE_DECISION_QUESTION_CAPABILITY`.

## Cheapest next test

Do not run more reframing examples.

Run the compact gate prospectively on a batch of new natural prompts *before* R&D, while shadow-running R&D behind it for evaluation only. Measure whether the gate can safely bypass the full loop.

Decision rule:
- if high bypass + low false-bypass + meaningful cost reduction → keep as routing optimization;
- if R&D repeatedly adds no delta but gate does → consider shrinking/rewriting R&D;
- if gate misses material R&D deltas → do not put it in front of the loop;
- if gate itself adds a repeated distinction unavailable to R&D/Neta → reopen separate-capability status.