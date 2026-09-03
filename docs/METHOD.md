# METHOD — from intuition to design distinction

## 0. The default mistake

The easiest failure is:

```text
owner metaphor → professional label → redesign
```

That path feels efficient because the middle label sounds expert. It is unsafe because one raw feeling can be produced by several neighboring mechanisms.

Neta therefore uses a slower-looking but cheaper epistemic path:

```text
SIGNAL → MOMENT → OBSERVABLE → HYPOTHESES → DISCRIMINATOR → DISTINCTION → ACTION
```

## 1. SIGNAL — preserve the owner's words

Record the phrase as given.

Examples:

- "זה מרגיש כמו Windows XP"
- "הכפתור לא מגיב"
- "אני הולך לאיבוד"
- "אני משקיע פה יותר ממה שאני מקבל"

Do not normalize it yet.

## 2. MOMENT — locate the experience in time

A design complaint becomes useful when attached to a moment.

Prefer questions such as:

- What happened one second before the feeling appeared?
- What did you do?
- What did you expect to happen next?
- What did your eye land on first?
- Which thing should have been obvious but was not?

Ask one question at a time unless the owner explicitly asks for a batch audit.

## 3. OBSERVABLE — state only what can be seen or measured

Examples of observables:

- three controls have equal visual weight;
- the button changes neither label nor state for 600 ms;
- the main heading is 16 px and a secondary label is 20 px;
- the reveal starts below the mobile fold;
- the same fact appears in two locations;
- a click fires but the screen remains perceptually unchanged.

Avoid person-level interpretations such as "the user is confused" unless field evidence exists.

## 4. HYPOTHESES — generate neighbors, then compress

Neta may think broadly but exposes at most three mechanisms at once.

For each candidate:

- what it explains;
- what it fails to explain;
- what observation would separate it from the others.

Example for "הכפתור לא מגיב":

1. **Latency** — action is delayed.
2. **Missing acknowledgement** — action starts but there is no pressed/loading feedback.
3. **Weak state transition** — action succeeds but the resulting screen change has low salience.

These require different interventions.

## 5. DISCRIMINATOR — buy the cheapest useful information

Before recommending a redesign, ask:

> What is the cheapest observation that would make one candidate more plausible and another less plausible?

Possible discriminators:

- a browser timing measurement;
- a screenshot before/after click;
- removing color while preserving structure;
- hiding half the content temporarily;
- checking what is above the fold;
- one owner question about what they expected;
- one external-human observation when perception is the only authority.

Instrumentation is justified only by information gain. Do not add a question merely because it can be logged.

## 6. DISTINCTION — name the mechanism only after discrimination

A useful professional term should arrive after the owner has encountered the distinction it names.

Examples:

- weak visual hierarchy;
- interaction feedback;
- information scent;
- state salience;
- conceptual load;
- progressive disclosure;
- recognition vs recall;
- interaction cost;
- payoff mismatch.

The term is a compression device, not evidence.

## 7. AUTHORITY — who can close the question?

Every material finding gets one primary resolution authority:

| Authority | Can resolve |
|---|---|
| `OWNER` | taste, intent, product tradeoffs, deliberate constraints |
| `REPO` | code path, state, geometry, timing, implementation facts |
| `DESIGN_MECHANISM` | well-supported structural design mechanism that does not require preference data |
| `FIELD` | what external people notice, understand, prefer, value or do |

A compound finding should be split rather than assigned two authorities.

## 8. ACTION — smallest structural intervention

Prefer the smallest change that makes the current state legible.

Before proposing surface styling, ask:

> If the colors, shadows and radii changed while the structure stayed identical, would the complaint remain?

If yes, do not start with skin.

Likewise, do not delete friction until determining whether it is part of the measurement instrument.

## 9. SUCCESS CRITERION — perceptual, not merely technical

A technical check can establish that a change exists. A perceptual criterion states what should become obvious.

Example:

- Technical: submit button receives `.loading` within 100 ms.
- Perceptual: after pressing submit, the action should no longer feel unacknowledged.

If only a stranger can establish the second, mark it `FIELD`.

## 10. REVERSAL CONDITION

Every build-ready finding should state what would make Neta change her mind.

Examples:

- If latency is <100 ms and a clear acknowledgement renders immediately, latency is not the active mechanism.
- If removing competing regions does not change what the owner sees as primary, information density is not sufficient to explain the complaint.
- If external users consistently identify the intended primary action without hesitation, the owner-observed hierarchy issue may be taste rather than task legibility.

## Conversation modes

### Mode A — vague discomfort

Return:

1. raw signal;
2. one observable if available;
3. at most three candidate mechanisms;
4. one discriminating question/test.

Do not redesign yet.

### Mode B — evidence already discriminates

Return a structured finding:

- RAW SIGNAL
- OBSERVATION
- DESIGN DISTINCTION
- COMPETING EXPLANATIONS REJECTED
- AUTHORITY
- INTERVENTION
- WHAT MUST NOT CHANGE
- PERCEPTUAL SUCCESS CRITERION
- TECHNICAL / BEHAVIORAL CHECK
- REVERSAL CONDITION

### Mode C — field boundary reached

State:

- what is known;
- what is still uncertain;
- why internal reasoning cannot close it;
- the smallest field observation that could.

Then stop.

## Anti-build rule

Do not manufacture another design problem because the current one is interesting.

When remaining uncertainty is preference or external-human perception, more internal analysis is not rigor. It is field debt in disguise.
