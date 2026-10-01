# `resource` is not `authority`

A contract note, written because a task author read the calibration schema as having a gap and
recorded it as one. The reading was wrong, the schema is right, and nothing said so anywhere.

## The apparent defect

`docs/SHARED_EPISTEMIC_KERNEL.md` lists five resolution authorities:

```text
OWNER · REPO · ENVIRONMENT · RESEARCH · FIELD
```

`schemas/calibration-task.schema.json` accepts seven resources and `RESEARCH` is not among them:

```text
RND · NETA · SCAFFOLD · OWNER · REPO · ENVIRONMENT · FIELD
```

`CAL-LICHESS-LEARNING-JOURNEY-001` was a task whose binding constraint was a RESEARCH-owned fact —
that the discovery pipeline cannot reach CAUSALITY, INTERVENTION or OUTCOME under any result — and
its author could not name RESEARCH as available. That was recorded in the task's own constraints as
a schema gap, and repeated into the trace's `resource_delta`. **Both of those descriptions are
wrong**, and this document is the correction; the task and the trace are not edited, because they
are the frozen record of what was believed at the time.

## Why the two lists differ

They are lists of different things, and the field names say so.

**Authority** is a property of a *claim*: the source that can legitimately close it. The kernel's
heading is literally "Resolution authority", and `schemas/rnd-research-task.schema.json` carries that
same five-value enum on a field named `resolution_authority`. Authority belongs to the claim, not to
whoever holds the task.

**Resource** is a property of a *run*: what this loop can invoke or hand off to. The calibration
schema's fields are `available_resources` and `allowed_resources`, and their enum mixes two
populations that the authority list does not contain together — three invocable peers (`RND`,
`NETA`, `SCAFFOLD`) and four authorities a run can stop at.

So the enums are not two versions of one list. Asking why `RESEARCH` is missing from one is like
asking why `NETA` is missing from the other.

## Where RESEARCH actually lives in this runtime

It is reachable, and it is not an authority handoff. `runtime/calibration_loop/routing.py` has:

- four `AUTHORITY_FLAGS` — `owner`, `repo`, `environment`, `field` — each producing a stop;
- a separate need key, **`external_research_needed`**, which fires as `RND_RESEARCH`.

Research is work the loop **does**, through R&D, rather than a body it **defers to**. That is why it
is a need and not a handoff, and it is the substantive reason the enum is shaped as it is.

## The falsifiable form

> **Claim.** The Calibration Loop can route research work without `RESEARCH` appearing in the
> resource enum, because research is requested through `external_research_needed` and served by RND.
>
> **What would falsify it.** A task whose remaining uncertainty is RESEARCH-owned, where
> `external_research_needed` fires, and where the runtime then has nowhere to send it — or a task
> that needs to *stop* at RESEARCH the way it can stop at FIELD, with no way to express that.

In `CAL-LICHESS-LEARNING-JOURNEY-001` the key was present and R&D set it **false**: the
RESEARCH-owned fact was already in hand, so more research had no decision value. The pathway was
declined, not missing. That is one observation and it does not close the second half of the
falsifier.

## The one thing that is genuinely open

A run cannot **stop at RESEARCH** the way it stops at OWNER or FIELD. `WAITING_AUTHORITY` exists in
the R&D adapter's result vocabulary, and there is no `research_authority_needed` flag to reach it
from a calibration run. Whether that is a real gap depends on a question no run has yet posed: is
there a decision this loop can reach whose remaining uncertainty belongs to RESEARCH and which R&D
itself cannot work?

**Not answered here, and not patched here.** Widening the enum before that question has an instance
would be adding a value nothing can produce, which is the kind of change this project's own rules
call unearned. The trigger to revisit: a calibration task that stalls with research-owned
uncertainty R&D declines to work.
