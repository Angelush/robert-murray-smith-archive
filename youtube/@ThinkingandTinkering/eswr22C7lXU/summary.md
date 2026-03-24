## Overview
Robert Murray-Smith demonstrates how to design and 3D print a compound hypocycloid drive that achieves an extraordinary gear ratio of approximately 1,482:1 (≈1,500:1) using only three functional parts. By stacking two cycloidal discs with a one-lobe difference (38 and 39 lobes respectively), the gear ratios multiply together to produce a near-hypnotic reduction in output speed. The video combines a clear mechanical explanation with a full walkthrough of the CAD design process and physical assembly.

## Key Topics
- What a cycloid (hypocycloid) drive is and how its gear profile differs from standard involute gears
- How gear ratio is determined by the number of lobes in a cycloidal disc
- The concept of using two cycloidal discs with a one-lobe difference to multiply gear ratios
- Step-by-step design of cycloidal gears in FreeCAD using the Gear Workbench
- Assembly and modification in Tinkercad (combining discs, creating the eccentric driver, pin rings)
- 3D printing and physical assembly of the compound hypocycloid drive
- The inverse relationship between speed reduction and torque multiplication

## Materials and Chemicals Mentioned
- 3D printed parts (material not explicitly specified, implied PLA or similar filament)
- Glue (used to fix the static rear disc to the stand and to secure the eccentric)
- Axle (20 mm diameter)
- Clips (used to retain the axle assembly)
- Pins (roller/pin diameter: 10 mm in the demo design; pin circle radius: 100 mm)

## Techniques and Methods
- **FreeCAD Gear Workbench**: Generating hypocycloid gear profiles with configurable parameters (lobe count, eccentricity, pin circle radius, roller diameter, height)
- **Tinkercad**: Importing STL files, aligning and stacking components, creating eccentric driver discs, adding holes, grouping objects
- **3D printing**: Fabricating all gear components
- **Eccentric offset**: Shifting the drive hole by 2 mm to create the eccentric that drives the wobbling cycloidal disc
- **Compound stacking**: Gluing two cycloidal discs (38-lobe and 39-lobe) back-to-back so they act as a single compound gear stage
- **Wobble cancellation**: Using two offset cycloidal discs to balance each other at higher speeds

## Notable Timestamps
- `[00:08]` — Introduction: what a cycloid drive is and how the hypocycloid profile works
- `[00:45]` — Explanation of how gear ratio is set by lobe count; comparison with involute gears
- `[01:17]` — Standard dual-disc design explained (two discs to cancel wobble)
- `[01:51]` — The key idea: what if the two discs had different lobe counts (38 vs 39)?
- `[02:09]` — FreeCAD Gear Workbench demo begins; generating a 38-lobe cycloidal disc
- `[04:00]` — Generating the 39-lobe disc and exporting both for printing
- `[05:11]` — Tinkercad assembly: combining discs, creating pin rings, building the eccentric driver
- `[07:54]` — Physical assembly of the 3D printed parts with axle, clips, and glue
- `[09:30]` — Live demonstration: turning the axle ~1,500 times to move the output one full revolution
- `[10:37]` — Conclusion: 1,482:1 ratio from three parts; torque implications; files to be posted on Thingiverse

## Robert's Own Replies
- **Not back-drivable**: Robert states twice that he does not believe this drive is back-drivable, which is a common characteristic of very high-ratio cycloidal drives.
- **Friction**: Acknowledges friction is a concern but argues it is no worse than a typical gear train of equivalent ratio.
- **Backlash**: Notes the backlash on this design should be quite tight (a positive attribute).
- **Stacking**: Confirms it should be possible to stack additional stages for even higher ratios, and is encouraging to those who want to engineer a refined version.
- **Wobble**: Attributes observed wobble in the demo to loose hand-holding and suggests tighter tolerances would help.
- **Bicycle differential**: Acknowledges a commenter's suggestion of using it in a bicycle differential as an interesting idea.
- **3D printing access**: Notes that even in his small English town of ~5,500 people, there are two 3D print shops, and online services are widely available for those without a printer.