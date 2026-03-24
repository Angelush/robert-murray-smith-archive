## Overview
Robert Murray-Smith presents a 3D-printed working model of a Torsen differential that he designed in TinkerCAD, explaining both its mechanical principles and demonstrating its operation. The video walks through why the worm-gear-based design is self-locking under normal drive but allows differential action during cornering, and why this makes it elegant and effective for traction control. STL files are made available for viewers to print their own.

## Key Topics
- What a Torsen differential is and why it's mechanically elegant
- The worm gear principle and why it cannot be back-driven
- How the differential achieves relative motion between wheels when cornering (using a change-of-reference-frame explanation)
- How differentials can both split and combine power
- Component breakdown: sun gears (acting as worm gears), helical gears, spur gears for synchronization, carriage, flanges
- Step-by-step assembly of the 3D-printed model
- Behavior under straight-line drive, cornering, and wheel-stuck scenarios
- Torque-biasing advantage over conventional open differentials

## Materials and Chemicals Mentioned
- None mentioned. (The model is 3D-printed plastic; no specific filament type is discussed.)

## Techniques and Methods
- 3D modelling in TinkerCAD
- FDM 3D printing of individual gear components
- Two-piece print-and-glue assembly technique for helical gear teeth (to preserve tooth quality)
- Pin-and-circlip assembly for securing planet gears in carriage
- Adhesive bonding of bevel gear to flange and final frame assembly

## Notable Timestamps
- `[00:08]` — Introduction to the Torsen differential model; STL files announced
- `[00:30]` — Explanation of the worm gear principle and why it cannot be back-driven
- `[01:04]` — How engine power locks the worm gears and drives the output flanges
- `[01:33]` — Relativity-of-motion argument used to explain differential action during cornering
- `[02:44]` — Differentials can combine power as well as split it
- `[03:07]` — Detailed look at the TinkerCAD model; components identified
- `[03:36]` — Sun gear, helical planet gears, and spur synchronising gears explained
- `[04:33]` — Assembly walkthrough begins
- `[06:15]` — Completed model demonstrated; straight-line and opposite-rotation tests
- `[07:05]` — Cornering explained via change of reference frame (stand on the slower wheel)
- `[08:22]` — Stuck-wheel scenario: torque transfers to stuck wheel rather than spinning free wheel

## Robert's Own Replies
- **TinkerCAD object limit:** Robert notes he keeps models under ~300 objects because TinkerCAD struggles beyond that. His workaround is to export and re-import parts individually so they are treated as a single object; he planned a tips video on this.
- **Cars that used Torsen differentials:** He confirms Lexus, Chevrolet, and Audi all used them, but was unsure about competition/racing cars.
- **Averaging across outputs:** When asked whether the spur-gear linkage averages torque across both output shafts, he thought it likely does but admitted he wasn't entirely certain.