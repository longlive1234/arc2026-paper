# Kaggle Paper-Track Writeup — form field values (copy/paste)

Competition: https://www.kaggle.com/competitions/arc-prize-2026-paper-track/writeups
Generated for the v6 package (S5b line is neutral "pending at submission"; update later if desired).

## 标题 Title (70/80 chars)
```
Compute Cannot Buy Identifiability: Two-Attempt Selection in ARC-AGI-2
```

## Writeup URL / slug (`写字URL`) — pick one, must be unique
```
compute-cannot-buy-identifiability-arc-agi-2
```
If taken, use:
```
compute-cannot-buy-identifiability-two-attempts
```

## 字幕 Subtitle (133/140 chars)
```
An information bound, a conditional compute-separation theorem, and measured limits of label-free two-attempt selection in ARC-AGI-2.
```

## 封面/缩略图 Cover & thumbnail (560 x 280)
Upload: `paper/figures/cover_560x280.png` （已按 560×280 生成）

## 提交路径 Submission path
`Main track`（页面自动选中，保持默认）

## 媒体画廊 Media gallery — 按顺序上传 4 张 + Caption

1. `paper/figures/fig1_pipeline.png`
   Caption: `Offline TTT pipeline: demonstrations → D4×S10 augmentation → per-task LoRA TTT → threshold-DFS decoding → candidate pool → coverage selection → two attempts. Schematic; no measured numbers.`
2. `paper/figures/fig9_verifier_identifiability.png`
   Caption: `Verifier-first search on the public eval split: g_V(d) eval vs train control, impossibility certificates, behaviour-class ambiguity, cost per depth. Public eval only; labels scoring-only; depth 3 not imputed.`
3. `paper/figures/fig7_pool_scaling.png`
   Caption: `Prefix two-attempt coverage vs candidate-prefix L (CompressARC, pilot16, dev20 S1/S5/S5_ens): alpha-hat = 1.83 [1.67, 2.06], saturation L* ≈ 257 for CompressARC. Fixed-solver top-2 reported separately; model fit, not a T7 test.`
4. `paper/figures/fig8_budget_accuracy.png`
   Caption: `Final public-LB snapshot (2026-11-01): 3,572 teams; our champion rank 2,414 at 16.25 (three teams tied). Rank anchors #30 68.06 … #1000 30.97. Public-half context only; no medal/SOTA claim.`

Do NOT upload the retired diversification-threshold figure (Fig. 9 old) or PILOT-labelled assets as evidence.

## 项目描述 Project description
Paste the full content of `paper/paper_track_submission/PROJECT_DESCRIPTION.md`
(1,483 words; ≤1,500; H1 title removed so it does not duplicate the Title field — the body starts at "## Abstract").
It already contains the three URLs, the best-score table, and the honesty caveats.

## 附件 / 项目链接 Attachments & Project links
Add these links (and optionally upload the PDF under Files):

- Paper PDF (upload): `paper/paper.pdf` (24 pp, v6) — or link `https://github.com/longlive1234/arc2026-paper/blob/main/paper.pdf`
- Paper repo (CC BY 4.0): `https://github.com/longlive1234/arc2026-paper`
- Code repo (MIT-0): `https://github.com/longlive1234/arc-selection`
- Notebook (make Public first): `https://www.kaggle.com/code/wen134/arc2026-ttt`
- Main-track submission ID: `57681632` (champion S5 L4, public LB 16.25%)
- arXiv/Overleaf source (optional): `paper/arxiv_source/`

## DOI 引文 DOI citation
Enable ("Create a DOI") — recommended; a DOI is created after the competition closes.

## 最后一步
Save the writeup, then use the page's **Submit / Link to competition** action and confirm it appears under the
competition's Writeups/Submissions. Daily limit is 5; one is enough.
If the form refuses the URL slug (taken), try the fallback slug above and tell me the final URL so I can record it.
