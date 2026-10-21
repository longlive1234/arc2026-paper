# Paper v4 numeric-evidence audit (Completeness criterion)

Scope: **every quantitative claim in `paper/paper_planC_draft_v4.md`** (sha256
`cfaa2bdf1f95856069b15bfed9350815f62bd6ec31c9d4ea7e15ef6fd7b6ee2a`, 402 lines, five theorems),
mapped to an on-disk artifact and a reproduction command. Auditor: data-analyst, 2026-10-21.
Status vocabulary: **VERIFIED** = artifact matches the quoted value/claim; **NEEDS-UPDATE** = number is
stale, conditional, ambiguous, or currently untraceable in the frozen artifact and should be fixed/
re-sourced before freeze; **UNTRACEABLE** = quoted value has no on-disk artifact at all.

Run this audit's checks with:

```bash
cd /home/chen/.dsh/ungrouped/arc2026
bash analysis/run_all.sh                       # exit 0, 169 s; frozen hashes stable
python analysis/official_scoring.py --self-test   # official eval + GPU run-dir + sample checks PASS
python analysis/selection_benchmark.py --self-test
python analysis/eval_subsets.py --self-test
python paper/qc_v4.py                          # v4 metadata (words/markers/refs/figures)
PYTHONPATH=code python -m pytest code/tests -q  # 190 passed, 25.73 s
```

**Audit-time summary: 84 VERIFIED, 13 NEEDS-UPDATE, 1 UNTRACEABLE** (98 audited claim rows).
**Post-resolution (see §12): 96 VERIFIED, 2 NEEDS-UPDATE, 0 UNTRACEABLE** — 12 items resolved by the
frozen LB snapshot, AUC artifact, C-gain confirmation and the paper-writer's v4 fixes; remaining:
v4 PDF rebuild and retry/Table 8/10/11 placeholders.

## 1. Document and provenance claims

| # | claim (≤12 words) | value | source artifact (path + sha / section) | reproducible command | status |
|---|---|---|---|---|---|
| 1 | v4 file identity | sha256 cfaa2bdf…b6ee2a | `paper/paper_planC_draft_v4.md` | `sha256sum paper/paper_planC_draft_v4.md` | VERIFIED |
| 2 | v4 base / backup identity | base 68eabd59…3cfa | `paper/paper_planC_draft_v4_pre_theorem5.md` | `sha256sum paper/paper_planC_draft_v4_pre_theorem5.md` | VERIFIED |
| 3 | v4 size and structure | 4,962 raw / 4,819 non-placeholder | `paper/paper_planC_draft_v4.md`; `paper/qc_v4.py` | `python paper/qc_v4.py` | VERIFIED |
| 4 | v4 markers, refs, figures | 16 V4-PEND; 30 cited refs; 8 figures | same; `paper/qc_v4.py` output | `python paper/qc_v4.py` | VERIFIED |
| 5 | v3 published identity / PDF | v3 00435c14…; PDF cacc194d… | `paper/paper_planC_draft_v3.md`; `paper/paper.pdf` | `sha256sum paper/paper_planC_draft_v3.md paper/paper.pdf` | VERIFIED |
| 6 | Kaggle writeup v4 size | 1,486 raw / 1,459 non-placeholder | `paper/writeup_kaggle_v4.md` (sha e6b01a58…58b2) | `python paper/qc_v4.py` | VERIFIED |
| 7 | paper "five theorems" vs abstract "four results" | 5 theorems; abstract/intro say four | paper §Abstract l.11 / §1 l.21; §3.1–3.5 | `grep -n "Theorem\|four results" paper/paper_planC_draft_v4.md` | NEEDS-UPDATE (wording) |
| 8 | v4 PDF exists for current draft | no; `paper/paper.pdf` is v3 | package README; `paper/paper.pdf` sha cacc… | `sha256sum paper/paper.pdf` | NEEDS-UPDATE (rebuild pending) |

## 2. Official data, characterization, leakage

| # | claim (≤12 words) | value | source artifact (path + sha / section) | reproducible command | status |
|---|---|---|---|---|---|
| 9 | Official eval size | 120 tasks / 358 pairs / 172 inputs | `data/comp/arc-agi_evaluation_challenges.json` sha e7c62a4b… | `python analysis/official_scoring.py --self-test` | VERIFIED |
| 10 | Official train size | 1,000 tasks / 3,232 pairs / 1,076 inputs | `data/comp/arc-agi_training_challenges.json` sha 779eaba8… | same command; `analysis/report.md` §1 | VERIFIED |
| 11 | Repo mirror differs | 167 inputs; 5 tasks differ | `analysis/official_data_notes.md` §2; mirror files | `python analysis/official_scoring.py --self-test` | VERIFIED |
| 12 | Official-file hashes | e7c62a4b… challenges; 84be4f4f… solutions | `data/comp/*`; `analysis/official_data_notes.md` §1 | `sha256sum data/comp/arc-agi_evaluation_*.json` | VERIFIED |
| 13 | Local test sample duplicate | 240 tasks / 259 inputs; exact training duplicate | `data/comp/arc-agi_test_challenges.json` sha 232264c5… | `python analysis/official_scoring.py --self-test` | VERIFIED |
| 14 | Rerun budget rates | 12.0 min/task; 11.1 min/input; 4 workers × 12 h | `analysis/official_data_notes.md` §3; Appendix F | `python - <<'PY'\nprint(2880/240,2880/259,0.9*2880/240,0.9*2880/259)\nPY` | VERIFIED |
| 15 | Leakage audit | 0 tasks / 0 pairs / 0 input grids | `analysis/report.md` §12 | `grep -n "shared" analysis/report.md` | VERIFIED |
| 16 | Intra-train reused input grids | 8 grids | `analysis/report.md` §12 | `grep -n "reused in >1" analysis/report.md` | VERIFIED |
| 17 | Trivial-heuristic solve rates | 1.6% train / 1.5% holdout / 0% eval | `analysis/results/baselines.json` sha b3a9f03f…; report §13 | `python analysis/baselines.py; grep -n "union of any heuristic" analysis/report.md` | VERIFIED |
| 18 | Train/eval max grid dim | 14.67 vs 21.95 (p<0.001) | `analysis/report.md` §11; `features_train/eval.json` | `python analysis/figures.py; grep -n "14.67" analysis/report.md` | VERIFIED |
| 19 | Eval in hardest train quartile | 64% | `analysis/report.md` §11 | `grep -n "64% of eval" analysis/report.md` | VERIFIED |
| 20 | Same-size rewrite family share | 54.5% train / 57.5% eval | `analysis/report.md` §9 counts 545/1000, 69/120 | `grep -n "same_size_transform" analysis/report.md` | VERIFIED |
| 21 | Object manipulation share | 12.2% train / 23.3% eval | `analysis/report.md` §9 counts 122/1000, 28/120 | same table; `python - <<'PY'\nprint(122/1000,28/120)\nPY` | VERIFIED |
| 22 | Grid-panel share | 11.7% train / 12.5% eval | `analysis/report.md` §9 counts 117/1000, 15/120 | `python - <<'PY'\nprint(117/1000,15/120)\nPY` | VERIFIED |
| 23 | Shape-rule prediction accuracy | 83.6% train / 69.2% eval | `analysis/report.md` §13 table | `grep -n "output-shape predictable" analysis/report.md` | VERIFIED |
| 24 | TTT-solvability tiers | A/B/C = 28 / 56 / 36 | `analysis/results/allocation.json` sha 772a8a48…; report §15 | `python -c "import json;a=json.load(open('analysis/results/allocation.json'));print(a['summary']['eval']['tier_counts'])"` | VERIFIED |
| 25 | Tier-B compute share | 76% (75.82%) of eval compute | `analysis/results/allocation.json` `summary.eval.share_by_tier_pct.B` | same command | VERIFIED |
| 26 | Official eval fallback score | 0/120 tasks; 0/172 inputs | `analysis/results/official_scores.json` sha 35360183… | `python analysis/official_scoring.py --recompute-all` | VERIFIED |
| 27 | Dataset B provenance | displayed 30.97; 20 tasks/29 inputs; 347 files | `analysis/results/pool_inventory.json` sha 6e503d70…; `research/lit/verified_solutions.md` | `python analysis/pool_importer.py --scan /tmp/kout_* --inventory-out analysis/results/pool_inventory.json` | VERIFIED |
| 28 | Dataset B reproduction gate | 29 inputs; oracle 9/29; top-2 8/29 | `logs/arch-theorist/external_reproduction_gate_arc2_dump.json` sha 62881c4b… | `cat logs/arch-theorist/external_reproduction_gate_arc2_dump.json` | VERIFIED |
| 29 | Dataset A reproduction gate | solved 137/400; ≤2 guesses 80/400 | `code/out/compressarc/verify_bundled_eval.json` sha 0fa8a7d5… | `python code/compressarc_harness.py verify-bundled --out code/out/compressarc/verify_bundled_eval.json` | VERIFIED |
| 30 | Dataset A split | 400 fit / 400 eval tasks | `analysis/results/selection_benchmark.json` sha 6c16abfe… (`datasets.A.split`) | `python analysis/selection_benchmark.py --self-test` | VERIFIED |
| 31 | Dataset C scale | 120 simulated tasks | same frozen JSON (`datasets.C`) | `python analysis/selection_benchmark.py --self-test` | VERIFIED |

## 3. Theory: Theorems 1–5 and frozen constants

| # | claim (≤12 words) | value | source artifact (path + sha / section) | reproducible command | status |
|---|---|---|---|---|---|
| 32 | Theorem 1 independent top-2 | U=p_i+p_j−p_i p_j | `research/design/theory.md` §4.1; paper §3.1 | `python - <<'PY'\np=[.5,.3];print(p[0]+p[1]-p[0]*p[1])\nPY` | VERIFIED (analytic) |
| 33 | Theorem 2 duplicate dominance | distinct candidate strictly dominates | `research/design/theory.md` §4; paper §3.2 | analytic restatement; no numeric constant | VERIFIED (analytic) |
| 34 | Theorem 3 correlated suboptimality | p=0.50, p3=0.35 gain +17.5 pts | paper §3.3; theory §4 | `python -c "print(.5+.35-.5*.35-.5)"` → 0.175 | VERIFIED (analytic) |
| 35 | Theorem 4 threshold formula | ρ*=√(p₂(1−p₁)/(p₁(1−p₂))) | paper §3.4 eq. (7); theory §4.2 | `python - <<'PY'\nimport math;print(math.sqrt(.05*.5/(.5*.95)))\nPY` → 0.2294 | VERIFIED (analytic) |
| 36 | Theorem 4 skew example | ρ*≈0.229 at p=0.50, p₂=0.05 | paper §3.4 Cor. 2 | `python -c "import math;print(round(math.sqrt(.05*.5/(.5*.95)),3))"` | VERIFIED |
| 37 | Theorem 4 equal marginal | ρ*=1; ΔU=p(1−p)(1−ρ) | paper §3.4 Cor. 1 | `python -c "p=.5;print(p*(1-p)*(1-0.0))"` → 0.25 | VERIFIED (analytic) |
| 38 | Theorem 5 count/statement | five theorem blocks incl. budget allocation | paper §3.5; theory §4.7; registry A.11 | `grep -n "Theorem 5" paper/paper_planC_draft_v4.md research/design/theory.md` | VERIFIED |
| 39 | Frozen gate margin δ | 0.05 | paper §3.4 derived gate; `research/design/selection_protocol_v2.md` §6d | `grep -n "delta\|δ" research/design/selection_protocol_v2.md` | VERIFIED (protocol) |
| 40 | ρ̂ clipping bounds | [−0.95, 0.99] | paper §3.6; `analysis/selection_benchmark.py` | `grep -n "clip" analysis/selection_benchmark.py` | VERIFIED |
| 41 | Paired bootstrap design | 2,000 resamples, seed 0, 80/95% CIs | `analysis/selection_benchmark.py` (`N_BOOT`, `SEED`); protocol §6 | `grep -n "N_BOOT\|SEED" analysis/selection_benchmark.py` | VERIFIED |
| 42 | Claim threshold | +1.0 point, 80% CI lower >0 | `research/design/selection_protocol_v2.md` §6; selection benchmark verdict strings | `grep -n "1.0\|claim" analysis/results/SELECTION_RESULTS.md` | VERIFIED (protocol) |
| 43 | Calibration gate thresholds | Brier≤0.10; slope [0.7,1.3] in paper | paper §3.6; **code uses slope [0.2,5.0]** | `grep -n "brier_ok" analysis/selection_benchmark.py; grep -n "slope_ok" analysis/selection_benchmark.py` | NEEDS-UPDATE (paper/code mismatch) |

## 4. Dataset B (NVARC-TTT pilot, 16 eval inputs / 11 tasks)

| # | claim (≤12 words) | value | source artifact (path + sha / section) | reproducible command | status |
|---|---|---|---|---|---|
| 44 | B split | fit 9 tasks/13 inputs; eval 11/16 | frozen JSON `datasets.B.split` sha 6c16abfe… | `python analysis/selection_benchmark.py --self-test` | VERIFIED |
| 45 | B oracle / deployable rules | all 31.25% | frozen JSON; `analysis/results/SELECTION_RESULTS.md` §B | `python analysis/selection_benchmark.py; grep -n "Dataset B" analysis/results/SELECTION_RESULTS.md` | VERIFIED |
| 46 | B 80% CI | [18.75, 43.75] | frozen JSON `rules.*.pass2_unit_ci80` | `python - <<'PY'\nimport json;d=json.load(open('analysis/results/selection_benchmark.json'));print(d['datasets']['B']['rules']['oracle_any2']['pass2_unit_ci80'])\nPY` | VERIFIED |
| 47 | B deployed fallback | 25.00% (one input below) | frozen JSON `rules.deployed.pass2_unit` | same command, key `deployed` | VERIFIED |
| 48 | B headroom | 0 on eval fold | derived from rows 45–47; frozen JSON task meta | `python analysis/selection_benchmark.py --self-test` | VERIFIED |
| 49 | B official-truth unchanged | B row unchanged; abc82100 spans labels | `analysis/results/selection_benchmark_official.json` sha cb830844…; C53/C55 | `python analysis/selection_benchmark.py --truth-mode official` | VERIFIED |
| 50 | B scale / files | 20 tasks, 29 inputs, 347 files | `pool_inventory.json`; external gate JSON | `grep -n "n_files" analysis/results/pool_inventory.json` | VERIFIED |

## 5. Dataset A (CompressARC, 400 tasks, unit=task)

| # | claim (≤12 words) | value | source artifact (path + sha / section) | reproducible command | status |
|---|---|---|---|---|---|
| 51 | A oracle / any-guess coverage | 34.25% (137/400) | frozen JSON sha 6c16abfe…; C39 | `python analysis/selection_benchmark.py; grep -n "Dataset A" analysis/results/SELECTION_RESULTS.md` | VERIFIED |
| 52 | A duplicate | 18.50% [16.00, 21.00] | frozen JSON `rules.duplicate` | `python - <<'PY'\nimport json;d=json.load(open('analysis/results/selection_benchmark.json'));print(d['datasets']['A']['rules']['duplicate'])\nPY` | VERIFIED |
| 53 | A argmax1+argmax2 | 19.50% [17.00, 22.00] | frozen JSON `rules.argmax1_argmax2` | same command | VERIFIED |
| 54 | A top2 consensus | 20.00% [17.50, 22.75] | frozen JSON `rules.top2_consensus` | same command | VERIFIED |
| 55 | A cal_indep | 18.00% [15.50, 20.75] | frozen JSON `rules.cal_indep` | same command | VERIFIED |
| 56 | A coverage_optimal | 17.75% [15.25, 20.25] | frozen JSON `rules.coverage_optimal` | same command | VERIFIED |
| 57 | A deployed fallback | 19.25% [16.75, 21.75] | frozen JSON `rules.deployed`; C39 | same command | VERIFIED |
| 58 | A headroom | 57 tasks = 14.25 pp | frozen JSON `extra.verification.headroom`; C30/C39 | `python - <<'PY'\nimport json;print(json.load(open('analysis/results/selection_benchmark.json'))['datasets']['A']['extra']['verification']['headroom'])\nPY` | VERIFIED |
| 59 | A missed-truth ranks | median 12; 24/57 in top-10 | frozen JSON `extra.missed_truth`; C40 | same command key `missed_truth` | VERIFIED |
| 60 | A margin / verdict | coverage−argmax −1.75 pp; DOWNGRADE | frozen JSON; `SELECTION_RESULTS.md` verdicts | `grep -n "DOWNGRADE" analysis/results/SELECTION_RESULTS.md` | VERIFIED |
| 61 | A candidate AUC | 0.981 | **not in frozen JSON**; only superseded C31 / older drafts | `grep -n "0.981" analysis/results/selection_benchmark.json` → absent | NEEDS-UPDATE (recompute or drop) |

## 6. Dataset C, calibration, statistics

| # | claim (≤12 words) | value | source artifact (path + sha / section) | reproducible command | status |
|---|---|---|---|---|---|
| 62 | C oracle | 41.67% [35.83, 47.50] | frozen JSON `datasets.C` | `python analysis/selection_benchmark.py --self-test` | VERIFIED |
| 63 | C duplicate / argmax / top2 | 16.67 / 23.33 / 21.67 | frozen JSON `datasets.C.rules` | same command | VERIFIED |
| 64 | C calibrated/coverage/deployed | all 41.67% | frozen JSON `datasets.C.rules` | same command | VERIFIED |
| 65 | C gain over argmax | +18.34 pp, 95% CI [11.7,25.0] | frozen JSON delta = 0.1833, CI [0.1167,0.25] | `python - <<'PY'\nimport json;d=json.load(open('analysis/results/selection_benchmark.json'));print(d['datasets']['C']['rules']['coverage_optimal']['delta_vs_argmax1_argmax2'], d['datasets']['C']['rules']['coverage_optimal']['delta_ci95_vs_argmax1_argmax2'])\nPY` | NEEDS-UPDATE (18.34 vs 18.33 rounding) |
| 66 | C gate slope | 0.025 | frozen JSON `datasets.C.calibration.reliability_slope` = 0.0247 | same command | VERIFIED |
| 67 | Gate outcomes | B/A/C gate FAIL (slope check) | frozen JSON calibration gates; C39/C41–C43 | same command, key `calibration.gate` | VERIFIED |
| 68 | Brier/slope thresholds in paper | Brier≤0.10, slope ∈ [0.7,1.3] | paper §3.6 vs code [0.2,5.0] | `grep -n "brier_ok" analysis/selection_benchmark.py; grep -n "slope_ok" analysis/selection_benchmark.py` | NEEDS-UPDATE (reconcile) |

## 7. GPU/dev evidence and first submission

| # | claim (≤12 words) | value | source artifact (path + sha / section) | reproducible command | status |
|---|---|---|---|---|---|
| 69 | Dev2 pilot wall / load | 466.7 s wall; 106.9 s model load | `logs/kaggle_runs.md` row 23; `logs/runs/2026-10-20_dev2/` | `python code/analyze_run.py --dir logs/runs/2026-10-20_dev2` | VERIFIED |
| 70 | Dev2 per-task walls | 202.51 s / 238.12 s; ≈220 s mean | same ledger row 23; worker logs | same command | VERIFIED |
| 71 | Dev2 train/decode ranges | train 53.0–144.4; decode 17.6–134.9 | same ledger row 23 | same command | VERIFIED |
| 72 | Dev2 candidates / oracle | 15 candidates; oracle 1/2 | `logs/runs/2026-10-20_dev2/offline_analysis.json`; ledger row 23 | `cat logs/runs/2026-10-20_dev2/offline_analysis.json` | VERIFIED |
| 73 | Dev2 attempt behaviour | attempt-1 hit one task; attempt-2 added none | offline_analysis `attempt1_hit/attempt2_hit` | same command | VERIFIED |
| 74 | Rerun budget / config | 41,400 s; S1/aug8; 4×L4 | packet manifest `notebook/ttt_packet/packet_manifest.json`; ledger row 25 | `cat notebook/ttt_packet/packet_manifest.json` | VERIFIED |
| 75 | Fair per-task cap | 578 s at 240 tasks; 1156 s if 120 | `code/arc/run.py::dynamic_task_cap_s`; computed 578.0/1156.0 | `python -c "print((41400-600)*4/240*0.85, (41400-600)*4/120*0.85)"` | NEEDS-UPDATE (paper states 578 flat while hidden size unknown) |
| 76 | Headroom / unused wall | 2.6× headroom; ~7.8 h unused | derived from rows 70/74/75 | `python -c "print(578/220.31, 11.5-240/4*220.31/3600)"` | VERIFIED |
| 77 | First submission identity/status | ref 57456856; created 00:01:15Z; COMPLETE; no score | `analysis/results/kaggle_submission_api_57456856.json` | `/home/chen/anaconda3/bin/kaggle competitions submissions -c arc-prize-2026-arc-agi-2` | VERIFIED |
| 78 | Error cause | `int("41400.0")` ValueError before pipeline | `analysis/rerun_failure_analysis.md` §2; `analysis/results/rerun_v8_diagnosis.json` | `cat analysis/results/rerun_v8_diagnosis.json` | VERIFIED |
| 79 | Rerun wall time | ≈2 h 34 min, queue-only | `logs/submission_57456856_monitor.log`; paper §4.1 | `tail -20 logs/submission_57456856_monitor.log` | VERIFIED |
| 80 | CPU test-suite count | 154 tests, ~10 s | paper §7/Table 5 | `PYTHONPATH=code python -m pytest code/tests -q` → **190 passed, 25.73 s** | NEEDS-UPDATE |
| 81 | CPU fallback runtime claim | 172 official inputs in 8.3 s on Kaggle | paper §7; `analysis/official_data_notes.md` §4c | `grep -n "8.3 s\|5.41" analysis/official_data_notes.md` | NEEDS-UPDATE (8.3 s was 167-input repo packet on Kaggle; official 172-input repackaging measured 5.4 s locally) |
| 82 | Pipeline reproduction wall | run_all.sh ~41 s | paper Appendix D; current run 169 s | `bash analysis/run_all.sh` | NEEDS-UPDATE |
| 83 | 2026-10-18 run count/breakdown | 13 runs: six probes, two fallback, two TTT, one probe | paper Appendix C; ledger rows 1–13 = 5 probes / 3 fallback / 5 TTT | `sed -n '1,20p' logs/kaggle_runs.md` | NEEDS-UPDATE (breakdown) |
| 84 | CompressARC reproduction row | 137/400 solved; 80/400 pass@2 | `code/out/compressarc/verify_bundled_eval.json`; Table 5 | `cat code/out/compressarc/verify_bundled_eval.json` | VERIFIED |
| 85 | Retry date / reserved rows | retry 2026-10-22; Tables 8/10/11 pending | paper Table 9 + V4-PEND markers | `grep -n "V4-PEND" paper/paper_planC_draft_v4.md` | NEEDS-UPDATE (pending data, by design) |

## 8. Landscape and external anchors

| # | claim (≤12 words) | value | source artifact (path + sha / section) | reproducible command | status |
|---|---|---|---|---|---|
| 86 | Open-notebook displayed cluster | nine notebooks, 29.7–31.4 | `research/lit/verified_solutions.md` §1; paper Table 4 | `sed -n '12,25p' research/lit/verified_solutions.md` | NEEDS-UPDATE (10 distinct notebooks row-wise; table also shows 29.17 and 15.69) |
| 87 | Title-claimed scores | 33.89 / 35.9 not displayed | `research/lit/verified_solutions.md` §1/§4 | same command | VERIFIED (context) |
| 88 | Table 4 per-notebook displayed/claimed values | 31.39/31.39/30.97/30.97/30.14/29.72/29.17/15.69/30.56 | `research/lit/verified_solutions.md` §1 | same command | VERIFIED (context) |
| 89 | Saved-artifact official scores | vanductan 5/120 tasks, 8/172 inputs; others 2–4/120 | `analysis/results/official_scores.json` sha 35360183… | `python analysis/official_scoring.py --recompute-all` | VERIFIED |
| 90 | CPU fallback official score | 0/120 tasks, 0/172 inputs | same official_scores JSON | same command | VERIFIED |
| 91 | Concurrent prior headroom | 26.1% scored vs 32.5% perfect selection | reference [26] URL; `research/design/experiment_registry.md` Y1 | paper References [26] | VERIFIED (external citation) |
| 92 | Pass@k ceiling diagnostic | selection ≈95% of candidate ceiling (M=5) | reference [27] URL | paper References [27] | VERIFIED (external citation) |
| 93 | LB context anchors | 3,091 teams; gold 31.81/silver 30.97/bronze 30.56 | **no on-disk artifact**; only paper/Lead context (`paper/v4_fill_plan.md`) | `grep -rn "3,091" paper analysis logs research` | UNTRACEABLE |
| 94 | Hidden-set size | unknown (120–240); sample 240/259 | `analysis/official_data_notes.md` §3; paper App. F | `python analysis/official_scoring.py --self-test` | VERIFIED (statement) |

| 95 | Competition format: two attempts, ~12 h offline | two attempts/input; ≈12 h; no internet | competition rules [15]; `notebook/ttt_packet/*.json` `enable_internet:false`; packet provenance | `grep -n "enable_internet" notebook/ttt_packet/kernel-metadata.competition.json` | VERIFIED (context) |
| 96 | Official data constraints | grids ≤30×30; colours 0–9 | `data/comp/arc-agi_evaluation_challenges.json`; training file | `python -c "import json,numpy as np;d=json.load(open('data/comp/arc-agi_evaluation_challenges.json'));print(max(max(np.shape(p['input'])) for t in d.values() for p in t['train']))"` | VERIFIED |
| 97 | Appendix H cross-source values | 50/70 split; best 1/70; cross 1/70; union 8/70 | frozen JSON `cross_source` sha 6c16abfe…; Appendix H | `python -c "import json;c=json.load(open('analysis/results/selection_benchmark.json'))['cross_source'];print(c['n_dev_tasks'],c['n_holdout_tasks'],c['holdout_best_single_source'],c['holdout_cross_source'],c['holdout_union_oracle'])"` | VERIFIED |
| 98 | Appendix E estimator constants | δ=0.05; pair cap 32; slope [0.7,1.3]; 2,000 boot/seed 0 | `research/design/diversification_threshold.py` (lines 15/127/228); protocol §6d | `grep -n "pair_cap" research/design/diversification_threshold.py; grep -n "1.3" research/design/diversification_threshold.py` | VERIFIED |

## 9. Frozen-hash verification (expected vs actual)

| artifact | expected in `paper/evidence_table.md` | actual 2026-10-21 | status |
|---|---|---|---|
| `analysis/results/selection_benchmark.json` | 6c16abfef7f0efe3a1a6bbe9f6251c9aeef1893ee7b0f44fdfdb9c2eb34ab71a (C38/C53/C55) | same | VERIFIED |
| `analysis/results/selection_benchmark_official.json` | cb8308448f78ed5064a8f13827ef9117908184cf5b6354f591cffa1951552df0 (C55) | same | VERIFIED |
| `analysis/results/official_scores.json` | used by C52 (no hash in table) | 35360183ab18f34c00b8b2268b4886b3b731c740312d572180a4bc0bb4e75f6e | VERIFIED |
| `analysis/results/saved_artifact_scores.json` | used by C44 (no hash in table) | 056828497fb222be90f36fd439beef2cd564c0f2e70325dfee725d6879e86ac5 | VERIFIED |
| `paper/paper_planC_draft_v4.md` | cfaa2bdf1f95856069b15bfed9350815f62bd6ec31c9d4ea7e15ef6fd7b6ee2a (C59) | same | VERIFIED |
| `paper/paper_planC_draft_v3.md` | 00435c14d832eb756d536feec680d1ac85f0488bf06cd1450c40dae2e3d29972 (C50) | same | VERIFIED |
| `paper/paper.pdf` | cacc194d02cf6f3f465cb0adbd922f7367b218d015f2d7dd0b384435e250ca26 (C54, v3 PDF) | same file (v3; **no v4 PDF**) | VERIFIED (as v3) / NEEDS-UPDATE (v4 rebuild) |
| `data/comp/arc-agi_evaluation_{challenges,solutions}.json` | e7c62a4b… / 84be4f4f… (C57) | same full hashes | VERIFIED |

**Run results (this audit):** `bash analysis/run_all.sh` exit 0, **169 s**; post-run checked hashes
identical to pre-run for all frozen artifacts (no drift). `analysis/official_scoring.py --self-test`
PASS (oracle 120/120 tasks & 172/172 inputs; sample schema; GPU scorer). `analysis/selection_benchmark.py
--self-test` PASS. `analysis/eval_subsets.py --self-test` PASS. `pytest code/tests` **190 passed in
25.73 s**.

## 10. Evidence-table drift (documentation, not frozen artifacts)

1. **C52** says official-fallback rebuild runtime "not measured"; **C56** later measured it locally
   (5.41 s median). The paper's 8.3 s/172-input sentence needs the C56 wording (row 81).
2. **C49** says 154 CPU tests; current suite is 190 after hardening tests (row 80). Update C49/Table 5.
3. **C14/C25** still carry repo-mirror counts (359/167, /167 inputs); canonical C51/C52 use official
   358/172. Paper v4 correctly uses C51; keep C14/C25 marked superseded so they are not re-used.
4. **C54** PDF hash is the v3 PDF; v4 PDF is deliberately not built yet (row 8).
5. No frozen hash changed after `run_all.sh`; all claims' frozen artifacts are intact.

## 11. Verdict and actions before freeze (audit-time; see §12 for resolutions)

Counts at audit time: **84 VERIFIED / 13 NEEDS-UPDATE / 1 UNTRACEABLE** (rows 1–98). Twelve of these
were resolved on 2026-10-21 (LB snapshot frozen, AUC recomputed, C gain confirmed, and paper-writer's
v4 fixes applied); see §12.

**Must fix (paper text, high priority):**
- `AUC 0.981` (row 61): either recompute/store it in the frozen benchmark artifact or delete it.
- `154 tests` (row 80) → current **190 tests / 25.7 s**; update §7 + Table 5 + C49.
- CPU-fallback `8.3 s / 172 inputs` (row 81) → use the hardened wording: 8.3 s = earlier 167-input
  repo packet on Kaggle; official 172-input repackaging = 5.4 s locally (no Kaggle run).
- Gate slope range (rows 43/68): paper says [0.7,1.3], implementation uses [0.2,5.0]; reconcile
  (either paper wording or code, then regenerate artifact/evidence).
- `run_all.sh ~41 s` (row 82) → current **169 s**.
- Appendix C breakdown (row 83) → ledger rows are 5 probes / 3 fallback / 5 TTT = 13; fix prose.
- Five-theorem wording (row 7) → abstract/intro say four results; either say four core results +
  Theorem 5 extension, or five.
- Dataset C +18.34 pp (row 65) → artifact delta is 0.1833; use 18.33 or display-consistent 18.34 and
  label CI [11.67,25.0] → [11.7,25.0].
- `578 s` cap in §4.1/Table 9 (row 75) is conditional on 240 tasks; state "578 s if 240 tasks; 1156 s
  if 120" (hidden-size dependence).
- Nine-notebook/29.7–31.4 wording (row 86) and title-claims sentence (row 87): table has 10 distinct
  notebooks incl. 29.17/15.69 and claimed 54.31%/80%+; scope/range must be stated precisely.
- **UNTRACEABLE**: LB context anchors 3,091 teams / gold 31.81 / silver 30.97 / bronze 30.56 (row 93):
  freeze a dated snapshot or drop the numbers; currently only Lead context/writeup.
- Pending-by-design rows 8/85 (v4 PDF, retry/Table 8/10/11) remain NEEDS-UPDATE until data lands.

**No action needed:** 70 VERIFIED rows match on-disk artifacts and frozen hashes; the selection
benchmark, official scoring, data characterization, dev2 and submission facts are all traceable.


## 12. Audit resolutions (2026-10-21, post-audit)

**Resolved to VERIFIED (12):**
1. **LB context (untraceable → frozen):** `analysis/results/leaderboard_snapshot_2026-10-20.{csv,json,md}`
   (CSV sha `f48304f7…a17ac6`, JSON sha `c7a5d093…2271f8`, MD sha `e635bc23…85365`); 3,091 rows
   (3,090 ranked + 1 rank-0), leader Tufa Labs 88.06; anchors top1/2/5/10/20/30% = ranks 30/61/154/309/618/927
   → scores 52.50/37.78/32.64/31.81/30.97/30.56; **medal cutoffs NOT asserted**; our team absent/no scored
   submission.
2. **AUC 0.981:** not reproducible from frozen artifacts; replaced by `analysis/results/candidate_auc.json`
   (sha `1522ab19…19f4`): eval **0.9688** (source score) / **0.9722** (calibrated p̂). v4 now quotes no
   AUC number ("predictable but score-dominated").
3. **C gain:** canonical **18.33 pp** (0.1833; 95% CI [11.67,25.00]); 18.34 was display rounding; paper
   v4 + writeup now use 18.33 [11.67,25.0]. `analysis/results/audit_resolutions.json`
   (sha `9a72dc93…11dfa`) records all three resolutions and the canonical values.
4. **Paper v4 fixes applied by paper-writer** (new v4 sha `7c0887fa…80a9`, writeup `44a2096d…b890`):
   five-results/theorem wording; gate slope states code range [0.2,5.0] (design target [0.7,1.3]);
   cap 578 s if 240 / 1156 s if 120; tests 190 (~26 s); fallback provenance 8.3 s=167-input Kaggle /
   5.4 s=official 172-input local; run_all 169 s; Appendix-C breakdown 5/3/5; ten-notebook/29.7–31.4
   scope; AUC number removed; C gain 18.33.

**Remaining NEEDS-UPDATE (2):**
- v4 PDF rebuild (row 8) — `paper/paper.pdf` is still v3 (sha `cacc194d…`); build at freeze.
- Retry row / Table 8/10/11 placeholders (row 85) — by design, pending the 2026-10-22 rerun and dev sweep.

**New frozen artifacts:** `selection_benchmark.md` sha `891c5873…f473` (C-gain audit note);
`audit_resolutions.json` sha `9a72dc93…11dfa`; LB set above; `candidate_auc.json` above.

*Auditor note: statuses classify citations to external works as VERIFIED (context) only when the
paper's References entry is present; they are not independently re-measured here.*
