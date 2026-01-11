# Summit Peak 2.1 Firmware Update Addendum V1 English En (Pages 16-18)

> Converted from PDF using `pymupdf4llm`. Source: `/Users/ethan.stark/dev/misc/audio-midi/pdf/summit_peak_2.1_firmware_update_addendum_v1_english_en.pdf`.

---

## Page 16

Summit and Peak Firmware Update - Version 2.1 Addendum

## Bug Fixes (from version 2.1)


   - Fixed the issue of the mod routine (incl. envelope & LFO rates) being slower in

Version 2.0.


   - Fixed envelopes dropping abruptly in the last portion of the decay stage, both

AEnv & MEnv - effects Env repeats (old envelopes finish earlier)


   - Tuning tables now respond to NRPN (25:6 - select table).


   - Fixed an issues where the Sustain Pedal input affected the engine when local

was off.


   - Key latch no longer lights up when sustain pedal and a front panel button is

pressed.


   - Fixed an issue where the synthesiser doesn’t go into Bootloader when

prompted by Components.


   - Fixed an issue where the VCA level changes preventing autoplay patches from

playing upon load.

#### Bug Fixes Exclusive to Summit


   - In multi-mode, Part B LFO1/2 LEDs display on Part A.


   - Page LEDs may not update correctly when switching between menus & parts.


   - Exiting a menu prompts a program change message.

## Improvements (Peak and Summit)


   - Bank & patch dumping to Components.


   - Voice management improvements to prevent voice dropping.


16

---

## Page 17

Summit and Peak Firmware Update - Version 2.1 Addendum

## Alterations

#### VCA clamping behaviour


In Firmare version 2.0 the mod destination, VCA level, was clamped in the mod
matrix when exceeding certain thresholds. However, this caused the mod routine to
slow down so we have had to remove this in version 2.1.


When the VCA level is reaching the upper threshold, through additional modulation
in the mod matrix, you may hear brief changes in phase (most notably as a short
click and changes to the stereo spread) and the VCA level may drop entirely when
exceeding the upper threshold. Similarly, the VCA may go from silent to audible
when passing the lower threshold.


Similar behaviour has been in present in past firmware releases. Of the possible
outcomes noted above, we expect a small amout of users to experience slight phase
alterations. If this is the case, use the **VCA Gain** control on the front panel and the
**PatchLevel** parameter in the **Voice** menu to make adjustments.


In most cases reducing **VCA Gain** and increasing **PatchLevel** will resolve the issue
and keep the patch at the same level.

## Known Issues


   - In multi-mode, Part B LFO1/2 LEDs display on Part A.


   - In some cases the LFO LEDs may appear out of phase when using phase sync

on both parts of a multi.


17

---

## Page 18

Summit and Peak Firmware Update - Version 2.1 Addendum

## MIDI Parameters List

|Parameter|CC/NRPN|Control Number|Range|Default Value|
|---|---|---|---|---|
|Pan Posn|NRPN|<br>0:51|0-127|<br>0|
|<br>Pan Type|NRPN|0:52|0-3|0|
|<br>Spread|NRPN|0:5|0-127|0|
|Chorus/Phaser/Flanger|NRPN|0:115|0-2|0|
|Lo-Fi Delay Time Mode|NRPN|0:98|0-4|0|
|<br>Select Tuning Table|NRPN|25:6|0-16|0|
|<br>Arp Chance|NRPN|25:33|01-100|100|
|<br>Animate 1 Att|NRPN|25:34|0-127|0|
|<br>Animate 1 Rel|NRPN|25:35|0-127|0|
|<br>Animate 2 Att|NRPN|25:36|0-127|0|
|<br>Animate 2 Rel|NRPN|25:37|0-127|0|
|<br>LFO3Phase|NRPN|25:38|0-120|0|
|LFO3Slew|NRPN|25:39|0-127|0|
|LFO3FadeTime|NRPN|25:40|0-127|0|
|LFO4Phase|NRPN|25:41|0-120|0|
|LFO4Slew|NRPN|25:42|0-127|0|
|LFO4FadeTime|NRPN|25:43|0-127|0|
|Atouch Scale|NRPN|64:3|1-10|5|
|<br>Patch Cue|NRPN|64:0|0-1|0|



18
