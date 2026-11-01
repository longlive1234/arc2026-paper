# Kaggle Paper-Track package — v6 (2026-11-08 deadline)

**Paper submission ID: `57681632`** (S5 L4 v16; public LB **16.25%**, champion). Other scored: S6 57716141 = 15.42%, S5_ens 57752011 = 15.42%, S1 57663405 = 14.17%, S5+LegC 57785740 = 14.17% (negative), CPU probe 57500870 = 0.00.

## Artifacts

- **Paper:** `paper/paper_planC_draft_v6.md` sha `7545550f…`; **8,109 words** (v6 cap 8,200); 42 refs; 12 figures.
- **PDF:** `paper/paper.pdf` sha `3624cb72…` (24 pp).
- **arXiv/Overleaf:** `paper/arxiv_source/main.tex` sha `37cef939…` (12 figures, 13 tables, 42 refs).
- **Writeup:** `paper/writeup_kaggle_v6.md` sha `0baaf0df…`; **1,478 raw / 1,476 non-placeholder** words (limit 1,500); 1 marker only (S5b pending).

## New in v6

Theorem 8 (verifier-induced identifiability): unique accepted behavior classes close the identifiability gap conditional on reachability; impossibility certificates bound depth allocation; hybrid exact-match correction with frozen notation. Bounded-DSL verifier on public eval120: **0/120 accepted**, 120/120 depth-2 impossibility certificates (334.7 CPU-min, 56 workers); F1a vacuous, F1b INCONCLUSIVE, F2 pre-registered FAIL (hybrid = TTT top-2, H−T=0; complementarity untestable at zero verifier coverage), F3 FAIL at measured depth 2 (depth 3 not measured/not imputed). Train control **1/12** (0520fde7); learned rules 0/120; LLM chat 0/20; LLM reasoner 0/10 (token-cap infrastructure null). GPU-scale implementation checks: T6 1e8 instances, 0 violations at 1e-6 (max excess 1.12e-7); T7 2e6 tasks, gap = mean δ = .260316, water-filling 3.5–8.8× uniform (TITAN Xp 12 GB cu118, 56-core CPU).

Honest framing: verifier numbers are **public-eval diagnostics, labels scoring-only, not a competition entry**; depth 3 is not imputed; LLM null is infrastructure-limited; no hidden-test/SOTA/medal claim; best hidden 16.25; reference replication 3/20.

## Media gallery — upload order (4)

| order | file | caption (≤80 words) |
|---|---|---|
| 1 | `paper/figures/fig1_pipeline.png` | Offline TTT system: demonstrations → D4×S10 augmentation → per-task LoRA TTT → threshold-DFS decoding → candidate pool → coverage selection → two attempts. Schematic; no measured numbers. |
| 2 | `paper/figures/fig9_verifier_identifiability.png` | Verifier search on public eval: g_V(d) eval vs train control; impossibility-certificate fraction; class ambiguity; cost by depth. Public eval, labels scoring-only, not a competition entry; depth 3 not imputed. |
| 3 | `paper/figures/fig7_pool_scaling.png` | Prefix coverage vs candidate-prefix L (CompressARC, pilot16, dev20 S1/S5/S5_ens): α̂=1.83 [1.67,2.06], L*≈257 for CompressARC; fixed-solver top-2 reported separately. Model fit, not a T7 test. |
| 4 | `paper/figures/fig8_budget_accuracy.png` | Final public-LB snapshot 2026-11-01: 3,572 teams; our champion rank 2,414 at 16.25 (3 tied); anchors #30 68.06 … #1000 30.97. Public-half context only; no medal/SOTA claim. |

Do **not** upload Fig. 9 diversification-threshold (omitted) as evidence; no PILOT-labelled asset as evidence.

## Final scoreboard

| ref | config | publicScore | note |
|---|---|---|---|
| **57681632** | **S5 L4 v16** | **16.25** | **champion; paper submission ID** |
| 57716141 | S6 dual-config v22 | 15.42 | below S5 |
| 57752011 | S5_ens two-model v23 | 15.42 | below S5 |
| 57663405 | S1 L4 v8 | 14.17 | first scored attempt |
| 57785740 | S5+LegC v25 | 14.17 | LegC net-negative (−2.08 vs S5) |
| 57500870 | CPU probe | 0.00 | probe only |
| 57854697 | S5b v24 | pending | final Nov 2 = v16 unless S5b >16.25 |
