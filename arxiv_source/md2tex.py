#!/usr/bin/env python3
"""Convert the paper Markdown draft to a self-contained LaTeX source tree (arXiv/Overleaf).

Scope: same constructs as md2typ.py (headings, paragraphs incl. display-formula lines, bullet /
numbered lists, pipe tables, fenced code, blockquotes, rules, images -> figures with captions,
inline code/bold/italic/links; simple `$...$` passthrough; LaTeX-ish math tokens kept literal with
unicode symbols translated to LaTeX commands).

Output: main.tex + figures/ (copied) + README_OVERLEAF.md. This converter is repo-side tooling;
the Overleaf/arXiv upload is just `main.tex` + `figures/`.

Usage:
    python md2tex.py ../paper_planC_draft_v2.md --out-dir . --figures-dir ../figures
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent                  # paper/arxiv_source
PAPER = HERE.parent                                     # paper
PROJECT = PAPER.parent
BUILD = PAPER / "build"
if str(BUILD) not in sys.path and (BUILD / "mdparse.py").is_file():
    sys.path.insert(0, str(BUILD))
import mdparse  # noqa: E402

AUTHOR = "ARC Prize 2026 Paper Track team"
DATE = "18 October 2026"

# punctuation unicode -> plain LaTeX text (no math mode)
UNICODE_TEXT = {
    "–": "--", "—": "---", "…": r"\ldots{}", "·": r"\textperiodcentered{}",
}

# math symbols -> LaTeX math-mode command (wrapped in $...$)
UNICODE_TEX = {
    "−": "-", "√": r"\surd{}", "∈": r"\in{}", "¬": r"\neg{}", "∧": r"\wedge{}",
    "∨": r"\vee{}", "→": r"\to{}", "↦": r"\mapsto{}", "≥": r"\ge{}", "≤": r"\le{}",
    "≈": r"\approx{}", "≠": r"\ne{}", "×": r"\times{}", "ρ": r"\rho{}", "κ": r"\kappa{}",
    "θ": r"\theta{}", "σ": r"\sigma{}", "δ": r"\delta{}", "Δ": r"\Delta{}",
    "Û": r"\hat{U}", "ŷ": r"\hat{y}", "p̂": r"\hat{p}", "ρ̂": r"\hat{\rho}",
    "κ̂": r"\hat{\kappa}", "‖": r"\|", "⊥": r"\perp{}", "∞": r"\infty{}",
    "∼": r"\sim{}", "⊂": r"\subset{}", "α": r"\alpha{}", "β": r"\beta{}",
    "γ": r"\gamma{}", "λ": r"\lambda{}", "μ": r"\mu{}", "Σ": r"\Sigma{}", "∑": r"\sum{}",
    "²": r"{}^{2}", "³": r"{}^{3}", "°": r"^{\circ}",
}
# combining variants written with a separate combining mark in the source
COMBINING = {"p\u0302": r"\hat{p}", "ρ\u0302": r"\hat{\rho}", "κ\u0302": r"\hat{\kappa}",
             "U\u0302": r"\hat{U}", "y\u0302": r"\hat{y}"}

LATEX_ESCAPE = {
    "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
    "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
}


def escape_text(s: str) -> str:
    for comb, rep in COMBINING.items():
        s = s.replace(comb, rep)
    out = []
    for ch in s:
        if ch in LATEX_ESCAPE:
            out.append(LATEX_ESCAPE[ch])
        elif ch in UNICODE_TEXT:
            out.append(UNICODE_TEXT[ch])
        elif ch in UNICODE_TEX:
            out.append("$" + UNICODE_TEX[ch] + "$")
        else:
            out.append(ch)
    return "".join(out)


def mathify_literal(s: str) -> str:
    """Render a literal formula line: wrap in $...$ and translate known unicode operators."""
    parts = []
    for ch in s:
        if ch in UNICODE_TEX and ord(ch) > 127:
            parts.append(" " + UNICODE_TEX[ch] + " ")
        elif ch in LATEX_ESCAPE:
            parts.append(LATEX_ESCAPE[ch])
        else:
            parts.append(ch)
    body = re.sub(r"\\_", "_", "".join(parts))
    return "$" + body.strip() + "$"


def inline_to_tex(segments) -> str:
    parts = []
    for seg in segments:
        kind = seg[0]
        if kind == "text":
            parts.append(escape_text(seg[1]))
        elif kind == "code":
            parts.append(r"\texttt{" + escape_text(seg[1]) + "}")
        elif kind == "math":
            parts.append("$" + seg[1] + "$")
        elif kind == "strong":
            parts.append(r"\textbf{" + inline_to_tex(seg[1]) + "}")
        elif kind == "em":
            parts.append(r"\emph{" + inline_to_tex(seg[1]) + "}")
        elif kind == "link":
            url = seg[2].strip().replace("%", r"\%").replace("#", r"\#")
            parts.append(r"\href{" + url + "}{" + inline_to_tex(seg[1]) + "}")
        else:
            parts.append(escape_text(str(seg[1])))
    return "".join(parts)


def md_inline(s: str) -> str:
    return inline_to_tex(mdparse.inline_segments(s))


def citeify(s: str, n_refs: int) -> str:
    """Replace plain numeric bracket groups (e.g. `[3, 21]`) with \\cite{refN,...}."""
    def rep(m):
        nums = [int(x.strip()) for x in m.group(1).split(",")]
        if nums and all(1 <= n <= n_refs for n in nums):
            return r"\cite{" + ",".join(f"ref{n}" for n in nums) + "}"
        return m.group(0)

    return re.sub(r"\[(\d+(?:\s*,\s*\d+)*)\]", rep, s)


def align_spec(aligns, ncols):
    a = (aligns + ["left"] * ncols)[:ncols]
    return "".join({"left": "l", "right": "r", "center": "c"}[x] for x in a)


def render_body(blocks, figure_dir_name: str, n_refs: int):
    out = []
    stats = {"figures": 0, "tables": 0, "refs": 0, "missing": []}
    in_refs = False
    in_abstract = False

    def close_abstract():
        nonlocal in_abstract
        if in_abstract:
            out.append(r"\end{abstract}")
            in_abstract = False

    for blk in blocks:
        kind = blk.kind
        if kind == "consumed":
            continue
        if kind == "heading":
            if blk.level <= 1:
                continue
            text = md_inline(blk.text)
            if blk.text.strip() == "Abstract":
                out.append(r"\begin{abstract}")
                in_abstract = True
                continue
            close_abstract()
            if blk.text.strip() == "References":
                in_refs = True
                continue  # thebibliography renders its own heading
            cmd = {2: r"\section", 3: r"\subsection", 4: r"\subsubsection"}.get(blk.level, r"\paragraph")
            out.append(f"{cmd}{{{text}}}")
        elif kind == "para":
            text = md_inline(blk.text)
            if blk.banner:
                out.append(r"\begin{quote}\small " + text + r"\end{quote}")
            elif blk.display:
                out.append(r"\begin{center}" + mathify_literal(mdparse.plain_text(
                    mdparse.inline_segments(blk.text))) + r"\end{center}")
            else:
                out.append(citeify(text, n_refs))
        elif kind == "hr":
            out.append(r"\medskip\noindent\hrule\medskip")
        elif kind == "code":
            out.append(r"\begin{verbatim}")
            out.append(blk.text)
            out.append(r"\end{verbatim}")
        elif kind == "quote":
            out.append(r"\begin{quote}" + citeify(md_inline(blk.text), n_refs) + r"\end{quote}")
        elif kind == "list":
            if in_refs and blk.ordered:
                out.append(r"\begin{thebibliography}{99}")
                for i, it in enumerate(blk.items, 1):
                    out.append(rf"\bibitem{{ref{i}}} " + citeify(md_inline(it), n_refs))
                out.append(r"\end{thebibliography}")
                stats["refs"] = len(blk.items)
                in_refs = False
                continue
            env = "enumerate" if blk.ordered else "itemize"
            out.append(f"\\begin{{{env}}}")
            for it in blk.items:
                out.append(r"  \item " + citeify(md_inline(it), n_refs))
            out.append(f"\\end{{{env}}}")
        elif kind == "image":
            base = os.path.basename(blk.path)
            if not (BUILD / "figures" / base).is_file() and not (HERE / figure_dir_name / base).is_file():
                stats["missing"].append(blk.path)
            cap = md_inline(blk.caption or blk.alt or "")
            out.append(r"\begin{figure}[htbp]")
            out.append(r"\centering")
            out.append(rf"\includegraphics[width=0.92\linewidth]{{{figure_dir_name}/{base}}}")
            out.append(rf"\caption*{{{cap}}}")
            out.append(r"\end{figure}")
            stats["figures"] += 1
        elif kind == "table":
            ncols = max(len(r) for r in blk.rows)
            aligns = blk.aligns + ["left"] * (ncols - len(blk.aligns))
            cap = md_inline(blk.caption or "")
            out.append(r"\begin{table}[htbp]")
            out.append(r"\centering")
            if cap:
                out.append(rf"\caption*{{{cap}}}")
            out.append(r"\small")
            if ncols > 3:
                out.append(r"\resizebox{\textwidth}{!}{%")
            out.append(rf"\begin{{tabular}}{{{align_spec(aligns, ncols)}}}")
            out.append(r"\toprule")
            header = [md_inline(c) for c in blk.rows[0]] + [""] * (ncols - len(blk.rows[0]))
            out.append(" & ".join(header) + r" \\")
            out.append(r"\midrule")
            for row in blk.rows[1:]:
                row = [md_inline(c) for c in row] + [""] * (ncols - len(row))
                out.append(" & ".join(row) + r" \\")
            out.append(r"\bottomrule")
            out.append(r"\end{tabular}")
            if ncols > 3:
                out.append(r"}%")
            out.append(r"\end{table}")
            stats["tables"] += 1
        else:
            raise NotImplementedError(kind)
    close_abstract()
    return "\n".join(out) + "\n", stats


def convert(md_text: str, author: str = AUTHOR, date: str = DATE) -> tuple[str, dict]:
    blocks = mdparse.parse_markdown(md_text)
    # Title/subtitle extraction (same rule as md2typ)
    title, subtitle = "", ""
    for idx, blk in enumerate(blocks):
        if blk.kind == "heading" and blk.level == 1 and not title:
            title = mdparse.plain_text(mdparse.inline_segments(blk.text))
            blk.kind = "consumed"
            if idx + 1 < len(blocks):
                nxt = blocks[idx + 1]
                if nxt.kind == "para":
                    segs = mdparse.inline_segments(nxt.text.strip())
                    if len(segs) == 1 and segs[0][0] == "em":
                        subtitle = mdparse.plain_text(segs[0][1])
                        nxt.kind = "consumed"
            break

    # reference count = length of the ordered list after the References heading
    n_refs = 0
    seen_refs = False
    for blk in blocks:
        if blk.kind == "heading" and blk.text.strip() == "References":
            seen_refs = True
            continue
        if seen_refs and blk.kind == "list" and blk.ordered:
            n_refs = len(blk.items)
            break

    body, stats = render_body(blocks, "figures", n_refs)
    stats.update({"title": title, "subtitle": subtitle, "n_refs": n_refs})

    title_tex = escape_text(title) if title else "Untitled"
    sub_tex = escape_text(subtitle) if subtitle else ""
    preamble = r"""% Auto-generated by paper/arxiv_source/md2tex.py — do not edit by hand.
% Compile on Overleaf (pdfLaTeX) or arXiv (pdfLaTeX). See README_OVERLEAF.md.
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=2.4cm]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{hyperref}
\usepackage{microtype}
\usepackage{textcomp}
\hypersetup{colorlinks=true,linkcolor=blue,urlcolor=blue,citecolor=blue}
\captionsetup{font=small,labelfont=bf,justification=raggedright,singlelinecheck=false}
\setlength{\parskip}{0.25em}
\setlength{\parindent}{0em}
"""
    preamble += f"\\title{{{title_tex}"
    if sub_tex:
        preamble += r"\\[0.4em] \large \textit{" + sub_tex + "}"
    preamble += "}\n"
    preamble += f"\\author{{{escape_text(author)}}}\n"
    preamble += f"\\date{{{escape_text(date)}}}\n"
    preamble += "\\begin{document}\n\\maketitle\n\n"
    return preamble + body + "\n\\end{document}\n", stats


FIGURES_DIR = "figures"


def copy_figures(md_text: str, out_dir: Path) -> tuple[list, list]:
    blocks = mdparse.parse_markdown(md_text)
    refs = sorted({b.path.strip() for b in blocks if b.kind == "image"})
    fig_dir = out_dir / FIGURES_DIR
    fig_dir.mkdir(parents=True, exist_ok=True)
    copied, missing = [], []
    for ref in refs:
        base = os.path.basename(ref)
        candidates = [PAPER / ref, PAPER / "figures" / base, PROJECT / ref,
                      PROJECT / "analysis" / "figures" / base]
        src = next((c for c in candidates if c.is_file()), None)
        if src is None:
            missing.append(ref)
            continue
        shutil.copy2(src, fig_dir / base)
        copied.append(base)
    return copied, missing


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("markdown")
    ap.add_argument("--out-dir", default=str(HERE))
    ap.add_argument("--author", default=AUTHOR)
    ap.add_argument("--date", default=DATE)
    args = ap.parse_args(argv)
    md = Path(args.markdown).read_text(encoding="utf-8")
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    tex, stats = convert(md, author=args.author, date=args.date)
    (out_dir / "main.tex").write_text(tex, encoding="utf-8")
    copied, missing = copy_figures(md, out_dir)
    print(f"[md2tex] wrote {out_dir / 'main.tex'} ({len(tex)} bytes); "
          f"{stats['figures']} figures, {stats['tables']} tables, {stats['n_refs']} refs")
    print(f"[md2tex] figures copied: {len(copied)}; missing: {missing}")
    if missing:
        return 1
    # machine-readable summary beside the tex
    (out_dir / "build_summary.json").write_text(json.dumps(
        {**stats, "figures_copied": copied, "missing": missing}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
