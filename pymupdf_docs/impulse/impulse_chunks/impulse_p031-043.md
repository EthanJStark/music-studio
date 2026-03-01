# Impulse User Guide V5 En (Pages 31-43)

> Converted from PDF using `pymupdf4llm`. Source: `/Users/ethan.stark/dev/misc/music-studio/pdf/impulse_user_guide_v5_en.pdf`.

---

## Page 31

**English**


# **DAW GUIDE**

We’re assuming that you are already quite familiar with the operation of your favourite DAW.
Because there are some differences in the way in which particular DAWs works with Impulse,
you should look at the Support page of the Novation website
[(novationmusic com/support), where you’ll find specific guidance on using Impulse with different](http://www.novationmusic.com/support)
DAWs.

**Ableton Live and Clip-launch mode (Mac or Windows)**
Ableton Live is a music software package which you will find bundled with Impulse. This
contains instructions on how to install it on your computer; there is also some additional
information in the Impulse Getting Started Guide.


There are some general points to note regarding the operation of Ableton Live Lite when using
Impulse as a controller.


  - When using Impulse 25 in **Mixer** mode, the rotary encoders will adjust the same
parameter on each track in a Bank of eight, the Bank depending on which Track is
currently selected in Ableton Live Lite. Thus, if Track 5 is selected, Tracks 1 to 8 will be
controllable; if Track 11 is selected, Tracks 9 to 16 will be controllable.

  - **Page+** and **Page–** let you scroll through the available mixer parameters: Pan, Sends A to
D, for the current set of eight Tracks. On Impulse 25 only, Track Volume is also available
as a controllable parameter.

  - Ableton Live Lite’s mixer may be configured with any number of Return channels (A, B, C,
etc.), but Impulse only allows control of the first four - Returns A to D.

  - On Impulse 25, the single fader will control the volume of the currently selected Track in
**Mixer** mode.

  - The **Track+** and **Track-** buttons select the ‘active’ Track in Ableton Live.

  - The functions of the Transport buttons vary between Ableton Live Lite’s Session View and
Arrangement View.


|Button|Session View|Arrangement View|
|---|---|---|
|Rwd|Steps up one scene|Rwd; Shift+Rwd = return to start|
|FFwd|Steps down one scene|FFwd; Shift+FFwd = go to end|
|Stop|Stops|Stop|
|Play|Play|Play|
|Loop|Play Selected Scene|Enables/disables Loop function|
|Rec|Starts Arrangement Recording|Records|



**31**

---

## Page 32

**English**




- Impulse can be placed in Clip Launch mode by pressing **Roll** and **Arp** buttons
simultaneously. This redefines the function of the drum pads, which now trigger the Clips
in the currently selected Scene. The pads will illuminate according to the Clip status:

  - Unlit – no Clip present

  - Yellow – Clip available

  - Green – Clip playing/ready to play

  - Red – Clip recording/ready to record
Flashing colours indicate that Ableton Live Lite is awaiting the start of the next bar before
acting on the last command.

- Impulse is also compatible with Ableton’s Max for Live. All controllers (faders, buttons,
encoders, pads) will be fully supported as Max for Live controls, i.e., using the Live API.
Wheels, aftertouch and pedals however will not be supported, as they do not interact with
Live directly; they simply send MIDI messages.

- Preview mode is provided to confirm how an encoder is currently configured without
actually changing any Ableton Live parameters. Enter Preview mode by holding down
**Shift** and pressing the **Controls** button. The LED in the **Controls** button blinks to confirm
the mode. Moving any of the eight encoders will display its Ableton Live assignment.
Pressing the **Controls** button again will exit Preview mode.



**32**

---

## Page 33

**English**


# **TROUBLESHOOTING**

For the latest information and assistance with your Impulse please visit:

support novationmusic com/


**Basic Troubleshooting Examples**


  - **Impulse will not power up properly when connected to a laptop computer via USB.**
When a USB connection is used to power the Impulse from a laptop computer the Impulse
may not power up successfully. This is due to the Impulse not being able to draw enough
power from the laptop computer. When powering Impulse from a laptop’s USB port, it is
recommended that the laptop is powered from AC mains rather than its internal battery.
See tip on page 5 for more information.
We also recommend that you connect Impulse directly to a computer’s native USB port,
and not via a USB hub. Correct operation cannot be guaranteed if a hub is in use.
Alternatively, for stand-alone use power the Impulse from a suitable AC:USB DC power
adaptor.


  - **Transmitting MIDI Program Change does not affect a connected MIDI device.**
Some MIDI devices will not accept Program Change messages without receiving a Bank
Select message (CC32 and/or CC0).


  - **Impulse cannot be selected as a MIDI device from within an application.**
When opening an application that uses the Impulse as its source of MIDI input and it is
found that the Impulse cannot be selected as the MIDI input - either the Impulse is greyed
out or it does not appear in a list of available MIDI devices - close the application, wait for
10 seconds, reopen the application and try again.


Under some circumstances it is possible for the Impulse driver to take a few seconds to
become active. If an application is started immediately after the Impulse is powered, without
a few seconds pause in between powering the Impulse and launching the application, the
Impulse driver may not always be available.



**33**

---

## Page 34

**English**


# **FACTORY TEMPLATES**










|No.|Template|Hardware name<br>(8 chars)|
|---|---|---|
|1|Basic MIDI template for standard control and MIDI<br>learn  Avoids commonly used MIDI CCs|<br>BascMIDI|
|2|Controls send commonly used MIDI CCs|UsefulCC|
|3|<br>General MIDI Mixer Template. Faders send volume<br>and encoders send pans on different MIDI channels|GM Mixer|
|4|Ableton Live and Live Lite|Live|
|5|Propellerhead Reason|Reason|
|6|Apple GarageBand|GarageBd|
|7|<br>Apple MainStage|MainStge|
|8|<br>Novation 'Stations' Template:<br>A-Station<br>K-Station<br>X-Station<br>V-Station<br>KS<br>Xio<br>Bass Station Keyboard<br>Bass Station Rack<br>Super Bass Station<br>Bass Station VST|NovaStat|
|9|Novation Ultranova|UltrNova|
|10|Novation Nova, Nova II, Supernova, Supernova II|SupaNova|
|11|<br>Native Instruments - Kontakt|Kontakt|
|12|<br>Native Instruments - FM 8<br>(requires mapping fle on DVD)|FM 8|
|13|Native Instruments - B4 Organ|B4 Organ|
|14|<br>Native Instruments - Massive<br>(requires mapping fle on DVD)|<br>Massive|
|15|Blank User Template|Blank|
|16|<br>Blank User Template|Blank|
|17|<br>Blank User Template|Blank|
|18|<br>Blank User Template|Blank|
|19|<br>Blank User Template|Blank|
|20|<br>Blank User Template|Blank|



**34**

---

## Page 35

**English**


# **ASSIGNABLE CONTROLS – PARAMETERS AND** **RANGES**

**Faders, encoders and Mod Wheel:**
Subsequent presses of the **+** button will offer the following parameter setting pages:

```
Type CC
```

: (Continuous Controller)
```
CC# 0 127
```
:(Controller number, to )
```
Max 0 127
```
: (Maximum parameter value, to )
```
Min 0 127
```
: (Minimum parameter value, to )
```
Channel 1 16 tPL) tPL
```
: MIDI Channel to be used ( to, or ; is as defined within the template
```
Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )

```
Type rPn
```

: (Registered Parameter Number)
```
MSB 0 127
```
: (Most Significant Byte, to )
```
Bank LSB 0 127
```
: (Least Significant Byte, to )
```
Max 0 127
```
: (Maximum parameter value, to )
```
Min 0 127
```
: (Minimum parameter value, to )
```
Channel 1 16 tPL) tPL
```
: MIDI Channel to be used ( to, or ; is as defined within the template
```
Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )

```
Type nrP
```

: (Non-Registered Parameter Number)
```
MSB 0 127
```
: (Most Significant Byte, to )
```
Bank LSB 0 127
```
: (Least Significant Byte, to )
```
Max 0 127
```
: (Maximum parameter value, to )
```
Min 0 127
```
: (Minimum parameter value, to )
```
Channel 1 16 tPL) tPL
```
: MIDI Channel to be used ( to, or ; is as defined within the template
```
Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )


**Drum pads:**
```
Type not
```
:
```
Note C-2 G8
```
: to
```
Max 0 127
```
: (Maximum parameter value, to )
```
Min 0 127
```
: (Minimum parameter value, to )
```
Channel 1 16 tPL) tPL
```
: MIDI Channel to be used ( to, or ; is as defined within the template
```
Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )

```
Type CC rPn nrP
```

:, and : as for encoders/faders



**35**

---

## Page 36

**English**



**Buttons:**
```
Type CC
```
:
```
CC# 0 127
```
:(Controller number, to )


```
 Btn.Type sgl
```

:
```
     Value (0 127)
```
: to
```
     Channel 1 16 tPL) tPL
```
: MIDI Channel to be used ( to, or ; is as defined
within the template
```
     Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type Mty
```
:
```
 Press 0 127
```
: ( to )
```
 Release 0 127
```
: ( to )


```
    Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
    Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type Tgl
```
:
```
On 0 127
```
: ( to )
```
Off 0 127
```
: ( to )
```
    Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
    Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type StP
```
:
```
To 0 127
```
: ( to )
```
From 0 127
```
: ( to )
```
StepSize 1 64
```
: ( to )


```
Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )


```
Type rPn
```

: (Registered Parameter Number)
```
MSB 0 127
```
: (Most Significant Byte, to )
```
LSB 0 127
```
: (Least Significant Byte, to )


```
 Btn.Type sgl
```

:
```
     Value (0 127)
```
: to
```
     Channel 1 16 tPL) tPL
```
: MIDI Channel to be used ( to, or ; is as defined
within the template
```
     Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type Mty
```
:
```
 Press 0 127
```
: ( to )
```
 Release 0 127
```
: ( to )


```
    Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
    Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type Tgl
```
:
```
On 0 127
```
: ( to )
```
Off 0 127
```
: ( to )


```
Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )



**36**

---

## Page 37

**English**


```
Btn.Type StP
```

:
```
To 0 127
```
: ( to )
```
From 0 127
```
: ( to )
```
StepSize 1 64
```
: ( to )
```
    Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
    Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )


```
Type nrP
```

: (Non-registered Parameter Number)
```
MSB 0 127
```
: (Most Significant Byte, to )
```
LSB 0 127
```
: (Least Significant Byte, to )


```
 Btn.Type sgl
```

:
```
     Value (0 127)
```
: to
```
     Channel 1 16 tPL) tPL
```
: MIDI Channel to be used ( to, or ; is as defined
within the template
```
     Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type Mty
```
:
```
 Press 0 127
```
: ( to )
```
 Release 0 127
```
: ( to )


```
    Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
    Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type Tgl
```
:
```
On 0 127
```
: ( to )
```
Off 0 127
```
: ( to )
```
    Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
    Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type StP
```
:
```
To 0 127
```
: ( to )
```
From 0 127
```
: ( to )
```
StepSize 1 64
```
: ( to )


```
Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )


```
Type Prg
```

:
```
Bank MSB 0 127
```
: (Most Significant Byte, to )
```
Bank LSB 0 127
```
: (Least Significant Byte, to )


```
 Btn.Type sgl
```

:
```
     Value (0 127)
```
: to
```
     Channel 1 16 tPL) tPL
```
: MIDI Channel to be used ( to, or ; is as defined
within the template
```
     Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type Mty
```
:
```
 Press 0 127
```
: ( to )
```
 Release 0 127
```
: ( to )


```
Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined



**37**

---

## Page 38

**English**



within the template
```
    Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type Tgl
```
:
```
On 0 127
```
: ( to )
```
Off 0 127
```
: ( to )


```
    Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
    Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )
```
Btn.Type StP
```
:
```
To 0 127
```
: ( to )
```
From 0 127
```
: ( to )
```
StepSize 1 64
```
: ( to )


```
Channel 1 16 tPL) tPL
```

: MIDI Channel to be used ( to, or ; is as defined
within the template
```
Ports tPL USb MId ALL
```
: MIDI port to be used (,,, )



**38**

---

## Page 39

**English**


# **MIDI IMPLEMENTATION TABLE**
























|Function|Transmitted|Recognized|Remarks|
|---|---|---|---|
|Basic<br>Default<br>Channel<br>Changed|1-16<br>1-16|X<br>X||
|Mode<br>Default<br> <br>Messages<br> <br>Altered|Mode 3<br>0<br>*****|X||
|Note<br>Number<br>True Voice|0-127<br>*****|X||
|Velocity<br>Note ON<br> <br>Note OFF|0<br>X|X<br>X||
|After<br>Key’s<br>Touch<br>Channel|X<br>0|X<br>X||
|Pitch Bend|0|X||
|Control<br>Change|0-127|X||
|Program<br>Change<br>True #|0-127|X||
|System Exclusive|0*|0*|*Send / recv frmware<br>update (Novation)<br>Send / recv template<br>data (Novation)|
|System<br>Song Position<br>Pointer<br>Common<br>Song Sel<br> <br>Tune Request|X<br>X<br>X|X<br>X<br>X||
|<br> <br>System<br>Clock<br>Real Time<br>Commands|0<br>0|0<br>X||
|Aux<br>Reset All Controllers<br>Messages<br>Local ON/OFF<br> <br>Active Sensing<br> <br>System Reset|0<br>X<br>X**<br>X|X<br>X<br>X**<br>X|**Can be passed thru<br>via MIDI interface|
|Notes||||


```
M
```

ode 1: OMNI ON, POLY Mode 2: OMNI ON, MONO 0: Yes
Mode 3: OMNI OFF, POLY Mode 4: OMNI OFF, MONO X: No



**39**

---

## Page 40

**English**



Novation
A division of Focusrite Audio Engineering Ltd.
Windsor House,
Turnpike Road,
Cressex Business Park,
High Wycombe,
Bucks,
HP12 3FX.
United Kingdom

Tel: +44 1494 462246
Fax: +44 1494 459920
e-mail: [sales@novationmusic com](mailto:sales@novationmusic.com)
Web: [novationmusic com](http://www.novationmusic.com)

## **Disclaimer**

Novation has taken all possible steps to ensure that the information given here is both correct and
complete. In no event can Novation accept any liability or responsibility for any loss or damage to
the owner of the equipment, any third party, or any equipment which may result from use of this
manual or the equipment which it describes. The information provided in this document may be
modified at any time without prior warning. Specifications and appearance may differ from those
listed and illustrated.



**40**

---

## Page 41

**English**


# **IMPORTANT SAFETY INSTRUCTIONS**

1. Read these instructions.
2. Keep these instructions.
3. Heed all warnings.
4. Follow all instructions.
5. Clean only with dry cloth.
6. Do not install near any heat sources such as radiators, heat registers, stoves, or other
apparatus (including amplifiers) that produce heat.
7. Protect the power cord from being walked on or pinched particularly at plugs, convenience
receptacles, and the point where they exit from the apparatus.
8. Only use attachments/accessories specified by the manufacturer.
9. Use only with the cart, stand, tripod, bracket, or table specified by the
manufacturer, or sold with the apparatus. When a cart is used, use caution
when moving the cart/apparatus combination to avoid injury from tip-over.
10.  Unplug this apparatus during lightning storms or when unused for long periods of time.
11. Refer all servicing to qualified service personnel. Servicing is required when the

apparatus has been damaged in any way, such as power-supply cord or plug is damaged,
liquid has been spilled or objects have fallen into the apparatus, the apparatus has been
exposed to rain or moisture, does not operate normally, or has been dropped.
12. No naked flames, such as lighted candles, should be placed on the apparatus.


**WARNING:** Excessive sound pressure levels from earphones and headphones can cause
hearing loss.


**WARNING:** This equipment must only be connected to USB 1.1, 2.0 or 3.0 type ports



**41**

---

## Page 42

**English**


# **ENVIRONMENTAL DECLARATION**

Compliance Information Statement: Declaration of Compliance procedure

Product Identification: Novation Impulse Keyboard

Responsible party: American Music and Sound

Address: 5304 Derry Avenue #C
Agoura Hills,
CA 91301

Telephone: 800-994-4984


This device complies with part 15 of the FCC Rules. Operation is subject to the following two
conditions: (1) This device may not cause harmful interference, and (2) this device must accept
any interference received, including interference that may cause undesired operation.


**For USA**



**To the User:**
1.  **Do not modify this unit!** This product, when installed as indicated in the instructions



contained in this manual, meets FCC requirements. Modifications not expressly approved by
Novation may void your authority, granted by the FCC, to use this product.
2.  **Important:** This product satisfies FCC regulations when high quality shielded USB cables

with integral ferrite are used to connect with other equipment. Failure to use high quality
shielded USB cables with integral ferrite or to follow the installation instructions within this
manual may cause magnetic interference with appliances such as radios and televisions and
void your FCC authorization to use this product in the USA.
3.  **Note:** This equipment has been tested and found to comply with the limits for a Class B



digital device, pursuant to part 15 of the FCC Rules. These limits are designed to provide
reasonable protection against harmful interference in a residential installation. This
equipment generates, uses and can radiate radio frequency energy and, if not installed
and used in accordance with the instructions, may cause harmful interference to radio
communications. However, there is no guarantee that interference will not occur in a
particular installation. If this equipment does cause harmful interference to radio or television
reception, which can be determined by turning the equipment off and on, the user is
encouraged to try to correct the interference by one or more of the following measures:

  - Reorient or relocate the receiving antenna.

  - Increase the separation between the equipment and receiver.

  - Connect the equipment into an outlet on a circuit different from that to which the receiver
is connected.

  - Consult the dealer or an experienced radio/TV technician for help.



**42**

---

## Page 43

**English**



**For Canada**


**To the User:**
This Class B digital apparatus complies with Canadian ICES-003.
Cet appareil numérique de la classe B est conforme à la norme NMB-003 du Canada.


**RoHS Notice**


Novation has conformed and product conforms, where applicable, to the European

Union’s Directive 2002/95/EC on Restrictions of Hazardous Substances (RoHS) as

well as the following sections of California law which refer to RoHS, namely sections

25214. 10, 25214. 10. 2, and 58012, Health and Safety Code; Section 42475. 2, Public

Resources Code.


**CAUTION:**


The normal operation of this product may be affected by a strong electrostatic

discharge (ESD). In the event of this happening, simply reset the unit by removing and

then replugging the USB cable. Normal operation should return.

# **COPYRIGHT AND LEGAL NOTICES**


Novation is a registered trade mark of Focusrite Audio Engineering Limited.
Impulse is a trade mark of Focusrite Audio Engineering Limited.


VST is a trade mark of Steinberg Media Technologies GmbH.


All other brand, product and company names and any other registered names or trade marks
mentioned in this manual belong to their respective owners.


2021 © Focusrite Audio Engineering Limited. All rights reserved.



**43**
