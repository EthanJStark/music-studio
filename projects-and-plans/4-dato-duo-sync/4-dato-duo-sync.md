# Dato Duo Quick-Connect

## Project Context

This is Phase 4 of the Intelligent MIDI Router project. It enables frictionless jamming with the Dato Duo synthesizer through automatic connection, sync, and routing.

**Prerequisite:** Phase 1 (Core MIDI Router) must be operational.

**Parent Project:** [1-midi-router](../1-midi-router/1-midi-router.md)

**Priority:** High - This is the next priority after Phase 1

## Phase 4: Dato Duo Quick-Connect (Priority After Phase 1)

**Goal:** Make jamming with 6yo son frictionless - instant sync and routing

### Problem Solved

**Before:**
- Dato Duo sync issues when connecting mid-session
- Tedious setup prevents spontaneous jam sessions
- Technical troubleshooting interrupts creative moments
- Dad spends more time configuring than playing

**After:**
- Plug in Dato → Instant connection and sync
- Son can start playing within 10 seconds
- Automatic MIDI clock forwarding
- Zero configuration required during jam sessions

### Hardware Connections

**Option A: MIDI DIN via Pi (Preferred)**
```
Dato Duo DIN Out → Pi MIDI In 3 (pimidi2:0)
Pi MIDI Out 3 (pimidi2:1) → Dato Duo DIN In
```

**Option B: USB MIDI (if Dato has USB)**
```
Dato Duo USB → Pi USB
```

**Routing Context (from Phase 1):**
```
Summit DIN Out → Pi MIDI In 1 → Pi MIDI Out 1 → Force DIN In
Force DIN Out → Pi MIDI In 2 → Pi MIDI Out 2 → Summit DIN In
TR-6S USB → Force USB (clock source)
```

### Implementation

**New Module:** `dato_manager.py`

**Location:** `/home/patch/midi-router/dato_manager.py`

**Responsibilities:**
- Detect Dato Duo connection (hot-plug detection)
- Automatically route MIDI clock from Force to Dato
- Route Dato notes to Force for recording
- Optional: Route Dato to control other synths (Summit, reface)
- "Kid Mode" preset for one-touch setup

### Dato Manager Implementation

```python
from pimidipy import ClockEvent, StartEvent, StopEvent, ContinueEvent

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
        elif 'Dato' in event.port_name and event.event_type == 'PORT_STOP':
            self.disconnect_dato()

    def connect_dato(self):
        """Auto-setup Dato routing"""
        try:
            self.dato_input = self.pimidipy.open_input('Dato Duo')
            self.dato_output = self.pimidipy.open_output('Dato Duo')

            # Register callback for Dato notes
            self.dato_input.add_callback(self.handle_dato_input)

            # Start clock forwarding
            if self.config['sync_clock']:
                self.force_input.add_callback(self.forward_clock_to_dato)

            self.dato_connected = True
            self.log_info("🎵 Dato Duo connected - ready to jam!")
            
            # Optional: Play connection sound/visual feedback
            if self.config.get('connection_feedback', True):
                self.play_connection_sound()
                
        except Exception as e:
            self.log_error(f"Failed to connect Dato: {e}")

    def disconnect_dato(self):
        """Handle Dato disconnection"""
        self.dato_connected = False
        self.dato_input = None
        self.dato_output = None
        self.log_info("Dato Duo disconnected")

    def handle_dato_input(self, event):
        """Route Dato notes to configured targets"""
        # Route to Force for recording
        for target in self.config['route_to']:
            if target == 'force':
                # Apply Kid Mode channel if enabled
                if self.config.get('kid_mode', {}).get('enabled', False):
                    event.channel = self.config['kid_mode']['dato_channel']
                self.force_output.write(event)
            elif target == 'summit':
                self.summit_output.write(event)

    def forward_clock_to_dato(self, event):
        """Forward MIDI clock from Force to Dato"""
        if not self.dato_connected:
            return
            
        if isinstance(event, (ClockEvent, StartEvent, StopEvent, ContinueEvent)):
            self.dato_output.write(event)

    def activate_kid_mode(self):
        """Activate Kid Mode preset"""
        if not self.dato_connected:
            self.log_warning("Dato not connected - cannot activate Kid Mode")
            return False
            
        preset = self.config['kid_mode']['presets']['simple']
        
        # Configure Force track for Dato
        # (This may require Force MIDI control implementation)
        self.log_info(f"Kid Mode activated: Dato → Force Track {preset['force_track']}")
        return True

    def play_connection_sound(self):
        """Optional: Play a sound when Dato connects"""
        # Could send a note to Summit or play via Pi audio out
        # Provides audible feedback that connection succeeded
        pass
```

### Configuration: `config/dato-config.json`

```json
{
  "auto_connect": true,
  "sync_clock": true,
  "route_to": ["force"],
  "connection_feedback": true,
  "kid_mode": {
    "enabled": true,
    "dato_channel": 3,
    "presets": {
      "simple": {
        "force_track": 5,
        "tempo_sync": true,
        "auto_arm_track": false,
        "default_sound": "summit_ch3"
      },
      "drums": {
        "force_track": 6,
        "tempo_sync": true,
        "route_to_tr6s": true
      }
    }
  },
  "advanced": {
    "forward_program_changes": false,
    "forward_cc_messages": true,
    "enable_dato_control": false
  }
}
```

### Integration with Main Router

**Modify:** `midi_router.py`

```python
# In MIDIRouter.__init__()
if self.config['features'].get('enable_dato_sync', False):
    from dato_manager import DatoManager
    self.dato_manager = DatoManager(config_path='config/dato-config.json')
    self.dato_manager.pimidipy = self.pimidipy
    self.dato_manager.force_input = self.force_in
    self.dato_manager.force_output = self.force_out
    self.dato_manager.summit_output = self.summit_out
    
    # Register port change callback for hot-plug detection
    self.pimidipy.add_port_callback(self.dato_manager.on_port_change)
    
    # Try to connect if Dato already plugged in
    try:
        self.dato_manager.connect_dato()
    except:
        self.log_info("Dato Duo not detected at startup")
```

### Key Features

**1. Hot-Plug Detection**
- Automatic detection when Dato is connected
- No manual configuration needed
- Reconnection if Dato temporarily disconnected

**2. Clock Forwarding**
- MIDI Clock from Force → Dato
- Start/Stop/Continue messages synchronized
- Dato stays perfectly in sync with project tempo

**3. Bidirectional Routing**
- Dato → Force (for recording sequences)
- Force → Dato (clock and playback)
- Optional: Dato → Summit/other synths

**4. Kid Mode**
- One preset optimized for simple jamming
- Pre-configured channel and track routing
- Minimal complexity for 6yo to start playing
- Optional auto-arm Force track for recording

### Files to Create/Modify

**New Files:**
```
/home/patch/midi-router/
├── dato_manager.py             # NEW: Dato connection and sync logic
├── config/
│   └── dato-config.json        # NEW: Dato configuration and presets
```

**Modified Files:**
```
/home/patch/midi-router/
├── midi_router.py              # MODIFY: Add Dato manager integration
└── config/config.json          # MODIFY: Add enable_dato_sync flag
```

### Configuration Update (`config/config.json`)

Add feature flag:
```json
{
  "features": {
    "enable_dato_sync": true,
    ...
  }
}
```

## Verification & Testing

### Phase 4 Testing

**1. Hot-Plug Detection**
- Start system with Dato disconnected
- Connect Dato Duo USB/MIDI
- Verify: Log message "🎵 Dato Duo connected - ready to jam!"
- Verify: MIDI clock immediately starts forwarding
- Check: `systemctl status midi-router` shows no errors

**2. Clock Synchronization**
- Set Force tempo to 120 BPM
- Connect Dato
- Verify: Dato syncs to 120 BPM
- Change Force tempo to 90 BPM
- Verify: Dato follows new tempo immediately
- Press Play on Force
- Verify: Dato receives Start message
- Press Stop on Force
- Verify: Dato receives Stop message

**3. Jam Session Workflow**
- Son plays notes on Dato
- Verify: Notes sound on Dato (local)
- Verify: Notes visible in Force MIDI monitor (if armed)
- Verify: Can record Dato performance to Force
- Play back recorded sequence
- Verify: Notes play back correctly

**4. Kid Mode Preset**
- Activate "simple" preset (via config or future UI)
- Verify: Dato routed to Force Track 5 (or configured track)
- Verify: Correct channel assignment (Ch 3)
- Verify: Tempo sync active and stable
- Test workflow: Plug in → Play → Record → Playback
- Verify: Entire flow works in <10 seconds

**5. Disconnection Handling**
- Unplug Dato during operation
- Verify: System continues working for other devices
- Verify: No crashes or hung processes
- Reconnect Dato
- Verify: Auto-reconnects and resumes sync

**6. Long-Run Stability**
- Run for 30-minute jam session
- Monitor clock sync accuracy
- Verify: No drift or timing issues
- Verify: No memory leaks or CPU spikes

## Success Criteria

- ✅ Dato connects instantly when plugged in (<2 seconds)
- ✅ Dato stays in perfect sync with Force tempo
- ✅ Son can start jamming within 10 seconds of connection
- ✅ No technical troubleshooting required during creative moments
- ✅ System recovers gracefully from disconnections
- ✅ Kid Mode preset enables one-touch setup
- ✅ Zero latency perception during sync'd playback

## Use Cases

### 1. Quick Jam Session
**Scenario:** Son asks "Can we make music?"
**Flow:**
1. Plug in Dato Duo → Auto-connects and syncs
2. Son starts playing → Immediately in sync with Force
3. Dad hits record on Force → Captures performance
4. Play back together → Layered jam session

**Time to music:** <10 seconds ✅

### 2. Collaborative Recording
**Scenario:** Building a track together
**Flow:**
1. Dad sets up drum pattern on TR-6S (via Force)
2. Dad creates bass line on Summit
3. Plug in Dato → Son adds melody line
4. All devices in perfect sync
5. Record multiple takes, comp the best

### 3. Learning Tool
**Scenario:** Teaching basic music concepts
**Flow:**
1. Dad programs simple chord progression on Force
2. Son plays melody on Dato (always in sync)
3. Experiment with different melodies
4. Record favorite ideas for later

## Future Enhancements

- **Multiple presets:** "Simple", "Drums", "Lead", "Bass" configurations
- **Visual feedback:** LED indicator or small display showing connection status
- **Button control:** Physical button on Pi case to activate Kid Mode
- **Auto-arm track:** Automatically arm Force track when Dato connected
- **Sound assignments:** Auto-load appropriate Summit patch for Dato channel
- **Session recall:** Save/recall Dato jam session configurations
- **Multi-Dato support:** Connect multiple Dato Duos (if you get more!)
