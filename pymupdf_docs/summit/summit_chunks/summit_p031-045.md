# Summit User Guide 1.1 En (Pages 31-45)

> Converted from PDF using `pymupdf4llm`. Source: `/Users/ethan.stark/dev/misc/audio-midi/pdf/Summit User Guide 1.1 EN.pdf`.

---

## Page 31

**LFO 1:**

    - can modify the waveform shape of each oscillator when LFO1 is selected by the
oscillator’s **Source** button 23 ;

    - can modulate the filter frequency; the amount of modulation is adjusted in the Filter
Section with **LFO 1 Depth** control 65 .


**LFO 2:**

    - can modulate the pitch of each Oscillator; the amount of modulation is adjusted
in the Oscillator Section with the **LFO 2 Depth** control 21 . This is the method of
adding “vibrato” to a sound.


Either LFO may additionally be patched in the Modulation Matrix to modulate many other
synth parameters.


**LFO 1 & 2 Waveform**
The **Type** button 24 selects one of four wave shapes – Triangle, Sawtooth,
Square or Sample and Hold. The LEDs above the button confirm the waveform selected.


**LFO 1 & 2 Rate**
The speed (or rate, or frequency) of each LFO is set by the **Range** button 26 and the
rotary **Rate** control 27 . The **Range** button has three settings: **Low**, **High** and **Sync** .
Selecting **Sync** reassigns the function of the **Rate** control, allowing the speed of the LFO
to be synchronised to an internal or external MIDI clock, based on a sync value selected by
the control. When **Sync** is selected, the OLED displays the LFO’s `RateSync` parameter
when the **Rate** control is moved: this allows you to choose the tempo division needed. See
LFO Sync Rate table on page 45


**LFO 1 & 2 Fade Time**
LFO effects are often more effective when faded-in, rather than just ‘switched on’; the
**Fade Time** parameter sets how long the LFO output takes to ramp up when a note is
played. The rotary control 25 is used to adjust this time. See also Fade Mode (page
32), where you can also make the LFO fade out after the Fade Time, or using a Gate
setting, start or end abruptly after the Fade Time.


**LFO 3 and LFO 4 hardware controls**





LFO 3 and LFO 4 share a set of panel controls which may be assigned to either LFO, and
each has its own page in the LFO menu with further parameters. The LFO outputs are
not routable using direct panel controls in the way that LFO 1 and LFO 2 are, but may be
routed to any of the Modulation Matrix’s destinations.


**LFO 3 & 4 Select**
The **Select** button 28 assigns the other controls on the **GLOBAL LFO 3 & 4** panel
section to LFO 3 or LFO 4 respectively.


**LFO 3 & 4 Waveform**
The **Type** button 29 selects one of four wave shapes - Triangle, Sawtooth,
Square or Sample and Hold. The LEDs above the button confirm the waveform currently
selected. Waveform selection may also be made from the LFO menu.


**LFO 3 & 4 Rate**
The speed (or rate, or frequency) of the selected LFO (LFO 3 or LFO 4) is set by the **Rate**
control 30 Selecting **Sync** 31 reassigns the function of the **Rate** control, allowing the
speed of the LFO to be synchronised to an internal or external MIDI clock, based on a
sync value selected by the control. When **Sync** is selected, the OLED displays the LFO’s
`RateSync` parameter when the **Rate** control is moved: this allows you to choose the
tempo division needed. See LFO Sync Rate table on page 45. LFO 3/4 Rate may also
be set from the LFO menu.


**31**



**LFO 3 & 4 Sync**
Pressing **Sync** 31 locks the LFO speed to an external or internal MIDI clock, to enable
it to be synchronised to external equipment. The sync division factor is adjusted by the
`LxRateSync` parameter (where x=3 or 4) in the LFO menu.


**The LFO Menu**
LFO1 and LFO 2 are ‘per voice’. This is a very powerful feature of Summit (and other
Novation synthesisers). For example, when an LFO is assigned to create vibrato, and a
chord is played, each note of the chord will be varied at the same rate, but not necessarily
in the same phase. There are various settings in the LFO Menu that control how the LFOs
respond and lock together.


LFO 1 and LFO 2 each have three menu pages; the parameters available for LFO 1 and
LFO 2 are identical.


As LFO 3 and LFO 4 are intended for the creation of additional modulation effects rather
than fundamental tone generation, they are ‘global’ as opposed to ‘per-voice’, meaning that
they can also be used to modulate FX parameters via the FX Modulation Matrix. They have
one menu page each; the parameters available for LFO 3 and LFO 4 are identical.


**LFO 1 and LFO 2: The default menu displays for LFO 1 are shown below:**


LFO 1      1/8

Phase   Free  H
MonoTrig  Legato

Slew     0


LFO 1      2/8
FadeMode  FadeIn H
FadeSync  On


LFO 1      3/8
Repeats  Off   H

Common   Off


**LFO Phase**
Displayed as: `Phase`
Initial value: Free
Range of adjustment: Free; 0deg to 357deg (in 3deg increments)


Each LFO runs continuously ‘in the background’. If the `Phase` is set to Free (the
default), there is no way of predicting where the waveform will be when a key is pressed.
Consecutive presses of a key will inevitably produce varying results. With all other values
of `Phase`, the LFO will re-start at the same point on the waveform every time a key is
pressed, the actual point being determined by the parameter value. A complete waveform
has 360º, and the control’s increments are in 3º steps. Thus a half-way setting (180deg)
will cause the modulating waveform to start at half-way through its cycle.





KEY "ON" KEY "ON"



**MonoTrig**
Displayed as: `MonoTrig`
Initial value: Legato
Range of adjustment: Legato or Re-Trig


`MonoTrig` only applies to monophonic Voice modes (see page 22). Providing LFO
`Phase` is not set to Free, the LFOs are re-triggered each time a new note is pressed. But
if you are playing in legato style (literally “smoothly” – playing further keys while one key is
still held), the LFOs will only re-trigger if `MonoTrig` is set to Re-Trig. If set to Legato, you
will only hear the effect of re-triggering on the first note.

---

## Page 32

**LFO Slew**
Displayed as: `Slew`
Initial value: 0
Range of adjustment: 0 to 127


`Slew` has the effect of modifying the shape of the LFO waveform. Sharp edges become
less sharp as Slew is increased. The effect of this on pitch modulation can be heard by
selecting Square as the LFO waveform and setting the rate fairly low so when a key is
pressed the output alternates between two tones. Increasing the value of `Slew` will cause
the transition between the two tones to become a “glide” rather than a sharp change. This
is caused by the vertical edges of the square LFO waveform being slewed.



**LFO Common Sync**
Displayed as: `Common`
Initial value: Off
Range of adjustment: Off or On


Common Sync is only applicable to polyphonic voices. When `Common` is On, it ensures
that the phase of the LFO waveform is synchronised for every note being played. When
set Off, there is no such synchronisation, and playing a second note while one is already
pressed will result in an unsynchronised sound as the modulations will be out of time.
When LFOs are in use for pitch modulation (their most common application), having
`Common` set to Off will give more natural results.





NOTE 1


NOTE 2







NOTE 1


NOTE 2







**Fade Mode**
Displayed as: `FadeMode`
Initial value: FadeIn
Range of adjustment: FadeIn, FadeOut, GateIn, GateOut


The function of the four possible settings of `FadeMode` are as follows:
1. **FadeIn**    - the LFO’s modulation is gradually increased over the time period set by
the **Fade Time** control 25 .


2. **FadeOut**    - the LFO’s modulation is gradually decreased over the time period set
by the **Fade Time** control, leaving the note unmodulated.


3. **GateIn**    - the onset of the LFO’s modulation is delayed by the time period set by
the **Fade Time** parameter, and then starts immediately at full level.


4. **GateOut**    - the controlled parameter is fully modulated by the LFO for the time
period set by the **Fade Time** parameter. At this time, the modulation stops abruptly.


Note that whichever of the Fade Modes is selected, it is always active; if you do not want to
hear its effect, turn the **Fade Time** control 25 down to zero.


**LFO Fade Sync**
Displayed as: `FadeSync`
Initial value: On
Range of adjustment: Off or On


The setting of `FadeSync` only applies to monophonic voice modes (see page 22).
`FadeSync` determines whether the time delay set by **Fade Time** is re-started each
time a key is pressed. With `FadeSync` set to On (the default), the LFO fade time
recommences; when set to Off, it is triggered only by the first note. This will only be of
relevance when playing in legato style.


**Repeats**
Displayed as: `Repeats`
Initial value: Off
Range of adjustment: Off, 1 - 127


`Repeats` sets how many cycles of LFO waveform will be generated each time the LFO
is triggered. So if set to 1, you will only hear the effect of any LFO modulation for a single
cycle, and hence for a short duration (depending on the setting of **Rate** ).


**32**



**LFO 3 and LFO 4: The default menu display for LFO 3 is shown below:**


LFO 3      7/8

L3Waveform Triangle H
L3Rate   64

L3RateSync 8 beats


**LFO 3/4 Waveform**
Displayed as: `LxWaveform` (where x=3 or 4)
Initial value: Triangle
Range of adjustment: Triangle, Sawtooth, Square, Rand S/H


**This parameter is the menu-based equivalent of the panel Type button** 29 **, and**
**performs the same function: setting the basic waveform for LFO 3 or LFO 4.**


**LFO 3/4 Rate**
Displayed as: `LxRate` (where x=3 or 4)
Initial value: 64
Range of adjustment: 0 to 127


**This parameter is the menu-based equivalent of the panel Rate rotary control** 30 **,**
**and performs the same function: setting the rate (frequency) of LFO 3 or LFO 4.**


**LFO 3/4 Rate Sync**
Displayed as: `LxRateSync` (where x=3 or 4)
Initial value: 8 beats
Range of adjustment: See table at page 45 for full details


LFO Rate Sync allows the speed of the LFO to be synchronised to an internal or external
MIDI clock: the parameter selects the sync division factor. For LFO Sync Rate to be
operational, it must first be enabled with the **Sync** button 30 .

---

## Page 33

**The Arpeggiator**
Summit has a versatile Arpeggiator (Arp) which allows arpeggios of varying complexity
and rhythm to be played and manipulated in real-time. When the Arpeggiator is enabled
and a single key is pressed, its note will be retriggered. If you play a chord, the Arpeggiator
identifies its notes and plays them individually in sequence (this is termed an arpeggio
pattern or ‘arp sequence’); thus if you play a C major triad, the notes making up the pattern
will be C, E and G.



**Arp Rhythm**
As well as being able to set the basic timing and mode of the arp sequence (with the **Type**
control and the `SyncRate` parameter in the **Arp/Clock** menu), you can also introduce
further rhythmic variations by adjusting the **Rhythm** control 57 . The Arpeggiator comes
with 33 pre-defined arp sequences; use the **Rhythm** control to select one. In general
terms, the sequences increase in rhythmic complexity as the numbers increase; Rhythm 1 is
a series of consecutive crotchets, and higher-numbered rhythms introduce more complex
patterns, shorter duration notes (semiquavers) and syncopation.











The primary controls for the Arpeggiator are on the panel: other, secondary arp parameters

- including clock source, swing and sync rate – are set up in the **Arp/Clock** menu (see
below). The Arpeggiator is enabled by pressing the **Arp On** button 51 .


**Tempo**
The **Tempo** control 53 sets the basic rate of the arp sequence: the range is 40 to 240
BPM. If Summit is being synchronised to an external MIDI clock (see page 34), it will
automatically detect the incoming tempo and disable the internal clock. The tempo of the
arp sequence will then be determined by the external MIDI clock.


Note that **Tempo** sets the clock rate for all Summit’s tempo-synchronised features: e.g.,
Delay Sync and LFO Rate Sync, as well as the Arpeggiator rate.


Tempo control is also available on Page 1 of the **Arp/Clock** menu as the `ClockRate`
parameter.





Rhythm pattern may also be selected on Page 2 of the **Arp/Clock** menu with the Rhythm
parameter.


**Octave range**
The **Octave** control 56 allows upper octaves to be added to the arp sequence. Set to 1,
the sequence will contain only the notes played. When set to 2, the sequence is played
as previously, then immediately played again an octave higher. Higher values extend this
process by adding additional higher octaves. Note that settings other than 1 have the effect
of doubling, tripling, etc., the length of the sequence. The additional notes added duplicate
the complete original sequence, but octave-shifted. Thus a four-note sequence played with
**Octaves** set to 1 will consist of eight notes when **Octaves** is set to 2. The range available
is from one to seven octaves.


Arp octave range may also be selected on Page 2 of the **Arp/Clock** menu as the
`Octaves` parameter.


**Note duration**
The Gate control 55 sets the basic duration of the notes played by the Arpeggiator
(though this will be further amended by the **Rhythm** control and the `SyncRate` menu
setting). Gate length is a percentage of the step length so the time during which the gate
is open depends on the master clock speed. The lower the parameter value, the shorter
the duration of the note played. At its maximum value (127), one note in the sequence is
immediately followed by the next without a gap. At a value of 63, the note duration is exactly
half the beat interval (as set by the **Tempo** control), and each note is followed by a rest of
equal length.


**Key Latch**
The **Key Latch** button 52 plays the currently selected arp sequence repeatedly without
the keys being held. If further key(s) are pressed while the initial keys are being held down,
the extra note(s) will be added to the sequence. If further keys are pressed after releasing
all the notes, a new sequence consisting only of the new notes will be played.


**Arp data transmission**
Summit can transmit MIDI note data from the arpeggiator, and can also force the
arpeggiator to play notes according to received MIDI note data. See page 42 for more
information.


**The Arp/Clock Menu**
The following Arpeggiator settings are available in the **Arp/Clock** menu, which has four
pages. Note that some of these settings duplicate physical controls in the panel **ARP**
section.


Arp Menu Page 1:


CLOCK      1/4
ClockRate  120BPM H
Source   Auto
Status INT 120.00bpm


**Tempo**
Displayed as: `ClockRate`
Initial value: 120 BPM
Range of adjustment: 40 to 240 BPM


This parameter sets Summit’s internal clock rate in BPM. It provides the clock for Summit’s
tempo-synchronised features: Arpeggiator, Delay Sync and LFO Rate Sync.
This parameter duplicates the physical **Tempo** control 53 .



**Arp Mode**
When enabled, the Arpeggiator will play all notes held down in a sequence which is
determined by the setting of the **Type** control 57 . The options available are summarised
in the table below. The third column of the table describes the nature of the sequence in
each case.

|TYPE|DESCRIPTION|COMMENTS|
|---|---|---|
|`K `|Ascending|Sequence begins with lowest note played|
|`J `|Descending|Sequence begins with highest note played|
|`KJ`|Ascend/descend|Sequence alternates|
|`KJ`2|`KJ`2|As`KJ`, but lowest and highest notes are<br>played twice|
|Play|Key order|Sequence comprises notes in the order in<br>which they are played|
|Random|Random|The notes held are played in a continuously-<br>varying random sequence|
|Chord|Chord|The notes making up the sequence are played<br>simultaneously, as a chord|



Type selection is also available on Page 2 of the **Arp/Clock** menu as the `Type` parameter.


**33**

---

## Page 34

**Clock source**
Displayed as: `Source`
Initial value: Auto
Range of adjustment: Auto, Internal, Ext-Auto, MIDI, USB


Summit uses a master MIDI clock in order to set the tempo of the arpeggiator and to
provide a time base for synchronisation to an overall tempo. This clock may be derived
internally or provided by an external device able to transmit MIDI clock. The `Source`
setting determines whether Summit’s tempo-synchronised features (including the
Arpeggiator) will follow the tempo of an external MIDI clock source or follow the tempo set
by the ClockRate parameter. The options are:


      - **Auto**       - when no external MIDI clock source is present, Summit will default to the
internal MIDI clock. Tempo will be set by the `ClockRate` parameter. If an external
MIDI clock is present, Summit will synchronise to it.

      - **Internal**       - Summit will synchronise to the internal MIDI clock irrespective of what
external MIDI clock sources may be present.

      - **Ext-Auto**       - this is an auto-detect mode whereby Summit will synchronise to any
external MIDI clock source (via USB or MIDI connection). Until an external clock
is detected, Summit will run at its internal clock rate. When an external clock is
detected, Summit automatically synchronises to it. If external clock is subsequently
lost (or stopped), Summit’s tempo then “flywheels” to the last-known clock rate.

      - **MIDI**       - synchronisation will be to an external MIDI clock connected to the (DIN)
MIDI input socket. If no clock is detected, the tempo “flywheels” to the last-known
clock rate.

      - **USB**       - synchronisation to an external MIDI clock received via the USB connection.
If no clock is detected, the tempo “flywheels” to the last-known clock rate.


When set to either of the external MIDI clock sources the tempo will be at the MIDI
Clock rate received from the external source (e.g., a sequencer). Make sure the external
sequencer is set to transmit MIDI Clock. If unsure of the procedure, consult the sequencer
manual for details.


The fourth row of Page 1 confirms the current status of the clock source, including the
precise BPM. This row is read-only.


Most sequencers do not transmit MIDI Clock while they are stopped. Synchronisation of
Summit to MIDI Clock will only be possible while the sequencer is actually recording or
playing. In the absence of an external clock, the tempo may flywheel and will assume the
last known incoming MIDI Clock value. In this situation, the fourth row of the OLED will
display `FLY` . (Note that Summit does NOT revert to the tempo set by the `ClockRate`
parameter unless `Auto` is selected.)


**Status**
Row 4 of Page 1 confirms the current clock source and BPM in use. It is not userselectable for adjustment.


ARP       2/4
Type    Up   H
Rhythm    1
Octaves    1


**Arp Mode**
Displayed as: `Type`
Initial value: Up
Range of adjustment: See table in “Arp Mode” on page 33


This parameter duplicates the physical **Type** control 57 .


**Arp Rhythm**
Displayed as: `Rhythm`
Initial value: 1
Range of adjustment: 1 to 33


This parameter duplicates the physical **Rhythm** control 54 .


**34**



**Octave range**
Displayed as: `Octaves`
Initial value: 1
Range of adjustment: 1 to 6


This parameter duplicates the physical **Octave** control 54 .


Arp Menu Page 3:


ARP       3/4
Swing    50   H
SyncRate  16th
KeySync  Off


**Swing**
Displayed as: `Swing`
Initial value: 50
Range of adjustment: 20 to 80


If `Swing` is set to something other than its default value of 50, some further interesting
rhythmic effects can be obtained. Higher values lengthen the interval between odd and
even notes, while the even-to-odd intervals are correspondingly shortened. Lower values
have the opposite effect. This is an effect which is easier to experiment with than describe!
Adding Swing is a great way to introduce a groove, or rhythmically swung musical feeling to
your arp sequences.


**Arp Rate Sync**
Displayed as: `SyncRate`
Initial value: 16th
Range of adjustment: See table at page 45 for full details


This parameter effectively determines the beat of the arp sequence, based on the tempo
rate set by the `ClockRate` parameter.


**Arp Key Sync**
Displayed as: `KeySync`
Initial value: Off
Range of adjustment: Off or On


`KeySync` only applies when **Key Latch** 31 is On. It determines how the sequence


ARP       4/4
ArpVelMode Rhythm H


**Arp Velocity Mode**
Displayed as: `ArpVelMode`
Initial value: Rhythm
Range of adjustment: Rhythm or Played


Arp Velocity Mode sets the relative volume of the notes comprising the arp pattern. With
the default setting of Rhythm, the pattern will be played with a predetermined volume for
each note, regardless of how the keys making up the pattern were struck. For most of the
patterns, this will mean all the notes will have the same volume. However, some of the more
complex patterns already have velocity information associated with each step, so the notes
making up the pattern may differ slightly in volume, as this is what was intended when the
pattern was created.


If `ArpVelMode` is set to Played, the way each key is struck is taken into account and the
velocity value of each is applied to the step. This results in an arp pattern that more closely
replicates how the notes defining the pattern’s content were played. In order for the Played
mode to operate correctly, it is necessary to first assign a non-zero value to the Velocity
parameter on Page 1 of the **Env** menu (see page 30). Alternatively, assign Velocity as a
source in the Mod Matrix to control another synth parameter, such as Filter Frequency.

---

## Page 35

**The Effects Section**
Summit comes equipped with two sound effects (FX) sections – one per Part. FX can
be applied to the sound the synth is generating to add colour and character. When Multi
Patches are in use, FX may be added to Parts A and B independently. All FX parameters
are saved with the Patch.













The FX tools comprise analogue distortion and three digital “time-domain” effects: Reverb,
Chorus and Delay. Each effect has its own set of controls and you can use any or all FX
without restriction.


In addition, the **FX** Menu provides extensive control of additional parameters for the digital
FX. These may be used in parallel configuration, or arranged in series in any order: the
configurations are set up in the **FX** Menu.


A second menu – **FX Mod** - gives access to a 4-slot modulation matrix dedicated to the
FX section. This is entirely independent of the main modulation Matrix (accessed through
its own **Mod** menu), and allows you to apply modulation control to most primary FX
parameters. See page 39 for full details.


The FX processing section is active by default: the Bypass button 79 switches the digital
FX processing out of circuit: it does not bypass the Distortion processor.


**Distortion**
Distortion may be added with the single **Level** control 68 . A controlled amount of
distortion is added after the VCA, in the analogue domain, and affects the sum of all sixteen
voices and any external audio inputs applied. (See the block diagram at page 21.) This
means the distortion characteristic will change as the amplitude of the signal changes over
time as a result of the Amplitude Envelope, and also with the number of active voices.


The output from the Distortion processor is then routed to the other FX.


Note that “per-voice” distortion may be added either post-filter by adjusting `Post`
`Filter Drive` on Page 3 of the **Voice** menu, or pre-filter by adjusting the **Overdrive**
control in the Filter section 62 .


**Chorus**
Chorus is an effect produced by mixing a continuously delayed version of the signal with
the original. The characteristic swirling effect is produced by the Chorus processor’s own
LFO making small changes in the delays. The changing delay also produces the effect of
multiple voices, some of which are pitch-shifted; this adds to the effect.


Summit has three stereo Chorus programs, named **2 Tap**, **4 Tap** and **Ensemble**, selected
by the **Type** button 77 . The names reflect the nature of traditional chorus generation,
which was to mix together several versions of the same signal, each with a different and
varying delay, derived from a multi-tap delay line. The amount of Chorus effect added to the
“dry” signal is adjusted by the **Level** control 78 . The **Rate** control 76 sets the frequency
of the Chorus processor’s dedicated LFO. Lower values give a lower frequency, and hence
a sound whose characteristic changes more gradually. A slow rate is often more effective.


There are further Chorus parameters available for adjustment in the **FX** Menu.


**35**



**Delay**
The Delay FX processor produces one or more repetitions of the note played. Although the
two are intimately related in an acoustic sense, delay should not be confused with reverb in
terms of an effect. Think of delay simply as “Echo”.


The **Time** control 69 sets the basic delay: the note played will be repeated after a fixed
time. Higher values correspond to a longer delay. If Time is varied while a note is being
played, pitch shifting will result.


It is often desirable to synchronise echoes to tempo: on Summit this can be done by
selecting **Sync** 70 . The **Time** control then invokes Page 4 of the **FX** menu, and varies the
`DelaySync` parameter, which is displayed on the OLED while the control is adjusted.
The sync value is limited by the maximum delay time of 1.4 seconds, consequently some
combinations of **ClockRate** (set on Page 1 of the **Arp/Clock** menu) and `DelaySync`
result in truncating the delay time to the maximum calculated sync rate permissible, i.e., the
delay time will reduce, but it will remain in sync.


The output of the delay processor is connected back to the input, at a reduced level; The
**Feedback** control 71 sets the level. This results in multiple echoes, as the delayed signal
is further repeated. With **Feedback** set to zero, no delayed signal at all is fed back, so
only a single echo results. As you increase the value, you will hear more echoes for each
note, though they still die away in volume. Setting the control in the centre of its range
(64) results in about 5 or 6 audible echoes; at the maximum setting the decay in volume is
almost imperceptible and the repetitions will still be audible after a minute or more.


The **Level** control 72 adjusts the level of the echoes: at the maximum setting (127), the
first echo is approximately the same volume as the initial, dry note.


There are further Delay parameters available for adjustment in the **FX** Menu.


**Reverb**
Reverberation (reverb) adds the effect of an acoustic space to a sound. Unlike delay,
reverb is created by generating a dense set of delayed signals, typically with different
phase relationships and equalisations applied to re-create what happens to sound in a real
acoustic space.


Summit provides three reverb presets, selected by the **Size** button 74 . The presets are
simply numbered **1**, **2** and **3**, and set the `RevSize` parameter (see page 37) to values
of 0, 64 or 127 respectively, thus simulating spaces of different sizes.


The **Time** control 73 sets the basic reverb time of the selected space and determines how
long it takes the reverb to die away to inaudibility. The **Level** control 75 adjusts the volume
of the reverb.


**The FX Menu**
The following additional parameters for the three time-domain effects are available in the
**FX** menu. Two menu pages are dedicated to Chorus (Pages 2 and 3) and two to Delay
(Pages 4 and 5); Reverb has three pages (Pages 6 to 8). There is one further page (Page
1) with “global” parameters affecting all three effects.


**Global FX page:**
**The default menu display is shown below:**


FX GLOBAL    1/8
WetLevel  127   H
DryLevel  127
Routing  Parallel


The parameters available on the Global FX page affect all three time-domain FX
processors (Chorus, Delay and Reverb).


**Wet and Dry Levels**
Displayed as: `WetLevel` `DryLevel`
Initial value: 64 and 127
Range of adjustment: 0 to 127 0 to 127


The inclusion of the ‘Wet” and “Dry” parameters are used here to assist with importing
patches from our Peak synthesizer. They have no effect on the engine of Summit.

If you wish to have a different level for the effects compared to the dry level you can send
the FX to a separate output to the Synth engine by adjusting the setting on page 13 of the
**Settings** menu. (See page 43).

---

## Page 36

**FX Routing**
Displayed as: `Routing`
Initial value: Parallel
Range of adjustment: Parallel, D->R->C, D->C->R, R->D->C, R->C->D,
C->D->R, C->R->D


When using more than one of the three time-domain effects (Chorus = C, Delay = D
and Reverb = R) simultaneously, the overall effect will differ depending on the order of
processing. For example, if Delay precedes Reverb, each echo added to notes by the Delay
processor will initiate its own reverberation. If Delay follows Reverb, the Delay processor
will attempt to generate a multiplicity of fresh reverberations as repeats. `Routing` allows
you to arrange the three time-domain processors in series in any order, or to configure them
to process sounds in parallel, i.e., simultaneously, with the outputs being blended together.
In parallel (the default configuration), the overall result is subtly different from any of the
series configurations.


**Chorus pages:**


CHORUS      2/8
ChorDepth  64   H
ChorFback  +0


CHORUS      3/8

LoPass   90   H
HiPass    2


**Chorus Depth**
Displayed as: `ChorDepth`
Initial value: 64
Range of adjustment: 0 to 127


The `ChorDepth` parameter determines the amount of LFO modulation applied to the
Chorus delay time, and thus the overall depth of the effect. A value of zero results in no
chorus effect being added.


**Chorus Feedback**
Displayed as: `ChorFback`
Initial value: 0
Range of adjustment: -64 to +63


The Chorus processor has its own feedback path between output and input, and a
degree of feedback can be applied to get a more effective sound. Negative values of the
`ChorFback` parameter mean the signal being fed back is phase-reversed: High values –
positive or negative – can add a dramatic “swooping” effect. Adding feedback and keeping
the value of `ChorDepth` low will turn the Chorus FX into a flanger.


**Chorus HF EQ**
Displayed as: `LoPass`
Initial value: 90
Range of adjustment: 0 to 127


The `LoPass` parameter adjusts a simple HF filter within the chorus processor. Adjusting
this will enhance or mask some of the additional higher harmonics added to the sound by
the Chorus effect. When `LoPass` is set to its maximum value of 127, the filter is fully open.


**Chorus HF EQ**
Displayed as: `HiPass`
Initial value: 2
Range of adjustment: 0 to 127


The `HiPass` parameter adjusts a simple LF filter within the chorus processor, letting you
refine the Chorus effect further. With `HiPass` set to zero, the filter is fully open.

**36**



**Delay pages:**


DELAY      4/8
DelaySync 4th T  H
LP Damp   85
HP Damp   0


DELAY      5/8

L/R Ratio  1/1  H
SlewRate  32

Width   127


**Delay Sync**
Displayed as: `DelaySync`
Initial value: 4th T
Range of adjustment: See table at page 36 for full details


Delay time may be synchronised to the internal or external MIDI clock, using a wide variety
of tempo dividers/multipliers to produce delays from about 5 ms to 1 second.


The value of `DelaySync` is also displayed while the front panel **Time** control 69 is
being adjusted, when **Sync** 70 is set On.





**HF Damping**
Displayed as: `LP Damp`
Initial value: 85
Range of adjustment: 0 to 127


Echoes produced acoustically by reflections in physical spaces decay at different rates
at different frequencies, depending on the type of surface producing the reflection. The
two Damping parameters `LP Damp` and `HP Damp` allow a simulation of this effect. `LP`
`Damp` (Lo-pass Damping) is a filter which can be used to reduce the brightness of later
echoes: with the parameter set to its maximum value of 127, the filter is fully open.


Note that the varying damping only applies to the delayed notes, not to the initial one. See
also the Damping parameters in the Reverb processor.


**LF Damping**
Displayed as: `HP Damp`
Initial value: 0
Range of adjustment: 0 to 127


This has a similar effect to `LP Damp`, but is a hi-pass filter. When the parameter is set
to zero, the filter is fully open: as the value is increased, later echoes will be progressively
reduced in LF content.


As with `LP Damp`, the varying damping only applies to the delayed notes, not to the initial
one. See also the Damping parameters in the Reverb processor.


**Left-Right Ratio**
Displayed as: `LR Ratio`
Initial value: 1/1
Range of adjustment: 1/1, 4/3, 3/4, 3/2, 2/3, 2/1, 1/2, 3/1, 1/3, 4/1, 1/4


The value of this parameter is a ratio, and determines how each delayed note is distributed
between the left and right outputs. Setting `LR Ratio` to the default 1/1 value places all
echoes centrally in the stereo image. With other values, echoes are alternated rhythmically
between left and right at simple ratios of the delay time: settings of 1/2 or 2/1 produces the
familiar “ping-pong” effect of equally spaced echoes alternating between left and right.

---

## Page 37

**Delay Slew Rate**
Displayed as: `SlewRate`
Initial value: 32
Range of adjustment: 0 to 127


The value of `SlewRate` affects the nature of the sound while the Delay Time is being
varied. Varying delay time produces pitch-shifting. With `Slew Rate` set to the maximum
value (127), almost no pitch-shift effects will be heard as the **Time** control 44 is adjusted.
With lower values, the pitch-shift effects become more evident. As the purpose of varying
delay time in performance is generally to produce pitch shift artefacts, a medium value is
usually desirable.


**Width**
Displayed as: `Width`
Initial value: 127
Range of adjustment: 0 to 127


The `Width` parameter is only relevant to settings of LR Ratio which result in the echoes
being split across the stereo image. With its default value of 127, any stereo placement of
delayed signals will be fully left and fully right. Decreasing the value of `Width` reduces the
width of the stereo image and panned echoes tend towards the centre position.


**Reverb pages:**


REVERB      6/8
PreDelay 40   H
LP Damp   50
HP Damp   1


REVERB      7/8

RevSize   64   H
ModDepth  64

ModRate   4


REVERB      8/8
LoPass   74   H
HiPass    0


**PreDelay**
Displayed as: `PreDelay`
Initial value: 40
Range of adjustment: 1 to 127


In a very large space, the first reflections making up the reverberation are not heard
immediately. `PreDelay` controls how soon after the start of the initial note the
reverberation begins, and thus allows a more accurate simulation of a real space to be
created. With `PreDelay` set to its maximum value (127), the first reflections are delayed
by approximately half a second.


**37**



**HF Damping**
Displayed as: `LP Damp`
Initial value: 50
Range of adjustment: 0 to 127


This parameter performs the same function for the reverb processor as the corresponding
one in the Delay processor, in that it simulates the effect of high-frequency absorption by
different surfaces. The low-pass filter used to create this effect is fully open when
`LP Damp` is set to its maximum value of 127.


**LF Damping**
Displayed as: `HP Damp`
Initial value: 1
Range of adjustment: 0 to 127


This parameter performs the same function for the reverb processor as the corresponding
one in the Delay processor, in that it simulates the effect of low-frequency absorption by
different surfaces. The high-pass filter used to create this effect is fully open when
`HP Damp` has a value of zero.
**Size**
Displayed as: `RevSize`
Initial value: 64
Range of adjustment: 0 to 127


The `RevSize` parameter alters the reverberation character: larger values introduce
additional and more prominent reflections, simulating the effect of a larger physical space.
Note that the **Size** button 74 sets `RevSize` to 0, 64 or 127, so the menu option allows
finer adjustment between these values.


**Reverb Modulation**
Displayed as: `ModDepth` `Modrate`
Initial value: 64 and 4
Range of adjustment: 0 to 127


The reverb processor includes a dedicated modulation source, which can be used to
alter the reverb time (set with the **Time** control 73 ). Two parameters are provided:
`ModDepth`, which controls the degree of modulation and `ModRate`, which controls the
modulation rate.


**Reverb HF EQ**
Displayed as: `LoPass`
Initial value: 74
Range of adjustment: 0 to 127


This parameter controls a simple low-pass filter, constituting an HF EQ section affecting
the reverberation itself. The effect differs the `LoPass` Damping parameter: `LoPass`
is a simple filter for the overall reverberation (not the initial note) while `LP` `Damp` is a
coefficient defining how the reverb algorithm itself operates on high frequencies. The filter
is fully open when the parameter has its maximum value of 127.


**Reverb LF EQ**
Displayed as: `HiPass`
Initial value: 0
Range of adjustment: 0 to 127


`HiPass` is the parameter controlling a corresponding high-pass filter affecting the lowfrequency content of the reverberation. The filter is fully open when the parameter is zero.

---

## Page 38

**The Modulation Matrix**
The power of a versatile synthesiser lies in its ability to interconnect the various controllers, sound generators and processing blocks such that one block is controlling – or “modulating”

- another, in as many ways as possible. Summit provides considerable flexibility of control routing, and there is a dedicated menu for this, the **Mod** Menu. As with every other aspect of
Summit, the Modulation Matrix routings for each of the two synths generating Parts A and B may be configured independently by selecting **A** or **B** in **MULTIPART CONTROL** when using a
Multi Patch.


The available modulating sources and destinations to be modulated can be thought of as the inputs and outputs of a large matrix:


MOD DESTINATIONS



Direct

ModWheel

AftTouch

ExprPED1

BrthPED2

Velocity

Keyboard

Lfo1+

Lfo1+/
Lfo2+

Lfo2+/
AmpEnv

ModEnv1

ModEnv2

Animate1

Animate2

CV +/
Lfo3+

Lfo3+/
Lfo4+

Lfo4+/
BndWhl+

BndWhl





















|O1|Osc O1|Osc Osc|Osc Osc|Osc Osc|Osc Osc|Osc Osc|Osc Osc|Osc Osc|Osc Osc|Osc Osc|Osc Osc|Osc Osc|Osc Noi|Noi Rin|Rin Vca|Vca Filt|Filt Filt|Filt Filt|Filt Filt|Lfo Lfo|Lfo Am|Am Am|Am Am|Am Mo|Mo Mo|Mo Mo Mo Mo|Mo Mo FM FM|FM FM|FM FM|O3 FM|O3 Ns>|Ns> Ffre|Ffre|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
||||||||||||S|lot1|~~S~~|~~lot 1~~|~~ 6~~|V<br>Ve|~~V~~<br>Vel<br>**Velo**<br>eloc<br>locit|~~Velo~~<br><br>~~eloc~~<br>ocit<br>**city**<br>ity<br>y|~~city~~<br><br>~~ity~~<br>y||||~~O~~<br><br><br>|Os<br>~~Osc~~<br>~~sc2~~<br><br><br>|c2S<br>~~2Sh~~<br>~~Sh~~<br><br><br>|hpe<br>~~pe~~<br>~~e~~<br><br>**Depth**||||||||
|||||||||||||||||~~Lf~~|L<br>~~Lf~~<br>~~**Lfo**~~<br>~~Lfo2~~<br>~~o2+/~~|Lfo<br>fo2<br>~~o2+~~<br>~~**2+**~~<br>~~+~~<br>~~-~~|2+<br>+<br>|||~~O~~|~~**O**~~<br>~~O~~sc<br>sc2|~~**c2**~~<br>2Sh<br>Shp|~~**hp**~~<br>pe<br>e|||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||
|||||||||||||||||||||||||||||||||||



The example here shows how any two sources, in this case Velocity and LFO 2, can
simultaneously modulate the same parameter, in this case Osc 2 Shape. Many mod matrix
assignments will only use a single source. Note that the two modulation sources are
effectively multiplied together, and the **Depth** parameter controls the overall degree of
modulation. The diagram depicts a single matrix “slot”: each of the two Summit synths has
16 such slots, allowing an enormous range of modulation possibilities.


Press the **Mod** button 9 to open the Modulation Menu, which comprises 16 pages, one
for each slot. Select a slot with the **Page** `I` and **Page** `H` buttons. The page lets you define
which (one or two) modulation sources are to control – i.e., modulate - a ‘destination’
parameter. The routing possibilities available in each slot are identical, and hence the
control description below is applicable to all 16 slots.


**The default menu display for Slot 1 is shown below:**


:sA  [Slot 1]  sB:

:HDirect : Direct
Destin   O123Ptch

Depth    +0


**38**

---

## Page 39

In addition, the Modulation Menu lets you assign the two **ANIMATE** buttons as sources
(see page 15).


**NOTE: The FX Modulation Matrix Menu**
In addition to the sources and destinations available in the main Modulation Matrix, four
additional matrix routing slots specifically dedicated to the FX section are available in
the **FX Mod** Menu. These allow most Modulation Matrix sources to directly modulate FX
parameters. See page 39 for full details.


Each slot has two inputs, A and B, which allows each destination parameter to be
modulated by two different sources. The three buttons to the left of the OLED display
select Rows 2, 3 or 4 for adjustment, but note that the Row 2 button toggles source
selection between slot inputs A and B. Source A is displayed on the left of Row 2 and
Source B on the right: in the default display shown above, both are set to `Direct` (no
modulation selected).


Use the **Page** `I` and **Page** `H` buttons to select one of 16 slots. All the slots have the
same selection of sources and destinations and any or all can be used. The same source
can control multiple destinations in different slots, and similarly, one destination can be
controlled by multiple sources by using several slots.


**Modulation Source**
Displayed as: `:sA [Slot n] sB:` (where n= slot number;
the two sources are displayed on Row 2)
Initial value: Direct (both A and B sources)
Range of adjustment: see table at page 46 for list of available sources


This lets you select a control source (modulator), which will be routed to the synth element
selected by `Destin` (see below). Setting both `sA` and `sB` to Direct means when the
Depth for the Slot is set to a non-zero value, a fixed change will be applied to the value of
the selected destination parameter (i.e., there is no time-varying modulation).


Note that the list of sources includes Expression pedals. If you connect an Expression
pedal to either of the rear panel pedal connectors, they can be selected to control any
destination you wish in the normal way. If you wish an Expression pedal to control overall
synth volume in a natural way, choose `VcaLevel` as the routing destination for `sA` and
`AmpEnv` for `sB` .


The CV input is also available as a source for the Mod Matrix. The CV input can be routed
to any of the available mod destinations. The CV input has been designed to respond to
control inputs without aliasing up to just over 1 kHz (which roughly corresponds to two
octaves above middle C).



**Modulation Depth**
Displayed as: `Depth`
Initial value: 0
Range of adjustment: -64 to +63


The `Depth` parameter sets “how much” control is being applied to the Destination – i.e.,
the parameter being modulated by the selected source(s). If both Source A and Source B
are active in the slot in question, `Depth` controls their combined effect.









**The FX Modulation Matrix**


Pressing **FX Mod** 9 opens the FX Mod Matrix menu. The FX Modulation Matrix is
effectively an extension of Summits’ main Modulation Matrix, but is devoted solely to using
various internal Summit sources to modulate FX parameters. It has four “slots” each with
two inputs, so you can simultaneously modulate up to four different FX parameters from up
to eight separate sources. It is set up in the same manner as the main Modulation Matrix.
The four pages are identical, and each allows one slot to be configured.


**The default menu display for Slot 1 is shown below:**


:sA [FxSlot 1] sB:

:HDirect  : Direct
Fx Destin Dist Lev

Depth    +0


As with the main Modulation Matrix, each slot has two inputs, A and B, which allows each
destination FX parameter to be modulated by two different sources. The three buttons to
the left of the OLED display select Rows 2, 3 or 4 for adjustment, but note that the Row 2
button toggles source selection between slot inputs A and B. Source A is displayed on the
left of Row 2 and Source B on the right: in the default display shown above, both are set to
`Direct` (no modulation selected).



**Modulation Destination**
Displayed as: `Destin`
Initial value: O123Ptch
Range of adjustment: see table on page 46 for available destinations list


This sets the parameter to be controlled by the selected source (or sources) in the
currently selected slot. The range of possibilities includes:
parameters that directly affect the sound:

     - three parameters per oscillator (Pitch, Vsync and Shape)

     - global pitch (O123Ptch)

     - the five mixer inputs from the oscillators, noise source, ring modulator and the
mixer output (see Tip below)

     - Filter frequency, resonance and distortion
parameters that can also act as modulating sources (thus permitting recursive
modulation):

     - LFO 1 & 2 frequency

     - the Attack, Decay and Release phases of all three Envelopes

     - Frequency Modulation of oscillators (FM) by filter other oscillators or Noise


**39**

---

## Page 40

Direct

ModWheel

AftTouch

ExprPED1

BrthPED2

Velocity

Keyboard

Animate1

Animate2

CV +/
Lfo3+

Lfo3+/
Lfo4+

Lfo4+/
BndWhl+

BndWhl


FX MOD DESTINATIONS


|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|Col15|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
|||||||~~nima~~|~~e 1~~||||||||
|||||||||||Chor|us Lev|el|||
|||||||LFO 3|||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||
||||||||||||||||



**FX Modulation Source**
Displayed as: `:sA and :sB`
Initial value: Direct
Range of adjustment: see table at page 46 for list of available sources


**FX Modulation Destination**
Displayed as: `FX Destin`
Initial value: Dist Lev
Range of adjustment: see table at page 46 for list of available
destinations


**FX Modulation Depth**
Displayed as: `Depth`
Initial value: 0
Range of adjustment: 64 to +63


The Depth parameter sets “how much” control is being applied to the Destination – i.e., the
parameter being modulated by the selected source(s). If both Source A and Source B are
active in the slot in question, Depth controls their combined effect. If no sources selected,
the **Depth** control can be used to adjust the “amount” of the destination parameter. Setting
a negative value of **Depth** has the effect of reducing the effect of the destination parameter
as set by its own control or menu option.


**The Settings Menu**
Press the **Settings** button 9 to open the **Settings** Menu. This menu has 31 pages,
numbered from 1 to 9, then from A to V. It contains a set of synth and system functions
which, once set up, will not need to be accessed on a regular basis. The **Settings** Menu
includes global synth settings, Patch backup routines, MIDI and pedal settings, I/O
routings and the 16 user-definable Oscillator Tuning Tables, among other functions.


The **Settings** Menu defines settings which are global for the synth, and are not saved with
individual Patches. However, it is possible to keep the current contents of the **Settings**
menu by opening **Settings** and pressing **Save** 11 . This ensures the settings (such as
Tuning Tables, `VelShape` and Patch Memory Protection) are kept after power-cycling.





**System pages:**


SYSTEM      1/V
Protect  Off   H
Pickup   Off
Brightness 64


SYSTEM      2/V
Msg Time  64   H
Version  070.618
H Calibrate


**Patch Memory Protection**
Displayed as: `Protect`
Initial value: Off
Range of adjustment: On or Off


Setting `Protect` to On disables Summit’s Patch Save function: subsequently, pressing
**Save** will generate the display message below:


Cannot Save Patch
Memory Protect ON


This is a useful function if you need to be sure Patches already saved (including factory
Patches) cannot be overwritten.


If `Protect` is Off, pressing **Save** will store all the current synth settings, including those
of the **Settings** menu. The message below will be displayed:


Settings Saved with
PROTECT OFF


**Pickup**
Displayed as: `Pickup`
Initial value: Off
Range of adjustment: On or Off


The setting of `Pickup` allows the current physical position of Summit’s rotary controls to
be taken into account. When `Pickup` is Off, adjusting any of Summit’s rotary controls will
produce parameter change and a potentially immediately audible effect (a small difference
between the parameter value corresponding to the control’s physical position and the value
currently in force for the Patch may result in the effect being inaudible). When set to On,
the control needs to be moved to the physical position corresponding to the value of the
parameter saved for the currently loaded Patch, and will only alter the parameter value once
that position is reached. For parameters with a range of 0 to 255, this means the 12 o’clock
position will correspond to a value of 127; for parameters with a range of -64 to +63, the
12 o’clock position will correspond to a value of zero.


**Brightness**
Displayed as: `Brightness`
Initial value: 64
Range of adjustment: 0 to 127


Adjusts the brightness of the OLED display.



**40**

---

## Page 41

**Message Time**
Displayed as: `Msg Time`
Initial value: 64
Range of adjustment: 0 to 127


`Msg Time` sets the time for which parameter values (and the saved value for the current
Patch) are displayed when a rotary control is adjusted. The maximum time (value of 127) is
equivalent to approx. 3 seconds.


**OS version**
Displayed as: `Version`


This is read-only data, and reports Summit’s OS (Operating System) version. This lets you
ensure you have the most up-to-date OS installed.


**Auto Calibration**
Displayed as: `Calibrate`


Pressing the Row 4 button initiates a calibration routine which sets up the filters, VCAs
and distortion circuitry accurately. This will have been done at the factory and should not
need to be run again, but the routine has been included for good measure. The procedure
takes several minutes, and the synth should not be touched while in progress. Note that the
routine overrides the master volume control and sets it to maximum.


**WARNING:** The test generates various tones which will be present at the synth’s
outputs; we recommend you mute or turn off any external amplifier or loudspeakers
connected as these tones will be at full volume.


When the calibration routine is complete, the display shows:


Calibration Complete
Re-Power Now


**Synth page:**


SYNTH      3/V
VelShape  64   H
TuneCents  +0
Transpose  +0


**Key Response**
Displayed as: `VelShape`
Initial value: 64
Range of adjustment: 0 to 127


This parameter modifies the synth’s response to the velocity curve set on the keyboard. The
default value of 64 results in a linear relationship between the velocity curve and the synth’s
response. Reducing the value will result in lighter key touches producing a greater volume;
a higher value results in the opposite. You can set the `VelShape` parameter to suit your
normal playing style.


**Master Fine Tuning**
Displayed as: `TuneCents`
Initial value: 0
Range of adjustment: -50 to +50


This control adjusts the frequencies of all the Oscillators by the same small amount,
allowing you to fine-tune the whole synth to another instrument if necessary. The
increments are cents (1/100 of a semitone), and thus setting the value to 50 tunes the
synth to a quarter-tone midway between two semitones. A setting of zero tunes keyboard
with the A above middle C at 440 Hz – i.e., standard Concert Pitch.


**41**



**Transpose**
Displayed as: `Transpose`
Initial value: +0
Range of adjustment: -12 to +12


`Transpose` is a useful global setting which “shifts” Summit’s keyboard up or down one
semitone at a time. It also applies the same “shift” to received MIDI Note data, so if you are
playing Summit from a master MIDI keyboard or controlling it from a sequencer, you can still
use transposition. `Transpose` differs from oscillator tuning in that it modifies the control
data from the keyboard rather than the actual oscillators. Thus setting `Transpose` to
+4 means you can play with other instruments in the actual key of E major, but only need to
play white notes, as if you were playing in C major.


Note `Transpose` does not affect Note data generated by the arpeggiator.


**MIDI pages:**


MIDI CHANNEL   4/V
PartA Chan  2   H
PartB Chan  3
Globl Chan  1


MIDI CONTROL   5/V
Local   On   H
Arp>MIDI  On


MIDI ENABLE   6/V
CC/NRPN  Rec+TranH
Bank/Patch Rec+Tran


MIDI protocol provides for 16 channels of data. This allows up to 16 devices to co-exist on
a MIDI network, provided each is assigned to operate on a different MIDI channel.


**Assign MIDI Channels - Part A**
Displayed as: `PartA Chan`
Initial value: 2
Range of adjustment: 1 to 16


Summit’s bi-timbral architecture effectively means it comprises two independent
synthesisers, one for each Part. When working with Multi Patches, you can configure it
to receive and transmit MIDI data for each of the two Parts on separate channels, for the
greatest flexibility of interfacing with external equipment.


`PartA Chan` lets you select which MIDI channel is to be used for MIDI data relating to
Part A.


No data is transmitted or received on the Single MIDI channels when Summit is in Multi
Patch mode. How Summit handles MIDI data in and out in Multi Patch mode is further
modified by the **MULTI MODE** in use. See page 46 for more details.


**Assign MIDI Channels - Part B**
Displayed as: `PartB Chan`
Initial value: 3
Range of adjustment: 1 to 16


`PartB Chan` lets you select which MIDI channel is to be used for MIDI data relating to
Part B. In all other respects, it operates described for as `PartA Chan` above.


**Assign MIDI Channels (Global)**
Displayed as: `Globl Chan`
Initial value: 3
Range of adjustment: 1 to 16


The Global MIDI channel should be used in Single Patch mode. No data is transmitted on
the Global MIDI channel when Summit is in Multi Patch mode.

---

## Page 42

**Local Control On/Off**
Displayed as: `Local`
Initial value: On
Range of adjustment: Off or On


In normal operation (with Local set to On), all of Summit’s physical controls are active, and
also transmit their settings as MIDI data, provided CC/NRPN on **Settings** Menu Page 6 is
set to either Transmit or Rec+Tran (see MIDI Control data setting below). With `Local` set
to Off, the physical controls no longer vary any internal Summit parameters, but still output
their values as MIDI data in the same way.


**Arp MIDI mode**
Displayed as: `Arp>Midi`
Initial value: On
Range of adjustment: Off or On


This setting determines how the arpeggiator handles MIDI data.


    - Off: the arp responds to incoming MIDI note data, either via the MIDI IN DIN port or
the USB port. Control data is transmitted from both the MIDI OUT and USB ports. If
the note data is received at the MIDI IN port, it is also retransmitted to MIDI THRU.

    - On: In this setting, the arp responds to received MIDI note data in the same manner,
but additionally transmits arpeggiator note data via both the MIDI OUT and USB
ports, along with control data.


**MIDI control data**
Displayed as: `CC/NRPN`
Initial value: Rec+Tran
Range of adjustment: Disabled, Receive, Transmit, Rec+Tran


With the default `CC/NRPN` setting of Rec+Trans, Summit’s physical controls transmit
their settings as MIDI CC or NRPN data (see table at page 47). Summit also responds
to received MIDI CC/NRPN data with this setting. You can choose to only transmit MIDI
data and not receive it (Transmit), or to receive it but not transmit (Receive). The fourth
option, Disabled, effectively isolates Summit from any other MIDI equipment to which it
is connected. See also Local Control On/Off above. Note CC/NRPN messages do not
include Patch data, which is handled separately as Program Change messages – see
Bank/Patch below.


**Patch Select via MIDI**
Displayed as: `Bank/Patch`
Initial value: Rec+Tran
Range of adjustment: Disabled, Receive, Transmit, Rec+Tran


This setting controls how Summit handles MIDI Program Change and Bank Change
messages. With the default setting of Rec+Trans, Summit sends a Program/Bank Change
message whenever a new Patch is loaded, and will also load a Patch when told to by an
external MIDI controller, such as the Novation SL MkIII. As with MIDI control data (above),
you can choose to set Receive or Disabled, so Summit does not transmit Program/Bank
Change messages when you change Patches, or to set Transmit or Disabled, so Summit
does not respond to Program/Bank Change messages from external equipment.



These two menu pages are concerned only with pedals of the switch (on/off) type. If you
are using one or more Expression pedals, these may be connected to either or both of
the two **PEDAL** sockets on the rear of the synth. There are no Settings Menu options for
Expression pedals: they are assigned in the Mod Matrix on a per-Patch basis.


**Pedal Types**
Displayed as: `Ped1Sense` `Ped2Sense`
Initial value: Auto and Auto


pedal!) Provided the default value of Auto is still set, the polarity will be correctly sensed.


**Pedal Modes**
Displayed as: `Ped1Mode` `Ped2Mode`
Initial value: Animate1 and Animate2
Range of adjustment: Animate1, Sustain, Sostnuto Animate1, Sustain, Sostnuto


The Pedal Mode settings determine what you want the switch pedals to do. The two pedals
can act as foot switches for Summit’s Animate functions: in this case, pressing a pedal
triggers the Animate effect that has been defined within the Patch. You can alternatively
assign either pedal to be a Sustain or a Sostenuto pedal (like the middle pedal on a threepedal piano). When set to Sostenuto, notes played while the pedal is being pressed will
be sustained. Once the pedal has been depressed, any further notes will not be sustained.
This is useful for playing melodies over a held chord.


**Misc Settings page**


MISC SETTINGS  9/V
VolRange  0dB  H

InputGain  64
Initialise IniPatch


**Volume Range**
Displayed as: `VolRange`
Initial value: 0 dB
Range of adjustment: -6 dB, -3 dB, 0 dB


This global parameter is effectively a 3 or 6 dB pad (or level reduction) in the main audio
outputs. It is useful when the equipment Summit’s outputs are connected to have a
restricted range of input level and you need to limit the maximum level Summit can output.


**External Input Gain**
Displayed as: `InputGain`
Default value: 64
Range of adjustment: 0 to 127


use for them is to route them to the FX section, so Summit’s FX processing may be applied.
This routing is enabled on Page C of the **Settings** menu (see page 43).


**Initialise Mode**
Displayed as: `Initialise`
Default value: IniPatch
Range of adjustment: IniPatch, Live


With the default setting of `IniPatch`, pressing the **Initialise** button 2 will load an
Initial Patch, complete with all its default parameter values, giving you a useful starting point
for creating new sounds. In Single Patch mode, this will be `Init Patch` ; in Multi Patch
mode, only the Part currently selected by **MULTIPART CONTROL** will be `Init Patch` .


By setting the `Initialise` parameter to `Live`, Summit will retain all current control
panel settings when loading the Initial Patch, so any sound modification you have been
working on will now be applied to a copy of the Initial Patch when **Initialise** is pressed.
Note that this applies only to the physical controls; any adjustments made to additional
menu settings will be overridden and replaced by those pertaining to the Initial Patch.





**Pedal pages:**


**42**



PEDAL SW SENSE  7/V
Ped1Sense Auto  H
Ped2Sense Auto


PEDAL SW MODE  8/V
Ped1Mode  Animate1H
Ped2Mode  Animate2

---

## Page 43

**Output Routing Page:**


OUTPUT ROUTING  A/V
PartA Out Main  H

PartB Out Main
PhonesOut Main


**Main Output Routing – Part A**
Displayed as: `PartA Out`
Default value: Main
Range of adjustment: Main, AUX


`PartA Out` lets you choose which of Summit’s two stereo outputs Part A is routed to.


**Main Output Routing – Part B**
Displayed as: `PartB Out`
Default value: Main
Range of adjustment: Main, AUX


See above for details.
`PartB Out` lets you choose which of Summit’s two stereo outputs Part B is routed to.


**Headphone Source**
Displayed as: `PhonesOut`
Default value: Main
Range of adjustment: Main, AUX, Split


`PhonesOut` is set to Main, you will hear both Parts in full stereo.


The third option, Split, routes a mono (L+R) sum of the signal assigned to the Main Output
to the left earpiece, and a mono sum of the signal assigned to the AUX Output to the right.
This is a useful setting to use if you are sending the two Parts to different outputs.


**FX Pages:**


The Settings menu has three pages related to Summit’s FX sections.


FX ROUTING    B/V
FxA Out  Main  H
FXB Out  Main


FX SOURCES    C/V
FxA Source Synth  H
FXB Source Synth


EXTERNAL FX DRY D/V
FxA Level 127  H
FxB Level 127


**43**



**FX Routing – Part A**
Displayed as: `FxA Out`
Default value: Main
Range of adjustment: Main, AUX


Summit lets you route the “wet” outputs of the two FX processors (for Parts A and B) – the
processed signal - independently of the “dry”, or unprocessed signal. The default setting is
for the output of both processors to be routed to the Main Output, but you can route either
or both of them to the AUX Output instead if you wish.


`FxA Out` lets you choose which stereo output the Part A processor is routed to.


**FX Routing – Part B**
Displayed as: `FXB Out`
Default value: Main
Range of adjustment: Main, AUX


See above for details.


`FxB Out` lets you choose which stereo output the Part B processor will be routed to.


**FX Source – Part A**
Displayed as: `FxA Source`
Default value: Synth
Range of adjustment: Synth, Extern


The default setting – Synth – routes the final output of Summit’s Part A synth signal chain
to the input of the Part A FX processor, in order that effects can be added to the synth
sound.


**FX Source – Part B**
Displayed as: `FxB Source`
Default value: Synth
Range of adjustment: Synth, Extern


The default setting – Synth – routes the final output of Summit’s Part B synth signal chain
to the input of the Part B FX processor, in order that effects can be added to the synth
sound.


**External FX Level – Processor A**
Displayed as: `FxA Level`
Default value: 127
Range of adjustment: 0 to 127


This control determines the level of the external input signal to be mixed with the output of
the Part A FX processor. With the default setting of 127 (maximum), the input (or “dry”)
signal will be heard at full level. At a setting of zero, the input signal will not be present at
the output and only the processed (or “wet”) signal will be heard.


This setting may be relevant if you are using the FX section in a send-and-return loop from
an external mixer: in this situation it is normal to mix the processed return signal with the dry
input signal within the mixer.

---

## Page 44

**External FX Level – Processor B**
Displayed as: `FxB Level`
Default value: 127
Range of adjustment: 0 to 127


This control performs the same function as FxA Level above for the Part B FX processor.


**Backup Page:**


Novation recommends the use of Novation Components online Librarian to fully manage your
Patches – see page 45. However, you may also import and export Patch data via MIDI
SysEx messages, using applications such as SysEx Librarian (Mac) or MIDI-OX (Windows).


BACKUP      E/V
Select   AllH
Send To  USBport
H Go


**Select Patches**
Displayed as: `Select`
Default value: All
Range of adjustment: PCurrent, P bank A, P bank B, P bank C, P bank D, P
ABCD, Mcurrent, M bank A, M bank B, M bank C,
M bank D, M ABCD, Settings, All


`Select` lets you choose which Patches to back up as SysEx data. You can choose either
the currently active Patch (Current), or any or all of the four Banks in full (128 Patches per
Bank) of either Single Patches (prefix P) or Multi Patches (prefix M). The two options P
ABCD and M ABCD select all four Banks of Single or Multi Patches respectively.


You can also choose to back up all the current synth settings (choose Settings), or the
current synth settings plus every Single and Multi Patch (choose All).


**Dump Port Select**
Displayed as: `Send To`
Default value: USBport
Range of adjustment: USBport, MIDIout


You can choose to send the SysEx data via either the **MIDI OUT** socket or the USB port,
with the `SendTo` setting. When you are ready to do the data dump, select the lower lefthand screen button, `Go`, to perform the action.


**Keyboard Settings:**


KEYBOARD     F/V
VelCurve  NORMAL H


Displayed as: `VelCurve`
Default value: NORMAL
Range of adjustment: HIGH, NORMHI, NORMAL, NORMLO, LOW


The `VelCurve` parameter operates in conjunction with the Velocity parameter, which is
set on Page 1 of the **Env** menu.


The response to velocity information from the keyboard may be set using this function. A
setting of HIGH indicates smaller changes in velocity (a lighter playing style) will create
a large change in response to velocity, be it volume or any other modulation destination
velocity is routed to. A setting of LOW indicates larger changes of velocity - a much harder
playing style, will create larger changes in response to velocity. NORMAL is obviously a
compromise between these two, and NORMHI and NORMLO further intermediate values.


**44**



**Tuning Table pages**
Summit gives you the capability to alter the intervals between notes on your keyboard,
letting you create alternative keyboard scales to the standard twelve-tone “Western” tuning
we are all familiar with.


This is achieved by the use of Tuning Tables, which are effectively “lookup tables” for the
oscillators, which tell them what frequency to generate when any particular key is struck.
There are 17 Tuning Tables in all, and selection of the Table to be used is made on Page 1
of the Oscillator Menu.


By default, the oscillators use Tuning Table 0, which generates standard Equal
Temperament tuning. The remaining 16 tables have the same default data (thus selecting
them without any prior modification will also produce standard Equal Temperament tuning),
but they may be altered to create any keyboard scale or layout you wish to use. This allows
you to create new chords and harmonies not achievable with standard tuning.


Each of the 16 definable Tuning Tables has its own page: these are Pages G to V of the
**Settings** menu. The pages are identical: the default page for Tuning Table 1 is shown
below as an example.


Bear in mind you won’t hear the effect of changing any Tuning Table parameters unless the
Tuning Table being set up is selected in Page 1 of the Oscillator Menu.


TUNING TABLE 1  G/V
Kbd Note  C 3  H
Retune Note C 3
Retune Frac  0


**Keyboard Note**
Displayed as: `Kbd Note`
Default value: C 3
Range of adjustment: C -2 to G 8


This parameter sets the keyboard note whose pitch is to be redefined. `Kbd Note` will
follow the last key struck: if you hit middle C without any octave shift or other transposition
being applied by the keyboard itself, `Kbd Note` will assume the value C 3. If octave
shift or transposition is active on the keyboard, the MIDI data sent will be changed and the
parameter will accordingly display the shifted note value.


**Retuned Note**
Displayed as: `Retune Note`
Default value: C 3
Range of adjustment: C -2 to G 8


Once you define the keyboard note to be redefined with `Kbd Note`, you can set
`Retune Note` to any note, above or below `Kbd Note` . Then when you play the note
defined by `Kbd Note`, you will hear the note defined by `Retune Note` .


`Retune Note` will always display the note actually being generated, and will by default
be the same value as `Kbd Note` before any retuning is applied. Once a key has been
redefined, `Kbd Note` will confirm which key is being pressed, while `Retune Note`
will display the actual note being generated by that key.


**Micro Intervals**
Displayed as: `Retune Frac`
Default value: 0
Range of adjustment: 0 to 255, repeating


Using Tuning Tables does not restrict you only to standard note intervals. Summit supports
“microtuning”, whereby any key can be made to generate an “in-between” note, to a
resolution of 1/256th of a semitone (0.4 cents). With `Retune Frac` set to 0, the
note being defined ( `Kbd Note` ) will adopt the pitch value set by `Retune Note` . As
`Retune Frac` is increased, the note’s pitch sharpens by one micro interval at a time.
When `Retune Frac` reaches a value of 255, one further step will generate the next
standard note in the scale, and the value will reset to zero. By the same principle, the
parameter may also be decreased in micro intervals to flatten the note.

---

## Page 45

# **APPENDIX**

**System Updates using Novation Components**
Novation Components is an online Patch Librarian, which allows you to manage your Patch
library. You can also restore original factory Patches and download new ones as they
become available.


Novation Components will also advise you if your Summit’s Firmware is out of date and will
update it for you if necessary.


Full details are available at [novationmusic.com/register](http://www.novationmusic.com/register)


**Patch import via SysEx**
It is also possible to import Patch data into Summit via MIDI SysEx messages, using
applications such as SysEx Librarian (Mac) or MIDI-OX (Windows). It is important to note
Patch Banks retain a reference to their original memory location and will be loaded back
into that location on import. Thus any Patches already in those locations will be overwritten.


**Sync values tables**


**Arp/Clock Sync Rate**
This table lists the sync rate divisions available for the Arpeggiator clock SyncRate
parameter ( **Arp/Clock** menu, page 3).

|Display|Display<br>Meaning|Musical Description|MIDI<br>Ticks*|
|---|---|---|---|
|`8 beats`|8 beats|1 cycle per 2 bars|192|
|`6 beats`|6 beats|1 cycle per 6 beats (2 cycles per 3 bars)|144|
|`5 + 1/3`|5 + 1/3|3 cycles per 4 bars|128|
|`4 beats`|4 beats|1 cycle per 1 bar|96|
|`3 beats`|3 beats|1 cycle per 3 beats (4 cycles per 3 bars)|72|
|`2 + 2/3`|2 + 2/3|3 cycles per 2 bars|64|
|`2nd`|2nd|2 cycles per 1 bar|48|
|`4th D`|4th dotted|2 cycles per 3 beats (8 cycles per 3 bars)|36|
|`1 + 1/3`|1 + 1/3|3 cycles per 1 bar|32|
|`4th`|4th|4 cycles per 1 bar|24|
|`8th D`|8th dotted|4 cycles per 3 beats (16 cycles per 3 bars)|18|
|`4th T`|4th triplet|6 cycles per 1 bar|16|
|`8th`|8th|8 cycles per 1 bar|12|
|`16th D`|16th dotted|8 cycles per 3 beats (32 cycles per 3 bars)|9|
|`8th T`|8th triplet|12 cycles per 1 bar|8|
|`16th`|16th|16 cycles per 1 bar|6|
|`16th T`|16th triplet|24 cycles per 1 bar|4|
|`32nd`|32nd|32 cycles per 1 bar|3|
|`32nd T`|32nd triplet|48 cycles per 1 bar|2|



- Assuming a resolution of 24 PPQN


**Delay Sync Rate**
This table lists the sync rate divisions available for the `DelaySync` parameter ( **FX** Menu,
page 4).

|Display|Display<br>Meaning|Musical Description|MIDI<br>Ticks*|
|---|---|---|---|
|`4 beats`|4 beats|1 cycle per 1 bar|96|
|`3 beats`|3 beats|1 cycle per 3 beats (4 cycles per 3 bars)|72|
|`2 + 2/3`|2 + 2/3|3 cycles per 2 bars|64|
|`2nd`|2nd|2 cycles per 1 bar|48|
|`4th D`|4th dotted|2 cycles per 3 beats (8 cycles per 3 bars)|36|
|`1 + 1/3`|1 + 1/3|3 cycles per 1 bar|32|
|`4th`|4th|4 cycles per 1 bar|24|
|`8th D`|8th dotted|4 cycles per 3 beats (16 cycles per 3 bars)|18|
|`4th T`|4th triplet|6 cycles per 1 bar|16|
|`8th`|8th|8 cycles per 1 bar|12|
|`16th D`|16th dotted|8 cycles per 3 beats (32 cycles per 3 bars)|9|
|`8th T`|8th triplet|12 cycles per 1 bar|8|
|`16th`|16th|16 cycles per 1 bar|6|
|`16th T`|16th triplet|24 cycles per 1 bar|4|
|`32nd`|32nd|32 cycles per 1 bar|3|
|`32nd T`|32nd triplet|48 cycles per 1 bar|2|



- Assuming a resolution of 24 PPQN


**45**



**LFO Sync Rate**
This table lists the sync rate divisions available for the LFO Sync clock; these are displayed
when an LFO **Rate** control 27 is adjusted with **Range** 26 set to **Sync** .

|Display|Display<br>Meaning|Musical Description|MIDI<br>Ticks*|
|---|---|---|---|
|`64 beats`|64 beats|1 cycle per 16 bars|1536|
|`48 beats`|48 beats|1 cycle per 12 bars|1152|
|`42 beats`|42 beats|2 cycles per 21 bars|1008|
|`36 beats`|36 beats|1 cycle per 9 bars|864|
|`32 beats`|32 beats|1 cycle per 8 bars|768|
|`30 beats`|30 beats|2 cycles per 15 bars|720|
|`28 beats`|28 beats|1 cycle per 7 bars|672|
|`24 beats`|24 beats|1 cycle per 6 bars|576|
|`21 + 1/3`|21 + 1/3|3 cycles per 16 bars|512|
|`20 beats`|20 beats|1 cycle per 5 bars|480|
|`18 + 2/3`|18 + 2/3|3 cycles per 14 bars|448|
|`18 beats`|18 beats|1 cycle per 18 beats (2 cycles per 9 bars)|432|
|`16 beats`|16 beats|1 cycle per 4 bars|384|
|`13 + 1/3`|13 + 1/3|3 cycles per 4 bars|320|
|`12 beats`|12 beats|1 cycle per 12 beats (1 cycle per 3 bars)|288|
|`10 + 2/3`|10 + 2/3|3 cycles per 8 bars|256|
|`8 beats`|8 beats|1 cycle per 2 bars|192|
|`6 beats`|6 beats|1 cycle per 6 beats (2 cycles per 3 bars)|144|
|`5 + 1/3`|5 + 1/3|3 cycles per 4 bars|128|
|`4 beats`|4 beats|1 cycle per 1 bar|96|
|`3 beats`|3 beats|1 cycle per 3 beats (4 cycles per 3 bars)|72|
|`2 + 2/3`|2 + 2/3|3 cycles per 2 bars|64|
|`2nd`|2nd|2 cycles per 1 bar|48|
|`4th D`|4th dotted|2 cycles per 3 beats (8 cycles per 3 bars)|36|
|`1 + 1/3`|1 + 1/3|3 cycles per 1 bar|32|
|`4th`|4th|4 cycles per 1 bar|24|
|`8th D`|8th dotted|4 cycles per 3 beats (16 cycles per 3 bars)|18|
|`4th T`|4th triplet|6 cycles per 1 bar|16|
|`8th`|8th|8 cycles per 1 bar|12|
|`16th D`|16th dotted|8 cycles per 3 beats (32 cycles per 3 bars)|9|
|`8th T`|8th triplet|12 cycles per 1 bar|8|
|`16th`|16th|16 cycles per 1 bar|6|
|`16th T`|16th triplet|24 cycles per 1 bar|4|
|`32nd`|32nd|32 cycles per 1 bar|3|
|`32nd T`|32nd triplet|48 cycles per 1 bar|2|



- Assuming a resolution of 24 PPQN


**List of Wavetables**


|BS sine|String|Glassy|Spirals|
|---|---|---|---|
|Random|BassOrgn|Granular|Steel|
|Zing|Acid|Grime|Sunrise|
|Tubey|Buzzy|Drow|Swell|
|Octaves|Carousel|Heavy|Thicker|
|Wobbler|Choral|Hedge|Thinner|
|Chords|Climbing|Hungry|Tides|
|Didgery|CoinFlip|Ladders|Tokyo|
|Harsh|Deep|Lead|Tops|
|Organ|Dub|Modeling|V.Chord|
|E. Piano|Eee|Modem|Variance|
|VoxOooEe|Eris|Monster|Vocaloid|
|VoxYahEe|Flame|Screech|Vowelled|
|Winds|Further|SeaBase|WeirdVox|
|SoftClav|GlassSaw|Shmorgan|Yeah|
