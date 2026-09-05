# PEER HANDOFF PROTOCOL — Neta ↔ R&D

Status: `CANONICAL_CROSS_AGENT`

Purpose: define machine-readable, non-hierarchical handoffs between peer agents.

## 1. Handoff object

Every peer handoff should preserve:

```text
handoff_id
from_agent
to_agent
live_claim_id
question
why_peer_is_needed
current_evidence_refs
current_claim_state
resolution_authority
requested_return
must_not_infer
stop_condition
```

A handoff is a request for bounded work, not delegation of final authority.

## 2. Neta → R&D

Use when a product/design decision depends on a research-owned uncertainty.

Required return should ask for one or more of:

- mechanism support/boundaries;
- construct validity;
- measurement/instrument options;
- prior null/refutation;
- evidence independence;
- falsification path;
- research authority ceiling.

R&D should not return a product intervention unless the handoff explicitly asks only for research implications and the intervention remains a Neta/OWNER decision.

## 3. R&D → Neta

Use when research has bounded the research question and the remaining uncertainty is product-specific.

Required return should ask for one or more of:

- which local mechanism is active;
- whether the product evidence meets build permission;
- owner tradeoff/intent integration;
- reversible intervention selection;
- product-specific FIELD requirement.

R&D should return the research claim state, boundaries and decision-relevant implications without pretending to own the product decision.

## 4. Peer challenge

A handoff may be a challenge rather than a continuation.

Examples:

- `CONSTRUCT_CHALLENGE`: the peer's proposed categories are not empirically separable.
- `AUTHORITY_CHALLENGE`: the peer is using RESEARCH/REPO evidence to answer a FIELD claim.
- `MEASUREMENT_CHALLENGE`: the proposed probe changes the behavior it measures.
- `RELEVANCE_CHALLENGE`: the research result is valid but does not resolve the live product decision.

Challenges must name the exact claim and what evidence could reverse the challenge.

## 5. Return object

A peer return should preserve:

```text
handoff_id
resolved_parts[]
unresolved_parts[]
new_evidence_refs[]
claim_updates[]
boundaries[]
next_authority
recommended_next_peer_or_stop
```

Do not return only prose if a machine-readable claim update can be produced.

## 6. Conflict handling

If peers disagree, do not vote.

Classify the conflict using `docs/AGENT_AUTHORITY_BOUNDARIES.md` and preserve both claim states until the correct authority/evidence resolves the disagreement.

## 7. Orchestrator compatibility

The future orchestrator should consume and emit the same handoff objects.

Its role is to maintain the dependency graph and route unresolved claims. It does not rewrite peer outputs into a single confidence score.
