# Distributed and Parallel Architectures Course Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **Execution:** user explicitly authorized proceeding without further review/choice; implement natively in this session after plan self-review.

**Goal:** Build and publish-ready a complete, static, teachable course website for “Distributed and Parallel Architectures” in `/home/stave/distributed-parallel-architectures/`, mirroring the reference course family and satisfying all spec requirements.

**Architecture:** Plain HTML/CSS/JS site (no external CDNs/services) with shared vendored assets adapted from `/home/stave/ai-ml-course` and `/home/stave/computer-vision-course`, a course dashboard, fundamentals content taught first, 13 lecture pages, companion labs/visuals/animations where they aid understanding, `CURRICULUM.md`, `README.md`, and `tools/build_site.py` generating `site/`. All internal links/assets are relative for local preview and GitHub Pages root deployment.

**Tech Stack:** HTML5, CSS, vanilla JS (adapted `course.js`/`graph.js`/`anim.js`/helpers), inline SVG/canvas for diagrams/animations, Python 3 for `build_site.py`, Markdown docs.

**Spec:** `docs/superpowers/specs/2026-11-14-distributed-parallel-architectures-design.md`

## Global Constraints

- Static, self-contained site; no external CDNs/services. Reuse/adapt reference assets/scripts/components where lessons/labs need them (all vendored locally).
- Audience: grad/advanced students with basic systems/programming background; rigorous bridge to advanced distributed/parallel architectures.
- Every lecture/fundamentals page: learning objectives, core ideas/mechanisms, architectural design decisions and trade-offs, limitations/scalability implications, research problems/open challenges, clear diagrams/tables/comparisons and worked examples (including speedup/efficiency calculations where relevant), recaps/check-for-understanding prompts, and consistent terminology/notation.
- Fundamentals taught first and explicitly connected forward: memory hierarchy → Lecture 2, MPI/OpenMP → Lecture 5, speedup/efficiency → Lecture 9 (and other relevant links).
- Every lecture page includes a dedicated **Research Activities** section with: (1) literature review of **two** credible, verifiable papers (full citation, link/DOI if available, core contribution, method/architecture, key results, limitations), (2) architecture comparison where applicable (two architectures/approaches with advantages, limitations, trade-offs, suitable use cases; table where helpful; if not applicable explain why and give closest meaningful comparison), (3) case study of a relevant real-world system/supercomputer/distributed architecture (what it is, architectural design, how it addresses challenges, strengths/limitations). Distinguish fact from discussion; do not fabricate; state uncertainty if needed.
- Deliverables: `index.html` dashboard, fundamentals + 13 lecture pages in consistent structure, shared `assets/`, `CURRICULUM.md`, `README.md` (with local preview and exact GitHub Pages deployment steps), `.nojekyll` as needed/root-deployable relative paths, and `tools/build_site.py`/`site/` mirroring reference.
- Accessible and responsive: semantic headings/landmarks, readable contrast, alt text/accessible names for figures/tables/SVG, keyboard-operable controls.

## Review Focus

- Missing required per-lecture elements (objectives, trade-offs, limitations/scalability, research problems, or any of the 3 Research Activities components) or missing fundamentals/lectures/navigation reachability.
- Fabricated, unverifiable, or incomplete paper/case-study details; citations lacking core required fields or presented as certain when uncertain.
- Broken internal links/asset paths (especially relative paths from `lessons/` vs root) or Pages deployment not working from root/`site/`.
- Diagrams/animations/interactive components inaccessible or non-functional without external resources (missing alt/labels, keyboard issues, or CDN dependency).
- Inconsistent terminology/notation or missing explicit fundamentals→lecture connections (L2/L5/L9).

---

## Task 1: Base assets, styles, and build tooling

**Files:**
- Modify: `assets/lesson.css`, `assets/figures.css`, `assets/course.js` (adapt as needed)
- Use/Create: `assets/graph.js`, `assets/anim.js`, additional helpers if needed
- Modify: `tools/build_site.py`
- Create: `.nojekyll`

**Interfaces:**
- Produces: shared styling/components (incl. Research Activities, comparison tables, recap/check prompts, rich figures/animations) and a working `python3 tools/build_site.py` that assembles deployable `site/` with relative paths and `.nojekyll`.

- [ ] **Step 1:** Adapt/extend CSS for course components (research blocks, comparison tables, callouts, responsive figures/tables) while preserving reference-family look and accessibility (contrast, focus).
- [ ] **Step 2:** Adapt JS/assets for navigation/progress/interactive figures/animations as needed; ensure no external dependencies.
- [ ] **Step 3:** Update `tools/build_site.py` to copy this project’s site dirs/files (index, tour, lessons, labs, assets, notebooks, decks, output, CURRICULUM/README/etc.) into `site/`, emit `.nojekyll`/metadata, preserve `site/.git`.
- [ ] **Step 4:** Verify build runs (`python3 tools/build_site.py`) and produces expected structure.
- [ ] **Step 5:** Commit base assets/tooling.

## Task 2: Fundamentals module page(s) (taught first)

**Files:**
- Create: `lessons/000-fundamentals.html` (or clearly separated fundamentals pages linked as a module)

**Interfaces:**
- Produces: complete, visualization-rich fundamentals covering all required topics with objectives, mechanisms, trade-offs/implications, worked examples (incl. speedup/efficiency), recaps/check prompts, and explicit forward links to Lectures 2, 5, 9 (and others relevant).

- [ ] **Step 1:** Implement fundamentals content: intro to parallel computing (why, Flynn’s basics, concurrency vs parallelism); shared vs distributed memory; cache & memory hierarchy (locality, levels, coherence/consistency intuition) → L2; basic MPI & OpenMP (concepts, minimal illustrative examples/pseudocode, when to use) → L5; basic speedup & efficiency and HPC concepts → L9.
- [ ] **Step 2:** Add diagrams/figures/animations/tables and worked speedup-efficiency calculations; include recaps/check-for-understanding and consistent nav.
- [ ] **Step 3:** Verify required sections and forward links present; commit.

## Task 3: Lecture 1 — Advanced Parallel Architecture Design

**Files:**
- Create: `lessons/001-advanced-parallel-architecture-design.html`

**Interfaces:** Full lecture page per template incl. Research Activities (2 papers, comparison, case study), visuals/animations, worked examples as relevant.

- [ ] **Step 1:** Write objectives, core content (evolution, multicore/many-core, trade-offs, performance/scalability), design decisions & trade-offs, limitations/scalability, research problems, recap/check prompts, rich diagrams/tables.
- [ ] **Step 2:** Add Research Activities: two verifiable papers (e.g. multicore/many-core/parallel architecture landmarks) with full required fields; architecture comparison (e.g. multicore vs many-core/GPU-like many-core or relevant approaches) with table; real-world case study (e.g. contemporary multicore/many-core processor or parallel system).
- [ ] **Step 3:** Verify required elements/links/citations; commit.

## Task 4: Lecture 2 — Advanced Memory Architectures and Memory Hierarchy

**Files:**
- Create: `lessons/002-advanced-memory-architectures-and-hierarchy.html`

- [ ] **Step 1:** Content: cache coherence; MESI; NUMA; memory consistency models; shared-memory challenges; trade-offs/limitations/scalability; research problems; visuals/animations (coherence states/transitions, NUMA topology, consistency intuitions) and examples; link back to fundamentals memory hierarchy.
- [ ] **Step 2:** Research Activities: two verifiable papers (coherence/consistency/NUMA), comparison (e.g. snooping vs directory coherence, or MESI-family/consistency models as applicable) with closest meaningful comparison justified, case study (e.g. NUMA multiprocessor system).
- [ ] **Step 3:** Verify and commit.

## Task 5: Lecture 3 — Interconnection Networks and Communication Architectures

**Files:**
- Create: `lessons/003-interconnection-networks-and-communication.html`

- [ ] **Step 1:** Content: topologies (Mesh, Torus, Fat-Tree, Hypercube), switching, routing, latency/bandwidth trade-offs; design decisions, limitations/scalability, research problems; rich topology/routing/animation visuals and comparisons.
- [ ] **Step 2:** Research Activities: two verifiable papers (interconnects/topologies/routing), comparison table of relevant topologies/approaches, case study (e.g. supercomputer/HPC interconnect).
- [ ] **Step 3:** Verify and commit.

## Task 6: Lecture 4 — Distributed Computing Architectures and Models

**Files:**
- Create: `lessons/004-distributed-computing-architectures-and-models.html`

- [ ] **Step 1:** Content: distributed system architectures; client-server; P2P; cluster; grid; distributed memory models; trade-offs/limitations/scalability; research problems; diagrams/tables.
- [ ] **Step 2:** Research Activities: two verifiable papers, comparison (e.g. client-server vs P2P, or cluster vs grid) with table, case study (e.g. large-scale distributed system/cluster/grid platform).
- [ ] **Step 3:** Verify and commit.

## Task 7: Lecture 5 — Advanced Message Passing and Communication Mechanisms

**Files:**
- Create: `lessons/005-advanced-message-passing-and-communication.html`

- [ ] **Step 1:** Content: advanced MPI concepts; collective communication; non-blocking communication; communication optimization; communication overhead; trade-offs/limitations/scalability; research problems; visuals/animations of collectives/non-blocking overlap; link back to fundamentals MPI/OpenMP.
- [ ] **Step 2:** Research Activities: two verifiable papers (MPI/collectives/communication optimization), comparison (e.g. blocking vs non-blocking, or collective algorithms/approaches), case study (e.g. MPI-based HPC application/system).
- [ ] **Step 3:** Verify and commit.

## Task 8: Lecture 6 — Distributed Synchronization and Consistency

**Files:**
- Create: `lessons/006-distributed-synchronization-and-consistency.html`

- [ ] **Step 1:** Content: distributed synchronization; clock synchronization; mutual exclusion; distributed coordination; consistency models; trade-offs/limitations/scalability; research problems; timelines/diagrams/animations.
- [ ] **Step 2:** Research Activities: two verifiable papers (e.g. Lamport clocks, mutual exclusion/consensus/consistency landmarks), comparison (e.g. consistency models or coordination approaches), case study (e.g. distributed datastore/coordination system).
- [ ] **Step 3:** Verify and commit.

## Task 9: Lecture 7 — Advanced Parallel Algorithms and Decomposition Techniques

**Files:**
- Create: `lessons/007-advanced-parallel-algorithms-and-decomposition.html`

- [ ] **Step 1:** Content: domain/task decomposition; parallel sorting; graph processing; parallel matrix operations; trade-offs/limitations/scalability; research problems; worked examples and visuals.
- [ ] **Step 2:** Research Activities: two verifiable papers, comparison (e.g. domain vs task decomposition, or parallel algorithm/graph frameworks), case study (e.g. parallel graph/matrix/sorting system at scale).
- [ ] **Step 3:** Verify and commit.

## Task 10: Lecture 8 — Load Balancing and Dynamic Resource Scheduling

**Files:**
- Create: `lessons/008-load-balancing-and-dynamic-resource-scheduling.html`

- [ ] **Step 1:** Content: static/dynamic load balancing; task scheduling; work stealing; resource allocation; scheduling strategies in distributed environments; trade-offs/limitations/scalability; research problems; animations/diagrams.
- [ ] **Step 2:** Research Activities: two verifiable papers (e.g. work stealing/scheduling), comparison (static vs dynamic / strategies) with table, case study (e.g. runtime/scheduler in HPC or distributed system).
- [ ] **Step 3:** Verify and commit.

## Task 11: Lecture 9 — Performance Modeling, Scalability and Optimization

**Files:**
- Create: `lessons/009-performance-modeling-scalability-and-optimization.html`

- [ ] **Step 1:** Content: strong/weak scaling; Amdahl’s and Gustafson’s laws; communication-to-computation ratio; performance profiling; scalability limitations; trade-offs/design decisions; research problems; extensive worked speedup/efficiency/scaling calculations and plots/diagrams; link back to fundamentals speedup/efficiency.
- [ ] **Step 2:** Research Activities: two verifiable papers (Amdahl/Gustafson/scalability/performance modeling landmarks), comparison (strong vs weak scaling or modeling approaches), case study (e.g. scalability study of a real supercomputer/application).
- [ ] **Step 3:** Verify and commit.

## Task 12: Lecture 10 — Heterogeneous Computing Architectures: CPU, GPU and Accelerators

**Files:**
- Create: `lessons/010-heterogeneous-computing-cpu-gpu-accelerators.html`

- [ ] **Step 1:** Content: CPU-GPU architectures; heterogeneous memory; GPU clusters; accelerator-based computing; hybrid parallel architectures; trade-offs/limitations/scalability; research problems; dataflow/architecture diagrams and examples.
- [ ] **Step 2:** Research Activities: two verifiable papers (GPU/accelerator/heterogeneous computing), comparison (CPU vs GPU/accelerators or programming/execution models) with table, case study (e.g. GPU-accelerated supercomputer or heterogeneous system).
- [ ] **Step 3:** Verify and commit.

## Task 13: Lecture 11 — Cloud, Edge and Serverless Distributed Computing

**Files:**
- Create: `lessons/011-cloud-edge-and-serverless-distributed-computing.html`

- [ ] **Step 1:** Content: cloud HPC architecture; distributed resource management; virtualization; containerization; edge computing; dynamic resource scaling; trade-offs/limitations/scalability; research problems; architecture diagrams.
- [ ] **Step 2:** Research Activities: two verifiable papers (cloud/edge/serverless/HPC), comparison (cloud vs edge, or VMs vs containers/serverless as applicable) with table, case study (e.g. cloud HPC/edge/serverless platform).
- [ ] **Step 3:** Verify and commit.

## Task 14: Lecture 12 — Fault Tolerance, Reliability and Energy-Efficient Computing

**Files:**
- Create: `lessons/012-fault-tolerance-reliability-and-energy-efficient-computing.html`

- [ ] **Step 1:** Content: fault tolerance; checkpointing; recovery mechanisms; resilient architectures; power-aware computing; energy efficiency; trade-offs/limitations/scalability; research problems; diagrams/animations.
- [ ] **Step 2:** Research Activities: two verifiable papers (checkpoint/restart, resilience, energy efficiency), comparison (e.g. checkpointing strategies or resilience/energy trade-offs), case study (e.g. resilient/energy-aware supercomputer or large system).
- [ ] **Step 3:** Verify and commit.

## Task 15: Lecture 13 — Future of Distributed and Parallel Architectures

**Files:**
- Create: `lessons/013-future-of-distributed-and-parallel-architectures.html`

- [ ] **Step 1:** Content: exascale computing; AI-driven HPC; quantum computing architectures; neuromorphic computing; emerging research challenges; trade-offs/limitations; research problems; forward-looking diagrams/tables.
- [ ] **Step 2:** Research Activities: two verifiable papers (exascale/AI-for-HPC/quantum/neuromorphic landmarks or surveys), comparison (e.g. emerging paradigms/architectures) with closest meaningful comparison justified, case study (e.g. exascale system or notable emerging-architecture platform/project).
- [ ] **Step 3:** Verify and commit.

## Task 16: Labs, tour, and companion visuals (as needed)

**Files:**
- Create/Modify: `labs/*.html`, `tour.html`, supporting assets/notebooks/decks/output artifacts as lessons benefit

- [ ] **Step 1:** Add/adapt tour and companion labs/demos for topics where interaction/animation aids understanding (e.g. topology/routing, coherence, collectives, scheduling, scaling), self-contained and linked.
- [ ] **Step 2:** Add any helpful notebooks/decks/output placeholders or artifacts consistent with reference organization when beneficial.
- [ ] **Step 3:** Verify links and self-containment; commit.

## Task 17: Dashboard (`index.html`) and site integration

**Files:**
- Create/Modify: `index.html`

- [ ] **Step 1:** Build dashboard with hero/topline, fundamentals-first module, Modules 1–5 and all 13 lectures with objectives/links/progression, and navigation to resources/labs/tour as included.
- [ ] **Step 2:** Ensure every fundamentals and lecture page is reachable; pagers and cross-links (incl. fundamentals→L2/L5/L9) consistent.
- [ ] **Step 3:** Verify responsive/accessible structure; commit.

## Task 18: `CURRICULUM.md` and `README.md`

**Files:**
- Create/Modify: `CURRICULUM.md`, `README.md`

- [ ] **Step 1:** Write `CURRICULUM.md` with overview, fundamentals objectives/mapping, Modules 1–5/Lectures 1–13 objectives/focus/progression, and research-activity expectations.
- [ ] **Step 2:** Write `README.md` with course description, structure, local preview commands, and exact GitHub Pages deployment steps (public repo, root deploy `main`/`/`, relative paths, `.nojekyll`, build `site/` usage), verification notes.
- [ ] **Step 3:** Commit.

## Task 19: Build, verify, and finalize

**Files:**
- Modify as needed for fixes; regenerate `site/`

- [ ] **Step 1:** Run `python3 tools/build_site.py` and confirm `site/` contains deployable content with `.nojekyll`.
- [ ] **Step 2:** Verify locally (structure sanity): all required files exist, index links resolve to fundamentals and 13 lectures, each lecture contains required sections including `Research Activities` with 2 papers/comparison/case study, relative asset paths correct.
- [ ] **Step 3:** Spot-check accessibility/semantics (headings, labels/alt where applicable) and fix issues.
- [ ] **Step 4:** Final commit(s) with clear messages; ensure working tree clean.

## Self-Review (performed)

1. **Spec coverage:** fundamentals, modules/lectures 1–13, per-lecture required sections and 3-part Research Activities, dashboard/CURRICULUM/README/assets/tools/site, GitHub Pages/root-relative paths covered by tasks 1–19.  
2. **Step scan:** content-heavy tasks specify required deliverables/sections/sources expectations (exact prose/figures determined during implementation but constrained by spec); verification/build steps have concrete commands/outcomes.  
3. **Type/interface consistency:** file paths and deliverables consistent across tasks; `build_site.py` produces `site/` consumed by deployment docs.  
4. **Review Focus:** added to owning tasks via required-elements checks (Tasks 2–15,17,19), citation/verifiability constraints (Tasks 3–15,19), path/deploy checks (Tasks 1,17,19), accessibility/self-containment (Tasks 1,16,17,19).  
5. **Proportion:** plan documents decisions/deliverables without transcribing full page bodies. Gaps addressed inline (labs/tour/resources, fundamentals mapping). 
