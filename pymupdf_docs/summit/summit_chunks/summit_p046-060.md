# Summit User Guide 1.1 En (Pages 46-60)

> Converted from PDF using `pymupdf4llm`. Source: `/Users/ethan.stark/dev/misc/audio-midi/pdf/Summit User Guide 1.1 EN.pdf`.

---

## Page 46

**MIDI operation in Single and Multi Patch modes**








|Col1|MIDI CHANNEL|Col3|Col4|
|---|---|---|---|
||**GLOBAL**|**PART A**|**PART B**|
|**Single Patches**|**Single Patches**|**Single Patches**|**Single Patches**|
||MIDI data is transmitted<br>and received on the Global<br>Channel only|No data transmitted or received|No data transmitted or received|
|**Multi Patches – MIDI Rx**|**Multi Patches – MIDI Rx**|**Multi Patches – MIDI Rx**|**Multi Patches – MIDI Rx**|
|LAYER MODE|MIDI data received regardless<br>of which Part is selected|Data for each Part accepted<br>on its assigned channel|Data for each Part accepted<br>on its assigned channel|
|SPLIT MODE|Data not accepted|Data not accepted|Data not accepted|
|DUAL MODE|Data accepted if**MULTIPART**<br>**CONTROL** is set to**Both**|Data accepted if**MULTIPART**<br>**CONTROL** is set to**Both**|Data accepted if**MULTIPART**<br>**CONTROL** is set to**Both**|
|**Multi Patches – MIDI Tx**|**Multi Patches – MIDI Tx**|**Multi Patches – MIDI Tx**|**Multi Patches – MIDI Tx**|
|LAYER MODE|No data transmitted|Data for each Part is<br>transmitted separately on its<br>assigned channel|Data for each Part is<br>transmitted separately on its<br>assigned channel|
|SPLIT MODE|SPLIT MODE|SPLIT MODE|SPLIT MODE|
|DUAL MODE|DUAL MODE|DUAL MODE|DUAL MODE|



**Modulation Matrix – sources**
The table below lists the sources of modulation available to Inputs A and B of each Slot in
the Modulation Matrix.

|Display|Controlling Source|Col3|Col4|
|---|---|---|---|
|`Direct`|The**Depth** control (|10|; select Row 4)|
|`ModWheel`|<br>Mod Wheel|<br>Mod Wheel|<br>Mod Wheel|
|`AftTouch`|Keyboard aftertouch|Keyboard aftertouch|Keyboard aftertouch|
|`ExprPED1`|Expression pedal connected at PEDAL 1 input|Expression pedal connected at PEDAL 1 input|Expression pedal connected at PEDAL 1 input|
|`BrthPED2`|Expression pedal connected at PEDAL 2 input|Expression pedal connected at PEDAL 2 input|Expression pedal connected at PEDAL 2 input|
|`Velocity`|Keyboard velocity|Keyboard velocity|Keyboard velocity|
|`Keyboard`|Key position on keyboard|Key position on keyboard|Key position on keyboard|
|`Lfo1+`|LFO 1 waveform varies controlled parameter in a positive sense|LFO 1 waveform varies controlled parameter in a positive sense|LFO 1 waveform varies controlled parameter in a positive sense|
|`Lfo1+/-`|LFO 1 waveform varies controlled parameter both positively and<br>negatively|LFO 1 waveform varies controlled parameter both positively and<br>negatively|LFO 1 waveform varies controlled parameter both positively and<br>negatively|
|`Lfo2+`|LFO 2 waveform varies controlled parameter in a positive sense|LFO 2 waveform varies controlled parameter in a positive sense|LFO 2 waveform varies controlled parameter in a positive sense|
|`Lfo2+/-`|LFO 2 waveform varies controlled parameter both positively and<br>negatively|LFO 2 waveform varies controlled parameter both positively and<br>negatively|LFO 2 waveform varies controlled parameter both positively and<br>negatively|
|`AmpEnv`|Amplitude envelope|Amplitude envelope|Amplitude envelope|
|`ModEnv1`|Modulation envelope 1|Modulation envelope 1|Modulation envelope 1|
|`ModEnv2`|Modulation envelope 2|Modulation envelope 2|Modulation envelope 2|
|`Animate1`|Animate Button 1|Animate Button 1|Animate Button 1|
|`Animate2`|Animate Button 2|Animate Button 2|Animate Button 2|
|`CV +/-`|CV input varies controlled parameter both positively and negatively|CV input varies controlled parameter both positively and negatively|CV input varies controlled parameter both positively and negatively|
|`Lfo3 +`|LFO 3 waveform varies controlled parameter in a positive sense|LFO 3 waveform varies controlled parameter in a positive sense|LFO 3 waveform varies controlled parameter in a positive sense|
|`Lfo3 +/-`|LFO 3 waveform varies controlled parameter both positively and<br>negatively|LFO 3 waveform varies controlled parameter both positively and<br>negatively|LFO 3 waveform varies controlled parameter both positively and<br>negatively|
|`Lfo4 +`|LFO 4 waveform varies controlled parameter in a positive sense|LFO 4 waveform varies controlled parameter in a positive sense|LFO 4 waveform varies controlled parameter in a positive sense|
|`Lfo4 +/-`|LFO 4 waveform varies controlled parameter both positively and<br>negatively|LFO 4 waveform varies controlled parameter both positively and<br>negatively|LFO 4 waveform varies controlled parameter both positively and<br>negatively|
|`BndWhl+`|Pitch Bend wheel up increases parameter|Pitch Bend wheel up increases parameter|Pitch Bend wheel up increases parameter|
|`BndWhl-`|Pitch Bend wheel up decreases parameter|Pitch Bend wheel up decreases parameter|Pitch Bend wheel up decreases parameter|



**Modulation Matrix – destinations**
The table below lists the destinations you can route each Modulation Matrix slot to.

|Display|Controlling Source|
|---|---|
|`O123Ptch`|Frequency of all three oscillators|
|`Osc1Ptch`|Oscillator 1 frequency|
|`Osc2Ptch`|Oscillator 2 frequency|
|`Osc3Ptch`|Oscillator 3 frequency|
|`Osc1VSnc`|Oscillator 1 VSync level|
|`Osc2VSnc`|Oscillator 2 VSync level|
|`Osc3VSnc`|Oscillator 3 VSync level|
|`Osc1Shpe`|Oscillator 1 Shape Amount|
|`Osc2Shpe`|Oscillator 2 Shape Amount|
|`Osc3Shpe`|Oscillator 3 Shape Amount|
|`Osc1 Lev`|Oscillator 1 level|
|`Osc2 Lev`|Oscillator 2 level|
|`Osc3 Lev`|Oscillator 3 level|
|`NoiseLev`|Noise source level|



**46**



**Modulation Matrix – destinations continued**

|Ring Lev|Ring Modulator output level (RM inputs are Osc 1 and Osc 2)|
|---|---|
|`VcaLevel`|Overall synth output level|
|`Filt Drv`|Pre-flter Overdrive|
|`FiltDist`|Post-flter Distortion|
|`FiltFreq`|Filter cut-off frequency (or centre frequency when Shape=BP)|
|`Filt Res`|Filter Resonance|
|`Lfo1Rate`|LFO 1 frequency|
|`Lfo2Rate`|LFO 2 frequency|
|`AmpEnv A`|Attack time of Amplitude envelope|
|`AmpEnv D`|Decay time of Amplitude envelope|
|`AmpEnv R`|Release time of Amplitude envelope|
|`ModEnv1A`|Attack time of Modulation envelope 1|
|`ModEnv1D`|<br>Decay time of Modulation envelope 1|
|`ModEnv1R`|Release time of Modulation envelope 1|
|`ModEnv2A`|Attack time of Modulation envelope 2|
|`ModEnv2D`|Decay time of Modulation envelope 2|
|`ModEnv2R`|Release time of Modulation envelope 2|
|`FM O1>O2`|Depth of Frequency modulation applied to Oscillator 2 by Oscillator 1*|
|`FM O2>O3`|Depth of frequency modulation applied to Oscillator 3 by Oscillator 2*|
|`FM O3>O1`|Depth of frequency modulation applied to Oscillator 1 by Oscillator 3*|
|`FM Ns>O1`|Amount of noise modulation applied to Oscillator 1*|
|`O3>FiltF`|Degree of control of flter cut-off/centre frequency by Oscillator 3*|
|`Ns>FiltF`|Degree of control of flter cut-off/centre frequency by noise source*|
|`FfreqSep`|Difference between the frequencies of two flters when used in<br>combination|



- Note that only positive values of **Depth** are effective for the FM options; all negative values are
considered as zero.


**FX Modulation Matrix – sources**
The table below lists the sources of modulation available to Inputs A and B of each Slot in
the FX Modulation Matrix.

|Display|Controlling Source|
|---|---|
|`Direct`|The**Depth** control ([10]; select Row 4)|
|`ModWheel`|Mod Wheel|
|`AftTouch`|Keyboard aftertouch|
|`ExprPED1`|Expression pedal connected at**PEDAL 1** input|
|`BrthPED2`|Expression pedal connected at**PEDAL 2** input|
|`Velocity`|Keyboard velocity|
|`Keyboard`|Key position on keyboard|
|`Animate1`|Animate Button 1|
|`Animate2`|Animate Button 2|
|`CV +/-`|CV input varies controlled parameter both positively and negatively|
|`Lfo3 +`|LFO 3 waveform varies controlled parameter in a positive sense|
|`Lfo3 +/-`|LFO 3 waveform varies controlled parameter both positively and<br>negatively|
|`Lfo4 +`|LFO 4 waveform varies controlled parameter in a positive sense|
|`Lfo4 +/-`|LFO 4 waveform varies controlled parameter both positively and<br>negatively|
|`BndWhl+`|Pitch Bend wheel up: increases parameter|
|`BndWhl-`|Pitch Bend wheel up: decreases parameter|



**FX Modulation Matrix – destinations**
The table below lists the destinations you can route each FX Modulation Matrix Slot to.


|Display|Controlled Parameter|
|---|---|
|`Dist Lev`|Distortion Level|
|`Chor Lev`|Chorus Level|
|`ChorRate`|Chorus Rate|
|`Chor Dep`|Chorus Depth|
|`Chor FB`|Chorus Feedback|
|`Del Lev`|Delay Level|
|`Del Time`|Delay Time|
|`Del FB`|Delay Feedback|
|`Rev Lev`|Reverb Level|
|`Rev Time`|Reverb Time|
|`Rev LPF`|Reverb Low Pass|
|`Rev HPF`|Reverb High Pass|

---

## Page 47

**MIDI parameters list**

|Parameter|CC/<br>NRPN|Control<br>Number.|Range|Default<br>Value|
|---|---|---|---|---|
|Patch Category|NRPN|0:0|0-14|0|
|Patch Genre|NRPN|0:1|0-9|0|
|Voice Mode|NRPN|0:2|0-4|3|
|Voice Unison|NRPN|0:3|0-4|0|
|Voice Unison Detune|NRPN|0:4|0-127|25|
|Voice Unison Spread|NRPN|0:5|0-127|0|
|Voice Keyboard Octave|NRPN|0:6|61-67 (-3 to +3)|64 (0)|
|Glide Time|CC|5|0-127 (0 to<br>+127)|0 (60)|
|Voice Pre-Glide|NRPN|0:7|52-76 (-12 to<br>+12)|64 (Off)|
|Glide On|CC|35|0-1 (0 to +1)|0 (0)|
|**Oscillators**|**Oscillators**|**Oscillators**|**Oscillators**|**Oscillators**|
|Osc Common Diverge|NRPN|0:9|0-127<br>(0 to +127)|0 (0)|
|Osc Common Drift|NRPN|0:10|0-127 (0 to<br>+127)|0 (0)|
|Osc Common Noise<br>LPF|NRPN|0:11|0-127<br>(0 to +127)|127|
|Oscillator 1 Range|CC|3|63-66 (-1 to +2)|64 (0)|
|Oscillator 1 Coarse|CC pair|14, 46|0-255<br>(-128 to +127)|128 (0)|
|Oscillator 1 Fine|CC pair|15, 47|28-228<br>(-100 to +100)|128 (0)|
|Oscillator 1<br>ModEnv2 > Pitch|CC|9|1-127<br>(-63 to +63)|64 (0)|
|Oscillator 1<br>LFO2 > Pitch|CC pair|16, 48|1-255<br>(-127 to +127)|128 (0)|
|Oscillator 1 Wave|NRPN|0:14|0-4 (0 to +4)|0 (2)|
|Oscillator 1 Wave More|NRPN|0:15|4-63 (4 to +63)|0 (4)|
|Oscillator 1<br>Shape Source|NRPN|0:16|0-2 (0 TO +2)|0 (0)|
|Oscillator 1<br>Manual Shape|CC|12|0-127<br>(-64 to +63)|64 (0)|
|Oscillator 1<br>ModEnv1 > Shape|CC|119|0-127<br>(-64 to +63)|64 (0)|
|Oscillator 1<br>LFO1 > Shape|CC|33|1-127<br>(-64 to +63)|64 (0)|
|Oscillator 1 Vsync|CC|34|0-127<br>(0 to +127)|0 (0)|
|Oscillator 1<br>Saw Density|NRPN|0:17|0-127<br>(0 to +127)|0 (0)|
|Oscillator 1<br>Saw Density Detune|NRPN|0:18|0-127<br>(0 to +127)|0|
|Oscillator 1 Fixed Note|NRPN|0:19|0-88 (0 to +88)|0 (Off)|
|Oscillator 1<br>Bend Range|NRPN|0:20|40-88<br>(-24 to +24)|76|
|Oscillator 2 Range|CC|37|63-66 (-1 to +2)|64 (0)|
|Oscillator 2 Coarse|CC pair|17, 49|0-255<br>(-128 to +127)|64|
|Oscillator 2 Fine|CC pair|18, 50|28-228<br>(-100 to +100)|64|
|Oscillator 2<br>ModEnv2 > Pitch|CC|38|1-127<br>(-63 to +63)|64 (0)|
|Oscillator 2<br>LFO2 > Pitch|CC pair|19, 51|1-255<br>(-127 to +127)|64|
|Oscillator 2 Wave|NRPN|0:23|0-4 (0 to +4)|0 (2)|
|Oscillator 2 Wave More|NRPN|0:24|4-63 (4 to +63)|0 (4)|
|Oscillator 2<br>Shape Source|NRPN|0:25|0-2 (0 TO +2)|0 (0)|
|Oscillator 2<br>Manual Shape|CC|39|0-127<br>(-64 to +63)|64 (0)|
|Oscillator 2<br>ModEnv1 > Shape|CC|40|0-127<br>(-64 to +63)|64 (0)|
|Oscillator 2<br>LFO1 > Shape|CC|41|1-127<br>(-64 to +63)|64 (0)|
|Oscillator 2 Vsync|CC|42|0-127<br>(0 to +127)|0 (0)|



**47**




|Parameter|CC/<br>NRPN|Control<br>Number.|Range|Default<br>Value|
|---|---|---|---|---|
|Oscillator 2<br>Saw Density|NRPN|0:26|0-127<br>(0 to +127)|0 (0)|
|Oscillator 2<br>Saw Density Detune|NRPN|0:27|0-127<br>(0 to +127)|0 (64)|
|Oscillator 2 Fixed Note|NRPN|0:28|0-88 (0 to +88)|0 (Off)|
|Oscillator 2<br>Bend Range|NRPN|0:29|40-88<br>(-24 to +24)|76 (12)|
|Oscillator 3 Range|CC|65|63-66 (-1 to +2)|64 (0)|
|Oscillator 3 Coarse|CC pair|20, 52|0-255<br>(-128 to +127)|128 (0)|
|Oscillator 3 Fine|CC pair|21, 53|<br>28-228<br>(-100 to +100)|128 (0)|
|Oscillator 3<br>ModEnv2 > Pitch|CC|43|<br>1-127<br>(-63 to +63)|64 (0)|
|<br>Oscillator 3<br>LFO2 > Pitch|CC pair|22,54|<br>1-255<br>(-127 to +127)|128 (0)|
|Oscillator 3 Wave|NRPN|0:32|0-4 (0 to +4)|0 (2)|
|Oscillator 3 Wave More|NRPN|0:33|4-63 (4 to +63)|0 (4)|
|Oscillator 3<br>Shape Source|NRPN|0:34|0-2 (0 TO +2)|0 (0)|
|<br>Oscillator 3<br>Manual Shape|CC|71|0-127<br>(-64 to +63)|64 (0)|
|<br>Oscillator 3<br>ModEnv1 > Shape|CC|72|<br>0-127<br>(-64 to +63)|64 (0)|
|<br>Oscillator 3<br>LFO1 > Shape|CC|73|<br>1-127<br>(-64 to +63)|64 (0)|
|<br>Oscillator 3 Vsync|CC|44|<br>0-127<br>(0 to +127)|0 (0)|
|Oscillator 3<br>Saw Density|NRPN|0:35|<br>0-127<br>(0 to +127)|0 (0)|
|<br>Oscillator 3<br>Saw Density Detune|NRPN|0:36|<br>0-127<br>(0 to +127)|0 (64)|
|<br>Oscillator 3 Fixed Note|NRPN|0:37|<br>0-88 (0 to +88)|0 (Off)|
|Oscillator 3<br>Bend Range|NRPN|0:38|40-88<br>(-24 to +24)|76 (12)|
|<br> <br>**Mixer**|<br> <br>**Mixer**|<br> <br>**Mixer**|<br> <br>**Mixer**|<br> <br>**Mixer**|
|Mixer Osc1|CC pair|23,55|0-255<br>(0 to +255)|255|
|Mixer Osc2|CC pair|24,56|0-255|0 (0)|
|Mixer Osc3|CC pair|25,57|(0 to +255)|0 (0)|
|Ring 1*2 Level|CC pair|26,58|0-255|0 (0)|
|Noise Level|CC pair|27,59|(0 to +255)|0 (0)|
|Mixer Patch Level|NRPN|0:41|0-127<br>(0 to +127)|64|
|Mixer VCA gain|NRPN|0:42|0-127<br>(0 to +127)|127|
|Mixer Dry Level|NRPN|0:43|0-127<br>(0 to +127)|127|
|Mixer Wet Level|NRPN|0:44|0-127<br>(0 to +127)|127|
|**Filter**|**Filter**|**Filter**|**Filter**|**Filter**|
|Filter Overdrive|CC|80|0-127<br>(0 to +127)|0 (0)|
|Filter Post Drive|CC|36|0-127<br>(0 to +127)|0 (0)|
|Filter Slope|NRPN|0:45|0-1 (0 to +1)|1|
|Filter Shape|NRPN|0:46|0-2 (0 to +2)|0 (0)|
|Filter Key Tracking|CC|75|0-127<br>(0 to +127)|127|
|Filter Resonance|CC|79|0-127<br>(0 to +127)|0 (0)|
|Filter Frequency|CC pair|29, 61|0-255<br>(0 to +255)|0 (255)|
|Filter<br>LFO1 > Filter|CC pair|28, 60|1-255<br>(-127 to +127)|128 (0)|
|Filter<br>Osc3 > Filter|CC|76|0-127<br>(0 to +127)|0 (0)|
|Filter Env Select|NRPN|0:47|0-1 (0 to +1)|0 (1)|
|Filter<br>AmpEnv > Filter|CC|77|1-127<br>(-63 to +63)|64 (0)|
|Filter<br>ModEnv1 > Filter|CC|78|1-127<br>(-63 to +63)|64 (0)|
|Filter Divergence|NRPN|0:48|0-127<br>(0 to +127)|0 (0)|

---

## Page 48

|Parameter|CC/<br>NRPN|Control<br>Number.|Range|Default<br>Value|
|---|---|---|---|---|
|**Envelopes**|**Envelopes**|**Envelopes**|**Envelopes**|**Envelopes**|
|Amp Envelope Attack|CC|86|0-127<br>(0 to +127)|0|
|Amp Envelope Decay|CC|87|0-127 (0 to<br>+127)|90|
|Amp Envelope Sustain|CC|88|0-127 (0 to<br>+127)|127|
|Amp Envelope Release|CC|89|0-127 (0 to<br>+127)|40|
|Amp Envelope Velocity|NRPN|0:55|0-127<br>(-64 to +63)|64 (0)|
|Amp Envelope Trigger|NRPN|0:56|0-1 (0 to +1)|0|
|Mod Envelope Select|NRPN|0:59|0-1 (0 to +1)|0 (1)|
|Mod Envelope 1 Attack|CC|90|0-127<br>(0 to +127)|0|
|Mod Envelope 1 Decay|CC|91|0-127<br>(0 to +127)|75|
|Mod Envelope 1 Sustain|CC|92|0-127<br>(0 to +127)|35|
|Mod Envelope 1<br>Release|CC|93|0-127<br>(0 to +127)|45|
|Mod Envelope 1<br>Velocity|NRPN|0:60|0-127<br>(-64 to +63)|64 (0)|
|Mod Envelope 1 Trigger|NRPN|0:61|0-1 (0 to +1)|0 (1)|
|Mod Envelope 2 Attack|CC|94|0-127<br>(0 to +127)|0|
|Mod Envelope 2 Decay|CC|95|0-127<br>(0 to +127)|75|
|Mod Envelope 2 Sustain|CC|117|0-127<br>(0 to +127)|35|
|Mod Envelope 2<br>Release|CC|103|0-127<br>(0 to +127)|45|
|Mod Envelope 2<br>Velocity|NRPN|0:64|0-127<br>(-64 to +63)|64 (0)|
|Mod Envelope 2 Trigger|NRPN|0:65|0-1 (0 to +1)|0 (1)|
|**LFOs**|**LFOs**|**LFOs**|**LFOs**|**LFOs**|
|LFO 1 Range|NRPN|0:68|0-2 (0 to +2)|0 (0)|
|LFO 1 Rate|CC pair|30, 62|0-255 (0 to<br>+255)|128|
|LFO 1 Sync Rate|CC|81|0-34 (0 to +34)|16|
|LFO 1 Wave|NRPN|0:69|0-3 (0 to +3)|0 (0)|
|LFO 1 Phase|NRPN|0:70|0-120<br>(0 to +120)|0 (0)|
|LFO 1 Slew|NRPN|0:71|0-127<br>(0 to +127)|0 (0)|
|LFO 1 Fade Time|CC|82|0-127<br>(0 to +127)|0 (0)|
|LFO 1 Fade In/Out|NRPN|0:72|0-3 (0 to +3)|0 (0)|
|LFO 1 One Shot|NRPN|0:75|0-1 (0 to +1)|0 (0)|
|LFO 1 Common|NRPN|0:76|0-1 (0 to +1)|0 (0)|
|LFO 2 Range|CC|83|0-2 (0 to +2)|0 (0)|
|LFO 2 Rate|CC pair|31, 63|0-255<br>(0 to +255)|128|
|LFO 2 Sync Rate|CC|84|0-34 (0 to +34)|0 (12)|
|LFO 2 Wave|NRPN|0:78|0-3 (0 to +3)|0 (0)|
|LFO 2 Phase|NRPN|0:79|0-120<br>(0 to +120)|0 (0)|
|LFO 2 Slew|NRPN|0:80|0-127<br>(0 to +127)|0 (0)|
|LFO 2 Fade Time|CC|85|0-127<br>(0 to +127)|0 (0)|
|LFO 2 Fade In/Out|NRPN|0:81|<br>0-3 (0 to +3)|0 (0)|
|LFO 2 One Shot|NRPN|0:84|0-1 (0 to +1)|0 (0)|
|LFO 2 Common|NRPN|0:85|0-1 (0 to +1)|0 (0)|
|**Effects**|**Effects**|**Effects**|**Effects**|**Effects**|
|Distortion level|CC|104|0-127<br>(0 to +127)|0 (0)|
|Effects Master Bypass|NRPN|0:88|0-1 (0 to +1)|0 (0)|
|Effects Routing|NRPN|0:89||0 (0)|
|Delay Level|CC|108|0-127<br>(0 to +127)|0 (0)|
|Delay Time|CC|109|<br>0-127<br>(0 to +127)|0 (64)|


**48**




|Parameter|CC/<br>NRPN|Control<br>Number.|Range|Default<br>Value|
|---|---|---|---|---|
|Delay Width|NRPN|0:92|0-127<br>(0 to +127)|0 (64)|
|Delay Sync|NRPN|0:93|0-1 (0 to +1)|0 (0)|
|Delay Sync Time|NRPN|0:94|0-18 (0 to +18)|0 (4)|
|Delay Feedback|CC|110|0-127<br>(0 to +127)|0 (64)|
|Delay LP Damp|NRPN|0:95|0-127<br>(0 to +127)|85|
|Delay HP Damp|NRPN|0:96|0-127<br>(0 to +127)|0 (0)|
|Delay Slew Rate|NRPN|0:97|0-127<br>(0 to +127)|32|
|Reverb Level|CC|112|0-127<br>(0 to +127)|0 (0)|
|Reverb Type|NRPN|0:101|0-2 (0 to +2)|2|
|Reverb Time|CC|113|0-127<br>(0 to +127)|0 (90)|
|Reverb Damping LP|NRPN|0:102|0-127<br>(0 to +127)|0 (50)|
|Reverb Damping HP|NRPN|0:103|0-127<br>(0 to +127)|0 (1)|
|Reverb Size|NRPN|0:104|0-127<br>(0 to +127)|64|
|Reverb Mod|NRPN|0:105|0-127<br>(0 to +127)|64|
|Reverb Mod Rate|NRPN|0:106|0-127<br>(0 to +127)|0 (4)|
|Reverb Low Pass|NRPN|0:107|0-127<br>(0 to +127)|0 (74)|
|Reverb High Pass|NRPN|0:108|0-127<br>(0 to +127)|0 (0)|
|Reverb Pre Delay|NRPN|0:109|0-127<br>(0 to +127)|40|
|Chorus Level|CC|105|0-127<br>(0 to +127)|0 (0)|
|Chorus Type|NRPN|0:111||2|
|Chorus Rate|CC|118|0-127<br>(0 to +127)|20|
|Chorus Mod Depth|NRPN|0:112|0-127<br>(0 to +127)|0 (64)|
|Chorus Feedback|CC|107|0-127<br>(-64 to +63)|64|
|Chorus LP|NRPN|0:113|<br>0-127<br>(0 to +127)|90|
|Chorus HP|NRPN|0:114|<br>0-127<br>(0 to +127)|2|
|<br>**ARP**|<br>**ARP**|<br>**ARP**|<br>**ARP**|<br>**ARP**|
|Arp/Clock Rate|NA|NA:NA|40-240<br>(40 to +240)|120|
|Arp/Clock Sync Rate|NRPN|0:116|<br>0-18 (0 to +18)|16th.|
|Arp/Clock Type|NRPN|0:117|0-6 (0 to +6)|0 (0)|
|Arp/Clock Rhythm|NRPN|0:118|0-32 (0 to +32)|0 (0)|
|Arp/Clock Octave|NRPN|0:119|0-5 (0 to +5)|1|
|Arp/Clock Gate|CC|116|0-127<br>(0 to +127)|64|
|Arp/Clock Swing|NRPN|0:120|<br>20-80<br>(20 to +80)|50|
|Arp/Clock On|NRPN|0:121|0-1 (0 to +1)|0 (0)|
|Arp/Clock Key Latch|NRPN|0:122|0-1 (0 to +1)|0 (0)|
|Arp/Clock Key Sync|NRPN|0:123|0-1 (0 to +1)|0 (0)|
|**ANIMATE**|**ANIMATE**|**ANIMATE**|**ANIMATE**|**ANIMATE**|
|Animate 1 Hold|CC|114|0-1 (0 to +1)|0 (0)|
|Animate 2 Hold|CC|115|0-1 (0 to +1)|0 (0)|
|**MODULATION MATRIX**|**MODULATION MATRIX**|**MODULATION MATRIX**|**MODULATION MATRIX**|**MODULATION MATRIX**|
|Mod Matrix Selection|NRPN|0:125|0-15 (0 to +15)|0 (0)|
|Mod Matrix 1 Source1|NRPN|1:0|0-16 (0 to +16)|0 (0)|
|Mod Matrix 1 Source2|NRPN|1:1|0-16 (0 to +16)|0 (0)|
|Mod Matrix 1 Depth|NRPN|1:2|0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 1<br>Destination|NRPN|1:3|0-36 (0 to +36)|0 (0)|
|Mod Matrix 2 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 2 Source2|NRPN||0-16 (0 to +16)|0 (0)|

---

## Page 49

|Parameter|CC/<br>NRPN|Control<br>Number.|Range|Default<br>Value|
|---|---|---|---|---|
|Mod Matrix 2 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 2<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 3 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 3 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 3 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 3<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 4 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 4 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 4 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 4<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 5 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 5 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 5 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 5<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 6 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 6 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 6 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 6<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 7 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 7 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 7 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 7<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 8 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 8 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 8 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 8<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 9 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 9 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 9 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 9<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 10 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 10 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 10 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 10<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 11 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 11 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 11 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 11<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 12 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 12 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 12 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 12<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 13 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 13 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 13 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 13<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 14 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 14 Source2|NRPN||0-16 (0 to +16)|0 (0)|


**49**



|Parameter|CC/<br>NRPN|Control<br>Number.|Range|Default<br>Value|
|---|---|---|---|---|
|Mod Matrix 14 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 14<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 15 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 15 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 15 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 15<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|
|Mod Matrix 16 Source1|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 16 Source2|NRPN||0-16 (0 to +16)|0 (0)|
|Mod Matrix 16 Depth|NRPN||0-127<br>(-64 to +63)|64 (0)|
|Mod Matrix 16<br>Destination|NRPN||0-36 (0 to +36)|0 (0)|


**Sound designers**
We’d like to thank the fantastic souls who came on the journey with us to give a voice to
Novation Summit. If you want to know more about them, you’ll find links to their work below.
The selected palette of sound attempts to display how flexible and beautiful or aggressive
Summit can be.


We hope these sounds will help inspire your future composition and creation.


|Sound Designer / Artist|If you want to know more about them…|
|---|---|
|Patricia Wolf|soundcloud.com/patriciawolf_music<br>facebook.com/patriciawolfmusic|
|Gforce Software|gforcesoftware.com|
|Legowelt|legowelt.org|
|Inhalt|inhalt.us<br>inhalt.bandcamp.com|
|Sandunes|sandunesmusic.com|
|Peter Dyer|peterdyer.net|
|Groundislava|soundcloud.com/groundislava<br>facebook.com/groundislava|
|Tim Mantle / Psalm 37|timmantle.com/psalm37.html|
|Enrico Cosimi|mastersuono.uniroma2.it/team/dott-enrico-cosimi|
|R Beny|rbeny.bandcamp.com<br>instagram.com/austinthecairns<br>soundcloud.com/rbeny<br>youtube.com/channel/UC5hhwOVY0lxIn4ELd5ZP1Bw|
|Chris Calcutt / Calc|youtube.com/user/boxkidnine|
|Alex Jann|soundcloud.com/alexjann<br>facebook.com/alexjann.uk|
|Loz Jackson|lozjackson.com<br>Loz is also one of the core developers of Novation<br>Components|
|Tristan McGuire|Tristan is Novation Summit Lead Test Engineer|
|Danny Nugent|Summit’s Product Designer|
|Jerome Meunier|facebook.com/myjima<br>instagram.com/myjima|

---

## Page 50

**List of factory Patches with designer credits**

|Patch No.|Single Patches – Bank A|Col3|Single Patches – Bank B|Col5|
|---|---|---|---|---|
|**Patch No.**|**Patch Name**|**Created by**|**Patch Name**|**Created by**|
|0|**Dystopian**|Gforce Software|**Dune Sunrise PAD**|Sandunes|
|1|**Buzzy Brass**|Enrico Cosimi|**Force Field**|Patricia Wolf|
|2|**Aetherphone**|Patricia Wolf|**Dearly Beloved**|Peter Dyer|
|3|**3 Osc BassSynth**|Gforce Software|**Triple Wavetable**|Enrico Cosimi|
|4|**GIL Deep Plane**|Groundislava|**Sergey Repetae**|Inhalt|
|5|**Death of a King**|Tim Mantle/Psalm37|**Careless Crystal**|Tim Mantle/Psalm37|
|6|**Epic Atmosphere**|Gforce Software|**4>8>12 UnisonPWM**|Gforce Software|
|7|**OperatahBass**|Peter Dyer|**80s Bell Patch**|Gforce Software|
|8|**Little Grey Bass**|Gforce Software|**80’s Digi-Syn**|Gforce Software|
|9|**Simple & Sublime**|Gforce Software|**99to88to78**|Gforce Software|
|10|**Droom Wolk**|Legowelt|**Arc de Triumph**|Gforce Software|
|11|**Alpine Crystal**|Legowelt|**Arps Of Joy**|Gforce Software|
|12|**Amatoral Concept**|Legowelt|**Breathy Trumpet**|Gforce Software|
|13|**Arpeggi Trancy**|Legowelt|**Buzz BASS!**|Gforce Software|
|14|**Beautiful Bits**|Legowelt|**Dirt Guitar Lead**|Gforce Software|
|15|**Carnival of Soul**|Legowelt|**Dirty Basstard**|Gforce Software|
|16|**Coastal Hamlet**|Legowelt|**DoAnimate2&Bend**|Gforce Software|
|17|**Digital Dew**|Legowelt|**Dream Arp**|Gforce Software|
|18|**Enery Splash**|Legowelt|**Dukey Lead**|Gforce Software|
|19|**Experial Evil**|Legowelt|**Eerie ModW^**|Gforce Software|
|20|**Florist Study**|Legowelt|**Epic Flutter**|Gforce Software|
|21|**Forestfull**|Legowelt|**Fifths**|Gforce Software|
|22|**Frog Empirium**|Legowelt|**Floating Ether**|Gforce Software|
|23|**Hiphat Garden**|Legowelt|**Floating OnWaves**|Gforce Software|
|24|**Jnverness Synth Shop**|Legowelt|**FM Piano Elec’**|Gforce Software|
|25|**Magic Castle**|Legowelt|**FM Xylo**|Gforce Software|
|26|**Precinct Bass**|Legowelt|**Fmod Bass**|Gforce Software|
|27|**Saucy Bass**|Legowelt|**Guitar Patch**|Gforce Software|
|28|**Spring Neptunium**|Legowelt|**Icicle Warmth**|Gforce Software|
|29|**Thera Atlantis**|Legowelt|**Little EP Tines**|Gforce Software|
|30|**\^/**|Jerome Meunier|**Little Strike**|Gforce Software|
|31|**Alpine Lake**|Patricia Wolf|**Music Box**|Gforce Software|
|32|**Ambient Arp**|Patricia Wolf|**Oldie Mogie**|Gforce Software|
|33|**Basement**|Patricia Wolf|**OwWaa Pad**|Gforce Software|
|34|**Bathysphere**|Patricia Wolf|**OxOsc Sync**|Gforce Software|
|35|**Beneath the Wave**|Patricia Wolf|**Rich Pad**|Gforce Software|
|36|**déjà vu Feeling**|Patricia Wolf|**Silky Retro Syn**|Gforce Software|
|37|**Dream Baby**|Patricia Wolf|**Simple Pad**|Gforce Software|
|38|**Dub Organ**|Patricia Wolf|**Soft OB**|Gforce Software|
|39|**Eating Tape**|Patricia Wolf|**Space Organ**|Gforce Software|
|40|**Electro-static**|Patricia Wolf|**Spiritual Skies**|Gforce Software|
|41|**Erosion**|Patricia Wolf|**Syn Clav**|Gforce Software|
|42|**Exorcism**|Patricia Wolf|**Three Digi Bells**|Gforce Software|
|43|**Found Sound**|Patricia Wolf|**Tino Moo**|Gforce Software|
|44|**From the Stars**|Patricia Wolf|**Voxarrhh Vocal**|Gforce Software|
|45|**Golden Egg**|Patricia Wolf|**You 70s FunkyCat**|Gforce Software|
|46|**Guitar Distorted**|Patricia Wolf|**Zither Guitar FX**|Gforce Software|
|47|**Hammered Dulcimer**|Patricia Wolf|**Wurli ModW Vib**|Gforce Software|
|48|**Haunting Memory**|Patricia Wolf|**Arpy Lead**|Sandunes|
|49|**Heliocentric**|Patricia Wolf|**Brass Stitcher**|Sandunes|
|50|**Hovercraft**|Patricia Wolf|**Chamber Pipes**|Sandunes|
|51|**Kick & Toms**|Patricia Wolf|**Cosmic Lead**|Sandunes|
|52|**Lace Timbre**|Patricia Wolf|**Crystal Sky**|Sandunes|
|53|**Life as a bee**|Patricia Wolf|**Detroitich**|Sandunes|
|54|**Lost At Sea**|Patricia Wolf|**Digi Harmonium**|Sandunes|
|55|**Mirage**|Patricia Wolf|**French Horn Pad**|Sandunes|
|56|**Mission Complete**|Patricia Wolf|**Glassy Drops**|Sandunes|



**50**

---

## Page 51

|57|Secret Room|Patricia Wolf|Gluey Stab|Sandunes|
|---|---|---|---|---|
|58|**Silver Bamboo**|Patricia Wolf|**Griffyndor**|Sandunes|
|59|**Snake Charmer**|Patricia Wolf|**Mars Arp**|Sandunes|
|60|**Spiritual Path**|Patricia Wolf|**Phat n Low**|Sandunes|
|61|**Talking Ghosts**|Patricia Wolf|**Round Sub**|Sandunes|
|62|**Techno Utopia**|Patricia Wolf|**Rubber Leady**|Sandunes|
|63|**Teles**|Patricia Wolf|**Rubber Sub Sub**|Sandunes|
|64|**Time-Lapse**|Patricia Wolf|**Sharp Wash**|Sandunes|
|65|**Vanishing Point**|Patricia Wolf|**Steely Dran**|Sandunes|
|66|**Over8iased**|Peter Dyer|**Sub Arp234**|Sandunes|
|67|**ArtilleryBass**|Peter Dyer|**Tasty Chorder**|Sandunes|
|68|**AyeEyeGuy**|Peter Dyer|**Tubey Sub**|Sandunes|
|69|**Big Hyper**|Peter Dyer|**Wail Pad**|Sandunes|
|70|**FestaBass**|Peter Dyer|**Wood Pecker**|Sandunes|
|71|**FlintTinder**|Peter Dyer|**Wurli Alloy**|Sandunes|
|72|**Gleamers**|Peter Dyer|**Alpha Omega**|Inhalt|
|73|**Gray Havens**|Peter Dyer|**Animate4Harmny**|Inhalt|
|74|**HouseLoveOrgan**|Peter Dyer|**Classic Keys**|Inhalt|
|75|**KlyMaxx**|Peter Dyer|**Clavier Sync**|Inhalt|
|76|**KnockDown Bass**|Peter Dyer|**Cocteaul Choire1**|Inhalt|
|77|**Let’s Go Paisley**|Peter Dyer|**Cocteaul Choire2**|Inhalt|
|78|**MagneticBloom**|Peter Dyer|**Digital BodyBass**|Inhalt|
|79|**MeowMod**|Peter Dyer|**Fat Fifths**|Inhalt|
|80|**OpticalBurn**|Peter Dyer|**FM Bells**|Inhalt|
|81|**Origins**|Peter Dyer|**Gas,GrassOrBrass**|Inhalt|
|82|**PastelShores**|Peter Dyer|**Glacial Mood**|Inhalt|
|83|**PVC Kalimba**|Peter Dyer|**Harding Bass**|Inhalt|
|84|**Rewinder**|Peter Dyer|**LastTrain2Bass**|Inhalt|
|85|**StPeters2095**|Peter Dyer|**Linear Fifty**|Inhalt|
|86|**StringMachine**|Peter Dyer|**Liquid Rave Chrd**|Inhalt|
|87|**Supertanker**|Peter Dyer|**Mallelt Vox!**|Inhalt|
|88|**That’s Super**|Peter Dyer|**Midnight**|Inhalt|
|89|**Thumper**|Peter Dyer|**Neural Scanner**|Inhalt|
|90|**TimeBender**|Peter Dyer|**Orange Nightmare**|Inhalt|
|91|**Wow&Flutter**|Peter Dyer|**PleasureDome**|Inhalt|
|92|**WuvaaLova**|Peter Dyer|**PWM Pad**|Inhalt|
|93|**CommsErrorPad**|Tristan McGuire|**RadiophonicOrgan**|Inhalt|
|94|**EasterlyPlucks**|Tristan McGuire|**Risky Biz**|Inhalt|
|95|**StringSectionSwell**|Tristan McGuire|**StankFunk Bass**|Inhalt|
|96|**Woodwindesque**|Tristan McGuire|**Table Organ**|Inhalt|
|97|**Analog Dawn**|Enrico Cosimi|**Vox Humana A**|Inhalt|
|98|**Analog Kick MW**|Enrico Cosimi|**Vox Humana B**|Inhalt|
|99|**Analog Separatn**|Enrico Cosimi|**West Coast LPG**|Inhalt|
|100|**Analog Snare**|Enrico Cosimi|**EP Overdrive**|Loz Jackson|
|101|**Bass SubOsc**|Enrico Cosimi|**EP2**|Loz Jackson|
|102|**Bite Poly**|Enrico Cosimi|**EP4**|Loz Jackson|
|103|**Eighties Organ**|Enrico Cosimi|**LFO Bass**|Loz Jackson|
|104|**Eighties Brass**|Enrico Cosimi|**LFO Bass 2**|Loz Jackson|
|105|**Epic Sync LoopEG**|Enrico Cosimi|**LFO Bass 3**|Loz Jackson|
|106|**Ethernal FM**|Enrico Cosimi|**Organ**|Loz Jackson|
|107|**FM Chaos**|Enrico Cosimi|**Soft Organ**|Loz Jackson|
|108|**Game Over**|Enrico Cosimi|**Saw Bass**|Loz Jackson|
|109|**HardSync Lead**|Enrico Cosimi|**Space Lead**|Loz Jackson|
|110|**LFO No Arpeggio**|Enrico Cosimi|**10p Ice Pops**|Tim Mantle/Psalm37|
|111|**Mellow Lead**|Enrico Cosimi|**70’s NYC Jam**|Tim Mantle/Psalm37|
|112|**Pad 3SawDnsAftBP**|Enrico Cosimi|**Blockers**|Tim Mantle/Psalm37|
|113|**Pad Sawdense**|Enrico Cosimi|**Bounty by Grace**|Tim Mantle/Psalm37|
|114|**Power Fifth**|Enrico Cosimi|**Bronzer**|Tim Mantle/Psalm37|
|115|**Prog Lead**|Enrico Cosimi|**Catharsis**|Tim Mantle/Psalm37|
|116|**Ring Dyn Ambient**|Enrico Cosimi|**Cone Blown**|Tim Mantle/Psalm37|


**51**

---

## Page 52

|117|SingleTrig Bass|Enrico Cosimi|Dalston Dream|Tim Mantle/Psalm37|
|---|---|---|---|---|
|118|**Triangle Motion**|Enrico Cosimi|**Digi Bass Basics**|Tim Mantle/Psalm37|
|119|**Belmont Whip GIL**|Groundislava|**Elysian**|Tim Mantle/Psalm37|
|120|**Blue Dulcimer**|Groundislava|**Expansion Card**|Tim Mantle/Psalm37|
|121|**Crush Bass GIL**|Groundislava|**Hard Bowed**|Tim Mantle/Psalm37|
|122|**Faerie Ring GIL**|Groundislava|**Intimate Rotary**|Tim Mantle/Psalm37|
|123|**GIL’s Memories**|Groundislava|**it’s all Ours**|Tim Mantle/Psalm37|
|124|**Glassy Strider GIL**|Groundislava|**Maybe Too Cool**|Tim Mantle/Psalm37|
|125|**Light House GIL**|Groundislava|**Pluck your keys**|Tim Mantle/Psalm37|
|126|**Sendai GIL**|Groundislava|**Reminiscent**|Tim Mantle/Psalm37|
|127|**Sp. Beam Cannon**|Groundislava|**Shadow Industry**|Tim Mantle/Psalm37|


**52**

---

## Page 53

|Patch No.|Single Patches – Bank C|Col3|Single Patches – Bank D|Col5|
|---|---|---|---|---|
|**Patch No.**|**Patch Name**|**Created by**|**Patch Name**|**Created by**|
|0|**Ponderosa**|Legowelt|**Init Patch**||
|1|**Evening Light**|Legowelt|**Init Patch**||
|2|**Star Simulator**|Legowelt|**Init Patch**||
|3|**Telcom Splendor**|Legowelt|**Init Patch**||
|4|**Raw Deal**|Legowelt|**Init Patch**||
|5|**Sesqua Valley**|Legowelt|**Init Patch**||
|6|**Cobra Duobass**|Legowelt|**Init Patch**||
|7|**Nomad Ninja**|Legowelt|**Init Patch**||
|8|**Sequenchoco**|Legowelt|**Init Patch**||
|9|**Nam Flashback**|Legowelt|**Init Patch**||
|10|**Druid Music**|Legowelt|**Init Patch**||
|11|**Space Giraffe**|Legowelt|**Init Patch**||
|12|**Emerald Cascade**|Legowelt|**Init Patch**||
|13|**Seafax Museum**|Legowelt|**Init Patch**||
|14|**Memory X Bass**|Legowelt|**Init Patch**||
|15|**Marin Pad**|Legowelt|**Init Patch**||
|16|**Olympius**|Legowelt|**Init Patch**||
|17|**Spacejazz Ranger**|Legowelt|**Init Patch**||
|18|**Analog Speedo**|Legowelt|**Init Patch**||
|19|**Simple Things**|Legowelt|**Init Patch**||
|20|**British Ambient**|Legowelt|**Init Patch**||
|21|**Artic Liqorish**|Legowelt|**Init Patch**||
|22|**Ravens Jazz**|Legowelt|**Init Patch**||
|23|**Nite Critters**|Legowelt|**Init Patch**||
|24|**Feed Me Wavesap**|Legowelt|**Init Patch**||
|25|**Welsh Synthesis**|Legowelt|**Init Patch**||
|26|**Candy Rainfall**|Legowelt|**Init Patch**||
|27|**Bamoose Bass**|Legowelt|**Init Patch**||
|28|**Ondes Messianen**|Legowelt|**Init Patch**||
|29|**Silver Shamrock**|Legowelt|**Init Patch**||
|30|**Parapoly 8000**|Legowelt|**Init Patch**||
|31|**Wasabi Ghost**|Legowelt|**Init Patch**||
|32|**Sprinkle Stars**|Legowelt|**Init Patch**||
|33|**Rusty Soul**|Legowelt|**Init Patch**||
|34|**Tamboura Rays**|Legowelt|**Init Patch**||
|35|**Oxford Dreams**|Legowelt|**Init Patch**||
|36|**Ural Myst**|Legowelt|**Init Patch**||
|37|**Ambient Sockshop**|Legowelt|**Init Patch**||
|38|**Thera Tears**|Legowelt|**Init Patch**||
|39|**Eomius Belay**|Legowelt|**Init Patch**||
|40|**Fantasoba**|Legowelt|**Init Patch**||
|41|**Steadybass Flute**|Legowelt|**Init Patch**||
|42|**New Age Marina**|Legowelt|**Init Patch**||
|43|**Side By Side**|Legowelt|**Init Patch**||
|44|**Glory Jam**|Legowelt|**Init Patch**||
|45|**Radiance Of Lite**|Legowelt|**Init Patch**||
|46|**Big Splash Snug**|Legowelt|**Init Patch**||
|47|**Einstein Strand**|Legowelt|**Init Patch**||
|48|**TapeWave Infoop**|Legowelt|**Init Patch**||
|49|**Jezebel**|Legowelt|**Init Patch**||
|50|**Wyoming LSD**|Legowelt|**Init Patch**||
|51|**Rain Shadow VIP**|Legowelt|**Init Patch**||
|52|**Computer Day**|Legowelt|**Init Patch**||
|53|**Valaxtica**|Legowelt|**Init Patch**||
|54|**Manta Day**|Legowelt|**Init Patch**||
|55|**Hypno Envelope**|Legowelt|**Init Patch**||
|56|**Caramelbass**|Legowelt|**Init Patch**||
|57|**Nine Gates**|Legowelt|**Init Patch**||


**53**

---

## Page 54

|58|Alpensynposium|Legowelt|Init Patch|Col5|
|---|---|---|---|---|
|59|**Jimi Patch**|Legowelt|**Init Patch**||
|60|**Bodega Bay**|Legowelt|**Init Patch**||
|61|**Season 3 Bass**|Legowelt|**Init Patch**||
|62|**Duneman**|Legowelt|**Init Patch**||
|63|**Parapoly Saw 700**|Legowelt|**Init Patch**||
|64|**Analog Jazz EP**|Legowelt|**Init Patch**||
|65|**Starlooper**|Legowelt|**Init Patch**||
|66|**PennyWaffe Sa8**|Legowelt|**Init Patch**||
|67|**Napa Breeze**|Legowelt|**Init Patch**||
|68|**Synth Marmalade**|Legowelt|**Init Patch**||
|69|**Lion Figurine**|Legowelt|**Init Patch**||
|70|**Haddonfeld**|Legowelt|**Init Patch**||
|71|**Shetland Pony**|Legowelt|**Init Patch**||
|72|**Historical Orleo**|Legowelt|**Init Patch**||
|73|**Lizard Breath**|Legowelt|**Init Patch**||
|74|**Modestoharpsi**|Legowelt|**Init Patch**||
|75|**AeonBass**|Legowelt|**Init Patch**||
|76|**Sinistrone Soup**|Legowelt|**Init Patch**||
|77|**Fadango Vampy**|Legowelt|**Init Patch**||
|78|**Katjesdrop**|Legowelt|**Init Patch**||
|79|**Socour Overcast**|Legowelt|**Init Patch**||
|80|**Arparoma**|Legowelt|**Init Patch**||
|81|**Golden Age**|Legowelt|**Init Patch**||
|82|**South Pacifc**|Legowelt|**Init Patch**||
|83|**Desert Bus**|Legowelt|**Init Patch**||
|84|**Xenomurf**|Legowelt|**Init Patch**||
|85|**Icepalace**|Legowelt|**Init Patch**||
|86|**Wave Dew**|Legowelt|**Init Patch**||
|87|**Oxford Manor**|Legowelt|**Init Patch**||
|88|**Elvenmeadow**|Legowelt|**Init Patch**||
|89|**Majestic Wolharp**|Legowelt|**Init Patch**||
|90|**Grand CanyonPad**|Legowelt|**Init Patch**||
|91|**Moddervet**|Legowelt|**Init Patch**||
|92|**Island Astronomy**|Legowelt|**Init Patch**||
|93|**Rigoheim**|Legowelt|**Init Patch**||
|94|**Lazybass**|Legowelt|**Init Patch**||
|95|**Swamp Satyr**|Legowelt|**Init Patch**||
|96|**Americana**|Legowelt|**Init Patch**||
|97|**Dream Plants**|Legowelt|**Init Patch**||
|98|**Solarius**|Legowelt|**Init Patch**||
|99|**Hyperborian Orca**|Legowelt|**Init Patch**||
|100|**OxoAcid Oz**|Legowelt|**Init Patch**||
|101|**VipeBuzz Big**|Legowelt|**Init Patch**||
|102|**Atmy Synt**|Legowelt|**Init Patch**||
|103|**Edensynt Seq**|Legowelt|**Init Patch**||
|104|**Moondust**|Legowelt|**Init Patch**||
|105|**Oervogel**|Legowelt|**Init Patch**||
|106|**Emotional Wealth**|Legowelt|**Init Patch**||
|107|**Castles**|Legowelt|**Init Patch**||
|108|**Smolzazia pad**|Legowelt|**Init Patch**||
|109|**Square Galapagos**|Legowelt|**Init Patch**||
|110|**Faroer Ichiban**|Legowelt|**Init Patch**||
|111|**Trip Cat**|Legowelt|**Init Patch**||
|112|**Mystery Coast**|Legowelt|**Init Patch**||
|113|**Mixtur Trautoni**|Legowelt|**Init Patch**||
|114|**lima Lama**|Legowelt|**Init Patch**||
|115|**Ambi Sludge Pro**|Legowelt|**Init Patch**||
|116|**Sweet Acid Seq**|Legowelt|**Init Patch**||
|117|**Juniper**|Legowelt|**Init Patch**||


**54**

---

## Page 55

|118|Winter Shore|Legowelt|Init Patch|Col5|
|---|---|---|---|---|
|119|**QuicksilverPudi**|Legowelt|**Init Patch**||
|120|**Norycove Harpsi**|Legowelt|**Init Patch**||
|121|**LAQidayS**|Legowelt|**Init Patch**||
|122|**Lifespan 75**|Legowelt|**Init Patch**||
|123|**Niteowl**|Legowelt|**Init Patch**||
|124|**Millenia**|Legowelt|**Init Patch**||
|125|**TV Detective**|Legowelt|**Init Patch**||
|126|**Mesc Uni Drums**|Legowelt|**Init Patch**||
|127|**P.O. BOX Space**|Legowelt|**Init Patch**||


**55**

---

## Page 56

|Patch No.|Multi Patches – Bank A|Col3|Multi Patches – Bank B|Col5|
|---|---|---|---|---|
|**Patch No.**|**Patch Name**|**Created by**|**Patch Name**|**Created by**|
|0|**FM Singularity**|Gforce Software|**Dream Stance**|Alex Jann|
|1|**Buzzy Brass**|Enrico Cosimi|**Eighties Brass**|Enrico Cosimi|
|2|**Bored of Canada**|Gforce Software|**Portal**|Patricia Wolf|
|3|**Alluvial**|r Beny|**Movement Above**|Inhalt|
|4|**FM Bell Layer**|Inhalt|**FM Piano & Pad**|Enrico Cosimi|
|5|**Gas Valves**|Peter Dyer|**Cyanide Sister**|Peter Dyer|
|6|**Puzzlebox GIL**|Groundislava|**Expanding Heads**|Gforce Software|
|7|**Dream Gazing**|Tim Mantle / Psalm37|**Warehouse Shapes**|Tim Mantle / Psalm37|
|8|**Tape Choir**|Gforce Software|**Imperfect 5ths**|Gforce Software|
|9|**Infnite Power**|Inhalt|**Italo Split**|Inhalt|
|10|**Cornish Pie**|Legowelt|**Bell Ensemble**|Groundislava|
|11|**Dark Funk Haven**|Legowelt|**Bubble Skyline**|Groundislava|
|12|**Deep Sea Jazz**|Legowelt|**Claw Bass GIL**|Groundislava|
|13|**Desert Springs**|Legowelt|**Damp Night GIL**|Groundislava|
|14|**Donker Moraes**|Legowelt|**Dark Planet GIL**|Groundislava|
|15|**Film Noir**|Legowelt|**Dark Funk Heaven**|Groundislava|
|16|**Florida Mallsad**|Legowelt|**Full Spectrum**|Groundislava|
|17|**Flying Boards**|Legowelt|**Hand of Midas**|Groundislava|
|18|**Night Mood**|Legowelt|**Mossy Log GIL**|Groundislava|
|19|**Outer Aegis**|Legowelt|**Plasma Battery**|Groundislava|
|20|**Pattern Bay**|Legowelt|**Rift Stone GIL**|Groundislava|
|21|**Pensive Planets**|Legowelt|**Sparklizer GIL**|Groundislava|
|22|**Puppy Hotel**|Legowelt|**Stone Organ GIL**|Groundislava|
|23|**Saturated Hues**|Legowelt|**Temple Depths**|Groundislava|
|24|**SID PWM & Poly**|Legowelt|**Tube World GIL**|Groundislava|
|25|**Spacial Experts**|Legowelt|**Tunnel Bass GIL**|Groundislava|
|26|**Spirited Moose**|Legowelt|**Twilight GIL**|Groundislava|
|27|**Tape Delay Jazz**|Legowelt|**Visual Light GIL**|Groundislava|
|28|**Twirly Mallets**|Legowelt|**Warm Wind GIL**|Groundislava|
|29|**Vampirion**|Legowelt|**Abyssal**|r Beny|
|30|**Vetbass & Cosmos**|Legowelt|**Algae**|r Beny|
|31|**6 Osc Bass**|Gforce Software|**Aurora Pockets**|r Beny|
|32|**80s Electro**|Gforce Software|**Belloma**|r Beny|
|33|**Anointed Poly**|Gforce Software|**Carl’stapes**|r Beny|
|34|**Arp & Wavetable**|Gforce Software|**Cedar**|r Beny|
|35|**Arp Perc Pad**|Gforce Software|**Chrome Forest**|r Beny|
|36|**Arp Triplet**|Gforce Software|**City Maps**|r Beny|
|37|**Arps Everywhere**|Gforce Software|**Fjossa**|r Beny|
|38|**Bass & Pad Synth**|Gforce Software|**Glass Bird**|r Beny|
|39|**Bass/Wurly C#3**|Gforce Software|**Iguana and Bee**|r Beny|
|40|**Bell Waves**|Gforce Software|**Kaleidaharp**|r Beny|
|41|**Big (-_-) Poly**|Gforce Software|**Kitro**|r Beny|
|42|**Blades of Fire**|Gforce Software|**Opal**|r Beny|
|43|**ChimEPad**|Gforce Software|**Pond**|r Beny|
|44|**Dirty Wiper**|Gforce Software|**Rivulet**|r Beny|
|45|**Dub Keys**|Gforce Software|**Seasick**|r Beny|
|46|**Echo Keys**|Gforce Software|**Sea Song**|r Beny|
|47|**Epic Start**|Gforce Software|**Sequoia**|r Beny|
|48|**Film Score Epic**|Gforce Software|**To The Wind**|r Beny|
|49|**Formant Peaks**|Gforce Software|**Animus**|Peter Dyer|
|50|**Funk Split**|Gforce Software|**Big Dreams**|Peter Dyer|
|51|**Hi Ya Nisqatsi**|Gforce Software|**Bubble Maker**|Peter Dyer|
|52|**Humana Vox**|Gforce Software|**Candy Machine**|Peter Dyer|
|53|**I Hear U Jon**|Gforce Software|**Chop Saw**|Peter Dyer|
|54|**LA Saccharinth**|Gforce Software|**Cloud Cover**|Peter Dyer|
|55|**Loving Chord**|Gforce Software|**Coast Clavier**|Peter Dyer|
|56|**Loving The Arps**|Gforce Software|**Coasting**|Peter Dyer|
|57|**Lymphadenopathy**|Gforce Software|**Cookie Cilffs**|Peter Dyer|


**56**

---

## Page 57

|58|Mid C Pattern|Gforce Software|Cotton Candy|Peter Dyer|
|---|---|---|---|---|
|59|**Moody Pad**|Gforce Software|**Drift On**|Peter Dyer|
|60|**Noise Nirvana**|Gforce Software|**Easy Bop**|Peter Dyer|
|61|**NuovaChord**|Gforce Software|**Flight Path**|Peter Dyer|
|62|**Octaves & Fifths**|Gforce Software|**Floating Lanterns**|Peter Dyer|
|63|**Pad & Lead 1**|Gforce Software|**Foam Chord**|Peter Dyer|
|64|**Pad & Lead 2**|Gforce Software|**Goose Bumps**|Peter Dyer|
|65|**Phased Delight**|Gforce Software|**Gulf Winds**|Peter Dyer|
|66|**Pick a Pad**|Gforce Software|**Horizon Bounce**|Peter Dyer|
|67|**Plucka Bed**|Gforce Software|**Night Crime**|Peter Dyer|
|68|**Plucket Again**|Gforce Software|**Old Friends**|Peter Dyer|
|69|**PoWeR SiNthesist**|Gforce Software|**Pacifc By Way**|Peter Dyer|
|70|**Red Alert!**|Gforce Software|**Plunker**|Peter Dyer|
|71|**Refractions**|Gforce Software|**Pomp Comp**|Peter Dyer|
|72|**Ricochet Pad**|Gforce Software|**Power Suit**|Peter Dyer|
|73|**Rise & Flutter**|Gforce Software|**Pump up**|Peter Dyer|
|74|**Romford Tecno 90**|Gforce Software|**RAM Flow**|Peter Dyer|
|75|**Seismic Lights**|Gforce Software|**Researching**|Peter Dyer|
|76|**Shifting Sands**|Gforce Software|**Riggles**|Peter Dyer|
|77|**Space Cadet**|Gforce Software|**Shoreline**|Peter Dyer|
|78|**Spiked**|Gforce Software|**Social Funk**|Peter Dyer|
|79|**Strings Octaves**|Gforce Software|**Speedish House**|Peter Dyer|
|80|**Stringy Fifths**|Gforce Software|**Start Screen**|Peter Dyer|
|81|**Super Chord**|Gforce Software|**The Forge**|Peter Dyer|
|82|**Super Nasty Lead**|Gforce Software|**The Orishas**|Peter Dyer|
|83|**Sync Clasher**|Gforce Software|**Tight Walk**|Peter Dyer|
|84|**Triumphant**|Gforce Software|**Vice City**|Peter Dyer|
|85|**Tyrell Brass**|Gforce Software|**Wild & Loose**|Peter Dyer|
|86|**Uni Bass & Poly**|Gforce Software|**Zeus Fanfare**|Peter Dyer|
|87|**Wind Staccato**|Gforce Software|**Alva Bass Pile**|Inhalt|
|88|**Windy Pad**|Gforce Software|**PolySummit Choir**|Inhalt|
|89|**Wurly\Lead C3**|Gforce Software|**Astral Duves**|Inhalt|
|90|**80s String Unit**|Tim Mantle / Psalm37|**Big EP**|Inhalt|
|91|**Back Catalogue**|Tim Mantle / Psalm37|**Big Romance**|Inhalt|
|92|**Brass for Days!**|Tim Mantle / Psalm37|**Cabaret Vol Spit**|Inhalt|
|93|**Carrillon Matron**|Tim Mantle / Psalm37|**City of Monica**|Inhalt|
|94|**Champs-Elysees**|Tim Mantle / Psalm37|**Cocteau1 Hour**|Inhalt|
|95|**Clingerclang**|Tim Mantle / Psalm37|**Covenant Split**|Inhalt|
|96|**Coming Abroad**|Tim Mantle / Psalm37|**Digistalgia Splt**|Inhalt|
|97|**Discovery Layer**|Tim Mantle / Psalm37|**Dueling Arps**|Inhalt|
|98|**Dust Down Love**|Tim Mantle / Psalm37|**Dyno My Piano**|Inhalt|
|99|**EP P37**|Tim Mantle / Psalm37|**FM AM Split**|Inhalt|
|100|**Escape Pod**|Tim Mantle / Psalm37|**FSOLos Angeles**|Inhalt|
|101|**Faux Century**|Tim Mantle / Psalm37|**Instant Intro**|Inhalt|
|102|**For Her Genius**|Tim Mantle / Psalm37|**Last Train**|Inhalt|
|103|**Fruit Picking**|Tim Mantle / Psalm37|**Liquid Stack**|Inhalt|
|104|**Fully Loaded**|Tim Mantle / Psalm37|**Massiv Strings**|Inhalt|
|105|**Grey’s Abduction**|Tim Mantle / Psalm37|**McBride’s Cave**|Inhalt|
|106|**Guilty Pleasures**|Tim Mantle / Psalm37|**Mifgr’s Split**|Inhalt|
|107|**Hardcore Score**|Tim Mantle / Psalm37|**Neologic split**|Inhalt|
|108|**Legacy Lead**|Tim Mantle / Psalm37|**Orange Chariots**|Inhalt|
|109|**Long Gone**|Tim Mantle / Psalm37|**Oranic**|Inhalt|
|110|**Mercury**|Tim Mantle / Psalm37|**Phantasia 2020**|Inhalt|
|111|**Nil by Mouth**|Tim Mantle / Psalm37|**Pleasure Quest**|Inhalt|
|112|**Panuc Stations**|Tim Mantle / Psalm37|**Pop Composer**|Inhalt|
|113|**Regeneration**|Tim Mantle / Psalm37|**Recombinant Mlab**|Inhalt|
|114|**Remember Fusion**|Tim Mantle / Psalm37|**Start The Rave**|Inhalt|
|115|**Revised Hope**|Tim Mantle / Psalm37|**Sunrise Summit**|Inhalt|
|116|**Slick & Trick**|Tim Mantle / Psalm37|**Thorny**|Inhalt|
|117|**Small Town USA**|Tim Mantle / Psalm37|**Unicorn Dreams**|Inhalt|


**57**

---

## Page 58

|118|Spectral Helper|Tim Mantle / Psalm37|Uno Linear Split|Inhalt|
|---|---|---|---|---|
|119|**Stock-Ex Montage**|Tim Mantle / Psalm37|**Violated**|Inhalt|
|120|**Such a Charmer!**|Tim Mantle / Psalm37|**Voice of Summit**|Inhalt|
|121|**That’s the Jazz!**|Tim Mantle / Psalm37|**Vurtual Rain**|Inhalt|
|122|**The Good Stuff**|Tim Mantle / Psalm37|**Warm Games**|Inhalt|
|123|**Them Feels**|Tim Mantle / Psalm37|**West End Split**|Inhalt|
|124|**Toe Tap 2000**|Tim Mantle / Psalm37|**InTheGloaming**|Tristan McGuire|
|125|**Find And Forget**|Tim Mantle / Psalm37|**Kosmic Hope**|Alex Jann|
|126|**Was it a Dream**|Tim Mantle / Psalm37|**Strung Out**|Alex Jann|
|127|**We Must Hide!**|Tim Mantle / Psalm37|**Zen Orbit**|Alex Jann|


**58**

---

## Page 59

|Patch No.|Multi Patches – Bank C|Col3|Multi Patches – Bank D|Col5|
|---|---|---|---|---|
|**Patch No.**|**Patch Name**|**Created by**|**Patch Name**|**Created by**|
|0|**Alchemy**|Patricia Wolf|**Init Multi**||
|1|**Anthromorphize**|Patricia Wolf|**Init Multi**||
|2|**Anticipation**|Patricia Wolf|**Init Multi**||
|3|**Aquatic Paridise**|Patricia Wolf|**Init Multi**||
|4|**Aurora Borealis**|Patricia Wolf|**Init Multi**||
|5|**Cascade**|Patricia Wolf|**Init Multi**||
|6|**Chasm**|Patricia Wolf|**Init Multi**||
|7|**Childhood Memory**|Patricia Wolf|**Init Multi**||
|8|**Chimera**|Patricia Wolf|**Init Multi**||
|9|**Clandestine**|Patricia Wolf|**Init Multi**||
|10|**Cloud Hopping**|Patricia Wolf|**Init Multi**||
|11|**Clouds Pass By**|Patricia Wolf|**Init Multi**||
|12|**Crystal Lattice**|Patricia Wolf|**Init Multi**||
|13|**Day Dream**|Patricia Wolf|**Init Multi**||
|14|**Degraded Tape**|Patricia Wolf|**Init Multi**||
|15|**Desert Sunset**|Patricia Wolf|**Init Multi**||
|16|**Electric Company**|Patricia Wolf|**Init Multi**||
|17|**Euphoria**|Patricia Wolf|**Init Multi**||
|18|**Fairyland**|Patricia Wolf|**Init Multi**||
|19|**Falling Water**|Patricia Wolf|**Init Multi**||
|20|**frst Kiss**|Patricia Wolf|**Init Multi**||
|21|**First Saw You**|Patricia Wolf|**Init Multi**||
|22|**Fond Memory**|Patricia Wolf|**Init Multi**||
|23|**Frozen Lake**|Patricia Wolf|**Init Multi**||
|24|**If You Believe**|Patricia Wolf|**Init Multi**||
|25|**In Your Head**|Patricia Wolf|**Init Multi**||
|26|**Introspection**|Patricia Wolf|**Init Multi**||
|27|**Ionic Bond**|Patricia Wolf|**Init Multi**||
|28|**Lady Bug**|Patricia Wolf|**Init Multi**||
|29|**Last Dance**|Patricia Wolf|**Init Multi**||
|30|**Longing**|Patricia Wolf|**Init Multi**||
|31|**Magic Pool**|Patricia Wolf|**Init Multi**||
|32|**Magic Sword**|Patricia Wolf|**Init Multi**||
|33|**Memory**|Patricia Wolf|**Init Multi**||
|34|**Mercury**|Patricia Wolf|**Init Multi**||
|35|**Metal Music**|Patricia Wolf|**Init Multi**||
|36|**Molten Core**|Patricia Wolf|**Init Multi**||
|37|**Moonlit Lake**|Patricia Wolf|**Init Multi**||
|38|**Morning Light**|Patricia Wolf|**Init Multi**||
|39|**Noble Cause**|Patricia Wolf|**Init Multi**||
|40|**Obstacle**|Patricia Wolf|**Init Multi**||
|41|**Quiet Guitar**|Patricia Wolf|**Init Multi**||
|42|**Racing Dolphins**|Patricia Wolf|**Init Multi**||
|43|**Rock Face**|Patricia Wolf|**Init Multi**||
|44|**Scrambled**|Patricia Wolf|**Init Multi**||
|45|**Secret Meeting**|Patricia Wolf|**Init Multi**||
|46|**Secret Mission**|Patricia Wolf|**Init Multi**||
|47|**Shimmer**|Patricia Wolf|**Init Multi**||
|48|**Snowy Owl**|Patricia Wolf|**Init Multi**||
|49|**Soaring**|Patricia Wolf|**Init Multi**||
|50|**Star Gazing**|Patricia Wolf|**Init Multi**||
|51|**Strong Along**|Patricia Wolf|**Init Multi**||
|52|**Sundown Arp**|Patricia Wolf|**Init Multi**||
|53|**Suspense**|Patricia Wolf|**Init Multi**||
|54|**The Weaver**|Patricia Wolf|**Init Multi**||
|55|**Tranquil Water**|Patricia Wolf|**Init Multi**||
|56|**Tundra**|Patricia Wolf|**Init Multi**||
|57|**Urban Decay**|Patricia Wolf|**Init Multi**||


**59**

---

## Page 60

|58|Water Dragon|Patricia Wolf|Init Multi|Col5|
|---|---|---|---|---|
|59|**Wild Horses**|Patricia Wolf|**Init Multi**||
|60|**Windswept**|Patricia Wolf|**Init Multi**||
|61|**Winged Migration**|Patricia Wolf|**Init Multi**||
|62|**Call and Action DN**|Danny Nugent|**Init Multi**||
|63|**Aggro Poly**|Enrico Cosimi|**Init Multi**||
|64|**Altered Arpeggio**|Enrico Cosimi|**Init Multi**||
|65|**Altered State**|Enrico Cosimi|**Init Multi**||
|66|**Arp & SyncLead**|Enrico Cosimi|**Init Multi**||
|67|**Bass & MellwLead**|Enrico Cosimi|**Init Multi**||
|68|**Bass & Organ**|Enrico Cosimi|**Init Multi**||
|69|**Bass & Pad**|Enrico Cosimi|**Init Multi**||
|70|**Bass & Prog Lead**|Enrico Cosimi|**Init Multi**||
|71|**Big Stab**|Enrico Cosimi|**Init Multi**||
|72|**Bouncing Pad**|Enrico Cosimi|**Init Multi**||
|73|**Bravo Delta Arp**|Enrico Cosimi|**Init Multi**||
|74|**Charlie & Pad**|Enrico Cosimi|**Init Multi**||
|75|**Charlie Delta 2Arp**|Enrico Cosimi|**Init Multi**||
|76|**Dawn**|Enrico Cosimi|**Init Multi**||
|77|**Deceleration**|Enrico Cosimi|**Init Multi**||
|78|**Dirdir**|Enrico Cosimi|**Init Multi**||
|79|**Drone Arpeggio**|Enrico Cosimi|**Init Multi**||
|80|**DynaDecelerated**|Enrico Cosimi|**Init Multi**||
|81|**Epic**|Enrico Cosimi|**Init Multi**||
|82|**FM Percuss Pad**|Enrico Cosimi|**Init Multi**||
|83|**Frozen Motion**|Enrico Cosimi|**Init Multi**||
|84|**Karabas**|Enrico Cosimi|**Init Multi**||
|85|**Kick & Snare**|Enrico Cosimi|**Init Multi**||
|86|**Layer Bass**|Enrico Cosimi|**Init Multi**||
|87|**Layer Pad**|Enrico Cosimi|**Init Multi**||
|88|**Moving Stab**|Enrico Cosimi|**Init Multi**||
|89|**Nigth Time**|Enrico Cosimi|**Init Multi**||
|90|**Out There**|Enrico Cosimi|**Init Multi**||
|91|**Separated Octave**|Enrico Cosimi|**Init Multi**||
|92|**Seq Friendly**|Enrico Cosimi|**Init Multi**||
|93|**Silk Pad**|Enrico Cosimi|**Init Multi**||
|94|**The Chase**|Enrico Cosimi|**Init Multi**||
|95|**Two Friends**|Enrico Cosimi|**Init Multi**||
|96|**Window Tears**|Chris Calcutt - aka CALC|**Init Multi**||
|97|**Leave The Latch**|Chris Calcutt - aka CALC|**Init Multi**||
|98|**Bass Chords**|Chris Calcutt - aka CALC|**Init Multi**||
|99|**Bubbling Vista**|Chris Calcutt - aka CALC|**Init Multi**||
|100|**Wooden Bridge**|Chris Calcutt - aka CALC|**Init Multi**||
|101|**Sustenance**|Chris Calcutt - aka CALC|**Init Multi**||
|102|**Pree Yrself**|Chris Calcutt - aka CALC|**Init Multi**||
|103|**Mechanical Pill**|Chris Calcutt - aka CALC|**Init Multi**||
|104|**Fuzzy Logic**|Chris Calcutt - aka CALC|**Init Multi**||
|105|**Instant Darkroom**|Chris Calcutt - aka CALC|**Init Multi**||
|106|**Bastian Machine**|Chris Calcutt - aka CALC|**Init Multi**||
|107|**Not Really Brass**|Chris Calcutt - aka CALC|**Init Multi**||
|108|**Smoke The Pipe**|Chris Calcutt - aka CALC|**Init Multi**||
|109|**80s Rolled Sleev**|Chris Calcutt - aka CALC|**Init Multi**||
|110|**Split Creamola**|Chris Calcutt - aka CALC|**Init Multi**||
|111|**Crustacian**|Chris Calcutt - aka CALC|**Init Multi**||
|112|**Gristling Throb**|Chris Calcutt - aka CALC|**Init Multi**||
|113|**Fresh Milk**|Chris Calcutt - aka CALC|**Init Multi**||
|114|**Wired Harmonium**|Chris Calcutt - aka CALC|**Init Multi**||
|115|**Tree Lined Walk**|Chris Calcutt - aka CALC|**Init Multi**||
|116|**Slow Arp DN**|Danny Nugent|**Init Multi**||
|117|**Puhu**|Jerome Meunier|**Init Multi**||


**60**
