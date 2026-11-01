# GPU T6/T7 lattice validation

Bound JSON: `analysis/results/gpu_sim/bound_sim_gpu_100m.json` sha `b1117f3812ab5200e544e70c4ef5f12c4a6e46dd0c82edcb26d4d8ab04c8f65c`; alloc JSON: `analysis/results/gpu_sim/alloc_sim_gpu_2m_v2.json` sha `e39cd282796366ae8876e780c8d88856c96e205d9fbee1d33ac4cbec45fa57a8`.

Device: {'gpu': 'NVIDIA TITAN Xp 12288 MiB', 'torch': '2.5.1+cu118', 'cuda': 'cuda', 'measured_fp32_tflops_4096_cubed_20iters': 9.16, 'host': '56 vCPU / 94 GB RAM', 'evidence': 'nvidia-smi; device cuda in alloc JSON; measured matmul benchmark recorded by run lead'}

## T6 bound at 100M instances

- n=100000000, K=8, **violations at 1e-6=0**; at 1e-9: 30063 (0.00030063)
- max bound excess 1.1219501772075091e-07 (float64 round-off); vacuous 0.6506917, non-vacuous 0.3493083
- tightness ratio (cap>0.05) 0.16397747920089945; elapsed 28.29 s

## T7 allocation at 2M tasks

- label-free ceiling 0.7396840577952887, verifier ceiling 1.0, gap 0.2603159422047113
- predicted mean δ 0.26031594220471127; gap=mean δ: True
- identifiable fraction 0.3494485020637512; waterfilling > uniform every rung: True
- verifier-optimal ceiling range [0.00042380211319625877, 0.017967410360780485]; pilot waterfilling below optimal ceiling every rung: True
- v1 `alloc_sim_gpu_2m.json` sha `629de32d69b02f85611f040b600eeccf689f3c389e2ad444ca01ff8d0403042a` is superseded (mislabeled ceiling); v2 used.

| budget | uniform | waterfilling true δ | verifier-optimal ceiling | oracle δ0 uniform | waterfilling / uniform |
| ---: | ---: | ---: | ---: | ---: | ---: |
| C=50 | 0.0000418840 | 0.0003702971 | 0.0004238021 | 0.0000566181 | 8.84× |
| C=100 | 0.0000837636 | 0.0006662492 | 0.0007778636 | 0.0001132302 | 7.95× |
| C=250 | 0.0002093760 | 0.0014184201 | 0.0016846079 | 0.0002830310 | 6.77× |
| C=500 | 0.0004186424 | 0.0024781324 | 0.0029683671 | 0.0005659139 | 5.92× |
| C=1000 | 0.0008368469 | 0.0042833768 | 0.0051670998 | 0.0011312357 | 5.12× |
| C=2500 | 0.0020888406 | 0.0086901032 | 0.0105770923 | 0.0028236591 | 4.16× |
| C=5000 | 0.0041668107 | 0.0146602184 | 0.0179674104 | 0.0056326216 | 3.52× |

## Commands

```bash
python code/lab/gpu_theory_sim.py bound --n 100000000 --out out/bound_sim_gpu_100m.json
python code/lab/gpu_theory_sim.py alloc --n-tasks 2000000 --budget 50 --out out/alloc_sim_gpu_2m_v2.json
```

## Honesty / limits

GPU-scale numerical validation of the T6/T7 implementations on a synthetic channel; not an ARC-AGI-2 measurement, not a competition entry, and not evidence about hidden tasks. The T6 bound itself is analytic; this only checks no finite-precision violations at scale.
