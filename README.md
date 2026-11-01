# Compute Cannot Buy Identifiability — ARC Prize 2026 Paper Track (paper + artifacts)

**Title:** *Compute Cannot Buy Identifiability: Information-Limited Two-Attempt Selection in ARC-AGI-2 Solver Pools*
**Subtitle:** *An information bound, a conditional compute-separation theorem, and measured evidence from real solver pools and six scored submissions*
**Status:** **v5 working draft (1 November 2026)** — 6,658-word main text (recorded internal v5 cap 6,700), 41 references, 11 figures, 10 tables; v4 (`paper_planC_draft_v4.md`, sha256 `784cffc7…`) remains frozen; no priority claim; not peer reviewed. v5 adds **Theorem 6** (proven label-free identifiability bound), **Prop. 6e/6f and Cor. 6g** (non-vacuity, score-conditional certificate, negative result about full-metadata bounds), conditional **Theorem 7** (compute cannot substitute), lemmas 6a/6b/6d, T5 downgraded to a setting observation, D1/D2 real-data analysis, and refs 29–41.

## What the paper contributes

ARC-AGI-2 gives each test input exactly **two attempts**, scored by exact match. Distinct candidate grids
are mutually exclusive, so the two-slot decision is a **label-free identification** problem:

1. **Theorem 6 (proven):** for any metadata rule, `E[U] ≤ p1+p2+min{T, sqrt(I(C;Z)/2)}` (nats), capped by
   oracle coverage; attained at I=0, vacuous when `I≥2T²`. The pilot certificate transfers to hidden tasks
   only under an explicit exchangeability assumption.
2. **Prop. 6e / Cor. 6g:** unconditional Pinsker-type bounds are **vacuous in score-dominated pools** and
   cannot certify label-free selection; the negative result is about the method.
3. **Prop. 6f (sharpest):** splitting `Z=(S,Z')` gives `E[U] ≤ U_S + min{g−U_S, sqrt(I(C;Z'|S)/2)}`, which is
   **tight (equals U_S) under score sufficiency**; only residual metadata can help.
4. **Theorem 7 (conditional A1–A3):** `lim_{C→∞} score = Σ_t(g_t∞−Δ_t∞)` is allocation-independent; the
   identification gap is budget-invariant; verifier-free compute cannot buy identifiability.
5. Supporting lemmas: swap regret `p2−p3` (6a), fixed-pool monotonicity and pass@k-inversion-as-generation-drift
   (6b), descriptive `g(L)·s(L)` identity (6d); T5 is recorded as a **setting observation** (SPLIT overlap).

### Measured limits (honest)

- D1 certificates are **vacuous on every pool** (I=.059–.183 vs 2T²=.008–.041): T6 is proven, not validated
  here; on dev20 S2/S5/S5_ens the measured gain equals the tail T exactly (ratio 1.00), while CompressARC
  loses −2.25 pp; +8.11 pp S5_ens headroom is selectable but **not realized** (hidden 15.42 < S5 16.25).
- D2 candidate-prefix replay is **definitional**, not T7 evidence; T7's support is only the hidden-score
  ladder (S5 16.25 > S6 = S5_ens 15.42 > S5+LegC 14.17), consistent **not conclusive** (n=6, truncation,
  S6 selection bug, 53-task superset, packet/config differences, unknown hidden size).
- Six scored submissions; champion S5 16.25%; dev20 S1 20.0%; reference replication 3/20; ~30 notebook
  band external only; no SOTA/medal claim.

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
