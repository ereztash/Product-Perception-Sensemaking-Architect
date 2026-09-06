# R&D Telos Peer Review — R&D DIAGNOSE

Status: `ROLE_CONDITIONED_MANUAL_RND_PASS · FROZEN_PROMPT_V0_2 · NOT_INDEPENDENT_MODEL_RUN`
Date: 2026-09-06
Prompt contract: `prompts/RND_AGENT_V0_2_CANDIDATE.md`
Task: `RND_TELOS_PEER_REVIEW_TASK_2026-09-06.md`

```json
{
  "material_question": "Is R&D's distinctive function better defined as calibrating epistemic effort to decision value rather than broadly improving resource-to-telos fit, and what is the narrowest formulation that preserves observed material R&D delta?",
  "bottleneck": "The v0.2 telos makes all system resources the apparent object of R&D, which leaks toward orchestration and general management. The owner's candidate correctly centers learning investment, but may over-narrow temporally with 'before' and may confuse a common activation trigger (a consequential commitment) with the telos itself.",
  "resource_assessment": [
    {
      "resource": "REPO_EVIDENCE",
      "expected_contribution": "Compare positive/no-delta R&D cases, current authority boundaries, and narrow-telos benchmark failures.",
      "authority_ceiling": "Can establish repository-defined behavior and historical benchmark pattern, not future field value.",
      "uncertainty": "Whether historical cases are sufficient to separate telos from trigger without another prospective run."
    },
    {
      "resource": "NETA",
      "expected_contribution": "Challenge whether 'epistemic budget', 'before research', and 'resource commitment' are the true mechanism, proxy, activity label, or trigger; discriminate competing framings.",
      "authority_ceiling": "Can improve framing/discrimination, not canonize R&D authority or empirical performance.",
      "uncertainty": "Whether Neta identifies a distinction that changes the candidate telos rather than merely wording."
    },
    {
      "resource": "EXTERNAL_RESEARCH",
      "expected_contribution": "Could provide adjacent vocabulary such as value of information or optimal stopping.",
      "authority_ceiling": "Cannot decide the repository-specific R&D role by analogy alone.",
      "uncertainty": "Low current marginal decision value because internal cases already discriminate the scope question."
    }
  ],
  "candidate_moves": [
    {
      "move": "USE_EXISTING",
      "resource": "REPO_EVIDENCE",
      "expected_decision_value": "HIGH",
      "reversibility": "HIGH"
    },
    {
      "move": "INVOKE_NETA",
      "resource": "NETA",
      "expected_decision_value": "HIGH",
      "reversibility": "HIGH"
    },
    {
      "move": "TEST",
      "resource": "NEIGHBOR_FIRE_NO_FIRE_BENCHMARK_AFTER_SYNTHESIS",
      "expected_decision_value": "MEDIUM_TO_HIGH if the peer synthesis materially changes the candidate boundary",
      "reversibility": "HIGH"
    },
    {
      "move": "RESEARCH",
      "resource": "EXTERNAL_LITERATURE",
      "expected_decision_value": "LOW_NOW",
      "reversibility": "HIGH"
    }
  ],
  "needs": {
    "signal_interpretation_ambiguity": true,
    "multiple_plausible_mechanisms": true,
    "proxy_substitution_risk": true,
    "research_to_intervention_transition": true,
    "broad_reasoning_needed": false,
    "architecture_alternatives_needed": false,
    "novel_synthesis_needed": false,
    "owner_authority_needed": false,
    "repo_authority_needed": false,
    "environment_authority_needed": false,
    "field_authority_needed": false,
    "external_research_needed": false
  },
  "rationale": "The observed useful behavior is not generic research production and not generic resource allocation. R&D repeatedly decides which uncertainty merits additional epistemic effort, which evidence/learning channel is admissible, and when marginal learning no longer changes the decision. A consequential resource or method commitment often creates the need for R&D, but the same R&D loop also evaluates evidence already acquired and whether to continue, reuse, adapt, retire, wait, or stop. Therefore the commitment may be a fire condition while epistemic-effort calibration is a better candidate telos. Neta is required because the remaining uncertainty is primarily a framing/proxy distinction." 
}
```

## R&D provisional interpretation before Neta

The strongest current candidate is no longer:

> manage resources toward telos

and is not exactly:

> decide what to research before committing resources

It is closer to:

> **calibrate epistemic effort to the decision it can still change.**

This must remain provisional until Neta discriminates the competing framings.