# Official-truth check for Dataset B (Table 2)

*Generated 2026-10-20 by paper-writer from the frozen benchmark artifact and the official competition files; no model runs.*

**Question.** Dataset B's selection benchmark attached truth from the repo-mirror public-eval files (167 inputs). The official competition files have 120 tasks / 172 inputs and differ on five tasks. Does this change any Table 2 B number?

B tasks checked: 20; repo/official differences found: 1.

**Result.** The only differing task present in Dataset B is `abc82100` (repo: 1 test input; official: 2, with an extra input prepended). Every other B task has identical repo/official test inputs and truth hashes. For `abc82100`'s only decoded pool unit (`abc82100_0`), 15 candidate files were decoded (18 samples); canonical grid deduplication yields **11 unique candidate grids**, and none matches the repo truth (`a0b31eef944bc3f8`), the official index-0 truth (`9fa8e6d4bcc5b007`) or the official index-1 truth (`a0b31eef944bc3f8`). Therefore the correct-candidate set for that unit is empty under every possible truth assignment, every rule contributes zero coverage for it, and all Dataset B rule metrics (oracle 31.25%, duplicate/argmax/top2/cal_indep/coverage 31.25%, deployed 25.00%) are unchanged.

**Artifacts and commands.**
```
python analysis/selection_benchmark.py   # frozen artifact analysis/results/selection_benchmark.json
sha256sum analysis/results/selection_benchmark.json  # 6c16abfef7f0efe3a1a6bbe9f6251c9aeef1893ee7b0f44fdfdb9c2eb34ab71a
# official files: data/comp/arc-agi_evaluation_{challenges,solutions}.json
```

**Status.** Table 2 unchanged. Confirmed by the formal official-truth rerun `analysis/results/selection_benchmark_official.json`, sha256 `cb8308448f78ed5064a8f13827ef9117908184cf5b6354f591cffa1951552df0` (`python analysis/selection_benchmark.py --truth-mode official`; evidence row C55), delivered 2026-10-20: B split, oracle, all rule values, deployed value, deltas and calibration are identical to the frozen artifact. This note records the independent pre-rerun check (2026-10-20).
