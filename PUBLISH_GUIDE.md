# PUBLISH_GUIDE — how to publish the paper, repo and artifacts

Paper: **"Two Guesses, One Score: Coverage-Optimal Selection and Its Empirical Limits in ARC-AGI-2
Solver Pools"** (ARC Prize 2026 Paper Track). This guide covers the three publication routes we
support. Nothing here is executed automatically; the Lead/owner runs these steps.

| artifact | path | status |
| :--- | :--- | :--- |
| Paper PDF (verified build) | `paper/paper.pdf` | built by `paper/build/build_paper.py` (Typst, deterministic) |
| LaTeX source (for arXiv/Overleaf) | `paper/arxiv_source/` (`main.tex` + `figures/`) | generated, **not compiled locally** (no TeX on this machine) |
| Code + data release repo | `release/arc-selection/` (tag `v0.1.0`) | 4 commits, 51 files, MIT-0, secret-scan clean |
| Repo git bundle | `release/arc-selection-v0.1.0.bundle` | `git clone`-able handoff artifact |
| Repo tarball | `release/arc-selection-v0.1.0.tar.gz` | `git archive` of tag `v0.1.0` |
| Cover image / figures | `paper/cover.png`, `paper/figures/` | final figures |
| Release notes / verification | `release/RELEASE_NOTES.md`, `release/VERIFY.md` | license + reproducibility evidence |

Recommended order: **(1) GitHub repo → (2) Zenodo DOI → (3) arXiv (if endorsement available)**, then
update `CITATION.cff`/release notes with the DOI and attach links in the Kaggle writeup.

---

## 1. GitHub — publish the code/data release

Assumes the owner is logged into GitHub and has a repository `arc-selection` (or creates it empty).

```bash
# 1) push the release repo from the local git repository (already committed + tagged)
cd release/arc-selection
git remote add origin git@github.com:<OWNER>/arc-selection.git      # or https://github.com/<OWNER>/...
git push -u origin main --tags

# 2) optional: verify the bundle reproduces the same tree elsewhere
cd /tmp && git clone /home/chen/.dsh/ungrouped/arc2026/release/arc-selection-v0.1.0.bundle verify
cd verify && git tag          # expect v0.1.0
python benchmarks/selection_benchmark.py   # dataset A runs offline; dataset B needs fetch

# 3) create a GitHub release with the paper PDF + reproducible archives attached
#    (requires the `gh` CLI: https://cli.github.com/)
cd /home/chen/.dsh/ungrouped/arc2026
gh release create v0.1.0-paper \
    paper/paper.pdf \
    release/arc-selection-v0.1.0.tar.gz \
    release/arc-selection-v0.1.0.bundle \
    --repo <OWNER>/arc-selection \
    --title "ARC Prize 2026 paper + reproducible release v0.1.0" \
    --notes-file release/RELEASE_NOTES.md
```

Repo settings to set once: description ("Two-attempt selection benchmarks for ARC-AGI-2 candidate
pools; MIT-0; reproducible CPU benchmark"), topics (`arc-agi`, `arc-prize-2026`, `program-synthesis`,
`selection`, `benchmark`), and enable the pre-commit secret scan for future commits
(`cd release/arc-selection && make install-hook`).

---

## 2. Zenodo — DOI route (recommended if arXiv endorsement is unavailable)

Zenodo gives a citable DOI without endorsement and is accepted by the ARC Prize paper track.

1. Create/log in to <https://zenodo.org>.
2. **New upload** → files:
   - `paper/paper.pdf` (the verified PDF; **primary artifact**),
   - `release/arc-selection-v0.1.0.tar.gz` (code + data release, MIT-0),
   - optional: `release/arc-selection-v0.1.0.bundle` and a zip of `paper/arxiv_source/`.
3. Metadata:
   - **Title:** Two Guesses, One Score: Coverage-Optimal Selection and Its Empirical Limits in
     ARC-AGI-2 Solver Pools
   - **Creators:** ARC Prize 2026 Paper Track team (add owner/team members as agreed)
   - **Publication type:** Publication → Preprint; add a second upload (or note) for the software
     release with type Software.
   - **Description:** paste the abstract (below).
   - **Keywords:** ARC-AGI-2, program synthesis, candidate selection, test-time training, benchmark,
     ARC Prize 2026.
   - **License:** paper text CC BY 4.0 (or arXiv non-exclusive license if publishing only on arXiv);
     code/data release MIT-0 (third-party data terms per `NOTICE.md`).
   - **Version:** 0.1.0; **Language:** English.
4. Publish → copy the **DOI** (e.g. `10.5281/zenodo.XXXXXXX`).
5. Update `release/arc-selection/CITATION.cff` (`doi:` field), `README.md`, and the Kaggle writeup
   with the DOI; commit as `docs: add Zenodo DOI` and push.

> Note on the unlicensed third-party candidate dump: it is **not** included in the Zenodo/GitHub
> artifacts (only fetched locally by users). Do not upload it to Zenodo.

---

## 3. arXiv — LaTeX route (needs endorsement for first-time submitters)

arXiv requires an **endorsement** for new submitters in cs.AI / cs.LG (ask a colleague with arXiv
submission history; if unavailable, use the Zenodo route — arXiv is not required by the ARC Prize
paper track). Do not upload a PDF only: arXiv expects LaTeX source for this content.

1. Regenerate the LaTeX source from the final Markdown (after any last content edits):
   ```bash
   python paper/arxiv_source/md2tex.py paper/paper_planC_draft_v2.md --out-dir paper/arxiv_source
   ```
2. **Compile once on Overleaf** (pdfLaTeX) and fix any residual errors — see
   `paper/arxiv_source/README_OVERLEAF.md` for the known-risk spots (wide tables, literal formulas,
   unused bibliography entries). This machine has no TeX, so `main.tex` is *not* locally compiled.
3. Package for arXiv: zip `main.tex` + `figures/` (arXiv accepts a .zip of the source tree; no PDFs
   inside except the figures).
4. Submit at <https://arxiv.org/submit>: category **cs.AI** primary, cross-list **cs.LG**.
5. **Title / authors:** as in the draft; add all agreed authors.
6. **Abstract:** paste (plain text/LaTeX-safe version below).
7. **Comments field (suggested):**
   `ARC Prize 2026 Paper Track. Main text: 4,986 words; 14 pages, 8 figures, 6 tables. Code and CPU-reproducible benchmark: https://github.com/<OWNER>/arc-selection (DOI: 10.5281/zenodo.XXXXXXX). No end-to-end solver score or leaderboard claim.`
8. **License:** arXiv non-exclusive license (or CC BY 4.0 if consistent with the team decision).
9. After announcement: add the arXiv ID to `CITATION.cff`, README, Kaggle writeup and GitHub release
   notes.

---

## Abstract (for Zenodo description / arXiv abstract field)

> ARC-AGI-2 gives each test input exactly two attempts, scored by exact match, so choosing the two
> answers is a first-class decision problem. We formalize it as coverage optimization — maximize
> U(a1,a2)=1−P(¬C(a1)∧¬C(a2)) — and prove three results: under independent correctness the optimal
> pair is the two largest calibrated probabilities; submitting the same grid twice is strictly
> dominated; and argmax-once is provably suboptimal when candidates share error modes. The theory is
> sound and the simulated benchmark is strongly positive (coverage 41.67% vs 16.67% duplicate and
> 23.33% argmax; +18.34 pp over argmax, 95% CI [11.7, 25.0]), but on real public pools the solver's
> own score ordering already saturates recoverable two-attempt coverage. On 400 CompressARC tasks the
> solver's top-2 covers 20.00% and our coverage-optimal rule 17.75% — below the top-2, below
> argmax+argmax (19.50%), level with duplicate (18.50%) — against 34.25% oracle coverage: 14.25 points
> of headroom that is not re-ranking-reachable (candidate AUC 0.981, score-dominated). On a small
> ARC-AGI-2 pilot (16 holdout inputs) every rule matches the 31.25% oracle ceiling while the deployed
> fallback loses one input. Two attempts are not two chances unless the pool carries genuinely
> independent evidence; the bottleneck is candidate generation/coverage, not selection. We also
> report a CPU-validated TTT system, a data characterization and leakage audit, and a
> platform-gated account. No end-to-end solver score or leaderboard claim is made.

*(This is the abstract as of the frozen draft; if the draft changes, re-copy from
`paper/paper_planC_draft_v2.md`.)*

---

## Pre-publication checklist

- [ ] Final PDF built from the frozen Markdown: `python paper/build/build_paper.py` (check
      `paper/build/build_report.json`: pages, sha256, 0 warnings).
- [ ] `paper/arxiv_source/main.tex` regenerated from the same frozen Markdown; overleaf compile
      checked by a human.
- [ ] Release repo tagged `v0.1.0`; `release/VERIFY.md` current; `make secrets` PASS.
- [ ] No competition data, no unlicensed third-party dump, no credentials in any artifact
      (`release/VERIFY.md` §1, `NOTICE.md`).
- [ ] Author list / order agreed; acknowledgement of third-party data and the public solver
      notebooks included in the paper's references and `ATTRIBUTION`.
- [ ] Kaggle writeup updated with links: submission notebook, GitHub repo, DOI/arXiv, PDF.
