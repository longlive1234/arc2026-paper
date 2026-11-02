# Compute Cannot Buy Identifiability — ARC Prize 2026 Paper Track (paper + artifacts)

**Title:** *Compute Cannot Buy Identifiability: Information-Limited Two-Attempt Selection in ARC-AGI-2 Solver Pools*
**Subtitle:** *An information bound, a conditional compute-separation theorem, and measured evidence from real solver pools and six scored submissions*
**Status:** **v6.1 (2 November 2026, final competition day)** — 8,198-word main text (internal cap 8,200), 42 references, 12 figures, 13 tables; v4/v5/v6 are archived frozen copies. v6.1 updates the final result to **seven scored Kaggle submissions, champion S5b 16.67% (ref 57854697)**, final public-LB snapshot 2026-11-02 (3,591 teams, our rank 2,429), the Fig. 8 panel, and the honest T7 interpretation (S5b is a generation-side change, not allocation). No priority claim; not peer reviewed. v6 adds **Theorem 8 (verifier-induced identifiability)**, an AWM-inspired verify-first experiment on the public eval split, and **large-scale GPU numerical verification** of Theorems 6–7; Theorem 6 remains proven but empirically vacuous, T7 conditional, T8 realized only in its impossibility-certificate regime with our bounded hypothesis class.

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
6. **Theorem 8 (verifier-induced identifiability, AWM-inspired):** demonstrations are the only labels; a
   verifier that leaves a unique behaviour class closes the gap (Δ=0, coverage `g_V(d)`), otherwise the
   residual gap is `g_V(1−Σ_{j≤2}q_j)`, and `A_d=∅` yields an *impossibility certificate* enabling
   depth-allocation/water-filling; verifier-assisted ceiling `Σg_t` requires `g_V=g` and `q1+q2=1`.
   Hybrid submission correction: exact coverage `p1+p2` (no product form); verifier-first beats TTT-first
   iff `E[1{unique}(φ−p_w2)]>0`; with zero verifier coverage it reduces to TTT top-1+runner-up.

### Measured limits (honest)

- D1 certificates are **vacuous on every pool** (I=.059–.183 vs 2T²=.008–.041): T6 is proven, not validated
  here; on dev20 S2/S5/S5_ens the measured gain equals the tail T exactly (ratio 1.00), while CompressARC
  loses −2.25 pp; +8.11 pp S5_ens headroom is selectable but **not realized** (hidden 15.42 < S5 16.25).
- D2 candidate-prefix replay is **definitional**, not T7 evidence; T7's support is only the hidden-score
  ladder (S5 16.25 > S6 = S5_ens 15.42 > S5+LegC 14.17), consistent **not conclusive** (n=6, truncation,
  S6 selection bug, 53-task superset, packet/config differences, unknown hidden size).
- **Verifier experiment (v6):** bounded-DSL verify-first search (depth ≤2, 56 cores) certifies **0/120**
  public-eval tasks (120/120 depth-2 impossibility certificates; 334.7 CPU-min); a 12-task training control
  yields **1/12** unique solves; learned-rule families 0/120; LLM proposals (DeepSeek-chat k=4) 0/20 and a
  reasoner-token-cap infrastructure null. So T8's restoration mechanism exists but its coverage `g_V` is
  ≈0 with an affordable hypothesis class — the bottleneck is generation, not verification.
- **GPU-scale numerical validation (v6):** T6 at **10^8 instances** → 0 violations at 1e-6 tolerance
  (max float excess 1.12e-7; 34.9% non-vacuous; 28.3 s); T7 at **2·10^6 tasks** → label-free ceiling
  0.739684 vs verifier ceiling 1.0, gap **0.260316 = mean δ** (budget-invariant to 1e-12), water-filling
  > uniform at every rung (20.1 s). Ran on a 12 GB TITAN Xp (torch 2.5.1+cu118) with 56 vCPU; commands,
  seeds and shas are in §5.4 and `artifacts/`.
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
| `paper.pdf` | compiled paper v6.1 (24 pages, 12 figures, 13 tables) |
| `drafts/paper_planC_draft_v6.1.md` | Markdown source of the paper v6.1 (8,198 words) |
| `writeup_kaggle_v6.1.md` | Kaggle paper-track writeup (1,500 words, final) |
| `artifacts/verifier/` | verifier experiment JSON+MD (eval120 0/120, train12 1/12, learned-rule/LLM nulls) |
| `artifacts/gpu_sim/` | GPU-scale T6/T7 validation JSON+MD + raw simulation outputs |
| `artifacts/raw/` | canonical engine outputs used for the paper tables |
| `artifacts/final_lb_snapshot_2026-11-02.*`, `artifacts/lb/` | final public-LB snapshot (2026-11-02T00:02:58Z) and provenance |
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
- Kaggle notebook: `wen134/arc2026-ttt` (L4×4, offline; competition submission ref **57681632** is the
  champion entry). The final Nov 2 entry re-submits the best COMPLETE version.
- Verifier + GPU experiments: `make verifier-eval`, `make verifier-train-smoke`, `make learned-rules`,
  `make gpu-bound`, `make gpu-alloc` in `arc-selection/lab/` (GPU optional; CPU fallback works).

## Citation

```bibtex
@misc{arc2026twoguesses,
  title  = {Compute Cannot Buy Identifiability: Information-Limited Two-Attempt Selection in ARC-AGI-2 Solver Pools},
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
