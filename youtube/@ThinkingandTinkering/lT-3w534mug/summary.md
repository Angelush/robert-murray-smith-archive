## Overview
Robert Murray-Smith explains the universal control electronics used for high-temperature devices such as kilns, filament extruders, hot plates, and injection molders. He walks through the five core components needed and how to wire them together safely, demonstrating with a real injection molding machine he refurbished. The key takeaway is that all these machines share the same simple wiring scheme, enabling cheap and effective upgrades of old equipment.

## Key Topics
- Why direct switching of mains voltage is unsafe and how to avoid it
- The heating element: types, forms, and how to make your own
- The Solid State Relay (SSR/SCR) as a low-voltage-controlled mains switch
- K-type thermocouples as temperature sensors
- PID/PIT controller units: pin wiring (pins 1, 2, 4, 5, 9, 10)
- Using Ohm's law to calculate resistance, current draw, and appropriate voltage
- Upgrading old machinery (kilns, injection molders) cheaply with modern control electronics
- Cost comparison: refurbished kiln for ~£250 vs. £5,000 new

## Materials and Chemicals Mentioned
- **Kanthal wire** — resistance wire used for kiln heating elements, wound into coils
- **Nichrome wire** — resistance wire used in kilns, hot presses, bag sealers, and foam cutters
- **Mica** — substrate around which nichrome is wound in cartridge heaters
- **Ceramic** — used as top/bottom cladding on flat plate heating elements

## Techniques and Methods
- Winding resistance wire into a coil to form a DIY heating element
- Using Ohm's law to size wire gauge and calculate amp draw for a given voltage
- Wiring a double-pole manual switch for both live and neutral
- Connecting a K-type thermocouple into pins 9 & 10 of a PIT controller
- Wiring the SSR control pins (DC 3–32 V) to pins 4 & 5 of the PIT controller (plus-to-plus, minus-to-minus)
- Wiring mains live/neutral through the manual switch into pins 1 & 2 of the PIT controller
- Routing mains through the SSR output to one leg of the heating element; neutral directly to the other leg
- Replacing legacy variable-resistor temperature control with closed-loop digital PID control

## Notable Timestamps
- `[00:15]` — Introduction: work with local schools and receipt of loaned equipment from King's School Canterbury
- `[01:08]` — Motivation: Robert regularly refurbishes old high-temperature machinery with modern control electronics
- `[01:44]` — Overview of the five core components (three of which are switches)
- `[02:20]` — Resistance wire explained: Kanthal and nichrome, coil construction
- `[03:31]` — Heating element types shown: bag-sealer strip, cartridge, band heater, flat ceramic plate
- `[06:39]` — Solid State Relay (SSR) introduced: four pins, low-voltage DC input switches mains output
- `[07:56]` — K-type thermocouple explained: two dissimilar metals, linear voltage output, 100–1300 °C range
- `[09:32]` — PIT controller units: cheap (~£2–5), pin layout, which pins to use
- `[10:31]` — Wiring summary: pins 1 & 2 (mains supply), 9 & 10 (thermocouple), 4 & 5 (SSR control)
- `[13:37]` — Internal wiring of the injection molder shown in practice
- `[17:25]` — Final result: injection molder with digital temperature control; kiln built for ~£250 vs. £5,000 new

## Robert's Own Replies
- Expressed agreement with a commenter about PIT/SSR controllers: confirms he uses them constantly, finding them **quick, easy, and reliable with pretty good accuracy**.