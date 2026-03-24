## Overview
Robert Murray-Smith demonstrates how to design helical gears entirely within Tinkercad by stacking thin (0.2mm) gear slices and rotating each layer incrementally to approximate a helix — a technique justified by the fact that 3D printing resolution cannot improve on this approximation anyway. The tutorial walks through two specific gears (10-tooth and 20-tooth, both modulus 1.5) used in a torsion differential project, including the rotation math and a workaround for Tinkercad's 300-object limit.

## Key Topics
- Why helical gears can be approximated by stacked rotated layers at 3D print resolution
- Calculating the per-layer rotation angle from total spiral degrees and layer count
- Step-by-step Tinkercad workflow: gear selection, layer height, copy-rotate-duplicate cycle
- Grouping, exporting as STL, and re-importing to collapse the object stack
- Tinkercad's 300-object limit and how to work around it

## Materials and Chemicals Mentioned
None mentioned.

## Techniques and Methods
- Setting gear modulus (1.5) and tooth count in Tinkercad's built-in gear component
- Slicing gears into 0.2mm-height layers matching FDM print layer height
- Incrementally rotating each duplicated layer (1.2°/layer for 180° helix over 150 layers; 0.8°/layer for 60° helix over 75 layers)
- Using Tinkercad's copy/repeat function with combined Z-offset and rotation angle
- Grouping the layer stack and exporting as STL
- Re-importing the STL to reduce 150–300 individual objects to a single mesh object
- Clockwise vs. anticlockwise spiral direction control via positive/negative rotation sign

## Notable Timestamps
- `[00:08]` — Introduction: showing the finished helical gears from the torsion differential
- `[00:22]` — Explanation of 3D printing resolution (0.2mm layers, 0.1mm best case)
- `[00:47]` — Layer count math: 30mm gear = 150 layers; 15mm gear = 75 layers
- `[01:35]` — Per-layer angle calculation: 180° ÷ 150 = 1.2°; 60° ÷ 75 = 0.8°
- `[02:21]` — Tinkercad tutorial begins (small 10-tooth gear)
- `[02:39]` — Setting modulus 1.5 and adjusting tooth count in the gear component
- `[03:00]` — Changing gear height to 0.2mm for a single layer
- `[03:13]` — Copy, set Z-offset 0.2mm, set rotation 1.2°, then duplicate repeatedly
- `[03:56]` — First helical gear completed; grouping and exporting
- `[04:10]` — Starting the larger 20-tooth gear with 0.8° per-layer rotation
- `[05:22]` — Second gear complete; group and export
- `[05:25]` — Tinkercad 300-object sulk: export → STL → re-import → delete stack workaround

## Robert's Own Replies
- **Drawing artefact clarification:** A visible artefact in the render is just a display issue and does not appear in the print.
- **Alternative methods in other tools:** He confirms helical gears can also be made using the spur gear script with a 30° sweep along a perpendicular line, or in Fusion 360 using the sweep function.
- **Metal printing:** He notes the gears could be sent to a print service for metal printing.
- **Fractal patterns across disciplines:** In a longer reply, Robert reflects that once you recognise recurring structural patterns in one field (mechanics, maths, chemistry), you find them everywhere — including across the multiple languages he speaks (German, Spanish, Italian, Turkish, Russian, and some Japanese) — suggesting they may be universals.