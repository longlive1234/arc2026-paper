# Evidence table — claims ↔ evidence ↔ status

Companion to `paper/writeup_draft_v1.md` (de-tagged working text, 1466 words) and
`paper/writeup_kaggle_upload.md` (Kaggle upload text, 1473 words). The evidence tags that were inline in
`paper/writeup_draft_v1_tagged.md` (archived 2026-10-18) are collected here; the main text now reads
naturally and keeps only numeric placeholders (`XX.X%`, `XX/120`, `+XX.X points`, `TBD`) where a number
must be filled by a real run.

**Status vocabulary:** `MEASURED` = produced by an artifact on disk (registry row or repo file);
`CONTEXT` = dated external anchor (source + date, not our measurement); `ANALYTIC` = proved/derived in
a design note; `PRE-REGISTERED` = frozen protocol value; `PLANNED` = planned experiment; `PLACEHOLDER`
= no artifact yet (blocked or pending). Registry rows are `research/design/experiment_registry.md`
(`C#` A.1, `X#` A.2, `K#` A.3; `B#` A.5 blocked/pending).

---

## 1. Claims made in the draft

| # | draft location | claim | evidence | status |
|---|---|---|---|---|
| E1 | Abstract, Context | ARC-AGI-2 is a two-attempt, offline, ~12 h Kaggle code competition; two attempts per test input; open-source required | `PROJECT_SPEC.md` v2 §0 (C1); `research/lit/report.md` §2 (Kaggle API, 2026-10-18) | CONTEXT |
| E2 | Context | Public notebooks display 29.7–31.4 | X3 (Kaggle code pages rendered 2026-10-18; `research/lit/verified_solutions.md` §1) | CONTEXT (secondary rendering) |
| E3 | Context | Title-claimed 33.89 is not a displayed score | X4; `research/lit/verified_solutions.md` §1/§4 | CONTEXT |
| E4 | Context | ≈37.4 gold line | X6; `research/lit/report.md` §7 | CONTEXT — **unverified** |
| E5 | Context | 35–50 planning band | `research/design/theory.md` §0; this is a plan, not a result | PLANNED (not a number to fill) |
| E6 | Context | Reruns span 26.9–32.2 displayed | X5; `luxluxshan` notebook markdown quoted in `research/lit/improvements.md` §1 | CONTEXT (secondary, self-reported) |
| E7 | Context | CPU-fallback local solve rates: 10/400 holdout, 0/120 public eval | `code/README.md` §4 (safety-net submission, measured CPU) | MEASURED (CPU) |
| E8 | Context | CPU-fallback public LB score `XX.X%` | B4 (`wen134/arc2026-cpu-fallback`, packet built, dry-run submission 350,047 B, registry K7) | PLACEHOLDER — pending owner verification/join |
| E9 | Approach | Model is Qwen3-4B ARC-SFT, 7.27 GB bf16 | C3 (`logs/env_facts.md` probe5; 7,267,233,496 B) | MEASURED |
| E10 | Approach | Pipeline constants: 128 training sequences, 16 decode views, 8 rescoring views, LoRA r=256/lr 5e-5/1 epoch, threshold NLL < −ln 0.2, 540 s cap, 4 workers | `research/lit/adaptation_handbook.md` §2; `code/README.md` §5; implemented in `code/arc/run.py`, `decode.py`, `ttt.py` | MEASURED (recipe reproduced in code; **register `adaptation_handbook.md`/`code/README.md` in A.4**) |
| E11 | Approach | One notebook, MIT-0, no internet or API calls at re-run | `code/README.md` §1/§6; kernel metadata `enable_internet: false` in `notebook/ttt_packet/` and `notebook/cpu_fallback/` | MEASURED |
| E12 | Theory | TTT as amortized Bayesian adaptation; PAC-Bayes sketch; κ_T proxy | `research/design/theory.md` §2; `calibration_protocol.md` §2.2b | ANALYTIC (sketch) |
| E13 | Theory | Coverage objective U(a1,a2)=1−P(¬C(a1)∧¬C(a2)) | `research/design/theory.md` §1/§4.1 | ANALYTIC |
| E14 | Theory | The theorem (independent-case top-2; duplicate dominance; argmax-once suboptimal under correlation; U formula) | `research/design/theory.md` §4 Theorems 1–3 + Prop. 4; reference implementation `research/design/select_calibrated.py` (self-tested) | ANALYTIC |
| E15 | Theory | Calibration on 600 dev / one-shot 400 holdout; Brier/slope gate; frozen artifact | `research/design/calibration_protocol.md` §2–§4 | PRE-REGISTERED |
| E16 | Progress | Zero shared tasks, pairs and input grids (SHA-256 audit) | `analysis/report.md` §12 (C9 artifact) | MEASURED (CPU) |
| E17 | Progress | `max_dim` 21.95 vs 14.67, p<0.001; 64% of eval tasks in hardest train quartile | `analysis/report.md` §11 (permutation tests, 5,000 perms, seed 0) | MEASURED (CPU) |
| E18 | Progress | Eight single-rule heuristics: 1.6% train, 1.5% holdout, 0% public eval | `analysis/report.md` §13 | MEASURED (CPU) |
| E19 | Progress | TTT-solvability prior: 28/56/36 tasks (A/B/C); 76% of TTT time on tier B | `analysis/report.md` §15–16; `analysis/compute_allocation.md` §3/§4 (prior-v1, `allocation.json`) | MEASURED (CPU) — **uncalibrated prior, not a solve rate** (stated in text) |
| E20 | Progress | Pre-registered decision rule: ≥1.0 official point, 80% paired-bootstrap CI lower >0, 2,000 resamples, dev-fit only | `research/design/calibration_protocol.md` §4; `risk_register.md` P0 | PRE-REGISTERED |
| E21 | Progress | Planned ablations A0–A10; predictions R1–R10 | `research/design/v1_plan.md` §Ablation matrix; `theory.md` §8 | PLANNED |
| E22 | Results | Best displayed open-notebook score 31.4 | X3 | CONTEXT |
| E23 | Results | Our TTT pipeline, public LB `XX.X%` | B3 (eval-120 final checkpoint) / B4 (competition submission) | PLACEHOLDER |
| E24 | Results | Our pipeline, local eval-120 `XX/120` | B3; command `code/run_eval_local.py --submission <json> --split eval` | PLACEHOLDER |
| E25 | Results | coverage_optimal − argmax_argmax on holdout `+XX.X points` | B2; output fields `verdict.point_points` / `verdict.claim` from `replay_policies.py` | PLACEHOLDER |
| E26 | Results | CPU-fallback submission, public LB `XX.X%` | B4 / K7 | PLACEHOLDER |
| E27 | Results | Kaggle submission ID `TBD` | B4 | PLACEHOLDER |
| E28 | Completeness | Open source MIT-0 code, tests, notebook builder, pool schema, selection protocol, analysis scripts | `code/README.md` §1/§8; `research/design/pool_schema.md`; `analysis/` | MEASURED (CPU artifacts) |
| E29 | Completeness | Public notebook link `TBD`; submission ID `TBD` | B4; notebook must be published only after submission ID recorded (PROJECT_SPEC §4) | PLACEHOLDER |
| E30 | Completeness | All checkpoints reported; provenance per run | `risk_register.md` R7/R8; `code/README.md` §2.4b (provenance env vars) | PLANNED (reporting protocol) |
| E31 | Universality | Selection rule applies to any K-attempt exact-match task with calibrated pools; admissibility conditions | `research/design/theory.md` §7; `calibration_protocol.md` §3 | ANALYTIC + PRE-REGISTERED |
| E32 | Universality | 2B–14B model sweep planned | `research/design/v1_plan.md` A1; `research/lit/model_inventory.md` | PLANNED |
| E33 | Limitations | Platform block: GPU requests run CPU-only; account not phone-verified/joined | K1–K5 (`logs/kaggle_runs.md`, `logs/env_facts.md`, registry B7) | MEASURED (platform evidence) |

---

## 2. Numeric placeholders and how to fill them (mechanical)

| placeholder | replace with | source of value | command / artifact |
|---|---|---|---|
| `XX.X%` (TTT public LB) | measured Kaggle LB to 1 decimal | Lead-recorded submission | `logs/kaggle_runs.md` row + submission ID |
| `XX/120` (local eval-120) | solved count out of 120 | frozen final checkpoint only, all checkpoints reported | `code/run_eval_local.py --submission … --split eval` → `logs/local_eval/<run>.json` |
| `+XX.X points` (holdout selection gain) | `verdict.point_points` (never recomputed by hand) | frozen calibrator + one-shot holdout replay | `replay_policies.py … --out logs/arch-theorist/selection_replay_<run>.json`; also paste `verdict.claim`, `verdict.deployed_rule`, `verdict.ci80_lower_bound_points` |
| `XX.X%` (CPU-fallback LB) | measured LB of the CPU-safe submission | Lead-recorded | B4/K7 |
| `TBD` (notebook link) | public Kaggle notebook URL | after submission ID recorded | PROJECT_SPEC §4 policy |
| `TBD` (submission ID) | Kaggle submission id string | Lead-recorded | `logs/kaggle_runs.md` |

**Rule:** if a run does not happen, do **not** fill; keep "not measured — platform-blocked" (Plan B
wording, `research/design/planB_paper.md`) and activate the Plan B framing. No estimated or
extrapolated numbers may be inserted.

---

## 3. Evidence/registry gaps to fix before the Nov 6 freeze

1. `code/README.md` and `research/lit/adaptation_handbook.md` are cited (E7/E10/E11/E28) but are not
   rows in `experiment_registry.md` A.4 — add artifact rows.
2. `analysis/figures/*.png` are used in the writeup/gallery but are not registered — add rows (with
   sha256) for figs 1–11.
3. The competition-format fact (E1) is currently covered by C1 (repo SPEC v2) rather than a primary
   source row — add a context row with URL + access date.
4. Every `CONTEXT` row cited must be frozen with URL + date on Nov 6 (`frozen_at` bump); X1 (leader
   scores) is no longer used in the draft and need not be frozen for this paper.
5. After tags were stripped, re-run the word-count audit (draft 1466 raw / Kaggle 1473 raw) on the
   final text; convert any remaining `XX` placeholders and recount.

---

# Plan C public paper — evidence rows (draft v1, 2026-10-18)

Companion to `paper/paper_planC_draft_v1.md` (main text 4,994 words) and
`paper/paper_planC_outline.md`. Provenance tags: `[OURS]` CPU-only measurement by us; `[TP]` our
analysis of third-party released artifacts (no model of ours runs); `[SIM]` simulated; `[CTX]` dated
external context. The `[DA]`/`[PEND]`/`[PRELIM]` labels below are historical registry states: all canonical results are now in C38–C49 and no open placeholder remains.

| # | claim | evidence | status |
|---|---|---|---|
| C1 | B = `vanductan/arc-agi-2-candidate-dump`; displayed LB 30.97; 347 candidate files; 20 tasks / 29 inputs | `analysis/results/pool_inventory.json`; `analysis/third_party_outputs/vanductan/`; protocol v2 §1 | `[TP]` provenance (displayed score `[CTX]`, secondary) |
| C2 | B is the only public candidate-dump notebook found; N fixed at 20/29 | Lead search 2026-10-18 + `analysis/pool_inventory.json` | `[OURS]` search result |
| C3 | B reproduction gate: 29 units, oracle-any-2 9/29 = 31.0%, top-2 8/29 = 27.6%, 0 per-input mismatches | `logs/arch-theorist/external_reproduction_gate_arc2_dump.json` | `[TP]` passed |
| C4 | B pilot (protocol v2, holdout 14 inputs): oracle 4/14 = 28.6%; argmax12 and all deployable rules 3/14 = 21.4%; duplicate rate 1.0 for duplicate rule; oracle gap +7.14 pts; verdict `PILOT_NO_CLAIM` | `logs/arch-theorist/external_s1.md`/`.json` | `[TP]` pilot, not claim-bearing |
| C5 | B dev calibration: Brier 0.053, reliability slope 0.081 (gate fails) | `external_s1.json` diagnostics | `[TP]` |
| C6 | B dev ρ: same_view −0.167 (n=48), same_model −0.107 (n=1531), cross_model pooled −0.109 (n=0) | `external_s1.json` `rho`/`rho_source` | `[TP]` |
| C7 | B full-sample non-pre-registered check: duplicate/top-2 8/29 = 27.6%; argmax1+2 7/29 = 24.1%; oracle 9/29 = 31.0%; task solved 25.0% | `code/docs/RESULTS.md` §3; `code/out/selection_bench_external_vanductan.json` | `[OURS]`/`[TP]`–both, label "not pre-registered" |
| C8 | A = CompressARC bundled `predictions_evaluation.npz` (MIT), ARC-AGI-1 eval, 400 tasks; fit 400 train; hash-level candidates | `data/CompressARC`; `code/compressarc_harness.py`; protocol v2 §1 | `[TP]` provenance |
| C9 | A reproduction: total solved 137/400; ≤2 guesses 80/400; matches upstream script | `code/docs/RESULTS.md` §2; `code/out/compressarc/verify_bundled_eval.json` | `[TP]` passed |
| C10 | A headroom: 137−80 = 57 tasks = +14.25 task-level points | derived from C9 by protocol v2 §4 | `[TP]` arithmetic |
| C11 | A rule table and per-rule CIs | frozen benchmark artifact `analysis/results/selection_benchmark.json`; **preliminary null in C31** | superseded by canonical C38–C49 |
| C12 | C simulated pools: generators, rules, seeds, estimator sanity | data-analyst simulated sweep | superseded by canonical C38–C49 (simulated) |
| C13 | Fig. 2 = rule comparison with CIs; Fig. 3 = pool diagnostics | `analysis/figures/fig12_selection_rules.png`, `fig13_pool_diagnostics.png` (data-analyst) | superseded by canonical C38–C49 |
| C14 | Public ARC-AGI-2 data: 1,000 train / 120 eval tasks; 3,232 / 359 pairs; 1,076 / 167 test inputs | `analysis/report.md` §1–2 | `[OURS]` |
| C15 | Leakage audit: 0 shared tasks / pairs / input grids between splits | `analysis/report.md` §12 | `[OURS]` |
| C16 | Trivial heuristics: 1.6% train, 1.5% holdout, 0% eval | `analysis/report.md` §13 | `[OURS]` |
| C17 | Eval shift: max dim 21.95 vs 14.67 (p<0.001); 64% of eval in hardest train quartile | `analysis/report.md` §10–11 | `[OURS]` |
| C18 | Taxonomy: 54.5% train / 57.5% eval same-size rewrites; object manipulation 12.2%/23.3%; grid panels 11.7%/12.5% | `analysis/report.md` §9 | `[OURS]` |
| C19 | Shape rule: 83.6% train / 69.2% eval | `analysis/report.md` §3/§13 | `[OURS]` |
| C20 | Solvability tiers 28/56/36; 76% of budget on tier B (uncalibrated prior) | `analysis/report.md` §15–16; `analysis/compute_allocation.md` | `[OURS]` prior, not a solve rate |
| C21 | CPU baselines (latest, docs/RESULTS.md): DSL 26/600 dev, 13/400 holdout, 0/120 eval; fallback 27/600, 14/400, 0/120 | `code/docs/RESULTS.md` §1 | `[OURS]` — **conflicts with older `code/README.md` §4 (9/400, 10/400); use docs/RESULTS.md and note the conflict** |
| C22 | System validation: 154 CPU tests; fallback packet 120 tasks/167 inputs in 8.3 s; hf_cpu TTT path; packets frozen | `code/docs/RESULTS.md` §4; `logs/kaggle_runs.md`; `logs/kaggle_freeze.md` | `[OURS]` |
| C23 | Platform gate: phone verification required to Join; 13 CPU-only runs; 0 GPU-hours; ticket submitted; packets frozen; resume path documented; local NVML failure | `logs/kaggle_freeze.md`, `logs/env_facts.md`, `logs/kaggle_runs.md`, `code/docs/RESULTS.md` hardware line | `[OURS]` |
| C24 | Public-solver landscape displayed scores 29.7–31.4; title claims 33.89/35.9 not displayed | `research/lit/verified_solutions.md` §1/§4 | `[CTX]` secondary rendering 2026-10-18 |
| C25 | Saved-artifact scores on public eval: anthonyxlyu 3, rabari9999 3, mayankraaz 4, woominyo 3, vanductan 8 per-input correct /167 → 1.8–4.8%; saved eval-mode outputs, not LB reruns | Lead-computed 2026-10-18; per-notebook artifact to be filed as `analysis/results/saved_artifact_scores.json` | `[OURS]` numbers supplied; **artifact pending** |
| C26 | CompressARC CPU feasibility: 26 s/step on smallest eval task; 1500 steps ≈ 10.8 h/task; 20-step subset ≈ 9 min | `code/docs/RESULTS.md` §2 | `[OURS]` |
| C27 | Licence: our code intended MIT-0; third-party licences retained (CompressARC MIT, ARC data Apache-2.0, notebooks attributed not relicensed); current `code/LICENSE` is MIT and must be switched to MIT-0 before release | Lead decision 2026-10-18; `code/LICENSE` | **repo fix pending** (owner: code maintainers) |
| C28 | Table 2 cells: filled mechanically from the frozen `selection_benchmark.json`; thresholds/rule order unchanged | C38–C42; protocol v2 §6 | complete |
| C29 | Own GPU TTT pools / own leaderboard score / hidden-test access: none exist | blocked rows B1–B3 in `research/design/experiment_registry.md`; `logs/kaggle_freeze.md` | not measured — platform-gated; never cited as results |

**Note on C21 conflict:** `code/README.md` §4 reports older CPU-baseline numbers (DSL 9/400, fallback
10/400) while the newer living document `code/docs/RESULTS.md` reports 13/400 and 14/400 after solver
improvements. The paper cites the newer document and labels the numbers as the current CPU baseline;
the README should be updated at freeze.

---

# Plan C revision R1 — negative-result evidence rows (2026-10-18, preliminary)

Added when the paper's framing changed to a bounded negative result. `[PRELIM]` values are
Lead-reported and will be superseded by the frozen benchmark artifact; final values replace them
mechanically (see C35). The theorem and protocol are unchanged.

| # | claim | evidence | status |
|---|---|---|---|
| C30 | Dataset A ceiling vs solver ranking: oracle-any-2 137/400 = 34.25%; solver top-2 80/400 = 20.00%; headroom 57 tasks = +14.25 task-level points | derived from C9 + protocol v2 §4 | `[TP]` |
| C31 | Dataset A **null re-ranking result (preliminary)**: candidate correctness AUC 0.981 but score-dominated; on a held-out half the two-attempt conversion is 18.4% → 19.9% (inside the noise band) and calibrated feature-based re-ranking recovers no additional coverage over the solver's own ranking | superseded by the canonical rule table in C39 (final CIs from the frozen artifact) | superseded |
| C32 | Dataset A claim status: no positive selection claim; negative result reported under protocol v2 §6 (Δ ≥ +1.0 pt AND 80% CI lower > 0 not met) | protocol v2 §6; C31 | `[TP]` (verdict will be pasted from artifact `verdict.claim`) |
| C33 | Dataset B has one input of headroom, not a measurable effect: holdout oracle 4/14 vs top-2 3/14; full-sample oracle 9/29 vs 8/29; calibration gate fails (Brier 0.053, slope 0.081) | `logs/arch-theorist/external_s1.md`; C4–C6 | `[TP]` |
| C34 | Interpretation: selection is not the bottleneck; candidate coverage/generation is. Falsification conditions: (F1) calibrated rule beats solver ranking by ≥+1.0 pt with 80% CI>0 on a claim-bearing pool; (F2) metadata beyond source score exposes oracle-gap candidates (e.g. cross-model agreement with low ρ); (F3) multi-decoder/ensemble union whose second-attempt marginal coverage exceeds the noise band | paper §4.4; theory §4; protocol v2 §6 | ANALYTIC / testable |
| C35 | Table 2 fill + acceptance procedure: run `python analysis/selection_benchmark.py`; read `analysis/results/selection_benchmark.json` (`rules.*.pass2`, `deltas_vs_*.point/ci80/ci95`, `verdict.claim`, `deployed_rule`, `rho`, calibration diagnostics); replace every `XX` cell mechanically; confirm no threshold/rule-order drift; paste verdict strings verbatim | `analysis/selection_benchmark.py` docstring; protocol v2 §6/§9 | superseded by canonical C38–C49 |
| C36 | Title/framing revision R1: recommended title "Two Guesses, Not Two Chances: Coverage-Optimal Selection and Its Empirical Limits in ARC-AGI-2 Solver Pools"; subtitle "Theory, a pre-registered benchmark on real solver candidate pools, and a measured negative result" | `paper/planC_title_candidates.md` (SELECTED block) | final |
| C37 | Paper headline must not imply a selection gain: abstract/intro/conclusion lead with the measured null, with the theorem as formalization and the oracle gap as the bound | draft R1 §Abstract/§1/§4.4/§9 | `[OURS]` writing decision (Lead 2026-10-18) |

---

# Plan C — CANONICAL FINAL SYNC (2026-10-18, supersedes C4/C7/C11/C30–C37 where they differ)

Source of record: `analysis/results/SELECTION_RESULTS.md`, regenerated from the frozen artifact
`analysis/results/selection_benchmark.json` sha256
`6c16abfef7f0efe3a1a6bbe9f6251c9aeef1893ee7b0f44fdfdb9c2eb34ab71a` by
`python analysis/selection_benchmark.py`. These are the values in `paper_planC_draft_v2.md` Table 2.
Every cell below was verified against SELECTION_RESULTS.md; no reconciliation footnote remains in the
paper.

| # | claim | evidence | status |
|---|---|---|---|
| C38 | Frozen artifact identity: `selection_benchmark.json` sha256 `6c16abfef7f0efe3a1a6bbe9f6251c9aeef1893ee7b0f44fdfdb9c2eb34ab71a`; canonical report `analysis/results/SELECTION_RESULTS.md`; regenerate with `python analysis/selection_benchmark.py` | files above | measured (artifact hash verified locally) |
| C39 | **A (CompressARC, 400 tasks, unit=task):** oracle 34.25% [31.25,37.50] (95% [29.75,39.00]); duplicate 18.50 [16.00,21.00]; argmax1_argmax2 19.50 [17.00,22.00]; top2_consensus 20.00 [17.50,22.75]; cal_indep 18.00 [15.50,20.75]; coverage_optimal 17.75 [15.25,20.25]; deployed 19.25 [16.75,21.75]; gate FAIL; headroom 57 tasks = 14.25 pp; margin coverage−argmax −1.75 pp; verdict `DOWNGRADE_TO_ANALYSIS` | SELECTION_RESULTS.md §Dataset A; selection_benchmark.json | measured (third-party pools) |
| C40 | A score-sufficiency evidence: missed truths have score-rank median 12; only 24/57 are in the top 10, so no re-ranking of exposed metadata recovers them | SELECTION_RESULTS.md §Verdicts 1 | measured (third-party pools) |
| C41 | **B (pilot, 16 inputs / 11 tasks):** oracle 31.25% [18.75,43.75]; duplicate/argmax/top2/cal_indep/coverage_optimal all 31.25%; deployed 25.00 [12.50,37.50]; gate FAIL; measured headroom 0 on the eval fold (every oracle-covered input already covered by every score-based rule) | SELECTION_RESULTS.md §Dataset B | measured (third-party pools, pilot) |
| C42 | **C (simulated, 120 tasks):** oracle 41.67% [35.83,47.50]; duplicate 16.67 [12.50,20.83]; argmax1_argmax2 23.33 [18.33,28.33]; top2_consensus 21.67 [16.67,26.67]; cal_indep = coverage_optimal = deployed = 41.67 [35.83,47.50]; +18.34 pp over argmax (95% CI [11.7,25.0]); gate FAIL but claim threshold MET; simulated, not evidence about real solvers | SELECTION_RESULTS.md §Dataset C | measured (simulated) |
| C43 | B deployment note: deployed = 25.0% because the gate fails and the protocol fallback (highest agreement) is worse than the aggregation ranking on this tiny pool; C deployed now equals the calibrated rules after the simulated-generator fix (earlier 2.5% was a fixed generator artifact, not a deployed-policy bug) | SELECTION_RESULTS.md §Reconciliation notes | measured |
| C44 | Saved-artifact scores (canonical): task-score range 1.67–4.17%, input-accuracy range 1.74–4.65%; displayed-score range 29.72–31.39; per-notebook counts vanductan 8, mayankraaz 4, woominyo/anthonyxlyu/rabari9999 3; saved eval-mode outputs, not LB reruns | `analysis/results/saved_artifact_scores.json` | measured (our scoring of saved artifacts) |
| C45 | Exploratory cross-source note (appendix only): task-level 50/70 dev/holdout split; best dev source solves 1/70 on holdout; best-source attempt-1 + cross-source attempt-2 also 1/70; union oracle 8/70 → no cross-source conversion on partial artifacts | SELECTION_RESULTS.md §Exploratory cross-source | measured, exploratory (not pre-registered) |
| C46 | Novelty verdict: PARTIALLY-KNOWN; qualified 35-word sentence used verbatim in §1; citations: dalezhong notebook [23] (uses "coverage-aware set selection" + P4 structural distinctness), FlexRouter COLM 2026 [24], Singham 2026 [25]; objective is classical (submodular/DPP/conformal lineage), contribution is ARC instantiation + estimator + score-sufficiency criterion; no priority/"first"/"no prior work" wording | `research/lit/novelty_check.md`; paper §1 related-work paragraph; references 23–25 | analytic/positioning |
| C47 | Licence/attribution: our code MIT-0 (SPDX MIT-0; repo LICENSE still MIT text → repo-side fix before release); third-party verified licences: ARC-AGI-2 data Apache-2.0, model + Qwen3 base Apache-2.0, CompressARC & arc-dsl MIT, Unsloth/transformers/peft Apache-2.0; public notebooks unlicensed → prior art only, clean-room re-implemented, cited by URL; NOTICE + per-file comments | `research/lit/license_audit.md`; paper §6 | audited |
| C48 | Number-sync audit: no `XX`/`[DA]`/`[PEND]`/draft provenance tags or reconciliation daggers remain in the v2 body; all main-text numbers trace to C38–C44 or to `analysis/report.md`/`code/docs/RESULTS.md`/`logs/kaggle_freeze.md`; GPU run and own leaderboard score are explicitly "not measured — platform-gated" | `paper/paper_planC_draft_v2.md`; this table | audit (paper-writer, 2026-10-18) |

| C49 | **Final QC (v2 freeze):** all 25 references cited in the main text (programmatic check, multi-number brackets parsed; uncited = none); Table 5 test count was 154 ~10 s at the v2 freeze; **superseded**: hardened suite is **190 tests (~26 s)**, see C60 (repo `code/docs/REPRODUCE.md` should be reconciled by the release owner); table 2 values are exact two-decimal from the frozen JSON; frozen hash 6c16abfe…4ab71a in paper + evidence table; zero remaining `XX`/`[DA]`/`[PEND]`/provenance tags or reconciliation daggers | `paper/paper_planC_draft_v2.md`; `paper/evidence_table.md`; `analysis/results/SELECTION_RESULTS.md`; `pytest tests -q` | audit (paper-writer, 2026-10-18) |

---

# v3 revision (2026-10-20) — freeze patch P1–P6 applied

**v2 archived unchanged:** `paper_planC_draft_v2.md`, sha256
`6ae661c55cd69574a384e18b209966507c0756ee20174df5c4f095de0d86ccb6`.
**v3:** `paper_planC_draft_v3.md`, sha256
`00435c14d832eb756d536feec680d1ac85f0488bf06cd1450c40dae2e3d29972`, main text 4,997 words,
all 30 references cited, zero placeholders. PDF rebuild: 16 pages, sha256
`cacc194d02cf6f3f465cb0adbd922f7367b218d015f2d7dd0b384435e250ca26` (Typst deterministic build, warnings none).

| # | claim | evidence | status |
|---|---|---|---|
| C50 | v3 applies the approved freeze patch: corrected novelty paragraph with [17, 23] MDL/structural credit, [26] arc-budget ("comparable pattern", "no better than" deployed vote rule, empirical instrumentation not a coverage model, headroom observation credited), [27] pass@k diagnostic (selection ≈95% of ceiling → generation-bound, correct direction), [28] identifiability gap at the score-sufficiency claim, [29] classical-lineage citation, [30] markbarney minority recoveries; [23] theory-note caveat; refs [26]–[30] with verified metadata; no priority wording | `paper/paper_planC_draft_v3.md` §1; refs 17, 23, 26–30; `research/design/paper_writer_handoff.md` §4b–4c | applied (Lead-approved 2026-10-20) |
| C51 | Official competition data: 120 tasks / **358 pairs / 172 inputs** (`data/comp/arc-agi_evaluation_{challenges,solutions}.json`); repo mirror 167 inputs (5 tasks differ, 4 with an extra prepended input, `faa9f03d` train-pair difference, `d8e07eb2` train-pair output difference); SHA-256 leakage audit on official files = 0 shared tasks / 0 pairs / 0 input grids; local `arc-agi_test_challenges.json` = 240 tasks/259 inputs, exact public-training duplicate (dev sandbox only); rerun budget 12.0 min/task, 11.1 min/input | `analysis/official_data_notes.md`; `analysis/official_scoring.py --recompute-all`; `paper/paper_planC_draft_v3.md` §5/§6/§7, Appendix F | measured (official files, 2026-10-20) |
| C52 | Official-eval landscape scores of saved artifacts: vanductan 5/120 tasks (4.17%) / 8/172 inputs (4.65%), efthimiosfousekis & yuvrajlamba 4/120, mayankraaz & yukailiu 3/120, anthonyxlyu/rabari9999/woominyo 2/120 → task-level range 1.67–4.17% (input-level 1.74–4.65%) vs displayed 29.72–31.39; our CPU fallback 0/120 tasks (0/172 inputs). **Runtime update (C56/C60):** official 172-input repackaging measured **5.41 s median locally**; the paper's **8.3 s was the 167-input repo packet on Kaggle**, now stated with that provenance | `analysis/results/official_scores.json`; `analysis/official_data_notes.md` §4–5 | measured (saved partial eval-mode artifacts, not LB reruns) |
| C53 | Dataset B official-truth check — **confirmed**: official-truth rerun `analysis/results/selection_benchmark_official.json` (sha256 `cb8308448f78ed5064a8f13827ef9117908184cf5b6354f591cffa1951552df0`, `python analysis/selection_benchmark.py --truth-mode official`) gives B split identical (fit 9 tasks/13 inputs; eval 11/16), oracle 31.25%, duplicate/argmax1_argmax2/top2_consensus/cal_indep/coverage_optimal all 31.25%, deployed 25.00%, all Δ=0, calibration identical; A/C identical to the frozen artifact (`6c16abfe…4ab71a`) → **Table 2 unchanged**. `abc82100_0`: 11 candidates, 0 correct under either label (repo truth = official index 1, oracle-false both; unit in fit fold; every candidate flag 0 → fitted calibrator unchanged). Independent check: `paper/official_b_truth_check.md` | rerun artifact + `paper/official_b_truth_check.md` | verified (data-analyst 2026-10-20; paper-writer cross-check) |
| C54 | v3 QC: main text 4,997 words (≤5,000); refs 1–30 all cited (programmatic bracket check); zero `XX`/`[DA]`/`[PEND]`/provenance tags/daggers; frozen benchmark hash unchanged; PDF 16 pages sha `cacc194d…ca26`; arxiv_source regenerated (main.tex, 30 refs, 8 figures, 6 tables) | `paper/paper_planC_draft_v3.md`; `paper/build/build_report.json`; `paper/arxiv_source/build_summary.json` | audit (paper-writer, 2026-10-20) |

| C55 | Official-truth benchmark rerun reproducibility: `analysis/results/selection_benchmark_official.json` sha256 `cb8308448f78ed5064a8f13827ef9117908184cf5b6354f591cffa1951552df0`, generated by `python analysis/selection_benchmark.py --truth-mode official`; `comparison_with_frozen` shows A/B/C rows unchanged from `selection_benchmark.json` (sha `6c16abfe…4ab71a`) | `analysis/results/selection_benchmark_official.json`; `analysis/official_data_notes.md` §4b | measured (official truth, 2026-10-20) |
| C56 | CPU fallback runtime (measured locally, i7-13700H, 20 threads, Python 3.12.4, incl. file writes; 3 runs): official 172-input repackaging 5.46/5.41/5.30 s (median 5.41), repo-shaped 167-input packet 5.39/5.52/5.42 s (median 5.42), both 0/120; official repackaging adds no measurable cost. The paper's 8.3 s figure is the earlier repo-shaped packet run on Kaggle and was not re-measured here; §6 text kept as-is (accurate, v3 frozen) | `analysis/official_data_notes.md` §4c; `paper/paper_planC_draft_v3.md` §6 | measured (local; Kaggle 8.3 s historical) |
| C57 | Official competition-file sha256: challenges `e7c62a4bd211867c6b538f66b8013b81f299663c82ca062f49a52bf439d6e4e8`; solutions `84be4f4f39b79e82c36d565fc878830988b094917f052ee7069aef30b33ca8f1` (test `232264c5…`; training `779eaba8…`; sample `6b372dce…`). 120 tasks / 358 pairs / 172 inputs confirmed | `analysis/official_data_notes.md` §1; `sha256sum data/comp/*.json` | measured (files verified locally) |

---

# v4 Theorem-5 patch (2026-10-21; Lead-approved, unpushed working copy)

| # | claim | evidence | status |
|---|---|---|---|
| C58 | Theorem 5 (budget-constrained coverage allocation) applied to v4: new §3.5 block (126 words) inserted after §3.4; estimator/TTT renumbered to §3.6/§3.7; §4.2 sentence (18 words) appended; Appendix G entry + Table 11 reserved, cross-source note renumbered to Appendix H; six §5.3/§8 trims matched exactly once and saved 153 words. Theory in `research/design/theory.md` §4.7; registry A.11; dev20 ladder EXPLORATORY/PENDING. Base v4 sha `68eabd59…`; backup `paper_planC_draft_v4_pre_theorem5.md` (same sha, untouched). Dry-run reproduced the projection (4,822 non-placeholder pre-fill / 16 markers / 30 refs / 8 figures) before the header note was added. | `paper/theorem5_patch.md`; `paper/apply_theorem5.py` (guarded applier, `--apply`); `paper/paper_planC_draft_v4.md`; theory §4.7; registry A.11 | applied (Lead-approved 2026-10-21) |
| C59 | Post-patch v4 state (superseded by C60 after audit fixes): sha256 `cfaa2bdf…`; 4,819 non-placeholder; 16 markers; 30/30 refs; 8/8 figures; fill 164 → 4,983. | `paper/qc_v4.py`; `paper/v4_fill_plan.md` | audit (paper-writer, 2026-10-21) |

| C60 | **v4 evidence-audit fixes applied (13 NEEDS-UPDATE items; paper only, unpushed).** New v4 sha256 `7c0887fae5e348b31c5f44676846d1a724ac341ef3dbd02f0c83ba2fa08480a9`; raw 4,971 / **non-placeholder 4,828**; fill 164 → **4,992**; 16 markers; 30/30 refs; 8/8 figures; no forbidden tokens. Fixes: removed unartifacted AUC 0.981; 154→**190 tests (~26 s)** (§7/Table 5); CPU-fallback provenance corrected (**repo 167-input Kaggle 8.3 s; official 172-input 5.4 s local, no Kaggle run**); calibration gate now states code range **[0.2,5.0]** (design target [0.7,1.3]); `run_all` **169 s**; Appendix-C breakdown **5 probes / 3 fallback / 5 TTT**; cap **578 s if 240 tasks (1156 s if 120)**; five-theorem wording in abstract/intro; C gain **+18.33 pp [11.67,25.0]**; ten-notebook/29.7–31.4 scope; v4 PDF marked "to be rebuilt at freeze". Writeup updated to sha `44a2096d…` (1,487 raw; 190 tests; 18.33; cap conditional; no medal-cutoff names). **LB snapshot is now frozen (C61–C62) and the v4/writeup LB statement is filled statically:** `analysis/results/leaderboard_snapshot_2026-10-20.json` (2026-10-20; rank-percentile points, e.g. top-10% = rank 309 at 31.81; no medal-cutoff names; our team absent). **AUC number deliberately kept out of the paper** per Lead (artifact 0.9688/0.9722 remains in C63); C gain +18.33 [11.67,25.0] confirmed (C64). Current v4 sha256 `ededae9bac8a166ef0706f8c6df0fb2a6c61c12c290e0b852c2b1d8325bc2b59`; raw 4,998 / non-placeholder **4,923**; 5 markers; remaining fill ≈70 → ≈4,993. (header nit fixed: first *submission attempt*, no 'valid'; abstract double period fixed) 16 markers; 30/30 refs; 8/8 figures. Writeup sha `13c227f3…f9c79` (1,481 raw).** v3 untouched (`00435c14…`). | `paper/evidence_audit_v4.md`; `paper/paper_planC_draft_v4.md`; `paper/writeup_kaggle_v4.md`; `paper/qc_v4.py` | applied (paper-writer, 2026-10-21) |

## 4. Audit-resolution rows (paper v4 numeric-evidence audit, 2026-10-21)

| # | claim | evidence | status |
|---|---|---|---|
| C61 | **LB snapshot frozen as a canonical artifact set.** CSV `analysis/results/leaderboard_snapshot_2026-10-20.csv` sha256 `f48304f7320abe561f735ceb454f469d35f3b4df911b48e772700b5eb8a17ac6` (source API file `arc-prize-2026-arc-agi-2-publicleaderboard-2026-10-20T15:14:42.csv`; Lead reference name `...15_09_23.csv`); JSON `analysis/results/leaderboard_snapshot_2026-10-20.json` sha256 `c7a5d093a18a960142ab7ad2ba0b4735e24dd2d9d18a2518a75f16823d2271f8` (authoritative: schema/download/command/sha/convention); MD `...md` sha256 `e635bc2331a3dcadcedd5a12c3a39d9705ad5f82751f3f505f9771de98485365` regenerated from the JSON. Command: `$KAGGLE competitions leaderboard -c arc-prize-2026-arc-agi-2 --download -p /tmp/lb` → `python analysis/leaderboard_snapshot.py`. | measured/context (cryptographic freeze; no model run) |
| C62 | **LB snapshot canonical values (rank-percentile reference points, NOT medal cutoffs).** Rows = 3,091 (n_ranked=3,090 + 1 rank-0/unranked row); leader = rank 1, Tufa Labs, 88.06. Anchors use ranked teams only: `rank = max(1, floor(pct/100 × 3,090))` → top1% rank 30 = 52.50; top2% rank 61 = 37.78; top5% rank 154 = 32.64; top10% rank 309 = 31.81; top20% rank 618 = 30.97; top30% rank 927 = 30.56. Medal cutoff names are explicitly NOT asserted; our team is absent (no scored submission; 57456856 errored pre-compute). | `analysis/results/leaderboard_snapshot_2026-10-20.json`/`.md`; `paper/evidence_audit_v4.md` §12 | measured/context (dated snapshot) |
| C63 | **AUC resolution.** `analysis/results/candidate_auc.json` sha256 `1522ab198935d4d11122beaea3815b285a1685d50fcff3b3813fdc6e716419f4`: CompressARC eval candidate-level AUC = **0.9688** (source merged score) / **0.9722** (frozen calibrated p̂); train 0.9659 / 0.9651 (eval n=776,954 candidates, 137 positives). The unsupported paper value 0.981 is not reproducible from frozen artifacts; v4 now says "correctness is predictable but score-dominated" with no AUC number. Command: `python analysis/candidate_auc.py`. | measured (recomputed artifact) |
| C64 | **C-rule gain resolution.** Frozen artifact delta vs argmax = **0.1833 = +18.33 pp**, 95% CI `[0.1167,0.25]` = `[11.67,25.00]` pp. The former +18.34 was two-decimal display rounding of 41.67−23.33; canonical scalar is 18.33. Paper v4 + writeup now quote +18.33 pp (95% CI [11.67,25.0]) — verified. | `analysis/results/selection_benchmark.json` sha `6c16abfe…`; `analysis/results/audit_resolutions.json` sha `9a72dc9314123e87617751adf43fefff2eacd9507af39fd2942bd3a953711dfa` | verified (artifact-correct) |

| C65 | **Dev20 sweep results entered (Table 8) and submission ledger updated (Table 9).** eval20 = 20 tasks / 32 inputs, L4×4, hardened packets: S1 **4/20 tasks (20.0%) / 6/32 inputs (18.8%)**, decode mean ≈235 s/task, 4 tasks capped; S2 aug16 **2/20 (10.0%) / 5/32 (15.6%)**, decode up to 618 s with truncation; S5 single **3/20 (15.0%) / 5/32 (15.6%)**; S6 same-model dual-config A-round **4/20**, A∪B attempt-union **5/20 (25%)**, candidate-union 5/20; cross-config candidate union **6/20 (30.0%)**. §4.3 sentence: single 20-task subset, no CI claim, config diversity dominates selection gains. Table 9: **57500870** (2026-10-22T00:00:23Z, kernel v3 hardened S1, CPU-created probe) COMPLETE, **publicScore 0.00** (only scored entry); **57663405** (2026-10-26T10:45Z, kernel v8 hardened S1 L4, packet `9060264c…`) PENDING >13 h; **57681632** (2026-10-27T00:00:28Z, kernel v16 competition S5 L4, packet `6211b694…`) PENDING. Hidden-set size remains unknown; pending rerun times are queue time, not a size signal. | `logs/kaggle_submissions.md` (dev20 table + submission entries), `paper/paper_planC_draft_v4.md` §4.3/Table 8/Table 9 | measured (dev20, L4×4) / pending (L4 submissions) |
| C66 | **Formal dev20 Table-8 recomputation from pool-v1 files (official labels).** `analysis/results/table8_dev20.json` sha256 `fc5335162c090d17a6db0f7d6380b2fcfee584190006eeb8e1e3c30ec97c670e`; `table8_dev20.md` sha256 `e0c8e3abd8e09987b082e4344b20a5f2cf387b4f65ffcef4cc4574a555fe19d8`; filled table `table8_filled.md` sha256 `596de09360aa2d739f70a4a0d704e758d243ba3e39b0f5908be8e444d6958504`; command `python analysis/dev20_table8.py`. S1 355.94 s/task, 66.1% decode, 4/20 pass@2, 4/20 oracle; S2 441.87 s, 72.7%, 2/20, 4/20; S5 491.54 s, 59.2%, 3/20, 5/20; S6 316.37 s, 64.3%, 2/20 (**selection-bug-affected: pass@2 flagged**; candidates/labels usable), 4/20 oracle; S5_ens (53-task superset) 174.14 s, 72.1%, 11/53, 15/53 oracle. Four-config union (S1/S2/S5/S6) = **5/20 (25%)** under candidate/attempt/union-of-sets definitions; all-five candidate union = **6/20 (30%)**, adding `28a6681f` via S5_ens (attempt union stays 5/20); official vs repo labels give identical per-config pass@2. **S6 source gap:** the paper's A-round 4/20 / A∪B 5/20 is not reproducible from the provided S6 v13 pool (which gives 2/20, selection-bug-affected) and needs its own source; do not present 4/20 without it. | `analysis/results/table8_dev20.json`; `analysis/results/table8_dev20.md`; `analysis/results/table8_filled.md` | measured (official labels, independent recomputation) |

| C66 | **Table 8 canonical recomputation (formal, from pool-v1 files):** `analysis/results/table8_dev20.json` sha256 `fc5335162c090d17a6db0f7d6380b2fcfee584190006eeb8e1e3c30ec97c670e`; `table8_dev20.md` sha `e0c8e3ab…`; `table8_filled.md` sha `596de093…`; command `python analysis/dev20_table8.py`; labels = official eval solutions (`84be4f4f…`). S1/S2/S5 task/input pass@2 and decode/wall match the paper exactly. **Corrections applied:** S6 v13 measures **2/20 pass@2** (selection-bug-affected; 4/20 oracle, candidates/labels usable) — the unreproducible "A-round 4/20, A∪B 5/20" was removed; **all-config candidate union = 6/20 (30%)** only including S5_ens overlap (adds `28a6681f`), while the four-config S1/S2/S5/S6 union is **5/20 (25%)** (attempt-union and oracle-set union also 5/20). S5_ens 53-task superset: 11/53 pass (20.75%), 15/53 oracle (28.3%), 174.14 s/task, 72.1% decode. | `analysis/results/table8_dev20.json`/`_filled.md`; `analysis/dev20_table8.py` | measured (formal recomputation) |
| C67 | **First scored hidden submission:** ref **57663405** (kernel v8, hardened S1 L4, packet `9060264c…`; submitted 2026-10-26T10:45:00Z; S1 TTT aug8, 64 train rows/64 steps, beam 4; 41,400 s budget; 4×L4). Status **COMPLETE, publicScore 14.17**, no errorDescription, ≈14 h incl. queue. Honest framing: half-cost S1 truncated at 578 s/task cap, far below the public-notebook band (~30), not a SOTA claim; same pipeline reaches 20.0% task-level on the dev20 public-eval subset (Table 8), a ≈5.8-point hidden/public-eval gap. 57500870 (CPU probe) = 0.00; 57681632 (S5 L4) pending. Paper/writeup updated (abstract, §4.1, Table 5, Table 9, §9). Current v4 sha256 `ca19455125d782f246fa360bf5436aeabcfb4509a0eb9ace8df3813f3380938d`; raw 5,004 / non-placeholder **4,971**; 4 markers; refs 30/30; figures 8/8; remaining fill 26 → **4,997**. | `logs/kaggle_submissions.md`; `analysis/results/submission_scratch/` / Kaggle API; `paper/paper_planC_draft_v4.md`; `paper/qc_v4.py` | measured (scored LB) |

| C68 | **New best hidden score (supersedes C67 staging):** ref **57681632** (kernel v16 = competition **S5** L4, packet `6211b694…`; submitted 2026-10-27T00:00:28Z) = **COMPLETE, publicScore 16.25**, no error. S1 ref 57663405 remains listed as first scored attempt at **14.17**; S5 adds **+2.08 pp** on the hidden half. Honest framing kept: both far below the public-notebook band (~30); half-cost configs truncated at the 578 s cap; no SOTA claim; hidden-set size still unknown. Abstract, §4.1, Table 5 (best-scored row), Table 9 (S5 = current best; Oct-28 S6 dual-config row pending with a marker), §9 (S1/S5 vs dev20 20.0% gaps ≈5.8/≈3.75), Appendix C updated; writeup updated to sha `f76c6a458a73554139630a344be281722f735fbb253cbac31317323400a1a6d5` (1,496 raw; 3 bare-URL markers). Current v4 sha `ca194551…938d`; 4,971 non-placeholder; 4 markers; fills 26 → 4,997. | `logs/kaggle_submissions.md`; Kaggle API; `paper/paper_planC_draft_v4.md`; `paper/qc_v4.py` | measured (scored LB) |

| C69 | **FINAL SCOREBOARD (all public LB, hidden half) and freeze state.** Scored: **57681632** (S5 v16 L4) **16.25 — champion**; **57716141** (S6 dual-config v22) **15.42**; **57752011** (S5_ens two-model v23) **15.42**; **57663405** (S1 v8) **14.17**; **57785740** (S5+LegC v25) **14.17** — LegC net-negative (−2.08 vs S5); **57500870** (CPU probe) **0.00**. Errors/misses: 57442788 invalid format; 57456856 rerun budget-parse error; Oct-31 submission missed. Pending: **57854697** (S5b v24, Nov-1 00:10:23Z). No score exceeds 16.25; reference public-notebook replication 3/20 on dev20 (below S1 4/20); ~30 notebook band external context only. Compute quota exhausted Oct31–Nov1. Current v4 sha `991982aa68fa88b7e41445adc604bb479ec749a49e0e3187346821c5c86e3340`: raw 4,996 / non-placeholder **4,976**; **2 markers** (Fig. 8, S5b score); fills 19 → **4,995**; refs 30/30; figures 8/8. Writeup sha `f107e064c77f888655daa3d86affae7d0a82fb7d4104ada21dcb97efe03696a2`: 1,481 raw, 4 markers (S5b + 3 URLs). | `logs/kaggle_submissions.md`; Kaggle API; `paper/paper_planC_draft_v4.md`; `paper/writeup_kaggle_v4.md` | measured (scored LB) / pending |

| C70 | **v5 theory + real-data package (final, 2026-10-31).** Theorem 6 (proven label-free bound `E[U] ≤ p1+p2+min{T,sqrt(I(C;Z)/2)}`; Prop. 6e non-vacuity iff `I<2T²`; Cor. 6g negative result for full-metadata Pinsker bounds; Prop. 6f score-conditional certificate `E[U] ≤ U_S+min{g−U_S,sqrt(I(C;Z'|S)/2)}`, tight under score sufficiency); Theorem 7 conditional on A1–A3 (budget-invariant gap); lemmas 6a/6b/6d; T5 downgraded to setting observation; refs 29–41 added. Data: `analysis/results/identifiability.json` sha `1299c9027016b20a6744e4ec03c16257e0da28e0d6b43994001b5ac8eff65212`; `analysis/results/pool_scaling.json` sha `478cd65ccdebbcb07f22d77205ab51c04cf12d46a2bfcc5ca60a88ae14482f84`; figures `fig7_pool_scaling.png` sha `6242c5f02605b6fdcd94e502ff36b248eaa79845e63e0c21d011a467def065ed`, `fig9_budget_ladder.png` sha `d0c26be28c10efd3…`. D1 certificates are **vacuous on every pool** (I=.059–.183 ≥ 2T²=.008–.041): honest caveat, not validation; gain=T exactly on dev20 S2/S5/S5_ens (ratio 1.00), CompressARC −2.25 pp; +8.11 pp S5_ens headroom is selectable but unrealized (hidden 15.42 < S5 16.25). D2 prefix replay is **definitional**, not T7 evidence; T7 support is the hidden-score ladder 16.25 > 15.42 = 15.42 > 14.17, consistent-not-conclusive (n=6; truncation; S6 bug; 53-task superset; packet/config; unknown hidden size). | `paper/theory_v5_new.md`; `research/design/theory.md` §4.9–4.10; `paper/paper_planC_draft_v5.md`; `analysis/results/identifiability.json`; `analysis/results/pool_scaling.json` | proven/conditional + measured caveats |
| C71 | **v5 build + writeup freeze state.** Paper v5 `paper/paper_planC_draft_v5.md` sha `682eb1ad9e3fb7d42f6a3b63fbee4eb50f4f32943858764c717e921326b9d2ce`: **6,658 non-placeholder words** (6,700 v5 cap; record final count), **0 markers**, 41/41 refs cited, 11/11 figures linked, no forbidden tokens; PV PDF `paper/paper.pdf` sha `23bac82e7b3bab865333…` (21 pp, deterministic rebuild, Typst); arXiv source `paper/arxiv_source/main.tex` regenerated (70,392 B; 11 figures, 10 tables, 41 refs, title updated). Writeup `paper/writeup_kaggle_v5.md` sha `c9750e3eebff3912ffb11032bc79b899e1d67d9a0d85c68da60dc7b136713110`: 1,492 raw / 1,487 non-placeholder ≤1,500; 4 markers (S5b + 3 URLs); honest framing (best hidden 16.25; reference 3/20; LegC negative; unconditional bound vacuous). v4 remains frozen/sha `784cffc7…`. Repo v2.1 staged locally, not pushed. | `paper/paper_planC_draft_v5.md`; `paper/paper.pdf`; `paper/arxiv_source/`; `paper/writeup_kaggle_v5.md`; `paper/qc_v5.py` | build/QC |

| C72 | **Prop. 6f score-conditional addendum (final v5).** Source `analysis/results/identifiability.json` sha `259e1055…`, MD `6f277361…`; `pool_scaling.json` sha `23e7a79c…`. Non-vacuous on **exactly CompressARC**: U_S=.200, g−U_S=.1425, I(C;Z'\|S)=.0336 nats, cap'=.1296 (12.96 pp), measured rule loss −2.25 pp lies inside; elsewhere still vacuous (0 violations total). Score-sufficiency check **inconclusive**: I(C;Z'\|S)=.083–.225 nats, not ≈0; pilot/dev20 score strata collapse to 2 bins (sparse, flagged), so tight-under-score-sufficiency is neither confirmed nor rejected. Added §3.7 paragraph + Table 12b (≤180 words), header cap raised to **6,850**. Final paper sha `a5d9728c29f5b2113d3770a74d53…`; **6,850 non-placeholder words**, 0 markers, 41 refs, 11 figures. PDF sha `af6803424de3fa00…` (21 pp); arXiv `main.tex` sha `e725ecd77183005b…` (11 figs, 11 tables, 41 refs); writeup sha `bb762e70…` (1,495 raw/1,493 non-pl; 1 marker = S5b). Repo v2.1 re-staged locally, not pushed. | `identifiability.json`; `identifiability.md`; `pool_scaling.json`; `paper/paper_planC_draft_v5.md`; Table 12b | measured/proven addendum |
