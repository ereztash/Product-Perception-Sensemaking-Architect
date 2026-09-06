# System Design Decision Research — Source Register Pass 1

Status: `BOUNDED_SOURCE_MAP`
Date: 2026-09-06
Task: `CAL-ARCH-SYSDESIGN-001`

## Rule

Sources are ranked by expected decision value for the surviving challenger:

> Does `MATERIAL_PRESSURE` need a measurable refinement (`required property + relevant workload/resource conditions + observed limit evidence`) for performance/reliability/scale decisions?

A source is not high priority merely because it teaches a widely used technology.

## Tier A — consume now / high decision value

### A1 — ByteByteGo: 8 Most Important System Design Concepts You Should Know
URL: https://www.youtube.com/watch?v=BTjxUS_PylA
Role: initiating pressure→mechanism primer.

Why it matters:
- exposes recurring pressure families quickly;
- explicitly warns that sharding is complex and difficult to reverse;
- useful as a source of positive/negative mechanism hypotheses.

Ceiling:
- often compresses `pressure → solution` too aggressively for an architecture decision contract.

### A2 — ByteByteGo: System Design Was HARD — Until You Knew the Trade-Offs
URL: https://www.youtube.com/watch?v=1nENigGr-a0
Role: tradeoff grammar.

Why it matters:
- shifts from pattern inventory to application-specific needs;
- covers SQL/NoSQL, normalization/denormalization, CAP/consistency spectrum, batch/stream processing;
- repeatedly frames choices as context-dependent rather than universally better/worse.

R&D expectation:
- higher transfer value than another “top N concepts” video because it strengthens the decision relation between required property and accepted cost.

### A3 — ByteByteGo: System Design Was HARD — Until You Knew the Trade-Offs, Part 2
URL: https://www.youtube.com/watch?v=2g1G8Jr88xU
Role: continuation of tradeoff grammar.

R&D expectation:
- inspect for additional tradeoff dimensions/counterexamples; retain only distinctions that alter the candidate pressure refinement or historical fixtures.

### A4 — ByteByteGo: Scalability Simply Explained in 10 Minutes
URL: https://www.youtube.com/watch?v=EWS_CIxttVw
Role: candidate vocabulary for workload, bottleneck, horizontal/vertical scaling, statelessness, loose coupling, async, caching, sharding and monitoring.

Why it matters:
- directly touches the surviving `WORKLOAD / BOTTLENECK` challenger.

Ceiling:
- strategy list alone does not establish when each mechanism should fire.

### A5 — Google SRE: Service Level Objectives
URL: https://sre.google/sre-book/service-level-objectives/
Role: primary decision framework for user-relevant measurable service properties.

Why it matters:
- strongest current evidence for making required behavior measurable where reliability/performance is material;
- explicitly works backward from what users care about rather than easy-to-measure internal metrics;
- connects targets to tradeoffs, costs and error budgets.

### A6 — Azure Architecture Center: Design principles
URL: https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/
Role: primary architecture framework.

Why it matters:
- links business requirements, self-healing, redundancy, scale-out, partitioning, operations, evolution, RTO/SLO and failure-mode analysis.

### A7 — AWS Well-Architected Framework
URL: https://docs.aws.amazon.com/wellarchitected/latest/userguide/waf.html
Role: primary multi-quality tradeoff framework.

Why it matters:
- prevents performance/scale from becoming the only architecture objective;
- architecture tradeoffs vary with business criticality and risk tolerance.

### A8 — Martin Kleppmann: Designing Data-Intensive Applications
URL: https://martin.kleppmann.com/2017/03/27/designing-data-intensive-applications.html
Role: authoritative principles/tradeoffs bridge.

Why it matters:
- reliability, scalability, maintainability, consistency, fault tolerance and complexity are treated as interacting system properties;
- useful for deeper mechanism adjudication after a real case fires.

## Tier B — open when a matching case fires

### B1 — ByteByteGo: 8 Most Important Tips for Designing Fault-Tolerant System
URL: https://www.youtube.com/watch?v=3Lis4w4_bBc
Open when:
- a historical/live case is about failure tolerance, failover, graceful degradation, redundancy or recovery objective.

Required discriminator before use:
- desired availability/recovery property and failure mode must be named; “need reliability” is insufficient.

### B2 — ByteByteGo: What is a LOAD BALANCER really about?
URL: https://www.youtube.com/watch?v=LQuuoHTyYz8
Open when:
- traffic distribution, horizontal scaling or failover routing is a live mechanism candidate.

Do not open merely because a service has multiple instances.

### B3 — ByteByteGo: What Is Redis Really About? Why Is It So Popular?
URL: https://www.youtube.com/watch?v=z_NbVtbgBJw
Open when:
- a read/latency/recomputation bottleneck survives measurement and caching is a plausible mechanism.

Required counterfactual:
- what happens without Redis / with in-process or existing cache;
- hit ratio, invalidation/staleness and operational burden.

### B4 — ByteByteGo: Apache Kafka Fundamentals You Should Know
URL: https://www.youtube.com/watch?v=-RDyEFvnTXI
Open when:
- temporal decoupling, backpressure, resumability, event retention or multi-consumer processing is a live architecture problem.

Do not treat “high writes” as sufficient reason to introduce Kafka.

### B5 — ByteByteGo: Consistent Hashing | Algorithms You Should Know #1
URL: https://www.youtube.com/watch?v=UF9Iqmg94tk
Open when:
- partition ownership changes dynamically and rebalancing movement is material.

Do not open as generic distributed-systems vocabulary.

## Tier C — defer / anti-curriculum

### C1 — broad “Top 20/30 System Design Concepts” lists
Role: discovery only.
Reason to defer:
- high pattern coverage but low incremental decision discrimination after A1;
- likely to increase vocabulary faster than decision quality.

### C2 — microservices/Kubernetes/tooling roadmaps
Reason to defer:
- architecture mechanism/tooling before a named workload/failure/ownership pressure would invert the research order.

### C3 — vendor-specific implementation deep dives without a live mechanism decision
Reason to defer:
- risk of learning implementation details for a mechanism the system does not need.

## Topic map after recovery

### Core now
1. Measurable quality requirements / SLOs.
2. Workload characterization and bottleneck evidence.
3. Tradeoff reasoning across consistency, latency, throughput, reliability, cost and complexity.
4. Failure-mode analysis and recovery objectives.
5. Evolution, migration and reversibility.

### Mechanisms on demand
1. Caching.
2. Async queues / event streaming.
3. Replication / failover / load balancing.
4. CDN / edge.
5. Storage models.
6. Observability mechanisms.
7. Indexing/query optimization.
8. Partitioning/sharding.

## Stop condition for the video lane

Stop watching additional system-design videos when two consecutive sources add no new:
- measurable decision variable;
- counterindication;
- failure mode;
- tradeoff dimension;
- migration/reversal condition;
- historical fixture distinction.

At that point, move to REPO/ENVIRONMENT evidence rather than a larger curriculum.
