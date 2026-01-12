# Perpendicular Keyboard Setup

## Project Context

This is Phase 3 of the Intelligent MIDI Router project. It enables dual-keyboard control of the Novation Summit's two Parts, creating a "perpendicular" performance setup.

**Prerequisite:** Phase 1 (Core MIDI Router) must be operational.

**Parent Project:** [1-midi-router](../1-midi-router/1-midi-router.md)

## Phase 3: Perpendicular Keyboard Setup

**Goal:** Impulse keybed controls Summit Part A, Summit keybed controls Part B

### Overview

Enable independent keyboard control of Summit's two Parts using two keyboards:
- **Impulse 61 keybed** → Summit Part A (Ch 1)
- **Summit's built-in keybed** → Summit Part B (Ch 2)

This creates a perpendicular performance layout where both keyboards control different timbres of the same instrument, ideal for layered playing, bass+lead splits, or dual-hand polyphonic parts.

### Hardware Connections

**New Connection:**
```
Impulse 61 USB → Pi USB (keyboard section)
```

**Existing (from Phase 1):**
```
Summit DIN Out → Pi MIDI In 1 → Pi MIDI Out 1 → Force DIN In
Force DIN Out → Pi MIDI In 2 → Pi MIDI Out 2 → Summit DIN In
```

### Summit Configuration

**Important Settings:**
- Local mode: "Off" (Settings Page 5/V) - Summit keybed doesn't trigger local engine directly
- Global Chan: 1
- Part A Chan: 1
- Part B Chan: 2

### Implementation

**New Module:** `keyboard_splitter.py`

**Location:** `/home/patch/midi-router/keyboard_splitter.py`

**Responsibilities:**
- Listen for keyboard input from both Impulse and Summit
- Route Impulse keybed → Summit Part A (Ch 1)
- Route Summit keybed → Summit Part B (Ch 2)
- Route both keyboards → Force (for recording)
- Apply optional transformations: transpose, octave shift, velocity curves

**Configuration:** `config/keyboard-config.json`

```json
{
  "keyboards": {
    "impulse": {
      "target_part": "A",
      "target_channel": 1,
      "transpose": 0,
      "octave_shift": 0,
      "velocity_curve": "linear",
      "route_to_force": true,
      "force_channel": 1
    },
    "summit": {
      "target_part": "B",
      "target_channel": 2,
      "transpose": 0,
      "octave_shift": 0,
      "velocity_curve": "linear",
      "route_to_force": true,
      "force_channel": 2
    }
  },
  "features": {
    "enable_split_mode": true,
    "allow_cross_routing": false,
    "sustain_pedal_per_part": true
  }
}
```

### Routing Logic

**Normal Mode (Perpendicular):**
```
Impulse keys → Pi → Summit Part A (Ch 1) + Force Track 1 (Ch 1)
Summit keys → Pi → Summit Part B (Ch 2) + Force Track 2 (Ch 2)
```

**Recording Flow:**
```
Both keyboards → Force (separate tracks/channels)
Force playback → Summit (respects Part A/B assignments via channels)
```

### Integration with Main Router

**Modify:** `midi_router.py`

```python
# In MIDIRouter.__init__()
if self.config['features'].get('enable_keyboard_split', False):
    from keyboard_splitter import KeyboardSplitter
    self.keyboard_splitter = KeyboardSplitter(
        config_path='config/keyboard-config.json'
    )
    
    # Note: Impulse input already registered if Phase 2 implemented
    # Summit input already registered in Phase 1
    # Just need to route keyboard events differently

def handle_impulse_input(self, event):
    """Process input from Impulse (both pads and keys)"""
    # If keyboard event (notes outside drum pad range)
    if isinstance(event, (NoteOnEvent, NoteOffEvent)) and event.note >= 48:
        routed_events = self.keyboard_splitter.route_keyboard(event, source='impulse')
        for target, routed_event in routed_events:
            if target == 'summit':
                self.summit_out.write(routed_event)
            elif target == 'force':
                self.force_out.write(routed_event)
        return
    
    # Otherwise, handle as drum pad (Phase 2 logic)
    # ...

def handle_summit_input(self, event):
    """Process messages from Summit controller"""
    # If keyboard split enabled and this is a keyboard event
    if (self.config['features'].get('enable_keyboard_split', False) and 
        isinstance(event, (NoteOnEvent, NoteOffEvent))):
        routed_events = self.keyboard_splitter.route_keyboard(event, source='summit')
        for target, routed_event in routed_events:
            if target == 'summit':
                self.summit_out.write(routed_event)
            elif target == 'force':
                self.force_out.write(routed_event)
        return
    
    # Otherwise, normal Phase 1 routing logic
    # ...
```

### Keyboard Splitter Implementation

```python
class KeyboardSplitter:
    def __init__(self, config_path):
        self.config = self.load_config(config_path)
        
    def route_keyboard(self, event, source):
        """Route keyboard event based on source keyboard"""
        if source not in self.config['keyboards']:
            return []
        
        kb_config = self.config['keyboards'][source]
        routed_events = []
        
        # Apply transformations
        transformed_event = self._transform_event(event, kb_config)
        
        # Route to Summit (with target channel)
        summit_event = transformed_event.copy()
        summit_event.channel = kb_config['target_channel']
        routed_events.append(('summit', summit_event))
        
        # Route to Force if enabled
        if kb_config.get('route_to_force', True):
            force_event = transformed_event.copy()
            force_event.channel = kb_config.get('force_channel', kb_config['target_channel'])
            routed_events.append(('force', force_event))
        
        return routed_events
    
    def _transform_event(self, event, config):
        """Apply transpose, octave shift, velocity curve"""
        transformed = event.copy()
        
        # Transpose
        if hasattr(transformed, 'note'):
            transformed.note += config.get('transpose', 0)
            transformed.note += config.get('octave_shift', 0) * 12
            transformed.note = max(0, min(127, transformed.note))  # Clamp
        
        # Velocity curve (future enhancement)
        # ...
        
        return transformed
```

### Files to Create/Modify

**New Files:**
```
/home/patch/midi-router/
├── keyboard_splitter.py          # NEW: Keyboard routing logic
├── config/
│   └── keyboard-config.json      # NEW: Keyboard configuration
```

**Modified Files:**
```
/home/patch/midi-router/
├── midi_router.py                # MODIFY: Add keyboard split routing
└── config/config.json            # MODIFY: Add enable_keyboard_split flag
```

### Configuration Update (`config/config.json`)

Add feature flag:
```json
{
  "features": {
    "enable_keyboard_split": true,
    ...
  }
}
```

## Verification & Testing

### Testing Plan

**1. Basic Routing**
- Play note on Impulse keybed
- Verify: Sounds on Summit Part A only
- Play note on Summit keybed
- Verify: Sounds on Summit Part B only

**2. Channel Separation**
- Load different patches on Part A and Part B
- Play Impulse → Verify Part A sound
- Play Summit → Verify Part B sound
- Verify: No cross-talk between Parts

**3. Recording to Force**
- Play phrase on Impulse
- Verify: Recorded on Force Track 1 (Ch 1)
- Play phrase on Summit
- Verify: Recorded on Force Track 2 (Ch 2)
- Play back both tracks
- Verify: Each plays correct Part (A/B)

**4. Transpose/Octave Shift**
- Set Impulse octave_shift: -1
- Play middle C on Impulse
- Verify: Sounds as C one octave lower
- Verify: No conflict with Summit keyboard

**5. Sustain Pedal**
- Connect sustain pedal to Impulse
- Hold notes, press pedal
- Verify: Only Part A sustains
- Repeat with Summit pedal
- Verify: Only Part B sustains

**6. Simultaneous Playing**
- Play both keyboards at once
- Verify: Clean polyphonic performance
- Verify: No stuck notes
- Verify: No latency issues

## Success Criteria

- ✅ Impulse keybed controls Summit Part A independently
- ✅ Summit keybed controls Summit Part B independently
- ✅ Both keyboards can be played simultaneously without conflicts
- ✅ Recording to Force captures each keyboard on separate tracks
- ✅ Force playback correctly routes to Part A/B based on channel
- ✅ Latency remains <1ms for natural playing feel
- ✅ Sustain pedals work per-Part (if implemented)

## Use Cases

### 1. Layered Performance
- Load complementary patches on Part A/B (e.g., pad + lead)
- Play chords on Impulse, melody on Summit
- Record both to Force for arrangement

### 2. Bass/Lead Split
- Part A: Bass patch (Impulse, lower octave)
- Part B: Lead patch (Summit, normal range)
- Jam with distinct roles per hand

### 3. Dual Polyphonic
- Both Parts playing full polyphonic patches
- Complex harmonic interplay
- Record multi-layered compositions

### 4. Teaching/Learning
- Teacher plays on one keyboard (model)
- Student plays on other keyboard (practice)
- Both hear their own Part clearly

## Future Enhancements

- **Split point:** Define keyboard ranges (e.g., Impulse plays only C2-C4)
- **Velocity zones:** Different Parts based on velocity
- **Smart merge:** Auto-detect when to merge vs split
- **Scene presets:** Quick-switch between split/layer/unison modes
- **Visual feedback:** LED indicators for active Part per keyboard
