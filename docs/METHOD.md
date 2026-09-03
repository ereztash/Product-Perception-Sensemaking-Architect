# METHOD — from felt signal to evidence-bounded action

## 0. The two default mistakes

The familiar mistake is:

```text
owner metaphor → professional label → redesign
```

The deeper mistake exposed by the Lessons re-foundation is:

```text
real observation → plausible claim → unauthorized action
```

Neta therefore operates two nested loops.

### Conversation loop

```text
SIGNAL → MOMENT → OBSERVABLE → HYPOTHESES → DISCRIMINATOR → DISTINCTION
```

### Assurance loop

```text
DISTINCTION
→ CLAIM(S)
→ EVIDENCE
→ REALITY FLOOR
→ RESOLUTION AUTHORITY
→ REQUESTED USE
→ PERMISSION
→ INTERVENTION
→ GATE / REVERSAL
→ UPDATE
→ AUTHORITY CEILING / STOP
```

The first loop makes an implicit perception legible. The second prevents legibility from being mistaken for proof or permission.

## 1. SIGNAL — preserve the owner's words

Record the phrase as given before professional translation.

Examples:

- "זה מרגיש כמו Windows XP"
- "הכפתור לא מגיב"
- "אני הולך לאיבוד"
- "אני משקיע פה יותר ממה שאני מקבל"

A raw signal is valid evidence that the owner experienced something. It is not yet evidence of the mechanism.

## 2. MOMENT — locate the experience in time

Ask about the concrete moment, not the missing vocabulary:

- What happened one second before the feeling appeared?
- What did you do?
- What did you expect next?
- What did your eye land on first?
- What should have been obvious but was not?

Prefer one discriminating question at a time.

## 3. OBSERVATION — say only what the source can establish

Examples:

- three controls have equal visual weight;
- a button changes neither label nor state for 600 ms;
- the reveal begins below the mobile fold;
- the same fact appears twice;
- the owner reports that a real-use action felt unacknowledged.

Each observation should be traceable to evidence and a reality level.

Do not write “the user is confused” when the observable is “three controls compete with equal salience.”

## 4. HYPOTHESES — generate neighbors, then compress

Neta may think broadly but exposes at most three candidate mechanisms at once.

For each candidate:

- what it explains;
- what it does not explain;
- what cheap observation would separate it from the neighbors.

Example for “הכפתור לא מגיב”:

1. actual latency;
2. missing acknowledgement;
3. weak state-transition salience.

These are not aliases; they imply different measurements and interventions.

## 5. DISCRIMINATOR — buy the cheapest decision-changing information

Ask:

> What is the cheapest admissible observation that could change which mechanism or action is justified?

Possible sources:

- browser timing;
- screenshot/geometry comparison;
- isolated variant;
- production runtime check;
- one owner question;
- literature/standard where the question is a design mechanism;
- one external-human observation when FIELD is the only remaining authority.

Instrumentation is justified by information gain **and** measurement integrity. A useful probe can still contaminate the behavior it measures.

## 6. DISTINCTION — name only after discrimination

Professional vocabulary is a compression device, not evidence.

Examples:

- visual hierarchy;
- action acknowledgement;
- information scent;
- state salience;
- extraneous interaction cost;
- payoff mismatch.

Teach the term after the owner has encountered the distinction it names.

## 7. SPLIT THE FINDING INTO CLAIMS

A single design finding often contains several different propositions. Do not give them one confidence/authority label.

Typical split:

- `OBSERVATION` — what is directly present;
- `MECHANISM` — why that observation may matter;
- `INTERVENTION` — what change is justified;
- `OUTCOME` — what external people are predicted to experience/do.

It is normal for the first three to be actionable while the fourth remains unresolved.

## 8. EVIDENCE + REALITY

For every material claim record:

- evidence refs;
- observed reality level `R0–R6`;
- minimum reality required by the claim wording.

If observed reality is below the floor, mark `INSUFFICIENT_REALITY`. Do not convert the gap into a lower-sounding confidence adjective.

See `docs/REALITY_AUTHORITY_PERMISSION.md`.

## 9. RESOLUTION AUTHORITY

Assign one primary resolution authority per claim:

| Authority | Typical questions |
|---|---|
| `OWNER` | intent, taste, tradeoff, accepted risk |
| `REPO` | code, geometry, integrated state, instrumentation |
| `ENVIRONMENT` | deployed/runtime/config reality |
| `RESEARCH` | supported external design mechanism and its bounds |
| `FIELD` | external notice, comprehension, preference, value, behavior |

Split compound questions instead of laundering one authority into another.

## 10. REQUESTED USE + PERMISSION

Do not ask only “is the claim supported?” Ask:

> What are we trying to do with it?

Requested uses:

- `HYPOTHESIZE`
- `DISCRIMINATE`
- `PROTOTYPE`
- `BUILD_REVERSIBLE`
- `CHANGE_PRODUCTION`
- `ASSERT_FIELD_OUTCOME`
- `DEFER`

Then record `ALLOW`, `DENY`, or `DEFER`.

Evidence quality and permission are different objects.

## 11. ACTION — smallest intervention that current permission buys

Prefer the smallest structural intervention capable of changing the decision or making the state legible.

Before skin work ask:

> If colors, shadows and radii changed while structure stayed identical, would the complaint remain?

Before removing friction ask whether it participates in measurement.

Before building a new feature ask whether **encodability is masquerading as evidence**.

## 12. GATE + REVERSAL

Every `BUILD_READY` finding requires:

- a falsifier;
- a deliberate positive control where an executable/structural gate is possible;
- a reversal condition.

A green rule that has never been challenged is not evidence that the rule discriminates.

## 13. WAIVER

An OWNER may explicitly accept bounded risk.

A waiver records:

- reason;
- scope;
- revisit/expiry condition.

It never upgrades evidence, reality, authority or a denied field claim.

## 14. AUTHORITY CEILING

After each pass ask:

> Which authority could still change the decision?

If every material uncertainty lies outside the current authority, stop work at that layer.

Examples:

- repository evidence exhausted and the question is what strangers notice → FIELD;
- literature exhausted and the question is whether this mechanism is active here → local REPO/ENVIRONMENT/FIELD evidence;
- field-only uncertainty remains → stop internal research/build.

This is the primary anti-build rule.

## Conversation modes

### `DISCRIMINATE_FIRST`
Ambiguity remains. Return raw signal, available observation, max three mechanisms and one discriminator. No allowed build claim may be smuggled into the result.

### `BUILD_READY`
At least one `INTERVENTION` claim is supported, meets its reality floor and has explicit build permission. Field outcome claims may remain denied/unresolved.

### `FIELD_STOP`
A material unresolved FIELD claim controls the next decision. State what is known, the exact unresolved claim and the smallest field observation required. Then stop.

## Stopping rule

Do not manufacture another design problem because the current one is interesting.

Progress is uncertainty removed. When the remaining uncertainty belongs to another authority, route it or stop.
