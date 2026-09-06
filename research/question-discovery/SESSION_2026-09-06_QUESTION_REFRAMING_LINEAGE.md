# Question Reframing Lineage — 2026-09-06

Status: `DURABLE_RESEARCH_DEPOSIT · PRODUCT_HYPOTHESIS_CANDIDATE · NOT_YET_CANONICAL`

Session theme: System Design → Architecture → Solution Architecture → Architecture Drivers → Question Discovery

## Why this document exists

During one continuous session, the owner repeatedly asked a reasonable question and the R&D method changed the **question that was worth resolving before buying more information or building anything**.

The important observation is not that the answers were good. It is that the system repeatedly identified a more decision-relevant question that the owner plausibly would have asked **if the missing domain distinctions had already been available to him**.

This document preserves the exact lineage as product evidence.

The candidate product-level phenomenon is:

> **Given a user's current question, identify the question they would most benefit from asking before paying to answer the current one.**

Working candidate names:
- `Decision Question Discovery`
- `Question Discovery`
- `The Question Before the Question`

No name is canonical yet.

---

## Q1 — Is this topic worth deepening, and does it belong to R&D or Neta?

### Owner question

> "אני להפעיל את R&D בשביל להבין האם יש כאן צורך בהעמקה בנושא הזה, והאהם זה לא תת תחום שלו או של נטע"

### Surface interpretation

The apparent question was whether the System Design / technical architecture material was important enough to study, and which existing peer should own it.

### Question the repo actually resolved

> **Is there an independent functional gap in the system, or is this merely domain knowledge/capability inside an already-owned function?**

More formally:

```text
TOPIC EXISTS
≠
NEW FUNCTION EXISTS
≠
NEW AGENT IS JUSTIFIED
```

### Repo answer

The repository already contained `Architecture Decision Discriminator v0` with status `CANDIDATE_CAPABILITY_NOT_AGENT`.

Therefore the current move was **not** to create an Architect peer and not to assign the whole subject to Neta or R&D. R&D owns whether the capability deserves resources; Neta may discriminate the meaning of a product signal; architecture-specific structural judgment remains a candidate capability.

### Decision delta

Before: `Should I deepen System Design / who owns it?`

After: `First test whether architecture-specific judgment is an independent decision capability at all.`

This prevented topic importance from being mistaken for an agent boundary.

---

## Q2 — Let's deeply research the videos and these topics

### Owner question

> "מעולה, אני רוצה שנחקור לעומק את הסר טונים והנושאים האלה"

Followed by:

> "תשתמש בריפו בשביל לחקור, זה בדיוק התפקיד שלו"

### Surface interpretation

A broad System Design literature/video review: caching, queues, replication, CDN, observability, indexing, sharding, etc.

### Question the repo actually resolved

> **Which distinctions from this body of knowledge produce a unique material decision delta in the existing Architecture capability, and which merely add vocabulary/pattern recall?**

The research unit changed from `TOPIC` to `DECISION DISTINCTION`.

### Repo answer

Historical recovery over real repository decisions showed that much of generic System Design knowledge was already represented by existing architecture objects such as:

- `STATE_AUTHORITY`
- `INVARIANT`
- `TEMPORAL_COUPLING`
- `FAILURE_DOMAIN`
- `MIGRATION_PATH`
- `REVERSIBILITY`

The broad candidate expansion was therefore narrowed.

The residual that survived was approximately:

```text
MATERIAL_PRESSURE
├─ REQUIRED_PROPERTY / SERVICE OBJECTIVE
├─ RELEVANT WORKLOAD / RESOURCE CONDITIONS
└─ OBSERVED BOTTLENECK / LIMIT EVIDENCE
```

### Decision delta

Before: `Research System Design deeply.`

After: `Research only the distinctions that can change an architecture decision; keep mechanisms such as Redis/Kafka/sharding on-demand.`

This prevented curriculum-building from being mistaken for capability improvement.

---

## Q3 — What stands behind architecture, and what do we call the person who fits architecture to the need?

### Owner question

> "אז בוא נלך צעד אחד אחורה, מה עומד מאחורי אכיטרטורה איך קוראים לאדם שמומחה בהתאמת הארכיטקטורה לצורך?"

The surface professional label proposed was `Solution Architect`.

The owner then explicitly asked:

> "בוא ננסה להריץ על זה שוב את ריפו"

### Surface interpretation

Identify the correct profession/domain name.

### Question the repo actually resolved

> **What exact transformation is currently unowned?**

The role label was treated as weak evidence. The repository instead isolated the candidate transformation:

```text
ACCEPTED NEED
+ CONSTRAINTS
+ REQUIRED QUALITIES
→ STRUCTURAL OPTIONS
→ TRADEOFF
→ BOUNDED ARCHITECTURE DECISION
```

### Repo answer

Most of the structural decision layer was already owned by `Architecture Decision Discriminator v0`.

`Solution Architecture` therefore looked less like a new peer and more like a **better professional framing of the telos of the existing Architecture candidate**.

The strongest remaining residual was narrower: the current architecture capability may begin too late, after architecture-relevant requirements are already supplied.

Candidate front door:

```text
ACCEPTED NEED
+ OWNER / FIELD constraints
→ ARCHITECTURE-RELEVANT REQUIREMENTS
→ REQUIRED QUALITY ATTRIBUTES / ACCEPTANCE CRITERIA
→ MATERIAL PRESSURE
→ existing Architecture Decision Discriminator
```

### Decision delta

Before: `Is Solution Architect the missing expert/agent?`

After: `Do we have an unowned need→requirements translation before the existing architecture decision method?`

This prevented an industry job title from becoming an ontology decision.

---

## Q4 — Exhaust the repo on Solution Architecture, then go to open source / YouTube / other languages

### Owner question

> "בוא נבצע על הנושא הזה מיצוי מידע מתוך הריפו, וכשלא נסליח לצממם ודאות בנושא נפנה לאופן סורס, סרטונים ביוטיוב, קרים של אחרים, וכמובן בשפות שונות, הכל עם הריפו"

### Surface interpretation

Run a comprehensive internal-then-external research program on Solution Architecture.

### Question the repo actually resolved first

> **Can the current internal benchmark even test the missing front-door transformation, or has the benchmark already pre-specified the information whose value we are trying to test?**

### Repo answer

The existing architecture benchmark contained 12 historical cases across 4 repositories and was methodologically useful for architecture-decision delta.

However, those cases were already expressed as `decision_question + known_constraints + authorities`. In other words, the benchmark largely starts **after** the messy need has already been translated into architecture-relevant language.

Therefore it cannot establish that the front-door translation is unnecessary.

The internal corpus then showed repeated examples of human/owner language being translated into system properties:

- "the button doesn't feel responsive" → immediate acknowledgement vs completion latency;
- "database available" → actual reachability within a bounded deadline, not configuration presence;
- persistence concern → durability + restore path;
- return-to-state concern → resumability without contaminating think-time measurement;
- production readiness → security / observability / performance / disaster-recovery requirements, while heavier infrastructure was rejected as premature for pilot scale.

The internal residual was narrowed again to a candidate `Architecture Drivers` layer: the transformation from accepted need into architecture-relevant requirements, quality attributes, constraints, acceptance criteria, and conflicts.

### Decision delta

Before: `Do exhaustive research on Solution Architecture, then external sources.`

After: `First prove and formalize the Architecture Drivers translation gap; external research is authorized only for the residual questions that internal evidence cannot resolve.`

This prevented an invalid benchmark and broad literature collection from answering a question they were structurally unable to answer.

---

## Q5 — Meta-observation: the system keeps finding the question I would have asked if I knew how to formulate it

### Owner observation

> "תבחן את הסשן הזה, שים לב כמה פעמים סוכן הR&D מצא את השאלה שהייתי ידוע לשאול אם רק הייתי יודע לנסח אותה בצורה המועילה ביותר"

Then:

> "רק זה, מוצר בפני עצמו"

### Candidate product question exposed by the session

> **Can question reformulation itself be isolated, benchmarked and delivered as a standalone capability whose output is the most decision-relevant question to resolve next?**

### Candidate transformation

```text
USER'S CURRENT QUESTION
→ UNDERLYING DECISION
→ HIDDEN ASSUMPTIONS / PREMATURE OBJECTS
→ NEIGHBORING QUESTION SPACE
→ MOST DECISION-CHANGING QUESTION
→ CHEAPEST ADMISSIBLE WAY TO RESOLVE IT
```

### What the session establishes

The session provides **observational product evidence** that this transformation occurred repeatedly and materially changed the next move.

It does **not** yet establish:

- that the capability generalizes beyond this owner/session;
- that R&D is the minimal implementation of it;
- that users prefer or understand the reformulated question;
- that the reformulation improves downstream outcomes in prospective tests;
- that the capability should be a peer agent rather than a bounded method/tool.

### Candidate value proposition

> Before paying to answer your question, determine whether it is the question that should be answered.

Or more operationally:

> Turn a reasonable but under-specified question into the decision-grade question whose answer can actually change what you do.

---

## Cross-session pattern

Across the four substantive research turns above, the direction of improvement was consistent:

```text
TOPIC
→ FUNCTION

CONTENT TO LEARN
→ DECISION DISTINCTION TO ACQUIRE

JOB TITLE
→ UNOWNED TRANSFORMATION

BROAD RESEARCH PROGRAM
→ VALID TEST OF THE RESIDUAL UNCERTAINTY
```

The recurring move is **not ordinary clarification**.

Ordinary clarification asks the user to state missing parameters more precisely.

The observed move here is different:

> The system changes the object of inquiry because the user's current vocabulary does not yet contain the distinction required to formulate the most useful question.

That is the candidate product mechanism.

---

## Product hypothesis v0

### Candidate name
`Decision Question Discovery`

### Telos

> Identify the question whose resolution removes the most material uncertainty from the user's actual decision before resources are spent answering a weaker question.

### Unit of work
One unresolved user question tied to one consequential decision.

### Input
- user's current question;
- available context;
- current decision/use;
- known constraints/evidence when available.

### Output
1. `QUESTION_AS_ASKED`
2. `UNDERLYING_DECISION`
3. `PREMATURE_ASSUMPTION / OBJECT`, if present
4. `COMPETING QUESTION FRAMINGS` — bounded set
5. `DECISION_GRADE_QUESTION`
6. `WHY IT DOMINATES THE ORIGINAL`
7. `CHEAPEST DECISION-CHANGING CHECK`
8. `WHAT WOULD MAKE THE ORIGINAL QUESTION SUFFICIENT`

### Non-goals
- make every question sound more sophisticated;
- expand scope automatically;
- replace OWNER intent;
- endlessly recurse into meta-questions;
- refuse to answer a sufficiently good question;
- reward abstraction over action.

### Success criterion
A reformulation counts only if it changes at least one of:
- evidence that should be collected;
- resource that should be invoked;
- option set;
- build/defer/stop decision;
- authority handoff;
- reversal condition;
- amount of work avoided.

A prettier or more expert-sounding question is **not** a success.

### Falsifier
If prospective cases show that the reformulated question rarely changes the decision path relative to answering the original question directly, do not treat Question Discovery as a standalone product capability.

---

## Evidence status

Current status: `SESSION_OBSERVATION → PRODUCT_HYPOTHESIS`

This session is strong enough to justify preserving and testing the capability.

It is not yet enough to claim standalone product-market value.

Next evidential step, if pursued later: freeze a set of raw user questions **before** reformulation, compare direct-answer baseline vs Question-Discovery-first workflow, and score only downstream decision delta / avoided work / authority correction — not elegance of wording.
