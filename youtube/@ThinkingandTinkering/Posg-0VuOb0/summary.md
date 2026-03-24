## Overview
Robert Murray-Smith explores the rhombic drive mechanism — a clever linkage invented by the Lanchester brothers in the late 1890s that converts piston motion to rotation with exceptional smoothness. He explains its historical context and why it failed commercially, then designs and 3D prints a working physical model, demonstrating how existing design assets can be reused to accelerate the process.

## Key Topics
- Late 19th-century automotive industry and the pressure to design for cost over performance
- The Lanchester Motor Company (Frederick, George, and Frank Lanchester) and their innovations, including disc brakes and epicyclic gearing
- How and why the Lanchester company went bankrupt in 1904 and was eventually absorbed into Land Rover/Tata
- The rhombic drive: how a rigid piston rod deforms a rhombus linked to two counter-rotating cranks/flywheels to produce smooth linear-to-rotational motion
- Why the rhombic drive is rare in motor vehicles (complexity, tight tolerances) but still found in Stirling engines
- Reusing STL components from a previous hypercycloidal engine design in TinkerCAD
- Designing and scaling flywheels, gears, crank arms, connecting shoes, and axles
- Step-by-step 3D-printed assembly of a working rhombic drive model
- Upload of all parts to Thingiverse for community use

## Materials and Chemicals Mentioned
- 3D-printed plastic parts (implied, no filament type specified)
- Glue (for securing axles, counterweights, and connecting pieces)
- Metal axles (6 mm and 2.8 mm bar stock)
- Washers (1 mm thin)
- Clips (for securing gear and crank assemblies)

## Techniques and Methods
- CAD modelling in TinkerCAD using primitive shapes (cylinders, boxes), boolean merge/subtract (hole/group operations), and alignment tools
- Importing and rescaling existing STL files (50% scale reuse of flywheel from hypercycloidal engine project)
- Metric gear generation via TinkerCAD's built-in shape library (module 1.5, tooth count tuned to match flywheel diameter)
- Adding keyed axle holes (flat keyway cut into circular shaft)
- 3D printing all components
- Physical assembly: press-fit and glued axles, counterweights keyed to gears, crank arms at 90° offset, clip retention

## Notable Timestamps
- `[00:08]` — Introduction to late 19th-century car industry boom and design-for-cost philosophy
- `[01:09]` — Lanchester Motor Company history: innovations and 1904 bankruptcy
- `[02:19]` — Explanation of how the rhombic drive works mechanically
- `[03:15]` — Why rhombic drives appear in Stirling engines (displacer tolerances are forgiving)
- `[03:36]` — Beginning of TinkerCAD modelling session; reusing flywheel STL from hypercycloidal engine
- `[07:10]` — Creating the gear sets; using metric gear shape, tuning module and tooth count
- `[10:49]` — Overview of remaining parts; announcement of Thingiverse upload
- `[11:17]` — Physical assembly walkthrough begins
- `[14:25]` — Completed model demonstrated; piston rods shown moving independently, 90° apart
- `[14:55]` — Mention of a simplified variant with a pivot point at the crankcase

## Robert's Own Replies
- **TinkerCAD copy/paste tip:** Confirmed that parts can be copied between two open TinkerCAD tabs using Ctrl+C / Ctrl+V — a practical workflow tip not shown in the video.
- **Molten salt heat source:** Stated he has no experience using molten salt as a heat source for Stirling engines and couldn't advise on it.
- **Related videos flagged:** Referenced video **1498 – Nitinol Engines** and video **2086 – Constantinesco** (with a direct link) as relevant companion content.
- **Self-assessment:** Remarked "it is an awesome model mate even if i do say so myself lol" — expressing genuine pride in the finished rhombic drive model.
- General replies are brief acknowledgements ("cheers mate", "glad you enjoyed it") with no additional technical content.