## Overview
Robert Murray-Smith demonstrates how to build a MIDI musical instrument using an Arduino Uno, piezoelectric transducers, and hand-painted conductive ink circuits on card. The device converts physical taps on piezo elements into MIDI signals, which can be routed into music software like GarageBand or FL Studio. The key insight is that passive components like resistors can be fabricated by painting and scraping conductive ink, making the entire circuit buildable without soldering.

## Key Topics
- Building a MIDI instrument from scratch using an Arduino Uno
- Using conductive ink to paint circuits and passive components onto paper/card
- Connecting piezoelectric transducers as sensor pads
- Routing MIDI output into music software (GarageBand, FL Studio, MS Wave Synthesizer)
- Techniques for connecting jumper wires to ink-painted circuits without soldering

## Materials and Chemicals Mentioned
- **Conductive ink** — painted onto card to form circuit traces, resistors, and connection points
- **Piezoelectric transducers (piezos)** — cheap discs used as sensor/strike pads; described as a few pence each
- **Masking tape** — used as a painting mask to define resistor geometry and as an insulating bridge over piezo discs
- **Ordinary glue** — used to attach piezo discs to the card
- **Arduino Uno** — the microcontroller that reads analog inputs and outputs MIDI over USB

## Techniques and Methods
- **Painted resistor fabrication** — applying masking tape as a stencil, painting ink lines, peeling the tape, then scraping with a blade to tune resistance to ~1 MΩ
- **Cold solder joints** — applying a spot of conductive ink to make electrical contact with piezo disc terminals
- **Needle-pierce wire attachment** — stabbing a needle through the card at connection points and inserting jumper cables directly into the holes
- **Analog input noise suppression** — connecting unused Arduino analog pins to ground to prevent spurious signals
- **Web-based Arduino IDE** — using the online IDE to copy, paste, and upload the MIDI sketch from GitHub

## Notable Timestamps
- `[00:15]` — Introduction and live demo of the instrument making a clicking MIDI sound
- `[00:37]` — Explanation of the signal chain: piezo → Arduino → MS Wave Synthesizer → amplifier → speaker
- `[01:43]` — Walkthrough of the physical connections and how jumper cables attach via needle holes
- `[02:29]` — Describes sourcing the Arduino sketch from GitHub and uploading via USB
- `[03:25]` — Reveals the circuit is made with conductive ink; explains painted 1 MΩ resistors
- `[04:13]` — Lists all materials needed to build the instrument
- `[04:32]` — Step-by-step fabrication begins: laying masking tape for resistor stencils
- `[05:35]` — Painting ink lines over the tape stencil
- `[07:01]` — Peeling tape to reveal resistor lines; joining pairs with a thin brush
- `[07:39]` — Painting the ground line
- `[08:07]` — Making signal attachment points and poking needle holes for jumper wires
- `[08:41]` — Gluing piezo discs onto the circuit, copper side down
- `[09:23]` — Bridging over the piezo discs with masking tape strips
- `[10:23]` — Painting ink over the masking tape bridges to complete the signal traces
- `[11:00]` — Applying ink spots to the piezo silver and copper contacts (cold solder)
- `[11:36]` — Final assembled board shown; recap of signal and ground lines
- `[12:40]` — Closing remarks and links to ink and Arduino sketch

## Robert's Own Replies
No author replies found.