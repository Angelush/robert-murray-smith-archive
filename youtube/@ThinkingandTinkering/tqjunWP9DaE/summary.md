## Overview
Robert Murray-Smith demonstrates building a 3D-printed compound gear train that achieves a 128:1 speed multiplication ratio, intended for use in hand-cranked, wind turbine, bicycle, or water wheel generators. The video is a practical follow-up to his earlier gear mathematics video (1827), showing how stacking 2:1 gear stages multiplies speed exponentially (2→4→8→16→32→64→128×). The key takeaway is that gearboxes work bidirectionally — high speed out, or high torque out — depending on which end you drive.

## Key Topics
- Compound gear train construction achieving 128:1 ratio through six 2:1 stages
- Gear ratio theory: reference circles, module, and center-to-center distance calculation
- Applications: hand-crank generators, wind turbines, water wheels, bicycle generators, and winches
- Bidirectional use of gearboxes (speed multiplication vs. torque multiplication)
- 3D printing practical tips for functional gears

## Materials and Chemicals Mentioned
- PLA/FDM filament (implied, 3D-printed plastic gears)
- 8mm steel bar (used as axle shafts and keyed drive shafts)
- Skateboard bearings: 7×22×8mm
- Small bearings: 3×12×8mm (inner diameter × outer diameter × depth)
- Super glue (mentioned as insufficient for high-torque connections)

## Techniques and Methods
- 3D printing gears in correct orientation so filament grain runs radially (parallel to tooth roots), preventing shear failure
- Adding 0.25mm center-distance clearance beyond theoretical to compensate for 3D printing tolerances
- Filing a flat edge on the steel shaft to create a key, paired with a keyway printed into the gear hub (via boolean merge in Tinkercad)
- Stacking gear pairs on shared axles so each stage multiplies the previous stage's speed
- Designing gear holes/bores in CAD by merging a cube into the circular hub to produce the keyway profile

## Notable Timestamps
- `[00:12]` — Introduction: six printed gears shown, 24-tooth and 12-tooth (module 2), bearings described
- `[00:42]` — Bearing specifications explained (7×22×8 and 3×12×8)
- `[01:13]` — Base plate described with two bearing holes set 36mm apart
- `[02:24]` — Assembly begins; live demo of 2×, 4×, 8× speed multiplication per added stage
- `[03:08]` — 16× stage added
- `[03:12]` — 32× stage added
- `[03:18]` — 64× stage; final drive gear doubles it to 128×
- `[03:53]` — Fully assembled gearbox demonstrated spinning at extreme speed
- `[05:19]` — Practical tip: 0.25mm extra clearance added to center distance
- `[06:14]` — Printing orientation tip: grain must run along tooth roots, not across them
- `[06:49]` — Keyway solution for high-torque gears using filed flat on 8mm bar
- `[07:44]` — Final gearbox with handle; input and output shafts identified

## Robert's Own Replies
- **No spacers used:** The bearings he selected have a 1mm projection on the inner ring, which naturally provides axial spacing — he acknowledged he should have pointed this out in the video.
- **One-way rotation mechanism:** When asked about preventing back-driving, he confirmed a ratchet and pawl is the right mechanism.
- **Planetary gears:** He acknowledged they could achieve a similar ratio in a more compact form, but noted they wouldn't teach gear ratios and the wheel analogy as clearly.
- **Long-term durability:** For anything beyond prototyping, he recommends cast or machined gears rather than 3D printed ones, but sees printed gears as excellent for working out designs.
- **Noise:** He acknowledged the gearbox is noisy and noted there are several reasons for this (without elaborating further in replies).
- **Generator clarification:** He explained that a generator transforms mechanical energy into electrical energy — it produces nothing without mechanical input, and output is directly proportional to mechanical movement.
- **Intended purpose:** Explicitly clarified the gearbox is a demonstration/learning tool, not a finished product, and his immediate plan is hand-crank use first.