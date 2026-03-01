# Studio Connections

Current wiring and signal-flow snapshot.

---

## MIDI Routing

All USB-MIDI connections run through the **Akai Force** as the central hub.

| Device | Connection | Direction | Notes |
|---|---|---|---|
| Novation Summit | USB MIDI (Force ↔ Summit) | Bidirectional | Force sequences Summit; Summit also acts as primary keyboard controller sending notes/CCs back to Force |
| Novation Impulse 61 | USB MIDI (Force ↔ Impulse) | Bidirectional | Impulse is a keyboard controller; sends notes/CCs to Force. Bidirectional allows Force to control Impulse's motorized faders / pad lights |

### Devices not yet mapped

The following owned devices are not yet documented with specific MIDI routing:

- Roland TR-6S (drums)
- Yamaha reface CS
- Dato Duo
- Akai APC40
- Raspberry Pi (TRS MIDI HAT)

---

## Audio Routing

The **Focusrite Scarlett 18i20** is the Force's audio interface.

| Device | Connection | Notes |
|---|---|---|
| Akai Force | USB audio → Scarlett 18i20 | Force uses Scarlett as its primary audio I/O |

### Devices not yet mapped

- Novation Summit (audio outputs → ?)
- Roland TR-6S (audio outputs → ?)
- Yamaha MG16XU (mixer role TBD)
- Zoom L6 (recorder role TBD)
- Yamaha reface CS
- Dato Duo

---

## Docs Reference

| Device | Manual location |
|---|---|
| Novation Impulse 61 | `pymupdf_docs/impulse/impulse_chunks/` |
| Novation Summit | `pymupdf_docs/summit/summit_chunks/` |
| Akai Force | `pymupdf_docs/force/force_chunks/` |
