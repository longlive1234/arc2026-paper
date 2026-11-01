# Kaggle Paper-Track package — v5 (2026-11-08 deadline)

**Paper submission ID: `57681632`** (S5 L4 v16; public LB **16.25%**, champion). S1 ref 57663405 (14.17%) is the first scored attempt; S6 57716141 = 15.42%, S5_ens 57752011 = 15.42%, S5+LegC 57785740 = 14.17% (negative), CPU probe 57500870 = 0.00.

## Writeup

- `paper/writeup_kaggle_v5.md` — sha256 `c9750e3eebff3912ffb11032bc79b899e1d67d9a0d85c68da60dc7b136713110`
- **1,492 raw words** / 1,487 non-placeholder (limit 1,500); 4 markers (S5b pending + 3 publication URLs).
- Honest framing: unconditional T6 certificate is **vacuous** on our pools (I≥2T²); gain=T on dev20 S2/S5/S5_ens; CompressARC −2.25 pp; +8.11 pp S5_ens headroom selectable but unrealized (hidden 15.42 < S5 16.25); T7 consistent-not-conclusive (n=6, truncation, S6 bug); best hidden 16.25; reference replication 3/20.

## Media gallery — upload order (4)

| order | file | caption (≤80 words) |
|---|---|---|
| 1 | `paper/figures/fig1_pipeline.png` | Offline TTT system: demonstrations → D4×S10 augmentation → per-task LoRA TTT → threshold-DFS decoding → candidate pool → coverage selection → two attempts. Schematic; no measured numbers. |
| 2 | `paper/figures/fig7_pool_scaling.png` | Prefix coverage vs candidate-prefix L under a rank power-law model (CompressARC, pilot16, dev20 S1/S5/S5_ens): α̂=1.83 [1.67,2.06] and L*≈257 for CompressARC; fixed-solver top-2 reported separately. Model fit, not a T7 test. |
| 3 | `paper/figures/fig9_budget_ladder.png` | Candidate-prefix replay (D2): unidentifiable subsets are flat by construction, identifiable subsets rise. **Definitional; not evidence for T7.** |
| 4 | `paper/figures/fig8_budget_accuracy.png` | Final public-LB snapshot 2026-11-01: 3,572 teams; our champion rank 2,414 at 16.25 (3 tied); anchors #30 68.06 … #1000 30.97. Public-half context only; no medal/SOTA claim. |

Optional cover: `paper/cover.png`. Do **not** upload Fig. 9 (omitted diversification-threshold plot) as evidence; no PILOT-labelled asset as evidence.

## Final scoreboard (public LB, hidden half)

| ref | config | publicScore | note |
|---|---|---|---|
| **57681632** | **S5 L4 v16** | **16.25** | **champion; paper submission ID** |
| 57716141 | S6 dual-config v22 | 15.42 | below S5 |
| 57752011 | S5_ens two-model v23 | 15.42 | below S5 |
| 57663405 | S1 L4 v8 | 14.17 | first scored attempt |
| 57785740 | S5+LegC v25 | 14.17 | LegC net-negative (−2.08 vs S5) |
| 57500870 | CPU-version probe | 0.00 | probe only |
| 57456856 | S1 v8 rerun | — | budget-parse error, no score |
| 57442788 | CPU-fallback insurance | — | invalid format |
| 57854697 | S5b v24 | pending | final Nov 2 entry = v16 unless S5b > 16.25 |

Confounders: hidden size unknown (120–240); truncation at 578 s cap; S6 selection bug; S5_ens 53-task superset; n=6; reference replication 3/20; ~30 notebook band external only. No SOTA/medal claim.
