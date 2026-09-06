# R&D Telos Peer Review Task — 2026-09-06

Status: `FROZEN_BEFORE_ROLE_CONDITIONED_RUN · REPO_GROUNDED · NOT_CANONICAL`

## Owner goal

Determine whether the emerging formulation of R&D as an **epistemic-budget manager** is more precise and useful than the current v0.2 telos, using R&D itself plus Neta as a framing/discrimination peer.

## Current v0.2 telos

> Improve the fit between the system's resources and its telos, given the state from which the system is actually starting.

## Candidate owner formulation

> R&D decides what is worth learning before we spend meaningful resources or turn a way of thinking into policy.

Related intuition:

> Before R&D researches the topic, it investigates what is actually worth researching / learning.

## Decision to make

Should the R&D telos be narrowed away from generic resource↔telos calibration toward a specific function of **calibrating epistemic effort to decision value**? If yes, what is the narrowest formulation that preserves observed material R&D value without collapsing into Neta, local response policy, OWNER, authority lookup, or orchestration?

## Evidence already available

1. `research/RND_AGENT_TELOS_REFOUNDATION_V0_2.md`
   - broad resource↔telos formulation;
   - contains narrower mechanism: cheapest admissible information that can change resource allocation.

2. `research/question-discovery/QD_VS_RND_V0_RUN.md`
   - commitment/question gate produced no unique epistemic decision beyond R&D + Calibration Loop;
   - suggests R&D already owns the deeper learning/allocation judgment.

3. `research/question-discovery/QD_YISHUMI_HOLDOUT_V0_ADJUDICATION.md`
   - full R&D materially changed 8/20 mechanically selected historical tasks;
   - 12/20 were no-material-delta and should bypass.

4. `research/rnd-agent/telos/RND_TELOS_SELF_CALIBRATION_2026-09-06.md`
   - candidate: reduce decision-controlling uncertainty enough to justify/reject consequential resource commitment using cheapest admissible learning move.

5. `research/rnd-agent/telos/RND_NARROW_TELOS_BENCHMARK_V0_ADJUDICATION.md`
   - narrow v0 agreement 12/13;
   - material recall 5/6 (83.3%);
   - one miss: cheap-per-use but reusable reasoning topology (`Waze` protocol) that becomes durable epistemic policy.

## Required peer roles

### R&D pass
Use `prompts/RND_AGENT_V0_2_CANDIDATE.md` as the role contract.
Diagnose whether the candidate formulation better explains R&D's useful decision delta and propose the cheapest next learning needed.

### Neta pass
Use `prompts/SYSTEM.md` as the role contract.
Treat the candidate telos wording as a raw signal / proposed interpretation. Identify competing mechanisms and one discriminator. In particular challenge:
- `budget` as possible metaphor/proxy;
- `before` as possible temporal over-narrowing;
- `research` as possible activity/output confusion;
- `resource commitment` as possible trigger confused with telos.

### R&D synthesis
After seeing Neta, R&D must compare the original v0.2 telos, the owner's candidate, its own DIAGNOSE, and Neta's discrimination.
Return a bounded candidate telos, fire/no-fire implications, what Neta uniquely changed, and whether to STOP or CONTINUE.

## Promotion prohibition

This run may create a candidate telos only. It may not silently modify canonical docs/prompts.

## Runtime limitation

The current execution environment does not expose `OPENAI_API_KEY`, so this run will be role-conditioned manual application of the frozen peer prompts, not `runtime/calibration_loop/run.py --strict`. Any result must retain that evidence ceiling.