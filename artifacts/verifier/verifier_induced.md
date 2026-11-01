# Verifier-induced identifiability (T8)

Engine `out/verifier_search_eval.json` sha `493cc629d237d22d6f4d6ac273d942c27eaa02c015e021a065c35caf2fba6c55`; labels `/home/chen/.dsh/ungrouped/arc2026/data/comp/arc-agi_evaluation_solutions.json` sha `84be4f4f39b79e82c36d565fc878830988b094917f052ee7069aef30b33ca8f1` (evaluation only).

## Full eval120 verifier

- Unique-verified coverage: **0/120 = 0.0%**
- Top-2 class coverage: 0.0%
- Attempt-1 precision: {'n_unique_tasks': 0, 'n_unique_exact': 0}
- Empty acceptance depth≤3: 120/120 (1.0)
- CPU total 35.05 min; mean 0.292 min/task; depth counts {'0': 0, '1': 0, '2': 0, '3': 0}

## F1a / F1b

- F1a: {'n_tasks_with_field': 0, 'total_violations': None, 'n_tasks_with_accepted': 0, 'verdict': 'PASS (vacuous: no accepted programs to re-verify)'}
- F1b d=1: {'depth': 1, 'n_unique': 0, 'n_exact': 0, 'phi': None, 'wilson80': [None, None], 'verdict': 'INCONCLUSIVE (no unique-class tasks)', 'wrong_examples': []}
- F1b d=2: {'depth': 2, 'n_unique': 0, 'n_exact': 0, 'phi': None, 'wilson80': [None, None], 'verdict': 'INCONCLUSIVE (no unique-class tasks)', 'wrong_examples': []}
- F1b d=3: {'depth': 3, 'n_unique': 0, 'n_exact': 0, 'phi': None, 'wilson80': [None, None], 'verdict': 'INCONCLUSIVE (no unique-class tasks)', 'wrong_examples': []}

## Cost curve

| depth | coverage % | CPU min | marginal pp/min |
| :--- | ---: | ---: | ---: |
| 0 | 0.0 | 0.0 | None |
| 1 | 0.0 | 0.65 | 0.0 |
| 2 | 0.0 | 35.05 | 0.0 |
| 3 | 0.0 | 35.05 | None |

## Joint 20-task hybrid (exploratory)

| TTT | verifier-only | TTT top2 | hybrid | grid overlap | F2 verdict |
| :--- | ---: | ---: | ---: | ---: | :--- |
| S1 | 0/20 (0.0%) | 4/20 (20.0%) | 4/20 (20.0%) | 0.0 | {'mean_H_minus_V_pp': 20.0, 'ci80_H_minus_V_pp': [10.0, 30.0], 'mean_H_minus_T_pp': 0.0, 'ci80_H_minus_T_pp': [0.0, 0.0], 'verdict': 'FAIL'} |
| S5 | 0/20 (0.0%) | 3/20 (15.0%) | 3/20 (15.0%) | 0.0 | {'mean_H_minus_V_pp': 15.0, 'ci80_H_minus_V_pp': [5.0, 25.0], 'mean_H_minus_T_pp': 0.0, 'ci80_H_minus_T_pp': [0.0, 0.0], 'verdict': 'FAIL'} |
| S5_ens | 0/8 (0.0%) | 2/8 (25.0%) | 2/8 (25.0%) | 0.0 | {'mean_H_minus_V_pp': 25.0, 'ci80_H_minus_V_pp': [0.0, 50.0], 'mean_H_minus_T_pp': 0.0, 'ci80_H_minus_T_pp': [0.0, 0.0], 'verdict': 'FAIL'} |

## eval120 vs train control (n=12 positive control)

| run | n tasks | accepted | unique | unique coverage | certificate empty | mean CPU min |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| eval120 | 120 | 0 | 0 | 0.0% | 1.0 | 0.292 |
| train control | 12 | 1 | 1 | 8.33% | 0.9167 | 0.1 |

## Null / control runs

| run | n | accepted | unique | elapsed | note |
| :--- | ---: | ---: | ---: | ---: | :--- |
| learned_rules | 120 | 0 | 0 | 0.3 | learned-rule families |
| llm_chat20 | 20 | 0 | 0 | 57.2 | DeepSeek-chat k=4, 20 eval tasks |
| llm_reasoner10 | 10 | 0 | 0 | 266.3 | every completion truncated at token cap; recorded as infrastructure null, not evidence about verifier capability |

## F3

{'testable_tasks': 120, 'nestedness_violations': [], 'nestedness_ok': True, 'nestedness_truncated_tasks': [], 'growth_tasks': 0, 'growth_frac': 0.0, 'growth_examples': [], 'flat_tasks': 120, 'verdict': 'FAIL (acceptance flat across all depths)', 'max_depth_measured': 2, 'depth3_status': 'not measured (max_depth=2)'}

## Honesty / limits

Public eval120 only, not hidden. Labels used for evaluation only; verifier search is label-free. This is not a submitted competition entry. TTT pools are 20-task dev20 subsets, so the joint/hybrid table is exploratory; full-eval verifier numbers are separate. Attempt-2 rule is frozen as in theory_v6 §5.
