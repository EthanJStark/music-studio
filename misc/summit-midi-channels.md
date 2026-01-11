To configure your MIDI settings for single and multi-timbral use on the Novation Summit, you will primarily use the Settings Menu.
Setting MIDI Channels
For a Single-Timbre Patch (Channel 1): Single patches utilize the Global MIDI Channel
. To set this:

1. Press the Settings button to open the menu
   .
2. Navigate to Page 4/V using the Page buttons
   .
3. Assign Globl Chan to 1 using the row selector and the rotary parameter control
   .
   For a Multi-Patch (Part A on Channel 1 + Part B on Channel 2): Multi-patches allow you to assign independent channels to each part
   . To set this:
4. In the same Settings Menu (Page 4/V), locate the part channel settings
   .
5. Set PartA Chan to 1
   .
6. Set PartB Chan to 2
   . Note: In Multi Patch mode, MIDI data is transmitted and received on these specific Part channels rather than the Global channel
   .
   Patch Changes (Program Changes)
   Patch changes—specifically MIDI Program Change and Bank Change messages—follow these rules:
   • Single Mode: Patch changes are transmitted and received on the Global MIDI Channel only
   .
   • Multi Mode: Data for each part, including patch changes, is handled separately on their assigned Part channels (Channels 1 and 2 in your requested setup)
   .
   • Quirk: Be aware that in some firmware versions, simply exiting a menu may prompt a Program Change message
   .
   Important MIDI Quirks and Features
   • Seq Local Mode: If you are using an external sequencer or DAW, you should consider setting Local to Seq (Settings Menu Page 5/V)
   . In this mode, the keys and wheels send MIDI data to your DAW without affecting the Summit's engine directly, while the front panel controls still affect the engine but do not send MIDI, effectively preventing MIDI feedback loops
   .
   • Global Channel Behavior in Multi Mode: In Firmware 2.1, the Global Channel can still influence Multi Patches depending on the mode
   :
   ◦ Layer Mode: Both parts respond to MIDI on the Global Channel
   .
   ◦ Split Mode: MIDI on the Global Channel affects parts based on the split point (e.g., notes below C3 affect Part A, notes above affect Part B)
   .
   ◦ Dual Mode: MIDI on the Global Channel affects only the currently selected part (A, B, or Both)
   .
   • Arp MIDI Out: By default, the arpeggiator might not send MIDI notes. You must set Arp>MIDI to On in the MIDI Control settings (Page 5/V) to transmit arpeggiated note data
   .
   • CC vs. NRPN: You can choose whether the Summit's controls transmit and receive standard MIDI CCs or more high-resolution NRPN data via the CC/NRPN setting on Page 6/V
   .
