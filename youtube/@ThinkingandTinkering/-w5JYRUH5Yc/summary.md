## Overview
Robert Murray-Smith demonstrates the fourth axis attachment for the Carvera Air desktop CNC machine, which functions as a mini lathe for rotational milling. He walks through the physical setup, the MakerCAM software workflow for 4-axis toolpaths, and machines a pair of brass axles with square profiles for a larger project he has been building across multiple videos.

## Key Topics
- Physical installation of the fourth axis (headstock, tailstock, chuck jaw configuration, cable connection)
- MakerCAM software setup for 4-axis projects: stock definition, 3D model import, orientation and positioning
- Creating support cylinders in MakerCAM as virtual stock geometry
- Generating and exporting a "rotation relief" toolpath
- Two-pass cutting strategy (rough pass then finish/engraving pass)
- X-offset configuration to control where the cut begins relative to the headstock marker
- Cutting 8 mm brass bar into two axles with 5 mm square-profile ends and 3 mm cleaned tops

## Materials and Chemicals Mentioned
- **8 mm brass bar** — stock material for the axles, 80 mm length
- **Aluminium** — previously machined parts that the axles are designed to fit

## Techniques and Methods
- **Chuck jaw reversal** — swapping jaws from external to internal grip order (4-3-2-1 vs 1-2-3-4) to hold round bar stock
- **4-axis (rotational) CNC milling** — using the rotation relief toolpath mode in MakerCAM rather than standard pocket/contour operations
- **Two-pass machining** — rough pass with a 3.175 mm flat-head metal bit followed by a finish pass with a 30°/0.2 mm metal engraving bit
- **Virtual support cylinder creation** — modelling cylindrical stock geometry in MakerCAM to define the full bar length around the target part
- **STEP file export from CAD** — exporting a padded 3D sketch as a STEP file for import into MakerCAM
- **X-offset configuration** — adjusting the start position of the cut relative to the headstock reference indent/probe point
- **Parting and filing** — cutting the machined bar in half and cleaning the ends down to 3 mm to yield two separate axles

## Notable Timestamps
- `[00:00]` — Introduction to the fourth axis attachment; comparison with his hobby lathe
- `[00:40]` — Physical installation: dowel alignment, M5×20 screws, headstock loosening
- `[01:28]` — Chuck jaw reversal procedure and key usage
- `[01:57]` — Connecting the cable to input port 1 and fitting the cable clamp
- `[02:28]` — Tailstock and headstock alignment; probe indentation as reference point
- `[02:55]` — MakerCAM software walkthrough: new 4-axis project, stock setup (brass, round, 8 mm × 80 mm)
- `[04:13]` — Importing the STEP model, correcting orientation, setting 50/54 mm X position
- `[05:22]` — Creating virtual support cylinders (50 mm and 22 mm) in MakerCAM
- `[07:40]` — Generating the rotation relief toolpath; enabling tailstock option; calculating and exporting the path
- `[08:36]` — Two-pass strategy explained: rough bit then 30°/0.2 mm engraving bit
- `[09:03]` — Loading the brass bar, configuring the X-offset (changed from 50 mm to 5 mm), running the cut
- `[10:38]` — Result: two axles produced; honest reflection on the learning curve, especially offsets

## Robert's Own Replies
The author replies in the comments are largely short social responses ("cheers mate", "awesome mate") directed at other viewers. Two contain substantive content relevant to adjacent topics:
- He suggests that for serious research (e.g. on drone frames) one should use **Google Scholar** and look at current research to learn the latest terminology and refine further searches.
- He notes the Carvera Air "basically looks like a cut-down Carvera" to him, and that the larger Carvera does have a **tool-change option** — hinting this could be a future avenue worth exploring.
- He mentions he was **unable to find** a video of someone machining watch gears on the fourth axis; he found someone making watch *plates* but not gears, and asks a commenter if they have a title for such a video.