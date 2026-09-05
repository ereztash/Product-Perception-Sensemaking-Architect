# REALITY · AUTHORITY · PERMISSION

This document is the detailed R0–R6 / authority / permission grammar originally operationalized for Neta v0.2.

Architectural note: `docs/SHARED_EPISTEMIC_KERNEL.md` now adopts these semantics cross-agent. This file remains the detailed canonical definition of the current ladder and permission laws, while `schemas/finding.schema.json` is Neta's adapter and `schemas/rnd-research-task.schema.json` is the R&D adapter. Historical origin inside Neta does **not** make Neta the owner of cross-agent epistemic law.

## 1. Reality ladder

The ladder describes the reality actually touched by the evidence, not how persuasive the prose feels.

| Level | Name | Example in design work |
|---|---|---|
| `R0` | asserted | “the button feels dead” |
| `R1` | static | code, DOM, screenshot, design file or literature exists |
| `R2` | isolated fixture | controlled variant/prototype reproduces or separates the mechanism |
| `R3` | integrated | mechanism is exercised in the real application path |
| `R4` | deployed | the deployed environment exhibits the measured state |
| `R5` | real input | owner/product uses the path with real task/data/input |
| `R6` | third party acted | an external person actually perceived/understood/chose/acted |

A higher number is not “better evidence” in every sense. It is evidence closer to a broader reality claim.

## 2. Claim reality floors

A claim must name the minimum reality required to support the exact wording.

Examples:

| Claim | Typical minimum floor |
|---|---:|
| element/style exists | `R1` |
| an isolated manipulation changes salience | `R2` |
| application state transitions correctly | `R3` |
| production behaves as specified | `R4` |
| the owner experiences the issue during real use | `R5` |
| a stranger notices the intended hierarchy | `R6` |
| users prefer one structurally valid variant | `R6` |
| users derive differentiated value | `R6` with a field design appropriate to that value claim |

If observed reality is below the required floor, the state is `INSUFFICIENT_REALITY`, not “low confidence”.

## 3. Resolution authorities

### `OWNER`
Can resolve:
- taste and preference for the owner's product;
- product intent;
- strategic tradeoffs;
- accepted risk/waiver;
- whether a reversible design change is worth trying.

Cannot establish:
- what strangers notice, understand, prefer, value or do.

### `REPO`
Can resolve:
- code path;
- component state;
- geometry/layout facts;
- timing measured in the implementation;
- what instrumentation is actually recorded;
- whether a local gate rejects an invalid state.

Cannot establish:
- production environment state unless that state is reproduced there;
- human interpretation or value.

### `ENVIRONMENT`
Can resolve:
- deployed configuration;
- production/runtime behavior;
- network/runtime policy;
- whether the deployed artifact corresponds to the intended build.

Cannot establish:
- field perception/value merely because the system is live.

### `RESEARCH`
Can resolve:
- what a literature/standard/evidence body supports within its actual construct and population;
- whether a proposed design mechanism has external support or known boundaries;
- research-method, measurement and evidence-synthesis questions within the actual evidence available.

Cannot establish:
- that the mechanism is active in this product without local evidence;
- that this product's users will value the intervention.

### `FIELD`
Can resolve:
- what external people notice;
- understand;
- prefer;
- value;
- choose;
- do under the field protocol actually run.

Cannot by itself resolve:
- the owner's strategic intention;
- unobserved causal explanations;
- code/environment facts not measured.

## 4. Requested uses

Every material claim states what we want to do with it:

- `HYPOTHESIZE`
- `DISCRIMINATE`
- `PROTOTYPE`
- `BUILD_REVERSIBLE`
- `CHANGE_PRODUCTION`
- `ASSERT_FIELD_OUTCOME`
- `DEFER`

Then the relevant peer adapter records a separate permission:

- `ALLOW`
- `DENY`
- `DEFER`

Permission answers **whether the current evidence/authority/reality justify that use**. It does not answer whether the claim is “true in general”.

## 5. Core permission laws

1. `ALLOW` requires the claim to be `SUPPORTED` and the observed reality to meet its required floor.
2. `OUTCOME` claims about external people require `FIELD` authority and ordinarily `R6`.
3. `ASSERT_FIELD_OUTCOME` may not be `ALLOW` below `R6`.
4. A Neta `BUILD_READY` finding requires at least one supported `INTERVENTION` claim explicitly allowed for `BUILD_REVERSIBLE` or `CHANGE_PRODUCTION`.
5. A Neta `DISCRIMINATE_FIRST` finding cannot smuggle an allowed build intervention into an unresolved diagnosis.
6. A Neta `FIELD_STOP` requires a material unresolved `FIELD` claim and a concrete `field_requirement`.
7. A waiver can accept risk; it cannot change a claim from unsupported to supported or raise its reality level.
8. Evidence from one authority may inform another authority's question but may not close it automatically.
9. An agent's role does not upgrade the resolution authority of the claim it is handling.

## 6. Mixed findings are expected

A useful finding can legitimately say all of the following at once:

- the repo fact is established;
- the mechanism is externally supported;
- a reversible intervention is owner-authorized;
- the user-outcome prediction is still denied pending FIELD.

This is not inconsistency. It is the point of the ledger.

## 7. Authority ceiling

For each unresolved material claim ask:

> What authority could change the decision now?

If all remaining claims point to a different authority, the current authority has reached its ceiling.

Do not pay technical work to close field debt.  
Do not pay literature work to close product-specific behavior debt.  
Do not pay UI polish to close an unresolved measurement-validity question.  
Do not keep an R&D task open when the remaining decision is OWNER/Neta/FIELD-owned.

## 8. Encodability bias check

Before any new feature/probe/system asks for build permission, answer:

1. Which live claim does it discriminate or resolve?
2. Which authority owns that claim?
3. Which peer/domain should work the question?
4. What information does the feature buy?
5. What behavior/measurement might the feature contaminate?
6. Is there a cheaper admissible observation or existing capability?
7. What would make us remove the feature?

If the best argument is “we can build it” or “it would be useful to have”, permission is `DEFER`.
