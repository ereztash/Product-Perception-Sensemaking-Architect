# Architecture Front Door — Natural Screen Pass 1

Status: `TARGETED_FALSIFICATION · HISTORICAL_NATURAL + ARCHITECTURE_CONTROLS · NO_NEW_AGENT`
Date: 2026-09-06

## Question

Does the previously observed gap

```text
ACCEPTED NEED
→ ARCHITECTURE-SIGNIFICANT REQUIREMENTS / QUALITY ATTRIBUTES
→ MATERIAL PRESSURE
→ STRUCTURAL OPTIONS
```

require a new reasoning capability/agent, or is it sufficiently handled by existing upstream qualification plus a stricter Architecture input contract?

## Comparator logic

Three possibilities:

1. `NEW_CAPABILITY`
   Need→requirement translation contains a recurring hidden judgment that existing Neta/R&D/front-door reasoning misses and that materially changes architecture decisions.

2. `ARCHITECTURE_ADAPTATION`
   The translation is necessary, but can be represented as a mandatory input-normalization/front-door step inside Architecture.

3. `EXISTING_UPSTREAM_COVERAGE`
   Generic upstream qualification already exposes the required properties/invariants; Architecture only needs to refuse premature structural commitment until those inputs are present.

## Natural positive-looking cases

### AF-NAT-01 — Deploy CRM to Vercel

Historical prompt family: Question Discovery NP-01.

Direct baseline:
- inspect stack;
- attempt/plan Vercel subject to compatibility;
- adapt or choose another host if incompatible.

Upstream challenger:
- identify runtime/state/operability requirements first: persistent process/filesystem, DB, background work, long-running requests, jobs, configuration, stable URL, operational visibility;
- choose deployment target from the feasible set rather than taking Vercel as fixed.

Historical adjudication: `PARTIAL_DELTA` because strong baseline already performs a compatibility check.

Architecture-front-door interpretation:
The useful transformation is real, but it is not uniquely architecture-specific reasoning. A strong general/upstream method already asks what properties the deployment must preserve before selecting a host.

Disposition: `REQUIREMENT_TRANSLATION_USEFUL · UNIQUE_CAPABILITY_NOT_SHOWN`.

### AF-NAT-02 — Google Sheet as lead-state source of truth

Historical prompt family: Question Discovery NP-02.

Direct baseline:
- build a Sheet tracker and make it the shared lead-state store.

Upstream challenger:
- first specify state authority requirements: concurrent writes, transactional consistency, audit history, deduplication, identity resolution, permissions, automated transitions and human editability;
- Sheet may survive as authority or become only a projection.

Historical adjudication: `MATERIAL_WIN` because the architecture/source-of-truth choice can change before automations are built.

Architecture-front-door interpretation:
This is strong evidence that structural choices must be preceded by required properties/invariants. But the material correction was already produced by the generic Question Discovery/upstream calibration behavior.

Disposition: `FRONT_DOOR_REQUIREMENT_CONFIRMED · SEPARATE_CAPABILITY_NOT_EARNED`.

## Architecture controls

The existing Architecture historical corpus includes decisions whose architecture-significant pressure is already explicit, for example:

- provider/model-specific execution concerns must remain outside a provider-neutral routing law;
- docs discoverability must improve while preserving numerous path references/tests;
- deployment verification must distinguish exact match, legitimate supersession and stale/broken states;
- chess position persistence must avoid duplicate truth and measurement-contaminating transient state.

In these cases an additional generic need-elicitation phase would add little: the required properties, constraints or invariants are already present in the case statement. The work is structural discrimination inside Architecture.

These are neighboring non-fire controls for any future front-door adaptation.

## Distinction learned

The natural cases support this rule:

```text
NAMED STRUCTURE / PLATFORM / STORE
+
REQUIRED PROPERTIES NOT YET EXPLICIT
→ QUALIFY REQUIREMENTS BEFORE ARCHITECTURE
```

But they do **not** support:

```text
→ CREATE REQUIREMENTS AGENT
```

Nor do they currently show that a separate Requirements capability beats:

```text
R&D / front-door qualification
→ explicit required properties + authorities
→ Architecture Decision Discriminator
```

## Minimal architecture adaptation candidate

Do not add a peer. Add, if/when Architecture capability itself is tested, a fail-closed input gate:

```text
ARCHITECTURE_INPUT_GATE

Required before structural recommendation:
- accepted need / telos;
- relevant stakeholders / authority;
- required property or quality attribute;
- context/workload where it must hold;
- mandatory constraints/invariants;
- acceptance observation or measurable criterion where material;
- current REPO/ENV facts required for the decision.
```

If one or more material items are absent:

```text
DO NOT GUESS STRUCTURE
→ request OWNER / REPO / ENV / FIELD input
or
→ R&D if there is a nontrivial choice of evidence program
```

This is a contract/gate adaptation, not a new agent.

## Pass-1 result

`NEED_TO_REQUIREMENT_TRANSLATION = REAL NECESSARY TRANSFORMATION`

`UNIQUE_NEW_REASONING_CAPABILITY = NOT SHOWN`

`REQUIREMENTS_AGENT = NOT_EARNED`

`BEST_CURRENT_FORM = ARCHITECTURE INPUT CONTRACT / GATE`

## Implication for Architecture candidate

The main unresolved Architecture question remains downstream:

> Does the Architecture Decision Discriminator itself materially outperform the strongest existing baseline (R&D + Scaffold + REPO/ENVIRONMENT) on structural decisions?

That clean A/B is still the required promotion evidence. Front-door work should not delay it or be mistaken for evidence that an Architecture peer is already earned.
