# Design Research Spine v0.1

## Status

**NON-SCORING · QUARANTINED · NO PROMPT CHANGE · NO HOLDOUT LEARNING**

This is a provenance and crosswalk layer for frontend-design knowledge. It is intentionally separated from the frozen GitHub benchmark and from `prompts/SYSTEM.md`.

The purpose is not to give Neta more design rules. The purpose is to decide, for every attractive frontend rule, what kind of thing it actually is:

```text
skill assertion
→ source lineage
→ source class
→ independent evidence families
→ existing Neta research anchor
→ contradiction / boundary
→ allowed use
→ denied inference
→ residual, if any
```

If this layer cannot show why a rule deserves promotion, the rule stays out of Neta.

## Why this was added

Open-source frontend skills are unusually useful because they expose the operational judgment that AI design systems actually encode: how they read a brief, preserve or replace an incumbent design, choose a visual direction, use motion, compress hierarchy, generate variants and critique their own work.

They are also unusually dangerous as evidence because the ecosystem is derivative. The same rule can appear in several repositories while still descending from one source.

The main lineage discovered in this pass is:

```text
Anthropic frontend-design
        ↓
    Impeccable
        ↓
   design-taste

Emil design-engineering ─────┘
Leon taste-skill ────────────┘
```

`design-taste` explicitly declares the three upstreams above. Impeccable explicitly states that it started from Anthropic's `frontend-design`. Therefore repetition inside that cluster is not automatically independent corroboration.

Superdesign is treated as a workflow/reference implementation. `flitzrrr/frontend-design-skills` is treated as a discovery corpus: it is excellent for finding candidate claims and source domains, but its synthesized DO/DON'T rules must be traced back to primary evidence before promotion.

## Source classes

The source registry separates:

1. **Primary practitioner skills** — useful for craft and operational judgment, not field proof.
2. **Derivative practitioner systems** — may add novel workflow knowledge, but inherited rules share lineage with parents.
3. **Secondary syntheses** — useful compression, zero new independence for inherited claims.
4. **Reference workflow implementations** — show how an agent can operationalize a process; do not prove the process is optimal.
5. **Discovery corpora** — indexes of candidate claims; never authority by citation count.
6. **Normative standards** — strong authority inside their declared construct, bounded outside it.
7. **Validated field instruments** — measure defined user constructs; do not diagnose mechanisms or prescribe fixes.

See `source-registry.json`.

## First-pass result: 14 candidate claims

The crosswalk classified 14 attractive frontend claims:

| Class | Count | Meaning |
|---|---:|---|
| `RESEARCH_COMPATIBLE_CANDIDATE` | 2 | genuine residuals worth future research |
| `ALREADY_COVERED` | 2 | Neta already has the useful distinction |
| `WORKFLOW_HEURISTIC` | 3 | good agent process, not field truth |
| `REJECT_AS_UNIVERSAL` | 3 | useful only after narrowing; strong wording is overbroad |
| `IMPLEMENTATION_CONVENTION` | 1 | local design-system choice, not a research construct |
| `MEASUREMENT_BOUNDARY` | 2 | standard/instrument is strong but cannot diagnose the fix |
| `SOURCE_METHOD` | 1 | provenance rule, not frontend behavior |

The important result is that most of the OSS knowledge **should not become new Neta rules**.

## What Neta already had before this pass

Several frontend-skill ideas that look new are already covered more rigorously by Neta's existing research:

### Feedback and responsiveness

`W1-FBK-001` already separates:

- actual completion latency;
- acknowledgement/status feedback;
- progress ambiguity;
- state-transition salience.

Emil and Anthropic add useful craft options, but the underlying distinction is already present and bounded.

### “Too much” and hierarchy

`W1-HIE-001` already keeps information quantity, grouping and visual rank separate. This is stronger than importing a generic “use more whitespace” rule.

### Cognitive economy

`W1-COG-001` already rejects “minimum information” and “minimum friction” as universal goals. The target is extraneous interaction cost relative to task, expertise and information value.

### One primary action

`W1-NAV-001` already narrows one-primary-action to execution states with a dominant task. Choice-overload evidence is heterogeneous; exploration and comparison legitimately expose alternatives.

This directly blocks a common skill shortcut such as “one CTA per viewport” from becoming a universal Neta law.

### Aesthetics versus usability

`W1-AES-001` already separates order/clarity, expressive originality, perceived craft/modernity and task usability. This prevents “AI slop” dislike from being relabeled as a usability defect.

## The two residuals worth pursuing later

### R1 — brief-to-visual-world synthesis

Practitioner systems repeatedly start by reading the product, audience, task, cultural context and constraints before choosing a visual world. ISO 9241-110 independently anchors task/context suitability.

The unresolved research question is narrower:

> How should Neta generate a visual-world candidate that is traceably grounded in product evidence rather than category defaults, without laundering the generated taste into OWNER or FIELD truth?

This is not permission to add a synthesis engine now. It is a candidate distinction to operationalize after the current holdout wave closes.

### R2 — user language versus internal ontology

Anthropic's frontend skill explicitly prefers end-user vocabulary over implementation vocabulary, and ISO 9241-110 supports self-descriptiveness and conformity with user expectations.

Neta already preserves owner language in conversation, but this has not yet been isolated as a frontend research construct.

The important boundary is:

- internal implementation jargon that users should not need;
- versus legitimate expert/domain vocabulary that *is* the user's real language.

A future discriminator should test predictability/comprehension of the action label, not reward simplistic “plain language” replacement.

## Claims rejected as universal

Three tempting rules were explicitly blocked:

1. **Exactly one primary action per viewport.** Conditional, not universal.
2. **Less content/fewer choices/more whitespace is inherently cognitively better.** False as a general rule; value, grouping, expertise and task state matter.
3. **Looking non-generic or non-AI is necessarily better.** Aesthetic/craft signal only unless task or field evidence establishes more.

A fourth family — fixed numeric recipes such as a 12-column grid, 8px spacing baseline or one canonical content width — is classified as an implementation convention, not a Neta construct.

## Standards and validated instruments

Two different source classes are deliberately kept separate from practitioner skills.

### Standards

- WCAG 2.2 is normative accessibility authority. Passing it cannot be converted into a general usability, comprehension or preference claim.
- ISO 9241-110:2020 gives broad interaction principles. It can support a mechanism or boundary, but cannot establish that a specific product violates the principle without local evidence.

### Instruments

- UEQ can measure defined field UX dimensions.
- UMUX-LITE can measure perceived ease of use and usefulness with a very short field instrument.

Their correct role is **measurement**. A score does not tell Neta which frontend mechanism caused the score and does not authorize a specific redesign by itself.

## Integration law

No item in this directory may directly change Neta behavior.

The allowed path remains:

```text
DESIGN-SPINE CLAIM
→ map to existing research claim OR create post-wave candidate
→ source-lineage dedupe
→ independent triangulation
→ falsification / counterevidence
→ context boundary
→ discriminator
→ fixture
→ clean-model failure
→ smallest prompt repair
→ neighboring control
```

The existing `research/PROMOTION_PROTOCOL.md` remains authoritative.

## Holdout quarantine

The GitHub benchmark currently contains unseen HOLDOUT cases. This design-spine work must not be injected into benchmark scoring or used to teach Neta before the wave closes.

Specifically, until the holdout wave closes:

- do not modify `prompts/SYSTEM.md` from this research;
- do not modify the benchmark rubric to reward these claims;
- do not reinterpret existing HOLDOUT cases through this new source layer;
- do not count HOLDOUT outcomes as confirmation of the two residual candidates;
- do not add design-spine knowledge to the baseline reviewer.

This preserves the benchmark's ability to falsify the current Neta version.

## Minimum information before any design-spine claim can advance

A residual needs all of the following before it should become a new research claim or Neta capability:

1. exact claim wording;
2. primary source lineage;
3. at least one genuinely independent evidence family where available;
4. a deliberate counterevidence search;
5. a neighboring case where the rule should *not* fire;
6. explicit context and culture boundaries;
7. one cheap discriminator;
8. exact requested use and denied inference;
9. a fixture that can fail;
10. a clean-model failure showing Neta actually needs the capability.

Without item 10, additional research may improve our bibliography but not Neta.

## Files

- `source-registry.json` — pinned sources, classes, licenses, lineage and authority limits.
- `claim-crosswalk.json` — 14 candidate claims mapped to current Neta research and decision permissions.

## Stop rule for this pass

The first pass has already separated the useful residuals from copied heuristics. Further frontend-skill collection is justified only if it changes one of these decisions:

- whether R1 or R2 survives as a residual;
- whether a rejected universal has a narrower supported form not already in Neta;
- whether a supposedly independent source is actually shared lineage;
- whether a new source provides a discriminator or counterexample that changes promotion state.

Do not collect another skill merely because it is popular.
