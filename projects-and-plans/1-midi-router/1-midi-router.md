# Intelligent MIDI Router for Raspberry Pi

## Project Overview

Build a Python-based MIDI routing system running on Raspberry Pi (Patchbox OS) that:
1. Eliminates MIDI feedback loops between Akai Force and Novation Summit
2. Automatically detects Summit patch types (Single/Multi) and adjusts routing
3. Provides foundation for future creative features (Dato Duo sync, Impulse integration, etc.)

## Phase 1 Executive Summary

Phase 1 delivers a production-ready Python MIDI routing system running as a systemd service on Raspberry Pi (Patchbox OS) that eliminates MIDI feedback loops and enables intelligent patch-aware routing between Akai Force and Novation Summit.

### Key Deliverables

**1. Core Routing Engine (`midi_router.py`)**
- 4-port MIDI router using pimidipy library
- Bidirectional routing: Summit controller → Force sequencer → Summit sound engine
- Anti-loop protection: Source tracking prevents messages from routing back to origin
- Message classification: Note On/Off, CC, Program Change, Clock, SysEx handling
- Debug logging: All routing decisions logged for troubleshooting

**2. Intelligent Patch Management (`patch_manager.py`)**
- Automatic patch detection: Listens for Summit Program Change messages
- Single/Multi mode routing:
  - **Single Patch Mode**: Force Ch 1 and Ch 2 both route to Summit Ch 1
  - **Multi Patch Mode**: Force Ch 1 → Summit Part A (Ch 1), Force Ch 2 → Summit Part B (Ch 2)
- Patch library: JSON database of patch types (program # → Single/Multi)
- Optional learning mode: Auto-detect patch types from MIDI traffic patterns

**3. Duplicate Detection (`message_cache.py`)**
- 50ms time window for duplicate filtering
- Ring buffer (100 message capacity) for efficient lookups
- Signature-based matching: (message_type, channel, note/cc_number, velocity/value)
- Prevents double notes and feedback loops

**4. Configuration Management**
- JSON-based config for port mappings, feature flags, cache settings, logging
- Patch library (`summit-patches.json`) - extensible patch database
- Routing rules framework for custom routing logic (future expansion)

**5. System Integration**
- Systemd service (`midi-router.service`) with auto-restart on failure
- Auto-start on boot: Launches automatically when Pi powers on
- Rotating logs: 10MB max per file, 5 backup files retained
- User-space service: Runs as `patch` user (non-root)

### Problem Solved

**Before Phase 1:**
- Summit and Force connected via USB MIDI create feedback loops
- Double notes/hanging notes from circular message routing
- Program changes cause system hangs
- Cannot reliably sequence Summit Multi patches from Force

**After Phase 1:**
- Clean bidirectional MIDI flow with guaranteed loop prevention
- Seamless Summit patch changes without interruption
- Automatic routing adaptation based on Single vs Multi patch type
- Reliable Force sequencing of Summit (both patch modes)
- System recovers automatically after power cycles or crashes

### Technical Stack

- **Python 3** with pimidipy (ALSA MIDI library)
- **Patchbox OS** (Raspberry Pi)
- **Systemd** for service management
- **JSON** for configuration
- **TRS MIDI HAT** (2 DIN MIDI ports = 4 channels: 2 IN, 2 OUT)

## Hardware Setup Changes

**Current:** Summit ↔ Force via USB MIDI (bidirectional, causes loops)

**New:**
```
Summit DIN Out → Pi MIDI In 1 (pimidi0:0) → Routing Logic → Pi MIDI Out 1 (pimidi0:1) → Force DIN In
Force DIN Out → Pi MIDI In 2 (pimidi1:0) → Routing Logic → Pi MIDI Out 2 (pimidi1:1) → Summit DIN In
TR-6S USB → Force USB (unchanged - works reliably for clock sync)
```

**Summit Configuration:**
- Local mode: "Seq" (Settings Page 5/V)
- Global Chan: 1
- Part A Chan: 1
- Part B Chan: 2

## Phase 1: Core MIDI Router Foundation

### Critical Files to Create

```
/home/patch/midi-router/
├── midi_router.py           # Main routing service
├── patch_manager.py         # Summit patch detection & routing rules
├── message_cache.py         # Duplicate detection
├── config/
│   ├── config.json          # Port mappings, feature flags
│   ├── summit-patches.json  # Patch library (program # → Single/Multi)
│   └── routing-rules.json   # Custom routing rules
├── systemd/
│   └── midi-router.service  # Systemd service unit
├── logs/
│   └── midi-router.log      # Rotating log file
└── requirements.txt         # Python dependencies
```

### 1.1 Core Routing Engine (`midi_router.py`)

**Responsibilities:**
- Initialize pimidipy with 4 MIDI ports (2 IN, 2 OUT)
- Register callbacks for each input port
- Classify messages (Note On/Off, CC, Program Change, Clock, SysEx)
- Apply routing rules from patch_manager
- Anti-loop protection: track message origins, never route back to source
- Call message_cache for duplicate detection
- Log all routing decisions (debug mode)

**Key Implementation Details:**
```python
from pimidipy import PimidiPy, NoteOnEvent, NoteOffEvent, ProgramChangeEvent, ControlChangeEvent
from patch_manager import PatchManager
from message_cache import MessageCache

class MIDIRouter:
    def __init__(self, config_path):
        self.pimidipy = PimidiPy("midi-router")

        # Open ports
        self.summit_in = self.pimidipy.open_input('pimidi0:0')    # Summit controller
        self.force_out = self.pimidipy.open_output('pimidi0:1')   # To Force
        self.force_in = self.pimidipy.open_input('pimidi1:0')     # Force sequencer
        self.summit_out = self.pimidipy.open_output('pimidi1:1')  # To Summit engine

        self.patch_manager = PatchManager()
        self.cache = MessageCache(window_ms=50, max_size=100)

        # Register callbacks
        self.summit_in.add_callback(self.handle_summit_input)
        self.force_in.add_callback(self.handle_force_input)

    def handle_summit_input(self, event):
        """Process messages from Summit controller"""
        # Check for duplicate
        if self.cache.is_duplicate(event, source='summit'):
            self.log_debug(f"Dropped duplicate: {event}")
            return

        # Special handling for Program Change
        if isinstance(event, ProgramChangeEvent):
            self.patch_manager.update_current_patch(event.program)
            # Route to Summit's own engine (panel patch changes)
            self.summit_out.write(event)
            # Also route to Force for tracking (optional: check config flag)
            if self.config.get('record_program_changes', False):
                self.force_out.write(event)
            return

        # Normal routing: Summit controller → Force
        self.force_out.write(event)
        self.cache.add(event, source='summit')

    def handle_force_input(self, event):
        """Process messages from Force sequencer"""
        if self.cache.is_duplicate(event, source='force'):
            return

        # Apply patch-aware channel routing
        routed_event = self.patch_manager.apply_routing(event)
        if routed_event:
            self.summit_out.write(routed_event)
            self.cache.add(routed_event, source='force')

    def run(self):
        """Start main event loop"""
        self.pimidipy.run()
```

**Anti-Loop Strategy:**
- Tag messages with source port when entering cache
- Never route message back to its source port
- Time-based cache (50ms window) for duplicate detection
- Cache key: (message_type, channel, note/cc_number, velocity/value)

### 1.2 Patch Manager (`patch_manager.py`)

**Responsibilities:**
- Load Summit patch library from JSON
- Track current patch number and type (Single/Multi)
- Provide routing rules based on current patch
- Learning mode: auto-detect patch types from observed MIDI traffic

**Patch Library Format (`summit-patches.json`):**
```json
{
  "patches": {
    "0": "single",
    "1": "multi",
    "2": "single",
    ...
  },
  "default_mode": "single"
}
```

**Routing Logic:**

**Single Patch Mode:**
- Force Track 1 (Ch 1) → Summit Ch 1 ✓
- Force Track 2 (Ch 2) → Merge to Summit Ch 1 ✓

**Multi Patch Mode:**
- Force Track 1 (Ch 1) → Summit Part A (Ch 1) ✓
- Force Track 2 (Ch 2) → Summit Part B (Ch 2) ✓

```python
class PatchManager:
    def __init__(self, patch_library_path):
        self.patches = self.load_patches(patch_library_path)
        self.current_patch = 0
        self.current_mode = self.get_patch_mode(0)

    def update_current_patch(self, program_number):
        """Update patch tracking when Program Change detected"""
        self.current_patch = program_number
        self.current_mode = self.get_patch_mode(program_number)
        self.log_info(f"Switched to patch {program_number} ({self.current_mode} mode)")

    def get_patch_mode(self, program_number):
        """Get mode for patch (single/multi), default if unknown"""
        return self.patches.get(str(program_number), self.patches.get('default_mode', 'single'))

    def apply_routing(self, event):
        """Transform event based on current patch mode"""
        if not hasattr(event, 'channel'):
            return event  # Non-channel messages pass through

        if self.current_mode == 'single':
            # Force Ch 2 → merge to Ch 1
            if event.channel == 2:
                event.channel = 1

        # Multi mode: no transformation needed (Ch 1→1, Ch 2→2)
        return event
```

**Learning Mode (Optional Phase 1.5):**
- Monitor MIDI traffic after Program Change
- If see activity on both Ch 1 and Ch 2 within 5 seconds → likely Multi
- If see activity only on Ch 1 → likely Single
- Auto-update patch library

### 1.3 Message Cache (`message_cache.py`)

**Responsibilities:**
- Maintain ring buffer of recent messages (last 100 messages, 50ms window)
- Detect duplicates based on message signature
- Track message source for anti-loop protection

```python
from collections import deque
import time

class MessageCache:
    def __init__(self, window_ms=50, max_size=100):
        self.window_ms = window_ms
        self.max_size = max_size
        self.cache = deque(maxlen=max_size)

    def _get_signature(self, event):
        """Create unique signature for message"""
        sig = [type(event).__name__]

        if hasattr(event, 'channel'):
            sig.append(event.channel)
        if hasattr(event, 'note'):
            sig.append(event.note)
        if hasattr(event, 'velocity'):
            sig.append(event.velocity)
        if hasattr(event, 'control'):
            sig.append(event.control)
        if hasattr(event, 'value'):
            sig.append(event.value)

        return tuple(sig)

    def is_duplicate(self, event, source):
        """Check if message is duplicate within time window"""
        now = time.time() * 1000  # ms
        signature = self._get_signature(event)

        # Clean old entries
        cutoff = now - self.window_ms
        while self.cache and self.cache[0]['timestamp'] < cutoff:
            self.cache.popleft()

        # Check for duplicate
        for entry in self.cache:
            if entry['signature'] == signature:
                return True

        return False

    def add(self, event, source):
        """Add message to cache"""
        self.cache.append({
            'timestamp': time.time() * 1000,
            'signature': self._get_signature(event),
            'source': source
        })
```

### 1.4 Configuration (`config/config.json`)

```json
{
  "midi_ports": {
    "summit_in": "pimidi0:0",
    "force_out": "pimidi0:1",
    "force_in": "pimidi1:0",
    "summit_out": "pimidi1:1"
  },
  "features": {
    "anti_loop": true,
    "duplicate_detection": true,
    "patch_auto_detection": true,
    "record_program_changes": false,
    "learning_mode": false
  },
  "cache": {
    "window_ms": 50,
    "max_size": 100
  },
  "logging": {
    "level": "INFO",
    "file": "/home/patch/midi-router/logs/midi-router.log",
    "max_bytes": 10485760,
    "backup_count": 5
  }
}
```

### 1.5 Systemd Service (`systemd/midi-router.service`)

```ini
[Unit]
Description=Intelligent MIDI Router for Studio
After=network.target

[Service]
Type=simple
User=patch
WorkingDirectory=/home/patch/midi-router
ExecStart=/usr/bin/python3 /home/patch/midi-router/midi_router.py
Restart=always
RestartSec=5
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

**Installation:**
```bash
sudo cp systemd/midi-router.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable midi-router
sudo systemctl start midi-router
```

### 1.6 Dependencies (`requirements.txt`)

```
pimidipy>=1.0.0
python-dotenv>=0.19.0
```

## Phase 2: Impulse 61 Drum Pads (Deferred)

**Goal:** Map Impulse drum pads to TR-6S drums and Force drum tracks

**Implementation:**
- Add Impulse USB → Pi USB connection
- New module: `impulse_mapper.py`
- Config: `config/impulse-mappings.json` (pad # → note # + channel)
- Route Impulse pad hits to Force (for TR-6S control via USB)
- Optional: Direct routing to other devices

**Config example:**
```json
{
  "drum_pads": {
    "pad_1": {"note": 36, "channel": 10, "target": "force"},
    "pad_2": {"note": 38, "channel": 10, "target": "force"},
    ...
  }
}
```

## Phase 3: Perpendicular Keyboard Setup (Deferred)

**Goal:** Impulse keybed controls Summit Part A, Summit keybed controls Part B

**Implementation:**
- Add Impulse USB → Pi USB connection
- New module: `keyboard_splitter.py`
- Config: Define which keyboard controls which Part
- Optional: Transpose/octave shift per keyboard

**Routing:**
```
Impulse keys → Pi → Summit Part A (Ch 1)
Summit keys → Pi → Summit Part B (Ch 2)
Both → Pi → Force (for recording)
```

## Phase 4: Dato Duo Quick-Connect (Priority After Phase 1)

**Goal:** Make jamming with 6yo son frictionless - instant sync and routing

**Problem Solved:**
- Dato Duo sync issues when connecting mid-session
- Tedious setup prevents spontaneous jam sessions

**Implementation:**

### 4.1 Dato Module (`dato_manager.py`)

**Responsibilities:**
- Detect Dato Duo connection (hot-plug)
- Automatically route MIDI clock from Force to Dato
- Route Dato notes to Force for recording
- Optional: Route Dato to control other synths

**Key Features:**
- "Kid Mode" preset: One-touch setup for quick sessions
- Auto-start when Dato detected
- Visual/audio feedback when connected

### 4.2 Physical Connection

**Option A: MIDI DIN via Pi**
```
Dato Duo DIN Out → Pi MIDI In 3 (pimidi2:0)
Pi MIDI Out 3 (pimidi2:1) → Dato Duo DIN In
```

**Option B: USB MIDI (if Dato has USB)**
```
Dato Duo USB → Pi USB
```

### 4.3 Routing Logic

**On Dato connection detected:**
1. Send MIDI Clock from Force → Dato (via Pi)
2. Route Dato notes → Force (for recording/sequencing)
3. Optional: Route Dato → Summit/reface for sound control
4. Log: "Dato Duo connected - ready to jam!"

**Config (`config/dato-config.json`):**
```json
{
  "auto_connect": true,
  "sync_clock": true,
  "route_to": ["force"],
  "kid_mode": {
    "enabled": true,
    "presets": {
      "simple": {
        "dato_channel": 3,
        "force_track": 5,
        "tempo_sync": true
      }
    }
  }
}
```

### 4.4 Implementation Details

```python
class DatoManager:
    def __init__(self, config):
        self.config = config
        self.dato_connected = False
        self.dato_input = None
        self.dato_output = None

    def on_port_change(self, event):
        """Handle Dato hot-plug detection"""
        if 'Dato' in event.port_name and event.event_type == 'PORT_START':
            self.connect_dato()

    def connect_dato(self):
        """Auto-setup Dato routing"""
        self.dato_input = self.pimidipy.open_input('Dato Duo')
        self.dato_output = self.pimidipy.open_output('Dato Duo')

        # Register callback for Dato notes
        self.dato_input.add_callback(self.handle_dato_input)

        # Start clock forwarding
        if self.config['sync_clock']:
            self.force_input.add_callback(self.forward_clock_to_dato)

        self.dato_connected = True
        self.log_info("🎵 Dato Duo connected - ready to jam!")

    def handle_dato_input(self, event):
        """Route Dato notes to configured targets"""
        for target in self.config['route_to']:
            if target == 'force':
                self.force_output.write(event)

    def forward_clock_to_dato(self, event):
        """Forward MIDI clock to Dato"""
        if isinstance(event, (ClockEvent, StartEvent, StopEvent, ContinueEvent)):
            self.dato_output.write(event)
```

## Verification & Testing

### Phase 1 Testing

**1. Basic Connectivity**
```bash
# Check MIDI ports recognized
python3 -c "from pimidipy import PimidiPy; p = PimidiPy(); print([port.name for port in p.list_ports()])"

# Expected output:
# ['pimidi0:0', 'pimidi0:1', 'pimidi1:0', 'pimidi1:1', 'Akai Force', 'Novation Summit']
```

**2. Loop Prevention**
- Play note on Summit
- Verify: Single note heard (not double)
- Verify: Note captured in Force clip
- Check log: No duplicate messages

**3. Program Change Routing**
- Change Summit patch from panel (Local On temporarily for testing)
- Verify: Patch changes on Summit
- Verify: No loop or hang
- Check log: Program Change detected and routed

**4. Single/Multi Patch Auto-Detection**
- Load Single patch on Summit
- Play notes on Force Track 2 (Ch 2)
- Verify: Notes sound (merged to Ch 1)

- Load Multi patch on Summit
- Play notes on Force Track 1 (Ch 1) and Track 2 (Ch 2)
- Verify: Independent timbres sound correctly

**5. Long-Run Stability**
- Run for 1 hour continuous play
- Monitor log for errors
- Check latency: Should remain <1ms

**6. Service Auto-Start**
```bash
sudo systemctl status midi-router
# Should show: active (running)

sudo reboot
# Wait for boot
sudo systemctl status midi-router
# Should show: active (running)
```

### Phase 4 Testing (Dato Duo)

**1. Hot-Plug Detection**
- Start with Dato disconnected
- Connect Dato Duo USB/MIDI
- Verify: Log message "Dato Duo connected"
- Verify: MIDI clock syncing

**2. Jam Session Workflow**
- Son plays notes on Dato
- Verify: Notes recorded in Force
- Verify: Dato stays in sync with Force tempo
- Change Force tempo → Verify Dato follows

**3. Kid Mode Preset**
- Activate "simple" preset
- Verify: Dato routed to Force Track 5
- Verify: Tempo sync active
- Verify: Easy to start/stop

## Success Criteria

**Phase 1:**
- ✅ No more double notes when playing Summit
- ✅ Can change Summit patches without hanging
- ✅ Force can record from Summit cleanly
- ✅ Force can sequence Summit reliably (both Single and Multi patches)
- ✅ System auto-starts on Pi boot
- ✅ Logs show clean operation (no errors under normal use)

**Phase 4:**
- ✅ Dato connects instantly when plugged in
- ✅ Dato stays in perfect sync with Force
- ✅ Son can start jamming within 10 seconds of connection
- ✅ No technical troubleshooting required during creative moments

## Future Expansion Points

The modular architecture supports adding:
- **Harmonizer/Arpeggiator modules** - Process incoming notes (inspired by Midihub pipes)
- **Creative routing modes** - Probability-based routing, generative patterns
- **Web dashboard** - Real-time MIDI monitor, config editor
- **Scene management** - Save/recall routing configurations
- **Cross-device modulation** - TR-6S triggers Summit filter sweeps, etc.

All future modules plug into the same routing engine via the plugin architecture.

## Notes

- **Latency target:** <1ms for transparent feel
- **Fail-safe:** If Pi crashes, reconnect Summit ↔ Force USB as fallback
- **Observability:** All routing decisions logged for debugging
- **Extensibility:** Clean separation between core routing and feature modules
