# Two Guesses, One Score — ARC Prize 2026 Paper Track (paper + artifacts)

**Title:** *Two Guesses, One Score: Coverage-Optimal Selection and Its Empirical Limits in ARC-AGI-2 Solver Pools*
**Subtitle:** *Theory, a pre-registered benchmark on real solver candidate pools, and a measured negative result*
**Status:** working paper / preprint draft v3 (20 October 2026; 4,997-word main text; 30 references). No priority claim. Not peer reviewed. v3 applies the official-competition-eval patch (120 tasks / 172 inputs) and the updated novelty positioning ([26]–[30]); v2 is archived in the project workspace (`paper_planC_draft_v2.md`, sha256 `6ae661c5…d86ccb6`).

ARC-AGI-2 gives each test input exactly **two attempts**, scored by exact match. This paper asks a
decision question that is separate from solving: *given a pool of candidate answers, which two should
be submitted?* We formalize this as **coverage optimization**, prove three results (independent-case
top-2 optimality, strict dominance of duplicate attempts, suboptimality of argmax-once under
correlated errors), give a calibrated plug-in estimator, and add a **score-sufficiency criterion** for
when reranking cannot realize a pool's oracle headroom.

We then run a **pre-registered benchmark on real third-party candidate pools**:

| dataset | unit | N | oracle-any-2 | solver top-2 | coverage rule |
|---|---|---|---|---|---|
| CompressARC (ARC-AGI-1, headline) | task | 400 | **34.25%** | **20.00%** | 17.75% |
| ARC-AGI-2 public eval TTT pilot (third-party dump) | test input | 16 | 31.25% | 31.25% | 31.25% |
| simulated pools (mechanism only) | task | 120 | 41.67% | 23.33% (argmax) | **41.67%** |

**Measured result: a bounded negative.** On the 400-task CompressARC pools, 14.25 points of oracle
headroom exist but the solver's own score ordering already captures the recoverable two-attempt mass;
every calibrated/coverage rule we tested is at or below it. In simulation the rule mechanics are
positive (+18.34 pp over argmax) when candidates carry score-orthogonal evidence. Conclusion:
**two attempts are not two chances in current open ARC solvers — the bottleneck is candidate
generation/coverage, not selection.** Falsification conditions F1–F3 are stated in the paper.

The paper also reports: a characterization and SHA-256 leakage audit of the public ARC-AGI-2 data; a
landscape analysis of nine public 2026 solver notebooks (displayed leaderboard 29.7–31.4 vs 1.7–4.8%
measured on their saved artifacts); an open-source offline TTT system (CPU-validated; GPU end-to-end
not measured); and a factual platform-gated access report (no hidden-test access, zero Kaggle GPU-hours).

## Files

| file | contents |
|---|---|
| `paper.pdf` | compiled paper (14 pages, 8 figures, 6 tables) |
| `paper_planC_draft_v2.md` | Markdown source of the paper (4,986 words main text) |
| `arxiv_source/` | LaTeX source (`main.tex` + figures) for Overleaf / arXiv; see `README_OVERLEAF.md` |
| `cover.png` | cover image |
| `figures/` | Figures 1–6 (build assets) |
| `evidence_table.md` | claim → artifact → status mapping for every quantitative claim |
| `SELECTION_RESULTS.md`, `selection_benchmark.json` | frozen benchmark results (Table 2 source) |
| `PUBLISH_GUIDE.md` | how to publish (GitHub / Zenodo DOI / arXiv) |

## Code and reproducible benchmark

The selection-rule engine and the CPU-reproducible benchmark live in a separate MIT-0 repository:
**https://github.com/longlive1234/arc-selection** (release `v0.1.0`).

```bash
git clone https://github.com/longlive1234/arc-selection
cd arc-selection && pip install -r requirements.txt
make repro-cpu        # reproduces the reduced CPU benchmark (~3 s, numpy only)
```

The release ships reduced derived pools so it reproduces without network access; the full third-party
candidate dumps are fetched by `scripts/fetch_third_party.sh` (unlicensed public-notebook data is
never redistributed). The paper's Table 2 was produced by the full analysis pipeline in the private
working tree and is frozen in `selection_benchmark.json` (sha256 `6c16abfe…b71a`).

## Citation

```bibtex
@misc{arc2026twoguesses,
  title  = {Two Guesses, One Score: Coverage-Optimal Selection and Its Empirical Limits in ARC-AGI-2 Solver Pools},
  author = {{ARC Prize 2026 Paper Track team}},
  year   = {2026},
  note   = {Preprint draft; code: https://github.com/longlive1234/arc-selection},
  url    = {https://github.com/longlive1234/arc2026-paper}
}
```

## Licensing

- Paper text and figures: **CC BY 4.0**.
- Code (separate repository): **MIT-0**.
- Third-party data: see the code repository's `NOTICE.md`; unlicensed public-notebook artifacts are
  cited as prior art and fetched by the user, never redistributed.
