# Studio Docs — Start Here

This repo is both:

- a snapshot of **my current electronic music studio setup**, and
- a set of **reference docs/manuals** I use for ideas when building software to run on a Raspberry Pi.

## What I own (current studio)

- **Core brain / sequencing**
  - Akai Force
- **Synths / instruments**
  - Novation Summit
  - Yamaha reface CS
  - Dato Duo
- **Drums**
  - Roland TR-6S
- **Controllers**
  - Akai APC40
  - Novation Impulse 61
- **Audio I/O / mixing / recording**
  - Novation Scarlett 18i20
  - Yamaha MG16XU
  - Zoom L6
- **Compute / MIDI**
  - Raspberry Pi running Patchbox OS
  - TRS MIDI HAT (for the Pi)

## Current primary workflow

Recording midi clips into Force, and recording audio clips of the summit into the force

Summit is the primary midi controller and sound generator

## What I _don’t_ own (reference-only in this repo)

- **Neuzeit Instruments DROP**: manual is included for inspiration only (I don’t own the device).
- **Blokas Midihub**: docs are included for inspiration only (I don’t own the device).

## Where to look in this repo (map)

- **Akai Force manual (owned)**: `pymupdf_docs/force/force_chunks/` (preferred) or `pymupdf_docs/force/force.md` (full)
- **DROP manual (reference-only)**: `pymupdf_docs/drop/drop_chunks/` (preferred) or `pymupdf_docs/drop/drop.md` (full)
- **Novation Summit manual (owned)**: `pymupdf_docs/summit/summit_chunks/` (preferred) or `pymupdf_docs/summit/summit.md` (full)
- **Midihub docs (reference-only)**: `midihub-docs/docs/` (MIDI "pipes" and routing ideas)
- **Patchbox OS / modules (Pi)**: `patchbox-os/`, `patchbox-modules/`
- **MIDI scripting library (Pi / ALSA)**: `pimidipy/`

## How I use these docs (quick workflow)

- **Need to do something on Force**: search within `pymupdf_docs/force/force_chunks/**` first; keep page numbers when you quote.
- **Need a MIDI processing idea**: skim `midihub-docs/docs/**` for a "pipe" that matches the behavior, then re-implement on the Pi.
- **Need to run it headless on the Pi**: prefer Patchbox OS modules/config patterns from `patchbox-os/` / `patchbox-modules/`.

## Next pages to add (suggested)

- **Audio routing**: what’s plugged into the Scarlett vs MG16XU vs Zoom L6, and why
- **MIDI routing**: Force/TR-6S/Summit/reface/Dato/APC40 + Pi TRS MIDI HAT mappings
- **Pi projects**: small, composable services (MIDI router/filter, clock tools, bridge scripts, etc.)
