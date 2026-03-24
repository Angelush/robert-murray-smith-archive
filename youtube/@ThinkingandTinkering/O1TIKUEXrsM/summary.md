## Overview
Robert Murray-Smith demonstrates how to design and 3D print planetary gear systems using simple math and free online tools. He walks through the key formula (ring teeth = 2× planet teeth + sun teeth), calculates a 5:1 gear ratio example, and uses stlgears.com and Tinkercad to generate and assemble a print-in-place double helical gear set. The main takeaway is that planetary gears are far simpler to design and fabricate than most people assume.

## Key Topics
- The fundamental geometry rule of planetary gear systems (circle/tooth relationship)
- Calculating gear ratios and tooth counts from scratch
- Practical limits of planetary gear ratios (optimal ~8:1, max ~10:1)
- Using stlgears.com to generate STL gear files
- Assembling the gear system in Tinkercad
- Print-in-place FDM techniques for herringbone/double helical gears
- Planet carrier design and construction
- Stacking gear stages for compounded ratios (e.g., 5:1 → 25:1 → 125:1 → 625:1)
- Planet spacing rules: divisibility of sun and ring tooth counts by the number of planets

## Materials and Chemicals Mentioned
- None mentioned.

## Techniques and Methods
- **Planetary gear ratio calculation** — using the formula: ring teeth = (2 × planet teeth) + sun teeth
- **Gear file generation** — using stlgears.com to produce STL files for spur, helical, double helical (herringbone), and internal ring gears
- **Double helical / herringbone gear design** — chevron teeth lock axially and improve torque transfer and noise vs. spur gears
- **FDM print-in-place** — printing the full gear assembly in one go; planet gears scaled to 99% to provide ~0.5 mm clearance and prevent sticking
- **Tinkercad assembly** — importing STL gears, aligning sun and ring on center axes, manually positioning planets, rotating ring to align teeth, duplicating planets at 90° intervals
- **Planet carrier fabrication** — cylinder with four peg cylinders and a square center hole, held by clips into indentations on the carrier top
- **Stage stacking** — printing multiple identical units and stacking them to multiply gear reduction

## Notable Timestamps
- `[00:08]` — Introduction: planetary gearboxes are simpler than they seem
- `[00:30]` — Visual explanation of ring/planet/sun geometry using circles
- `[01:26]` — Key formula introduced: ring teeth = 2 × planet teeth + sun teeth
- `[02:08]` — Discussion of practical gear ratio limits (8:1 optimal, 10:1 max)
- `[03:13]` — Walkthrough of calculating a 5:1 ratio: sun=20, planet=30, ring=80
- `[05:24]` — Introduction to stlgears.com for generating STL gear files
- `[06:14]` — Choosing double helical (herringbone) gears for print-in-place advantages
- `[07:00]` — Inputting tooth counts into stlgears.com and downloading gears
- `[08:11]` — Importing into Tinkercad; scaling planet to 99% for print clearance
- `[09:03]` — Aligning and positioning gears; rotating ring to mesh teeth correctly
- `[10:15]` — Duplicating and rotating planets 90° to complete the assembly
- `[10:47]` — Final assembly: adding axle, planet carrier, handle; gear works first print
- `[11:46]` — Stacking stages: 25:1, 125:1, 625:1 by printing multiples
- `[12:57]` — Planet position divisibility rules for 3- vs. 4-planet configurations

## Robert's Own Replies
The author replies are brief, friendly acknowledgements ("cheers mate", "you're welcome", etc.) with no substantive technical follow-up. Two minor points of note:
- Confirms a **dynamometer** should be used to measure torque output ("yes - use a dynomometer")
- Notes that **resin printers** have remarkable resolution these days, relevant to gear accuracy
- Suggests using **T-Cut** (a cutting/polishing compound) in the gear assembly, likely as a lubricant or to smooth tight fits
- Confirms one commenter's point that he can be "a little loose with some things," acknowledging minor imprecision in the presentation