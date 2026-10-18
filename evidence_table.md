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

| C49 | **Final QC (v2 freeze):** all 25 references cited in the main text (programmatic check, multi-number brackets parsed; uncited = none); Table 5 test count updated to 154 tests ~10 s (measured `pytest tests -q` 2026-10-18; repo `code/docs/REPRODUCE.md` still says 148 and should be reconciled by the release owner); table 2 values are exact two-decimal from the frozen JSON; frozen hash 6c16abfe…4ab71a in paper + evidence table; zero remaining `XX`/`[DA]`/`[PEND]`/provenance tags or reconciliation daggers | `paper/paper_planC_draft_v2.md`; `paper/evidence_table.md`; `analysis/results/SELECTION_RESULTS.md`; `pytest tests -q` | audit (paper-writer, 2026-10-18) |
