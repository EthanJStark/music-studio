# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Start Here

See `START_HERE.md` for a complete map of the repo, including what devices are owned vs reference-only.

## Repository Overview

This repository is both:
- A snapshot of the user's **current electronic music studio setup**
- A set of **reference documentation** for building MIDI/audio software on Raspberry Pi

### Owned Devices (Current Studio)
- **Akai Force** - Main sequencer/brain (`claude_docs/force_chunks/` or `claude_docs/force.md`)
- **Raspberry Pi** - Running Patchbox OS with TRS MIDI HAT (`patchbox-os/`, `patchbox-modules/`, `pimidipy/`)
- Various synths, drums, controllers, and audio interfaces (see START_HERE.md)

### Reference-Only Documentation (Not Owned)
- **DROP Manual** (Neuzeit Instruments) - `claude_docs/drop_chunks/` or `claude_docs/drop.md` - For inspiration only
- **Midihub Documentation** (Blokas Labs) - `midihub-docs/` git submodule - For MIDI processing ideas only

## Quick Workflow

### Working with Force (Owned Device)
- Search within `claude_docs/force_chunks/**` first for specific topics
- Open the smallest chunk containing the topic (prefer `*_chunks/` over full `.md` files)
- Quote page numbers from headings when answering questions
- Avoid loading full `force.md` when chunks suffice

### MIDI Processing Ideas (Reference-Only)
- Skim `midihub-docs/docs/**` for "pipes" that match desired behavior
- Use these as inspiration for implementing on Raspberry Pi

### Raspberry Pi / Patchbox OS
- `patchbox-os/` - OS configuration and system patterns
- `patchbox-modules/` - Modular audio/MIDI service examples
- `pimidipy/` - Python library for MIDI scripting with ALSA

### DROP Manual (Reference-Only)
- Search within `claude_docs/drop_chunks/**` for inspiration
- Prefer chunks over full `drop.md` file

See `claude_docs/CLAUDE.md` for more detailed guidance on the DROP and Force manuals.

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

### claude_docs/
- `force.md` - Full Akai Force manual (owned device)
- `force_chunks/` - Force manual split into smaller chunks (preferred for LLM context)
- `drop.md` - Full DROP manual (reference-only)
- `drop_chunks/` - DROP manual split into smaller chunks (preferred for LLM context)
- `.jsonl` files - Structured data for each manual

### midihub-docs/ (Reference-Only)
- `docs/` - Markdown documentation files
- `mkdocs.yml` - MkDocs configuration
- Organized by device features and "pipes" (MIDI processing modules)

### Raspberry Pi / Patchbox OS
- `patchbox-os/` - Patchbox OS configuration and system patterns
- `patchbox-modules/` - Modular audio/MIDI service examples for headless Pi operation
- `pimidipy/` - Python library for MIDI scripting with ALSA on the Pi
