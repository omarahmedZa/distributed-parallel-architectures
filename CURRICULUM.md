# Distributed and Parallel Architectures — Curriculum

Graduate/advanced course emphasizing architectural design decisions, advanced mechanisms, trade-offs, scalability, and open research problems. Fundamentals are taught first and explicitly connected to later lectures.

## Audience and prerequisites

- **Audience:** students with basic systems/programming concepts who need a rigorous bridge into advanced distributed and parallel architectures.
- **Entry prerequisites:** basic programming, data structures, and operating-systems/computer-architecture awareness (processes/threads, memory, basic networking helpful).

## Fundamentals module (taught first)

| Topic | Learning objectives | Forward connections |
|---|---|---|
| Introduction to parallel computing | Explain why parallelism is used; apply Flynn’s taxonomy basics; distinguish concurrency vs parallelism. | Frames Lecture 1, 3, 7, 10. |
| Shared-memory vs distributed-memory concepts | Compare models, programming implications, and trade-offs (address spaces, communication, synchronization). | Lectures 2, 4, 5, 6, 8. |
| Basic cache and memory hierarchy | Explain locality and cache levels; give coherence/consistency intuition as a lead-in. | **→ Lecture 2** (coherence, MESI, NUMA, consistency models). |
| Basic MPI and OpenMP programming | Describe core concepts, minimal illustrative examples/pseudocode, and when to use each. | **→ Lecture 5** (advanced message passing and communication). |
| Basic speedup and efficiency calculations | Compute/interpret speedup, efficiency, cost, and overhead intuition; fundamental HPC concepts. | **→ Lecture 9** (scaling laws, modeling, optimization). |

## Modules and lectures

### Module 1 – Advanced Parallel Computer Architectures

| Lecture | Title | Key objectives and focus |
|---|---|---|
| 1 | Advanced Parallel Architecture Design | Evolution of parallel architectures; multicore vs many-core systems; architectural trade-offs; performance and scalability implications. |
| 2 | Advanced Memory Architectures and Memory Hierarchy | Cache coherence, MESI, NUMA, memory consistency models, and shared-memory challenges; design decisions and scalability trade-offs. |
| 3 | Interconnection Networks and Communication Architectures | Topologies (Mesh, Torus, Fat-Tree, Hypercube), switching, routing, and latency/bandwidth trade-offs. |

### Module 2 – Distributed Systems Architecture

| Lecture | Title | Key objectives and focus |
|---|---|---|
| 4 | Distributed Computing Architectures and Models | Distributed architectures; client-server, peer-to-peer, cluster, grid; distributed memory models and trade-offs. |
| 5 | Advanced Message Passing and Communication Mechanisms | Advanced MPI concepts; collective and non-blocking communication; communication optimization and overhead. |
| 6 | Distributed Synchronization and Consistency | Clock synchronization, mutual exclusion, distributed coordination, and consistency models; correctness/performance trade-offs. |

### Module 3 – Advanced Parallel Processing and Optimization

| Lecture | Title | Key objectives and focus |
|---|---|---|
| 7 | Advanced Parallel Algorithms and Decomposition Techniques | Domain/task decomposition; parallel sorting, graph processing, parallel matrix operations; communication/load/scalability analysis. |
| 8 | Load Balancing and Dynamic Resource Scheduling | Static/dynamic load balancing; task scheduling; work stealing; resource allocation and scheduling strategies in distributed environments. |
| 9 | Performance Modeling, Scalability and Optimization | Strong/weak scaling; Amdahl’s and Gustafson’s laws; communication-to-computation ratio; profiling; scalability limitations and optimization. |

### Module 4 – Heterogeneous and Emerging Architectures

| Lecture | Title | Key objectives and focus |
|---|---|---|
| 10 | Heterogeneous Computing Architectures: CPU, GPU and Accelerators | CPU–GPU architectures; heterogeneous memory; GPU clusters; accelerator-based and hybrid parallel designs and trade-offs. |
| 11 | Cloud, Edge and Serverless Distributed Computing | Cloud HPC; distributed resource management; virtualization/containerization; edge computing; dynamic resource scaling. |

### Module 5 – Advanced Research Topics

| Lecture | Title | Key objectives and focus |
|---|---|---|
| 12 | Fault Tolerance, Reliability and Energy-Efficient Computing | Fault tolerance; checkpointing/recovery; resilient architectures; power-aware and energy-efficient computing trade-offs. |
| 13 | Future of Distributed and Parallel Architectures | Exascale computing; AI-driven HPC; quantum and neuromorphic architectures; emerging research challenges. |

## Per-lecture expectations (all lectures)

Every lecture page includes:
- **Learning objectives**, in-depth core content/mechanisms, **architectural design decisions and trade-offs**, **limitations and scalability implications**, and **research problems/open challenges**.
- **Diagrams/tables/comparisons**, worked examples (including speedup/efficiency calculations where relevant), and **recaps/check-for-understanding** prompts.
- A dedicated **Research Activities** section with:
  1. **Literature review:** summarize **two** credible, relevant research papers (for each: full citation, link/DOI if available, core contribution, method/architecture, key results, and limitations).
  2. **Architecture comparison (where applicable):** compare **two** architectures/approaches with advantages, limitations, trade-offs, and suitable use cases (table where helpful). If not directly applicable, explain why and provide the closest meaningful comparison.
  3. **Case study:** analyze a relevant real-world system, supercomputer, or distributed architecture (what it is, architectural design, how it addresses the lecture’s challenges, observed strengths/limitations).

Sources must be credible and verifiable; established facts are distinguished from discussion, and uncertainty is stated when applicable.

## Pedagogy and consistency

- Teach fundamentals first; maintain explicit prerequisite/forward links and consistent terminology/notation across the site.
- Focus on architectural design decisions, advanced mechanisms, and research problems (not only introductory definitions).
- Use clear visuals and step-by-step explanations to maximize understandability.
