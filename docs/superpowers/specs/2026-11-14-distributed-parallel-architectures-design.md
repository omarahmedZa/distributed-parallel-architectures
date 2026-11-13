# Distributed and Parallel Architectures — Course Website Design Spec

**Date:** 2026-11-14  
**Status:** Approved in chat (user delegated self-review and authorized build to proceed)  
**Project root:** `/home/stave/distributed-parallel-architectures/`  
**References:** `/home/stave/ai-ml-course`, `/home/stave/computer-vision-course`

## 1. Summary

Build a complete, teachable, static educational website for the graduate/advanced course **“Distributed and Parallel Architectures.”** The site mirrors the structure and visual/UX feel of the reference course projects (plain HTML/CSS/JS, course dashboard, lesson pages, shared assets, curriculum-driven organization) while covering required fundamentals, 13 lectures, and per-lecture research activities. Content emphasizes architectural design decisions, advanced mechanisms, trade-offs, scalability, and open research problems.

## 2. Goals and non-goals

### Goals
- Deliver a self-contained, GitHub Pages–ready course site with all required pages, navigation, curriculum, and documentation.
- Teach prerequisites/fundamentals first and connect them explicitly to later lectures.
- Provide in-depth, understandable content per lecture: objectives, mechanisms, design decisions/trade-offs, limitations/scalability, research problems, diagrams/tables/comparisons, worked examples (including speedup/efficiency where relevant), and recaps/check-for-understanding.
- Include required per-lecture Research Activities (2 verifiable papers, architecture comparison, real-world case study).
- Reuse/adapt reference-family components, scripts, and interaction patterns where lessons/labs benefit (assets, figures, animations, labs, supporting tooling/artifacts), keeping everything vendored locally (no external CDNs/services).

### Non-goals
- No external backend/services or unnecessary third-party runtime dependencies.
- No fabrication of paper details or case-study facts; uncertain/unverifiable specifics must be stated as such and replaced with verifiable examples where needed.

## 3. Audience and pedagogy

- **Audience:** students with basic systems/programming concepts needing a rigorous bridge into advanced distributed and parallel architectures.
- **Per lecture/fundamentals page:** state learning objectives; explain core ideas and mechanisms; highlight architectural design decisions and trade-offs; discuss limitations/scalability implications; surface relevant research problems.
- **Clarity aids:** abundant explanatory paragraphs and step-by-step walkthroughs, diagrams/figures/tables/comparisons, worked examples (including basic speedup/efficiency calculations where relevant), and recaps/check-for-understanding prompts.
- **Consistency:** uniform terminology and notation across the site; fundamentals explicitly linked forward to dependent lectures.

## 4. Approach and deployment

**Chosen approach:** Approach 1 (faithful mirror of reference structure/feel) with a **root-deployable public-repo** GitHub Pages configuration as requested.

- Source organized like the references with shared `assets/`, `lessons/`, `labs/` (as needed), curriculum/docs, and `tools/` including `build_site.py` to assemble a `site/` publish directory (mirroring `ai-ml-course`).
- The repository root will also be directly deployable to GitHub Pages (index, assets, lessons, etc. at root with relative paths) so Pages can serve from **`main` / `/ (root)`** of a public repository.
- `tools/build_site.py` emits `site/.nojekyll` and site metadata; `.nojekyll` included at root as needed. All internal links/assets are relative for correctness in local preview and on the Pages root.

## 5. Site structure and file layout

**Root:** `/home/stave/distributed-parallel-architectures/`

- `index.html` — dashboard/map (modules, lectures, fundamentals, progress/navigation).
- `tour.html` — short usage tour (reference-style), if included.
- `lessons/` — one HTML page per lecture (13) plus fundamentals/prerequisite page(s), clearly ordered and reachable from dashboard.
- `labs/` — companion interactive demos/labs where helpful (self-contained SVG/canvas/HTML/JS), linked from relevant lessons/dashboard.
- `assets/` — vendored shared assets adapted from references as needed: `lesson.css`, `figures.css`, `course.js`, `graph.js`, `anim.js`, and demo/helper scripts/styles required by components, figures, animations, or labs.
- `notebooks/`, `decks/`, `output/` — supporting artifacts where lessons/labs/materials benefit (reference-family organization).
- `tools/` — support/build scripts including `build_site.py`.
- `site/` — generated publish output (reproducible build).
- `CURRICULUM.md` — modules, objectives, prerequisites/fundamentals mapping, research-activity expectations.
- `README.md` — course overview, structure, local preview, and exact GitHub Pages deployment steps.
- `docs/superpowers/specs/` — design spec; `docs/superpowers/plans/` — implementation plan.

## 6. Dashboard, navigation, and progression

- **Dashboard (`index.html`):** topline/chrome and hero (title, subtitle, entry/continue affordance, progress indicator consistent with reference patterns), and course map grouped as **Fundamentals (first)** then **Modules 1–5** listing all lectures with titles/objectives/links and progression cues. All fundamentals and 13 lectures reachable.
- **Fundamentals-first:** prerequisites module explicitly labeled and taught before advanced lectures.
- **Navigation:** lesson masthead/topline with course-map link and position, sequential pager (prev/next), and cross-links; fundamentals connected forward to Lectures 2, 5, 9 (and others as relevant) and lectures link back to prerequisites.
- **Discoverability:** labs/companions and key resources linked from dashboard and/or relevant lessons. Responsive, semantic, keyboard-navigable structure.

## 7. Scope and content model

### 7.1 Fundamentals module (prerequisites)
- Introduction to parallel computing (why parallelism, Flynn’s taxonomy basics, concurrency vs parallelism).
- Shared-memory vs distributed-memory concepts (models, programming implications, trade-offs).
- Basic cache and memory hierarchy (locality, cache levels, coherence/consistency intuition as lead-in) — connected to **Lecture 2**.
- Basic MPI and OpenMP programming (core concepts, minimal illustrative examples/pseudocode, when to use each) — connected to **Lecture 5**.
- Basic speedup and efficiency calculations and fundamental HPC concepts (speedup, efficiency, cost, overhead intuition) — connected to **Lecture 9**.

### 7.2 Modules and lectures (each its own page)
- **Module 1 – Advanced Parallel Computer Architectures**: L1 Advanced Parallel Architecture Design; L2 Advanced Memory Architectures and Memory Hierarchy; L3 Interconnection Networks and Communication Architectures.
- **Module 2 – Distributed Systems Architecture**: L4 Distributed Computing Architectures and Models; L5 Advanced Message Passing and Communication Mechanisms; L6 Distributed Synchronization and Consistency.
- **Module 3 – Advanced Parallel Processing and Optimization**: L7 Advanced Parallel Algorithms and Decomposition Techniques; L8 Load Balancing and Dynamic Resource Scheduling; L9 Performance Modeling, Scalability and Optimization.
- **Module 4 – Heterogeneous and Emerging Architectures**: L10 Heterogeneous Computing Architectures: CPU, GPU and Accelerators; L11 Cloud, Edge and Serverless Distributed Computing.
- **Module 5 – Advanced Research Topics**: L12 Fault Tolerance, Reliability and Energy-Efficient Computing; L13 Future of Distributed and Parallel Architectures.

### 7.3 Per-lecture/fundamentals template
- Masthead/topline, position, title, and learning objectives.
- Lede/why it matters and prerequisite/forward links.
- Core ideas and mechanisms (in-depth, sectioned).
- Architectural design decisions and trade-offs.
- Limitations and scalability implications.
- Research problems / open challenges.
- Rich visuals: multiple diagrams/figures/tables/comparisons and animations/interactive visuals where they aid understanding (self-contained SVG/canvas/JS via adapted reference assets).
- Worked examples with step-by-step arithmetic where relevant (including speedup/efficiency; Amdahl/Gustafson, strong/weak scaling, communication-to-computation in L9).
- Recap and check-for-understanding prompts.
- Pager and related links/sources.

### 7.4 Research Activities (required on every lecture page)
Dedicated **Research Activities** section containing:
1. **Literature review (two papers):** for each, full citation, link/DOI if available, core contribution, method/architecture, key results, and limitations. Credible, relevant, verifiable sources; distinguish fact from discussion; state uncertainty if any.
2. **Architecture comparison (where applicable):** structured comparison of two relevant architectures/approaches (advantages, limitations, trade-offs, suitable use cases), table where helpful. If not directly applicable, explain why and provide the closest meaningful comparison.
3. **Case study:** relevant real-world system/supercomputer/distributed architecture (what it is, architectural design, how it addresses lecture challenges, observed strengths/limitations), verifiable.

## 8. Assets, visuals, accessibility

- Adapt and extend `lesson.css`, `figures.css`, `course.js`, `graph.js`, `anim.js`, and helpers from references; add consistent styles for Research Activities, comparisons, and rich figure/animation layouts. All local/vendored.
- Favor abundant, self-contained diagrams/figures and animations/interactions that improve comprehension; static explanations remain complete.
- **Accessibility:** semantic headings/landmarks, descriptive links, labeled tables/figures, alt text and SVG accessible names/descriptions, readable contrast, visible focus, keyboard-operable controls, responsive layout.

## 9. Documentation and deployment

- **`CURRICULUM.md`:** overview, fundamentals with objectives and forward mapping, Modules 1–5/Lectures 1–13 with objectives and focus, and research-activity expectations.
- **`README.md`:** course description, structure, local preview commands, and exact step-by-step GitHub Pages deployment (public repo, deploy from `main` / root; relative paths; `.nojekyll`; build/publish via `tools/build_site.py` and/or direct root deploy), plus notes on verifying dashboard/lessons/labs/assets/links.
- Local preview via `python3 -m http.server` (root and/or built `site/`).

## 10. Acceptance criteria

- Fundamentals section and all 13 lectures present, complete, and reachable from dashboard with working navigation.
- Every lecture includes objectives, core content, trade-offs/design decisions, research problems, and the three research-activity components (2 papers, comparison, case study).
- Site renders correctly served locally and is structured/configured for GitHub Pages root deployment (relative paths, `.nojekyll`, documented steps).
- Structure and visual/interaction style clearly mirror the reference course family. Content is rigorous, visualization-rich, and fact-based.