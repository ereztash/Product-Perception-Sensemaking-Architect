# R&D Self-Scope Discovery — SYNTHESIS

Status: `ROLE_CONDITIONED_MANUAL_RND_SYNTHESIS · NETA_REVIEWED · REPO_GROUNDED · NOT_RUNTIME_EXECUTION · NOT_CANONICAL`
Date: 2026-09-06

## decision_before

The system had a strong but still broad candidate claim:

> R&D exists to calibrate inquiry/learning effort to uncertainty that can still change a consequential decision.

The owner requested a program that discovers the actual operating boundary where R&D gives the most value and does not stop until the boundary claim receives >95% evidential support.

## decision_after

The strongest current **scope hypothesis** is narrower than the telos:

> **R&D's highest marginal value should concentrate where a consequential decision remains open AND there is a nontrivial unresolved choice about whether, how, or how much to learn.**

Nearest negative neighbor:

> consequential decision + uncertainty exists, but one direct legitimate authority or one cheap reversible discriminator already dominates.

This distinction must be tested, not promoted.

## Neta resource delta

`material: YES`

Neta prevented a circular benchmark by separating:
- pre-outcome task features;
- post-outcome R&D failure/diagnosis labels.

Preferred pre-outcome axes:
1. decision consequence;
2. epistemic allocation burden;
3. resolution structure;
4. learning phase.

Modifiers such as cost, delay, contamination and reusable-policy impact remain secondary until evidence shows independent boundary effects.

## statistical scaffold delta

`material: YES`

The owner's “do not stop until >95% certainty” requirement makes fixed-N evaluation insufficient if the system repeatedly checks the result while adding cases.

The protocol therefore requires sequentially valid confidence evidence:
- preferred: time-uniform confidence sequences;
- conservative fallback: familywise alpha-spending one-sided binomial bounds across prespecified looks/endpoints.

The 95% claim applies to frozen statistical boundary statements under the sampled task distribution; it is not subjective confidence.

## primary program

1. freeze tested prompts, coding manual and outcome rubric;
2. discovery on natural historical tasks — discovery only, no confirmation credit;
3. freeze at most a small number of primary scope regions and nearest neighbors;
4. prospective / independently frozen unseen natural cases;
5. paired CURRENT_RND vs strong baseline with same base model where possible;
6. blinded independent adjudication from different model lineage or qualified humans;
7. sequential accumulation until prespecified scope bounds cross;
8. no retrofitting: any scope repair creates a new version and new confirmatory stream.

## high-value core promotion rule

A region may be called `HIGH_VALUE_CORE` only after minimum balance/sample requirements and when simultaneous/anytime-valid bounds establish all of:

- lower bound on material-win rate > 0.50;
- upper bound on material-loss rate < 0.05;
- conservative lower net-benefit bound > 0;
- separation from nearest negative neighbors, or else the regions are merged/reported as co-high-value.

Minimum confirmatory floor: 60 independent adjudicable cases per promoted critical region, with PRE/MID/POST and domain balance where applicable.

## stop_or_continue

`CONTINUE`

The **design task** is complete enough to execute.

The **scope research** is not complete and must not stop yet.

## why >95% is not currently claimable

Existing evidence cannot satisfy the requested threshold because most prior runs are same-model/manual and the current environment has no `OPENAI_API_KEY` for live independent adapter execution.

Repeatedly generating more same-lineage self-tests would create apparent sample size without independent information and would violate the existing eval protocol.

Therefore:

`95PCT_SCOPE_CERTAINTY = NOT_YET_ACHIEVED`

The next legitimate move is independent natural-case collection and paired evaluation under the frozen program.

## artifacts

- `RND_SELF_SCOPE_DISCOVERY_TASK_2026-09-06.md`
- `RND_SELF_SCOPE_DISCOVERY_DIAGNOSE_2026-09-06.md`
- `NETA_SCOPE_DECOMPOSITION_REVIEW_2026-09-06.md`
- `RND_SCOPE_DISCOVERY_PROGRAM_V0_1.md`
- `schemas/rnd-scope-case.schema.json`

## current disposition

`SCOPE_HYPOTHESIS: CONSEQUENTIAL_DECISION × NONTRIVIAL_EPISTEMIC_ALLOCATION`

`PROGRAM: EXECUTABLE`

`BOUNDARY: NOT_YET_VALIDATED`

`95PCT_STOP_RULE: FROZEN`
