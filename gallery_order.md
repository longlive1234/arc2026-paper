# Media gallery order & captions — Kaggle writeup upload

Companion to `paper/writeup_kaggle_upload.md` (1473 words, seven inline `media/image_k.png`
references) and `paper/writeup_draft_v1.md` (1466 words, de-tagged working text).
Reference paths in the writeup are **placeholders**: after uploading each file through the Kaggle
writeup editor, replace `media/image_k.png` with the URL Kaggle returns. The order below is the order
the images appear in the writeup body (Approach → Theory → Progress) and therefore the order to upload.
Keep each caption in the Kaggle gallery caption field (captions do not count toward the writeup body).

**Suggested cover image:** `paper/cover.png` (1200×630, ~1.9:1) — title band + public-eval task
panels + two-attempt selection schematic, with honesty labels ("uncalibrated prior", "illustrative,
not a measured result"). Fallback if a reviewer prefers a data-only cover:
`analysis/figures/fig10_eval_task_gallery.png` (see `figures_plan.md` §1).

---

## 1. Ordered upload list

| order | upload file | writeup ref | position in `writeup_kaggle_upload.md` | status |
|---|---|---|---|---|
| 1 | `paper/cover.png` | — (cover field) | cover / media-gallery header | EXISTS |
| 2 | `analysis/figures/fig3_symmetry.png` | `media/image_1.png` | Approach, after the pipeline paragraph | EXISTS (800×340) |
| 3 | `paper/fig_selection_concept.png` | `media/image_2.png` | Theory, after the estimator paragraph | EXISTS (1600×640) |
| 4 | `analysis/figures/fig10_eval_task_gallery.png` | `media/image_3.png` | Progress, after "Without a GPU we can still measure the benchmark." | EXISTS (800×670) |
| 5 | `analysis/figures/fig5_taxonomy.png` | `media/image_4.png` | Progress, after image_3 | EXISTS (800×400) |
| 6 | `analysis/figures/fig6_train_vs_eval.png` | `media/image_5.png` | Progress, after the train/eval-shift sentence | EXISTS (800×360) |
| 7 | `analysis/figures/fig9_baselines.png` | `media/image_6.png` | Progress, after the trivial-heuristics sentence | EXISTS (800×340) |
| 8 | `analysis/figures/fig11_difficulty_solvability.png` | `media/image_7.png` | Progress, after the solvability-prior sentence | EXISTS (800×350) |
| — | `analysis/figures/fig8_colour.png` | — (optional) | gallery extra: colour/S10 rationale | EXISTS (800×340) |
| — | `analysis/figures/fig1_grid_sizes.png` | — (optional) | gallery extra: grid sizes | EXISTS (800×320) |
| — | `analysis/figures/fig2_output_size.png` | — (optional) | gallery extra: output-size relations | EXISTS (800×340) |
| — | `analysis/figures/fig4_objects.png` | — (optional) | gallery extra: object statistics | EXISTS (800×320) |
| — | `analysis/figures/fig7_difficulty.png` | — (optional) | gallery extra: difficulty proxy | EXISTS (800×320) |
| — | `paper/figures/fig_pipeline.png` | slot on build | Approach (F1 pipeline diagram) | TO BUILD — no GPU needed |
| — | `paper/figures/fig_selection.png` | slot on build | Results/Theory (F2 real replay figure) | BLOCKED on B1/B2 |
| — | `paper/figures/fig_ttt_aug.png` | slot on build | Progress (A3/A4 curves) | BLOCKED on GPU |
| — | `paper/figures/fig_scaling.png` | slot on build | Progress (A10 scaling) | BLOCKED on GPU |
| — | `paper/figures/fig_failures.png` | slot on build | Limitations (failure taxonomy) | BLOCKED on B1 |

Notes:
- Optional extras (fig8, fig1, fig2, fig4, fig7) may be added only if the editor/word-count budget
  allows (each inline image adds ~3 words to the body; the Kaggle draft is 27 words below 1500).
- Blocked evidence figures must **not** be uploaded as evidence. If a figure is ever shown from
  simulated/CPU-fallback pools, it needs the handoff banner "pipeline validation — not TTT evidence;
  no claim" (`research/design/paper_writer_handoff.md` §3).
- Existing analysis figures are 800 px wide. If the editor rejects them, re-render
  `analysis/figures.py` at higher dpi (currently saves at 100 dpi; a one-line change, owner
  data-analyst) — the figure data itself is regenerable from `bash analysis/run_all.sh`.
- When F1 is built, insert it right after the cover and renumber `media/image_k.png` / the
  `gallery_order` rows; recount the writeup body (~+3 words).

---

## 2. Captions (≤80 words each; paste into the Kaggle gallery caption field)

**Cover** — *"Two Guesses, Correlated Candidates: title band, public ARC-AGI-2 evaluation task grids from the analysis gallery, and a schematic of the two-attempt selection idea. The selection panel is illustrative, not a measured result; tier labels in the task panels are an uncalibrated prior, not solve rates."*

**Image 1 — D4 symmetry.** *"D4 symmetry is latent rather than free: inputs are invariant under a non-identity D4 operation in 13.8% of training tasks, outputs in 25.6%, while the identity solves none. This motivates D4 augmentation and shows why the augmentation prior can be invalid on some tasks (analysis/report.md §6)."*

**Image 2 — selection schematic.** *"Illustrative schematic of the coverage-optimal two-attempt rule: candidate pool grouped by relation class, calibrated p̂/ρ̂, pair coverage U(a1,a2), and the chosen pair. Toy values are chosen to illustrate the formula — NOT measured; no TTT candidate pool exists yet (GPU platform-blocked)."*

**Image 3 — public-eval task gallery.** *"Eight public-eval tasks shown as train input → train output | test input, spanning the TTT-solvability tiers A/B/C with budget weights. Tier assignment is an uncalibrated prior from `analysis/allocator.py`, not a measured solve rate. Grids are rendered at original resolution with the official ARC palette (analysis/report.md §15)."*

**Image 4 — task taxonomy.** *"Rule-based task families (priority-ordered decision list) for the 1,000 training and 120 public-eval tasks. Same-size pixel rewriting dominates both (54.5% train, 57.5% eval); every eval family also occurs in train. Benchmark characterisation only — no solver result. Source: analysis/report.md §9."*

**Image 5 — train vs eval shift.** *"Public eval is shifted harder than train: larger grids, more colours, fewer demonstrations, and less often a black-0 background. Left: prevalence indicators; right: eval/train mean ratios. Computed from the public data release only (analysis/report.md §11); no solver performance is shown."*

**Image 6 — trivial baselines.** *"Trivial-floor baselines: eight single-rule heuristics solve 1.6% of training, 1.5% of holdout and 0% of public-eval tasks. Per-cell modal output fits 43% of training tasks but solves only 2. Solver results should be reported net of this floor. Source: analysis/report.md §13."*

**Image 7 — solvability prior.** *"Difficulty proxy versus task size (left) and the TTT-solvability prior versus maximum grid dimension (right). Public-eval tasks cluster large and hard. The prior is uncalibrated until per-task TTT logs exist; it is a scheduling prior, not a solve rate (analysis/report.md §15–16)."*

Optional extras (if inserted): colour statistics (§4), grid sizes (§3), output-size relations (§5),
object statistics (§7), difficulty proxy (§10) — caption from `analysis/report.md` section noted in
parentheses, always with "analysis only, no solver result".

---

## 3. Upload checklist

- [ ] Cover image set to `paper/cover.png` (or fig10 fallback).
- [ ] Images 1–7 inserted in the order above; replace `media/image_k.png` with the editor's URLs.
- [ ] Captions pasted (≤80 words each); every caption states what is measured vs illustrative.
- [ ] No blocked/simulated evidence figure uploaded; no figure implies a measured solver number.
- [ ] Body re-counted after inserting images (target ≤1500; currently 1473).
- [ ] Alt text retained from the writeup markdown (accessibility + alt fallback).
- [ ] Final gallery passes a thumbnail check: each image readable at ~400 px wide.
