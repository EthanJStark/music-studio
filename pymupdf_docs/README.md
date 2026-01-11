# PDF → Markdown Conversion (pymupdf4llm)

This folder contains PDF manuals converted to Markdown using [`pymupdf4llm`](https://pypi.org/project/pymupdf4llm/) for LLM-friendly reference with better table/layout preservation than `markitdown`.

## Why pymupdf4llm?

- **Preserves multi-column tables** as Markdown tables (e.g., wavetable lists in Summit manual)
- **Better layout detection** for complex reference manuals
- **Structured page chunks** for targeted reads without loading full manuals

## Structure

- `_raw/`: Raw `pymupdf4llm` output (for debugging/reference)
- `force/`: Akai Force User Guide (417 pages)
  - `force.md`: Full manual with `## Page N` headings
  - `force_chunks/`: 15-page chunks for targeted reads
- `drop/`: Neuzeit Instruments DROP Manual (67 pages)
  - `drop.md`: Full manual
  - `drop_chunks/`: 15-page chunks
- `summit/`: Novation Summit User Guide (62 pages)
  - `summit.md`: Full manual
  - `summit_chunks/`: 15-page chunks

## Regeneration

To re-run the conversion:

```bash
# From repo root (requires pymupdf-venv)
./scripts/convert_pdfs_pymupdf.sh

# With custom chunk size
PAGES_PER_CHUNK=10 ./scripts/convert_pdfs_pymupdf.sh
```

### Setup (first-time only)

```bash
# Create venv + install dependencies
python3 -m venv pymupdf-venv
. pymupdf-venv/bin/activate
pip install --upgrade pip pymupdf pymupdf4llm
```

## Notes

- Page numbers come from `pymupdf4llm`'s page metadata
- Each page gets a canonical `## Page N` heading for easy citation
- Chunks follow the pattern `<name>_p001-015.md` (zero-padded page ranges)
- Tables are rendered as Markdown tables (pipe-separated format)

## Why pymupdf4llm?

Previous conversion attempts (`markitdown`, manual extraction) scrambled multi-column content. For example:

| Previous tools | Wavetables Output |
|------|-------------------|
| `markitdown` / manual | Scrambled list: "BS sine, Random, Zing, Tubey, Octaves..." (wrong order, incomplete) |
| `pymupdf4llm` | Clean table: `\|BS sine\|String\|Glassy\|Spirals\|` (preserves 4-column structure) |
