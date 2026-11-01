# ARC Prize 2026 项目最终报告（主赛道已冻结，论文赛道待上传）

> 生成时间：2026-11-01（UTC）。所有数字均来自可复现产物：
> `paper/evidence_table.md`、`paper/evidence_audit_v4.md`、`logs/kaggle_submissions.md`、`analysis/`。
> 主赛道截止：2026-11-02 23:59 UTC；论文赛道截止：2026-11-08。

## 一、最终比赛成绩（诚实记录）

| 日期 (UTC) | ref | 配置（kernel 版本） | 状态 | publicScore |
|---|---|---|---|---|
| 2026-10-21 | 57456856 | S1 L4 v8（rerun budget 解析 bug） | COMPLETE（error） | — |
| 2026-10-22 | 57500870 | CPU-version 探针 v3 | COMPLETE | **0.00** |
| 2026-10-26 | 57663405 | **S1 L4 v8**（aug8 / 64 行 / 64 步 / beam 4，578 s 上限） | COMPLETE | **14.17** |
| 2026-10-27 | 57681632 | **S5 L4 v16**（单模型 + palette/dim penalty + rescue ladder + aug-by-demos） | COMPLETE | **16.25 → 最终 champion** |
| 2026-10-28 | 57716141 | S6 双配置 L4 v22（A aug8 + B aug16/eval2） | COMPLETE | **15.42** |
| 2026-10-29 | 57752011 | S5_ens 双模型 L4 v23（sorokin + xcalibur，fixed selection） | COMPLETE | **15.42** |
| 2026-10-30 | 57785740 | S5 + LegC 验证归纳混合 L4 v25 | COMPLETE | **14.17**（负结果：−2.08 vs S5） |
| 2026-11-01 | 57854697 | S5b L4 v24（S5 + eval_color_perms=2） | PENDING | 待出分 |
| 2026-11-02 | 待填 | 最终提交：v16 (S5, 16.25) 或 v24（若 >16.25） | — | — |

**结论**：6 次有效评分中最好成绩为 **16.25%**（S5 单模型配置）。距公开 notebook 区间（≈29.7–31.4）
仍有明显差距，不宣称 SOTA/奖牌。GPU 周配额在 10-31 耗尽（刷新在 11-07，晚于截止），
11-01 起无法再创建新版本，最终只能从既有 COMPLETE 版本中选择。

## 二、原创理论（5 条定理 + 1 条修正）

1. **两 attempt 覆盖目标**：`U(a1,a2)=1−P(¬C1∧¬C2)` 的形式化；独立情形下 top-2 最优。
2. **重复候选严格劣于不同候选**（duplicate dominance）。
3. **正相关下 argmax-once 次优**（精确 Bernoulli 相关配对公式）。
4. **多样化阈值定理**：`ρ < ρ* = sqrt(p2(1−p1)/(p1(1−p2)))` 时 pair 严格优于重复 top-1，
   增益 `ΔU = sqrt(p1(1−p1)p2(1−p2))(ρ*−ρ)`。
   **重要修正（实测驱动）**：对 *exact-match* 验证器，两个不同网格互斥（`C1∧C2=∅` ⇒ ρ<0），
   定理 4 的正相关阈值区间不可达；此时 top-2 = 按校准概率排序的两个最大者（Corollary 4），
   真实候选池上的负结果来自**估计/可识别性**（Prop. 5）而非 ρ 门槛。Corollary 3 仅对
   non-exclusive 验证器成立（论文 v4 已修正，Table 10 改为 EXPLORATORY 检查，Fig. 9 撤销）。
5. **预算约束覆盖分配定理**：凹覆盖函数下均匀分配最优（Jensen）；异质凹函数下贪心/注水最优；
   边际单交叉 ⇒ 难度阈值规则；饱和时多算力应重分配。

## 三、真实数据与消融（dev20 = 公开 eval 20 任务 / 32 输入，L4×4）

| config | task-level | input-level | 备注 |
|---|---|---|---|
| S1 | 4/20 = 20.0% | 6/32 = 18.8% | 578 s 上限，decode 均值 ≈235 s |
| S2 (aug16) | 2/20 = 10.0% | 5/32 = 15.6% | 预算截断 |
| S5 | 3/20 = 15.0% | 5/32 = 15.6% | hidden 16.25 → 最好 |
| S6 双配置 | A 轮 4/20；A∪B 5/20 | — | hidden 15.42（no gain）|
| S5_ens 双模型 | 无干净读（dev 包手册分支问题）| — | hidden 15.42（no gain）|
| 参考实现（public notebook 复刻）| **3/20 = 15.0%**（60 min 预算，仅处理 13/20） | 5/21 | 每任务 ≈17 min → 240 任务会截断 |
| S5 + LegC 混合 | 未完成干净 dev 读 | — | hidden 14.17（LegC 预检 1 h 挤压 base）|

**核心经验**：(a) hidden 分数与 dev20 排序不完全一致；(b) 更“强”的组合（S6/S5_ens/LegC）
均未超过单模型 S5，说明在 12 h/240 任务预算下**预算分配与截断**比模型多样性更关键；
(c) 公开 notebook 参考实现与我们同量级，其高分更依赖完整 12 h 预算与特定数据条件。

## 四、交付物

- **论文（v4 冻结版）**：`paper/paper.pdf`（重建后）、`paper/paper_planC_draft_v4.md`（sha 见 evidence C60 系列）
- **Kaggle writeup（≤1500 词）**：`paper/writeup_kaggle_v4.md`
- **公开仓库**：
  - https://github.com/longlive1234/arc-selection （MIT-0：代码 + CPU 基准 + 全部测试）
  - https://github.com/longlive1234/arc2026-paper （CC BY 4.0：论文 + 证据表 + 图）
- **提交系统**：`notebook/ttt_packet/`（pinned packets + push/gate/monitor 工具链）
- **提交账本**：`logs/kaggle_submissions.md`（含失败提交与负结果，逐条可查）
- **论文赛道包**：`paper/paper_track_submission/`（writeup + 媒体画廊顺序 + notebook 链接 + submission ID）

## 五、诚实边界

- 失败/无效提交全部记录：#57442788 invalid format；#57456856 rerun crash 根因 + 修复；
  #57500870 CPU 探针 0.00；10-30 LegC 负结果；10-31 提交因会话缺口错过（recorded）。
- hidden test 大小未知（120/172 或 240/259 均为本地 sample 形状，非官方披露）。
- 不宣称 SOTA/奖牌；LB 百分位仅为 2026-10-20 snapshot 的外部参照。
- 理论主张限定在实测支持范围：A 集负结果、B 集 pilot、C 集模拟机制验证；
  Theorem 4 的 exact-match 修正为 v4 的核心诚实修正。

## 六、剩余用户动作（论文赛道，截止 2026-11-08）

1. 在 Kaggle "ARC Prize 2026 — Paper Track" 页面提交论文：上传 `paper/paper.pdf`（或 arXiv 链接）+ writeup 正文 + 媒体画廊（按 `paper/gallery_order.md` 顺序）。
2. 关联主赛道提交 ID：**57681632**（最终 champion，或 11-02 最终提交的 ref）。
3. 公开 notebook/仓库链接：`https://github.com/longlive1234/arc-selection`、`https://github.com/longlive1234/arc2026-paper`。
4. 如需 arXiv：上传 `paper/arxiv_source/` 目录。
