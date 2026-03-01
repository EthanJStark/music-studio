# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Studio Context

@START_HERE.md

## Working with Device Documentation

### Owned Device Manuals (Force, Summit)

- **IMPORTANT:** Always search chunks first — `pymupdf_docs/<device>/<device>_chunks/**` — not the full `.md` files
- Full manuals are very large; open only the smallest chunk that answers the question
- Quote page numbers from headings when answering questions
- Available: Force (`pymupdf_docs/force/force_chunks/`), Summit (`pymupdf_docs/summit/summit_chunks/`)

### Reference-Only Documentation (Midihub, DROP)

- **IMPORTANT:** These devices are not owned — use docs for inspiration only, not as instructions for owned hardware
- Midihub "pipes": `midihub-docs/docs/**` — MIDI processing ideas to re-implement on Raspberry Pi
- DROP manual: `pymupdf_docs/drop/drop_chunks/**`

### Raspberry Pi / Patchbox OS

- `patchbox-os/` - OS configuration and system patterns
- `patchbox-modules/` - Modular audio/MIDI service examples for headless operation
- `pimidipy/` - Python library for MIDI scripting with ALSA
