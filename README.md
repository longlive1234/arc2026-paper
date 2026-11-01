# Two Guesses, One Score — ARC Prize 2026 Paper Track (paper + artifacts)

**Title:** *Two Guesses, One Score: Coverage-Optimal Selection and Its Empirical Limits in ARC-AGI-2 Solver Pools*
**Subtitle:** *Theory, a pre-registered benchmark on real solver candidate pools, and a measured negative result*
**Status:** **v4 freeze (1 November 2026)** — 4,981-word main text (limit 5,000), 30 references, 9 figures, 8 tables; no priority claim; not peer reviewed. Supersedes v3 (`paper_planC_draft_v3.md`, sha256 `00435c14…`). v4 applies the **Theorem-4 exact-match correction**, adds the real Kaggle code-competition results, and replaces the pending diversification table with an honest exploratory check.

## What the paper contributes

ARC-AGI-2 gives each test input exactly **two attempts**, scored by exact match. The paper formalizes
the two-slot choice as **coverage optimization** and proves five results:

1. independent-case top-2 optimality (coverage objective `U(a1,a2)=1−P(¬C1∧¬C2)`);
2. duplicate attempts are strictly dominated by distinct positive-probability candidates;
3. argmax-once is suboptimal under correlated errors (exact Bernoulli-correlation pair formula);
4. an exact **diversification threshold** `ρ < ρ* = sqrt(p2(1−p1)/(p1(1−p2)))`, with the crucial
   **exact-match correction**: two distinct grids are mutually exclusive (`C1∧C2=∅` ⇒ ρ<0), so the
   positive-ρ regime is unreachable and top-2 by calibrated probability is optimal — the real null is
   estimation/identifiability, not a correlation gate;
5. a **budget-constrained coverage allocation** theorem (Jensen ⇒ uniform under concave coverage;
   greedy/water-filling under heterogeneous concavity; single-crossing ⇒ difficulty-threshold rule;
   saturation ⇒ reallocate compute).

## Measured result: bounded negative + real competition numbers

- **Selection study (real third-party pools):** CompressARC 400 tasks — oracle-any-2 **34.25%**,
  solver top-2 **20.00%**, coverage-optimal **17.75%**; a 16-input ARC-AGI-2 pilot ties every rule at
  the 31.25% oracle ceiling; simulation validates mechanics (+18.33 pp over argmax, 95% CI [11.67, 25.0]).
  Verdict: `DOWNGRADE_TO_ANALYSIS` — selection is not the bottleneck; candidate generation is.
- **Real Kaggle code-competition submissions (hidden half, public LB):**
  **S5 L4 = 16.25% (best; ref 57681632)**, S6 dual-config 15.42%, S5_ens two-model 15.42%,
  S1 L4 14.17%, S5+LegC verified-induction hybrid 14.17% (net-negative −2.08 vs S5),
  CPU probe 0.00%; one invalid-format attempt and one rerun error are documented in the ledger.
- **Final LB context (snapshot 2026-11-01T00:13Z):** 3,572 ranked teams; leader 88.06; our champion
  16.25 → rank **2,414 / 3,572** (67.5th percentile from top); the ~30–31 public-notebook band sits at
  ranks ≈500–1000. Public LB shows our **best** score, not the last submission. No SOTA/medal claim.
- **Reference replication:** the public notebook pipeline (NVARC TTT + optional DSL induction) measured
  **3/20** on our 20-task public-eval subset (below our S1 4/20) and ~17 min/task, so it is not a
  matched reproduction of the ~30 band.

## Files

| file | contents |
|---|---|
| `paper.pdf` | compiled paper v4 (17 pages, 9 figures, 8 tables) |
| `drafts/paper_planC_draft_v4.md` | Markdown source of the paper v4 (4,981 words) |
| `writeup_kaggle_v4.md` | Kaggle paper-track writeup (≤1,500 words) |
| `evidence_table.md` | numeric-evidence audit table (all paper numbers traceable to scripts) |
| `kaggle_package_final.md` | final submission ID, media-gallery order, scoreboard |
| `FINAL_REPORT_CN.md` | Chinese final report (scores, ablations, honest limits) |
| `kaggle_submissions.md` | full submission ledger (valid, invalid, errored, missed) |
| `figures/` | all figures incl. final LB snapshot (Fig. 8) |
| `arxiv_source/` | LaTeX source (`main.tex` + figures) for Overleaf / arXiv |
| `cover.png`, `gallery_order.md` | paper-track media gallery assets |

## Reproduction

- Code + CPU experiments: https://github.com/longlive1234/arc-selection (MIT-0). CPU-only
  `analysis/run_all.sh` reproduces every selection number in ≈3 minutes; `pytest` covers the solver,
  packet builder, rerun gates and safety cells.
- Kaggle notebook: `wen134/arc2026-ttt` (private kernel, L4×4, offline; competition submission ref
  **57681632** is the champion entry). The final Nov 2 entry re-submits the best COMPLETE version.

## Citation

```bibtex
@misc{arc2026twoguesses,
  title  = {Two Guesses, One Score: Coverage-Optimal Selection and Its Empirical Limits in ARC-AGI-2 Solver Pools},
  author = {{ARC Prize 2026 Paper Track team}},
  year   = {2026},
  note   = {Preprint; code: https://github.com/longlive1234/arc-selection},
  url    = {https://github.com/longlive1234/arc2026-paper}
}
```

## Licensing

- Paper text and figures: **CC BY 4.0**.
- Code (separate repository): **MIT-0**.
- Third-party data: see the code repository's `NOTICE.md`; unlicensed public-notebook artifacts are
  cited as prior art and fetched by the user, never redistributed.
