# R&D Self-Triangulation — External Findings 1

Status: `EXTERNAL_RESEARCH_DEPOSIT · NO_PROMOTION`
Date: 2026-09-08
Plan: `RND_SELF_TRIANGULATION_DR_PLAN_1.json`

Purpose: freeze decision-relevant external findings before R&D synthesis. This is conceptual/source triangulation, not independent runtime adjudication.

## F1 — Resolution authority is not the same object as legitimacy, representation or decision right

**External finding.** Multiple traditions distinguish knowing/answering a question from who is legitimately entitled to frame, govern, participate in, or be affected by the inquiry/decision.

Evidence families:

- Critical Systems Heuristics (Ulrich tradition): boundary critique distinguishes people involved in a system/intervention from those affected but not involved and treats stakeholder roles, values and boundary judgments as constitutive of responsible problem structuring. A South African policy case found CSH useful for eliciting worldviews and improving policy, while also finding that the method itself could not neutralize unequal power relations and historical-political fractures.
- Etuaptmumk/Two-Eyed Seeing research reviews report governance, prioritization, relationships, participation, analysis/interpretation and dissemination as distinct domains; source-grounded characterizations include co-learning, responsibility to future generations, self-determination and Indigenous governance/data ownership. Reviews warn against simplified appropriation.
- Kaupapa Māori research principles, as attributed to Linda Tuhiwai Smith in a New Zealand public-sector methodology, include respect, listening, caution, not trampling mana, benefit to Māori and integrity/commitment.
- Participatory Action Research in the Fals-Borda tradition explicitly combines theory, action and participation, and later historical analysis describes a shift from participation **by** to participation **with** people; the ontology of participation is presented as distinct from instrumental/top-down participation.
- Epistemic injustice literature separates testimonial credibility injustice from hermeneutical injustice caused by gaps/structural prejudice in shared interpretive resources.
- Ubuntu scholarship offers a relational/communitarian ethical vocabulary emphasizing interdependence, social responsibility and harmonious relationship; recent critical work also warns against treating Ubuntu as one generalized 'African philosophy' and stresses regional specificity and contestation.

Representative sources:

- Roher et al. 2024, *How Etuaptmumk/Two-Eyed Seeing is used in Indigenous health research*, PMID 39298423, https://pubmed.ncbi.nlm.nih.gov/39298423/
- Roher et al. 2021, *How is Etuaptmumk/Two-Eyed Seeing characterized in Indigenous health research?*, DOI 10.1371/journal.pone.0254612
- New Zealand Audit Office, Māori-centred methodology using Kaupapa Māori research principles: https://ao.parliament.nz/2022/maori-perspectives/methodology.htm
- Fals-Borda 1987, *The Application of Participatory Action-Research in Latin America*, DOI 10.1177/026858098700200401
- Díaz-Arévalo 2022, *In search of the ontology of participation in Participatory Action Research*, DOI 10.1177/14767503221103571
- Luckett 2006, *An Assessment of the Application of Critical Systems Heuristics to a Policy Development Process*.
- Fricker 2007, *Epistemic Injustice: Power and the Ethics of Knowing*, Oxford University Press.
- Metz/Ubuntu-related systematic and applied bioethics literature; e.g. *Core aspects of ubuntu: a systematic review*, South African Journal of Bioethics and Law 12(2), 2019; and *Ubuntu as a Framework for Ethical Decision Making in Africa: Responding to Epidemics*, Ethics & Behavior 30(1), DOI 10.1080/10508422.2019.1583565.

**Challenges R&D.** The current `OWNER / REPO / ENVIRONMENT / RESEARCH / FIELD` map answers resolution authority, but may not represent a different question: who has legitimate standing to define the decision boundary, be represented in it, or authorize tradeoffs that affect others.

**Competing interpretation.** The existing kernel already separates authority from permission and OWNER from FIELD. Legitimacy might therefore be a permission/governance concern rather than a new resolution authority. Adding a new `LEGITIMACY` authority could incorrectly collapse normative governance into truth resolution.

**Repository delta candidate.** Test, do not yet amend, the distinction:

`RESOLUTION AUTHORITY ≠ DECISION RIGHT ≠ REPRESENTATION / LEGITIMACY`

Targets: `docs/AUTHORITY_MAP.md`, `docs/SHARED_EPISTEMIC_KERNEL.md`.

**Status:** `KERNEL_CHALLENGE + FIELD_HUMAN_REQUIRED`

**Prospective challenge.** Create matched cases where all factual/field evidence is valid and OWNER intent is explicit, but affected stakeholders lack representation or the OWNER lacks legitimate standing to impose the tradeoff. Correct behavior should not invent evidence; it should surface the unresolved legitimacy/decision-right object without pretending it is a RESEARCH or FIELD truth claim.

---

## F2 — Expected decision value is not interchangeable with robustness, option value or plural-value legitimacy

**External finding.** Decision Making Under Deep Uncertainty (DMDU) literature argues that predict-and-act approaches can be ineffective under deep uncertainty and emphasizes robust/adaptable strategies. Reviews also find context influences feasible options and method choice. Multi-Criteria Decision Analysis treats conflicting objectives and preferences as part of the decision object. Real-options literature distinguishes option value under irreversible choices from ordinary information value.

Representative sources:

- Bonjean Stanton & Roelich 2021, *Decision making under deep uncertainties: A review of the applicability of methods in practice*, Technological Forecasting & Social Change 171:120939, DOI 10.1016/j.techfore.2021.120939.
- 2026, *A review of tools and resources to support Decision-Making Under Deep Uncertainty*, Environmental Modelling & Software 198:106900, DOI 10.1016/j.envsoft.2026.106900.
- MCDA review literature on conflicting criteria, uncertainty and preferences; e.g. European Journal of Operational Research reviews.
- Information/option value literature on irreversible decisions, including classic resource-economics work distinguishing the value of preserving options from ordinary information value.

**Challenges R&D.** R&D v0.2 says to select the observation/resource invocation with the best expected decision value relative to cost and contamination risk and repeatedly frames the target as the cheapest decision-changing information. Under deep uncertainty or irreversibility, the best move may instead be a robust/adaptive action or preserving option value even when no information move has the highest scalar expected value.

**Competing interpretation.** R&D already includes reversibility, risk, WAIT, TEST and qualitative resource costs. The wording may be flexible enough that robustness and option value are already admissible decision-value considerations. If so, this is a test/clarity issue, not a telos defect.

**Repository delta candidate.** Stress-test the non-equivalence:

`EXPECTED INFORMATION VALUE ≠ ROBUSTNESS ≠ OPTION VALUE ≠ MULTI-CRITERIA / PLURAL-VALUE FIT`

Targets: `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`, `research/rnd-agent/scope-discovery/RND_SCOPE_MAP_V0_2_FROZEN_FOR_CONFIRMATION.md`.

**Status:** `RND_TELOS_CHALLENGE + SCOPE_CHALLENGE`

**Prospective challenge.** Construct irreversible/deep-uncertainty cases in which (A) a cheap information-gathering move has plausible expected value but closes options or delays adaptation, while (B) a robust/adaptive/option-preserving action dominates across plausible futures. Neighbor controls should include ordinary probabilistic cases where cheapest decision-changing information should still win.

---

## F3 — Telos can itself become the learning target

**External finding.** Pragmatist inquiry, double-loop organizational learning, reflection-in-action and Participatory Action Research all contain versions of a stronger idea than learning how to execute a fixed objective: inquiry/action can transform the problem definition, governing variables, policies, objectives or the situation itself.

Representative sources:

- Stanford Encyclopedia of Philosophy, *Pragmatism* / *John Dewey*: Deweyan inquiry begins with an indeterminate/problematic situation and transforms the situation; problem formulation is itself part of inquiry.
- Argyris 1977, *Double Loop Learning in Organizations*, Harvard Business Review: double-loop learning challenges underlying policies/objectives rather than merely correcting action to meet stated objectives.
- Schön, Drake & Miller 1984, *Social Experimentation as Reflection-in-Action*, DOI 10.1177/107554708400600101; and later scholarship on reflection-in-action under uncertain/unique/unstable practice.
- Fals-Borda/PAR literature: knowledge generation, collective analysis and action are intertwined rather than ordered as detached research then implementation.

**Challenges R&D.** R&D begins from a telos and correctly routes unresolved OWNER-owned telos rather than inventing one. But the loop is less explicit about a different event: evidence/action shows that a previously authorized telos, objective, governing variable or problem boundary itself should be reopened.

**Competing interpretation.** `RECALIBRATE → UPDATED STATE` plus OWNER handoff may already permit this. The gap may be representation/traceability rather than reasoning capability.

**Repository delta candidate.** Test the distinction:

`TELOS AS AUTHORIZED INPUT ≠ TELOS AS REVISABLE LEARNING TARGET`

and separately:

`ACTION AFTER DECISION ≠ ACTION AS INQUIRY`

Targets: `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`, `docs/DECISION_EXECUTION_LEARNING_LOOP.md`, R&D scope map.

**Status:** `RND_TELOS_CHALLENGE + SCOPE_CHALLENGE`

**Prospective challenge.** (1) A field test validates the planned mechanism but reveals that the stated business/social objective creates a larger contrary outcome; R&D should reopen OWNER/legitimacy rather than optimize harder. (2) A case where no pre-action research can distinguish alternatives, but a small reversible action changes the state and reveals the next question; R&D should recognize action itself as the epistemic move. Neighbor control: a case where execution path is already justified and no learning allocation remains (R3).

---

## F4 — Research support does not imply transportability without context–mechanism fit

**External finding.** Realist evaluation and implementation-science literature repeatedly asks what works, for whom, in what circumstances and why. Context–Mechanism–Outcome configurations are used to explain why interventions can differ across settings. Reporting guidance also stresses fidelity/adaptation and contextual description for external validity.

Representative sources:

- Salter & Kothari 2014, *Using realist evaluation to open the black box of knowledge translation*, Implementation Science 9:115, DOI 10.1186/s13012-014-0115-y.
- Lemire et al. 2020, *What Is This Thing Called a Mechanism? Findings From a Review of Realist Evaluations*, DOI 10.1002/ev.20428.
- StaRI / RAMESES implementation and realist-evaluation reporting literature.

**Challenges R&D.** External RESEARCH evidence can be valid about a mechanism/sample while being non-transportable to the current context. The question is whether the existing `RESEARCH ≠ FIELD` and current-state discipline already enforce this strongly enough.

**Competing interpretation.** The current authority map already says RESEARCH cannot close whether a mechanism is active here or product-specific value, and R&D explicitly starts from current state. That may fully cover the material distinction.

**Repository delta candidate.** Before changing anything, test:

`RESEARCH SUPPORT ≠ LOCAL TRANSPORTABILITY WITHOUT CONTEXT–MECHANISM FIT`

Targets: `docs/AUTHORITY_MAP.md`, R&D telos/resource map.

**Status:** `BOUNDARY_CANDIDATE`, with a serious possibility of `NO_DELTA`.

**Prospective challenge.** Give R&D a strong systematic-review finding plus a target context with a known mechanism-breaking constraint. Correct output should route local mechanism/activity to FIELD/ENVIRONMENT rather than inherit efficacy from RESEARCH. If current R&D already does this reliably, close as `NO_DELTA`.

---

## F5 — Ill-structured, multi-perspective problem framing may be DOMAIN_METHOD_PRIMARY rather than R&D core

**External finding.** Problem Structuring Methods (PSMs) in operational research are explicitly designed for ill-structured/wicked situations with multiple actors, perspectives, conflicting interests, uncertainty and intangibles. Reviews characterize them through ontological, epistemological, axiological and methodological assumptions, and participatory modelling is a central feature.

Representative sources:

- Smith & Shaw 2019, *The characteristics of problem structuring methods: A literature review*, European Journal of Operational Research 274(2):403-416.
- Mingers & Rosenhead 2004, *Problem structuring methods in action*, European Journal of Operational Research 152(3):530-554.

**Challenges R&D.** A complicated, multi-hypothesis or stakeholder-rich problem can look like nontrivial epistemic allocation while its primary unresolved work is actually problem framing/domain method. This directly neighbors the known false-fire that motivated `R4_DOMAIN_METHOD_PRIMARY`.

**Competing interpretation.** The current frozen scope already contains R4 precisely for domain-method-primary cases. PSM literature may therefore strengthen test construction without requiring a new region.

**Repository delta candidate.** Build R1/R4 neighbor cases involving stakeholder problem framing vs a separable choice of whether/how/how much to learn.

Target: `research/rnd-agent/scope-discovery/RND_SCOPE_MAP_V0_2_FROZEN_FOR_CONFIRMATION.md`.

**Status:** `SCOPE_CHALLENGE`, likely test enrichment rather than immediate scope amendment.

---

## F6 — Cross-cultural convergence exists, but has low decision value unless it changes a boundary

**External finding.** Several traditions contain recognizable analogues to parts of R&D: Deweyan inquiry transforms problematic situations; Japanese Hoshin Kanri uses participative strategy deployment, review and catchball/nemawashi processes; continuous-improvement traditions emphasize iterative learning; relational-autonomy and Ubuntu literature challenge isolated-individual models of decision making.

Representative sources:

- Witcher & Butterworth 2001, *Hoshin Kanri: Policy Management in Japanese-Owned UK Subsidiaries*, Journal of Management Studies 38(5):651-674, DOI 10.1111/1467-6486.00253.
- *Hoshin Kanri: Implementing the Catchball Process*, Long Range Planning 34(3):287-308, DOI 10.1016/S0024-6301(01)00039-5.
- Akhtar et al. 2024, systematic review of factors influencing autonomy in healthcare decision-making in the Global South, PMID 39175161.

**Challenges/supports R&D.** These parallels show that R&D's loop is not conceptually isolated, but similarity does not establish unique value, universality or correctness. Hoshin Kanri in particular is a management method with its own domain/telos assumptions; it is not evidence that R&D should absorb that method.

**Repository delta candidate.** None unless a parallel sharpens one of F1–F5 or creates a new falsifier.

**Status:** `NO_DELTA` for capability promotion; `CONCEPTUAL_LINEAGE_ONLY`.

---

# Cross-branch synthesis frozen before R&D sees it

Three strongest candidate distinctions survived the external pass:

1. `RESOLUTION AUTHORITY ≠ DECISION RIGHT ≠ REPRESENTATION / LEGITIMACY`
2. `EXPECTED INFORMATION VALUE ≠ ROBUSTNESS ≠ OPTION VALUE ≠ PLURAL-VALUE FIT`
3. `TELOS AS AUTHORIZED INPUT ≠ TELOS AS REVISABLE LEARNING TARGET`

Two additional challenge families should be tested rather than promoted:

4. `RESEARCH SUPPORT ≠ LOCAL TRANSPORTABILITY WITHOUT CONTEXT–MECHANISM FIT`
5. `ILL-STRUCTURED / MULTI-PERSPECTIVE PROBLEM ≠ EPISTEMIC-ALLOCATION PROBLEM`

## Explicit no-promotion statement

This deposit does **not** show that R&D is cross-culturally valid, empirically superior, or independently confirmed. The external sources are independent research evidence about neighboring constructs and failure conditions. R&D's interpretation of them remains part of the system under test. Any kernel/telos/scope amendment must be earned by prospective challenge cases and the repository's own change gates; runtime confirmation still requires independent model lineage or qualified human/domain adjudication.
