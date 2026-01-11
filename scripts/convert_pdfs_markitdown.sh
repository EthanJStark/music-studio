#!/usr/bin/env bash
set -euo pipefail

# Convert PDFs under `pdf/` to markdown using `markitdown`, then post-process into:
# - a single paged markdown file with `## Page N` headings
# - page-range chunk files (default: 15 pages per chunk)
#
# Output is written to `markitdown_docs/`.

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
IN_DIR="${REPO_ROOT}/pdf"
OUT_ROOT="${REPO_ROOT}/markitdown_docs"
RAW_DIR="${OUT_ROOT}/_raw"
PAGES_PER_CHUNK="${PAGES_PER_CHUNK:-15}"

POSTPROCESS="${REPO_ROOT}/scripts/markitdown_postprocess.py"

mkdir -p "${RAW_DIR}"

slug_for_pdf() {
  local filename="$1"
  case "${filename}" in
    "Force - User Guide - v3.3.pdf") echo "force" ;;
    "Drop_Manual_v1_07.pdf") echo "drop" ;;
    "Summit User Guide 1.1 EN.pdf") echo "summit" ;;
    "summit_peak_2.1_firmware_update_addendum_v1_english_en.pdf") echo "summit_peak_addendum" ;;
    *)
      # Fallback: normalize to something filesystem-friendly.
      echo "${filename%.*}" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/_/g; s/^_+|_+$//g'
      ;;
  esac
}

title_for_slug() {
  local slug="$1"
  case "${slug}" in
    force) echo "Akai Force User Guide v3.3" ;;
    drop) echo "Neuzeit Instruments DROP Manual v1.07" ;;
    summit) echo "Novation Summit User Guide 1.1" ;;
    summit_peak_addendum) echo "Novation Summit/Peak Firmware Update Addendum v2.1" ;;
    *) echo "${slug}" ;;
  esac
}

shopt -s nullglob
pdfs=( "${IN_DIR}"/*.pdf )
if (( ${#pdfs[@]} == 0 )); then
  echo "No PDFs found in: ${IN_DIR}" >&2
  exit 1
fi

for pdf_path in "${pdfs[@]}"; do
  filename="$(basename "${pdf_path}")"
  slug="$(slug_for_pdf "${filename}")"
  title="$(title_for_slug "${slug}")"

  raw_out="${RAW_DIR}/${slug}.raw.md"
  out_dir="${OUT_ROOT}/${slug}"
  full_out="${out_dir}/${slug}.md"
  chunks_dir="${out_dir}/${slug}_chunks"

  mkdir -p "${out_dir}"

  echo "==> Converting: ${filename}"
  markitdown "${pdf_path}" -o "${raw_out}"

  python3 "${POSTPROCESS}" \
    --input "${raw_out}" \
    --output "${full_out}" \
    --chunks-dir "${chunks_dir}" \
    --pages-per-chunk "${PAGES_PER_CHUNK}" \
    --title "${title}" \
    --source-pdf "${pdf_path}"
done

echo ""
echo "Done. Outputs in: ${OUT_ROOT}"

