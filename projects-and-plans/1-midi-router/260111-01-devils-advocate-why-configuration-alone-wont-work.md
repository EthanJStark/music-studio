<!-- jot:md-rename -->
---
title: "Devil's Advocate: Why Configuration Alone Won't Work for MIDI Router"
date: 2026-01-11
type: analysis
status: completed
tags: [midi-router, design-rationale, phase-1]
---

# Devil's Advocate: Why Configuration Alone Won't Work for MIDI Router

I'll address this devil's advocate argument head-on by examining why "just configure it correctly" fails for this specific use case.

## The Devil's Advocate Position

"Why build a complex Python router? Just carefully configure your MIDI settings - set the right Local modes, use the correct channels, disable feedback in the Force, and you won't need any of this."

## Why Configuration Alone Fails

### 1. **USB MIDI is Architecturally Bidirectional**

USB MIDI connections don't have separate "disable input" or "disable output" switches at the hardware level. When you connect Summit ↔ Force via USB:

- Both devices see each other as both input AND output
- Force can't selectively ignore Summit's controller data while still receiving sequencer playback
- Summit can't selectively ignore Force's note data while still sending its keys for recording

You'd need to choose: "Do I want Summit keys recorded in Force?" or "Do I want Force to sequence Summit?" - but you want **both**.

### 2. **Summit Local Mode Doesn't Solve the Loop Problem**

From the plan, Summit has Local mode options (Settings Page 5/V):
- **Local Off**: Keys don't trigger internal sound (USB/MIDI only)
- **Local On**: Keys trigger internal sound directly
- **Local "Seq"**: Intended for sequencer use

But here's the problem:
- **Local Off**: You lose the ability to play Summit standalone (keys make no sound)
- **Local On**: Creates instant feedback loop when connected via USB to Force
- **Local "Seq"**: Still sends MIDI out, which Force echoes back

None of these modes solve: "I want to play Summit keys, have Force record them, then have Force sequence Summit back, **and** change patches from the panel, all without loops."

### 3. **The Single vs Multi Patch Problem Has No Configuration Solution**

This is the **killer argument**. Consider these scenarios:

**Scenario A: Summit Single Patch Loaded**
- Force Track 1 (Ch 1) should play Summit → ✓ Works
- Force Track 2 (Ch 2) should ALSO play Summit (merged to Ch 1) → ❌ **No configuration can do this**

**Scenario B: Summit Multi Patch Loaded**
- Force Track 1 (Ch 1) should play Part A → ✓ Works
- Force Track 2 (Ch 2) should play Part B → ✓ Works

**The Problem:**
Force doesn't know which patch type is loaded. You'd have to **manually reconfigure Force's output channels every time you change Summit patches**. That's:
1. Disruptive to creative flow
2. Easy to forget (leading to "why isn't Track 2 making sound?" confusion)
3. Tedious (some Summit patches are Single, some are Multi - you'd be reconfiguring constantly)

### 4. **Program Change Feedback Is Unsolvable via Settings**

When you change a Summit patch from the panel:
1. Summit sends Program Change message out via USB
2. Force receives it (and might record it in a track)
3. Force echoes it back to Summit (because USB is bidirectional)
4. Summit receives its own Program Change again
5. **System hangs or double-triggers**

There's no Force setting for "ignore incoming Program Change messages" because you might **want** Force to send Program Changes to change Summit patches. You need **routing logic** that says:
- "PC from Summit → goes to Summit's own engine (to change patch) but NOT back to Summit via Force"
- "PC from Force → goes to Summit (to remotely change patches)"

### 5. **The "Works Until It Doesn't" Problem**

Let's say you find a configuration that works today:
- Summit Local = Seq
- Force MIDI Input = Summit
- Force MIDI Output = Summit
- Force Tracks 1-2 set to Ch 1 (for Single patches)

Now you want to:
- **Use a Multi patch** → Breaks (Track 2 won't sound - wrong channel)
- **Add Dato Duo for jamming** → Breaks (where does Dato connect? How does clock routing work?)
- **Change a Summit setting during troubleshooting** → Breaks (did you document the exact config?)

You'd spend more time **debugging MIDI settings than making music**.

### 6. **Cognitive Load Kills Creativity**

Every jam session becomes:
1. "Wait, which Local mode was I supposed to use again?"
2. "Is this a Single or Multi patch? Let me check... okay, now change Force Track 2 to Ch 1..."
3. "Why am I getting double notes? Oh right, I forgot to..."

Compare to the router approach:
1. Turn on gear
2. Make music

## What the Router Actually Provides

The router isn't "over-engineering" - it's providing **capabilities that don't exist in the devices**:

| Capability | Possible via Configuration? | Router Solution |
|------------|----------------------------|-----------------|
| Bidirectional routing without loops | ❌ No | ✅ Source tracking + anti-loop logic |
| Auto-adapt Force channels based on Summit patch type | ❌ No | ✅ Listens for Program Change, adjusts routing |
| Program Change without feedback | ❌ No | ✅ Routes PC to Summit engine but not back to source |
| Hot-plug Dato Duo for instant jamming | ❌ No | ✅ Detects connection, auto-configures clock sync |
| Recover from crashes/power cycles | ❌ No | ✅ Systemd auto-restart |

## The Real Test

Ask yourself: **"If careful configuration worked, why are there no forum posts saying 'Here's how I solved Summit ↔ Force USB MIDI loops'?"**

The answer: Because it's an **architectural limitation**, not a configuration problem. The router is building missing middleware that the devices can't provide themselves.

---

**TL;DR:** You can't configure your way out of hardware/firmware limitations. The router provides intelligent routing logic that doesn't exist in the devices - particularly the dynamic Single/Multi patch routing, which has no configuration-based solution.
