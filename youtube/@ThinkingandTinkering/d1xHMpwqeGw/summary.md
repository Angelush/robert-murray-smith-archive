## Overview
This video uses a hinge as a practical design exercise to teach the two fundamental approaches to modelling: **build up** (adding material to form a shape) and **cut down** (removing material from a block). Robert walks through designing a functional 3D-printable hinge in TinkerCAD, step by step, demonstrating how breaking any component into its constituent parts is the core mental skill needed for all CAD and real-world fabrication.

## Key Topics
- The universal duality of fabrication: build up vs. cut down
- Identifying the sub-components of a hinge (flap, barrel, pin)
- Step-by-step hinge design in TinkerCAD using primitive shapes
- Aligning, merging, and duplicating objects in TinkerCAD
- The work plane tool and the `D` key for surface-to-surface alignment
- Clearance tolerances for 3D-printed moving parts (the ~0.1 mm gap trick)
- The hinge as a pin joint (follow-on from video 2270)
- Homework challenge: applying the same methodology to design a chain

## Materials and Chemicals Mentioned
- 3D printing filament (implied; no specific material stated)

## Techniques and Methods
- **Build up**: adding primitives (cylinder, box) to construct a form
- **Cut down**: using hole primitives merged into solids to remove material (e.g., boring the barrel hole)
- Primitive-based CSG (Constructive Solid Geometry) modelling in TinkerCAD
- Aligning objects using TinkerCAD's Align tool on specific axes
- Using the Work Plane tool to set a reference surface, then pressing `D` to drop a component flush onto it
- Duplicate + rotate (180°) to create the mirrored hinge half
- Leaving a 0.1 mm clearance gap between interlocking barrel sections for printable tolerance
- Sizing the pin slightly undersized (5.6–5.8 mm for a 6 mm hole) to ensure fit without binding

## Notable Timestamps
- `[00:08]` — Introduction; recap of video 2270 on pin joints; hinge as example
- `[00:50]` — Explanation of the two universal fabrication approaches: build up and cut down
- `[01:40]` — Opening TinkerCAD; placing the ruler; beginning the hinge model
- `[02:06]` — Creating the barrel: cylinder primitive (10×10 mm) with a 6×6 mm central hole
- `[03:09]` — Adding the flap tab (box primitive, 10×10×4 mm); aligning and merging with barrel
- `[04:04]` — Duplicating barrel units ×5; rotating one set 180° for the opposing hinge leaf
- `[04:22]` — Creating the flap body (25×50.8×4 mm); 0.1 mm gap tolerance explained
- `[05:34]` — Work plane tool demonstrated; `D` key to drop components surface-to-surface
- `[07:31]` — Assembling the second hinge leaf; fine 0.1 mm arrow-key positioning
- `[08:17]` — Creating the hinge pin (cylinder, 5.6–5.8 mm × 50 mm); pressing `D` to seat it
- `[09:19]` — Showing the printed result assembled and working
- `[09:28]` — Key clarification: this is about design methodology, not just TinkerCAD
- `[09:51]` — Homework: design a chain link using the same methodology

## Robert's Own Replies
- **Printing orientation**: confirmed the hinge prints better laid flat.
- **CAD tool philosophy**: emphasised that TinkerCAD, FreeCAD, Fusion 360, etc. are just tools — the critical skill is the build-up/cut-down mental model for "seeing" the part, which is why he focuses on methodology over software tutorials.
- **Why TinkerCAD**: considers it excellent for teaching and learning; beginners are more often confused by 3D design concepts than by the software itself.
- **Parametric modelling**: acknowledged it adds another dimension, but kept the focus on foundational concepts at this stage.
- **His own use of TinkerCAD**: noted he has extended its use to generator and wind turbine design, beyond simple parts.
- **Channel content note**: pointed out he has 168 videos on batteries, supercapacitors, and charging/control circuits, organised in a playlist, in response to someone who couldn't find them.