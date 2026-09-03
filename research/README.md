# Neta Research Quarantine

This directory is the only path by which external research may change Neta's behavior.

The rule is deliberately asymmetric:

> Sources may create candidate distinctions immediately. They may not change `prompts/SYSTEM.md` immediately.

Neta v0.1 was distilled mainly from one owner's portfolio. The research layer exists to prevent portfolio repetition from being mistaken for universality.

## Core loop

```text
candidate capability
→ source triangulation
→ falsification search
→ culture/context scope
→ contradiction handling
→ recursive split or narrowing
→ operationalization
→ fixture
→ promotion decision
```

A contradiction is not just a confidence penalty. It asks whether the original concept was too broad and should be split into neighboring mechanisms.

## Four orthogonal evidence coordinates

Every candidate may be described by a vector. **Never average these dimensions.**

- **G — Generalization (1–7):** the Lessons ladder, from preference to external replication.
- **C — Cultural breadth (0–4):** how many materially different cultural/contextual conditions have actually been represented.
- **A — Adversarial survival (0–4):** how seriously contrary explanations and counterevidence have been searched and survived.
- **O — Operationalization (0–5):** from prose concept to discriminating fixture/gate/field observation.

`G6 · C0 · A3 · O4` is not "better" or "worse" than `G3 · C3 · A2 · O2`; they answer different questions.

## Promotion states

1. `QUARANTINE` — sourced idea, no behavioral authority.
2. `TRIANGULATED` — supported by independent evidence surfaces.
3. `ADVERSARIAL` — counterevidence and neighboring explanations explicitly searched.
4. `BOUNDED` — culture/context boundaries stated; over-broad claim narrowed or split.
5. `FIXTURE_READY` — can be expressed as a discriminator or case.
6. `CANDIDATE_CAPABILITY` — earns use in evaluation, not yet the canonical prompt.
7. `PROMPT_ELIGIBLE` — may be proposed for `prompts/SYSTEM.md`; still requires a prompt-change fixture failure under `CLAUDE.md`.
8. `DEFER_FIELD` — internal research cannot close the question.
9. `REJECTED` — the candidate failed or became unnecessary after splitting.

Promotion is monotonic only in evidence, not in status. A later contradiction may demote or split a capability.

## Research surfaces

Research should draw from independent surfaces rather than many citations from one intellectual lineage:

- controlled or observational HCI / cognitive / behavioral research;
- design and interaction research;
- accessibility and human-factors standards where relevant;
- cross-cultural / localization / socio-cultural research;
- adjacent disciplines that measure the same mechanism under a different name;
- real product incidents or field reports when provenance is strong;
- falsification and null-result sources.

Three papers citing the same dataset count as one evidence family.

## Culture rule

Country is not a mechanism.

Never encode rules such as "Japanese users prefer X" or "Israelis need Y" merely from nationality. Prefer measured or explicit axes such as:

- writing direction and script;
- visual-density conventions;
- language and register;
- direct vs contextual communication conventions;
- expertise / digital fluency;
- domain culture;
- accessibility or cognitive constraints;
- local institutional conventions.

Countries and regions are sampling contexts, not causal explanations unless the research design supports that claim.

## Registers

- `registers/claims.json` — canonical candidate-claim objects.
- `registers/sources.tsv` — one row per source, including provenance and independence family.
- `registers/contradictions.tsv` — evidence that weakens, narrows, or splits a candidate.
- `registers/culture-scope.tsv` — what contexts were represented and which were not.
- `PROMOTION_PROTOCOL.md` — exact promotion gates.
- `WAVE1_PREREGISTRATION.md` — frozen first research wave.
- `AMENDMENTS.md` — any post-freeze change must be recorded before it is used.

## Anti-build / anti-research stop

Stop recursive research when either condition is met:

1. two consecutive recursion passes produce **no new design distinction, reversal condition, or boundary condition**; or
2. the unresolved question's authority is `FIELD` / community evidence.

More reading after that point is not rigor. It is research debt in disguise.
