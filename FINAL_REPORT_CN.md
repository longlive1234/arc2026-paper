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

## 七、论文 v5（原创理论突破，2026-11-08 论文赛道截止前完成）

在用户要求"不要常规策略、要原创新理论"后，我们做了 2026 年 10 月的 arXiv 最新文献扫描（12+ 篇，
含 ARC-AGI-2 Technical Report 2603.06590、Multi-Perspective Transformers 2605.01154（21.7% eval）、
test-time scaling law 2605.10716、pass@k inversion 2607.20543、SPLIT 2610.23255、selectable coverage
2610.32235），并重构论文为 v5：

**标题**：*Compute Cannot Buy Identifiability: Information-Limited Two-Attempt Selection in ARC-AGI-2 Solver Pools*
（compute 不能买来可识别性：ARC-AGI-2 双 attempt 选择的信息极限）

**新增原创理论（已证明）**：
- **Theorem 6（label-free 信息上界）**：exact-match 互斥 ⇒ U=p1+p2；任何使用元数据 Z 的规则满足
  `E[U] ≤ p1+p2 + min{T, sqrt(I(C;Z)/2)}`（TV-Lipschitz + Pinsker + Jensen），附可计算的 pilot 证书。
- **Prop. 6e（非空泛判据）**：当且仅当 `I(C;Z) < 2T²` 时该界严格有信息量；在 score 主导的 exact-match
  候选池中它退化为 oracle 界 —— 这是对 Pinsker 类认证方法本身的**负结果**（诚实呈现，不冒充验证）。
- **Cor. 6g**：score 主导池中全元数据信息界无法认证 label-free 选择。
- **Prop. 6f（构造性修复，最锐利结果）**：拆分 Z=(S,Z′)，`E[U] ≤ U_S + min{g−U_S, sqrt(I(C;Z′|S)/2)}`；
  在 score sufficiency（Prop. 5）成立时恰为 U_S。CompressARC 上首次**非空泛**（cap=12.96pp），
  实测规则损失 −2.25pp 在其内；其余数据集仍空泛、0 违规。
- **Theorem 7（条件性可分离定理，A1–A3 显式）**：`lim_{C→∞} score = Σ_t(g_t∞−Δ_t∞)`，与算力分配无关；
  有 verifier 的分配器才能逼近 `Σ g_t∞` —— 解释了 S6/S5_ens/LegC 在 hidden 上无增益。
- 支撑引理：6a swap regret、6b 固定池单调性（重排序不能造成 pass@k inversion，需 generation drift）、
  6d g·s 描述性分解。T5 降级为 setting observation（与 SPLIT 等重叠，诚实引用）。

**新增真实数据**：pool-scaling 曲线（CompressARC C2 20→28.8% 到 L=20，α̂=1.83；dev20 S5_ens 21.6→29.7%，
α̂=2.75，L*≈7）；identifiability 表（7 数据集、0 违规、6f 仅 CompressARC 非空泛）；关键发现：dev20
S2/S5/S5_ens 的选择增益恰等于 tail T（+6.25/+6.25/+8.11pp），但我们的提交流水线未兑现该 headroom。

**产物**：paper v5 md sha `682eb1ad…`（约 6,700 词，41 refs，11 figs，21 页 PDF `23bac82e…`）、
writeup v5（≤1,500 词，1,495）、arXiv main.tex `3f70db2f…`、repo v2.1（commit `73c3923`，待推送）。

## 八、论文 v6（"超级算法"模块：AWM 启发的验证器优先求解 + 云算力大规模验证）

用户要求以 arXiv 最新工作为启发、在云 GPU 上实现真正的"超级算法"。我们以 **arXiv:2610.40503
"Algebraic World Model"（Pan/Tan/Yuan/Yao, 2026-10-29）** 的 explore→可执行假设→验证→形式化/剪枝
思想为蓝本，结合我们 T6/T7 的信息极限理论，完成以下新模块（全部 CPU/GPU 可复现）：

**新理论 Theorem 8（验证器诱导的可识别性）**：
(i) 若验证后仅剩一个行为等价类，可识别性缺口 Δ=0，覆盖率达 g_V(d)；(ii) 一般情形 verifier-only
最优覆盖 = g_V·Σ_{j≤2}q_j，残余缺口 = g_V(1−Σ_{j≤2}q_j)；(iii) 空接受集 A_d=∅ 给出"深度≤d 的
DSL 类不可行"证书，由此得到验证算力的水填充/阈值分配规则；(iv) 与 T7 对比：verifier 天花板
Σg_t 只有在 g_{V,t}=g_t 且 q1+q2=1 时可达到——**标签免费（演示对），覆盖不免费**。另冻结混合
提交公式与"verifier-first 优于 TTT-first"的充要条件 E[1{unique}(φ−p_w2)]>0。

**验证器实验（诚实负结果）**：
- 有界 DSL 搜索（深度≤2 + 参数扫描，LegC DSL 53 函数，56 核）：**eval120 认证 0/120**（120/120
  不可能性证书；334.7 CPU-min）；训练集小样本 12 任务正对照 **1/12 唯一解**（0520fde7）。
- 学习型规则族（颜色映射/3×3 CA/周期/裁剪/缩放/常数）：**0/120**。
- LLM 提议（DeepSeek-chat k=4，20 任务）：**0/20**；DeepSeek-reasoner 因 token 截断为基础设施
  空结果（如实记录）。结论：AGI-2 上"验证器诱导可识别性"在可负担假设类下无法兑现，瓶颈是
  候选生成（与 T6/T7 一致）。

**云算力大规模数值验证（12 GB TITAN Xp + 56 核）**：
- T6 信息上界：**1 亿随机实例**，1e-6 容差下 **0 违反**（最大超出 1.12e-7 = float64 舍入；
  非空泛比例 34.9%；紧度 0.164；28.3 s）。
- T7 分配分离：**200 万任务**，label-free 天花板 0.739684 vs verifier 天花板 1.000，**差距
  0.260316 = 平均 δ（1e-12 精度，预算不变）**；water-filling 在每个预算档均优于 uniform（20.1 s）。
- 环境与命令已写入论文 §5.4；脚本以 MIT-0 发布于 arc-selection `lab/`（commit `f371ba7`）。

**产物**：paper v6 md sha `7ab170f3…`（8,109 词、42 refs、12 figs、24 页 PDF `b5b962b2…`）、
arXiv main.tex `af08a0ab…`、writeup v6（1,476 词，仅 S5b 待填）、fig9 验证器可识别性图；
paper-repo 暂存 commits `93ac381`+`a4246c1`（tag v2.2，待推送）；arc-selection 已推送 lab 模块。
