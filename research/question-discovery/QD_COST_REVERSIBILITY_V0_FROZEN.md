# Cost / Reversibility Sensitivity Challenge v0 — Frozen

Status: `FROZEN_BEFORE_RUN · CONTROLLED_STRUCTURAL_PAIRS`
Date: 2026-09-06

## Hypothesis

If the capability is a useful pre-investment gate, its intervention threshold should depend on action cost, lock-in and informational value.

For the same underlying uncertainty:
- high-cost / low-reversibility action should trigger upstream qualification;
- cheap / reversible / informative action may be allowed to proceed as the discriminator itself.

## Pairs

### Pair A — CRM workflow friction

A-HIGH:
> The team says the CRM wastes time. Should we commit the next six weeks to migrating the whole company to a new CRM?

A-LOW:
> The team says the CRM wastes time. Should we spend 30 minutes reproducing our worst workflow in a new CRM sandbox to see whether the friction disappears?

### Pair B — Mobile demand

B-HIGH:
> Several customers ask for a mobile app. Should we fund an 8-week native iOS/Android build now?

B-LOW:
> Several customers ask for a mobile app. Should we spend an hour mocking the requested mobile workflow in the existing responsive web product and put it in front of two requesters?

### Pair C — Market uncertainty

C-HIGH:
> We are unsure why prospects are not buying. Should we commission a three-week market research project before changing anything?

C-LOW:
> We are unsure why prospects are not buying. Should we review the last five lost deals today and tag the exact point/reason each one stalled?

### Pair D — Kubernetes learning

D-HIGH:
> I want to become better at scalable systems. Should I enroll now in a 40-hour Kubernetes course?

D-LOW:
> I want to become better at scalable systems. Should I spend 20 minutes mapping which recent architecture decisions I could not make because I lacked Kubernetes-specific knowledge?

## Expected sensitivity criterion

The full capability passes this structural test only if it distinguishes `commitment requiring qualification` from `cheap action that is itself a useful discriminator`, rather than mechanically reframing both.