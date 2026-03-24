## Overview
Robert Murray-Smith demonstrates how to design and 3D-print a cross-roller ring (slew) bearing entirely from scratch in Tinkercad, explaining each geometric step in detail. The bearing is centerless, making it ideal for applications like turntables, wind turbines, and motors where unobstructed central space is needed. A load test at the end shows the 25%-infill printed bearing can support the weight of a person (~75–85 kg) without damage.

## Key Topics
- Why rollers are preferable to balls for 3D-printed bearings (easier to print, less support structure)
- Advantages of a centerless/ring bearing design
- Step-by-step construction of the raceway using Tinkercad's SVG Revolver tool
- Design and fabrication of the roller cage with snap-fit slots
- Calculating roller count and angular spacing (20 rollers at 18° intervals)
- Alternating roller orientation (cross-roller pattern at 45°) for multi-axis load handling
- Real-world load testing of the finished printed bearing
- Potential applications: turntables, wind turbines, motors, drives

## Materials and Chemicals Mentioned
- PLA or generic 3D-printing filament (implied throughout; nylon suggested in comments as an alternative)
- 1 cm acrylic sheet (used as a load-spreading platform for the weight test)

## Techniques and Methods
- SVG Revolver in Tinkercad — revolving a 45°-rotated square profile 360° to generate a toroidal raceway groove
- Export/re-import at 1000% scale to overcome Tinkercad's SVG Revolver size limitations, then scale back
- Boolean subtraction (hole primitives) to cut the raceway channel and hollow the cage ring
- Cylinder alignment using Tinkercad's align tool (center + edge) to position rollers accurately
- Mirroring roller cutouts to create the alternating (cross) roller orientation
- Rotational copy at 18° increments (×20) to populate the full cage
- Snap-fit slot design (2 mm wide box subtraction) to allow rollers to be pressed and twisted into the cage
- Infill tuning: demonstrated at 25%; 100% infill suggested for higher-load applications
- Live load test: bearing placed on floor, acrylic sheet on top, person standing on it

## Notable Timestamps
- `[00:00]` — Introduction; shows the existing Archimedes drive model and its cross-roller ring bearing
- `[00:52]` — Explains the centerless advantage and the wind turbine use-case
- `[02:02]` — Begins Tinkercad walkthrough; opens SVG Revolver and exports a box as SVG
- `[03:14]` — Rotates the SVG sketch 45° to create the diamond/roller-groove profile
- `[04:02]` — Scales the race to 220 mm diameter using the 1000% export/re-import trick
- `[05:09]` — Constructs the raceway housing (outer and inner cylinder booleans, 3 mm margins)
- `[07:59]` — Designs the cage ring (4 mm high, 228 mm outer, 192 mm inner)
- `[09:09]` — Places and aligns the first 10×10×10 roller cutout at 45°; adds snap-fit slot
- `[11:00]` — Works out roller count: 20 rollers at 18° spacing
- `[12:27]` — Creates the mirrored roller set and rotates by 9° to interleave the cross pattern
- `[13:33]` — Defines the actual roller cylinders at 9.8×9.8×9.8 mm (clearance fit)
- `[16:22]` — Load test: person stands on the assembled bearing on a 1 cm acrylic sheet
- `[16:43]` — Confirms the bearing survived ~75–85 kg with no damage at 25% infill

## Robert's Own Replies
- Confirmed he had made a previous video on this topic approximately 3 years earlier.
- Clarified that the bottom ring was **glued to the floor** (not free-standing) during the load test.
- Agreed that **nylon** would be a good filament choice for printing this bearing.
- Suggested the centerless design **should give a boost** to wind turbine efficiency when applied to that project.
- Acknowledged he is "no engineer" but engages in good-faith experimentation — consistent with his informal, hands-on style.