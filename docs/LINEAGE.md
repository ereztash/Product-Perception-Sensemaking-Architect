# LINEAGE — portfolio mechanisms Neta inherits

Neta is not being invented from a blank page. Her method is a transfer of recurring mechanisms already implemented or argued in Erez's portfolio.

This file records **lineage, not universality**. A mechanism repeated across one operator's portfolio is still not external replication.

| Principle in Neta | Portfolio source | What transfers |
|---|---|---|
| **State should nearly dictate the next action** | `lichess_app/docs/INERTIAL_UX_LAWS.md` | The user should not need to understand product architecture to know what to do now. |
| **Visual salience must agree with product state** | `lichess_app/docs/VISUAL_ARCHITECTURE_AUDIT.md` | One logical primary action is insufficient if the eye ranks other regions above it. |
| **Measurement before intervention** | `lichess_app/docs/INERTIAL_UX_LAWS.md` | Do not expose prior evidence while the user is producing evidence that exposure could contaminate. |
| **One current next move** | `pre-call/README.md`, `pre-call/docs/market-ready.md` | A surface should not say “here is everything, figure it out”; current state should resolve to one action. |
| **Speak in felt language, think in technical constructs** | `proofminer/docs/UX.md` | Internal diagnosis can be technical; user-facing language should be something the person could actually say about themselves. |
| **First light before dashboard** | `proofminer/docs/UX.md` | Early value should reveal something concrete before exposing the full system architecture. |
| **Mirror, not judge** | `CRM_Google_ai/README.md` | Describe evidence and ownership without turning low signal into a character judgment. |
| **Score/claim authority cannot outrun evidence** | `proofminer/README.md`, `anti-silo/README.md` | A polished output must remain narrower than the measurement that supports it. |
| **Separate score from permission** | `anti-silo/README.md` | “How good is the evidence?” and “what does it authorize?” are different questions. |
| **Not measured is not zero** | `MATI/README.md`, `lessons` methodology | Missing evidence should remain explicitly missing rather than converted into a negative score. |
| **One insight object should include answer, reason, uncertainty and action** | `ampaign-craft/README.md` (`InsightActionCard`) | Keep recommendation, rationale, confidence state and next move coherent rather than scattered. |
| **A gate must be shown capable of failure** | `--Android/README.md`, `lessons` | A validator that has never rejected a deliberate defect has not demonstrated that it gates anything. |
| **The expert's hidden judgment is the productization target** | `Agent-Architect/README.md` | After every case ask what the expert did implicitly that the prompt did not yet encode. |
| **Start from the symptom, not required vocabulary** | `strategic-portal/README.md` | Users can describe “robotic text” or another symptom; the system performs the technical translation. |

## The synthesis Neta adds

The portfolio contains the ingredients separately. Neta combines them into one explicit sensemaking loop for product perception:

```text
owner intuition
→ preserve raw wording
→ locate the moment
→ separate observable from inference
→ generate neighboring mechanisms
→ buy the cheapest distinguishing information
→ name the distinction
→ assign resolution authority
→ make the smallest bounded intervention
→ record what the owner learned
```

## What is new and therefore provisional

The following are Neta-specific syntheses, not yet established portfolio-wide principles:

- the seven-lens set: Perception / Orientation / Action / Feedback / Payoff / Accumulation / Trust;
- learning an owner's private metaphor vocabulary as probabilistic mappings;
- making design-discrimination transfer to the owner an explicit success criterion;
- `DESIGN_MECHANISM` as a resolution-authority class distinct from `OWNER`, `REPO`, and `FIELD`.

Treat these as hypotheses until repeated use earns stronger language.
