## Overview
Robert Murray-Smith demonstrates how to design a canoe in FreeCAD using the Curves Workbench and the lofting technique, drawing directly from plans in the book *Canoe Craft* by Ted Moores and Marilyn Mower. Working from tabulated measurements, he builds a full skeletal framework of cross-sectional "stations," skins them with the lofting tool, and mirrors the result into a complete canoe hull ready for STL export. His broader point is that lofting in FreeCAD's Curves Workbench is a powerful, general-purpose technique applicable to wind turbine blades, aircraft fuselages, propellers, and more.

## Key Topics
- Motivation for building vs. buying a canoe, and choosing the Peterborough canoe design
- Introduction to the traditional boat-building concept of **lofting** and its digital equivalent
- Installing and using the **FreeCAD Curves Workbench**
- Setting up a parametric sketch in the **XZ plane** to plot cross-sectional frame points from tabulated plans
- Using the **Interpolate Curve** tool to draw smooth curves through plotted points (digital "bendy stick")
- Organising sections into groups and copying/editing them to build all eight stations
- Placing stations along a virtual **strong back** using Y-axis positioning
- Skinning the rib framework using the **Lofting tool** in the Parts Workbench
- Completing the hull via double **mirroring** (YZ then XZ planes)
- Exporting to STL for 3D printing; plans to print on an Aligu Orstone Giga
- Broader applications of the lofting workflow (wind turbine blades, propellers, surfboards)

## Materials and Chemicals Mentioned
- **PLA** — target 3D printing material; estimated ~20 kg for the printed canoe (lighter than the ~60 kg wood original)
- **Cedar strips** — described in the context of traditional strip-canoe construction (rounded edge with tongue-and-groove profile)
- **Wood/timber** — referenced for traditional strong back and frame construction
- **Ferro cement** — briefly mentioned as one alternative boat-building material
- **Fabric and glue** — noted in comments as a lightweight, durable alternative skinning method

## Techniques and Methods
- **Lofting** — defining cross-sectional profiles at intervals and generating a surface skin between them, both in traditional boat building and digitally in FreeCAD
- **FreeCAD Sketcher** — plotting frame points on a 2D grid in the XZ plane using polylines, equality constraints, and dimension tools; units set to US customary inches
- **Interpolate Curve (Curves Workbench)** — fitting a smooth spline through selected sketch points to produce each cross-sectional curve
- **Group copy workflow** — duplicating section groups (Ctrl+C / Ctrl+V) and editing point coordinates directly to generate each subsequent station efficiently
- **Y-axis placement** — moving each copied station 12 inches along the Y axis to space stations on the virtual strong back
- **Lofting tool (Parts Workbench)** — selecting all curves as profiles to generate a continuous surface skin
- **Mirroring tool** — applied twice (YZ plane, then XZ plane) to produce the full symmetric hull from a quarter-model
- **STL export** — final step to prepare the model for 3D printing

## Notable Timestamps
- `[00:08]` — Introduction: living in Kent, desire to build and canoe the river
- `[01:37]` — Philosophy: building something yourself means you value it more
- `[02:21]` — Decision to 3D print the canoe
- `[03:02]` — Introducing the *Canoe Craft* book and the Peterborough canoe design
- `[04:13]` — Opening FreeCAD; installing the Curves Workbench via Add-on Manager
- `[05:57]` — Creating a sketch in the XZ plane; setting units to US customary (inches)
- `[06:57]` — Drawing the grid (8 polyline points, 2-inch spacing) to represent "graph paper"
- `[08:26]` — Entering actual frame measurements from Chart B (horizontal offsets from centreline)
- `[09:11]` — Entering measurements from Chart A (vertical offsets from baseline)
- `[09:45]` — All points placed; closing the sketch; enlarging point size to 10 for easy selection
- `[10:20]` — Applying Interpolate Curve from the Curves Workbench — first rib curve drawn
- `[10:46]` — Creating groups and using copy/paste to duplicate sections; renaming to Section One, Section Two, etc.
- `[12:07]` — Repeating the process for all eight sections
- `[12:42]` — Using Y-axis placement to space stations 12 inches apart on the virtual strong back
- `[13:49]` — Revealing the ghost skeleton of the canoe with all ribs in place
- `[16:00]` — Switching to Parts Workbench; using the Lofting tool to skin all curves
- `[17:07]` — Lofted skin applied — a quarter of the canoe hull appears
- `[17:23]` — First mirror (YZ plane) produces a half-hull; second mirror (XZ plane) produces the full hull
- `[18:27]` — Discussing STL export and 3D printing challenges; mentions Aligu Orstone Giga printer
- `[18:48]` — Broader applications: aircraft fuselages, propellers, wind turbine blades

## Robert's Own Replies
- **Weight and buoyancy of a 3D-printed canoe:** Robert clarifies that PLA doesn't need to float on its own — boats float because the weight of displaced water exceeds the boat's weight. The original wood canoe weighs ~60 kg; in PLA it would be ~20 kg. He notes this may actually make it *too light* for the designed waterline, which could be a problem.
- **Skinning alternatives:** He mentions that fabric and glue are a good skinning method — easy, lightweight, and durable — and that the hardest part of the whole process is the initial setup.
- **Real motivation for the video:** He acknowledges that other 3D-printed canoes and surfboards have already been made, but his primary goal was to use the canoe as a vehicle to walk viewers through the Curves Workbench for curved/organic objects in general.
- **Other replies** are brief social exchanges ("cheers mate", "lol") with no substantive technical content.