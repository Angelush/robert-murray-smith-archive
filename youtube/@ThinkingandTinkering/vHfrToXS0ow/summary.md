## Overview
Robert Murray-Smith demonstrates how to design an Archimedean spiral gear using a combination of FreeCAD and Tinkercad. The gear is effectively a single-tooth worm-style drive with a self-locking property, making it ideal for applications like lifts and lathes. The tutorial shows that creating such a gear is surprisingly straightforward by leveraging FreeCAD's spiral primitive and sketch sweep, then finishing assembly in Tinkercad.

## Key Topics
- What an Archimedean spiral gear is and how it works mechanically
- Self-locking property of the gear and its practical applications
- Step-by-step FreeCAD workflow: creating a spiral primitive, sketching a tooth profile, and sweeping via additive pipe
- Importing the FreeCAD STL into Tinkercad for final gear assembly
- Centering and aligning components in Tinkercad
- Assembling the full 1:25 gear set with a modulus-2 driven gear

## Materials and Chemicals Mentioned
- None mentioned.

## Techniques and Methods
- **FreeCAD spiral primitive creation** — using "Create Primitives" in the Part workbench to generate a parameterized Archimedean spiral (growth ~2 mm, radius ~45 mm, 1 rotation)
- **Sketch constraining in FreeCAD** — drawing a triangular tooth profile on the XZ plane with distance and coincidence constraints to define tooth dimensions for a mod-2 gear
- **Additive Pipe (sweep)** — sweeping the tooth sketch along the spiral path in Part Design to produce the 3D spiral tooth body
- **STL export from FreeCAD** — exporting the spiral tooth as an STL for import into Tinkercad
- **Tinkercad assembly** — combining the spiral tooth with cylinder primitives, centering/nudging for alignment, grouping, and preparing for 3D printing
- **3D printing** — printing the spiral gear and a 25-tooth mod-2 driven gear

## Notable Timestamps
- `[00:00]` — Introduction: demonstrating the physical Archimedean spiral gear, 1:25 ratio, self-locking property
- `[00:50]` — Real-world applications: lathe headstocks, differentials
- `[01:16]` — Overview of the FreeCAD + Tinkercad workflow
- `[01:35]` — FreeCAD tutorial begins: opening a new file, switching to Part workbench
- `[01:42]` — Creating the spiral primitive (growth, rotations, radius parameters)
- `[02:56]` — Adjusting spiral position to center it on the axis cross
- `[03:56]` — Switching to Part Design, creating a body and sketch on the XZ plane
- `[04:53]` — Drawing the triangular tooth profile with line and constraint tools
- `[07:29]` — Using Additive Pipe to sweep the sketch along the spiral path
- `[08:07]` — Result: completed Archimedean spiral tooth; exporting as STL
- `[09:21]` — Tinkercad segment begins: importing the STL spiral
- `[09:33]` — Adding and sizing cylinder primitives, centering the spiral to the cylinder
- `[11:05]` — Grouping all components into the final spiral gear
- `[11:20]` — Introducing the 25-tooth mod-2 driven gear and the gear housing assembly
- `[12:24]` — Final assembled 1:25 Archimedean gear set demonstrated spinning

## Robert's Own Replies
No author replies found.