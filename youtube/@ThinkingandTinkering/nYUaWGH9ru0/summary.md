## Overview
Robert Murray-Smith introduces FreeCAD from a conceptual standpoint, explaining the mental model behind 3D CAD design before touching the software. The video walks through installing FreeCAD, understanding its workbench system, and creating an involute gear with axle holes as a practical worked example. His central takeaway is that understanding *what* you are doing and *why* matters far more than memorising button sequences.

## Key Topics
- The philosophy of learning a CAD program: understanding intent before interface
- Decomposing machines → mechanisms → parts → sketches
- Installing FreeCAD (Windows, Mac, Linux) and initial setup
- The workbench concept and navigating between workbenches
- Creating a Part and Body container hierarchy
- Using the built-in involute gear generator in Part Design
- Drawing and fully constraining sketches in the Sketcher workbench
- Extruding sketches with the Pad tool
- Cutting holes with the Pocket tool
- Exporting to STL for 3D printing
- Project context: designing a 60:1 reduction gearbox for CNC or clock use

## Materials and Chemicals Mentioned
- Aluminum — mentioned as the intended manufacturing material for a gear axle handle (replacing the plastic prototype)

## Techniques and Methods
- **Sketch-based parametric modelling** — drawing 2D profiles on planes (XY, XZ) then extruding
- **Involute gear generation** — using FreeCAD's built-in Part Design → Involute Gear tool, setting teeth count, module, pressure angle, and internal/external flag
- **Fully constraining sketches** — applying dimensional and positional constraints so every element is fully defined before proceeding
- **Copy-paste of sketch elements** — duplicating a constrained circle and repositioning it by editing individual constraints
- **Pad (extrusion)** — extruding a closed sketch profile to a specified thickness (e.g. 3–5 mm)
- **Pocket (subtraction)** — cutting holes through a solid body by reversing an extrusion
- **STL export** — exporting the finished model as an STL mesh for 3D printing

## Notable Timestamps
- `[00:07]` — Introduction: learning FreeCAD like looking at the jigsaw box lid before starting
- `[01:40]` — Physical demonstration with an escapement mechanism to illustrate machine → part decomposition
- `[03:16]` — How to download and install FreeCAD; overview of workbenches
- `[05:27]` — Focus on Part Design and Sketcher workbenches; opening a new file
- `[07:01]` — Project introduction: a 20:1 gearbox to be redesigned as a 60:1 aluminium version
- `[10:02]` — Live demo begins: creating a Part and Body in FreeCAD
- `[12:00]` — Using the built-in Involute Gear generator; setting 120 teeth, module, and pressure angle to 30°
- `[14:26]` — Padding (extruding) the gear sketch to 3–5 mm thickness
- `[15:11]` — Switching to Sketcher workbench to hand-draw axle and drive holes
- `[17:57]` — Explanation of constraints: why FreeCAD requires full constraint of every sketch element
- `[21:39]` — Copy-paste workflow for placing eight equally spaced circles using dimension constraints
- `[25:29]` — Applying the Pocket tool to cut holes through the gear body
- `[26:14]` — Exporting as STL and showing the printed result

## Robert's Own Replies
Robert's comments are mostly brief acknowledgements, but several substantive points emerge:

- **Follow-up video**: Multiple viewers asked for clarification on a step Robert missed (likely sketch attachment or a specific workflow detail); he confirmed a follow-up video was published the following Monday.
- **Equally-spaced circles tip**: He explained how to place circles at 45° intervals — draw a 30 mm construction line, dimension it to the axis to get an angle constraint, set it to 45°, draw the circle, and make it coincident with the far end of the line.
- **Software choice defence**: He pushed back firmly against comments criticising his choice of FreeCAD, noting that all CAD programs must perform CAD functions; the choice is personal preference, and negative comments without constructive content add nothing.
- **Spreadsheet tool**: He noted FreeCAD's spreadsheet tool is more useful for series of related designs than one-off parts.
- **Background**: He confirmed he had prior experience with Fusion 360, Onshape, and Tinkercad, and that technical drawing taught in school was a significant help.
- **Personal note**: He confirmed that "Patti" seen in the background was his wife, who passed away a year before the video was published.