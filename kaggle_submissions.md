# Kaggle submission journal — ARC Prize 2026 (`arc-prize-2026-arc-agi-2`)

Owner: kaggle-runner. All times UTC. One row per competition submission (and its rerun status).
Quota note: L4 wall-hour = 2 quota-hours; **reruns are free** (1/day); version creations ≈0.1–0.2 quota-h.
Kernel: `wen134/arc2026-ttt` (private; re-created 2026-10-21, `id_no 140000007`), competition source
attached, pinned BYOD image. Submission action: **Lead only**.
*(This file was accidentally truncated 2026-10-28 00:03Z by a bad append; reconstructed from session
records and `logs/kaggle_runs.md` — all refs/scores re-checked against the Kaggle API on 2026-10-28.)*

## Submission table

| # | ref | submitted (UTC) | kernel / version | description | status | publicScore | notes |
| ---: | :--- | :--- | :--- | :--- | :--- | ---: | :--- |
| 1 | `57442788` | 2026-10-20 14:56:07 | `wen134/arc2026-cpu-fallback` (CPU) | cpu fallback insurance: submission ID + rerun-path validation | COMPLETE | — (blank; CPU/no valid score) | CPU insurance + rerun-path wiring test; 120-task eval artifact at creation |
| 2 | `57456856` | 2026-10-21 00:01:15 | `wen134/arc2026-ttt` **v8** (packet `3774c892…`/`87ca30dd…`) | S1 half-cost TTT baseline v1: 240-task hidden budget, aug8, coverage selection | COMPLETE ~02:35Z | — (no score) | **RERUN ERROR**: env-int landmine `os.environ["ARC_BUDGET_S"] = str(11.5*3600)` = `"41400.0"` then `int("41400.0")` **before** try/except → notebook dies instantly; Kaggle queue made it look like 2 h 34 min. Root cause confirmed by Lead + local gate; fix: `int(float(...))` parsers + no-raise validate/SAFETY cells |
| 3 | `57500870` | 2026-10-22 00:00:23 | `wen134/arc2026-ttt` **v3** (hardened S1 CPU version) | hardened S1 CPU-version probe (rerun-hardware test) | COMPLETE | **0.00** | Case B confirmed: rerun respected CPU-flag → no TTT work; valid scored submission, no score |
| 4 | `57663405` | 2026-10-26 10:45:00 | `wen134/arc2026-ttt` **v8** (hardened S1 L4, packet `9060264c…`) | hardened S1 L4 TTT baseline (v8) | COMPLETE | **14.17** | First real L4 rerun score; long queue (~13.6 h to COMPLETE) but clean |
| 5 | `57681632` | 2026-10-27 00:00:28 | `wen134/arc2026-ttt` **v16** (competition S5 L4, packet `6211b694…`) | S5 L4 TTT baseline v1 (single-model palette/rescue, Oct 27) | COMPLETE | **16.25** | **Champion** (+2.08 over S1); daily allowance consumed by Lead's timed execution; duplicate CLI attempts got 400 "daily Submission allowance (1) used today" (harmless) |
| 6 | `57716141` | 2026-10-28 00:00:27 | `wen134/arc2026-ttt` **v22** (fixed competition_s6 L4, packet `83112d6a…`) | S6 dual-config L4 (A aug8 + B aug16/eval2, Oct 28) | **PENDING** (watcher) | — | Oct 29 candidate after score; manual branch verified 240/259 before submit |

Champion history: S1 CPU 0.00 → S1 L4 14.17 → S5 L4 **16.25** → S6 dual-config pending.

## Root cause of the v8 rerun failure (for the paper/engineering evidence)

- Rerun-only branch set `os.environ["ARC_BUDGET_S"] = str(11.5*3600)` = `"41400.0"`; the run cell did
  `int(os.environ.get("ARC_BUDGET_S", 11.5*3600))` → `ValueError: invalid literal for int() with base
  10: '41400.0'` **before** its try/except → notebook died on rerun.
- Fix (in hardened packets): `BUDGET_S = int(11.5*3600)`; env writes `str(int(...))`; all parsers
  `int(float(...))`; validate/repair cell never raises; FINAL SAFETY cell always writes a validated
  2-attempt submission (`ensure_valid_submission`), preserving internal challenge ids/counts.
- Rerun log retrieval: competition-rerun logs are **web-UI only**; `kernels output …/8` returns the
  latest version's manual-run output (`kaggle kernels output/file` version suffix is effectively
  ignored once newer runs exist). `/api/v1/competitions/submissions/<ref>` → 404.

## Rerun-simulation gate (mandatory before every competition push)

Script: `notebook/tools/gate_rerun_sim.py`. Matrix: `--inject none|invalid|missing|exception` ×
(240-task sample `data/comp/arc-agi_test_challenges.json`, 120-task-shaped `/tmp/ch120.json`).
Hardened packet `competition` sha `9060264c…` (source `7a1c16cb…`) = **8/8 PASS** (zero exceptions,
`submission_valid=True errors=[]`; invalid colour 12 clamped, missing task restored; Lead's
independent gate also PASS). Result recorded in
`notebook/ttt_packet/pinned_2026-10-22_hardened_s1/gate_report.json`.

## Kernel incident (2026-10-21)

- `wen134/arc2026-ttt` was deleted mid-S5-smoke; re-created by kaggle-runner under the same slug with a
  tiny CPU placeholder (**new `id_no 140000007`**); old v1–v10 outputs gone, all needed artifacts
  preserved locally (pinned packets, dev2 logs, gate reports).
- Version numbering restarted; push races have since caused baked `ARC_NOTEBOOK_REF` to lag the actual
  version (`/21` baked, version 22/23 assigned) — cosmetic only.

## Pending submission monitors

- `logs/submission_2026-10-26_monitor.log` — 57663405 (captured: COMPLETE 14.17).
- `logs/submission_2026-10-27_monitor.log` — 57681632 (captured: COMPLETE 16.25).
- `logs/submission_oct28plus_monitor.log` — generic new-ref watcher (captured 57716141 PENDING).

## Cadence rules

1. Gate every competition packet (`gate_rerun_sim.py`, 4 injections × 2 shapes) → PASS required.
2. Push at ~23:45 UTC (manual cheap branch ≈2–3 min ≈0.1–0.2 quota-h); verify version COMPLETE and
   manual branch artifact = 240/259 with `validation errors: NONE`.
3. Lead submits at 00:01 UTC with `-f submission.json -v <N>`; daily allowance = 1/day; reruns free.
4. Record ref/version/packet sha/score; keep `logs/kaggle_runs.md` + `logs/submission_calendar.md` current.
5. Keep ≥0.20 h buffer before quota refresh; save ≥8 h of refreshed quota for final-day versions.

## 2026-10-28 01:32Z — version staging (no submission yet)
- **v25 = competition_s5_legc** (`412d10a3…`): S5 TTT base + LegC verified-induction pre-pass (qwen2.5-coder-7b),
  monotone merge (floor = plain S5 16.25), projected ~6.1 h, manual artifact **240/259** verified → Oct 30 00:01 candidate.
- **v23 = fixed competition_s5_ens** (`4cb6e181…`) → Oct 29 00:01 candidate.
- **v24 = competition_s5b** (`00afc2a9…`, S5 + eval_color_perms=2) → fallback for Oct 30.
- Reference-path status: dev20_ref L4 = **3/20 (15%)** at 3600 s budget (below S1 4/20) → reference base NOT promoted;
  dev20_ref_7200 (`2e980714…`, 2 h budget) queued for Oct 31 refresh to test full-budget reference quality.
- Quota before refresh: ~1.1 h; refresh 2026-10-31 00:00 UTC → 30 h.

## 2026-10-28/29 results
- **Oct 28: ref 57716141 (v22 = fixed S6 dual-config L4) → COMPLETE, publicScore = 15.42.**
  Below the S5 champion (16.25): S6's extra second round did not add coverage on the hidden half
  (−0.83 vs S5), consistent with dev20 (S6 A-floor ≈ S1; A∪B union gain not realized through selection).
- **Oct 29: ref 57752011 (v23 = fixed competition_s5_ens, 2 models sequential, score_aug + monotone guard)**
  submitted 2026-10-29T00:02:23Z → PENDING. This probes whether the 2-model ensemble beats single-model S5 (16.25).
- Scoreboard so far: S5 **16.25** (champion) > S6 15.42 > S1 14.17 > CPU probe 0.00.
- Quota before Oct 31 refresh: 0.29 h; refresh 2026-10-31T00:00Z → 30 h.

## 2026-10-29/30 results + submissions
- **Oct 29: ref 57752011 (v23 = fixed S5_ens two-model) → COMPLETE, publicScore = 15.42.**
  Same score as S6 (15.42); both below single-model S5 (16.25). Two-model ensemble did not beat S5 on the hidden half.
- **Oct 30: ref 57785740 (v25 = S5 TTT + LegC verified-induction pre-pass, monotone merge, floor=S5)**
  submitted 2026-10-30T00:02:21Z → PENDING. This is the first submission with a component that can only ADD
  train-verified DSL outputs on top of the S5 champion (LegC promotes attempt_1 monotone; fallback = plain S5).
- Scoreboard: **S5 16.25 (champion)** > S6 15.42 = S5_ens 15.42 > S1 14.17 > CPU probe 0.00.
- Quota: 0.29 h until 2026-10-31T00:00Z refresh (30 h).
- Next: Oct 31 refresh → run dev20_s5_legc (`864e4bcd…`) and dev20_ref_7200 (`2e980714…`) validations, then
  choose Nov 1 champion; Nov 2 final submission + paper freeze.

## 2026-10-30 → 2026-11-01 results (critical updates)
- **Oct 30: ref 57785740 (v25 = S5 + LegC verified-induction hybrid) → COMPLETE, publicScore = 14.17.**
  The LegC pre-pass HURT (−2.08 vs S5 16.25): the 1 h induction pre-pass reduced S5's base budget and/or
  promoted candidates that displaced better S5 attempts. Champion remains S5 (16.25).
  → LegC hybrid rejected as a submission path; paper reports it as a negative ablation.
- **Oct 31 submission MISSED** (session gap; reminder queued and delivered late). No ref for 2026-10-31.
- **Nov 1: ref 57854697 (v24 = S5b: S5 + eval_color_perms=2)** submitted 2026-11-01T00:10:23Z → PENDING.
  Last probe of the S5 family before the final submission.
- **GPU quota now exhausted before the deadline** (weekly limit consumed, remaining 0.00 h; refresh 2026-11-07
  after the competition closes). Therefore NO new version creation is possible: the only remaining
  submissions must use already-COMPLETE versions (v8 S1=14.17, v16 S5=16.25 champion, v22 S6=15.42,
  v23 S5_ens=15.42, v24 S5b=pending, v25 S5_legc=14.17).
- Scoreboard: **S5 16.25 (champion)** > S6 15.42 = S5_ens 15.42 > S1 14.17 = S5_legc 14.17 > CPU probe 0.00.
- Final plan: tonight's (Nov 2 00:01 UTC) submission = best COMPLETE version among {v16 S5 16.25, v24 S5b if it beats it}.
