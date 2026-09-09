# Execution deviation 01 — builder substitution before generation

Date: 2026-09-09
Applies to: `PREREGISTRATION_2026-09-09.md`
Status: `RECORDED_BEFORE_SUCCESSFUL_GENERATION`

## Trigger

The preregistration named Lovable as the common builder. The first Stage-1 Arm A creation call was rejected before project creation because the user-owned Lovable workspace had no credits. No Arm A or Arm B artifact was generated under this preregistered Stage-1 attempt, so no outcome was observed before this deviation was recorded.

## Substitution

For Stage 1 only, substitute the common builder with GitHub Copilot CLI running in one GitHub Actions job.

Controls:
- same Copilot CLI version for both arms;
- provider-default model for both arms; exact model lineage is recorded as unknown unless the CLI exposes it;
- separate empty working directories per arm;
- separate non-interactive CLI process per arm;
- `--no-custom-instructions`;
- no network/tooling needed beyond local file write and local shell checks;
- static HTML/CSS/JavaScript prototype format for both arms so dependency/toolchain choice cannot dominate the comparison;
- one generation turn per arm;
- no repair before scoring;
- exact frozen Arm A and Arm B prompts remain unchanged.

The hypothesis, target domain, endpoints, gates, and Stage-1 decision rule do not change.

## Interpretation boundary

Any result applies to this Copilot-CLI builder setting, not Lovable. It cannot be combined with the earlier Lovable outreach prototype as if it were a replication under one builder.
