# Kaggle Paper-Track package — v6.1 FINAL (2026-11-02)

**Paper submission ID: `57854697`** (S5b L4 v24; public LB **16.67%**, champion; seven scored submissions).
Prior best: S5 57681632 = 16.25; S6 57716141 = 15.42; S5_ens 57752011 = 15.42; S1 57663405 = 14.17; S5+LegC 57785740 = 14.17 (negative); CPU probe 57500870 = 0.00. Final duplicate 57887571 pending; not used as evidence.

## Artifacts

- **Paper:** `paper/paper_planC_draft_v6.1.md` sha `bcf0cae8…`; **8,198 words** (cap 8,200); 42 refs; 12 figures; 0 markers.
- **PDF:** `paper/paper.pdf` sha `0b7c8622…` (24 pp).
- **arXiv/Overleaf:** `paper/arxiv_source/main.tex` sha `33f70b64…` (12 figures, 13 tables, 42 refs).
- **Writeup:** `paper/writeup_kaggle_v6.1.md` sha `35b88ec3…`; **1,500 raw / 1,500 non-placeholder** (limit 1,500); **0 markers**; submission ID 57854697.
- **Form fields:** `paper/paper_track_submission/FORM_FIELDS.md`; description/body updated to v6.1 (1,487 words).

## Final results (public LB, hidden half)

| ref | config | publicScore | note |
|---|---|---|---|
| **57854697** | **S5b L4 v24** | **16.67** | **champion; paper submission ID** |
| 57681632 | S5 L4 v16 | 16.25 | prior best |
| 57716141 | S6 dual-config v22 | 15.42 | below S5 |
| 57752011 | S5_ens two-model v23 | 15.42 | below S5 |
| 57663405 | S1 L4 v8 | 14.17 | first scored attempt |
| 57785740 | S5+LegC v25 | 14.17 | LegC net-negative (−2.08 vs S5) |
| 57500870 | CPU probe | 0.00 | probe only |
| 57887571 | S5b duplicate | pending | final duplicate; LB best stays 16.67 |

**T7 honesty:** S5b = S5 + second evaluation-time colour permutation (≈2× decode compute); **generation-side change, not allocation**; does not violate conditional T7 (fixed-pool allocation) and supports the generation-bottleneck verdict. Hidden ladder: S5b 16.67 > S5 16.25 > S6 = S5_ens 15.42 > S5+LegC 14.17; consistent, not conclusive.

**Final LB snapshot 2026-11-02T00:02:58Z:** 3,591 teams, leader 88.06; our team "wen Chen" (TeamId 17156552) rank **2,429** at 16.67; anchors #30 69.72, #50 57.78, #100 39.17, #200 33.06, #500 31.81, #1000 30.97. Public-half context only; no medal/SOTA claim.

## Media gallery — upload order (4)

| order | file | caption (≤80 words) |
|---|---|---|
| 1 | `paper/figures/fig1_pipeline.png` | Offline TTT system: demonstrations → D4×S10 augmentation → per-task LoRA TTT → threshold-DFS decoding → candidate pool → coverage selection → two attempts. Schematic; no measured numbers. |
| 2 | `paper/figures/fig9_verifier_identifiability.png` | Verifier-first search on public eval: g_V(d) eval vs train control; impossibility certificates; class ambiguity; cost per depth. Public eval only; labels scoring-only; depth 3 not imputed. |
| 3 | `paper/figures/fig7_pool_scaling.png` | Prefix coverage vs candidate-prefix L (CompressARC, pilot16, dev20 S1/S5/S5_ens): α̂=1.83 [1.67,2.06], L*≈257 for CompressARC; fixed-solver top-2 separate; model fit, not a T7 test. |
| 4 | `paper/figures/fig8_budget_accuracy.png` | Final public-LB snapshot 2026-11-02: 3,591 teams; our champion rank 2,429 at 16.67 (three teams tied); anchors #30 69.72 … #1000 30.97. Public-half context only; no medal/SOTA claim. |

Do not upload the retired diversification-threshold figure or PILOT-labelled assets as evidence.
