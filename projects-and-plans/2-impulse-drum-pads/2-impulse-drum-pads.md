# Impulse 61 Drum Pads Integration

## Project Context

This is Phase 2 of the Intelligent MIDI Router project. It extends the core routing engine built in Phase 1 to add Impulse 61 drum pad mapping capabilities.

**Prerequisite:** Phase 1 (Core MIDI Router) must be operational.

**Parent Project:** [1-midi-router](../1-midi-router/1-midi-router.md)

## Phase 2: Impulse 61 Drum Pads

**Goal:** Map Impulse drum pads to TR-6S drums and Force drum tracks

### Overview

Add Impulse 61's drum pads as a dedicated drum input controller, routing pad hits to the TR-6S (via Force USB connection) and enabling recording of drum performances on Force drum tracks.

### Hardware Connections

**New Connection:**
```
Impulse 61 USB → Pi USB
```

**Existing (from Phase 1):**
```
Summit DIN Out → Pi MIDI In 1 → Pi MIDI Out 1 → Force DIN In
Force DIN Out → Pi MIDI In 2 → Pi MIDI Out 2 → Summit DIN In
TR-6S USB → Force USB (unchanged - for clock sync and sound engine)
```

### Implementation

**New Module:** `impulse_mapper.py`

**Location:** `/home/patch/midi-router/impulse_mapper.py`

**Responsibilities:**
- Listen for Impulse USB MIDI input (drum pad section)
- Map pad numbers to specific MIDI notes and channels
- Route mapped notes to Force (which passes to TR-6S via USB)
- Optional: Direct routing to other devices

**Configuration:** `config/impulse-mappings.json`

**Config example:**
```json
{
  "drum_pads": {
    "pad_1": {"note": 36, "channel": 10, "target": "force"},
    "pad_2": {"note": 38, "channel": 10, "target": "force"},
    "pad_3": {"note": 42, "channel": 10, "target": "force"},
    "pad_4": {"note": 46, "channel": 10, "target": "force"},
    "pad_5": {"note": 48, "channel": 10, "target": "force"},
    "pad_6": {"note": 50, "channel": 10, "target": "force"},
    "pad_7": {"note": 51, "channel": 10, "target": "force"},
    "pad_8": {"note": 49, "channel": 10, "target": "force"}
  },
  "features": {
    "velocity_curve": "linear",
    "enable_aftertouch": false,
    "route_to_force": true,
    "direct_tr6s_routing": false
  }
}
```

### Integration with Main Router

**Modify:** `midi_router.py`

Add Impulse port initialization and callback registration:

```python
# In MIDIRouter.__init__()
if self.config['features'].get('enable_impulse_pads', False):
    from impulse_mapper import ImpulseMapper
    self.impulse_mapper = ImpulseMapper(
        config_path='config/impulse-mappings.json'
    )
    self.impulse_in = self.pimidipy.open_input('Impulse 61')
    self.impulse_in.add_callback(self.handle_impulse_input)

def handle_impulse_input(self, event):
    """Process drum pad hits from Impulse"""
    mapped_event = self.impulse_mapper.map_drum_pad(event)
    if mapped_event:
        self.force_out.write(mapped_event)
        self.log_debug(f"Routed Impulse pad: {event} → {mapped_event}")
```

### Impulse Mapper Implementation

```python
class ImpulseMapper:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        self.pad_mappings = self.config['drum_pads']
        
    def map_drum_pad(self, event):
        """Map Impulse pad hit to configured note/channel"""
        if not isinstance(event, NoteOnEvent):
            return None
            
        # Impulse pads send notes 36-43 (typical drum pad range)
        # Check if this is a pad hit we want to map
        pad_key = f"pad_{event.note - 35}"  # pad_1, pad_2, etc.
        
        if pad_key in self.pad_mappings:
            mapping = self.pad_mappings[pad_key]
            # Create new event with mapped note and channel
            return NoteOnEvent(
                note=mapping['note'],
                channel=mapping['channel'],
                velocity=event.velocity
            )
        
        return None  # Pass through unmapped pads
```

### Files to Create/Modify

**New Files:**
```
/home/patch/midi-router/
├── impulse_mapper.py          # NEW: Drum pad mapping logic
├── config/
│   └── impulse-mappings.json  # NEW: Pad mappings configuration
```

**Modified Files:**
```
/home/patch/midi-router/
├── midi_router.py             # MODIFY: Add Impulse input handling
└── config/config.json         # MODIFY: Add enable_impulse_pads flag
```

### Configuration Update (`config/config.json`)

Add feature flag:
```json
{
  "features": {
    "enable_impulse_pads": true,
    ...
  }
}
```

## Verification & Testing

### Testing Plan

**1. Pad Detection**
```bash
# Check Impulse recognized as USB MIDI device
python3 -c "from pimidipy import PimidiPy; p = PimidiPy(); print([port.name for port in p.list_ports()])"

# Expected: 'Impulse 61' in list
```

**2. Pad Mapping**
- Hit each drum pad on Impulse
- Verify: Correct note sent to Force (check Force MIDI monitor)
- Verify: TR-6S sounds trigger correctly (via Force USB)
- Check log: Mapping transformations logged

**3. Velocity Response**
- Hit pads with varying velocities (soft/hard)
- Verify: TR-6S responds with appropriate dynamics
- Verify: No velocity clipping or distortion

**4. Recording to Force**
- Arm drum track on Force
- Play pattern on Impulse pads
- Verify: Pattern recorded accurately
- Verify: Playback triggers TR-6S correctly

**5. Simultaneous Use**
- Play drums on Impulse pads
- Simultaneously play Summit from Force sequencer
- Verify: No conflicts, both work cleanly
- Verify: No latency issues

## Success Criteria

- ✅ All 8 drum pads respond reliably
- ✅ Pad hits route to TR-6S via Force with <5ms latency
- ✅ Velocity sensitivity works naturally
- ✅ Can record drum performances on Force
- ✅ No interference with Phase 1 routing (Summit/Force)
- ✅ Service remains stable with Impulse connected

## Future Enhancements

- **Velocity curves:** Linear, logarithmic, exponential options
- **Pad layers:** Different sounds per velocity range
- **Pattern repeat:** Hold pad to repeat pattern
- **Quantization:** Snap pad hits to grid
- **Multi-target routing:** Send pads to multiple devices simultaneously
