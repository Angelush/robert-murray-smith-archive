## Overview
Robert Murray-Smith demonstrates how to build a basic stylophone using conductive ink painted onto paper, centred around a 555 timer circuit. The ink acts as both circuit traces and a passive resistive element (~10 kΩ), with a wire stylus varying resistance along a painted line to change pitch. He concludes that the device works but needs an LM386 amplifier stage to reach a useful volume, and hints at a full paper-based stylophone as the next step.

## Key Topics
- Converting a 555 timer schematic into a painted paper circuit
- Using conductive ink as "cold solder" to attach SMD components
- Using masking tape to achieve fine painted lines around tiny surface-mount components
- Painting a passive resistor element directly onto paper using conductive ink
- Using a wire stylus along a resistive ink strip to vary pitch (stylophone principle)
- Plans to add an LM386 amplifier for greater volume

## Materials and Chemicals Mentioned
- **Conductive ink** — used as circuit traces, passive resistor (~10 kΩ), and cold-solder adhesive for components
- **Paper / card** — substrate for the circuit
- **Masking tape** — used to mask areas for fine painting around small components

## Techniques and Methods
- **Cold soldering** — applying conductive ink as a blob to adhere and electrically connect SMD components without heat
- **Masking-tape stencilling** — applying and peeling masking tape in successive layers to paint fine circuit lines around very small components
- **Schematic-to-layout conversion** — manually planning a non-crossing, compact trace layout before painting
- **Variable resistance via stylus** — touching a wire to different points along a painted resistive strip to change tone

## Notable Timestamps
- `[00:07]` — Introduction; announces plan to build a 555-timer-based noisemaker using conductive ink
- `[00:31]` — Explains how the ink acts as cold solder for electronic components
- `[01:04]` — Describes the 555 pin connections used (pins 1, 2, 3, 6, 8) and 9 V supply
- `[02:16]` — Reveals the planned circuit layout drawing; explains piezo and variable resistor connections
- `[04:00]` — Explains masking-tape technique for painting fine lines around the tiny SMD chip
- `[05:28]` — Shows the completed painted circuit (version 2) with an ink-painted passive resistor element
- `[06:33]` — Demonstrates the finished assembled circuit; cold-soldered NE555 and piezo in place
- `[07:00]` — Live demo: pitch changes as stylus moves along the resistive strip
- `[07:33]` — Notes the output is too quiet; proposes adding an LM386 amplifier chip as next step

## Robert's Own Replies
- **Amplifier wiring detail:** Connect from pin 3 of the 555 through a 0.1 µF capacitor to a 10 kΩ pot; ground one end of the pot and wire the wiper to pin 3 of an LM386. The stylus also connects to pin 3.
- **Durability:** The circuit has survived a couple of days of handling; for a more permanent build he recommends a tougher substrate and a spot of glue on components (he says he'll "steal" the idea from a commenter).
- **Electroplating potential:** The ink was originally developed for electroplating organic substrates, so it is capable of being plated. He acknowledges the challenge of ohmic contact with semiconductor material as the main barrier to printing diodes, but finds the concept of fully printed electronics exciting.
- **Substrate suggestion:** Floats the idea of painting circuits onto plastic for better durability.
- **Drawing use:** The ink works with a dip pen, but is not suitable for general drawing purposes beyond that.