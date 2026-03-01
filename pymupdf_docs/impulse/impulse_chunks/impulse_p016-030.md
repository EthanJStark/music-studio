# Impulse User Guide V5 En (Pages 16-30)

> Converted from PDF using `pymupdf4llm`. Source: `/Users/ethan.stark/dev/misc/music-studio/pdf/impulse_user_guide_v5_en.pdf`.

---

## Page 16

**English**


```
                       Tempo
```

**Page 3: Tempo (** **)**
This sets the tempo of Impulse’s internal MIDI clock, in
BPM. This can be useful in live performance for arpeggiator
and roll timings. The range is 40 to 240, with a default value
of 120 BPM.

```
                          ClockSrc
```

**Page 4: Clock source (** **)**
This setting selects the source for Impulse’s clock
synchronisation, which is used for the Arpeggiator and Roll
```
                                Int Usb
```
functions. The options are: Internal ( ), USB ( ), MIDI
```
                Mid Aut
```
( ) or Auto ( ). In Auto setting, the setting reverts to
Internal when no USB sync source is present; note that Auto
mode ignores any clock signal that may be present at the
**MIDI In** DIN socket. Also, Auto mode will ensure that the
internal clock will continue to run at the ‘last-known’ external
clock rate should the external USB clock source fail.

```
                            DIN From
```

**Page 5: MIDI Out source (** **)**
This setting determines whether an external device
connected to the DIN **MIDI Out** socket will receive its
```
                                 Loc
```
MIDI commands locally from Impulse ( ) or from your
```
                    Usb
```
computer ( ). This is a useful feature when you are using
both music software and additional external devices such as
```
                               Loc
```
synths. The default setting is local ( ).

```
                             DumpSYX?
```

**Page 6: SysEx Data Dump** ( )
With this option selected, pressing **Enter** 14 will let
you download all Impulse’s current internal settings for
the currently active template. This is a useful exercise
for backup security, or for transferring a template to
another Impulse.


Note – There is no need to enter any specific ‘mode’ to import SysEx data. Impulse is always
in ‘read’ mode; it is only necessary to transmit the SysEx data (either from another Impulse or
from a computer using a MIDI SysEx utility). The imported data is initially loaded into a RAM
buffer; when you are happy that the transfer is complete you can then overwrite (save) the
template data into the desired template location.



**16**

---

## Page 17

**English**



**Keyboard Settings**
Primary keyboard parameters can be set in Keyboard mode, which is entered by pressing
the **Keyboard** button 8 ; the LED in the button confirms the mode. Keyboard settings are
per-template, so be sure you are working with the correct template before entering this mode.
Keyboard settings pages can be selected by pressing the **+/–** buttons 7 with the settings in
each adjusted with the **Data** knob 14

```
                        MIDIPort
```

**Page 1: Midi Port** ( )
This lets you set the MIDI port to be used with the
```
                                     Usb
```
currently-selected template. Options are: USB ( ),
```
                  Mid ALL
```
MIDI ( ) or All ( ). The default is All (i.e., both USB
and the DIN MIDI ports).

```
                                VelCurve
```

**Page 2: Keyboard Velocity Curve** ( )
```
                                 1 4
```
This selects one of four velocity tables ( to ) Velocity
```
                  2
```
curve is the default, and should be acceptable for most
playing styles. Using the same amount of force, setting
```
                VelCurve 1
```
to will output lower note velocities when
```
                               3 4 Off
```
compared to the higher settings of or . When set to,
all notes played from the keyboard have a fixed velocity of
127.

```
                         Aftertch
```

**Page 3: Aftertouch** ( )
Impulse’s keyboard is equipped with Channel Aftertouch,
which sends an additional set of MIDI data when further
pressure is applied to a key while it is being pressed. The
options are **On** or **Off** . The default setting is **On** as many
plug-ins use Aftertouch, but in some situations, you may
prefer to switch it off.



**17**

---

## Page 18

**English**



**MIDI Channel**



MIDI data can be sent on any one of 16 channels, and will
only be received and interpreted correctly if the receiving
device is set to the same channel. Press the **MIDI Chan**
button to set the channel number.


Use the Data knob to change the MIDI channel number from
the default of 1. Note that MIDI channel numbers are part of
the template, and therefore any changes must be saved to
the template as described above (see “Loading and Saving
a Template” on page 13).



**Zones**
Normally Impulse’s keyboard uses the same MIDI channel for all its notes. Using Zones, it can
be split into 2, 3 or even 4 separate or overlapping regions. Each Zone can have its own MIDI
channel, port, and keyboard range. This feature can be of tremendous benefit when playing
live.


Press the **Zones** button to enable and configure keyboard zones; the LED in the button lights to
confirm the mode.

```
                           KbdZones
```

**Page 1: Zones Enable** ( )
Use the data entry knob to select **On** or **Off** (default). When
Zones are set **On**, a **ZONES ON** element lights in the
display to remind you that Zones are enabled.

```
                          Z1 Start
```

**Page 2: Zone 1 Start** ( )
There are two methods of selecting the lowest note in the
Zone: i) press the note on the keyboard, and its note name
will be displayed; ii) use the data knob to scroll through the
list of available notes.



**18**

---

## Page 19

**English**


```
                         Z1 End
```

**Page 3: Zone 1 End** ( )
You can set the upper note of the Zone in the same manner
as the lowest.

```
                           Z1 Octav
```

**Page 4: Zone 1 Octave** ( )
This enables you to change the octave that the keys in the
```
                           0
```
zone will play. A setting of (the default) means that the
notes in the zone will play at their normal pitch. Note that
the range of octaves available varies between the three
Impulse models.

```
                              Z1 Chan
```

**Page 5: Zone 1 MIDI Channel** ( )
Each Zone can use a different MIDI channel, enabling you
to play different sound sources from different parts of the
keyboard. You can set the Zone to any of the 16 standard
```
                           tPL
```
MIDI channels, or select, when the Zone’s MIDI
channel will follow that set in the current template.

```
                          Z1 Ports
```

**Page 6: Zone 1 Ports** ( )
As well as selecting a different MIDI channel for each
Zone, you can also set the MIDI Port each Zone uses. The
```
                          tPL
```
options are: Template ( ) – the port will be that set in the
```
                          Usb
```
current template; USB ( ) – the USB port will be used;
```
                  Mid ALL
```
MIDI ( ) – the DIN sockets will be used; All ( ) – both
```
                                Off
```
USB and DIN ports will be used; Off ( ) – the Zone is
disabled.


**Pages 7 to 21: Zones 2 to 4**
The remaining pages in the Zones menu repeat the settings available for Zone 1 in Pages 2 to 6.


**Program Change**


You can manually transmit a MIDI Program Change
message from Impulse. Press **Shift** + **MIDI Chan** to enable
**Prog Change** mode.


Select the Program Change number with the Data knob and
the MIDI data will be transmitted. Note: Program Change
MIDI values are automatically transmitted as the Data knob
is turned – i. e., this makes it possible to browse through
patches simply by turning the knob. Press **Enter** to exit this
mode and revert the screen to the normal display.



**19**

---

## Page 20

**English**



**Transport Controls**
Impulse is provided with a standard set of six ‘transport’ controls 18, which can be used to
start, stop, relocate, etc., within your DAW’s timeline. They act as a convenient remote control
for the software and duplicate the on-screen buttons.


The transport buttons are always active, but your DAW will need to be set correctly to respond
to their commands. Also, you will need to ensure that they are set to send the correct type of
MIDI message – MIDI Machine Control or Continuous Controller – for the DAW. (See “Setup
Mode” on page 15)


**Arpeggiator**
Impulse has a powerful Arpeggiator feature which allows arpeggios of varying complexity and
rhythm to be played and manipulated in real-time. If a single key is pressed, the note will be
retriggered by the Arpeggiator. If you play a chord, the Arpeggiator identifies its notes and plays
them individually in sequence (this is termed an arpeggio pattern or ‘arp sequence’); thus if you
play a C major triad, the selected notes will be C, E and G.


The Impulse Arpeggiator is enabled by pressing the **Arp** button 15 ; its LED will light to confirm
and the eight drum pads will turn green. Holding a note down will repeat the note in the
sequence, and you will see the pads’ illumination changing as the pattern progresses. Initially
all enabled beats in the sequence are sounded, but if you press a pad, the beat corresponding
to that pad’s position will now be omitted from the sequence, generating a rhythmic pattern.
The ‘deselected’ pads will show red instead of green. A ‘deselected’ pad may be re-enabled by
tapping it a second time. The pads are velocity-sensitive, and how hard the pads are hit, when
being enabled determines the velocity of the note in the sequence. The initial default state is for
all notes in the sequence to be at equal velocity.



**20**

---

## Page 21

**English**



**Arpeggiator Settings menu**
Various parameters controlling the Arpeggiator’s operation can be set in the Arpeggiator
Settings menu, which is entered by holding down the **Shift** button and pressing **Arp** ; the LED
in the **Arp** button flashes in this mode.

```
                      Sync 1/x
```

**Page 1: Sync** ( )
This parameter effectively determines the beat of the
arp sequence, based on the tempo rate. The sync rate is
adjusted with the Data knob and can have any of 12 values
from 1 beat to 96, which correspond to divisions of the
tempo rate.

```
                      Gate
```

**Page 2: Gate** ( )
This parameter sets the basic duration of the notes played
by the Arpeggiator, though this may be further amended by
the Swing parameter (see below). The lower the parameter
value, the shorter the duration of the note played. At a
setting of 100, each note in the sequence is immediately
followed by the next without a gap. At the default value of
50, the note duration is exactly half the beat interval as
set by the tempo rate, and each note is followed by a rest
of equal length. Values over 100 will cause the notes to
‘overlap’.

```
                       Swing
```

**Page 3: Swing** ( )
If this parameter is set to something other than its default
value of 50, some further interesting rhythmic effects can
be obtained. Higher values of Swing lengthen the interval
between odd and even notes, while the even-to-odd
intervals are correspondingly shortened. Lower values
have the opposite effect. This is an effect which is easier to
experiment with than describe!



**21**

---

## Page 22

**English**


```
                         Arp Mode
```

**Page 4: Arp Mode** ( )
The Arpeggiator will play all notes held down in a sequence
which is determined by the Arp Mode setting. The options are:

                         - **Up** ( `uP` ) - sequence begins with the lowest note played

                         - **Down** ( `dn` ) - sequence begins with the highest note
played

                         - **Up/Down 2 (** `ud2` **)**                         - sequence alternates in direction
and repeats the highest and lowest notes

                         - **Chord** ( `crd` ) – all keys held are played simultaneously
as a chord

                         - **Up/Down** ( `uPd` ) – sequence alternates in direction

                         - **Random** ( `rnd` ) – the keys held are played in a
continuously varying random order

                         - **Key Order** ( `PLY` ) – sequence comprises notes in the
order in which they are played

```
                         Arp Octv
```

**Page 5: Arp Octave** ( )
This setting adds upper octaves to the arp sequence. If Arp
Octave is set to 2, the sequence is played as normal, then
immediately played again an octave higher. Higher values
of Arp Octave extend this process by adding additional
higher octaves. Arp Octave values greater than 1 have the
effect of doubling, tripling, etc., the length of the sequence.
The additional notes added duplicate the complete original
sequence, but octave-shifted. Thus a four-note sequence
played with Arp Octave set to 1, will consist of eight notes
when Arp Octave is set to 2. You can set Arp Octave to 1, 2,
3 or 4.

```
                         ArpLngth
```

**Page 6: Arp Length** ( )
This sets the length of the sequence, and has a default
value of 8. Reducing it to a lower value simply reduces the
number of notes in the sequence.


**Setting the Arp/Roll Tempo**
The tempo for Arp and Roll modes is set in the Tempo page of the Setup menu (see “Tempo”
on page 16). However, it may also be accessed directly by pressing **Shift** + **Roll** 8 + 15 ; the
**Roll** LED and drum pad 5 flash in this mode. Alternatively, you can set the tempo ‘manually’, by
tapping a steady beat on drum pad 5. Note that tapping out a tempo in this way is only possible
if Clock Source is set to Internal (see “Clock Source” on page 16).


Note that by pressing **+**, you can also access the Clock Source settings menu page from here.


Press **Roll** again to cancel and return to default display.



**22**

---

## Page 23

**English**



**Roll Mode**
Roll mode gives you a convenient method of repeatedly triggering a single note – typically a
percussive effect such as a drum sound. Enable Roll by pressing the **Roll** button 15 The Roll
button LED illuminates and the drum pads glow red. Pressing a drum pad will now trigger the
sound assigned to it for as long as the pad is pressed. The pads’ velocity-sensing is still active

- the volume will be proportional to the pressure applied to the pad. See also “Pad Curve” on
page 15.


Certain arp parameters (set in the Arpeggiator Settings menu – see page 21) have an effect on
the rhythmic pattern of the roll.

**Boot Menu**
The boot menu will not be required in normal operation, but is there to let you update Impulse’s
firmware, check firmware version numbers and also to reset all the settings to the original
factory values.


Boot menu is entered by holding down the **+**, **-** and **Shift** buttons simultaneously while applying
power – i.e., while plugging in the USB cable.

```
                      Exit
```

**Page 1: Exit** ( )
Press Enter to leave the boot menu.

```
                       Setup
```

**Page 2: Setup** ( )
This is related to the Impulse model and is for factory use
only. Do not alter this setting! A long press on the **–** button
(Cancel) will exit this level.

```
                        Version
```

**Page 3: Version** ( )
Pressing **Enter** shows the firmware version of the Boot



**23**

---

## Page 24

**English**



Program; press the **+** button to see the version number of the main firmware program. A long
press on the – button (Cancel) will exit this level.
```
                                Fac Rst
```

**Page 4: Restore Factory defaults** ( )
This will restore all Impulse’s internal settings to their
original factory values. Any changes you have made will
be lost. Pressing **Enter** will give you a confirmation screen
```
                Really?
```
( ) to give you one more chance to change your
mind! Press **Enter** again to continue, or a long press on
the **–** button (Cancel) will exit this level.



**24**

---

## Page 25

**English**


# **USING IMPULSE WITH HUI**

**Introduction**
The HUI protocol allows the Impulse to act like a Mackie HUI device and interact with DAWs
that provide HUI support (for example, Cubase, Studio One, Reaper and Pro Tools).

**HUI Connection**
From the standard template mode, the Impulse automatically switches to HUI view as soon as
it detects a Heartbeat message (sent by a DAW once settings are configured). If the Impulse
does not receive a heartbeat message for over five seconds, it automatically switches back to
standard template mode.


While in HUI mode, a connection icon will appear
on the screen, and the Mixer / Plugin buttons will
illuminate.


It is possible to individually release either the fader section or the encoder section from HUI
mode without breaking the HUI connection, while retaining the remaining HUI functionality.


**Releasing/re-entering the fader section from HUI mode**
To release the fader section from HUI mode, press the MIDI button beside the fader section.
The MIDI button will become lit while the mixer button will become unlit, signalling the mode
release. To re-enter HUI mode, press the Mixer button.


Note that Impulse 25 only has a single Fader section button which will toggle between the
aforementioned modes. When the button is lit the fader is in HUI mode, when the button is unlit
the fader is in standard template mode


**Releasing/re-entering the encoder section from HUI mode**
To release the encoders from HUI mode, press the MIDI button beside the encoder section.
The MIDI button will become lit while the Plugin button will become unlit, signalling the mode
release. To re-enter HUI mode press the Plugin and MIDI button at the same time.

**Channel Control**


**Volume**
You can change Volume with the first eight faders of Impulse. The 9th fader (or the only fader
on Impulse 25) sends CC#7 message on Impulse’s MIDI port.


**Pan**
You can change a channel’s Pan position using the rotary encoders.



**25**

---

## Page 26

**English**



**Mute/Solo**
The first eight soft buttons under the faders can be used to control Mute or Solo functions
on individual channels. The Mute/Solo button can be used to toggle between Mute and
Solo control and display. Depending on the DAW you are using, buttons LEDs may behave
differently. For example, in Pro Tools, if a track is soloed then the others will flash. Note that
Impulse 25 doesn’t have any solo/mute buttons.


**Send Control**
Press Shift + Plugin/MIDI to change the encoder assignment to control send levels.


**Transport Control**
The Transport buttons control the equivalent DAW functions. While mostly similar, the function
of each button depends on the DAW. Generally, the functionality is (from left to right) as follows:
Rewind, Fast-Forward, Stop, Play, Loop On/Off, Arm/Record.


**Track Left and Right**
This moves the currently controlled bank (8 channels) one channel to the left or right. Press
Shift + Octave Down to move left or Shift + Octave Up to move right.


**Bank Up and Down**
This moves a full bank up or down. Shift + Mixer triggers Bank up or Shift + MIDI triggers Bank
down.



**26**

---

## Page 27

**English**



**DAW Setup**


**Cubase**
To set up the Impulse as a HUI control surface in Cubase, navigate to ‘Studio’ > ‘Studio Setup’

- ‘MIDI Port Setup’. Be careful to set your ports as shown below, the ‘Impulse HUI’ port MUST
NOT have “in ‘all MIDI ins’” enabled.


Click the small ‘+’ icon in the Cubase ‘Studio Setup’ window and select ‘Mackie HUI’. Now, in
the ‘Mackie HUI’ tab, set the input and output port to ‘Impulse HUI’ as shown below.


Note: The ‘Impulse HUI’ port may show as ‘MIDIIN3’/’MIDIOUT2’ or something similar on
Windows.



**27**

---

## Page 28

**English**



**Reaper**
Please note that Reaper version 5. 941 or newer is required to work with the Impulse.


To set up the Impulse as a HUI control surface in Reaper, navigate to ‘Options’ > ‘Preferences...’

- ‘MIDI Devices’. Be sure to set your ports to ‘Focusrite A.E. Ltd. - Impulse HUI (MIDIIN3 for
Windows), as shown above, the ‘Focusrite A.E. Ltd. - Impulse HUI’ should not say ‘!! N/A...’ If
this is the case please right-click the device and choose ‘Forget device’.


Navigate to the ‘Control/OSC/web’ tab in the ‘Reaper Preferences’ window and click ‘Add’
to add a new control surface. Now, in the ‘Control Surface Settings’ window, set the Control
surface mode to HUI (partial) and set the input and output port to ‘Focusrite A.E. Ltd. - Impulse
HUI’ as shown below.



**28**

---

## Page 29

**English**



**Studio One**
To setup the Impulse as a HUI control surface for Studio One, navigate to ‘Preferences’ >
‘External Devices’ and click ‘Add’ to add a new device. Now, in the ‘Add Device’ window, select
HUI under the Mackie folder and set Studio One to receive from ‘Impulse HUI’ and send to
‘Impulse HUI’ as shown below.


On Windows, Studio One should receive HUI messages through MIDIIN3 and send to
MIDIOUT2.


Press OK and the Preferences-External Devices Menu should look as shown below.



**29**

---

## Page 30

**English**



**Pro Tools**
To set up the Impulse HUI in Pro Tools, navigate to ‘Setup’ > ‘Peripherals...’ > ‘MIDI Controllers’.
Ensure your ports are set up as below. Set Type to ‘HUI’, Receive From/Send To to the ‘Impulse
HUI’ port (MIDIIN 3/MIDIOUT2 on Windows) and # Ch’s to 8.



**30**
