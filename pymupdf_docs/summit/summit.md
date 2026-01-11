# Summit Peak 2.1 Firmware Update Addendum V1 English En

> Converted from PDF using `pymupdf4llm`. Source: `/Users/ethan.stark/dev/misc/audio-midi/pdf/summit_peak_2.1_firmware_update_addendum_v1_english_en.pdf`.

---

## Page 1

Summit and Peak Firmware Update - Version 2.1 Addendum

# **Version 2.1**


For Firmware Updates 2.0 and 2.1


1

---

## Page 2

Summit and Peak Firmware Update - Version 2.1 Addendum

# **Version 2.1 User Guide Addendum**


There are three themes to the features of the Version 2.0 and 2.1 firmware updates
for Peak and Summit:


   - Stereo - Three additional Spread modes that open possibilities for stereo

sound design.

   - Control - We’ve included additional mod destinations, envelope parameters,

and more, to enhance your control.

   - Unpredictability - Arp Chance adds a level of unpredictability to Peak &

Summit’s arpeggiator patterns.

#### Updating your Firmware


You can update the firmware for your Summit or Peak synthesiser using our Novation
Components software. You can access Novation Components one of two ways:


   - Web version: in a browser that supports web MIDI (Chrome, Edge, Opera) go

to the URL: [components.novationmusic.com.](https://components.novationmusic.com/)

   - Standalone version: You can download the Components standalone

application from inside your Novation account at: [customer.novationmusic.](http://customer.novationmusic.com)
[com. You need to register your Summit or Peak to download the software.](http://customer.novationmusic.com)


After you’ve opened Novation Components, you can update your Summit or Peak:


1. Connect your synthesiser to your computer using the USB cable.
2. Hold the three buttons to the left of the screen and power on your synthesiser

in bootloader mode.
3. Open Novation Components.
4. Click Update in Components to update your firmware.


Components will instruct you through the steps to update your Summit or Peak with
the Version 2.0 and 2.1 firmware, enjoy!


2

---

## Page 3

Summit and Peak Firmware Update - Version 2.1 Addendum

# **Stereo**

#### Voice Menu: Spread


The Voice panning setting ‘Spread’ (formerly known as ‘UniSpread’) has broken out
into four unique Spread Modes:




- **Diverge** - The former ‘ **UniSpread** ’

behaviour remains; The more voices
you add to the sound, the further
voices diverge from the centre of the
stereo field. If no notes are held the
pattern resets.


- **Alternate** - As you add more voices

**Spread** pans even-numbered voices
left and odd-numbered voices right.




- **Diverge 2** - The voices you add run

a round-robin to move the stereo
position from the centre to the left
and the right. The sound gradually
gets wider before it resets back to
the centre, regardless of held voices.




- **NoteVal** - NoteVal masks each note

giving it a unique and repeatable
stereo position. This works well on
arp sequences.



We’ve moved **Spread** to page 2 of the **Voice** Menu. This moves it alongside the
other stereo voice controls:

   - Spread Mode: **Diverge**, **Alternate**, **Diverge 2**, **NoteVal**

## VOICE      2/4 Spread    0   H SpreadMode Diverge PanPosn   +0


3

---

## Page 4

Summit and Peak Firmware Update - Version 2.1 Addendum

#### Voice Menu: Pan Position


You can now control the Pan position ( **PanPosn**, **Voice** menu) of the voices. With
**Spread** set to 0, the voices pan where you set the ‘ **PanPosn** ’ from hard left to hard
right, -64 to +63.

## VOICE      2/4 Spread    0   H SpreadMode Diverge PanPosn   +0


Pan Position is dependent on the **SpreadMode** and amount.


   - **Diverge** : Pan Position of the first voice matches what you select, as you add

more voices the further the voices move from the initial pan position.


   - **Alternate** : Even-numbered voices still pan left and odd-numbered voices

right, however, as you pan each way, the voices in the opposite direction move
more toward the centre. This results in less-extreme differences weighting the
voices to one side of the stereo image.


   - **Diverge 2** : The voices still run in a round-robin but **Spread** affects how clear

the result is. For example, with **Spread** set to 64 and Pan posn of 0, the
spread is even across the stereo field. Increasing **PanPosn** to +63, voices
previously panned hard left are now central. However, if **Spread** is 127 some
voices stay panned hard left/right when **PanPosn** is +63/-64 respectively.


   - **NoteVal** : The voices retain their unique and repeatable stereo position but

with a weighting added by the **PanPosn** value. If the notes **C**, **E** and **G** are
panned hard left, centre, and hard right, respectively, when **PanPosn** is set
to -64, the **C** will remain hard-left, **E** will become hard-left and **G** will become
centre panned.


The Pan position is also available as a Mod Matrix destination: **PanPosn** .


4

---

## Page 5

Summit and Peak Firmware Update - Version 2.1 Addendum

# **Control**

#### Mod Matrix Destinations


We’ve added three new destinations to the Mod Matrix Destination menu:




- Pan Position – **PanPosn** - allows you to modulate the pan of the voice.

- O123 Shape – **O123Shpe** - modulates the shape control for all three



oscillators simultaneously.

- Control of Amp Envelope and Mod 1 & 2 Envelopes’, Delay, Hold and Sustain



stages: **AEnvDel**, **AEnvHld**, **AEnvSus**, **MEnv1Del**, **MEnv1Hld**, **MEnv1Sus**,
**MEnv2Del**, **MEnv2Hld**, **MEnv2Sus** .


#### Patch Cue

**PatchCue** is a performance feature allowing you to ‘cue’ a new patch by separating
the patch selection into two steps. With **PatchCue** off the encoder or patch +/allows you to switch immediately to a new patch.


With **PatchCue** on you can navigate to a new patch with the encoder or Patch +/buttons. The patch won’t change but the **Patch** button (Peak) or **Single** / **Multi** button
(Summit) flashes to let you know you’ve cued a patch. Press the flashing button to
execute the change when you want.


To enable **PatchCue** go to the Settings menu (‘ **MISC SETTINGS** ’).

## MISC SETTINGS  9/26 PatchCue  On   H


5

---

## Page 6

Summit and Peak Firmware Update - Version 2.1 Addendum

#### Animate Envelopes


We’ve added envelopes to the **Animate** buttons. Both **Animate** buttons now include
attack and release stages. You can change the attack and release of the **Animate**
buttons in the **Env** Menu. You can adjust **AnimXAtt** and **AnimXRel** from 0 – 127. The
Animate Envelope settings are exponential with values of 70ms at 32, 600ms at 64,
3.5 seconds at 96 and 15 seconds at 127.


### ANIMATE 1 ENVS  7/8 Anim1Att   0 H Anim1Rel   0


### ANIMATE 2 ENVS  8/8 Anim2Att   0 H Anim2Rel   0



Pressing an **Animate** button triggers the attack stage and releasing the button
triggers the release stage.

#### LFO 3 and 4 Additional Parameters


We’ve added three new parameters to LFOs 3 and 4:


   - **Slew**   - Adds slew to LFO 3 and 4. Slew changes the shape of the LFO

waveform. As you increase Slew it smooths sharp edges.


   - **Phase**   - Turns on key sync and phase – LFOs 3 and 4 aren’t per voice so LFO

will reset from all notes off to any number of notes on (allowing you to play
chords without constant resetting as you add more notes).


   - **FadeTime**   - Adds a fade-in for LFO 3 and 4 depth.


The new parameters for LFOs 3 and 4 were already available for LFOs 1 and 2, either
in the **LFO** menu ( **Slew** and **Phase** ) or as a top panel control ( **Fade** **Time** ).


6

---

## Page 7

Summit and Peak Firmware Update - Version 2.1 Addendum

#### FX Mod Slot Destinations


New FX Destinations are available on pages 9/10 of the **FX** Menu:

|FX Destination|Menu Name|
|---|---|
|<br>Reverb Size|<br>Rev Size|
|Reverb Low-Pass Filter|RevLpass|
|Reverb High-Pass Filter|RevHpass|
|Delay Slew|Del Slew|
|Delay LF Damp|DelLdamp|
|Delay HF Damp|DelHdamp|
|Delay Width|DelWidth|
|Delay Ratio|DelRatio|
|LFO 3 Rate|Lfo3Rate|
|LFO 4 Rate|Lfo4Rate|
|Noise Low-Pass Filter|NoiseLPF|
|Noise High-Pass flter|NoiseHPF|



7

---

## Page 8

Summit and Peak Firmware Update - Version 2.1 Addendum

#### Chorus/Flanger/Phlanger


We’ve added two new modes to the **Chorus** effect. On page 2 of the **FX** menu, the
**Mode** setting changes how the chorus effect works. We’ve produced each effect
using the same approach with varying intensities– Altering the number of notches
and number of cancellations present to change the effect. **Chorus** uses the highest
number of notches and ‘ **Phlanger** ’ uses the lowest.


In the **Chorus** and **Flanger** modes, changing between 2-Tap and 4-Tap offsets the
phase of the modulation source. This results in an increase in cancellation. With
both 2-pole and 4-pole, the modulation source synchronises, resulting in repeating
modulation. Set to **Ensemble**, the modulation source’s phase isn’t synchronised, this
results in ‘movement’ in the peaks & troughs across the frequency spectrum.


When using **Phlanger**, switching between 2-pole and 4-pole doesn’t change
the modulation source’s phase, however, switching to **Ensemble** results in the
modulation source no longer being synced.


All three effects share the range of rate, depth, and feedback parameters:


   - Depth: 0 - 127

   - Feedback: -63 - +63

   - Rate: 0 - 127 (approx. 0.02 - 3Hz)

## CHORUS     2/10 DEPTH    64 H FEEDBACK  +0 MODE    Chorus

   - **Chorus**   - The existing Chorus mode.


   - **Flanger**   - The Flanger is like the Chorus but uses more detuning and

feedback to produce a more pronounced swirling sensation emphasising the
harmonics in the sound as it sweeps through them.


   - **Phlanger**   - Phlanger follows the same approach as Flanger. It is an even

further reduced Chorus configured for a Phaser-like effect. Phlanger works well
with slow rates and high feedback values.


8

---

## Page 9

Summit and Peak Firmware Update - Version 2.1 Addendum

#### Switchable Delay Modes


We’ve added two new delay modes and a new Output setting to the Delay FX
settings.


   - **Original**   - the original delay; one delay time with a left tap time and a right

tap time.


   - **CrossFed**   - the left input feeds the right delay and the right input feeds the

left delay, similar to ping pong delay but incorporates left, right & central
panning.


   - **Dual**   - Each side of the delay has it’s own delay time equal to the tap

time. This effect starts to distinguish itself from **Orginal** when **Feedback** is
introduced.


**Output** is a switch to choose where the delay output is picked from. Either from the
delay output ( **PreDamp** ), or from the delay filter output ( **PostDamp** ).


For the **Original** delay style, **PostDamp** monos the delay and only gives the longest
delay tap time.


For the **CrossFed** and **Dual** delay styles **PostDamp** gives you the ability to hear the
first delay and filter in stereo.


9

---

## Page 10

Summit and Peak Firmware Update - Version 2.1 Addendum
# **Unpredictability**

#### Lo-Fi Delay


We’ve added a **TimeMode** feature to the delay section of the **FX** menu. This adjusts
the delay’s sample rate creating longer delays. As the delay’s sound quality reduces
as the delay gets longer– resulting in a lo-fi effect


**TimeMode** settings:


   - **Normal**   - A ‘clean’ delay at the rate and time you specify. Identical to the

previous functionality.

   - **Double**   - A ‘clean’ delay at half of the rate and time you specify.

   - **Treble**   - A ‘clean’ delay at a third of the rate and time you specify.

   - **QuadLoFi**   - A ‘Lo-Fi’ delay at a quarter of the rate and time you specify.

   - **HexVLoFi**   - A ‘’Very’ Lo-Fi’ delay at a sixth of the rate and time you specify.

## DELAY      6/10 TimeMode  Normal H

#### Noise as a Mod Source


We’ve added **Noise** to the **Mod** source menu so you can use it as a modulation
source in both the **Mod** Matrix and **FX** Mod Matrix.


10

---

## Page 11

Summit and Peak Firmware Update - Version 2.1 Addendum

#### Arp Chance


You can set the probability of a step playing in an arp sequence. To enable this, go
to page 4 of the **Arp/Clock** menu. You can set **ArpChance** between 10% and 100%.
10% gives each step a 1 in 10 chance of triggering and set to 100% each step will
always play.

## ARP       4/4 ArpChance  100% H

#### Arp mode – Chord 2


**Chord 2** relates to the **ArpChance** setting.


   - In **Chord 1** mode, **ArpChance** dictates how likely it is the whole chord plays.


   - In **Chord 2** mode **ArpChance** works per note; only some notes of the chord

play creating interesting effects. For example, a triad chord with a 10%
**ArpChance** results in scattered melodies, a more dense, layered chord with
higher **ArpChance** values can result in a moving harmony.

## ARP       2/4 Type    Chord2 H Rhythm    1 Octaves   1


11

---

## Page 12

Summit and Peak Firmware Update - Version 2.1 Addendum

## Update Features Exclusive to Peak


The following features can already be found on Summit, so are exclusive to the Peak
in the version 2.1 firmware update. If you have a Summit, you can use this guide too,
or find more detailed descriptions in the Summit User Guide.

#### Amp & Mod Env Delay


We’ve added a stage before the **AHDSR** - sequence of the **Amp** and **Mod**
Envelopes: envelope **Delay** . This is in the **Env** menu and updates Peak’s envelopes
to match Summit.


Envelope **Delay** changes how long it takes for the attack time – and the entire
**AHDSR** sequence - to start after you send a note. **Delay** time leads us to rename the
envelope sequence **DAHDSR** for completeness.

## AMP ENVELOPE   2/8 Delay    0 HoldTime   0 Repeats  Off


When **Delay** has the default value of 0, the envelopes start their attack phase as soon
as Peak receives MIDI. **Delay** inserts a lag between striking the key and the start of
the **AHDSR** envelope.


You can set envelope **Delay** between 0-127. At 127, the **AHDSR** starts after
10 seconds. Shorter delay times are typically more useful, so the delay time is
exponential: a value of about 85 has a delay of one second.


The new envelope **Delay** stages are also present in Peak’s **Mod** **Matrix** .


*Attack, Hold, Decay, Sustain, Release.


12

---

## Page 13

Summit and Peak Firmware Update - Version 2.1 Addendum

#### Noise HPF


We’ve added a High-pass noise filter to the **Osc** menu to match Summit. The High
filter performs the same function as Peak’s existing **NoiseLPF**, except high pass. As
you increase the **Noise HPF** value, the filter’s higher frequencies pass, and the filter
rejects more low-frequency content of the noise signal.


   - Displayed as: **NoiseHPF**

   - Initial value: 0

   - Range of adjustment: 0 to 127

## OSC COMN 2    2/9 KeySync   Off Noise LPF  127 Noise HPF  0


The parameter’s default value of zero sets the filter “fully open”. The effect of
applying this is that each voice will have its own tuning characteristic.

#### FX Mod Destinations


We’ve separated the modulation destinations **RevHPF** and **RevLPF** into four
damping and filtering options:




- **RevLdamp**

- **RevLpass**




- **RevHdamp**

- **RevHpass**



13

---

## Page 14

Summit and Peak Firmware Update - Version 2.1 Addendum

## Update Features Exclusive to Summit

#### Seq Local Mode


This is a variation of Summit’s **Local** mode. **Seq** local mode means you can use
Summit with an external sequencer, looping MIDI back into Summit, without causing
any MIDI feedback issues. With Local set to **Seq** :


   - The keys, mod and pitch wheels and aftertouch send MIDI data but don’t

affect Summit’s synth engine. All other front panel controls affect the engine
but don’t send out MIDI data.

## MIDI CONTROL   5/33 Local    Seq H Arp>MIDI  On


Local options: Off, On, Seq

#### Aftertouch Scaling


You can tweak the pressure you need to use aftertouch using the **Settings** menu item
**AtouchForce.** You can adjust **AtouchForce** between 1-10. Lower values require less
pressure, higher values require more pressure.

## KEYBOARD    17/33 VelCurve  NORMAL H AtouchForce 5


14

---

## Page 15

Summit and Peak Firmware Update - Version 2.1 Addendum

## Bug Fixes


   - Fixed an issue VCA gain controls did not affect voices 9-16 in single mode

(both via local and external MIDI control).


   - Modulation from LFO 3+4 now affects voices 9-16.


   - Sending performance data via external MIDI control (including Modulation

Wheel, Breath, Expression, etc.) now affects voices 9-16.


   - Fixed a syncing issue with external MIDI clocks where it took a while to

respond to clock signals correctly.


   - FM controls now send and respond to their NRPN messages:

     - FM OSC3 -> 1 Manual Amount NRPN 25:13 0-127 (0 to +127)

     - FM OSC1 -> 2 Manual Amount NRPN 25:17 0-127 (0 to +127)

     - FM OSC2 -> 3 Manual Amount NRPN 25:21 0-127 (0 to +127)


   - Fixed an issue where some front panel controls still influence the engine when

Local is Off.


   - Changed the way Summit receives Aftertouch and other performance data

from external MIDI on the Global channel when using multi parts:

     - Layer Mode - Both parts respond to MIDI received on the Global Channel.

     - Split Mode - MIDI received on the Global Channel affects both engines per

the split settings, for example, if the split point is C3, anything below C3
will affect part A and C3 and above will affect part B.

     - Dual Mode - MIDI received on the global channel affects the currently

selected part - i.e. A, B, or Both.


   - Fixed an issue where patch location was displayed incorrectly when viewing

single patches inside a Multi-Patch.


15

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
