## Overview
Robert Murray-Smith converts his previously demonstrated "Perpetual Wedge" gear mechanism (with a 60:1 ratio) into a functional clock by combining it with a 60 RPM DC motor, a cycloid gear stage, and bevel gears. He walks through the full assembly process, explaining how each gear stage drives the second, minute, and hour hands. The video concludes by acknowledging the clock lacks accurate motor control — identified as the next topic in the series.

## Key Topics
- Recap of the Perpetual Wedge mechanism and its 60:1 gear ratio
- Using a 60 RPM DC motor as the clock's time base (1 rotation = 1 second)
- Comparison of gear types: planetary gears (4–8:1), cycloid drives (10–20:1), and Perpetual wedge (up to 100:1)
- Designing a cycloid (epicycloid) gear stage for a 12:1 ratio to drive the hour hand
- Correcting hand rotation direction using bevel gears as an idler stage
- Full step-by-step physical assembly of the clock mechanism
- Noise issues from rubbing surfaces and the absence of bearings
- The missing "control mechanism" for accurate timekeeping, previewing a future video on motor control

## Materials and Chemicals Mentioned
- 3D-printed PLA parts (implied, printed on a home printer)
- 60 RPM DC motor (6V, sourced from Amazon)
- 4-battery box with on/off switch (6V power supply)
- Glue (used to fix cams, axles, bevel gear cage, and feet)
- 3mm washer

## Techniques and Methods
- 3D printing of gears, cams, discs, cages, and clock face components (designed in TinkerCAD)
- Cycloid/epicycloid gear generation using a dedicated program (K=12 lobes, R2=0.5, 13 pins on pin disc)
- Sanding printed cycloid gear to smooth TinkerCAD's 200-iteration resolution limit
- Using bevel gears as an inline idler to reverse minute-hand rotation direction
- Assembly with press-fit shafts, glued axles, and free-rotating gears
- Swapping motor wire polarity to set rotation direction

## Notable Timestamps
- `[00:08]` — Introduction: recap of Perpetual Wedge and motivation for 60:1 ratio clock
- `[00:34]` — 60 RPM motor introduced; explains why 60 RPM maps to 1 revolution per second
- `[01:58]` — Comparison of gear ratio ranges: planetary, cycloid, and Perpetual wedge
- `[03:05]` — Cycloid gear design for 12:1 hour-hand ratio; TinkerCAD parameters explained
- `[04:20]` — Problem of hand rotation direction identified; bevel gear solution introduced
- `[05:15]` — Bevel gear cage assembly walkthrough
- `[06:00]` — Full clock assembly sequence begins
- `[09:22]` — Motor attachment and wiring described
- `[10:10]` — Clock powered on for the first time (with laughter)
- `[10:28]` — Post-demo observations: noise from rubbing surfaces, need for bearings
- `[10:41]` — Identifies missing component: accurate motor control; previews next video

## Robert's Own Replies
- **Motor sourcing:** Just get any 60 RPM motor and adjust the hole size in the mount to fit — the exact model doesn't matter much.
- **Power supply:** The motor runs off a battery, so mains voltage fluctuations are irrelevant.
- **Noise/bearings:** He is actively working on a quieter version; adding bearings is endorsed as a great improvement idea.
- **Design philosophy:** He 3D prints everything purely to demonstrate the concept — there are many valid ways to build it, and alternatives (e.g. cardboard) would work too.
- **Motor control follow-up:** Confirmed a video on controlling the motor would be published on the following Friday.
- **Clock face idea:** He liked a commenter's idea of having the clock face itself move.