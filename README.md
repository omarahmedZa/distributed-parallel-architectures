# Distributed and Parallel Architectures — Course Website

A static, self-contained educational website for a graduate/advanced course titled **“Distributed and Parallel Architectures.”** The site teaches prerequisite fundamentals first, then covers 13 lectures across 5 modules with an emphasis on architectural design decisions, advanced mechanisms, trade-offs, scalability, and open research problems.

Modeled after the structure and visual/UX style of the reference projects:
- `/home/stave/ai-ml-course`
- `/home/stave/computer-vision-course`

## What’s included

- **`index.html`** — course dashboard/map showing fundamentals, modules, all lectures, and navigation/progression.
- **`lessons/000-fundamentals.html`** — prerequisites module (parallelism/Flynn’s basics, concurrency vs parallelism, shared vs distributed memory, cache/memory hierarchy intuition, basic MPI & OpenMP, speedup/efficiency/HPC fundamentals) with explicit forward links to Lectures 2, 5, and 9.
- **`lessons/001-...013-*.html`** — one page per lecture (13 total), each with learning objectives, in-depth core content, architectural design decisions & trade-offs, limitations & scalability implications, research problems, diagrams/tables/comparisons and worked examples (including speedup/efficiency calculations where relevant), recaps/check-for-understanding prompts, and a dedicated **Research Activities** section (2-paper literature review, architecture comparison, real-world case study).
- **`assets/`** — shared, vendored styles/scripts adapted from the reference family (e.g. `lesson.css`, `figures.css`, `course.js`, `graph.js`, `anim.js`) for consistent layout, figures, and interactions; no external CDNs/services.
- **`labs/`**, **`notebooks/`**, **`decks/`**, **`output/`** — supporting/companion artifacts and directories consistent with the reference organization (included where useful).
- **`tour.html`** — short guide to using the course.
- **`CURRICULUM.md`** — modules, lecture objectives, prerequisites/fundamentals mapping, and research-activity expectations.
- **`tools/build_site.py`** — assembles a deployable `site/` directory (mirroring the reference publish workflow).
- **`site/`** — generated publish output (created by the build script).
- **`.nojekyll`** — included for GitHub Pages compatibility.

## Project structure

```text
.
├─ index.html                 # Dashboard / course map
├─ tour.html                  # How to use the course
├─ lessons/                   # Fundamentals + 13 lecture pages
├─ assets/                    # Shared CSS/JS/figure assets (local)
├─ labs/                      # Companion labs/demos (as included)
├─ notebooks/                 # Supporting notebooks (as included)
├─ decks/                     # Supporting decks (as included)
├─ output/                    # Supporting outputs (as included)
├─ tools/
│  └─ build_site.py           # Builds ./site publish directory
├─ site/                      # Generated publish directory
├─ CURRICULUM.md
├─ README.md
└─ .nojekyll
```

## Local preview

No external services are required. Serve the project locally with Python:

```bash
cd /home/stave/distributed-parallel-architectures
python3 -m http.server 8000
```

Then open: <http://localhost:8000/>

To preview the generated publish directory instead:

```bash
python3 tools/build_site.py
python3 -m http.server 8000 --directory site
```

## GitHub Pages deployment

This project is structured for **GitHub Pages deployment from the repository root** on a **public** repository (branch `main`, folder `/ (root)`), with relative internal links/asset paths and `.nojekyll` for compatibility. A reference-style `site/` publish build is also provided.

### Recommended (root deploy, public repo)

1. **Initialize and commit (if needed):**
   ```bash
   cd /home/stave/distributed-parallel-architectures
   git init
   git checkout -B main
   git add -A
   git commit -m "Initial course site"
   ```

2. **Create a public GitHub repository and push:**
   ```bash
   git remote add origin <YOUR_PUBLIC_REPO_URL>
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - In GitHub: **Settings → Pages**
   - **Source:** Deploy from a branch
   - **Branch:** `main` and **Folder:** `/ (root)`
   - Save and wait for the deployment to complete.

4. **Verify:** open the published URL and confirm the dashboard, fundamentals, all 13 lectures, assets/visuals, and internal navigation/links load correctly.

> Note: This environment can prepare the repository contents and commits locally, but it cannot create or change repository visibility on GitHub for you. Ensure the repository is **public** (or on a plan that supports Pages for your chosen visibility) and that Pages is configured as above.

### Alternative (reference-style `site/` publish)

1. **Build the publish directory:**
   ```bash
   cd /home/stave/distributed-parallel-architectures
   python3 tools/build_site.py
   ```
   This regenerates `site/` (including `site/.nojekyll`).

2. **Publish `site/` contents** to a Pages-configured branch/repository root (for example, by pushing the contents of `site/` to a repo/branch served from `/ (root)`), then enable **Settings → Pages → Deploy from a branch → (that branch) / `/ (root)`**.

3. Rebuild and republish after any source changes.

## Notes on content and sources

- Every lecture includes objectives, core mechanisms, architectural design decisions & trade-offs, limitations/scalability, research problems, visuals/worked examples, checks, and **Research Activities** (2-paper review, comparison, case study).
- Research citations and case studies are selected to be credible and verifiable; established facts are distinguished from discussion. If a specific detail cannot be verified, uncertainty is stated and well-known examples are preferred.

## License / usage

Educational course materials. Verify third-party paper/system details against the cited original sources for authoritative use.
