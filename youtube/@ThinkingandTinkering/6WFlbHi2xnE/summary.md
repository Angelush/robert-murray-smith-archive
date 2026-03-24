## Overview
Robert Murray-Smith provides a beginner-friendly introduction to using an oscilloscope, walking through how to connect probes, adjust voltage and time resolution controls, and use triggering. The video concludes with a practical debugging demonstration using a microcontroller and transistor circuit, showing why dual-channel measurement and proper grounding are essential.

## Key Topics
- What an oscilloscope displays (voltage vs. time)
- Connecting probes and understanding the ground reference
- Adjusting voltage resolution (volts/division) and time base (time/division)
- Storage mode vs. non-storage mode
- Triggering: auto-trigger and manual trigger level control
- Measuring a 24V AC transformer output and verifying with RMS calculation
- Dual-channel measurement for circuit debugging
- Importance of common ground between circuits
- Comparing vintage vs. modern oscilloscopes (Rigol DS1074Z)
- Buying advice for vintage oscilloscopes

## Materials and Chemicals Mentioned
- None mentioned.

## Techniques and Methods
- Connecting oscilloscope probes to a DC power supply to demonstrate voltage display
- Adjusting volts/division to scale signals on-screen
- Adjusting time/division (time base) to resolve slow and fast signals
- Using storage mode to capture slow waveforms
- Manual trigger level adjustment to stabilize a periodic waveform
- Estimating signal frequency by counting cycles across a known time window
- Peak-to-peak voltage measurement and RMS conversion (`V_peak-to-peak / 2√2`)
- Dual-channel simultaneous measurement to correlate input and output signals
- Using the hold/store function to freeze a trace for analysis
- Debugging a microcontroller–transistor–LED circuit by identifying a missing common ground

## Notable Timestamps
- `[00:03]` — Introduction: scope of the video (connecting probes, dials, triggering)
- `[00:34]` — Overview of the oscilloscope hardware and screen axes (voltage vs. time)
- `[02:45]` — Connecting probe to a DC power supply; demonstrating voltage display
- `[05:44]` — Time base control explained; demonstrating slow scan (5 s/cm)
- `[07:43]` — Storage oscilloscope mode explained and demonstrated
- `[09:05]` — Connecting to a 24V AC transformer; displaying a 50 Hz sine wave
- `[10:33]` — Triggering explained and demonstrated with the AC waveform
- `[12:57]` — Measuring peak-to-peak voltage and verifying against multimeter RMS reading (28.8 V)
- `[15:05]` — Dual-channel debugging demo: microcontroller driving LEDs via a transistor
- `[19:23]` — Problem identified: missing common ground between driver and output circuits
- `[19:44]` — Fix applied (tying grounds together); LEDs begin blinking correctly
- `[22:34]` — Modern oscilloscope (Rigol DS1074Z) comparison; controls are analogous
- `[23:49]` — Buying tips: prioritise storage scope, then highest bandwidth available

## Robert's Own Replies
Robert left two brief replies in the comments ("cheers mate"), both simply thanking commenters. No technical clarifications or follow-up insights were added.