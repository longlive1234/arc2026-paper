# Overleaf / arXiv LaTeX source — README

**Status: generated, NOT compiled locally** (this machine has no TeX installation). The Typst build of
the same Markdown draft (`paper/build/build_paper.py` → `paper/paper.pdf`) is the verified PDF.
Compile this LaTeX source on Overleaf and iterate on any errors there.

## What to upload

Upload these to Overleaf (or to arXiv as the source archive):

```
main.tex            # the whole paper, generated from paper/paper_planC_draft_v2.md
figures/            # 8 PNGs referenced by main.tex
```

`md2tex.py` and `build_summary.json` are repo-side tooling/provenance and are **not** needed for
compilation. `figures/` must keep its name; `main.tex` references `figures/<name>.png`.

## How to compile on Overleaf

1. New Project → Upload Project, upload `main.tex` + `figures/` (or zip them).
2. Menu → Compiler: **pdfLaTeX** (default). No shell-escape, no extra fonts needed.
3. Compile twice (references/citations need a second pass).
4. Known things to check in the log and fix if needed (these are the only places where the
   generator's "literal text" policy can bite):
   - **Wide tables**: tables with >3 columns are wrapped in `\resizebox{\textwidth}{!}{...}`.
     If a table still overflows or looks too small, replace `\resizebox` with `\small` + `\setlength`
     or split the table. Tables 1 and 4 are the widest (6 and 5 columns).
   - **Literal formulas**: the draft keeps math as literal text. Display formulas are wrapped in
     `$...$` with unicode operators translated (`\neg`, `\wedge`, `\surd`, `\rho`, ...). If a
     formula line trips LaTeX, wrap the offending text in `\texttt{...}` or split it; do not try to
     fully typeset it.
   - **Captions**: manual numbers are preserved with `\caption*{}` (requires the `caption` package,
     already in the preamble). Keep them; the draft's numbering is intentionally non-sequential.
   - **Unused bibliography entries**: the References list has 25 items but 4 are uncited
     (`ref16`–`ref19`). LaTeX will warn/skip them; remove them before submission if the venue
     requires all references cited (`\cite` any or delete the `\bibitem`).
   - `\texttt{DOWNGRADE\_TO\_ANALYSIS}` etc. are escaped and should compile as-is.
5. Expected output: ~17–20 pages, 8 figures, 6 tables.

## Conversion mapping (for auditing)

| Markdown | LaTeX |
| :--- | :--- |
| `# Title` | `\title{...}` (+ italic subtitle from the following `*...*` line) |
| `## Section` / `### Sub` | `\section` / `\subsection` (Abstract → `abstract` env; References → `thebibliography`) |
| `**bold**` / `*italic*` / `` `code` `` | `\textbf` / `\emph` / `\texttt` |
| `[text](url)` | `\href{url}{text}` |
| `[1, 2]` in body text | `\cite{ref1,ref2}` (only groups of integers that index the 25 `\bibitem`s; decimal bracket groups are left literal) |
| pipe tables | `table` + `booktabs` `tabular` (header bold via `\toprule/\midrule`), caption via `\caption*` |
| `![alt](path)` + following `**Figure N.** …` | `figure` + `\includegraphics[width=0.92\linewidth]` + `\caption*` |
| fenced code | `verbatim` |
| `> quote` | `quote` env |
| `---` | `\hrule` |

## Regenerating

```bash
python paper/arxiv_source/md2tex.py paper/paper_planC_draft_v2.md --out-dir paper/arxiv_source
```

Do not edit `main.tex` by hand for content changes — edit the Markdown and regenerate (hand edits are
fine for compile fixes, but note them in the PR/issue so the next regeneration keeps them).
