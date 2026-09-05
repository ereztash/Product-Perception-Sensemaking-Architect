# AUTHORITY MAP — canonical artifacts, peer roles and resolution authorities

This file keeps three different questions separate:

1. **Artifact authority** — which repository artifact is canonical for a governance question?
2. **Agent-role authority** — which peer should work a class of question?
3. **Resolution authority** — what kind of evidence can legitimately close the exact claim?

These are not interchangeable.

## A. Cross-agent artifact authority

| Question | Canonical authority | Not the authority |
|---|---|---|
| What epistemic laws apply across peer agents? | `docs/SHARED_EPISTEMIC_KERNEL.md` | Neta prompt, R&D charter, chat history |
| Are Neta and R&D peers or parent/child? | `docs/AGENT_AUTHORITY_BOUNDARIES.md` | order of implementation |
| How do peers hand work to each other? | `docs/PEER_HANDOFF_PROTOCOL.md` + `schemas/peer-handoff.schema.json` | free-form prose only |
| What is the shared machine-readable claim object? | `schemas/epistemic-claim.schema.json` | either peer's private schema |
| What is the current R&D runtime contract? | `schemas/rnd-research-task.schema.json` | Wave 1 research-claim schema |
| What is the R&D Agent's domain method? | `research/RND_AGENT_CHARTER_V0_1.md` | Neta METHOD |
| How is R&D-agent capability evaluated/promoted? | `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md` | Neta capability gate |

## B. Neta artifact authority

| Question | Canonical authority | Not the authority |
|---|---|---|
| Why does Neta exist? | `docs/TELOS.md` | README slogans |
| What is the v0.2 assurance thesis? | `docs/NETA_ASSURANCE_THESIS.md` | chat history |
| How does Neta reason about product/design? | `docs/METHOD.md` | R&D charter or examples in fixtures |
| What do R0–R6, authorities and permissions mean in the current Neta adapter? | `docs/REALITY_AUTHORITY_PERMISSION.md` | ad-hoc prose elsewhere |
| What was frozen as v0.1? | `docs/V0_1_FREEZE.md` + commit `b1dbfdda...` | current files rewritten later |
| What behavior does the frozen clean-model baseline prompt contain? | `prompts/SYSTEM.md` at the frozen blob hash | v0.2 docs pretending the prompt already changed |
| What finding shape is valid for Neta v0.2? | `schemas/finding.schema.json` + `scripts/validate_finding.py` | shared schema alone |
| Does the Neta finding gate actually reject epistemic violations? | CI + `scripts/check_contract.py` | presence of validator code |
| How is Neta evaluated? | `eval/RUBRIC.md` + Neta-specific eval programs | R&D eval protocol |
| Which historical Neta failures created current gates? | `docs/FAILURE_LINEAGE.md` | memory of prior chats |
| How completely was Lessons re-foundation transferred? | `docs/LESSONS_COVERAGE_AUDIT.md` | one lineage table |
| Where did design principles originate? | `docs/LINEAGE.md` | claims of universality |
| What has Neta learned about owner language? | `memory/owner-language.yaml` | permanent phrase→diagnosis mapping |
| Which Wave 1 questions/thresholds were preregistered? | `research/WAVE1_PREREGISTRATION.md` | v0.2 overlay |
| What candidate claims and original G/C/A/O/status exist? | `research/registers/claims.json` | `WAVE1_ASSURANCE_REVIEW.md` |
| How may Neta research progress toward prompt eligibility? | `research/PROMOTION_PROTOCOL.md` | citation count or R&D-agent promotion |
| What did v0.2 change after source collection began? | `research/AMENDMENTS.md` | silent edits |
| How may Wave 1 be used under v0.2 without rewriting history? | `research/WAVE1_ASSURANCE_REVIEW.md` | retroactive threshold changes |
| Does Neta research quarantine reject invalid promotion? | CI + `scripts/check_research_contract.py` | prose policy |

If two artifacts answer the same governance question differently, the canonical artifact above wins and the disagreement is a defect.

## C. Agent-role authority

Agent-role authority answers **who should work the question**, not what evidence can close it.

### Neta

Primary for product-perception and product/design sensemaking:

- raw product signal;
- concrete product moments/observables;
- neighboring product/design mechanisms;
- product discriminators;
- product/design distinctions;
- reversible product interventions;
- product-specific field requirements.

### R&D Agent

Primary for research/evidence sensemaking:

- research-question decomposition;
- evidence/instrument recovery;
- reuse/adapt/build discrimination;
- preregistration/falsification;
- construct/measurement validity;
- research execution planning;
- run/deposition continuity;
- null/refutation/inconclusive disposition;
- lineage, independence and current-runnability checks.

### Future orchestrator

Primary for routing/dependency management/synthesis across peers.

It is **not** a truth authority and cannot close a claim merely because it sees all peer outputs.

See `docs/AGENT_AUTHORITY_BOUNDARIES.md`.

## D. Resolution authority

Resolution authority belongs to a **claim**, not an agent or entire conversation.

| Authority | May close | May not close merely by being strong |
|---|---|---|
| `OWNER` | intent, taste, strategic tradeoff, accepted risk | stranger behavior/value |
| `REPO` | code, geometry, integrated state, recorded instrumentation | production reality or human interpretation |
| `ENVIRONMENT` | deployed/runtime/config reality | user value/comprehension |
| `RESEARCH` | external mechanism/support within actual constructs and samples; research-method/measurement questions | whether mechanism is active here; product-specific value |
| `FIELD` | external notice, comprehension, preference, value, behavior actually observed | owner's strategic intent; unmeasured causality |

The detailed R0–R6 semantics currently live in `docs/REALITY_AUTHORITY_PERMISSION.md` and are adopted cross-agent by `docs/SHARED_EPISTEMIC_KERNEL.md`.

Historical location does not imply Neta owns the constitutional semantics.

## E. Promotion boundaries

Do not cross-promote between peers.

- Neta capability changes require Neta's own gate.
- R&D capability changes require `eval/rnd-agent/RND_AGENT_EVAL_PROTOCOL_V0_1.md`.
- shared-kernel changes require cross-agent failure evidence and kernel change control.
- one peer's successful benchmark cannot silently promote the other peer.

## F. Questions deliberately unresolved

| Question | Why unresolved | What would create authority |
|---|---|---|
| Does Neta improve Erez's design discrimination over time? | no prospective independent outcome measure | preregistered transfer checks over repeated sessions |
| Does Neta work for another owner-builder? | no external operator replication | second-operator use under frozen method |
| Are Neta's seven lenses complete? | working decomposition only | failure coverage showing stability or forcing revision |
| Does the R&D Agent improve research decision quality? | charter/schema/eval exist but no frozen agent baseline + HOLDOUT run yet | implementation freeze + blind/adjudicated R&D benchmark |
| Does R&D continuity reduce duplicated research cost in real work? | no prospective live-transfer evidence yet | repeated live tasks with baseline comparison and durable run traces |
| What should the future orchestrator optimize? | only two peer contracts are now being established; cross-peer routing failures are not yet measured | stable peer outputs + observed handoff/dependency failures |
| Which model/provider is best for either peer? | no controlled comparative runs | same frozen tasks across clean model surfaces |
| Should the ecosystem have a UI? | no UI-specific need has earned build permission | repeated workflow failures whose cheapest repair is UI-specific |

## G. Research quarantine boundary

External literature, standards, examples and culture/context observations do not directly modify `prompts/SYSTEM.md`, the R&D Agent charter, or the shared kernel.

Wave 1 source collection already began under a frozen preregistration. Neta's v0.2 assurance re-foundation remains a prospective overlay, not a retroactive rewrite.

The R&D Agent is a separate peer and must earn its own capability changes under its eval protocol.

## H. Shared non-collapse rules

- remembered phrase ≠ evidence by itself;
- fixture ≠ field behavior;
- deployment ≠ value;
- paper ≠ product-specific mechanism;
- instrument ≠ run;
- run ≠ durable evidence;
- historical evidence ≠ current runnability;
- agreement ≠ independent triangulation;
- null ≠ refuted;
- pending ≠ failed;
- promotion state ≠ probability of truth;
- G/C/A/O ≠ action permission;
- supported claim ≠ permission for every requested use;
- waiver ≠ upgraded evidence;
- executable feature ≠ justified feature;
- green gate never challenged ≠ demonstrated gate.
