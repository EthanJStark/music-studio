#!/usr/bin/env bash
set -euo pipefail

# Convert PDFs → Markdown using pymupdf4llm (better table/layout handling than markitdown)
#
# Usage:
#   ./scripts/convert_pdfs_pymupdf.sh
#
# Optional env vars:
#   PAGES_PER_CHUNK=15   # How many pages per chunk file (default: 15)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
PDF_DIR="$REPO_ROOT/pdf"
OUT_DIR="$REPO_ROOT/pymupdf_docs"
VENV_DIR="$REPO_ROOT/pymupdf-venv"
PAGES_PER_CHUNK="${PAGES_PER_CHUNK:-15}"

# Ensure venv exists
if [ ! -d "$VENV_DIR" ]; then
  echo "ERROR: pymupdf-venv not found. Run:"
  echo "  python3 -m venv pymupdf-venv"
  echo "  . pymupdf-venv/bin/activate"
  echo "  pip install --upgrade pip pymupdf pymupdf4llm"
  exit 1
fi

# Activate venv
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

# Convert each PDF
for pdf_path in "$PDF_DIR"/*.pdf; do
  [ -e "$pdf_path" ] || continue
  pdf_name="$(basename "$pdf_path" .pdf)"
  
  # Slugify: "Force - User Guide - v3.3" → "force"
  slug="$(echo "$pdf_name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9_-]/_/g' | sed 's/_*-_*/_/g' | sed 's/^_//;s/_$//' | sed 's/__*/_/g' | cut -d'_' -f1)"
  
  echo "==> Converting: $pdf_name (slug: $slug)"
  
  python3 "$SCRIPT_DIR/pymupdf_convert.py" \
    --pdf "$pdf_path" \
    --output-dir "$OUT_DIR" \
    --slug "$slug" \
    --pages-per-chunk "$PAGES_PER_CHUNK"
done

echo ""
echo "Done. Outputs in: $OUT_DIR"
