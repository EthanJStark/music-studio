#!/usr/bin/env python3
"""
Convert a PDF to Markdown using pymupdf4llm, then split into page-chunked files.

Usage:
  python3 pymupdf_convert.py --pdf <path> --output-dir <dir> --slug <name> [--pages-per-chunk N]
"""
import argparse
import os
import re
import sys
from pathlib import Path

try:
    import pymupdf4llm
except ImportError:
    print("ERROR: pymupdf4llm not installed. Run:")
    print("  pip install pymupdf4llm")
    sys.exit(1)


def extract_pages_from_markdown(md_text: str) -> list[tuple[int, str]]:
    """
    Parse pymupdf4llm markdown output with page separators into (page_num, content) tuples.
    
    pymupdf4llm with page_chunks=True outputs markdown like:
    
        -----
        
        # Page 1
        
        content...
        
        -----
        
        # Page 2
        
        content...
    
    Returns:
        List of (page_number, page_content_markdown) tuples (1-indexed).
    """
    pages = []
    # Split on "-----" separators (pymupdf4llm page delimiters)
    chunks = re.split(r'^-{5,}$', md_text, flags=re.MULTILINE)
    
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk:
            continue
        
        # Look for "# Page N" at the start
        match = re.match(r'^#\s+Page\s+(\d+)', chunk, re.IGNORECASE)
        if match:
            page_num = int(match.group(1))
            # Remove the "# Page N" heading itself (we'll re-add it in a canonical format)
            content = re.sub(r'^#\s+Page\s+\d+\s*\n', '', chunk, count=1).strip()
            pages.append((page_num, content))
        else:
            # If there's no page heading but there's content, treat it as a continuation
            # (shouldn't happen with page_chunks=True, but be defensive)
            if chunk:
                # Try to infer page number from previous
                prev_page = pages[-1][0] if pages else 0
                pages.append((prev_page + 1, chunk))
    
    return pages


def main():
    parser = argparse.ArgumentParser(description="Convert PDF to Markdown using pymupdf4llm")
    parser.add_argument("--pdf", required=True, help="Path to input PDF")
    parser.add_argument("--output-dir", required=True, help="Output directory (will create slug subdirs)")
    parser.add_argument("--slug", required=True, help="Short name for this manual (e.g., 'force', 'summit')")
    parser.add_argument("--pages-per-chunk", type=int, default=15, help="Pages per chunk file")
    args = parser.parse_args()
    
    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"ERROR: PDF not found: {pdf_path}")
        sys.exit(1)
    
    output_dir = Path(args.output_dir)
    slug = args.slug
    pages_per_chunk = args.pages_per_chunk
    
    # Create output structure: output_dir/slug/slug.md + slug_chunks/
    slug_dir = output_dir / slug
    slug_dir.mkdir(parents=True, exist_ok=True)
    chunks_dir = slug_dir / f"{slug}_chunks"
    chunks_dir.mkdir(exist_ok=True)
    raw_dir = output_dir / "_raw"
    raw_dir.mkdir(exist_ok=True)
    
    # Convert PDF → Markdown with page chunks
    print(f"  → Extracting markdown from {pdf_path.name}...")
    page_chunks_data = pymupdf4llm.to_markdown(
        str(pdf_path),
        page_chunks=True,          # Returns list of dicts with 'metadata' and 'text'
        page_width=612,            # Standard letter width
        table_strategy="lines_strict",  # Best for structured tables
        ignore_code=False,
        show_progress=False,
    )
    
    # page_chunks=True returns a list of {"metadata": {...}, "text": "..."} dicts
    # Rebuild into (page_num, content) tuples
    pages = []
    if isinstance(page_chunks_data, list):
        for chunk in page_chunks_data:
            if isinstance(chunk, dict):
                page_num = chunk.get("metadata", {}).get("page", len(pages) + 1)
                text = chunk.get("text", "").strip()
                if text:
                    pages.append((page_num, text))
    else:
        # Fallback: if it returned a string (shouldn't happen with page_chunks=True)
        md_text = page_chunks_data
        pages = extract_pages_from_markdown(md_text)
    
    # Save raw output for debugging (reconstruct full text)
    raw_md = "\n\n-----\n\n".join(f"# Page {pn}\n\n{txt}" for pn, txt in pages)
    raw_path = raw_dir / f"{slug}.raw.md"
    raw_path.write_text(raw_md, encoding="utf-8")
    print(f"  → Wrote raw markdown: {raw_path}")
    if not pages:
        print(f"WARNING: No pages detected in {pdf_path.name}")
        sys.exit(1)
    
    total_pages = max(p[0] for p in pages)
    print(f"  → Detected {len(pages)} page chunks (total pages: {total_pages})")
    
    # Build full markdown with canonical "## Page N" headings
    pdf_basename = pdf_path.name
    title = pdf_basename.replace(".pdf", "").replace("_", " ").title()
    
    full_md_lines = [
        f"# {title}",
        "",
        f"> Converted from PDF using `pymupdf4llm`. Source: `{pdf_path.resolve()}`.",
        "",
    ]
    
    for page_num, content in pages:
        full_md_lines.append("---")
        full_md_lines.append("")
        full_md_lines.append(f"## Page {page_num}")
        full_md_lines.append("")
        full_md_lines.append(content)
        full_md_lines.append("")
    
    full_md = "\n".join(full_md_lines)
    full_path = slug_dir / f"{slug}.md"
    full_path.write_text(full_md, encoding="utf-8")
    print(f"  → Wrote full markdown: {full_path} ({total_pages} pages)")
    
    # Split into chunks
    chunk_num = 0
    chunk_start = 1
    while chunk_start <= total_pages:
        chunk_end = min(chunk_start + pages_per_chunk - 1, total_pages)
        chunk_num += 1
        
        chunk_pages = [(pn, pc) for pn, pc in pages if chunk_start <= pn <= chunk_end]
        if not chunk_pages:
            break
        
        chunk_md_lines = [
            f"# {title} (Pages {chunk_start}-{chunk_end})",
            "",
            f"> Converted from PDF using `pymupdf4llm`. Source: `{pdf_path.resolve()}`.",
            "",
        ]
        
        for page_num, content in chunk_pages:
            chunk_md_lines.append("---")
            chunk_md_lines.append("")
            chunk_md_lines.append(f"## Page {page_num}")
            chunk_md_lines.append("")
            chunk_md_lines.append(content)
            chunk_md_lines.append("")
        
        chunk_md = "\n".join(chunk_md_lines)
        chunk_filename = f"{slug}_p{chunk_start:03d}-{chunk_end:03d}.md"
        chunk_path = chunks_dir / chunk_filename
        chunk_path.write_text(chunk_md, encoding="utf-8")
        
        chunk_start = chunk_end + 1
    
    print(f"  → Wrote {chunk_num} chunk files to {chunks_dir}")


if __name__ == "__main__":
    main()
