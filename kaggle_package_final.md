# Kaggle Paper-Track package — final (2026-11-02)

**Competition submission ID for the paper (final champion): `57681632`**
(S5 L4, kernel v16; public LB **16.25**; S1 14.17 also cited as first scored attempt.)

## 1. Writeup

- File: `paper/writeup_kaggle_v4.md` — sha256 `f107e064c77f888655daa3d86affae7d0a82fb7d4104ada21dcb97efe03696a2`
- Length: **1,481 raw words** / 1,476 non-placeholder (limit 1,500); 30 refs not required for the writeup.
- Final results stated: S5 16.25 (champion), S6 15.42, S5_ens 15.42, S1 14.17, S5+LegC 14.17 (negative),
  CPU probe 0.00; dev20 S1 20.0%; reference replication 3/20; no score above 16.25; no SOTA/medal claim.
- Links to fill at upload: notebook `https://www.kaggle.com/code/wen134/arc2026-ttt` (version 16);
  repo `https://github.com/longlive1234/arc2026-paper`; paper/release URL (fill at publication).
  These are the only `[[V4-PEND: URL]]` markers in the writeup.

## 2. Media gallery — upload in this order (4 images)

| order | file | caption (gallery field; does not count in body) |
|---|---|---|
| 1 | `paper/figures/fig1_pipeline.png` | Offline TTT system: demonstrations → augmented TTT → threshold-DFS decoding → candidate pool → calibrated coverage selection → two-attempt submission. Schematic; no measured numbers encoded. |
| 2 | `paper/figures/fig4_selection_schematic.png` | Coverage-optimal selection schematic: candidates grouped by relation class, calibrated p̂/ρ̂, pair coverage U, chosen distinct pair. Toy values only — illustrative, not measured. |
| 3 | `paper/figures/fig2_selection_rules.png` | Selection rules on A/B/C: pass@2 with 80%/95% bootstrap CIs; oracle is a ceiling, not a rule. C is simulated and not evidence about real solvers. |
| 4 | `paper/figures/fig3_pool_diagnostics.png` | Pool diagnostics: oracle gap, duplicate rates, relation-class ρ with pair counts, calibration reliability. |

Optional cover: `paper/cover.png`. Do **not** upload Fig. 9 (omitted; exact-match exclusivity makes the
positive-ρ test inapplicable) or any PILOT-labelled asset as evidence.

## 3. Final scoreboard (public LB, hidden half; cite exactly)

| ref | config | publicScore | note |
|---|---|---|---|
| **57681632** | **S5 L4 v16** | **16.25** | **champion; paper submission ID** |
| 57716141 | S6 dual-config v22 | 15.42 | below S5 |
| 57752011 | S5_ens two-model v23 | 15.42 | below S5 |
| 57663405 | S1 L4 v8 | 14.17 | first scored attempt |
| 57785740 | S5+LegC v25 | 14.17 | negative: LegC −2.08 vs S5 |
| 57500870 | CPU-version probe | 0.00 | probe only |
| 57456856 | S1 v8 rerun | — | budget-parse error, no score |
| 57442788 | CPU-fallback insurance | — | invalid format |
| 57854697 | S5b v24 | pending (Nov 1) | final Nov 2 entry = v16 unless S5b > 16.25 |

Honest framing: six scored submissions, none above 16.25; ~30 public-notebook band is external context
only; hidden-set size unknown; no SOTA/medal claim; compute quota exhausted Oct 31–Nov 1.
