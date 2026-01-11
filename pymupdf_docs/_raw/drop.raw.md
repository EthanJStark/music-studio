# Page 1

# Manual

Firmware version 1.07
www.neuzeit-instruments.com

-----

# Page 2

### **Table of Contents**

2

-----

# Page 3

3

-----

# Page 4

|Col1|Col2|
|---|---|
|**grid**<br>**JUMP**|**grid**<br>**JUMP**|



4

-----

# Page 5

TAP tap in the tempo by hand
CLOCK bpm and clock config


SHIFT access the
secondary functions


SAVE Save snapshot
EDIT Edit snapshot


BANK
Select snapshot bank
COPY
Copy snapshot


Cycle buttons
A _cycle has a length of 1-32 bars_ .
The button s LEDs show the ’
playback position within the cycle,
also signaling ongoing Jumps or
Drops by turning blue or red.


PLAY
Opens the performance views.


LAYER A / B
Switch between two layers
of the control elements.



Fade time for snapshot Jump
Maximum duration is configurable in settings


JUMP
Fire snapshots in jump mode.

GRID
Use the button matrix to launch clips in a DAW or

play notes like on a keyboard.


DROP
Schedule snapshots in Drop mode at the end of a cycle.

CHAIN
Arrange snapshots on a timeline.


Button matrix
Function depending on mode.
Fire snapshots, select bank, trigger

clips in DAW using grid mode.


Single or Repeat
execution of snapshots in Drop mode.


MENU
Opens the main menu for configuration and

setup. Also used to go _back_ in some menus.


MENU encoder
Turn and push for navigation.

5



START clock
STOP clock

-----

# Page 6

## **What s in the box’**

Drop ships with some useful accessories to get you started.


- Power supply 12V 1500mA, with adaptors for EU, USA, AU, UK


- USB-C to USB-C cable, can also be used to power the device


- USB-C male to USB-A female adaptor when Drop is USB host


- MIDI adaptor TRS to DIN female


- 2 x MIDI TRS cable 120cm, braided gold-black


- Micro SD-card adaptor to regular sized SD-card

## **Firmware updates**

[Download the latest firmware from our website and save it on your computer.](https://www.neuzeit-instruments.com/drop)


1 Put Drop's SD-card into your computer.)


2 Copy the firmware file into the ) _/Firmwares_ folder on the SD-card.


3 Turn off Drop, reinsert the SD-card.)


4 While powering on Drop, press and hold the Shift button until the display shows up.)


5 Use the menu encoder to select the firmware file and push to update the firmware. )


6

-----

# Page 7

## **Power**

Power Drop using the _included power supply_ or via the _USB1 port_ . The benefit of using the included 12V power supply is that you still have both

USB-C ports available to connect other gear. It is also the best choice to suppress audible noise caused by ground loops.


_Power input: 12V DC, 1200 mA min_ _what Drop requires when powered via external power supply_
_USB1 input:_ _5V DC,  1500 mA min_ _what Drop requires when powered via USB1_
_USB1 output: 5V DC,  1500 mA max_ _when Drop is used as USB host to power other gear via USB (automatic host role detection)_
_USB2 output: 5V DC,  500 mA max     when Drop is used as USB host to power other gear via USB (automatic host role detection)_


If you are using USB-C, you must use the USB1 port with the little flash symbol next to it. You also need a USB-C-to-C connection and your USB host

must be able to supply at least 1500mA. Computer USB-C ports usually can supply twice as much current.


_Only USB-C to USB-C cables in conjunction with a USB-C host or power supply can be used to power Drop. USB-A cables and USB-A power_
_supplies will NOT work for power, even if the power supply meets the electrical requirements. The USB-A socket does not allow the necessary_
_power negotiation between Drop and power supply._



7



_Does not work for powering_ _Works for powering from USB-C_ _Does not work for_ _Works for powering, if_
_host with min 1500mA output_ _powering, no matter_ _min 1500mA output_

_how much current out_ _current_

-----

# Page 8

## **Connectivity**

Drop can control up to eight other MIDI devices with

its user interface. Drop features 2x USB and 4x TRS

MIDI ports, so that each device benefits from _its own_

_connection_, providing full data bandwidth and its own

clock signal with individual micro-delay.


**In this example...**


The laptop ( _DAW_ only offers USB connections, so it is)

obvious to connect it via USB. The laptop may also

power Drop via its USB1 port.


The _SEQUENCER_ may send a lot of MIDI data, so it

may be a good choice to connect it via USB. Also,

Drop can eventually power the sequencer via USB.


_Incoming MIDI_, e.g. from KEYBOARD, GROOVEBOX,

DAW, SEQUENCER, SYNTH A, can be distributed to

other devices using Drop s ’ _Device Merger_ function.


Drop s MIDI ’ _In and Out ports are not related_ to each

other and can be used for different devices, like

KEYBOARD and SYNTH D in this example.


It is still possible to connect devices in classic daisy
chain cabling, using MIDI Thru, like SYNTH A and B.


Drop s two ’ _CV inputs and outputs_ are mostly used for

clock and timing. The outputs can also be variable 0
5V control voltages 12-bit DAC .( )


8

-----

# Page 9

#### **USB, TRS, CV pros and cons**

USB-MIDI: High data rate, not so precise with MIDI clock timing. Requires class-compliant MIDI gear if Drop is used as USB host.
TRS-MIDI: Low data rate, but mostly sufficient, especially when each device has its own cable carrying only the device s data. Precise clock timing.’
CV: On Drop, same clock timing precision as TRS-MIDI.

#### **2x USB-C**

**USB MIDI**


Connect laptops or class-compliant MIDI devices to Drop. With USB, there is always host and device role to be negotiated. Drop will automatically

detect which mode is necessary and can also act as a MIDI host for other controllers and instruments. In MENU > Settings, you can switch the mode

for each port from Host + Device auto-detection to Device Only . As a MIDI host, Drop can supply 5V on each port to power the connected “ ” “ ”

device. USB1 can supply up to 1500mA and USB2 up to 500mA. The specs are also printed on Drop s bottom side. You can also use the included ’

USB-C to USB-A adaptor if your device requires an oldschool USB-A/B cable.


_USB-hubs are not supported, so you can only connect one USB device per port._


To connect to MIDI devices via USB, your device must be class-compliant. This means, that no driver needs to be installed to use it, which applies to
most gear out on the market. However, some manufacturers e.g. Roland still require a driver for their USB-MIDI gear. To use their devices with ( )
Drop, you need to use the classic MIDI TRS/DIN connection. Drop will show you a popup message if the USB gear connected is not class-compliant.

**USB keyboard**


Connect a USB computer keyboard for navigation and to name devices, controls and

snapshots.


In Menu > Settings, select the approriate layout e.g. ( QWERTY, QWERTZ, AZERTY .)


Navigation = Arrow keys, Escape, Enter, Backspace.
Change slot = Shift + Arrow keys
CTRL+9 = MENU button
CTRL+0 = PLAY button
CTRL+1-8 = Buttons around the display, clockwise


9

-----

# Page 10

#### **4x MIDI TRS In, 4x MIDI TRS Out**

Use these ports to connect any MIDI equipment to Drop. Four ports enable you to connect one device per port in a star-topology instead of daisy

chaining the MIDI signal from device to device. The star-topology enables high data throughput and individual MIDI clock delays per device.


_Use the small switches on the back to select TRS type A or B for Drop s MIDI output. If you pick the wrong mode, your device may not receive ’_
_MIDI data from Drop._

#### **2x CV out**

Drop s CV inputs and outputs support a voltage range between 0,0 and 5,0 Volts. ’


The outputs can be used independently to send different kinds of clock signals, triggers and gates to sync analogue gear. They can also be used as a

simple continuous voltage outputs that can be assigned to any of Drop s controls. The resolution is 12 bits 4096 steps .’ ( )

#### **2x CV in**

Use CV inputs 1 and 2 to connect Drop to an external analogue clock source. CV1 expects the clock signal 16( th or 8th notes and CV2 can be )

configured to receive a dedicated start and stop trigger or gate signal.


There is also another mode available that lets you use the CV1 and 2 inputs to fire snapshots from external modular gear, where CV In 1 receives

triggers and CV In 2 receives a control voltage to select a snapshot. You can enable this mode in the _CV Config_ menu.


If you are planning to control your modular rack with Drop, we recommend to use a dedicated MIDI-to-CV-out converter module.


10

-----

# Page 11

## **Step-by-step workflow**

**1 Decide which gear to use)**


Before getting into Drop, you should have an idea of what kind of setup you want to build and what gear you want to connect to Drop. Ideally, you

already have your grooveboxes or synths play a loop, and now it is time to create an accessible user interface for them on Drop.


**2 Init your project)**


Select _Project > Clean Init_ . You now have an empty project that does absolutely nothing the perfect starting point for a – _setup with hardware gear_,

where mapping is all done in Drop.

For a DAW-only setup, _Project > DAW Init_ is a one-click init option that applies a default mapping to Drop, so that every control element sends out a

default CC message over USB1. From there, you can map everything in your DAW. You can skip steps 3 and 4.


**3 Create and configure devices)**


Go to the _Devices_ menu and add the devices you want to use in your live set up to 8 devices max . Even if your device uses multiple MIDI channels, ( )

you only need to list it as one device in Drop. Also hook up keyboards and sequencers that merge their data with Drop s data and send it out to ’

other connected gear. You should also configure clocks in this step.


**4 Mapping on Drop)**


Each of Drop s controls can send out up to 8 different MIDI messages with different curves which allows flexible macro mapping. Each control offers ’

8 Slots to set up different kind of MIDI messages. This is an essential and powerful feature to create a user interface that speaks across multiple

devices in your setup.


Use the _Mapping_ menu to configure the controls you want to use. Depending on your target device, you can either enter the MIDI parameters by

hand, use MIDI Learn, or use the included MIDI CC and NRPN database if it contains your target device.


**5 Snapshots)**


By now, you should have developed a feeling for your newly created user interface. It is time to create some snapshots! These can either be fallback

safety net points, peak moments, snapshots that only affect a subset of controls so you can combine them later, a fixed chain of snapshots that

follow your song s arrangement, or you simply skip snapshots and use them spontaneously on stage as save-and-recall points. ’


11

-----

# Page 12

## **PLAY view**

#### **Beatjump**

This view controls and shows the playback position

inside the current cycle. Use the eight buttons around

the display to jump to another playback position while

playing.



**MIDI traffic monitor**



TRS 1-4 output
TRS 1-4 input


USB 1-2 output
USB 1-2 input



_Note: Performing a beatjump also sends a Song Position message to all devices, that have the according_

_check mark set in the clock menu._



dark green = only clock and system data
green = data
light grey = no traffic
red = data overflow, lose packets
dark grey = nothing connected
blue = USB keyboard connected
Flash symbol = USB port serves as host, delivers
5V power to the connected device.



Change the playback position
Push the eight cycle buttons to change the playback
position. This is useful for example, if you have
scheduled a Drop, and need to shorten or extend the
time until it fires.



Cycle end = Drop time
The 12 o clock position marks the start and end of a cycle. It also marks ’
the time when a snapshot in Drop mode is executed.



Current playback position

Current Jump fade time

Here: bar nr 7 quarter note 3

Changes its length depending on the fade
time potentiometer. If you push a snapshot in
Jump mode right now, this is the time it needs
to fade to it.
Blinking cycle button

playback position



12

-----

# Page 13

#### **Cycle length**

The cycle length can be set from 1 to 32 bars.


Drop is not a sequencer itself, but you can connect other sequencers or

grooveboxes with their internal sequencers to Drop. These other devices

can run their own sequencers with their own time signature. Drop on the

other hand simply keeps a global time measure.


Internally, Drop uses 16 sixteenth notes per bar. But this only plays a role

for clock signals.

#### **Quantization**


Beatjump quantization
Select between 1 bar and

1/4th note quantization

when pushing the cycle

buttons to change the

playback position.


13



Cycle length in bars

Quick select values
1, 2, 4, 8, 16, 32 bars



JUMP snapshot
quantization
Use the other six buttons
to select the quantization
for firing a snapshot in
Jump mode.

-----

# Page 14

#### **Monitor**

The MIDI monitor helps to see and debug what is going on between Drop and a connected MIDI device.


  - Verify, that Drop sends out the data your device expects.


  - Verify, that the connected device sends data back.


  - Check if a device sends unnecessary data that can be filtered out in the MIDI merge filter.


Toggle between input and

output monitoring


message history,
turn the menu encoder



Recording live
messages



Select the
MIDI in port



Select the
MIDI out port



14

-----

# Page 15

## **MENU view**

#### **Devices**

Setting up devices is the first step you should do when creating a new live set. In this menu, up to 8 MIDI

devices can be configured that Drop can interact with at the same time.


Decide, to which port you want to connect your device and if it needs MIDI output, input, or both.


_You can verify proper communication using the MIDI Monitor in the PLAY view._


**ON** Activate or deactivate the device and the control elements linked to it.


**Name** Enter the name of your device, for convenience during the mapping process.


**Default Channel** The default MIDI channel number. Each control that maps to this device can either send to the

default channel or a specific channel 1-16. If your device only uses one channel, use the default channel in the

mapping. That way, if you want to switch the channel at a later point, you only have to change it in the device

menu instead of changing it in each control.


_If you connect a device that uses multiple channels, you should still set up only one device for it._


You can select each control element s channel in that element s mapping specifically. The channel you’ ’

set in the device is just a default value.


15



device



via USB



Enter the device s name’

-----

# Page 16

**Output** The physical port USB1-2 or TRS1-4 on which Drop sends MIDI out to the device


**Input** The physical port USB1-2 or TRS1-4 on which Drop receives data from the device.


**Sub-Port** Only relevant when the device is connected via USB. Some USB devices offer multiple

internal Sub-Ports for communication. Sub-Port 1 works just fine for most USB gear.


_If communication to your USB device fails and it offers more than one Sub-Port, try another one._
_Unfortunately, sub-ports are often not documented in the device s user manual. You simply ’_
_have to try._



_Example: This is how a synth with two USB_
_sub-ports shows up in Ableton Live._



For the nerds: The Sub-Port corresponds to the cable number CN in the USB MIDI protocol. Sub-ports are also reffered to as virtual cables.


_Note: In the clock menu, you can specify to which sub-ports clock and transport messages are being sent._


Gear with MIDI mapping table - Synths and grooveboxes


Enable MIDI Output, and only enable MIDI Input if needed: For example, if the device can send MIDI data back to Drop when turning its knobs, you

can use convenient MIDI Learn for mapping. You should also enable the MIDI Input, if the device includes a MIDI sequencer or a keyboard whose

notes you want to forward to other connected devices.


Gear for MIDI Input only - Keyboards


Usually there is no need to enable MIDI Output, picking only a MIDI Input port is sufficient. To setup MIDI forwarding to another device, use the

target device s MERGER function, described on the following pages.’


Gear with own MIDI mapping - DAWs and workstations


Generally, you should enable both, MIDI Input and Output, and do the mapping on your DAW or workstation. You might also prefer USB over TRS

MIDI. Usually, DAWs and workstations offer their own internal MIDI Learn function and parameter mapping. Use _MENU > Project > DAW Init_ to

quickly apply a default initialization for use with a DAW.


16

-----

# Page 17

**Program Change Pre-Delay** This is a useful feature for grooveboxes that need to receive program

change messages just a little bit before their internal sequencer s pattern ends. ’


Let s assume, you schedule a snapshot in Drop mode fires at the end of a cycle and that snapshot contains’ ( )

a program change message to tell your groovebox to switch to the next pattern. The groovebox may need

to know about the pattern change a little earlier, just before the pattern ends, so it has some

time left to prepare everything for the pattern change. This is what we call a pre-delay. You can select from

different values, like a fixed number of milliseconds or tempo-dependent values like 3/16th notes.


_You want the Program Change Pre-Delay to be as small as possible and as large as necessary._
_Sequencer-based devices (grooveboxes) may need a time-related value like 3/16th notes, while synths_
_may need a fixed amount of time to load a new preset._


You simply have to try out which pre-delay value works best for your device.


card. This database contains mapping tables of popular MIDI gear and simplifies the mapping process.


more convenient.


[The database can be found on https://github.com/pencilresearch/midi](https://github.com/pencilresearch/midi)


has when downloading it.


17

-----

# Page 18

#### **Devices Merger**

Drop s MIDI merger allows you to forward MIDI input data to a’

MIDI output. You can even modify incoming data before it gets

forwarded, like transposing MIDI notes.


_Use case:_

You want to control your synth by Drop s controls, but it should’

also receive notes from a MIDI keyboard. However, your synth

only has one MIDI-In port. This means, the MIDI data from Drop s’

controls must be merged together with the MIDI data from the

keyboard.


18



_Example: Merging a MIDI sequencer, a keyboard and Drop s control elements to ’_
_a synth. Notes can be transposed by Drop s control elements along the way.’_

-----

# Page 19

In order to do this, you need to create two devices on Drop: One for the synth and one for the keyboard. The synth device needs to have a MIDI

Output port selected, the keyboard must have a MIDI Input port.


Now, in the _Devices_ menu, select the receiving device the synth with the lower two buttons dark blue . Scroll down to the MERGER part. Select ( ) ( )

Merger 1-4 with the upper buttons light blue and turn the switch ON to activate the Merger. ( )


_Each device has its own 4 Merger instances. That means, per device you can forward up to 4 different MIDI input streams, which come from_
_other connected devices._



**Merge** Activate the merger instance.


**Input** The device from which this merger instance receives incoming MIDI

data. Obviously, the selected device must have a MIDI Input enabled.


**Listen to Channels** Select the MIDI channels on which the input device sends

the relevant data. This does not necessarily have to match the receiver s MIDI’

channel. It should simply cover the channels which carry the data that is

relevant for the MIDI stream you want to capture.


_Use Drop s MIDI monitor to inspect the MIDI data that comes in. ’_
_Set the message filters and channel selection in a way, so that the_
_receiving device only gets MIDI data it actually understands. Avoid_
_unnecessary MIDI traffic for best responsiveness._



Select the Merger instance
Here: Merger 1 out of 4


Activate the Merger


Select the output device
Here: Device 3 out of 8
named WARP



_Note: Incoming SysEx messages are not forwarded to the receiver. This is because SysEx could potentially block the whole traffic as long as_
_the sender wants._



19

-----

# Page 20

As a best-practice, you should configure your input device first, so that it only sends relevant data and

does not spam unnecessary messages around. Do this as far as possible, and filter out the rest in Drop s’

MIDI Merger.


**Notes** Filter On/Off for MIDI note events


**Bank, CC** Filter On/Off for CC messages. This also includes 14-bit CC messages, NRPN messages and

Bank Select messages.


**Pitchbend** On/Off filter MIDI pitchbend data.


**Aftertouch** On/Off filter MIDI aftertouch, including channel pressure and polyphonic key pressure.


**Prog Chg** On/Off filter MIDI program change messages


**Target Channel** _No Change:_ Leave the MIDI channel as it comes in.

_By Device:_ Modify the channel to the device s Default Channel.’

_Channel 1-16:_ Modify the channel to this channel number.

**Note Gate** Enables mute/unmute functionality for incoming MIDI notes.


_Off:_ Note Gate function disabled.

_On:_ Note Gate enabled. Control element max value = notes pass, min = blocked

_On, inverted:_ Note Gate enabled. Control element max = notes blocked, min = pass.

**Link** Link one of the control elements to the Note Gate function. Press Link“ …”, so the control

elements will start to blink. Then, turn/move/push the control element you want to assign.


**clear** Push the menu encoder to clear the assigned control element.


20



Enable only the MIDI message types

your target synth should receive

-----

# Page 21

The merger also offers note transposition. Notes can be shifted by semitones and octaves. Both menus
are similar.


**Semitone / Octave** Enables note semitone/octave shifting functionality for incoming MIDI notes.


**Shift/Min** The lower boundary of the shifting range. If no Link is set, MIDI notes are always shifted by

that number of semitones/octaves.


**Max** The upper boundary of the shifting range. If a Link is set, the MIDI note shifting range goes

from the minimum to the maximum value.


**Link** Link one of the control elements to the octave shift function. Press Link“ …”, so the control

elements will start to blink. Then, turn/move/push the control element you want to assign.


**clear ←** Push the menu encoder to clear the assigned control element.


_Tip: When linking a rotary control to note shifting, you can also select one of the stepped LED_
_feedback options, so the LED ring jumps in discrete steps instead of moving continuously. Additionally,_
_you can assign the push function of the rotary control to reset the rotary knob to the center/left/right_
_position and thereby reset the transposition._


_Note: When the MIDI cable of a sequencer or keyboard is pulled out while some notes are still on,_
_they will stay on forever as the receiving synth never receives the corresponding Note-Off message._
_This is a classic thing to happen with MIDI, and requires a note panic to be sent which will stop all“_ _”_
_notes. You can force a note panic by pushing Shift + MENU or stopping playback._


21

-----

# Page 22

## **Mapping**

Once you have set up your devices, we can start mapping the controls! But first things first… There are two main categories of MIDI receiving

devices that you should be aware of.

#### **Devices with fixed mapping table synths, grooveboxes( )**

Most synths and grooveboxes offer a MIDI mapping table in their manual, which is a list of device parameters e.g. volume, cutoff frequency, etc. ( )

that can be remotely controlled via MIDI. The device expects a specific MIDI message e.g. CC message #13 value range 0-127 per parameter and ( )

you need to configure your MIDI sender Drop to transmit exactly that message in order to control that parameter. ( )


_For devices with a fixed MIDI table, it is best practice to start off with an empty project and populate Drop s controls bit by bit. ’_


This kind of mapping can be quite a bit of work. Therefore, Drop offers different ways to help you get through this process as fast as possible.


  - Look up the MIDI mapping table of your synth and manually enter the MIDI message type, numbers, value ranges on Drop.


  - Your device can send MIDI out when you turn its knobs? Great! You can use MIDI learn on Drop which significantly speeds up the mapping

process. First, ensure your device actually sends MIDI data often, this must be enabled in its settings and connect the device s MIDI out to ( ) ’

Drop s MIDI in, so that communication works in both directions. Also ensure that in Drop s Device settings, you enabled and selected the ’ ’

corresponding MIDI input. On Drop, you can go to _PLAY > Monitor_ to check and verify the incoming and outgoing messages.


  - If your device is listed in the Pencil Research MIDI database on Drop s SD-card, you can select the device parameter from the database. This is ’

a convenient alternative to look up the parameter name in the device s manual and entering the MIDI control parameters by hand on Drop.’


_Example of a typical MIDI mapping table, taken from the_
_Elektron Rytm MK1 manual_


22

-----

# Page 23

#### **Devices with MIDI learn DAW, workstations( )**

Software DAWs e.g. Ableton Live or hardware workstations e.g. Akai MPC series have so many parameters that it is just too many for a fixed ( ) ( )

mapping table. Instead, they offer a MIDI-Learn function to map parameters to incoming MIDI messages. For the DAW, it doesn t matter which ’

specific MIDI message your controller sends, as long as it is a unique message per control.


Go to Project > DAW Init to quickly apply a default mapping to use Drop with a DAW. This function sets MIDI messages to each of Drop s control ’

elements at once, so that each control element sends out a different MIDI CC or MIDI note message.


_Example of MIDI mapping in a DAW (Ableton Live)_


23

-----

# Page 24

#### **Control element configuration**

element.


its settings from before.


element, its name is displayed on the screen when in PLAY view. You can disable this in the settings.


**Behavior** Describes the physical behavior of the control element. It is different, depending on the

type of control element.






|Rotary knob turn|Precision|Slow turning speed for precise adjustments.|
|---|---|---|
||_Dynamic Pot_|Emulates potentiometer behavior, so that the physical position corresponds to the LED ring. When turning<br>slowly, precise adjustments are possible, though.|
||_Dynamic Fast_|Sensitive to manual movement. When turning slowly, precise adjustments are still possible, though.|
|_Rotary knob push_|_Toggle_|Pressing the rotary knob functions as a separate MIDI button. Each push alternately sends the MIDI min or<br>max value and turns the button on or off.|
||_Temporary_|Pressing the rotary knob functions as a separate MIDI button. When pressed, the MIDI maximum value is sent;<br>when released, the minimum value is sent._ Use this setting with a DAW that sends MIDI feedback to Drop._|
||_Quick Turn_|While pressed, the turning knob speed is 4x faster.|
||_Reset Left/_<br>_Center/Right_|Resets the rotary to its left/center/right position when pressed.|



24

-----

# Page 25

|Mute button|Toggle|Each push alternately sends the MIDI min or max value and turns the button on or off.|
|---|---|---|
||_Temporary_|When pressed, the MIDI maximum value is sent; when released, the minimum value is sent. Use this setting<br>with a DAW that sends MIDI feedback to Drop.|
|_Fader_|_Layer AB dual_|Layer A and B offer their own separate faders, similar to Rotary knobs and Mute buttons.|
||_Layer A only_|The fader of Layer A is in permanent operation, even when on Layer B.<br>This setting is convenient if you do not need a separate fader on Layer B and want permanent access without<br>value-catch to the fader on Layer A.<br>As the faders can not automatically change their physical position, it is required to manually move the fader<br>cap to the underlying virtual position before the fader reacts to manual movement.|


**LED style** Only accessible for rotary knob turn. Choose from different LED ring styles.

|Rotary knob turn|Line from left|For 0-100% unidirectional values. A line of LEDs ranging from 0 to the knob ’s position.|
|---|---|---|
||_Line from center_|For ±100% bidirectional values. A line of LEDs ranging from the top to knob s position on the left or right side.<br>’|
||_Dot_|Universal minimalist setting that only shows an LED dot at the knob s internal position.<br>’|
||_1-25 Steps_|Using the single LEDs of the LED ring to visualize discrete steps.<br>_Example use case:_<br>_Mapping a rotary knob to an oscillator s octave setting. Assume the range goes from_<br>_’_<br>_-2 to +2 octaves, that makes 5 steps (-2, -1, 0, +1, +2) and you get a nice visualization with the 5 Steps setting._|
||_Blank_|The internal value is not shown at all.<br>This LED style is useful in combination with the Relative MIDI output curve. In this mode, the rotary knob<br>“<br>”<br>does not send its internal absolute position, but instead only its relative change if it is turned left or right. Your<br>target application may require relative MIDI data for scrolling through DAW clip scenes or a file list in a<br>browser. In such cases, the internal value of the rotary knob is also irrelevant, so we don t need to show it.<br>’|



25

-----

# Page 26

**Drop Prio** When the control element is used in a snapshot that is fired in Drop mode, you can

select _Normal_ or _PreDrop_ priority. This affects micro timing of MIDI messages in a Drop.


_Normal_ Use this by default. The MIDI output of the control element is sent right after the Drop.


_PreDrop_ The MIDI output of the control element is sent right before the Drop and a second time

right after the Drop.


_Example use case:_


own internal sequencer. You also have a snapshot that re-enables the kick drum.


When firing this snapshot in Drop mode, it musically releases the energy after a peak moment. With

_Normal_ priority, the MIDI message for Mute re-enable is sent an instant after the Drop moment, but it

might be just too late and we might miss out the first kick at the downbeat of the new bar.


By enabling _PreDrop_ priority, the Mute enable message is sent additionally just before the Drop moment, which ensures the kick is enabled at the

downbeat of the next bar.


**CV Out link** Shows, if a control element is mapped to the CV OUT 1 or 2 jack.


You can use the control elements not only to send out MIDI, but also to control the two CV outputs. The CV outputs may be configured as clock

signals, but they can also be used as simple variable linear voltage outputs in MENU > CV Config. There, you can also set the voltage range 0,0 to (

5,0 Volts, 12-bit DAC .)


_The actual linkage of a control element to a CV output is in MENU > CV Config._


**Merge link** Shows, if the control element is linked to any parameter in a Device Merger.


You can use the control elements not only to send out MIDI, but also to manipulate incoming MIDI data that passes through the Device Merger. The

Device Merger offers manipulation of incoming MIDI data before it is redirected to another device e.g. note transposition . The manipulation ( )

parameters can be mapped to Drop s control elements. ’


_The actual linkage of a control element to a Merger parameter is in MENU > Devices._


26

-----

# Page 27

**Feedback by MIDI-In**


Drop s control elements can not only send out MIDI data,’

they can also be remotely controlled by receiving MIDI, also

called Feedback. You can enable MIDI feedback separately

for each control element.


However, if you enable MIDI Feedback, it must always

correspond to one of the slots for MIDI-Output. These are

the requirements:


- The MIDI device linked to the slot must have a MIDI-Input

port set in _MENU > Devices._


- Slot curve should be set to _Linear_, as incoming feedback

messages will also be mapped in a linear way back to the

control element s position.’


- NRPN messages are not supported for MIDI feedback


_Hardware gear usually does not send MIDI feedback when_
_switching programs/presets, as it would most likely cause_
_traffic overload. MIDI feedback is only sent when turning a_
_knob on the device. This raises the question, if MIDI feedback_
_is necessary for hardware gear at all. DAWs however offer_
_good support for MIDI feedback._


27

-----

# Page 28

MIDI Learn
A convenient way to
learn the MIDI
parameters as the
hardware device sends
them. First, verify that
the device sends MIDI
back to Drop as you
move its knobs.


#### **MIDI Output slots**

Each control element offers eight slots for different MIDI Output messages to different devices.


**Slot** Activate the slot.


**Device** Select one of the eight devices configured in _MENU > Devices_


**Channel** The MIDI channel 1-16. Select by device to use the default channel of the device.“ ”


**Msg Type** The MIDI message type. These message types are available:



MIDI Database
If your hardware device
is featured in the
database, this is an
alternative to looking up
MIDI parameters in
device s manual. ’
Select the database file
in the device menu first.













|Note On|Buttons + snapshots<br>only|Mostly used for on/off parameters.|
|---|---|---|
|_CC_|All controls + snapshots|Most commonly used control change message.|
|_CC 14_<br>_CC 14 LSB first_|All controls + snapshots|Two consecutive CC messages for high 14-bit resolution.<br>Typically used for coarse and fine adjustment of a<br>parameter. LSB or MSB first default<br>(<br>)|
|_NRPN_|All controls + snapshots|Some hardware devices offer NRPN access to their<br>parameters, which offers high 14-bit resolution and<br>more parameter numbers than CC. If your device offers<br>both CC and NRPN for the same parameter, CC has<br>lower resolution but is preferred for fast response times.|
|_Pitchbend_|All controls + snapshots|Pitchbend message type, 14-bit resolution.|
|_Aftertouch_|All controls + snapshots|Channel pressure message type.|
|_ProgChg_|Snapshots|Program change message, commonly used to switch<br>presets or patterns, value range 0-127.|
|_Prog + Bank_|Snapshots|Bank select and program change afterwards. Required<br>by some devices that offer more than 128<br>presets/patterns.|


28



Select the mapping slot
Here: Slot 2 out of 8. Slots

1, 2, 4 are set active.

-----

# Page 29

Invert
Switches Min and Max
value, which inverts the
curve on the Y-axis.



**Message #** The message number. If the message type requires it, this may be split into MSB and

LSB (most significant and least significant

byte .)


On the next page, the output range and curve of the slot can be set.


**Max** The upper limit of the output curve.


**Min** The lower limit of the output curve.


Depending on the message type, Min and Max may have different value ranges. For example, Note

On and CC messages range from 0 to 127, while NRPN and CC 14-bit go from 0 to 16383 and

pitchbend from -8192 to +8191. These are simply the values the MIDI protocol offers.


_Shift + Turn the menu encoder to do coarse / fine value adjustments._


**Curve** Only available for faders and rotary knobs.


Select from several output curve types: Linear, Exponential, only the left or right half, On-Off



_Default Linear curve_



Duplicate
Copy-and-paste the

current slot to the

next free one.





29

-----

# Page 30

#### **MIDI Learn**

Drop can listen to incoming MIDI messages, pick a message, and apply its parameters to a control element as outgoing MIDI message.

This is how it works: Some hardware devices can send MIDI on their output port when turning a potentiometer or changing a parameter. Usually, this

is the same message type, channel and number which the device also expects as input to control the parameter.


First, _make sure the connected device actually sends MIDI output for parameter changes_ . Many devices require this option to be activated in their

settings first. Also, _connect the MIDI output of your hardware device to one of Drop s MIDI inputs’_, or use USB instead.


When in _MENU > Mapping_, enter the slot you want to map and push the _Learn button_ on the top right.

Now, Drop shows live recording of incoming MIDI messages. _On the device, move the parameter you want to map_, and Drop should receive the

corresponding MIDI messages. Use the lower two buttons to select another MIDI input port if necessary.


Press the upper right button to _stop live recording_, then scroll through the history list and _select the message you want to map_ by pushing the menu

encoder.


Usually, it is the newest message top position, but( )

sometimes a device parameter sends several

messages at once, so you can select the right

message from the history list.


If you only need your device s incoming MIDI’

messages for MIDI Learn, you can remove the cable

again after mapping.


_Note: Messages that can not be assigned to the_

_control element are shown in red. E.g. Note messages_

_can not be assigned to rotary encoders and faders._


30

-----

# Page 31

#### **MIDI CC & NRPN database**

Drop ships with an open-source MIDI database* on board, which contains the MIDI mapping tables of many popular devices.


First, go to _MENU > Devices > Database_ and scroll through the list to see if your hardware device is included. If you found it, select the file to assign

it to the device.


Then, enter _MENU > Mapping_, turn, push, move the control element to map and scroll to the Slot page. Now, when you select the device with the

newly assigned database file, the green Database button is enabled. Push it to conveniently select the parameter you want to map from a list, „ “



instead of looking up its parameters in the manual.


_MENU > Devices_
Open the database and
look for your target device.


_MENU > Mapping_
Press the Database
button and select the
parameter you want to
assign.


- https://github.com/pencilresearch/midi


31



Back
Select another
parameter from the
database



Apply
Take over and fill the
MIDI parameters
with data



**Name** If enabled, the name of the
whole control element will be set
according to the selected parameter.
It may happen though, that the
parameter s name is too long. Drop ’
crops it into a short name.

**→** **edit** Edit the new short name
manually.

**MIDI-feedb** If set, the control
element s MIDI feedback selection will ’
be set to the newly assigned slot.

**LED style** If set, when mapping a
rotary knob, the LED ring will be set to
_Line from left_ or _Line from center_, based
on information the database entry.



Select the target slot
where to apply the mapping to.

-----

# Page 32

#### **Copy and Move a control element**

be copied to another fader, a rotary knob can only be moved to another rotary knob.


and Mergers also move.


**COPY** Copies the whole control element with its mapping, also to another layer.

Links to CV Out and Mergers stay at the original control.


32

-----

# Page 33

## **Snapshots**

Snapshots are used to _save and recall_ the state of _rotary positions, buttons on-off status and fader positions_ .

A project contains 20 banks with 20 snapshots each.


They can contain _all of Drop s control elements or only a subset’_ . Snapshots enable you to automatically turn multiple control elements at once, which

would not be possible with only two hands. You can also execute multiple snapshots at once and combine them.


In addition, snapshots can also _hold up to 8 MIDI messages_ that are being sent as one-shot messages when the snapshot is executed. These MIDI

messages can also contain _program change_ and _bank select_ messages to tell your devices to switch patterns or load the next preset.


Snapshots can be recalled in Jump mode or in Drop mode, _or both_ at the same time. In Jump mode, snapshots are executed with an adjustable fade

time, that can also be zero for immediate execution. In Drop mode, snapshots are scheduled in advance to be executed at the end of the current

playback cycle, which marks the point where the current 1-32 bar pattern ends and the next one begins. In Drop mode, execution takes place with

no fade time, and also automatically ends ongoing Jumps, resulting in a timed and immediate change in music.


With this behavior, the combination of Jumps and Drops makes it easy to create a _buildup followed by a sudden drop_ in music, by virtually turning

parameters on up to eight hardware devices.


You can even go one step further and prepare sequences of Jumps and Drops in advance, using CHAIN mode. That way, you can prepare a song

arrangement using snapshots. Per project, there are 20 chains available with up to 64 snapshots each.


It is up to you as a musician, if and to what extent you want to use snapshots in your performance. _Here are some ideas_ :


  - Safety net when improvising and trying something risky .“ ”


  - Saving the hey, this sounds cool moment for later, while jamming around.“ ”


  - One-button solution for specific parameters, e.g. resetting effects across all devices.


  - One-button solution to load presets and switch patterns on multiple devices at once.


  - A third hand that can take care of a sub-task, so you can focus on the fun part .“ ” “ ”


  - Step through your song arrangements manually, one snapshot after another, or fully automated.


33

-----

# Page 34

#### **Save snapshots**

To save the current state of the control elements, _push the SAVE button_ to enter save view. The control

elements will turn red or green, which indicates if the element will be saved into the snapshot or not.


GREEN: Selected, will be saved into snapshot. RED: Deselected, will not be saved into snapshot.


You can now change the state for each control element individually by turning, pushing or moving it.


To save the snapshot, simply press a snapshot button and you are done.

Selection groups help you to get the desired selection of control elements faster.


**GROUP**
The current selection is automatically stored inside one of eight groups. Use the two buttons to select
another group and make a new selection of elements. When you go back to the previous group, the
previous selection is also still there.
This is a fast way to switch between the selections you commonly use in your setup.



**Color**

by turning the menu encoder.


**Values mode**
Instead of selecting and
deselecting control elements,
operation changes their value as
usual.


**Select mode**

Select mode, described above.


34



**SAVE**
Push the snapshot

with the current
selection of control
elements.



Rotary knob
Turn right: select, LEDs turn green
Turn left: deselect, LEDs turn red

Rotary push and Round buttons
Push: toggle selection status

Fader
Move up: select, LEDs turn green
Move down: deselect, LEDs turn red


_Example: Selected, deselected and_
_inactive controls which do not have a_
_mapping yet._

-----

# Page 35

#### **Edit snapshots**

Edit existing snapshots. You can also enter MIDI messages that are sent as one-shots when the snapshot is executed.



**Move**
Move the selected snapshot to another button.
_Caution: Existing snapshots will be overwritten!_

**Color**
Change the color of the snapshot
by turning the menu encoder.

**Name**
Set a name for the snapshot, to
remember or in CHAIN mode.

**Values mode**
Instead of selecting and
deselecting control elements,
operation changes their value as
usual.

**Select mode**
By default, the EDIT view starts in
Select mode, described on the
previous page.


COPY snapshots



**MIDI message slots**
Activate up to 8 slots for different MIDI messages to be sent when the
snapshot is executed. Besides all other
common MIDI message types,
you can also enable _Program_
_Change and Bank Select_
messages here. If you send
them to a device running its
own internal sequencer, you
may want to set a Pre-Drop
delay in _MENU > Devices_,
so that the device receives
the message just before the
pattern ends. Entering a MIDI
message here is _similar to_
_MENU > Mapping_, except there
are no curves. Instead, a _fixed message value is sent every time_ .
Note On messages are immediately followed by a Note Off message.



Press _Shift + copy_ to select a source snapshot, then press the target snapshot. Press _Shift + copy_ again

to exit copy mode. Before pressing the target snapshot, you can select options for copying:


**Also copy MIDI slots** When active, also the MIDI message slots are copied.

**Create Auto name** When active, the target snapshot will get a default auto name.

Otherwise, the source name will be copied, too.


35

-----

# Page 36

#### **Jump mode**



In the PLAY menu, you can set snapshot
quantization in JUMP mode.
The quantization also applies if you
trigger the snapshot remotely via MIDI.


In _MENU > Settings > Latest snapshot_ you
can enable, that the last snapshot
pressed keeps blinking softly. This helps
to remember when performing, how you
got where you currently are.
The blinking can be stopped by stopping
playback or by pressing the JUMP or
DROP button again, depending in which
mode you currently are.



**Fade time**
**potentiometer**

snapshot.

jump.

_Settings_





Jump to finish.

in progress.


36

-----

# Page 37

#### **Drop mode**

Drop.


If enabled in
_MENU > Settings_,


for the next cycle.


**DROP scheduled**

at the top.

happen instantly.


37



**DROP and JUMP simultaneously**
A snapshot is scheduled for a
Drop at the end of the cycle, while
another snapshot is currently
fading in Jump mode.
_A Drop will end the Jump_
automatically.
That way, you can _create a buildup_
_with a Jump until the Drop_
changes the whole set at once.


**Jump fade time end**

advance.

-----

# Page 38

#### **Manual fade mode**

You can also use the small potentiometer to manually fade from the

current state to another snapshot or a combination of snapshots.


First, hold the Jump button while pressing the snapshot you want to


in _SETTINGS > multiple Jumps_ . Also here, if there is an overlap


pressed count.


Then, you need to move the potentiometer all to the left in order to

start the manual fade. As soon, as the leftmost position is reached,

you can fade towards the selected snapshots by turning the

potentiometer to the right. In the rightmost position, the snapshots

are faded in at 100%.


Button presses and MIDI data from the snapshot itself like program(

change messages, etc. are sent out as soon as the potentiometer)

leaves the 0% position. If you turn the potentiometer back to 0%,

only button values may change again, but snapshot-contained MIDI

messages will not be sent out again.


There are several ways to leave manual fade mode:


Push one of the bottom circle buttons to exit and leave the state as

it is or leave and reset to the original state we had before the fade.

Also, pushing the Jump button again stops the manual fade and

leaves the state as it is.


You can also schedule a Drop while the manual fade is in operation.

A Drop will also leave the manual fade.


38

-----

# Page 39

## **Chain**

#### **Workflow**

The chain function allows you to _prepare and play back a series of_

_snapshots in a specific order_ . For example, if you are performing a

song that follows a fixed arrangement, you can set the snapshot

sequence here and then simply start the chain on stage instead of

firing off the snapshots manually.


The chain function offers a high degree of automation. Automating

an entire performance may not be the purpose of a live set, but you

can, for example, automate tedious parts of your performance and

outsource them to Drop so that you have your hands free for other,

more creative tasks.


There are a total of 20 chains, just as there are 20 snapshot banks. If

your performance is song-based, it can make sense to use one bank

and one chain per song. In _MENU > Settings_, there are two switches

to link banks to chains bidirectionally. Switching bank 1-20 may

automatically select the corresponding chain 1-20, and vice versa.


In chain mode, _snapshots are always fired exclusively_ . You can not

trigger multiple snapshots at the same time with a single chain entry.

However, _you can still manually fire snapshots during chain playback_

without stopping the chain.


Each chain can be up to 64 snapshots long. The snapshots in a chain

can belong to any of the 20 banks.


39



**Chain mode**

The snapshot buttons continue to work
normally during chain playback.
The SINGLE and REPEAT buttons are
blinking while a chain is playing.
Push _Shift + SINGLE_ or _Shift + REPEAT to_
_stop chain playback_, no matter in which
menu.


**Select**
Switch to a different chain 1-20. Switching
the chain will stop the currently active
chain. In _MENU > Settings_, there is a switch
to link chains and snapshot banks in both
directions, so that selecting a bank also
changes the chain and vice versa.


**Name**
You can give each chain its own name. E.g.
this could be the name of a song.


**Add +**
Push this button to add a snapshot to the
chain. Use the encoder to select the insert
position. Select Pause to insert a line “ ”
without firing a snapshot.


**Del -**
Push this button to delete the currently
selected entry.

-----

# Page 40

**Circle buttons**
LED feedback is shown as usual red or blue

when snapshots are executed in Drop or

Jump mode.


**Playback marker**


After that, the cycle length will be 8 bars.


**Color**
Red = Drop, Blue = Jump, Grey = Pause



**Start Stop**
Use the upper left circle button to start chain playback at the current cursor position. You can also
start a chain in the middle instead of at the beginning.

**Snapshot name**
Use _Shift + edit_ to give
snapshots a name.


**Cycle length**
_“Stop“_
Do not continue chain
playback after this
snapshot s execution.’

_“- ”_
Leave the cycle length as
it is.

_“1-32 Bars ”_
Set the cycle length to
the specified length after
the snapshot was
executed.



For each snapshot, you can select Jump or Drop mode, as well as the fade time and the number of beats per cycle that follow. A progress bar and

LED feedback provide information about the playback position. Note: Entry GO 1 is a Drop and has set its length to ---, followed by BUILDUP “ ” “ ” “ ”

which is a Jump.


Note: When the _Drop length is set to -, a following Jump will start right after the Drop“ ”_ has been executed.


40

-----

# Page 41

specified length is also the fade
time.




#### **Link Chains and Banks**





If you want to build your performance song by song and use one chain per song, it may also be useful to link snapshot banks and chains. For that

reason, there are 20 snapshot banks and 20 chains available per project.


In _MENU > Settings_, you will find two options for linking.


**Chain to Bank** When active, selecting another chain in chain view will automatically select the corresponding snapshot bank.


**Bank to Chain** When active, switching banks using the BANK button will automatically select the corresponding chain.


_Note: When switching chains, playback of the current chain is stopped._


41

-----

# Page 42

## **Clock**

Drop s timing can be synchronized with other devices using MIDI clock or CV clock signals.’


**Source - CV clock** Drop syncs its own tempo to an incoming CV clock.
CV1 is always the clock signal, while CV2 can be used as a separate
trigger or gate signal. Clock speed and CV2 s usage must be set in ’
_MENU > CV In/Out_ .


**MIDI clock device**
Select the MIDI clock source device.


42



**Nudge BPM**
Use the upper blue buttons to temporarily speed
the tempo up or down. Only available if running on


When Drop sends MIDI clock to multiple other
devices, they may still get out of sync due to
different tempo change algorithms or accidentally
pushing the stop button on one device.
ReSync _quickly sends a Stop + Start_ message to all
MIDI clock outputs at the beginning of the next bar,
which is _usually inaudible and sets everything back_
_in sync_ .

-----

# Page 43

#### **Clock delays**

Use clock delays to counteract different audio processing latencies of your connected gear.
If an instrument uses any kind of digital signal processing, it inevitably needs a little bit of time, also
called latency, from when e.g. a MIDI note message is received until the sound appears at the device s’
audio output. Manufacturers try to keep the latency as low as possible and if you play only one
instrument alone, you may not even notice. However, if you are running multiple devices in parallel,
different latencies may become audible.


**Left  clock delay in milliseconds–**
This delay time is independent of the tempo and _counteracts audio processing time_ .


**Right  clock delay in MIDI clocks–**
Only use this if you know what you are doing! Some DAWs and sequencers may not count the first
MIDI clock packet, or also count the start message as a MIDI clock. Use this, to counteract such
misbehavior.


Start off with all clock delays set to 0. Make sure, every device receives MIDI clock by Drop. Start playback and try to find out by ear if a device is
constantly playing a little bit ahead or after. It gets a lot easier if your devices play the same musical pattern, e.g. a short plucky sound every quarter.
If it is unclear, choose a reference device the one you expect to have the largest latency, let it play a pattern and unmute other devices one by one.( )
In our experience, hardware gear has very low latency in the 1-3 ms range. DAWs, however, can have significant and varying delay times, depending
on CPU load and audio settings.
_Positive delay times are preferred._ You can also apply _negative delay_ values. In this case, the clock will speed up a little bit after playback starts, until
the target pre-delay has been reached. So, playback will only be in sync after a short amount of time. For that reason, it is recommended to use
negative clock delays _only when necessary_ .


43

-----

# Page 44

**Send MIDI clock while stopped**
If this option is activated, Drop will send MIDI clock signal also while playback is stopped. This option
should be enabled unless it disturbs a connected device. Sending MIDI clock while being stopped is
typical groovebox behavior. It constantly updates the tempo information on the receiving device, and if
the receiving device is smart enough, you get better timing precision right after starting the clock.

#### **Clock send enable**

On the next page, you can enable MIDI clock, transport and song position pointer output for every
physical port separately.


The default setting with the _two left checkmarks enabled is the right choice_ for most grooveboxes,
synths and DAWs send MIDI clock and transport .( )


**Left  MIDI Clock–**
Sends clock messages, which contain tempo information.


**Middle MIDI Transport–**
Sends start and stop messages, telling the connected device so start/stop playback.


**Right Song position pointer–**


**Clock to Sub-Ports of USB1/2**
MIDI via USB offers up to 16 virtual cables sub-ports .( )
Some MIDI USB devices may offer more than one subport, but need to receive MIDI clock only on a specific
one. Therefore, you can select to which sub-ports clock,
transport and song position pointer messages are being
sent and to which ones not.

-----

# Page 45

## **CV Config**

Drop has two control voltage CV inputs and outputs each that can be used in different ways. All four CV ports are designed for voltages from 0-5V.( )

The outputs can create continuous voltages with a resolution of 12 bits 4096 steps . The CV inputs can read analog voltages with a resolution of 16 ( )

bits 65536 steps . To interface with a bigger modular system, you may want to use a Midi-to-CV converter( )

module.

#### **CV OUT 1+2**

**Signal**









|Linked Control|Assign any of the control elements directly to the CV output. Turning the<br>corresponding rotary knob or moving the fader linearly changes the CV output<br>value between the Min and Max voltage range.<br>To assign a control element, select the Set Link option. Turn, push, move the<br>control element you want to assign. Use the clear option to remove the link.|
|---|---|
|_24/12/8/4/2_<br>_PPQN Clock_|Clock signal with the specified number of pulses per quarter note PPQN .<br>(<br>)<br>Each pulse has a length of 5 ms.|
|_16th/8th/4th/1Bar_<br>_Clock 50%_|Clock signal with the specified frequency. The PWM duty cycle is 50%.|
|_Start Trig_|Outputs a one-shot trigger when playback starts.|
|_Is Running Gate_|Outputs the Max voltage while playback is running, and Min when stopped.|
|_Cycle Start Trig_|Outputs a trigger at the start of each cycle.|
|_Cycle/Bar Pos CV_|Outputs a linearly rising voltage corresponding to the cycle/bar progress.|
|_Jump Prog._<br>_Rise/Fall_|Outputs a linearly rising/falling voltage corresponding to the progress within<br>an ongoing Jump.|


45

-----

# Page 46

**Min / Max** Set the minimum and maximum output voltage range of the outgoing signals. Clock

signals are _rising edge per default_ . You can turn then into _falling edge by inverting Min and Max_ voltage.

Hold Shift while changing the parameter increases the step size, so the parameter changes faster.

#### **CV IN 1+2**

The CV inputs can either be used for clock signals or to trigger snapshots by external CV and gate signals.







|CV IN1|4PPQN (16th notes)<br>2PPQN (8th notes)|The incoming clock signal may have two different speeds.|
|---|---|---|
|**CV IN2**|_Without function_|With this setting, CV IN2 is ignored. When Drop is synced to<br>CV1 s clock input, playback will start with the first rising edge<br>’<br>at CV IN1 and stop playback when the clock signal stops after<br>a short timeout.|
||_Start Trigger_|Starts the clock when a trigger occurs at CV IN2.|
||_Start/Stop Gate_|Playback keeps running while the signal at CV IN2 is high and<br>stops as soon as the signal goes low.|
|**CV IN1+2**|_Jump Snapshot Trig_<br>_Jump Snapshot Select_||


This option is to connect the CV and gate output of a sequencer

to Drop s CV IN1 and IN2 to select and fire snapshots in Jump’

mode. The voltage at CV IN2 selects the snapshot, with the

voltage range from 0 to 5V is mapped to the 20 snapshots of the

current bank. When there is a rising edge at CV IN1, the

snapshot will be fired in Jump mode and the potentiometer

determines the fade time.


46

-----

# Page 47

## **Remote**

Drop can also be remotely controlled via MIDI. You can link two or more Drops to jam with your band members and keep the same timing, or

expand the amount of available controls and connections, or use another MIDI device to control Drop s functions and embed it into a bigger setup.’

#### **Jump by MIDI notes**

Fire _snapshots from an external MIDI source_ like a sequencer or a keyboard. Only the 4x5 _snapshots of the current bank_ are affected. Snapshots are

fired in Jump mode, the fade potentiometer determines the fade time, and _PLAY > Quantization_ is used for timing.

|Mode|Col2|
|---|---|
|_Off_|Ignore notes.|
|_By Pitch_|The note number pitch determines chooses the snapshot. The Base Note and the<br>(<br>)<br>19 notes above are taken into account and are mapped to one snapshot each.<br>Notes exceeding that range are cropped and treated like the base note or the<br>highest note which is base note + 20. The base note corresponds to the lower left<br>snapshot and the highest note to the upper right snapshot. If the incoming note<br>does not exactly match a snapshot, the closest snapshot is selected.<br>_Use this mode to connect a programmable MIDI sequencer._|
|_Velo 1-20_|Only the base note is taken into account, other notes do not fire a snapshot. Choose<br>the snapshot according to velocity values 1-20. If the incoming note has a velocity<br>larger than 20, it is cropped and treated as velocity = 20. Also here, velocity = 0<br>corresponds to the lower left and velocity >= 20 to the upper right snapshot.<br>_Use this mode to connect a programmable MIDI sequencer._|
|_Velo 1-127_|Only the base note is taken into account, other notes do not fire a snapshot. The<br>snapshot is selected using the velocity value, where the full velocity range 1-127 is<br>spread evenly across snapshots.<br>_Use this mode to connect a MIDI trigger pad played by hand._|



47

-----

# Page 48

#### **Receive and Send**

Many of Drop s functions can be remotely accessed via MIDI CC messages. There are different levels of depth’

tailored to real-world use cases that enable remote control.


You can use these settings to _link two or more Drop units_ to play along.


On both Drops, you need to add a Device for the other connected Drop and select a MIDI out and a MIDI

input port. In MENU > Settings, you can enable Receive and Send independently and thereby have a master


on both Drops. also make sure, that for each data direction, the MIDI channel is identical.


You still need to _setup MIDI clock separately_ .


**Jam Mode**


The intended use case for this mode is _playing a live set with a partner_ . Both have their own independent

setup with their own Drop as the master controller. Jam mode ensures that the Drop moment and the cycle

playback position are in sync across both setups. Besides that, each of you can play their own setup

independently.


**Dual Mode**


Drop, the receiver Drop will also switch the bank. Also, all snapshot related settings like quantization,

exclusiveness, or the fade time potentiometer are overwritten on the receiver Drop by the sender Drop.


**Full Mode**


_schedules and fires the same snapshot on the receiver_ Drop.


48

-----

# Page 49

**MIDI table**



|CC number|Description|Jam|Dual|Full|
|---|---|---|---|---|
|#11-30|Fire snapshot in_Jump_ mode.<br>CC number # Selects the snapshot: 1 = bottom left, 20 = top right.<br>Value 0<br>Do nothing.<br>Value 1-20<br>_Emulate button push_. Fires a snapshot or removes it from the selection if it is already in execution.<br>Value selects bank number 1-20.<br>Value 21-40<br>_Starts a manual fade_ with the selected snapshot. Value selects bank number 1-20.<br>Value 41-60<br>_Force fire snapshot_ in Jump mode, fire again if already in execution. Value selects bank number.<br>Value 61<br>Same as value  1-20, but on_currently active bank_.<br>Value 62<br>Same as value 21-40, but on_currently active bank_.<br>Value 63<br>Same as value 41-60, but on_currently active bank_.<br>Value 64<br>Do nothing.<br>Value 65-84<br>Same as value  1-20, but allows only one snapshot_exclusively_.<br>Value 85-104<br>Same as value 21-40, but allows only one snapshot_exclusively_.<br>Value 105-124 Same as value 41-60, but allows only one snapshot_exclusively_.<br>Value 125<br>Same as value  1-20, but allows only one snapshot_exclusively_ and on_currently active bank_.<br>Value 126<br>Same as value 41-60, but allows only one snapshot_exclusively_ and on_currently active bank_.<br>Value 127<br>Same as value 61-80, but allows only one snapshot_exclusively_ and on_currently active bank_.|-|-|Yes|
|#31|Stop all ongoing Jumps.<br>Value 0<br>Do nothing<br>Value 1<br>Stop all Jumps. If in manual fade mode, Exit & Reset.<br>Value 2~127<br>Stop all Jumps. If in manual fade mode, Exit.|-|-|Yes|


49




|Col1|Value 0|Do nothing.|
|---|---|---|
||Value 1-20|_Emulate button push_. Fires a snapshot or removes it from the selection if it is already in execution.<br>Value selects bank number 1-20.|
||Value 21-40|_Starts a manual fade_ with the selected snapshot. Value selects bank number 1-20.|
||Value 41-60|_Force fire snapshot_ in Jump mode, fire again if already in execution. Value selects bank number.|
||Value 61|Same as value   1-20, but on_currently active bank_.|
||Value 62|Same as value 21-40, but on_currently active bank_.|
||Value 63|Same as value 41-60, but on_currently active bank_.|
||Value 64|Do nothing.|
||Value 65-84|Same as value   1-20, but allows only one snapshot_exclusively_.|
||Value 85-104|Same as value 21-40, but allows only one snapshot_exclusively_.|
||Value 105-124|Same as value 41-60, but allows only one snapshot_exclusively_.|
||Value 125|Same as value   1-20, but allows only one snapshot_exclusively_ and on_currently active bank_.|
||Value 126|Same as value 41-60, but allows only one snapshot_exclusively_ and on_currently active bank_.|
||Value 127|Same as value 61-80, but allows only one snapshot_exclusively_ and on_currently active bank_.|


|Value 0|Do nothing|
|---|---|
|Value 1|Stop all Jumps. If in manual fade mode, Exit & Reset.|
|Value 2~127|Stop all Jumps. If in manual fade mode, Exit.|

-----

# Page 50

|CC number|Description|Jam|Dual|Full|
|---|---|---|---|---|
|#41-60|Schedule snapshot in_Drop_ mode.<br>CC number # Selects the snapshot: 1 = bottom left, 20 = top right.<br>Value 0<br>Do nothing.<br>Value 1-20<br>_Emulate button push_. Schedules a snapshot or removes it from the selection if already scheduled.<br>Value selects bank number 1-20.<br>Value 21-40<br>_Remove snapshot from ongoing Drop_ and do nothing if not selected for Drop yet.<br>Value selects bank number 1-20.<br>Value 41-60<br>_Force schedule snapshot_ in Drop mode.<br>Value selects bank number 1-20.<br>Value 61<br>Same as value  1-20, but on_currently active bank_.<br>Value 62<br>Same as value 21-40, but on_currently active bank_.<br>Value 63<br>Same as value 41-60, but on_currently active bank_.<br>Value 64<br>Do nothing.<br>Value 65-84<br>Same as value  1-20, but allows only one snapshot_exclusively_.<br>Value 85-104<br>Same as value 21-40, but allows only one snapshot_exclusively_.<br>Value 105-124 Same as value 41-60, but allows only one snapshot_exclusively_.<br>Value 125<br>Same as value  1-20, but allows only one snapshot_exclusively_ and on_currently active bank_.<br>Value 126<br>Same as value 41-60, but allows only one snapshot_exclusively_ and on_currently active bank_.<br>Value 127<br>Same as value 61-80, but allows only one snapshot_exclusively_ and on_currently active bank_.|-|-|Yes|
|#61|Stop all ongoing Drops.<br>Value 0<br>Do nothing<br>Value 1~127<br>Un-schedule Drop.|-|-|Yes|


50




|Col1|Value 0|Do nothing.|
|---|---|---|
||Value 1-20|_Emulate button push_. Schedules a snapshot or removes it from the selection if already scheduled.<br>Value selects bank number 1-20.|
||Value 21-40|_Remove snapshot from ongoing Drop_ and do nothing if not selected for Drop yet.<br>Value selects bank number 1-20.|
||Value 41-60|_Force schedule snapshot_ in Drop mode.<br>Value selects bank number 1-20.|
||Value 61|Same as value   1-20, but on_currently active bank_.|
||Value 62|Same as value 21-40, but on_currently active bank_.|
||Value 63|Same as value 41-60, but on_currently active bank_.|
||Value 64|Do nothing.|
||Value 65-84|Same as value   1-20, but allows only one snapshot_exclusively_.|
||Value 85-104|Same as value 21-40, but allows only one snapshot_exclusively_.|
||Value 105-124|Same as value 41-60, but allows only one snapshot_exclusively_.|
||Value 125|Same as value   1-20, but allows only one snapshot_exclusively_ and on_currently active bank_.|
||Value 126|Same as value 41-60, but allows only one snapshot_exclusively_ and on_currently active bank_.|
||Value 127|Same as value 61-80, but allows only one snapshot_exclusively_ and on_currently active bank_.|


|Value 0|Do nothing|
|---|---|
|Value 1~127|Un-schedule Drop.|

-----

# Page 51

|CC number|Description|Col3|Col4|Col5|Jam|Dual|Full|
|---|---|---|---|---|---|---|---|
|#1|_MENU > Settings > Multiple Jumps_<br>Value 0<br>Allowed<br>Value 1~127<br>Not allowed|_MENU > Settings > Multiple Jumps_<br>Value 0<br>Allowed<br>Value 1~127<br>Not allowed|_MENU > Settings > Multiple Jumps_<br>Value 0<br>Allowed<br>Value 1~127<br>Not allowed|_MENU > Settings > Multiple Jumps_<br>Value 0<br>Allowed<br>Value 1~127<br>Not allowed|-|Yes|Yes|
|#2|_MENU > Settings > Multiple Drops_<br>Value 0<br>Allowed<br>Value 1~127<br>Not allowed|_MENU > Settings > Multiple Drops_<br>Value 0<br>Allowed<br>Value 1~127<br>Not allowed|_MENU > Settings > Multiple Drops_<br>Value 0<br>Allowed<br>Value 1~127<br>Not allowed|_MENU > Settings > Multiple Drops_<br>Value 0<br>Allowed<br>Value 1~127<br>Not allowed|-|Yes|Yes|
|#3|Set fade time, overrides potentiometer. Potentiometer LED starts to blink, indicating that you need to catch the<br>value to get it back into operation.<br>Value 0-127<br>Fade time 0-100%|Set fade time, overrides potentiometer. Potentiometer LED starts to blink, indicating that you need to catch the<br>value to get it back into operation.<br>Value 0-127<br>Fade time 0-100%|Set fade time, overrides potentiometer. Potentiometer LED starts to blink, indicating that you need to catch the<br>value to get it back into operation.<br>Value 0-127<br>Fade time 0-100%|Set fade time, overrides potentiometer. Potentiometer LED starts to blink, indicating that you need to catch the<br>value to get it back into operation.<br>Value 0-127<br>Fade time 0-100%|-|Yes|Yes|
|#4|_MENU > Settings > Jump time_. Sets the maximum fade time of a Jump.<br>Value 0<br>One full cycle<br>Value 1-6<br>1: 10 seconds; 2: 20 seconds; 3: 30 seconds; 4: 40 seconds; 5: 50 seconds; 6~127: 60 seconds;|_MENU > Settings > Jump time_. Sets the maximum fade time of a Jump.<br>Value 0<br>One full cycle<br>Value 1-6<br>1: 10 seconds; 2: 20 seconds; 3: 30 seconds; 4: 40 seconds; 5: 50 seconds; 6~127: 60 seconds;|_MENU > Settings > Jump time_. Sets the maximum fade time of a Jump.<br>Value 0<br>One full cycle<br>Value 1-6<br>1: 10 seconds; 2: 20 seconds; 3: 30 seconds; 4: 40 seconds; 5: 50 seconds; 6~127: 60 seconds;|_MENU > Settings > Jump time_. Sets the maximum fade time of a Jump.<br>Value 0<br>One full cycle<br>Value 1-6<br>1: 10 seconds; 2: 20 seconds; 3: 30 seconds; 4: 40 seconds; 5: 50 seconds; 6~127: 60 seconds;|-|Yes|Yes|
|#5|_PLAY > Length_. Sets the number of bars per cycle.|_PLAY > Length_. Sets the number of bars per cycle.|_PLAY > Length_. Sets the number of bars per cycle.|_PLAY > Length_. Sets the number of bars per cycle.|Yes|Yes|Yes|
|#5||Value 0|Do nothing|||||
|#5||Value 1-32|Nr of bars. If the chosen nr of bars is not allowed, the next lower number will be selected.|Nr of bars. If the chosen nr of bars is not allowed, the next lower number will be selected.|Nr of bars. If the chosen nr of bars is not allowed, the next lower number will be selected.|Nr of bars. If the chosen nr of bars is not allowed, the next lower number will be selected.|Nr of bars. If the chosen nr of bars is not allowed, the next lower number will be selected.|
|#5||||||||
|#33|_PLAY > Quantization,_sets the quantization for Jump.|_PLAY > Quantization,_sets the quantization for Jump.|_PLAY > Quantization,_sets the quantization for Jump.|_PLAY > Quantization,_sets the quantization for Jump.|-|Yes|Yes|
|#33||Value 0-5|0: No quantization; 1: 1/16th; 2: 1/8th; 3: 1/4th; 4: 1/2th; 5~127: 1 bar|||||
|#33||||||||
|#34|_PLAY > Quantization,_ sets the quantization for Beatjump.|_PLAY > Quantization,_ sets the quantization for Beatjump.|_PLAY > Quantization,_ sets the quantization for Beatjump.|_PLAY > Quantization,_ sets the quantization for Beatjump.|Yes|Yes|Yes|
|#34||Value 0|1 bar|||||
|#34||Value 1~127|1/4th note|1/4th note|1/4th note|1/4th note|1/4th note|
|#34||||||||


51




|Value 0|Allowed|
|---|---|
|Value 1~127|Not allowed|


|Value 0|Allowed|
|---|---|
|Value 1~127|Not allowed|


|Value 0|One full cycle|
|---|---|
|Value 1-6|1: 10 seconds; 2: 20 seconds; 3: 30 seconds; 4: 40 seconds; 5: 50 seconds; 6~127: 60 seconds;|

-----

# Page 52

|CC number|Description|Col3|Col4|Col5|Jam|Dual|Full|
|---|---|---|---|---|---|---|---|
|#35|Drop mode|Drop mode|Drop mode|Drop mode|-|Yes|Yes|
|#35||Value 0|Single|||||
|#35||Value 1~127|Repeat|Repeat|Repeat|Repeat|Repeat|
|#35||||||||
|#36|Snapshot BANK select|Snapshot BANK select|Snapshot BANK select|Snapshot BANK select|-|Yes|Yes|
|#36||Value 0|Do nothing|||||
|#36||Value 1-20|Bank number|Bank number|Bank number|Bank number|Bank number|
|#36||||||||
|#37|Chain start and stop|Chain start and stop|Chain start and stop|Chain start and stop|-|Yes|Yes|
|#37||Value 0|Do nothing|||||
|#37||Value 1-20|Chain number, re- start<br>(<br>)|Chain number, re- start<br>(<br>)|Chain number, re- start<br>(<br>)|Chain number, re- start<br>(<br>)|Chain number, re- start<br>(<br>)|
|#37||Value 21|Stop current chain|Stop current chain|Stop current chain|Stop current chain|Stop current chain|
|#37||||||||
|#39|Beatjump Button ID.|Beatjump Button ID.|Beatjump Button ID.|Beatjump Button ID.|Yes|Yes|Yes|
|#39||Value 0|Do nothing|||||
|#39||Value 1-8|Circle button ID|Circle button ID|Circle button ID|Circle button ID|Circle button ID|
|#39||||||||
|#40|Layer select|Layer select|Layer select|Layer select|-|-|Yes|
|#40||Value 0|Activate Layer A|||||
|#40||Value 1~127|Activate Layer B|Activate Layer B|Activate Layer B|Activate Layer B|Activate Layer B|
|#40||||||||


52

-----

# Page 53

## **Grid Mode**

In Grid mode, Drop s button matrix can be used in two ways: As a mini keyboard ’

or a clip launcher with a connected DAW.

#### **Notes Mode**

Use the buttons as a small keyboard to send MIDI notes to a connected synth.


**Device** Select the MIDI device to which the MIDI notes should be sent.


**Channel** Set the MIDI channel on which the device receives the notes.


**Scale** Select the note scale in semitones that can be accessed with the

buttons. Exclude notes that do not match the note scale of your music.


**Velo** The velocity value of the Note-On messages sent out.

Use the four blue buttons to change the root note bottom left button in ( )

octaves or semitones. For better orientation, the root note buttons light up white.


53



**Root note**
**octaves**


**Root note**


**Root note**
**transpose**

-----

# Page 54

#### **DAW Grid Mode**

Use the buttons to launch clips and scenes within your DAW.

Currently, _Bitwig_ and _Ableton Live_ are supported.


track.


**Device**


54

-----

# Page 55

Press and _hold shift_ to access a secondary layer with stop-all-clips button and _scene_

_launch_ buttons.


There are a few default MIDI channel uses when using Grid mode and a DAW:

Channel 1: Rotary encoder and fader, CC messages

Channel 2: Rotary and Track button push, Note messages

Channel 16: Clip launcher buttons and LED feedback, Note messages

#### **Bitwig setup**

Bitwig natively supports Drop as a controller from version 6 on and later. For earlier

versions, please download the file _Drop.bwextension_ from our website and move it

into Bitwig s extension folder ’ ( **[link](https://www.bitwig.com/support/technical_support/how-do-i-add-a-controller-extension-or-script-17/)** . )



**Launch scene**
Launch a scene with the
DAW s timing.’

**Launch scene as DROP**
The red buttons schedule a
scene launch for when the
playback marker reaches
the top and a DROP occurs.

**Stop all clips**
The white button is used
to stop all clips that are
currently playing.



Then in the Bitwig settings, select _Add Controller > Neuzeit Instruments > Drop_ . Optionally, enable Drop as the clock source in Bitwig and make sure,

that Drop also sends clock and transport messages to Bitwig.


The Bitwig extension is built to work with the default _PROJECT > DAW-Init_ settings and also ensures correct LED feedback. Besides selecting Drop as

MIDI input and output, the keyboard MIDI channel for Notes mode must be set in the _Keyboard Channel_ field. When changing the keyboard

channel, the extension must be switched off and on again in order to take it over.


55

-----

# Page 56

#### **Ableton Live setup**

First, you need to _download the remote script files_ from our website and copy them

into the required folder on your computer.


These are the paths in which the downloaded .pyc files need to be placed. You may

need to create an empty folder Remote Scripts first, and also a subfolder Drop, in“ ” “ ”

which the .pyc files go. When done, restart Ableton Live for the script to show up.


_Windows folder:_ \Users\[username]\Documents\Ableton\User Library\Remote Scripts\Drop

_Mac folder:_ Macintosh HD/Users/[username]/Music/Ableton/User Library/Remote Scripts/Drop


This **[link](https://help.ableton.com/hc/en-us/articles/209072009-Installing-third-party-remote-scripts)** on Ableton s website describes the installation of third-party remote scripts in more detail.’



**Control Surface**
Select Drop as the control surface and
activate its Input and Output when Drop is
connected to the computer.
_If Drop does not show up, the script files_
_are not in the right place yet!_


56



**In**
Activate _Remote_ to map Drop s control ’
elements to parameters in Ableton Live.
Activate _Track_ to forward MIDI notes from a
Merger to Live s MIDI tracks.’
Activate _Sync_ if you want to use Drop as the
master clock for Ableton Live.


**Out**
Activate _Remote_ to receive MIDI feedback
from Ableton Live.
Activate _Track_ to receive MIDI notes from
Ableton Live s clips and forward them ’
through Drop s Mergers.’
Activate _Sync_ if you want to use Ableton as
the master clock for Drop.
Set _Song_ as MIDI clock type if you want
Drop to beatjump when jumping in
Ableton s timeline, otherwise use ’ _Pattern_ .

-----

# Page 57

## **Settings**







|Options|Col2|
|---|---|
|**Brightness**|The overall LED and display brightness. Stored globally, not per project.|
|**Default Color**|When activating a new control element, this is the default LED color.|
|**Keyboard layout**|Tells if a connected USB keyboard has QWERTY or QWERTZ layout. Stored globally.|
|**Moving shows**|When moving a control element, the display can also_show the name and/or the value_ of the control element. When playing<br>in bright sunlight, the display s readability is usually better than the LEDs.<br>’<br>Note: You can give each control element its own name, so when coming back to a project after some time it is easier to<br>remember everything. To speed up naming and menu navigation, you can_connect a USB keyboard_ to Drop.|
|**Latest Snapshot**|When executing a snapshot in Jump mode, Drop mode, or by editing it, its button keeps blinking softly. This helps to<br>remember the last action during a performance and to keep track of everything.|
|**MENU but returns**<br>**to root**|In some menus, the MENU button is also used as a back button. When this option is activated, the MENU button takes you<br>back all the way to the root of the menu, otherwise it may only take you back one step. Deactivate this option if you feel<br>familiar with Drop.|
|**Multiple Drops**|When activated, multiple snapshots can be combined to be_scheduled simultaneously as a Drop_. If two snapshots share the<br>same control elements, the snapshot you press last has priority.<br>When deactivated, only one snapshot can be_exclusively_ scheduled as a Drop.|
|**Multiple Jumps**|When activated, multiple_snapshots can be combined in a Jump_. If two snapshots share the same control elements, the<br>snapshot you press last has priority. Adding a snapshot to an ongoing Jump will re-start the fade time. When a Jump is<br>already fading, you can also deselect snapshots from the fade one by one.<br>When deactivated, only one snapshot can be_exclusively_ be used for a Jump at a time.|


57

-----

# Page 58

|Jump time|The maximum Jump time when the fade time potentiometer is turned fully to the right. In the leftmost position, the fade time<br>is always 0, resulting in an instant Jump.<br>1 cycle max: One full cycle, no matter how many bars or which tempo is currently set.<br>10...60 seconds: Fixed time, independent from tempo and number of bars per cycle.|
|---|---|
|**Send all after load**|When loading a project, all control element s current MIDI values and Remote TX messages are sent as one-shots.<br>’<br>Note: Press_Shift + Play to force-send all MIDI and Remote TX_ messages any time.|
|**Chain to Bank**|In chain mode, selecting a different chain 1-20 also changes the snapshot bank 1-20.|
|**Bank to Chain**|When selecting a different snapshot bank 1-20, the snapshot chain with the same number 1-20 is automatically selected.<br>Note: Switching to a different chain will always stop playback of the currently active chain.<br>Note: Bank<br> Chain linkage is especially useful, when you arrange your set to perform up to 20 songs, using one chain and<br>↔<br>one snapshot bank per song.|
|**USB1/2 port mode**|Host + Device: When connected to another USB device, Drop auto detects if its USB port 1 or 2 should take host or device<br>role. In Host mode, Drop also applies 5V power to the connected device.<br>Device Only: Drop s USB port 1 or 2 is forced to stay in device role and does not supply power to the connected device.<br>’|

#### **Test mode**

Push the Test button to enter a test mode in which you can verify that Drop s hardware works correctly. Turn the encoder to switch pages. Test “ ” ’

mode allows you to see if all LEDs work as expected, lets you test all push buttons, encoders and faders and lets you test CV and TRS inputs and

outputs.


_Note: In test mode, CV and MIDI will not work. Test signals (0-5V ramp) and test messages are sent over all CV and TRS outputs which are not valid_

_MIDI data._


58

-----

# Page 59

## **Project**

#### **Management**

In MENU > Project you can save, recall, create, rename and delete projects. Also, there are options to

initialize a new project for either DAW-only use or hardware device use, as well as a purge function to help

you clean up a cluttered project.


Projects are stored on Drop s Micro SD card in the /Projects folder. The file format is .json JavaScript object’ (

notation which means that it is a human-readable format that is open for future editing in a web)

environment.


You can also navigate subfolders inside the /Projects directory if you need to, but you need to create them

on the SD card using your computer.

|Save Project|Store the current project. Push the NEW+ button to create a new project or select an existing project name. Leave<br>the name as it is to overwrite the existing file or change the name to save a second version of the project.|
|---|---|
|**Load Project**|Select and load a project from the file system. Use the NEW+ button to start off with an empty project same as<br>(<br>Clean Init .<br>“<br>”)|
|**Rename Project**|Give an existing project a different name|
|**Delete Project**|Delete the selected project file from the SD card permanently. There is a safety step before the actual delete.|



59

-----

# Page 60

|Purge Project|Helps you clean up a cluttered project. There are several tasks available that can be turned on or off separately<br>before proceeding. The purge function does not change the functionality of your project, it simply cleans up<br>unused parts and re-sorts slots.|Col3|
|---|---|---|
|**Purge Project**|_Reset unused devices_|The parameters of devices that are not turned ON in_MENU > Devices_, will be reset to t<br>states. So if you turned on a device, changed some parameters, then turned it off again<br>changed parameters still persist in case you want to re-enable the device later. This fun<br>the parameters of all devices that are not enabled.|
|**Purge Project**|_Re-sort device order_|If there are gaps between active devices, active devices with higher slot numbers will b<br>lower slots, so that gaps are closed. E.g. if only devices 1, 3, 4, 7 are activated, they will<br>slots 1, 2, 3, 4.|
|**Purge Project**|_Remove inactive controls_|Checks for each control element if it is active but does not have any MIDI mapping or a<br>link CV out or Merger assignment . If the control element is not actively used, it will be<br>(<br>)<br>and reset to its initial state.<br>Also snapshots are checked. If a snapshot is active but does not contain any data and d<br>MIDI assigned, it will be turned off and reset to its initial state.|
|**Purge Project**|_Reset unused slots_|Goes over all MIDI slots of all control elements and snapshots. If a slot is not used or h<br>where the corresponding device is not active, the slot will be reset to its initial state.|
|**Purge Project**|_Re-sort slots_|Goes over all MIDI slots of all control elements and snapshots. If there are gaps betwee<br>slots with higher numbers will be moved to lower slots, so that gaps are closed.|
|**Purge Project**|||


60

-----

# Page 61

|Device|Defines the device slot ID used for the DAW device.|
|---|---|
|**Port**|Select the physical port for the DAW. If choosing TRS, make sure to connect Input and Output.|
|**Color Start**|Sets the color of the first line or row or all control elements, depending on color mode.|
|**Color Mode**|Set a color scheme, e.g. Per Line, Per Column or Same Color.|
|**Quickturn**|Active:    The push function of all rotary knobs is set to Quickturn, no MIDI out.<br>Inactive:  Rotary push acts as a MIDI push button.|

-----

# Page 62

#### **Hardware Initialization**

**Clean Init** Use this as a starting point for a setup with other hardware devices.


With this initialization function, all control elements and devices are deactivated

and reset, so Drop s control surface will be dark at first. ’


This is a clean starting point for a setup with _devices with a MIDI mapping table_ .

This applies to most synths and grooveboxes, so the device expects a specific

message for each parameter and all mapping is done in Drop. You should only

activate the control elements you actually need and set up the right MIDI

messages the receiving device expects.


If you have a _MIDI device that has its own internal MIDI learn function_, you should

still start off with an empty project. Then, just activate the needed controls and a

MIDI slot and stick with the default unique message type and message number.

Then, use the receiver s learn function.’


_Starting with a blank project is usually the best way to create a clean and_
_reactive setup with no MIDI message overhead._


62

-----

# Page 63

#### **Default mapping**

This is the default mapping applied to each control element when using the functions Purge Project, Create New, DAW Init or Clean Init. Except from

DAW Init, the control elements may be disabled, but the MIDI messages are already set up under the hood, so you only need to activate the control

element when you need it.


Pink MIDI CC message, channel 1.

Blue MIDI Note message, channel 2.

Green MIDI Note message, example. Slots are deactivated and snapshots do not send out MIDI by default. But the note numbers are already set up

in the background. Note numbers 0-119 are applied, repeating after bank 7 starting with note number 0 again.


_Note: Some CC numbers are missing (CC #0, #6, #32, #38, #97, #98) as they are used for NRPN and Bank Change messages. By skipping those_

_numbers, the mapping does not intersect._


63

-----

# Page 64

## **Troubleshooting**

Setting up Drop is all about making two MIDI devices talk to each other the right way. This may not always be straight forward, so this is a list of

common pitfalls and tips.


**What messages does Drop actually send/receive?**


Use the MIDI Monitor in the PLAY view to see what messages are going in and out of Drop at each MIDI port. Drop keeps a history of the past

messages. You can stop recording and scroll through the history to see what is going on.


**MIDI TRS type A or B**


When using MIDI over TRS, there are historically two standards type A and B where the tip and the ring of the jack are physically switched. A

receiving device may only understand one of the two types. Drop has a switch next to each MIDI Output TRS port to select either type A or B.


MIDI TRS to DIN adaptors also have one specific type A or B. If the wrong type is selected, the outgoing MIDI DIN signal does not work.


Drop can receive both type A and B on its input. The switch only affects the outgoing signal.


**MIDI USB must be class-compliant**


When using a MIDI device over USB, communication only works if the connected device supports class-compliant MIDI. Unfortunately, this is not the

case for all MIDI devices. If your device needs a _driver to be installed, it is not class-compliant_ and can not be used over USB with Drop. Use TRS MIDI

instead. During our tests, we found that some Roland and Boss devices do not support class-compliant MIDI.


Drop may also show an error message and offer you to save a Log file. Before sending us the Log file, please double-check if the device really is

supposed to be class-compliant.


**USB sub-port**


MIDI over USB uses sub-ports, also known as cable ID or virtual cable. The index ranges from 1 to 16. Per sub-port, another 16 MIDI channels can be

sent. Most devices only use one cable ID, but some may also offer multiple ones. Make sure you set up the right one in MENU >Devices or simply try

to find the one that works. The number of sub-ports the device offers is only shown when the MIDI device is connected.


64

-----

# Page 65

**MIDI channel**


Make sure the channel on which Drop sends MIDI messages corresponds to the channel on the receiving device. Drop uses channel numbering 1-16

as the MIDI specification says. However, some devices may use a numbering scheme from 0-15 which is the actual data transmitted in the protocol.


**USB hubs can not be used.**


USB hubs are not supported by Drop. You can only use one direct USB connection from Drop to the device.


**MIDI port selection in** _MENU > Devices_


The MIDI Input and Output ports selected in _MENU > Devices_ are simply the ports where your device is physically connected to and have nothing to

do with routing MIDI from device A to device B.


If you want to route incoming MIDI notes from a keyboard or sequencer to a synth, the synth does not necessarily need the MIDI Input port

enabled. Instead, set up a second Device for the keyboard or sequencer and use the Merger function of the synth Device to set up the routing.


You only need to enable the MIDI Input port, if

- your device is a keyboard or a sequencer

- your device is a groovebox or synth that sends MIDI feedback when turning its knobs and you also want to use it in Drop

- your device is a groovebox or synth that sends MIDI feedback when turning its knobs and you want to use MIDI Learn to set up the mapping.


**Do not ignore warnings**


Throughout all mapping and setup menus, Drop may show a ! warning sign wherever it detects a misconfiguration. For example, when a mapping “ ”

is applied to a Device that does not have an output port set, a warning sign is shown. Warning signs usually mean, that messages are not being sent

or received.


**Enable MIDI-Feedback only if really needed**


Each of Drop s control elements can react to incoming MIDI messages and be remotely turned, moved or pushed that way. The intention is that ’

when you turn the mapped control on the receiver, the mapped control element on Drop also changes its value.


If the control element uses more than one slot and also sends messages to other devices, these messages are also sent when MIDI feedback is

received.


65

-----

# Page 66

For example: You macro-mapped a rotary knob to Synth-A s filter on Slot 1 and Synth-B s volume on Slot 2. The rotary knob s MIDI feedback is ’ ’ ’

enabled and set to Slot 1. Assuming that Synth-A sends back MIDI when turning its filter knob, the rotary control thereby changes its value. To avoid

a potential MIDI feedback loop, Drop will not respond by sending MIDI over Slot 1 on which it also receives incoming MIDI feedback from Synth-A,

however it will still send MIDI out to Slot 2 so that Synth-B changes its volume.


**Remote TX and RX accidentally enabled**


Drop offers the option to be remotely controlled via MIDI which can be enabled in _MENU > Remote_ . This function is also intended to link several

Drop units, which is why Drop can also send the same MIDI messages out, such as the selected cycle length, quantization settings, beatjumps, and

many more. Besides that, incoming MIDI notes can be used to trigger snapshots remotely, e.g. from a MIDI keyboard or sequencer.


Only enable the Remote functions if you really need them, otherwise incoming MIDI messages may change settings in Drop without you even

noticing. The same way, Drop may send MIDI messages without intention.


**MIDI feedback loops**


A MIDI feedback loop is caused when a device receives a message which causes it to respond or pass it through and send another message back,

which in turn causes the other device to also respond with a MIDI message again. By that, both devices end up sending messages back and forth in

a loop and the whole MIDI communication gets stuck. Loops can also occur across three or more devices.


Drop already has some built-in features to prevent MIDI feedback, but it is still possible to create them.


There is no allround solution on how to prevent MIDI feedback loops, but the MIDI Monitor in the PLAY menu may help to find out what is going on.


**Optimize for performance**


It is good practice to make sure only the messages which are actually needed pass through your cables. This reduces errors and improves latency.


- Use the Merger s message filters and only enable what is actually needed.’

- Send MIDI clock only to the ports and devices which actually make use of it. Also, double check if the receiving device needs and understands

Start/Stop and Song Position messages and disable it when not needed.

- Disable all control elements that are not used. If an unused control element is part of a snapshot, it will send unnecessary MIDI data when

executing the snapshot.


66

-----

# Page 67

## **Miscellaneous**

#### **Warranty**

This product is covered by a 24-month warranty starting from the date of purchase. The warranty covers material and manufacturing defects that

occur during normal use.

Excluded from the warranty are: 1 Damage caused by improper handling, accidents, or modifications. 2 Normal wear and tear. 3 Damage ( ) ( ) ( )

resulting from using non-approved accessories or power supplies. In case of a warranty claim, please contact your dealer or our customer service.

Please keep your purchase receipt as proof of warranty.

#### **Safety Warnings**

Only use the supplied power supply or a manufacturer-approved replacement.

Do not expose the device to moisture, rain, or extreme temperatures. Ensure sufficient ventilation and avoid placing the unit near heat sources.

Disconnect the power supply when the device is not in use for long periods. Do not attempt to open or repair the device yourself; this may cause

electric shock and void the warranty. Use the product only as described in this manual and in accordance with local electrical regulations. Keep the

device out of reach of children.

#### **Regulatory**

This product is subject to the WEEE Directive. Do not dispose of the device in household waste. Please use local electronic waste collection points.

#### **Contact**

[Feel free to join the discussion on our ModWiggler forum.](https://www.modwiggler.com/forum/viewforum.php?f=132&sid=e81e89c4830380b4ea573523feea9de1)

[You can also contact us via Email contact@neuzeit-instruments.com](mailto:contact@neuzeit-instruments.com)


The latest firmware and version of this manual can be found on Drop s website: ’ [https://www.neuzeit-instruments.com/drop](https://www.neuzeit-instruments.com/drop)


67