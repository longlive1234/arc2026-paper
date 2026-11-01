# ARC Prize 2026 — Paper Track submission package (v6, prepared 2026-11-01)

Status: **ready except the owner-only Kaggle upload steps**. All paper artifacts are frozen in the repo;
the competition's scored submission ID is known (below). The final Nov-2 competition entry may add one more
submission ref but does not change the paper's reported numbers.

## What to submit on Kaggle (Paper Track, deadline 2026-11-08)

| requirement | artifact | status |
|---|---|---|
| Writeup ≤ 1,500 words | `paper/writeup_kaggle_v6.md` (1,476 non-placeholder; final for v6; only the S5b score line is filled at freeze) | **ready** |
| Media gallery (images + captions) | order/captions in `paper/gallery_order.md`; cover `paper/cover.png`; figures in `paper/figures/` (Fig. 8 = final LB snapshot; Fig. 9 = verifier identifiability) | **ready** |
| Paper PDF | `paper/paper.pdf` v6 (24 pages, 42 refs, 12 figures; sha at freeze) + GitHub `longlive1234/arc2026-paper` | **ready** |
| Public notebook link | Kaggle notebook **`wen134/arc2026-ttt`** — currently private; make it **public** (owner action) and insert its URL in the writeup | **owner action** |
| Submission ID (ARC-AGI-2) | **`57681632`** — champion S5 L4, publicScore **16.25**; other scored refs in `logs/kaggle_submissions.md` (final Nov-2 ref appended at close) | **ready** |
| Open-source requirement | `https://github.com/longlive1234/arc-selection` (MIT-0: solver/benchmark/lab scripts) and `https://github.com/longlive1234/arc2026-paper` (CC BY 4.0: paper/evidence) | **ready** |
| Numeric-evidence audit | `paper/evidence_table.md` (C-rows incl. C73–C75 for v6 verifier/GPU experiments) and `paper/evidence_audit_v4.md` | **ready** |

## Exact owner actions (in order)

1. **Make the notebook public** (after the competition closes on 2026-11-02 23:59 UTC, or as the owner
   prefers): Kaggle → `wen134/arc2026-ttt` → Settings → visibility Public. Public URL:
   `https://www.kaggle.com/code/wen134/arc2026-ttt`.
2. **Upload the writeup** on the Paper Track submission page: paste `paper/writeup_kaggle_v6.md`
   (≤1,500 words), insert the notebook/repo/paper URLs and the submission ID `57681632` (the writeup file
   already contains the URLs and the S5b line; verify the final ref if the Nov-2 entry is required).
3. **Attach the media gallery** in `paper/gallery_order.md` order (4 images, captions provided).
4. **Link the paper PDF / GitHub repo** (`https://github.com/longlive1234/arc2026-paper`); optional arXiv
   upload from `paper/arxiv_source/` (Overleaf instructions in `paper/arxiv_source/README_OVERLEAF.md`).
5. Done — no further engineering work needed.

## Honest-content invariants (do not violate at freeze)

- Failed/errored attempts are reported verbatim (`57456856` rerun error with root cause; `57442788` invalid
  format; `57500870` CPU probe 0.00); never presented as scores.
- Champion **16.25%** public LB (rank 2,414/3,572 on the 2026-11-01 snapshot); no SOTA/medal claim; the ~30
  public-notebook band is external context only; hidden-test size unknown.
- The v6 verifier module is an honest **negative/validity result** on public eval (0/120 certified at depth 2;
  1/12 training control); the LLM reasoner null is infrastructure-limited (token truncation).
- Theorem 6 is proven but empirically **vacuous** on our pools; Theorem 7 is conditional; Theorem 8 holds
  in principle but its coverage premise fails for our bounded hypothesis class. These labels must stay.
- The TITAN-Xp/56-core numbers are reproducible from `arc-selection/lab/gpu_theory_sim.py` with the exact
  commands/seeds in §5.4 of the paper.
