## Overview
Robert Murray-Smith walks through the iterative design process of creating a compact, high-ratio cycloidal gear reducer (60:1) in FreeCAD, intended to be fabricated in aluminium on a CNC machine. He demonstrates that absolute beginners can produce real, functional 3D-printable parts using only a handful of FreeCAD operations within an hour or two, using a plastic prototype to validate the design before committing to metal.

## Key Topics
- Design iteration philosophy: prototype in plastic before committing to metal
- Redesigning an existing 20:1 Tinkercad gear reducer into a compact 60:1 cycloidal gear suitable for a NEMA stepper motor
- Step-by-step FreeCAD workflow: creating involute gears, sketches, pads, and pockets
- Material constraints shaping final design decisions (available aluminium stock sizes)
- Encouragement for beginners to "just start" with CAD rather than waiting to master it

## Materials and Chemicals Mentioned
- **Aluminium bar stock** — 10 mm thick, 100 mm long; intended material for final CNC-machined parts
- **3 mm aluminium sheet** — secondary stock material considered for back plate construction
- **PLA/FDM plastic** (implied) — used for rapid prototyping and design validation before metal fabrication

## Techniques and Methods
- **Iterative prototyping** — printing successive plastic versions to validate design before metal machining
- **FreeCAD involute gear generation** — using the Part Design > Involute Gear tool with specified tooth count, module, and pressure angle
- **Sketch-based parametric modelling** — placing and constraining circles/rectangles using dimensional and coincident constraints
- **Pad and Pocket operations** — extruding sketches and cutting recesses to defined depths (3 mm, 3.1 mm clearance, 6 mm, 10 mm)
- **Sketch copying** — using Ctrl+C / Ctrl+V to reuse existing sketches across bodies and reassigning them via drag-and-drop
- **Fillet application with equality constraints** — adding and equalising corner radii across a profile
- **STL export** — exporting bodies for 3D printing

## Notable Timestamps
- `[00:00]` — Introduction; overview of the ongoing project series (metal 3D printing / CNC)
- `[00:45]` — Description of the existing 20:1 plastic gear reducer and goal to reach 60:1–100:1 in a compact form
- `[01:52]` — Philosophy of iterative design: why redrawing matters
- `[03:06]` — Introduces available aluminium stock and how material constraints shape the design
- `[03:31]` — Reveals redesigned version: 120/122 tooth gears at 0.5 modulus, ~70 mm diameter, 3 mm plate thickness
- `[05:50]` — FreeCAD live demo begins: creating the drive gear (120 teeth, 0.5 modulus, 30° pressure angle)
- `[06:29]` — Creating the eccentric hole layout sketch (six circles, 20 mm from centre, 60° spacing)
- `[11:16]` — Exporting STL and printing the gear
- `[12:29]` — Creating the back plate body: 122-tooth ring gear (external = false), 75×75 mm square housing with fillets, bearing pocket (19 mm), 3.1 mm gear pocket
- `[18:18]` — Creating the top plate body by copying the back plate sketch
- `[21:47]` — Creating the eccentric body: 5 mm square drive socket offset 0.25 mm from centre for 0.5 mm throw
- `[23:43]` — Creating the drive output plate: 60 mm base disc, 5 mm square socket, 13.5 mm drive pins at 60° spacing, padded to 3 mm + 6 mm
- `[29:04]` — Assembly demonstration: dot on output confirms 60:1 reduction is working
- `[29:22]` — Closing remarks on the minimal toolset needed to get started in FreeCAD

## Robert's Own Replies
Robert's comments are mostly brief acknowledgements and thanks, but a few offer meaningful context:
- He confirms the FreeCAD method he used ("method 1") is exactly what he did, not a polished approach — the point was to show a beginner's real workflow.
- He estimates the entire FreeCAD session took "an hour or so," but notes he already had experience with Onshape, Fusion 360, and Tinkercad, so the learning curve was shorter for him.
- He pushes back (politely but firmly) on commenters who criticised his technique without providing actionable guidance, emphasising the video targets absolute beginners and that useful tips need enough detail to follow.
- He agrees with comments noting there are more elegant ways to do what he showed, but frames this positively: "what is important is it was done."
- He acknowledges he could not do one suggested tip ("not sure i know how to do that mate"), reinforcing his self-presented beginner/intermediate status in FreeCAD.