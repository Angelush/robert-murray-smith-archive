## Overview
Robert Murray-Smith designs and 3D prints a functional cable wrapping machine, inspired by a mechanical drawing he encountered online. The machine uses an external ring gear mechanism — driven by hand crank rather than a motor or chain — to rotate a tape carrier around a cable or bundle. The build demonstrates that 3D printing can produce real, working machines beyond hobbyist models.

## Key Topics
- The potential of 3D printing for making functional machines, not just models
- Ring gear mechanism design (internally vs. externally driven)
- Designing in TinkerCAD using the metric gear primitive
- Solving the gear engagement gap problem with two offset drive gears
- Hand-crank vs. motor-driven operation
- Design philosophy: adapting tools to your own needs and constraints

## Materials and Chemicals Mentioned
- Superglue — used to bond the 3D-printed parts together as the primary fastener

## Techniques and Methods
- TinkerCAD modelling: using the built-in metric gear primitive, adjusting module (tooth size) and tooth count, subtracting hole primitives to create ring gears and wire-pass cutouts
- Slicing and FDM 3D printing of all structural components
- External ring gear drive design (as a simplification over internal drive)
- Dual drive gear arrangement to maintain continuous engagement across the ring gap
- Hand-crank actuation via a printed crank arm and grip handle
- Superglue assembly of printed parts

## Notable Timestamps
- `[00:08]` — Introduction: questioning whether 3D printing can produce real machines
- `[00:26]` — Inspiration: a mechanism drawing by "than than" and a steel cable-wrapping machine build
- `[01:06]` — TinkerCAD walkthrough begins: placing and configuring the metric gear primitive
- `[02:00]` — Creating the ring gear by subtracting a cylinder hole from the external gear
- `[03:00]` — Adding a wedge cutout so wires can pass through the center
- `[04:00]` — Showing the printed ring gear and tape carrier assembly
- `[05:00]` — Explaining the three design changes (external drive, no bearings, hand crank instead of chain)
- `[05:51]` — Introducing the dual-gear solution to prevent loss of drive at the ring gap
- `[06:50]` — Assembly of base plate, ring gear, drive gears, and top plate
- `[07:57]` — Explaining the gear direction logic that eliminates the need for a chain
- `[08:33]` — First live demonstration of the assembled machine turning
- `[09:00]` — Tape carrier positioning adjustment to avoid gear clash
- `[10:10]` — Full cable-wrapping demonstration — it works
- `[10:26]` — Reflection: plans to add a motor; files to be posted on Thingiverse

## Robert's Own Replies
Several of Robert's comments are brief acknowledgements ("cheers mate"), but a few contain meaningful follow-up insights:

- **Gear tension warning:** If you try to enclose or tighten the gearing too much, it pinches them — you must leave adequate slack.
- **Motor upgrade encouraged:** He agrees a motor would improve usability and is actively hoping community members will design their own motor options.
- **Drill attachment idea:** He suggests the machine could be adapted to run off a handheld drill as a quick motorisation route.
- **Coil winding adaptation:** He mentions he is thinking about adapting the mechanism for coil winding — a notable potential extension of the design.
- **Workshop interest:** He acknowledges he should think about running workshops around this kind of project.
- **TinkerCAD endorsement:** Reiterates that TinkerCAD is surprisingly capable and accessible for this level of design work.
- **Health note:** In one reply he mentions he can "hold it together for a video but the pain is great," indicating he works through significant physical discomfort.