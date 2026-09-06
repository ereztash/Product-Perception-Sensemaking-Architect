# R&D Self-Scope Discovery — DIAGNOSE

Status: `ROLE_CONDITIONED_MANUAL_RND_RUN · REPO_GROUNDED · NOT_RUNTIME_EXECUTION`
Date: 2026-09-06

## material_question

What bounded task region repeatedly receives material decision value from R&D, relative to strong alternatives, and what evidence would justify claiming that boundary with at least 95% sequentially valid confidence?

## bottleneck

The current bottleneck is **not lack of a plausible telos**. It is lack of an independently validated mapping from task characteristics to material R&D delta.

Current evidence is rich for discovery but weak for >95% scope claims because:
- many cases were authored or interpreted after candidate distinctions were visible;
- manual runs share the same underlying model lineage;
- theoretical convergence with applied epistemology / VOI is not independent performance evidence;
- current eval protocol tracks many R&D skills but does not yet estimate the probability of material R&D delta conditional on a task-region;
- the current candidate boundary may be partly tautological if the scope taxonomy uses features defined by R&D's own method.

## resource_assessment

### R&D historical artifacts
Expected contribution: discovery priors, known failure families, candidate positive/negative regions, existing natural prompts.
Authority ceiling: cannot independently validate R&D because most prior adjudication shares model/author lineage.
Uncertainty: which patterns generalize to unseen natural tasks.

### Existing eval protocol
Expected contribution: strong non-collapse rules, adversarial/holdout/live-transfer separation, explicit prohibition on same-model self-critique as independent corroboration.
Authority ceiling: designed mainly for capability promotion, not conditional scope estimation.
Uncertainty: how to extend it without rewriting frozen historical results.

### Neta
Expected contribution: challenge scope decomposition, detect proxy categories, overlaps and boundary leakage, especially R&D vs product signal→mechanism→intervention.
Authority ceiling: cannot adjudicate empirical R&D superiority; agreement is not independent validation.
Uncertainty: whether proposed scope features are genuinely orthogonal or simply restate R&D's own telos.

### Statistical scaffold
Expected contribution: sequentially valid confidence design so the program may continue sampling until evidence threshold without optional-stopping inflation; fixed-N Wilson intervals can be used as descriptive checks.
Authority ceiling: statistical validity does not repair non-independent cases, biased case generation or bad labels.
Uncertainty: exact model should remain simple enough for heterogeneous task families.

### Independent baseline / judge
Expected contribution: break same-model lineage and establish case-level correctness / material delta.
Authority ceiling: judge must itself be blinded to candidate label and must preserve domain authority; human/domain adjudication may still be needed for ambiguous cases.
Uncertainty: availability in current environment.

### REPO
Expected contribution: recover and freeze historical natural cases and provenance.
Authority ceiling: repository state cannot determine whether a reasoning decision was substantively correct in FIELD/external reality.

## candidate_moves

1. `USE_EXISTING` — preserve current eval protocol as constitutional base; do not replace it.
2. `INVOKE_NETA` — challenge and refine the task-feature space before outcomes are used.
3. `USE_SCAFFOLD` — add sequential-confidence methodology for the 95% stopping requirement.
4. `RECOVER` — build discovery corpus from existing natural tasks across repositories/conversations where provenance exists.
5. `TEST` — run baseline vs R&D paired evaluations with blinded, independent adjudication.
6. `TEST` — generate/freeze prospective neighbor-balanced cases only after discovery taxonomy is frozen.
7. `COLLECT_FIELD` where the claimed benefit is actual downstream decision/outcome rather than reasoning-path correctness.
8. `STOP` only when prespecified confidence criteria for the boundary claims are satisfied or the result remains explicitly inconclusive due unavailable independent evidence.

## needs

```json
{
  "signal_interpretation_ambiguity": true,
  "multiple_plausible_mechanisms": true,
  "proxy_substitution_risk": true,
  "research_to_intervention_transition": false,
  "broad_reasoning_needed": true,
  "architecture_alternatives_needed": false,
  "novel_synthesis_needed": true,
  "owner_authority_needed": false,
  "repo_authority_needed": true,
  "environment_authority_needed": false,
  "field_authority_needed": false,
  "external_research_needed": false
}
```

## rationale

The candidate telos itself predicts that another wording iteration has low information value. The highest-value next uncertainty is whether material R&D delta concentrates in a stable, describable task-region once outcomes are blinded and independently judged. Because the boundary representation can manufacture apparent success, Neta should challenge the decomposition before confirmatory evidence is observed. Sequential statistical tooling is justified by the owner's explicit requirement not to stop until >95% evidential support is achieved.
