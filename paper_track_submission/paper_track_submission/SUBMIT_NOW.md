# FINAL STATUS — 2026-11-02 (competition closed)

- **Champion: S5b ref `57854697` = 16.67 public LB** (seven scored submissions; prior S5 `57681632` = 16.25).
- Final duplicate `57887571` (same v24 config) is PENDING and not used as evidence; best-of-submissions keeps 16.67.
- Final LB snapshot 2026-11-02: 3,591 teams; our team rank **2,429** at 16.67.
- Paper: `paper_planC_draft_v6.1.md` / `paper.pdf` v6.1; writeup `writeup_kaggle_v6.1.md` (1,500 words, 0 markers); paper-track submission ID **57854697**.
- Repository push pending Lead/QC; paper track deadline 2026-11-08.

---

# 两个比赛的提交页 — 最终操作清单

生成时间：2026-11-01 ~11:30 UTC。本文件说明**哪些提交已自动完成/已排程**，以及**需要你在浏览器点完的最后一步**。

---

## 1) 主赛道：ARC Prize 2026 — ARC-AGI-2（代码竞赛）

提交页：https://www.kaggle.com/competitions/arc-prize-2026-arc-agi-2/submissions

- **状态：已自动排程，无需你操作。** 今天的每日 1 次提交额度已被 S5b（ref 57854697，11-01 00:10Z）用掉，
  Kaggle 每日额度在 00:00 UTC 重置。最终提交已由自动化任务在 **2026-11-02T00:00:25Z** 执行：
  - 若 S5b 分数 > 16.25 → 提交 **v24**（S5b）；
  - 否则提交 **v16**（S5 配置，当前 champion **16.25**，ref 57681632）。
  - 提交后自动核对 PENDING 状态并记录 ref 到 `logs/kaggle_submissions.md`。
- 你可以随时在提交页看到最终 ref；最终排名取最好公开分（当前 16.25）。

## 2) 论文赛道：ARC Prize 2026 — Paper Track（Hackathon）

提交页：https://www.kaggle.com/competitions/arc-prize-2026-paper-track

**为什么必须由你在浏览器完成**：Kaggle Hackathon 的 "submission" 是 **Writeup**（在比赛页的 Writeups 标签下创建），
公开 API 没有创建/提交 writeup 的端点（已实测：`kaggle` CLI 2.2.4 + `kagglesdk` 0.1.38 均无该端点；直接上传文件被
服务端拒绝且不产生 submission，5/天额度未消耗；HackathonApiService 的 list 接口对 API token 返回 403 需网页会话）。
因此最后一步需要你的已登录浏览器，约 2–3 分钟。

### 2.1 需要粘贴/上传的内容（全部已就绪）

| 项 | 文件/值 |
|---|---|
| 标题 | `Compute Cannot Buy Identifiability: Information-Limited Two-Attempt Selection in ARC-AGI-2 Solver Pools` |
| Writeup 正文（≤1,500 词，已 1,496 词） | `paper/paper_track_submission/WRITEUP_BODY.md`（整体复制粘贴） |
| 封面（可选） | `paper/cover.png` |
| 媒体图 1 | `paper/figures/fig1_pipeline.png` + 说明（见 §2.3） |
| 媒体图 2 | `paper/figures/fig9_verifier_identifiability.png` |
| 媒体图 3 | `paper/figures/fig7_pool_scaling.png` |
| 媒体图 4 | `paper/figures/fig8_budget_accuracy.png` |
| 论文 PDF | `paper/paper.pdf`（24 页，v6） |
| GitHub（论文+证据） | https://github.com/longlive1234/arc2026-paper |
| GitHub（代码，MIT-0） | https://github.com/longlive1234/arc-selection |
| 公开 notebook 链接 | https://www.kaggle.com/code/wen134/arc2026-ttt （需先将该 notebook 设为 Public） |
| 主赛道 submission ID | **57681632**（champion S5 L4，16.25%） |
| arXiv（可选） | `paper/arxiv_source/` 可直接上传 Overleaf/arXiv |

### 2.2 操作步骤

1. 打开 https://www.kaggle.com/code/wen134/arc2026-ttt → **Settings → Visibility → Public**（竞赛于
   2026-11-02 23:59 UTC 结束后再公开也可；论文截止 2026-11-09）。
2. 打开 https://www.kaggle.com/competitions/arc-prize-2026-paper-track → **Writeups → New Writeup**
   （或页面上的 "Submit" → 创建 writeup；Hackathon 的提交即 writeup）。
3. 标题填上表第一行；正文整体粘贴 `WRITEUP_BODY.md` 的内容。
4. 通过编辑器上传/插入 4 张媒体图（顺序与说明见 §2.3；`cover.png` 可设为封面）。
5. 在正文/链接区确认三处 URL：notebook、`arc-selection`、`arc2026-paper`；正文已包含。
6. 保存后点击 **Submit writeup to this competition**（页面可能显示 "Submit" / "Link to competition"），
   确认 submission 出现在 My Submissions / Writeups 中。每日 5 次额度，可用。
7. 完成后把 writeup URL / submission 记录发我，我更新 `logs/` 与最终报告。

### 2.3 媒体图上传顺序与说明（英文，直接粘贴）

1. `fig1_pipeline.png` — "Offline TTT system: demonstrations → D4×S10 augmentation → per-task LoRA TTT → threshold-DFS decoding → candidate pool → coverage selection → two attempts. Schematic; no measured numbers."
2. `fig9_verifier_identifiability.png` — "Verifier search on public eval: g_V(d) eval vs train control; impossibility-certificate fraction; class ambiguity; cost by depth. Public eval, labels scoring-only, not a competition entry; depth 3 not imputed."
3. `fig7_pool_scaling.png` — "Prefix coverage vs candidate-prefix L (CompressARC, pilot16, dev20 S1/S5/S5_ens): alpha-hat=1.83 [1.67,2.06], L*≈257 for CompressARC; fixed-solver top-2 reported separately. Model fit, not a T7 test."
4. `fig8_budget_accuracy.png` — "Final public-LB snapshot 2026-11-01: 3,572 teams; our champion rank 2,414 at 16.25 (3 tied); anchors #30 68.06 … #1000 30.97. Public-half context only; no medal/SOTA claim."

**不要上传** Fig. 9 diversification-threshold（已撤销）或任何 PILOT 标注资产作为证据。

---

## 3) S5b 最后一行更新

S5b（ref 57854697，v24 = S5 + eval_color_perms=2）当前 PENDING，预计 2026-11-01 ~14:00 UTC 出分：
- 若 >16.25：论文正文的 "pending" 改为该分数，并注明 champion 变为 S5b；
- 否则：改为 "S5b completed at X%, below S5; final entry v16 S5 = 16.25"。
我将在出分后自动更新 `WRITEUP_BODY.md` 并重新生成 PDF，无需你等待（论文赛道截止 11-09，时间充足）。

## 4) 已完成核对的交付物

- 论文 v6：`paper/paper_planC_draft_v6.md`（8,152 词、42 refs、12 figs、0 placeholders、QC green）
- PDF `paper/paper.pdf`（24 页）、arXiv `paper/arxiv_source/`
- 已推送 GitHub：`arc2026-paper` main `b5a252a`（含 v6 + 验证器/GPU artifacts）、`arc-selection` main `f371ba7`（lab 脚本）
- 证据审计：`paper/evidence_table.md`（含 C73–C75）
