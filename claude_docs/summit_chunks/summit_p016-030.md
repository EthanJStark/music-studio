# Focusrite Summit User Guide v1.1 (EN) (Pages 16-30)

> Chunked conversion from PDF for faster targeted reads.



---

## Page 16

16
SYNTHESIS TUTORIAL
This section covers the general principles of electronic sound generation and processing in
more detail, including references to Summit’s facilities where relevant. It is recommended
that this chapter is read carefully if analogue sound synthesis is an unfamiliar subject.
Users familiar with this subject can skip this section and move on to the next.
To gain an understanding of how a synthesiser generates sound it is helpful to have an
appreciation of the components that make up a sound, both musical and non-musical.
The only way a sound may be detected is by air vibrating the eardrum in a regular, periodic
manner. The brain interprets these vibrations (very accurately) into one of an infinite number
of different types of sound.
Remarkably, any sound may be described in terms of three properties, and all sounds
always have them. They are:
•	 Pitch
•	 Timbre
•	 Volume
What makes one sound different from another is the relative magnitudes of the three
properties as initially present in the sound, and how the properties change over the
duration of the sound.
With a musical synthesiser, we deliberately set out to have precise control over these
three properties and, in particular, how they can be changed during the “lifetime” of the
sound. The properties are often given different names, e.g., Volume may be referred to as
Amplitude, Loudness or Level, Pitch as Frequency and sometimes Timbre as Tone.
Pitch
As stated, sound is perceived by air vibrating the eardrum. The pitch of the sound is
determined by how fast the vibrations are. For an adult human, the slowest vibration
perceived as sound is about twenty times a second, which the brain interprets as a low
bass sound; the fastest is many thousands of times a second, which the brain interprets as
a high-pitched sound.
Time
Time
A
B
If the number of peaks in the two waveforms (vibrations) are counted, there are exactly
twice as many peaks in Wave B as in Wave A. (Wave B is actually an octave higher in pitch
than Wave A.) The number of vibrations in a given period determines the pitch of a sound.
This is the reason pitch is sometimes referred to as frequency. It is the number of waveform
peaks counted during a given period of time which defines the pitch, or frequency.
Timbre
Musical sounds consist of several different, related pitches occurring simultaneously.
The lowest is usually referred to as the ‘fundamental’ pitch and corresponds to the
perceived note of the sound. Other pitches making up the sound which are related to the
fundamental in simple mathematical ratios are called harmonics. The relative loudness
of each harmonic as compared to the loudness of the fundamental determines the
overall tone or ‘timbre’ of the sound.
Consider two instruments such as a harpsichord and a piano playing the same note
on the keyboard and at equal volume. Despite having the same volume and pitch, the
instruments still sound distinctly different. This is because the different note-making
mechanisms of the two instruments generate different sets of harmonics; the harmonics
present in a piano sound are different to those found in a harpsichord sound.
Volume
Volume, which is often referred to as the amplitude or loudness of the sound, is determined
by how large the vibrations are. Very simply, listening to a piano from a metre away would
sound louder than if it were fifty metres away.
Volume
A
B
Having shown just three elements may define any sound, these elements now have to
be realised in a musical synthesiser. It is logical that different sections of the synthesiser
‘synthesize’ (or create) each of these different elements.
One section of the synthesiser, the Oscillators, generate raw waveform signals which
define the pitch of the sound along with its raw harmonic content (tone). These signals
are then mixed together in a section called the Mixer, and the resulting mixture is then fed
into a section called the Filter. This makes further alterations to the tone of the sound, by
removing (filtering) or enhancing certain harmonics. Lastly, the filtered signal is fed into the
Amplifier, which determines the final volume of the sound.
Oscillators
Mixer
Filter
Amplifier
Additional synthesiser sections - LFOs and Envelopes - provide further ways of altering
the pitch, tone and volume of a sound by interacting with the Oscillators, Filter and
Amplifier, providing changes in the character of the sound which can evolve over
time. Because LFOs’ and Envelopes’ only purpose is to control (modulate) the other
synthesiser sections, they are commonly known as ‘modulators’.
These various synthesiser sections will now be covered in more detail.
The Oscillators and Mixer
The Oscillator section is  the heart of the synthesiser. It generates an electronic wave
(which creates the vibrations when eventually fed to a loudspeaker). This waveform is
produced at a controllable musical pitch, initially determined by the note played on the
keyboard or contained in a received MIDI note message. The distinctive tone or timbre of
the waveform is actually determined by the waveform’s shape.
Many years ago, pioneers of musical synthesis discovered just a few distinctive waveforms
contained many of the most useful harmonics for making musical sounds. The names
of these waves reflect their actual shape when viewed on an instrument called an
oscilloscope, and they are: Sine waves, Square waves, Sawtooth waves, Triangle waves
and Noise. Each of Summit’s Oscillator sections can generate all these waveforms,
and can generate non-traditional synth waveforms as well. (Note that Noise is actually
generated independently and mixed in with the other waveforms in the Mixer section.)
Each waveform (except Noise) has a specific set of musically-related harmonics which can
be manipulated by further sections of the synthesiser.
The diagrams below show how these waveforms look on an oscilloscope, and illustrate
the relative levels of their harmonics. Remember, it is the relative levels of the various
harmonics present in a waveform which determine the tonal character of the final sound.
Sine Waves
Volume
Harmonic
1
Sine Wave
These possess just one harmonic. A sine waveform produces the “purest” sound because
it only has this single pitch (frequency).
Triangle Waves
Volume
Harmonic
1
3
5
7
Triangle Wave
These contain only odd harmonics. The volume of each decreases as the square of its
position in the harmonic series. For example, the 5th harmonic has a volume 1/25th of the
volume of the fundamental.


---

## Page 17

17
Sawtooth Waves
Sawtooth Wave
Volume
Harmonic
1
2
3
4
5
Sawtooth waves are rich in harmonics, and contain both even and odd harmonics of the
fundamental frequency. The volume of each is inversely proportional to its position in the
harmonic series.
Square / Pulse Waves
Square Wave
Volume
Harmonic
1
2
3
4
5
Square/Pulse waves contain only odd harmonics, which are at the same volume as the odd
harmonics in a sawtooth wave.
The square waveform spends an equal amount of time in its ‘high’ state as in its ‘low’ state.
This ratio is known as the ‘duty cycle’. A square wave always has a duty cycle of 50% which
means it is ‘high’ for half the cycle and ‘low’ for the other half. Summit lets you adjust the
duty cycle of the basic square waveform (via the Shape controls) to produce a waveform
which is more ‘rectangular’ in shape. These are often known as Pulse waveforms. As the
waveform becomes more and more rectangular, more even harmonics are introduced and
the waveform changes its character, becoming more ‘nasal’ sounding.
The width of the pulse waveform (the ‘Pulse Width’) can be altered dynamically by a
modulator, which results in the harmonic content of the waveform constantly changing. This
can give the waveform a ‘fat’ quality when the pulse width is altered at a moderate rate.
A pulse waveform sounds the same whether the duty cycle is – for example - 40% or 60%,
since the waveform is just “inverted” and the harmonic content is exactly the same.
50%
40%
10%
60%
Noise
Noise is a random signal, and does not have a fundamental frequency (and therefore
has no pitch property). Noise contains all frequencies, and all are at the same volume.
Because it possesses no pitch, noise is often useful for creating sound effects and
percussion type sounds.
Volume
1
2
3
4
5
Ring Modulation
A Ring Modulator is a sound generator that takes signals from two oscillators and
effectively “multiplies” them together. Summit’s Ring Modulator uses Oscillator 1 and
Oscillator 2 as inputs. The resulting output depends on the various frequencies and
harmonic content present in each of the two oscillator signals, and will consist of a series
of sum and difference frequencies as well as the frequencies present in the original signals.
OSC 1
OSC 2
X
Frequency Modulation (FM)
Another method of combining the signals from two sources is Frequency Modulation,
or FM. In this technique, the frequency of one oscillator – sometimes referred to as
the “carrier” - is dynamically varied about its nominal “centre” value by an amount
corresponding to the instantaneous amplitude of the signal from the second oscillator.
Summit has a set of controls on the panel dedicated to adding FM effects.
The precise sonic result will depend on the wave shapes of each oscillator, their relative
pitch, and the maximum amplitude of the modulating signal: on Summit this latter parameter
may be controlled manually, and may be further varied by both LFO and Envelope.
The result of frequency modulation is the generation of a wide range of additional
harmonics (in fact, theoretically infinite), both above and below the pitch of the oscillator
being modulated. In FM language, these harmonics are often referred to as sidebands.
The number of “significant” sidebands is proportional to the amplitude of the modulating
signal and inversely proportional to the frequency difference between the carrier and the
modulator. If the modulator is already rich in harmonics, e.g., something other than a simple
sine wave, each harmonic creates its own set of sidebands, further enriching the spectral
content of the result.
FM
MODULATOR
OSC 1
OSC 2
FREQUENCY
MODULATED OUTPUT
OSC 1 PITCH
Harmonics


---

## Page 18

18
The Mixer
To extend the range of sounds you can produce, typical analogue synthesisers have more
than one Oscillator (Summit has three for Part A and three for Part B). By using multiple
Oscillators to create a sound, it is possible to achieve interesting harmonic mixes. It is also
possible to slightly detune individual Oscillators against each other, which creates a warm,
‘fat’ sound.
Summit’s Mixer allows you to create a sound consisting of the waveforms of Oscillators 1, 2
and 3, a Noise source and the Ring Modulator output, all mixed together as needed.
OSC 1
OSC 1 VOLUME
OSC 2 VOLUME
OSC 3 VOLUME
   COMPLEX
WAVEFORM
MIX OF
OSC1, 2, 3,
NOISE AND
RING
MODULATOR
MIXER
INPUT TO
  FILTER
OSC 2
OSC 3
NOISE
RING MOD
NOISE
RING MOD
The Filter
Summit is a subtractive synthesiser. Subtractive implies part of the sound is subtracted
somewhere in the synthesis process.
The Oscillators provide the raw waveforms with plenty of harmonic content and the Filter
section subtracts some of the harmonics in a controlled manner.
There are three basic filter types, all of which are available in Summit: low-pass, band-pass
and high-pass. The type of filter most commonly used on synthesisers is low-pass. In a
low-pass filter, a “cut-off frequency” is chosen and any frequencies below this are passed,
while frequencies above are filtered out, or removed.
The setting of the Filter Frequency parameter dictates the point above which frequencies
are removed. This process of removing harmonics from the waveforms has the effect of
changing the sound’s character or timbre. When the Frequency parameter is at maximum,
the filter is completely “open” and no frequencies are removed from the raw Oscillator
waveforms.
In practice, there is a gradual (rather than a sudden) reduction in the volume of the
harmonics above the cut-off point of a low-pass filter. How rapidly these harmonics reduce
in volume as frequency increases above the cut-off point is determined by the filter’s Slope
parameter. The slope is measured in ‘volume units per octave’. Since volume is measured in
decibels, this slope is usually quoted as so many decibels per octave (dB/oct). The higher
the number, the greater the rejection of harmonics above the cut-off point, and the more
pronounced the filtering effect. Each of Summit’s filter sections has a 12 dB/oct slope, but
two of the same type can be cascaded (placed in series) to produce a slope of 24 dB/oct.
Summit also allows two different types of filter to be cascaded, or even to be placed “in
parallel”, so the mixer output is treated by both.
A further important parameter of the filter is Resonance. Frequencies at the cut-off point
may be increased in volume by advancing the filter’s Resonance control. This is useful for
emphasising certain harmonics of the sound.
As Resonance is increased, a whistling-like quality will be introduced to the sound passing
through the filter. When set to very high levels, Resonance actually causes the filter to
self-oscillate whenever a signal is being passed through it. The resulting whistling tone
being produced is actually a pure sine wave, the pitch of which depends on the setting of
the Frequency control (the filter’s cut-off point). This resonance-produced sine wave can
actually be used for some sounds as an additional sound source if wished.
The diagram below shows the response of a typical low pass filter. Frequencies above the
cut-off point are reduced in volume.
Volume
Frequency
Cut-off
Frequency
When resonance is added, the frequencies around the cut off point are boosted in volume.
Volume
Frequency
Cut-off
Frequency
In addition to the traditional low-pass filter type, there are also high-pass and band-pass
types. On Summit, the filter type is selected with the Shape switch 58  .
A high-pass filter is similar to a low-pass filter, but works in the “opposite sense”, so
frequencies below the cut-off point which are removed. Frequencies above the cut-off
point are passed. When the Filter Frequency parameter is set to minimum, the filter is
completely open and no frequencies are removed from the raw Oscillator waveforms.
Volume
Frequency
Cut-off
Frequency
With a band-pass filter, just a narrow band of frequencies centred around the cut-off point
is passed. Frequencies above and below the band are removed. It is not possible to fully
open this type of filter and allow all frequencies to pass.
Volume
Frequency
Cut-off
Frequency


---

## Page 19

19
More complex relationships between volume and frequency can be obtained by using
simple filters of the types described above in combination. Summit allows you to “cascade”
two filters of different types, creating a “series” combination. Such a combination will
generally result in more frequencies being removed than with a single filter section, as both
filters are subtractive. However, interesting results can arise if the two filters have different
cut-off frequencies.
For example, if a low-pass filter is followed by a high-pass filter, the low-pass filter
will pass only very high frequencies to the high-pass filter, which will remove some of them,
leaving a narrow band of frequencies “between” the cut-off frequencies of both filters.
The width of this band depends on the difference between, or “separation of” the two
cut-off frequencies.
LPF
(f1)
HPF
(f2)
LP > HP
f1
Low pass filter
12 dB/oct
High pass filter
12 dB/oct
Combined
response when
Frequency
Low pass filter
12 dB/oct
High pass filter
12 dB/oct
f2
f1
f2
f1 < f2
Combined
response when
f1 > f2
Combining the same filters in parallel produces quite a different result, as the responses of
the two sections are effectively summed together. Low frequencies will be passed by the
low-pass filter and high frequencies by the high-pass filter, resulting in a dip or a hump in
the response in the area between the two cut-off frequencies.
LPF
(f1)
HPF
(f2)
+
f1
Low pass filter
12 dB/oct
High pass filter
12 dB/oct
f2
Combined
response when
f1 < f2
Frequency
Low pass filter
12 dB/oct
High pass filter
12 dB/oct
f1
f2
Combined
response when
f1 > f2
Envelopes And Amplifier
In earlier paragraphs, the synthesis of the pitch and the timbre of a sound was described.
The next part of the Synthesis Tutorial describes how the volume of the sound is controlled.
The volume of a note created by a musical instrument often varies greatly over the duration
of the note, according to the type of instrument.
For example, a note played on an organ quickly reaches full volume when a key is pressed.
It stays at full volume until the key is released, then the volume level falls instantly to zero.
TIME
KEY "ON"
KEY "OFF"
VOLUME
A piano note quickly attains full volume after a key is pressed, but gradually falls in volume
to zero after several seconds, even if the key is held.
TIME
KEY "ON"
KEY "OFF"
VOLUME
A string section emulation only attains full volume gradually when a key is pressed. It
remains at full volume while the key is held down, but once the key is released, the volume
falls to zero fairly slowly.
TIME
KEY "ON"
KEY "OFF"
VOLUME
In an analogue synthesiser, changes to a sound’s character which occur over the duration
of a note are controlled by sections called Envelope Generators. One of these (Amp Env)
is always related to the Amplifier, which controls the note’s amplitude – i.e., the volume
of the sound - when the note is played. In Summit, each envelope generator has five main
parameters, which determine the shape of the envelope; these are referred to as the
AHDSR parameters, or the envelope “phases”.
VOLUME
TIME
KEY “ON”
KEY “OFF”
SUSTAIN
ATTACK
HOLD
DECAY
RELEASE
DELAY
Attack Time
Adjusts the time it takes after a key is pressed for the volume to climb from zero to full
volume. It can be used to create a sound with a slow fade-in.
Hold Time
This parameter is not found on many synthesisers, but is available in Summit. It determines
for how long the note’s volume remains at its maximum level following the Attack Time,
before commencing the volume drop set by the Decay Time.


---

## Page 20

20
Decay Time
Adjusts the time it takes for the volume to fall from its initial full volume to the level set by the
Sustain control while a key is held down.
Sustain Level
This is unlike the other Envelope controls as it sets a level rather than a period of time.
It sets the volume level that the envelope remains at while the key is held down, after the
Decay Time has expired.
Release Time
Adjusts the time it takes for the volume to fall from the Sustain level to zero once the key is
released. It can be used to create sounds that have a “fade-out” quality.
Delay Time
You will notice the diagram also includes a further, initial phase, Delay. This is how long it
takes for the Attack Time – and hence the entire AHDSR sequence - to commence after
the key is struck. This is another envelope phase which is not generally found on other
synthesisers, but is available in Summit. The addition of a Delay Time leads us to rename
the envelope sequence DAHDSR for completeness (though many users will continue to
refer to it by the more traditional term ADSR).
Most modern synthesisers can generate multiple envelopes. Summit has three Envelope
Generators: Amp Env has a dedicated set of hardware ADSR slider controls (Delay and
Hold are controlled separately via the menu), and is always applied to the amplifier to
shape the volume of each note played, as detailed above. The two Modulation Envelopes
(Mod Env 1 and Mod Env 2) share an identical set of controls, with an assignment switch
selecting the envelope being controlled. Modulation envelopes can be used to dynamically
alter other sections of the synthesiser during the lifetime of each note. Summit’s Mod Env
Generators can be used to modify the filter cut-off frequency, or the pulse width of the
Oscillators’ Square Wave outputs, for example.
FILTER
CUT-OFF
FREQUENCY
TIME
KEY “ON”
KEY “OFF”
SUSTAIN
ATTACK
HOLD
DECAY
RELEASE
DELAY
LFOs
Like the Envelope Generators, the LFO (Low Frequency Oscillator) section of a synthesiser
is a Modulator. Instead of being a part of the sound synthesis itself, it is used to change (or
modulate) other sections of the synthesiser. In Summit, for example, the LFOs can be used
to alter Oscillator pitch, or Filter cutoff frequency, as well as many other parameters.
Most musical instruments produce sounds that vary over time both in volume and in pitch
and timbre. Sometimes these variations can be quite subtle, but still contribute greatly
towards characterising the final sound.
Whereas an Envelope is used to control a one-off modulation over the lifetime of a single
note, LFOs modulate by using a repeating cyclic waveform or pattern. As discussed
earlier, Oscillators produce a constant waveform, which can take the shape of a repeating
sine wave, triangle wave etc. LFOs produce waveforms in a similar way, but normally at
a frequency which is too low to produce a sound the human ear could perceive directly.
As with an Envelope, the waveforms generated by the LFOs may be fed to other parts of
the synthesiser to create the desired changes over time – or ‘movements’ - to the sound.
Summit has four LFOs, two of which are completely independent, with their own full set of
hardware controls. All the LFOs may be used to modulate different synthesiser sections
and can run at different speeds.
Imagine this low frequency wave being applied to an Oscillator’s pitch. The result is the
pitch of the Oscillator slowly rises and falls above and below its original pitch. This would
simulate, for example, a violinist moving a finger up and down the string of the instrument
whilst it is being bowed. This subtle up and down movement of pitch is referred to as the
‘Vibrato’ effect.
A waveshape often used for an LFO is a Triangle wave.
PITCH
PITCH WITHOUT
MODULATION
TIME
Alternatively, if the same LFO signal were to modulate the Filter cut-off frequency instead of
the Oscillator pitch, a familiar wobbling effect known as ‘wah-wah’ would be the result.
Summary
A synthesiser can be broken down into five main sound generating or sound modifying
(modulating) blocks:
1.	Oscillators that generate waveforms at a various pitches.
2.	A Mixer that mixes the outputs from the Oscillators together (and add Noise and
other signals).
3.	Filters that remove certain harmonics, changing the character or timbre of the sound.
4.	An Amplifier controlled by an Envelope generator, which alters the volume of a
sound over time when a note is played.
5.	LFOs and Envelopes that can be used to modulate any of the above.
Much of the enjoyment to be had with a synthesiser is with experimenting with the factory
preset sounds (Patches) and creating new ones. There is no substitute for ‘hands on‘
experience. Experiments with adjusting Summit’s various controls will eventually lead to a
fuller understanding of how the various synth sections alter and help shape new sounds.
Armed with the knowledge in this chapter, and an understanding of what is actually
happening in the synth when tweaks to the knobs and switches are made, the process of
creating new and exciting sounds will become easy. Have fun!


---

## Page 21

21
SUMMIT: SIMPLIFIED BLOCK DIAGRAM
FPGA
Voice 1
Osc 1
Osc 2
Osc 3
Voice 16
Osc 1
Osc 2
Osc 3
Analogue
Sum
Filter
12dB
Filter
12dB
Filter
Pre Filter
Overdrive
Pre VCA
Distortion
Left VCA
Right VCA
Analogue
Sum
Filter
12dB
Filter
12dB
Filter
Pre Filter
Overdrive
Pre VCA
Distortion
Left VCA
Right VCA
VCA
Sum 16
VCA
Sum 1
Overdrive
Left
(Analogue)
Overdrive
Right
(Analogue)
Sum
Audio Inputs
Summed to mono
FX Left
(FPGA)
FX Right
(FPGA)
Sum L
Sum R
Main or Aux Left
Main or Aux Right
Summit’s architecture essentially comprises two complete, identical, but entirely separate
synthesisers with a single set of controls. Depending on the type of Patch in use – Single
or Multi – the two synths either work in an identical manner, with each control affecting the
same parameter in both synths simultaneously (Single Patches), or they work differently, to
generate Parts A and B of a Multi Patch, with each control affecting its parameter in only
one of the two synths at a time.
Each of Summit’s two Parts uses eight separate voices, which are treated independently
throughout the remaining signal chain. The voices are synthesised digitally in a Field
Programmable Gate Array (FPGA) using Numerically Controlled Oscillators running at an
extremely high clock rate, resulting in waveforms which are indistinguishable from those
using traditional analogue synthesis.
Each voice is a mix of the outputs of the three oscillators; when you adjust one of the
oscillator level controls 38 , 39  or 40  you are effectively adjusting the level of eight voices
simultaneously. The subsequent elements in the signal processing chain are entirely in the
analogue domain. Note that distortion can be added in several places – before the filter
(Overdrive 62 ), after the filter (FltPostDrv in the Voice Menu) and after final voice
summation (Distortion Level 68 ). The sonic effect can be quite different in each case.
Note that the time-domain effects (FX) – chorus, delay and reverb – are digitally generated
within the FPGA as well. The stereo effects send into the FX processing section is taken
from post the main VCA, so all distortions added to the signals are processed by the FX.
The FX return signal is added back to the same point in the signal path.
External inputs
Summit also has a pair of audio inputs (see  10  at page 9): these allow you to connect
external audio sources – e.g., from other synth modules - and then use Summit’s extensive
processing capabilities to treat their sounds. The two ¼” jack sockets are intended for the
left and right signals of a stereo pair, but you can connect a mono source to the LEFT input
only if you wish.
Page 3 of the Voice menu enables these inputs and lets you choose whether the external
signals connected are to be mixed with each of the 16 voices at the input of the analogue
filter section, or to be added to the synth sound “post-VCA” at the output of the filter
section. The first option – PreFilt in the menu – effectively adds the external signals
to Summit’s own internally generated sounds, and they will therefore undergo the same
signal processing as the native synth sounds, including analogue Pre Filter Overdrive and
Pre-VCA Distortion.
The second option – PostFilt in the menu – lets you route the external signals directly
to Summit’s FX section, where they can either be added to the native synth sounds,
or have one of the FX sections allocated to them exclusively: this selection is made on
Page C of the Settings menu. Because the outputs of the FX sections may be routed to
either the main or auxiliary outputs, this allows you to add FX to external signals entirely
independently of any synthesiser functions.


---

## Page 22

22
SUMMIT IN DETAIL
In this section of the manual, each section of the synthesiser is discussed in greater detail.
The sections are arranged in order of “signal flow” – see the Block Diagram above. Within
each section, the surface physical controls are described first, followed by a reference
guide to the display menu relating to the section. In general, the menus offer “fine control”
parameters to which access is less readily needed. The “initial value” given for each
parameter is that for the factory Init Patch: these will differ when another Patch is loaded.
NOTE:
Because of Summit’s bi-timbral architecture, the description of each section’s controls
and menu applies equally to both Parts of a Multi Patch. The descriptions can be taken
as equally applicable to either Part A or Part B, though the adjustments will be made
to only one Part at a time, unless MULTIPART CONTROL is set to Both.
We must emphasise that there is no substitute for experimentation. Adjusting controls
and tweaking individual parameters while listening to different patches will tell you more
about what each parameter does than this User Guide ever could. In particular, we would
encourage you to experiment with the effect that varying a parameter has on different
Patches – you will find there can be considerable differences between Patches, depending
on how the sound is being generated.
Voices
Summit is a bi-timbral, 16-voice, polyphonic instrument. “Polyphonic” basically means
you can play multiple notes on the keyboard, and every note you hold down will sound.
“Bi-timbral” means Summit’s Patches have two separate Parts, which may be adjusted as
if they were one, or completely independently. When you select a Single Patch, Summit
becomes a single synth with sixteen voices. With Multi Patches, you still have sixteen
voices, but now eight are allocated to generating Part A and eight to Part B.
As you play, each note is assigned one or more ‘voices’, and as Summit supports eight
voices per Part, you will often run out of fingers before you run out of voices! But this does
depend on how many voices are assigned to each note – see the Unison parameter in the
Voice Menu page 23). However, if you are controlling Summit from a MIDI sequencer
or DAW, it is possible to run out: sequencers don’t have the human constraint of a finite
number of fingers. Although this is likely to happen infrequently, users may occasionally
observe this phenomenon, which is termed ‘voice stealing’.
The alternative to polyphonic voicing is mono. With mono voicing, only one note sounds
at a time; pressing a second key while holding the first down will cancel the first and play
the second – and so on. The last note played is always the only one you hear. All the early
synths were mono, and if you are trying to emulate a 1970s analogue synth, you may wish
to set the voicing to mono as the mode imposes a certain restriction on playing style that
will add to authenticity.
Each of Summit’s two synths may have its own polyphony mode: as you select different
factory Multi Patches, you will find some create Part A using one mode and Part B using
another. Other Patches use the same mode for both Parts.
Per-Part Selection of Summit’s polyphony mode is made with the Voice Mode button
48 . Further voicing and Glide parameters are available for adjustment in the Voice menu
(see opposite), which also includes settings related to some other synth functions.
49
50
48
As the names imply, three of the possible modes are mono and two are polyphonic.
1. 	Mono – this is standard monophonic mode; only one note sounds at a time, and
the “last played” rule applies -  if you play more than one key, only the last pressed
will be heard. The same voice or voices are used for every note: this means each
note played will re-trigger the voices even if the previous note is still sounding.
When Glide is turned On, a portamento glide with always occur between
successive notes.
2. 	Mono 2 – this mode operates in the same way as Mono, except voices are
assigned “in rotation” as each note is played. Unlike Mono or MonoLG, this has
the effect (depending on playing speed) of allowing each note to complete its
individual envelope. The main advantage of the Mono 2 voice mode is when using
envelopes with an appreciable attack phase length: the envelope is always reset
when a new key is pressed. This is not how analogue envelope generators work,
but many digital envelope generators work on this principle.
3. 	MonoLG – LG stands for Legato Glide. This is an alternative mono mode, which
differs from Mono in the way Glide and Pre-Glide work. In MonoLG mode, Glide
and Pre-Glide only work if the keys are played in a legato style, i.e., with note
overlap; playing notes separately produces no glide effect. As with Mono, the same
voices are re-used for every note.
4. 	Poly – in polyphonic mode, up to 16 voices of a Single Patch can sound
simultaneously: depending on how many voices are assigned in the Patch, this
means you can play up to 16 notes simultaneously (you may not have enough
fingers for this, but an external MIDI sequencer probably has!). If you play the same
note repeatedly, each note will be assigned a different voice, and you will hear the
individual envelopes of every note.
5. 	Poly2 – in this alternative polyphonic mode, successively playing the same note(s)
uses the same voices, the voices being re-triggered by new notes. This can change
the behaviour of voice stealing. For example, in Poly mode, when playing chord
shapes with similar notes (e.g., Amin7 to Cmaj) the notes C, E and G will be played
twice as well as the A and the B, i.e., a total of eight voices. If playing a melody
in the other hand, one voice from the first chord will be stolen, which may be the
lowest A. In Poly 2 mode, the C, E and G will only be played once, which will leave
three voices free for playing a melody.
The effect of the different polyphony modes can be quite subtle, depending on the Patch in
use and playing style, and we recommend you experiment!
Glide
Summit’s Glide function makes notes played sequentially glide from one to the next,
rather than immediately jumping from one pitch to another. It is enabled with the Glide
On button  49 . The synth remembers the last note played per Voice and the glide – up or
down - will start from that Voice’s last triggered pitch even after the key has been released.
The duration of the glide is set by the Glide Time control  50 : the maximum glide time
available is approximately 5 seconds.
Glide is primarily intended for use in a mono Mode, where it is particularly effective. It
can also be used in Poly modes, but its operation can be slightly unpredictable, because
the glide will be from the previous note used by the voice now assigned to the note being
played. This may be particularly evident with chords. Note the PreGlide parameter (on
Page 2 of the Voice Menu) must be set to zero in order for Glide to be operative.


---

## Page 23

23
The Voice Menu
Press Voice 9  to open the Voice menu. This has four pages: Pages 1 and 2 contain
voicing parameters, while Pages 3 and 4 contain various other synth parameters (these are
described here for logical consistency).
Voice Menu Page 1:
VOICE            1/4
Unison       1     H
UniDeTune   25
UniSpread    0
Unison

Displayed as:

Unison

Initial value:

1

Range of adjustment:
1, 2, 3, 4, 8
Unison can be used to “thicken” the sound by assigning additional voices (up to eight
in total) for each note. Be aware the number of voices is finite and with multiple voices
assigned, the polyphonic capability of the active Part may be reduced. With four voices per
note, only two notes may be played together fully polyphonically, if further notes are played,
“voice stealing” is implemented and the first note played will be cancelled. With Unison set
to 8, Summit’s currently selected Part becomes a multi-voice monophonic synth.
If the limitation on polyphony imposed by Unison Voices is restrictive and
the oscillators are set to Sawtooth, a similar effect can be obtained by
using the SawDense and DenseDet parameters in the Oscillator
Menu. (In fact, some of the factory patches use this technique.)
SawDense and DenseDet have no impact on the polyphony.
Voice DeTune

Displayed as:

UniDeTune

Initial value:

25

Range of adjustment:
0 to 127
Unison Detune is only effective when Unison is set to something other than 1. The
parameter determines how much each voice is detuned relative to the others; detuning is
generally desirable as adding additional “identical” voices has much less effect.
Voice panning

Displayed as:

UniSpread

Initial value:

0

Range of adjustment:
0 to 127
UniSpread gives you a method of controlling how the separate voices are positioned
in the stereo image. With UniSpread set to zero, all voices are centrally panned,
effectively providing a mono image. As the value of UniSpread is increased, multiple
voices are panned increasingly left and right – odd-numbered voices to the left and even
to the right.
Fully Left
Fully Right
centre
unison voice 4
unison voice 3
unison voice 2
unison voice 1
Stereo image placement diagram for 4 voice unison with UniSpread set mid way
Stereo image placement diagram for 4 voice unison with UniSpread increased
Fully Left
Fully Right
centre
unison voice 4
unison voice 3
unison voice 2
unison voice 1
Note UniSpread is still effective even with unison voices set to 1: in this case, a single
note played is positioned centrally in the stereo image, while playing multiple notes results
in left or right panning, depending whether the voice in use is odd- or even-numbered.
When used like this, best results are obtained with moderate amounts of UniSpread.
Voice Menu Page 2:
VOICE            2/4
PreGlide    +0     H
PatchLevel  64
Pre-Glide

Displayed as:

PreGlide

Initial value:

0

Range of adjustment:
-12 to +12
If set to a value other than zero, Pre-Glide takes priority over Glide, though it does use
the setting of the Glide Time control 50  to determine its duration. Note that Glide On
49  must be selected for Pre-Glide to work. PreGlide is calibrated in semitones, and
each note played will actually begin on a chromatically-related note up to an octave above
(value = +12) or below (value = -12) the note corresponding to the key pressed, and glide
towards the ‘target’ note, over a time set by the Glide Time control. This differs from Glide
in that, e.g., two notes played in sequence will each have their own Pre-Glide, related to the
notes played, and there will be no glide ‘between’ the notes.
Although the use of Glide is not recommended in Poly modes when
playing more than one note at a time, this restriction does not apply to
Pre-Glide, which can be very effective with full chords.
Patch Level

Displayed as:

Patch Level

Initial value:

64

Range of adjustment:
0 to 127
This is an additional level trim control, whose setting is saved with the Patch. This allows
you to set the overall volume of each Patch, so all the Patches in use are at the levels you
want. With a value of 0, the Patch volume is halved; with a value of 127, it is doubled.
Voice Menu Page 3:
VOICE            3/4
FltPostDrv   0     H
FltDiverge   0
AudioInput Off
Post Filter Distortion

Displayed as:

FltPostDrv

Initial value:

0

Range of adjustment:
0 to 127
This parameter controls how much pre-envelope distortion is added to the sound after the
filter, but (crucially) before the amplifier. This distortion will thus remain constant when
the amplifier is gradually opened and closed by the amplitude envelope, unlike that added
by the Effects section DISTORTION Level control [68], which follows the amplifier
in the signal chain. Note also this distortion is distinct from the distortion which results
from adjusting the Overdrive control [62] in the filter section: it is applied only to the
frequencies passed by the filters, whereas Filter Overdrive applies distortion to the sound’s
full frequency spectrum before the filter.
Filter Divergence

Displayed as:

FltDiverge

Initial value:

0

Range of adjustment:
0 to 127
This parameter re-creates the subtle effect of poor filter calibration found on early analogue
synths. The filter for each voice is deliberately detuned by a different, fixed amount. The
effect will be more apparent when the filter is close to resonance.


---

## Page 24

24
External Audio Input Routing

Displayed as:

AudioInput

Initial value:

Off

Range of adjustment:
Off, PreFilt, PostFilt
Stereo audio from external equipment connected to Summit’s external inputs  10  can
be inserted into the signal processing paths of each synth either before (PreFilt) or after
(PostFilt) the filter section. Stereo audio sent through the filter will be summed to mono.
Audio sent directly to the FXs (in the Global Settings menu) will not be summed and heard
in full stereo.

When a Multi Patch is selected, you can independently select how the external signal is
routed to either Part A or Part B, or both. Note that an external audio signal will not be
heard if the VCA is not being triggered. If no notes are being played, the VCA is not being
opened by the keyboard and no audio can pass through.
When using Summit to process external audio in the same way as you
would use an FX processor, you can turn down the mixer inputs
(Oscillators, Noise and Ring Mod) so their sounds is not combined with
the external signal. If you then hold a note on and press Key Latch, the
VCA will remain open at all times, allowing the external signal to be constantly processed.
When using Summit to process external audio, it is important to remember
that the number of voices held open can affect the external audio’s input
level. The more voices held open, the more “instances” there are of the
external signal being passed through the synth’s processing.
However, if too many voices are used it can cause unwanted level clipping. You should
experiment, but for the best results, one or two notes will often provide enough of a
desired signal for processing.
Note that the external audio inputs may also be routed to the FX section. This routing is
completely independent of the that enabled by AudioInput, and is enabled in the
Settings menu. See page 42.
Voice Menu Page 4:
VOICE            4/4
FltShpMore LP > HP H
FltFreqSep  +0
Dual Filter Options

Displayed as:

FltShpMore

Initial value:

LP > HP

Range of adjustment:
LP > HP, LP > BP, HP > BP, LP + HP, LP + BP,
HP + BP, LP + LP, BP + BP, HP + HP
As explained in the Filter Section description (see page 27), Summit offers two separate
filters, each of which may be configured as low-pass, band-pass or high-pass by the Filter
section’s Shape control 58 . For the three settings LP, BP and HP, the Slope control
59  inserts either a single filter (12dB) or two identical filters in series (24dB) into the
signal path. When Slope is set to Dual, the Voice menu page above is displayed and
Slope is fixed at 12dB.
The FltShpMore parameter offers nine further combinations of the two filters. The first
three, those including a ‘>’ symbol, place two different filters in series, while the other six,
those including a ‘+’ symbol, place two filters in parallel. Note that in the case of parallel
configurations, the two filters may be of the same type.
These dual filter options give the filter sections greatly increased flexibility over
conventional designs employing a single, configurable filter. While the main Frequency
control 60  continues to adjust the cut-off (or centre) frequency of both filters, the second
parameter on this page, FltFreqSep, allows the two cut-off (or centre) frequencies to
be different, or “separated”.
Series and parallel combinations of two filters result in radically different overall frequency
responses. With filters in series, the combined effect is subtractive: the harmonic content
of the signal after the first filter will already have been reduced by its action, and will then
be further reduced by the second. Therefore frequencies will be removed by both filters.
Conversely, the combined effect of parallel filters may be considered as additive, because
the same signal is applied to both filters, so frequencies removed by one filter may be
passed by the other, depending on their relative type and cut-off (or centre) frequencies.
In general, combining filters in parallel is likely to produce a response shape with a peak or
dip between the frequencies of the two filters, but a wide range of shapes can be created
by combining two filters of different types. The value of  the “separation” parameter,
FltFreqSep (see below), also has a major effect on the resulting frequency response.
(a) LP > HP
(b) LP > BP
(c) HP > BP
(d) LP + HP
(e) LP + BP
(f) HP + BP
(g) LP + LP
(h) BP + BP
(i) HP + HP
FILTERS IN SERIES
FILTERS IN PARALLEL
Filter frequency separation

Displayed as:

FltFreqSep

Initial value:

0

Range of adjustment:
-64 to +63
Two filters configured in either series or parallel by selecting one of the dual filter
options may have different frequencies. The difference – or separation – of the two filter
frequencies is set by the FltFreqSep parameter. When separation is zero, the two
filters have the same frequency.
Positive values of FltFreqSep will lower the frequency of the first filter while increasing
that of the second, thus “separating” the response curves of the two filter sections. The
converse applies with negative values: the frequency of the first filter increase while that of
the second decreases, so the frequencies effectively “cross over”.
The audible effect of these options will largely depend on the two filter types selected by
FltShpMore. The “first” and “second” filters referred to in the previous paragraph are
the two listed in the FltShpMore setting, e.g., with FltShpMore set to HP + BP, the
“first” filter will be a high-pass type and the second a band-pass type.
In all dual filter options, the resultant frequency response from the combination will have
two turning points if FltFreqSep is set to something other zero, thereby giving the
two filters different frequencies. Frequency always adjusts the overall filter combination
regardless of the separation, but will maintain the “offset” between the two cut-off (or
centre) frequencies – as a constant octave value - as it is varied.


---

## Page 25

25
The Oscillator Section
16
19
23
17
18
20
21
22
The Oscillator section for each of Summit’s two synths consists of three identical
oscillators, each with its own set of controls. Therefore, the following descriptions apply
equally to any of the oscillators.
Oscillator Waveform
The Wave button 19  selects one of five wave shape options: four are the common
fundamental waves,
 Sine,
 Triangle,
 (rising) Sawtooth and
 Square/Pulse.
The fifth option, more, allows selection from a range of 60 further wavetables, accessed
by the WaveMore parameter in the Osc menu. The LEDs confirm the waveform option
currently selected. Note that the display immediately changes to the Osc menu, showing
the WaveMore parameter for the oscillator being adjusted, as soon as more is selected.
The last 10 slots in the WaveMore section are user configurable and can be loaded from
the Novation Components software.
Oscillator Pitch
The three controls Range 16 , Coarse 17  and Fine 18  set the Oscillator’s fundamental
frequency (or Pitch). The Range button selects using traditional “organ-stop” units, where
16’ gives the lowest frequency and 2’ the highest. Each doubling of stop length halves
the frequency and thus transposes the pitch of a note played at the same position on a
keyboard down one octave. When Range is set to 8’, the keyboard will be at concert pitch
with Middle C in the centre. The LEDs confirm the stop length currently selected.
The Coarse and Fine rotary controls adjust the pitch over a range of 1 octave and 1
semitone respectively. The OLED display shows the parameter value for Coarse in
semitones (12 semitones = 1 octave) and Fine in cents (100 cents = 1 semitone).
Summit is not limited to traditional “Western” note intervals, nor to the standard equaltempered scale. You can reprogram the keyboard in almost any way by using Tuning
Tables; these are described in detail at page 26.
Pitch Modulation
The frequency of each Oscillator can vary by modulating it with either (or both) LFO 2
or the Mod Env 2 envelope. The two Pitch controls, Mod Env 2 Depth  20  and LFO 2
Depth  21  control the depth – or intensity – of the modulation sources. (Many other pitch
modulation possibilities are available by using the Modulation Matrix – see page 38.)
Each Oscillator has a Depth control for modulation by Modulation Envelope 2. Adding
envelope modulation can give some interesting effects, with the oscillator pitch altering
over the duration of the note as it is played. A Mod Env 2 parameter value of 30 shifts the
pitch of one octave for the maximum level of the modulation envelope (e.g., if sustain is
at maximum). Negative values invert the sense of the pitch variation; i.e., the pitch will fall
during the attack phase of the envelope if Mod Env 2 has a negative value.
Each Oscillator also has a Depth control for modulation by LFO 2. Adding LFO Modulation
can add a pleasing vibrato when a triangle LFO waveform is used, and the LFO speed is
set neither too high nor too low. A sawtooth or square LFO waveform will produce rather
more dramatic and unusual effects. Oscillator pitch can be varied by up to five octaves,
but the LFO 2 depth control is calibrated to give finer resolution at lower parameter values
(less than ±12), as these are generally more useful for musical purposes.
Negative values of LFO 2 Depth “invert” the modulating LFO waveform; the effect will be
more obvious with non-sinusoidal LFO waveforms, e.g., with positive Depth values a falling
sawtooth LFO waveform will cause the oscillator pitch to lower and then rise sharply before
lowering again, but if Depth has a negative value, the pitch variation will be the opposite.
Waveform Shape
Summit lets you modify the shape of the selected waveform; this will alter the harmonic
content and thus the timbre of generated sound. The degree of modification – or deviation
from the original waveform shape – can be varied both manually and as a modulation. The
modulation sources available using the panel controls are Mod Env 1 and LFO 1; any other
mod source may be selected using the Modulation Matrix – see page 38
The Source button 23  assigns the Shape Amount control 22  to adjust the amount of
waveform alteration by one of the three sources. Note that all three possible sources –
Manual, Mod Env 1 and LFO 1 may be used in any combination, each with a different
value of Shape: their effect is additive.
When set to Manual, Shape lets you alter the waveform shape directly; the parameter
range is -63 to +63, where 0 results in an unmodified waveform. The sonic effect of Shape
will depend on the waveform in use.
When the Sine waveform is selected, a non-zero Shape parameter causes the sine wave
to become asymmetric, resulting in the addition of upper harmonics. Varying Shape with
Triangle or Sawtooth waveforms also modifies the wave shape and the harmonic content.
When Square/Pulse is selected as the waveform, Shape will vary the pulse width: a value
of 0 produces a 1:1 square wave. The timbre of the “edgy” square wave sound can be
modified by varying the pulse width, or duty cycle, of the waveform. Extreme clockwise
and anticlockwise settings of Shape produce very narrow positive or negative pulses,
with the sound becoming thinner and more “reedy” as the control is advanced. When
fully anticlockwise (parameter value -64), the square wave assumes a duty cycle of 0%
and is thus “off”. When varied to this degree by, e.g., adding LFO modulation, a rhythmic
character can be added to the oscillator waveform.
When Wave  19  is set to more, Shape sweeps through the wavetable’s waveform
(selected by the WaveMore parameter in the Osc Menu) by interpolating across the five
indexes of the selected wavetable to produce a “morphing” of two adjacent indexes: the
sonic effect of this will vary greatly depending on the active patch and the wavetable in use.
Each wavetable is actually a bank of five waveforms, between which you can interpolate
with the Shape control. We recommend you experiment altering Shape with different
waveforms to hear the effect. See also the WaveMore menu option described below.
Waveform shape may be modulated further by either (or both) Mod Env 1 or LFO 1, with
the amount of waveform modification due to each individually adjustable by Shape,
according to the setting of Source. With pulse waveforms, the sonic effect of LFO
modulation is dependent on the LFO waveform and speed used, while using envelope
modulation can produce some good tonal effects, with the harmonic content of the note
changing over its duration.
The Oscillator Menu
The following additional Oscillator parameters are available in the Osc menu. Each of
the three oscillators has two menu pages; the parameters available for each oscillator
are identical. There are also two further pages (OSC COMN pages, 1/8 and 2/8), with
parameter controls common to all three oscillators.
Common Oscillator pages:
The parameters available on the Common menu pages affect all three oscillators.
The default menu display is shown below:
OSC COMN 1       1/8
Diverge      0     H
Drift        0
TuningTable  0
OSC COMN 2       2/8
KeySync    Off     H
Noise LPF  127
Noise LPF    0
Diverge

Displayed as:

Diverge

Initial value:

0

Range of adjustment:
0 to 127
Each Voice is generated by three oscillators within the FPGA, giving a Summit a total
of 48 oscillators. Diverge applies small pitch variations independently to each of these
48 oscillators. The effect of applying this is that each voice will have its own tuning
characteristic. This adds a further interesting colouration to the sound quality and can be
used to bring the synth alive. The parameter sets the degree of variation.
Try setting BendRange to different values for each of the three oscillators.
This can produce some interesting triad chords when the pitch wheel is
moved.


---

## Page 26

26
Oscillator Drift

Displayed as:

Drift

Initial value:

0

Range of adjustment:
0 to 127
Summit has a dedicated low frequency oscillator which can be used to apply a slight
meandering detune to the three Oscillators. This is to emulate the oscillator drift of
traditional voltage controlled analogue synths: by applying a controlled amount of detuning,
the oscillators become slightly out of tune with each other, adding a “fuller” character to the
sound. Unlike Diverge, the drift effect changes over time.
Tuning Table

Displayed as:

TuningTable

Initial value:

0

Range of adjustment:
0 to 16
Summit normally operates with the tuning of a standard piano keyboard. The data which
relates the notes of the keyboard (or other MIDI transmitting device connected to Summit)
to the oscillator pitch intervals is called a Tuning Table: the default is Table 0, which cannot
be edited. The TuningTable parameter lets you select one of 16 alternative tuning
tables, which you can send to Summit via Novation Components, or create yourself. See
page 26 for details of how to create a Tuning Table. Note that all 16 Tuning Tables are
initially copies of Tuning Table 0, so their effect will not be apparent until a different table
has been created.
Key Sync

Displayed as:

KeySync

Initial value:

Off

Range of adjustment:
Off or On
With KeySync set Off, Summit’s three oscillators are free-running and even when set
accurately to the same pitch, may not be in phase with each other. This often does not
matter, but if the Ring Modulator or FM effects are in use, the out-of-phase effect may not
produce the result needed. To overcome this, KeySync may be selected to On, which
ensures the oscillators always start generating their waveforms at the start of a cycle when
a key is pressed.
Low-pass noise filter

Displayed as:

NoiseLPF

Initial value:

127

Range of adjustment:
0 to 127
In addition to the three Oscillators, Summit also has a noise generator. Noise is a signal
comprising a wide range of frequencies, and is a familiar “hissing” sound. This Noise filter
is a low-pass type: restricting the bandwidth of the noise alters the characteristic of the
“hiss”, and you can adjust the filter cut-off frequency to do this. The parameter’s default
value of 127 sets the filter “fully open”. Note that the noise generator has its own input
to the mixer, and in order to hear it in isolation, its input will need to be turned up and the
oscillator inputs turned down. (See “The Mixer Section” on page 27)
High-pass noise filter

Displayed as:

NoiseHPF

Initial value:

0

Range of adjustment:
0 to 127
This filter performs the same function as NoiseLPF, except it is a high-pass filter, and
therefore as the parameter value is increased, the filter’s higher frequencies are passed
and more low-frequency content of the noise signal is rejected. The parameter’s default
value of zero sets the filter “fully open”. The effect of applying this is that each voice will
have its own tuning characteristic.
Per-Oscillator pages:
The default menu displays for Oscillator 1 are shown below:
OSCILLATOR 1     3/8
WaveMore   BS sine H
FixedNote  Off
BendRange  +12
OSCILLATOR 1     4/8
Vsync        0     H
SawDense     0
DenseDet    64
More Waveforms

Displayed as:

WaveMore

Initial value:

BS sine

Range of adjustment:
See list on page 45 for a list of wavetables
Summit includes a set of wavetables, so you can generate a broader palette of sounds than
the simple sine, triangle, sawtooth and pulse waveforms can provide. Each wavetable is a
bank of five custom waveforms, you can interpolate with the Shape control 22 .
The WaveMore parameter selects the oscillator wavetable when Wave 19  is set to
more. The name of the wavetable appears on Row 2 of the display and gives a clue to the
nature of the sound. As with many other aspects of Summit, you will gain an understanding
of wavetables by experimenting, and by adjusting the Shape control. In many cases, this
will alter the sonic nature of the selected waveform quite dramatically.
The last 10 slots in the more waveforms menu contain user waveforms you can generate in
the Components software. Here you can design store and manage waveforms you create.
Single Fixed Note

Displayed as:

FixedNote

Initial value:

Off

Range of adjustment:
Off, C -2 to D# 5
Some sounds need not be chromatic pitch-dependent. Examples would be certain
percussion sounds (e.g., bass drums), and sound effects, such as a laser gun. It is possible
to assign a fixed note to a patch, such that playing any key on the keyboard generates the
same sound. The pitch on which the sound is based may be any semitone note in a range
of over eight octaves. With the parameter set Off, the keyboard behaves as normal. With it
set to any other value, every key plays the sound at the pitch corresponding to the value.
Pitch Wheel Range

Displayed as:

BendRange

Initial value:

+12

Range of adjustment:
-24 to +24
The keyboard pitch wheel can vary the pitch of each of the oscillators by up to two octaves,
up or down: BendRange may have a different value for each oscillator. The units are
semitones, with a default value of +12, moving the pitch wheel up will increase the pitch
of the notes by one octave, and moving it down takes them down an octave. Setting the
parameter to a negative value reverses the operation of the pitch wheel. Many of the factory
patches either have this parameter set to +12, giving a pitch wheel range of ±1 octave, or
to +2 for a range of 1 tone.
Try setting BendRange to different values for each of the three oscillators.
This can produce some interesting triad chords when the pitch wheel is
moved.
Oscillator Sync

Displayed as:

VSync

Initial value:

0

Range of adjustment:
0 to 127
Oscillator Sync is a technique of using one oscillator (the master) to add harmonics to
another (the slave). Summit provides Oscillator Sync by using a virtual oscillator for each of
the three main oscillators. The virtual oscillators are not heard, but the frequency of each is
used to re-trigger that of the main oscillator.
The Vsync parameter controls the frequency offset of the virtual oscillator relative to the
(audible) main oscillator. The nature of the resulting sound varies as the parameter value
is altered because the virtual oscillator frequency increases in proportion to the main
oscillator frequency as the parameter value increases.
When the Vsync value is a multiple of 16, the virtual oscillator frequency is a musical
harmonic of the main oscillator frequency. The effect is a transposition of the oscillator
that moves up the harmonic series, with values between multiples of 16 producing more
discordant effects.
OSC 2
OSC 1 (MASTER)
OSC 2 (SLAVE)


---

## Page 27

27
Vsync may be controlled for any or all oscillators using the Modulation
Matrix. See page 38 for details of how to use the Matrix.
To get the best out of Vsync, try modulating it using the LFO. Try assigning
it to the MOD wheel for real-time control.
Sawtooth Density

Displayed as:

SawDense

Initial value:

0

Range of adjustment:
0 to 127
Sawtooth Density only affects sawtooth waveforms. It adds copies of the oscillator
waveform to itself. Two additional virtual oscillators are used for this, producing a “thicker”
sound at low to medium values, but if the virtual oscillators are detuned slightly (see
Density Detuning below), a more interesting effect can be obtained.
Density Detuning

Displayed as:

DenseDet

Initial value:

64

Range of adjustment:
0 to 127
Density Detuning should be used in conjunction with Sawtooth Density. It detunes the
virtual density oscillators, and you will notice not only a thicker sound, but a beating as well.
You can use the Sawtooth Density and Density Detuning parameters to
“thicken” the sound, and simulate the effect of additional Voices. You can
use the Unison and Unison Detune parameters in the Voice Menu to
create a similar effect, but using Density and Density Detune have the
advantage of not needing to use additional Voices.
The Mixer Section
38
43
41
42
39
40
MIXER
OSC 1
TO ENVELOPES
SECTION
RING MOD
OSC 2
OSC 3
NOISE
The outputs of the various sound sources can be mixed together in any proportion to
produce the overall synth sound, using what is essentially a standard 5-into-1 mono mixer.
The three Oscillators, the Noise source and the Ring Modulator output each have level
controls, Osc 1 38 , Osc 2 39 , Osc 3 40 , Noise 42  and Ring 1*2 41  respectively.
There is also a  “master” level control, VCA Gain 43 , which sets the output level of
the mixer. As the mixer section precedes the Envelopes section, this control scales the
DAHDSR amplitude envelope.
Summit is capable of producing levels in the mixer section that can clip if
all sources are turned up to maximum. It may be necessary to balance the
levels either by turning the sources down or by reducing the VCA Gain
control 43  to ensure that audible clipping does not occur.
The Filter Section
66
60
65
67
62
61
58
64
59
63
The sum of the sounds from the mixer, plus any external audio inputs, is fed to the analogue
Filter Section. The filter is used to modify the harmonic content of this combined sound.
In Single mode, the filter affects all voices: in Multi mode, you can apply different filtering
characteristics to each of the two Parts. Summit’s filters are of analogue design, and have
an extensive set of configuration, modulation and control options.
Filter type and slope
The Shape button 58  selects one of three filter types: low-pass (LP), band-pass (BP)
or high-pass (HP). A fourth option, Dual, gives access to a wide range of further filter
configuration options through the Voice menu.
Cutoff frequency
Frequency
Volume
Low pass filter
12 dB/oct
Cutoff frequency
Frequency
Volume
High pass filter
12 dB/oct
Centre frequency
Frequency
Volume
Band pass filter
12 dB/oct


---

## Page 28

28
The filter section of each of Summit’s two internal synths is devised around analogue filters
with a slope of 12 dB/octave: each voice played includes two such filters.
The Slope button 59  sets the degree of rejection applied to out-of-band frequencies;
in the 12 dB setting, only one filter is placed in circuit, but when set to 24 dB, two filter
sections are cascaded (placed in series), resulting in a steeper slope. An out-of-band
frequency will be attenuated more severely with the 24 dB setting.
Cutoff frequency
Frequency
Volume
Low pass filter
24 dB/oct
Cutoff frequency
Frequency
Volume
High pass filter
24 dB/oct
Centre frequency
Frequency
Volume
Band pass filter
24 dB/oct
The Slope settings only have relevance when a low-pass, band-pass or high-pass filter
is selected by the Shape button. The diagrams below illustrate the effect of Slope with
Shape set to LP (the same principle applies to BP and HP):
LPF
12 dB/oct
Slope = 12 dB
LPF
12 dB/oct
Slope = 24 dB
LPF
12 dB/oct
Cutoff frequency
Frequency
Volume
Low pass filter
12 dB/oct
Cutoff frequency
Frequency
Volume
Low pass filter
24 dB/oct
If Shape is set to Dual, page 4 of the Voice menu is displayed on the OLED and Slope
is set to 12 dB (Note - the Slope LEDs may still indicate 24 dB if this was the last setting
with a single filter configuration selected). This menu page lets you combine the two filter
sections in several other ways; specifically, by allowing combinations of two different filter
types.
Many additional filter configurations are available via the Voice menu.
See Dual Filter Options and Filter Frequency Separation on
page 24
Frequency
The large rotary Frequency control 60  sets the cut-off frequency of the filter when Shape
is set to HP or LP. With BP selected, Frequency sets the centre frequency of the filter’s
pass-band.
Sweeping the filter frequency manually will impose a “hard-to-soft” characteristic on almost
any sound.
Frequency is more complex when Shape is set to Dual and you select one of the dual
filter combinations. See the section on the Voice menu on page 22 for more details.
Resonance
The Resonance control 61  adds gain to the signal in a narrow band of frequencies
around the frequency set by the Frequency control. It can accentuate the swept-filter
effect considerably. Increasing the resonance parameter is good for enhancing modulation
of the cut-off frequency, creating an edgy sound. Increasing Resonance also accentuates
the action of the Frequency control, giving it a more pronounced effect.
Volume
Frequency
Cutoff
Frequency
Low Pass 24 dB
with Resonance
Setting Resonance to a high value can greatly increase the output signal level – the synth
volume – and in some cases can cause unwanted clipping. This can be compensated for
by adjusting VCA Gain 24 .
Filter modulation
The filter’s Frequency parameter may be modulated - using the physical controls - by the
output of LFO 1, the Amplitude Envelope, Modulation Envelope 1, Oscillator 3, or any
combination of these.
Modulation by LFO 1 is controlled by the LFO 1 Depth control 65 , and by the Env
Depth control 64  for either of the two envelopes. The Env Depth control is assigned
to the Amplitude Envelope by selecting Amp Env with the Source button 63 , and to
Modulation Envelope 2 by setting Source to Mod Env. Both mod sources may be used
simultaneously, with the Env Depth control adjusting only the currently selected envelope.
As with many other control routings between synth sections, a great many more options for
modulating the filter may be explored using the Modulation Matrix (see page 38).
Note that only one LFO – LFO 1 - is available for filter modulation using the panel controls.
(LFOs 2 -4  may be patched to modulate the filter using the Modulation Matrix.) Filter
frequency can be varied by up to eight octaves.
Negative values of LFO 1 Depth “invert” the modulating LFO waveform; the effect of this
will be more obvious with non-sinusoidal LFO waveforms and low LFO rates. With positive
Depth values a falling sawtooth LFO waveform will cause the filter frequency to drop
and then rise sharply before lowering again, but if Depth has a negative value, the filter
frequency variation will be the opposite.

Modulating the filter frequency with an LFO can produce some unusual “wah-wah” type
effects. Setting LFO 1 to a slow speed can add a gradual hardening and then softening
edge to the sound.
When the filter’s action is triggered by an envelope, the filter action changes over the
duration of the note. By adjusting the Envelope controls carefully, this can produce some
very pleasing sounds, as for example, the spectral content of the sound can be made to
differ considerably during the attack phase of the note compared to its “fade-out”.
Env Depth lets you control the “depth” and “direction” of the modulation; the higher the
value, the greater the range of frequencies over which the filter will sweep. Positive and
negative values make the filter sweep in opposite directions, but the audible result of this
will be further modified by the filter type in use.
Summit also allows direct modulation of the Filter frequency using Oscillator 3: this is
controlled by the Osc 3 Filter Mod control 66 . The intensity of the resulting effect is
dependent on the control setting, but also almost all Osc 3 parameters - range, pitch,
waveform, pulse width, plus any modulation applied to the Oscillator - can have a profound
effect on the filter’s behaviour,.
Try adding Osc 3 Filter Mod while sweeping Osc 3 pitch with the pitch
wheel.


---

## Page 29

29
Filter tracking
The pitch of the note played can be made to alter the cut-off frequency of the filter. This
relationship is controlled by the setting of the Key Tracking control 67 . At the maximum
value (127), the filter cut-off frequency moves in semitone steps with the notes played
on the keyboard – i.e., the filter tracks the pitch changes in a 1:1 ratio. This means when
playing two notes an octave apart, the filter cut off frequency will also change by one
octave. At minimum setting (value 0), the filter frequency remains constant, whatever
note(s) are played on the keyboard.
When using filter resonance as an additional oscillator, set Key Tracking
to maximum (127) to allow the filter to be played ‘in tune’.
Overdrive
The filter section includes a dedicated drive (or distortion) generator; the Overdrive
control 62  adjusts the degree of distortion treatment applied to the signal. The drive is
added before the filter.
Two further Filter-related parameters – Filter Post Drive and Filter
Divergence - are also available for adjustment in the Voice menu.
See page 23.
The Envelopes Section
Each of Summit’s two internal synths generates three envelopes each time a key is
pressed, which can be used to modify the synth sound in many ways. The envelope
controls are based on the familiar ADSR concept, though Summit adds two further
envelope phases, Delay and Hold, which are adjusted in the Env menu. Thus we refer in
this User Guide to the DAHDSR sequence.
VOLUME
TIME
KEY “ON”
KEY “OFF”
SUSTAIN
ATTACK
HOLD
DECAY
RELEASE
DELAY
The DAHDSR envelope can be most easily visualised by considering the amplitude
(volume) of a note over time. The envelope describing the “lifetime” of a note can be split
into six distinct phases:
•	 Delay – the time from when the key is struck to when the Attack phase of the
envelope commences. The note is not audible during this phase. For most regular
playing styles, Delay will be set to zero, but it is a useful parameter when setting up
special sound effects.
•	 Attack – the time it takes for the note to increase from zero (i.e., from the end of the
Delay phase) to its maximum level. A long attack time produces a “fade-in” effect.
•	 Hold – the time for which the note stays at the level reached in the Attack phase.
•	 Decay – the time it takes for the note to drop in level from the maximum value
reached at the end of the Attack phase (and maintained throughout the Hold phase)
to a new level, defined by the Sustain parameter.
•	 Sustain – this is an amplitude value, and represents the volume of the note after the
Attack, Hold and initial Decay phases – i.e., while holding the key down. Setting a
low value of Sustain can give a short, percussive effect (providing the Attack, Hold
and Decay times are short).
•	 Release – This is the time it takes for the note’s volume to drop back to zero after
the key is released. A high value of Release will cause the sound to remain audible
(though diminishing in volume) after the key is released.
Although the above discusses DAHDSR in terms of volume, note that each of Summit’s
two Parts has the facilities of three separate envelope generators, referred to as Amp
Envelope, Mod Envelope 1 and Mod Envelope 2. All three envelopes per Part are
generated each time a key is struck, though each may have a completely different set of
parameters.
•	 Amp Env controls the amplitude of the synth signal, and is always routed to the
VCA in the output stage (see page 21). Summit also allows Amp Env to directly
modulate the frequency of the Filter section using panel controls.
•	 Mod Env 1 & 2 – the two modulation envelopes – are routed to various other
sections of Summit, where it can be used to alter other synth parameters over the
duration of the note. These are:
•	 Mod Env 1 can modulate the waveform shape of any of the three Oscillators, at
a degree set by the Shape controls 22  when the associated Source button
23  is set to Mod Env 1.
•	 Mod Env 1 may also modulate the filter frequency, at a degree set by the Env
Depth control 64  when the Source button 63  is set to Mod Env 1.
•	 Mod Env 2 can modulate the pitch of any of the three Oscillators, at a degree
set by the Mod Env 2 Depth controls 20 .
It must be emphasised that the above routings are only those available directly using
Summit’s top panel controls: many more routing options are available using the Modulation
Matrix (see page 38).
47
47
46
44
45
Summit’s Envelope section has two sets of four slider controls, one set for Amp Env,
the other for either Mod Env 1 or Mod Env 2, as selected by the Select button 46 .
The sliders are dedicated to four of the DAHDSR parameters (attack, decay, sustain and
release); the descriptions below describe the effect of the Amp Envelope controls as
amplitude variations are more easily visualised, though the effect of the corresponding
Mod Envelope controls is identical. The two remaining envelope phases, Delay and Hold
are adjusted in the Envelopes Menu.
•	 Attack - sets the note’s attack time. With the slider at its lowest position, the
note attains its maximum level immediately the key is pressed; with the slider in its
uppermost position, the note takes over 18 seconds to reach its maximum level.
•	 Decay - sets the time the note takes to decay from the level reached in the Attack
phase and maintained throughout the Hold phase, to that defined by the Sustain
parameter. Maximum decay time is approx. 22 seconds.
•	 Sustain - sets the volume of the note after the decay phase. A low Sustain value
with a higher Decay phase will have the effect of emphasising the start of the note;
with the slider fully down, the note is inaudible when the decay time has elapsed.
•	 Release - Many sounds acquire some of their character from the notes remaining
audible after the key is released; this “hanging” or “fade-out” effect, with the note
gently dying away naturally (as with many real instruments) can be very effective.
Summit has a maximum release time of over 24 seconds, but shorter times will
probably be more useful!  The relationship between the parameter value and the
Release Time is not linear: this means much finer control is available over shorter
release times.
With a high Sustain setting and zero Attack, Decay and Release, the
envelope will act like an On/Off control when the key is pressed and
released: the note will begin immediately the key is pressed and stop
immediately when it is released. This can be reminiscent of the style of key
control found on traditional organs.


---

## Page 30

30
The Envelopes Menu
The following Envelope parameters are available in the Env menu. Each Envelope has two
menu pages; the parameters available for each Envelope are identical, except that the
default value of the MonoTrig parameter for the Mod Envelopes is Re-Trig.
The default menu displays for the Amp Envelope are shown below:
AMP ENVELOPE     1/6
Velocity     +0    H
MonoTrig   Legato
AMP ENVELOPE     2/6
HoldTime     0
Repeats      3
Delay        0
Velocity

Displayed as:

Velocity

Initial value:

0

Range of adjustment:
-64 to +63
Velocity does not modify the shape of the DAHDSR envelope in any way, but adds
touch sensitivity to the sound. In the case of the Amplitude Envelope, setting a positive
parameter value will mean the harder you play the keys, the louder will be the sound. If set
to zero, the volume is the same regardless of how the keys are played. The relationship
between the velocity at which a note is played and volume is determined by the value. Note
that negative values have the inverse effect.
For the most “natural” playing style, try setting Amplitude Velocity to
about +40.
The sonic effect of the corresponding Velocity parameter for the two Modulation Envelopes
will depend on what the Envelopes are used for: for example, if they are used to modulate
Filter Frequency (a common application), a positive Velocity parameter will result in a
greater degree of filter action when the keys are struck harder.
Further control of keyboard touch sensitivity is available by adjusting the
VelCurve parameter, which can be found on Page F of the Settings
menu. See page 44 for more details.
Multi-Triggering

Displayed as:

MonoTrig

Initial value:

Legato

Range of adjustment:
Legato or Re-Trig
When this parameter is set to Re-Trig, each note played will trigger its full DAHDSR
envelope, even if other keys are held down. In Legato mode, only the first key to be
pressed will produce a note with the full envelope, all subsequent notes will omit the Attack
and Decay phases, and sound only from the start of the Sustain phase. “Legato” literally
means “smoothly”, and this mode aids this style of playing.
It is important to appreciate for the Legato mode to be operative, Mono or MonoLG
modes must be selected in the VOICE control area of the panel – it will not work with
polyphonic voicing or Mono2 mode. See page 22.
What is Legato?
The musical term Legato means “smoothly”. A Legato keyboard style is
one where at least two notes overlap. This means as you play the melody,
you keep the previous (or an earlier) note sounding as you play another
note. Once that note is sounding, you then release the earlier note.
Delay

Displayed as:

Delay

Initial value:

0

Range of adjustment:
0 to 127
Summit adds two additional phases to the traditional ADSR envelope: the first of these
is Delay. When Delay has the default value of 0, the envelopes commence their Attack
phase as soon as a key is struck. Delay inserts a variable time lag between striking the key
and the start of the remainder of the AHDSR envelope. At its maximum value of 127, the
envelope does not begin until 10 seconds after the key is pressed. Delays much shorter
than this are likely to be of more interest, and the relationship between the parameter value
and the delay time has been deliberately made exponential to allow for this: a value of about
85 introduces a delay of one second.
Hold time

Displayed as:

HoldTime

Initial value:

0

Range of adjustment:
0 to 127
The Hold parameter is a further additional phase of the envelope: many synthesisers
only offer control of an ADSR envelope but Summit allows further control of the note’s
“lifetime”. Once the note has completed the Attack phase, the envelope will remain at its
maximum level for a determined set by HoldTime. In terms of the Amplitude Envelope,
if HoldTime is not set to zero, the note will stay at its maximum volume for a finite time
before reducing in volume over the time set by Decay. If HoldTime is set to zero, the
Decay phase commences immediately the maximum level is reached at the end of the
Attack phase. The maximum value of 127 corresponds to a hold time of 500 mS.
Repeats

Displayed as:

Repeats

Initial value:

On

Range of adjustment:
1 to 126, On
Repeats allows you to set “looping envelopes”: when a note is struck, the Attack, Hold
and Decay phases of the envelope can be made to repeat any number of times up to 126
before the sustain and release phases of the envelope are started. This looping function is
enabled (and disabled) with the Loop button 47 . With Loops off, the DAHDSR envelope
is followed as normal. When Loop is on, the value of Repeats sets the number of times
the Attack, Hold and Decay envelope phases are implemented. When set to the default
value of On, the Attack, Hold and Decay phases are repeated continuously until the note is
released, when the release phase commences.
The LFO Section
Summit has four Low Frequency Oscillators (LFOs), denoted LFO 1 to LFO 4. LFO 1 and
LFO 2 are per-voice; that is, their modulating effect is applied independently to each of the
voices. Their primary parameters are immediately user-adjustable via panel controls: there
are numerous further parameters in the LFO menu.
LFO 3 and LFO 4 are “global”, in that their modulating effect is applied to the eight voices
after they have been mixed together. This is particularly useful as these LFOs can be used
to modulate FX parameters via the FX Modulation Matrix. Waveform and rate controls for
LFO 3 and LFO 4 are provided on the panel; again, further parameters are available in the
LFO menu.
All four LFOs are also available for routing to other parts of Summit via the Modulation
Matrix.
LFO 1 and LFO 2 hardware controls
24
26
25
27
LFO 1 and LFO 2 are identical in terms of features, but their outputs may be directly routed
using the panel controls to different parts of the synth and are thus used differently, as
outlined below:
