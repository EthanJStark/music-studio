# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains documentation for audio/MIDI devices in LLM-friendly formats:

- **DROP Manual** (Neuzeit Instruments) - `claude_docs/drop.md` and `claude_docs/drop_chunks/`
- **Force User Guide** (Akai v3.3) - `claude_docs/force.md` and `claude_docs/force_chunks/`
- **Midihub Documentation** (Blokas Labs) - `midihub-docs/` git submodule

## Working with Device Manuals

See `claude_docs/CLAUDE.md` for detailed guidance on using the DROP and Force manuals.

Quick reference:
- Search within `claude_docs/**` for relevant keywords first
- Open the smallest chunk containing the topic (prefer `*_chunks/` over full `.md` files)
- Quote page numbers from headings when answering questions
- Avoid loading full manuals when chunks suffice

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
- `drop.md` / `force.md` - Full manuals in single files
- `drop_chunks/` / `force_chunks/` - Manuals split into smaller chunks (preferred for LLM context)
- `.jsonl` files - Structured data for each manual

### midihub-docs/
- `docs/` - Markdown documentation files
- `mkdocs.yml` - MkDocs configuration
- Organized by device features and "pipes" (MIDI processing modules)
