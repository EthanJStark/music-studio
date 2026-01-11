# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Start Here

See `START_HERE.md` for a complete map of the repo, including what devices are owned vs reference-only.

## Repository Overview

This repository is both:

- A snapshot of the user's **current electronic music studio setup**
- A set of **reference documentation** for building MIDI/audio software on Raspberry Pi

### Owned Devices (Current Studio)

- **Akai Force** - Main sequencer/brain (`pymupdf_docs/force/force_chunks/` or `pymupdf_docs/force/force.md`)
- **Novation Summit** - Synthesizer (`pymupdf_docs/summit/summit_chunks/` or `pymupdf_docs/summit/summit.md`)
- **Raspberry Pi** - Running Patchbox OS with TRS MIDI HAT (`patchbox-os/`, `patchbox-modules/`, `pimidipy/`)
- Various synths, drums, controllers, and audio interfaces (see START_HERE.md)

### Reference-Only Documentation (Not Owned)

- **DROP Manual** (Neuzeit Instruments) - `pymupdf_docs/drop/drop_chunks/` or `pymupdf_docs/drop/drop.md` - For inspiration only
- **Midihub Documentation** (Blokas Labs) - `midihub-docs/` git submodule - For MIDI processing ideas only

## Quick Workflow

### Working with Device Manuals (Owned Devices)

- Search within `pymupdf_docs/<device>/<device>_chunks/**` first for specific topics
- Open the smallest chunk containing the topic (prefer `*_chunks/` over full `.md` files)
- Quote page numbers from headings when answering questions
- Avoid loading full `.md` files when chunks suffice
- Available manuals: Force (`pymupdf_docs/force/force_chunks/`), Summit (`pymupdf_docs/summit/summit_chunks/`)

### MIDI Processing Ideas (Reference-Only)

- Skim `midihub-docs/docs/**` for "pipes" that match desired behavior
- Use these as inspiration for implementing on Raspberry Pi

### Raspberry Pi / Patchbox OS

- `patchbox-os/` - OS configuration and system patterns
- `patchbox-modules/` - Modular audio/MIDI service examples
- `pimidipy/` - Python library for MIDI scripting with ALSA

### DROP Manual (Reference-Only)

- Search within `pymupdf_docs/drop/drop_chunks/**` for inspiration
- Prefer chunks over full `drop.md` file

## Midihub Documentation (Git Submodule)

The `midihub-docs/` directory is a git submodule pointing to https://github.com/BlokasLabs/midihub-docs.git

### Serving Documentation Locally

```bash
# Install dependencies (requires Python 3.5+)
pip install mkdocs mkdocs-material mkdocs-redirects

# Serve documentation
cd midihub-docs
mkdocs serve
```

The documentation will be available at http://localhost:8000

### Submodule Management

```bash
# Initialize submodule after clone
git submodule update --init --recursive

# Update submodule to latest
cd midihub-docs
git pull origin main
cd ..
git add midihub-docs
git commit -m "Update midihub-docs submodule"
```

## Documentation Structure

### pymupdf_docs/

- `force/force.md` + `force/force_chunks/` - Force manual (417 pages)
- `drop/drop.md` + `drop/drop_chunks/` - DROP manual (67 pages)
- `summit/summit.md` + `summit/summit_chunks/` - Summit manual (62 pages)
- `_raw/` - Raw `pymupdf4llm` output (debugging)
- **Tables preserved as Markdown tables** (better than previous conversions)

### midihub-docs/ (Reference-Only)

- `docs/` - Markdown documentation files
- `mkdocs.yml` - MkDocs configuration
- Organized by device features and "pipes" (MIDI processing modules)

### Raspberry Pi / Patchbox OS

- `patchbox-os/` - Patchbox OS configuration and system patterns
- `patchbox-modules/` - Modular audio/MIDI service examples for headless Pi operation
- `pimidipy/` - Python library for MIDI scripting with ALSA on the Pi
