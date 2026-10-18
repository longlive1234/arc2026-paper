# GitHub README summary (public, plain language)

Companion to `paper/paper_planC_draft_v2.md`. Short public-facing text for the repository README:
**(A)** a 250-word plain-language summary and **(B)** a three-sentence "what we learned" block.

---

## A. What this repository and paper are about (250 words)

ARC-AGI-2 gives two answers per test input and counts a task solved only if one is exactly right on all inputs. We study which two answers to submit from grids produced by a test-time-trained model. We formalize this as coverage optimization: choose two distinct candidates maximizing P(at least one is exactly correct). When candidate errors are independent, the best pair is the two with highest calibrated correctness probabilities, in either order. Duplicating a grid is strictly worse than any different candidate that could be right. When candidates share error modes, as they do from one model or decoding run, maximizing the single best guess is not optimal: a decorrelated second guess can cover more. We test the theory on real candidate pools from public ARC solvers under a pre-registered protocol. The simulation behaves as predicted: 41.7% for the coverage rule vs 16.7% for top-candidate-twice and 23.3% for top-two. On 400 ARC-AGI-1 tasks with 34.2% oracle coverage, the solver's own top-two reaches 20.0%, while our calibrated coverage rule reaches 17.8% — no better than duplicate submission. The oracle gap is real but not reachable by re-ranking exposed metadata. On a small ARC-AGI-2 pilot every rule ties at the 31.2% ceiling. The conclusion is a bounded negative result: selection is not the bottleneck; generation is. Two attempts are not two chances unless the pool contains genuinely independent evidence. We release the theory, protocol, benchmark, data characterization and a CPU-validated offline TTT system under MIT-0, documenting the platform restrictions that prevented GPU runs.

*(Word count: 250.)*

## B. What we learned (three sentences)

First, the two-attempt ARC format is a coverage problem, and standard top-two ranking is not coverage-optimal when candidate errors correlate. Second, on real public solver pools the solver's own score ordering already captures essentially all two-attempt coverage that re-ranking can reach: on 400 CompressARC tasks a calibrated coverage rule scored 17.8% against 20.0% for the solver's top-two, despite 34.2% oracle coverage. Third, selection is therefore not the current bottleneck — candidate generation and coverage are — and this release contains the theory, the pre-registered negative result, the benchmark artifacts, and a CPU-validated MIT-0 pipeline, while a GPU run remains platform-gated.
