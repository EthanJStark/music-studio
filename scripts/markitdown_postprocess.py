#!/usr/bin/env python3
"""
Post-process `markitdown` Markdown output into:
- a single "paged" markdown file with `## Page N` headings
- optional page-range chunk files (e.g., *_p001-015.md)

We infer page breaks from form-feed characters (\\f / U+000C), which `markitdown`
commonly emits when converting PDFs.
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Page:
    number: int
    text: str


def _read_text(path: Path) -> str:
    # markitdown output should be UTF-8, but be resilient.
    return path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")


def _split_pages(markdown: str) -> list[str]:
    # Normalize any literal U+000C into '\f' (Python already represents it this way).
    parts = markdown.split("\f")
    # Keep relative spacing inside each page, but trim outer whitespace.
    pages = [p.strip() for p in parts]
    # Filter empty pages.
    return [p for p in pages if p]


def _render_full(title: str, pages: list[Page], source_pdf: str | None) -> str:
    header = [f"# {title}", ""]
    meta = "> Converted from PDF using `markitdown`; pages inferred from PDF form-feed markers."
    if source_pdf:
        meta += f" Source: `{source_pdf}`."
    header += [meta, "", "---", ""]

    out: list[str] = header
    for p in pages:
        out += [f"## Page {p.number}", "", p.text, "", "---", ""]
    return "\n".join(out).rstrip() + "\n"


def _chunk_ranges(total_pages: int, pages_per_chunk: int) -> list[tuple[int, int]]:
    if total_pages <= 0:
        return []
    ranges: list[tuple[int, int]] = []
    start = 1
    while start <= total_pages:
        end = min(total_pages, start + pages_per_chunk - 1)
        ranges.append((start, end))
        start = end + 1
    return ranges


def _render_chunk(
    title: str,
    pages: list[Page],
    start: int,
    end: int,
    source_pdf: str | None,
) -> str:
    header = [f"# {title} (Pages {start}-{end})", ""]
    meta = "> Converted from PDF using `markitdown`; pages inferred from PDF form-feed markers."
    if source_pdf:
        meta += f" Source: `{source_pdf}`."
    header += [meta, "", "---", ""]

    out: list[str] = header
    for p in pages:
        if start <= p.number <= end:
            out += [f"## Page {p.number}", "", p.text, "", "---", ""]
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Post-process markitdown markdown into paged + chunks.")
    parser.add_argument("--input", required=True, help="Input markdown file produced by markitdown.")
    parser.add_argument("--output", required=True, help="Output markdown file with ## Page N headings.")
    parser.add_argument("--chunks-dir", required=False, help="If set, write page-range chunks into this dir.")
    parser.add_argument("--pages-per-chunk", type=int, default=15, help="Pages per chunk (default: 15).")
    parser.add_argument("--title", required=False, help="Title for the output markdown H1.")
    parser.add_argument("--source-pdf", required=False, help="Optional source PDF path to include in header.")
    args = parser.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)
    chunks_dir = Path(args.chunks_dir) if args.chunks_dir else None

    raw = _read_text(in_path)
    page_texts = _split_pages(raw)
    title = args.title or in_path.stem

    pages = [Page(i + 1, t) for i, t in enumerate(page_texts)]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(_render_full(title, pages, args.source_pdf), encoding="utf-8")

    if chunks_dir:
        chunks_dir.mkdir(parents=True, exist_ok=True)
        for start, end in _chunk_ranges(len(pages), max(1, args.pages_per_chunk)):
            chunk_name = f"{out_path.stem}_p{start:03d}-{end:03d}.md"
            chunk_path = chunks_dir / chunk_name
            chunk_path.write_text(
                _render_chunk(title, pages, start, end, args.source_pdf),
                encoding="utf-8",
            )

    rel_in = os.fspath(in_path)
    rel_out = os.fspath(out_path)
    print(f"Wrote paged markdown: {rel_out} (pages: {len(pages)}) from {rel_in}")
    if chunks_dir:
        print(f"Wrote chunks: {os.fspath(chunks_dir)} (pages_per_chunk: {args.pages_per_chunk})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

