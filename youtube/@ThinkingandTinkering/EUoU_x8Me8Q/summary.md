## Overview
Robert Murray-Smith demonstrates why 3D-printed bearings built with spherical ball bearings are suboptimal, since FDM printers struggle to produce accurate spheres. He proposes and builds a **cross-roller bearing** using cylindrical rollers instead, walking through the complete TinkerCAD design process. The result is a universal 3D-printed bearing that handles radial, axial, and moment forces, well-suited for applications like turntables.

## Key Topics
- The three types of bearing forces: radial, axial (thrust), and moment
- Why spheres are poorly suited to FDM 3D printing (stepwise/digital approximation)
- Why cylinders are superior for FDM printing
- The concept of designing *for* 3D printing strengths rather than replicating traditional designs
- Step-by-step TinkerCAD design of a cross-roller bearing (race + rollers)
- The "elephant's foot" artefact in FDM printing and how to mitigate it with bevels
- Using SVG export + SVG Revolver in TinkerCAD to create a toroidal race
- Snap-and-socket clips to hold the bearing assembly together
- Alternating 90° roller placement to approximate spherical force distribution
- Applications: turntables, motors, general mechanical assemblies

## Materials and Chemicals Mentioned
- **PLA+** (generic) — FDM filament used to print the rollers and race (confirmed in comments)

## Techniques and Methods
- **Beveling cylinder ends** in TinkerCAD to counteract elephant's foot artefact during FDM printing
- **SVG export + SVG Revolver** in TinkerCAD to revolve a 2D diamond profile 360° into a toroidal race groove
- **Pythagorean calculation** to determine race height: diagonal of a 10×10mm square = √(10²+10²) = 14.14 mm
- **Alternating 90° roller placement** — each successive roller rotated 90° relative to the previous one to distribute load in multiple directions
- **Snap-and-socket feature** in TinkerCAD to clip the two race halves together without fasteners
- **Cylinder hole subtraction** to create a central axle bore (10 mm diameter)
- Printing rollers separately (10×10×10 mm cylinders) and assembling by hand

## Notable Timestamps
- `[00:00]` — Introduction; 3D-printed bearings are among the most popular Thingiverse designs
- `[00:33]` — Explanation of radial, axial, and moment forces in bearings
- `[01:20]` — Why spheres are the best shape for traditional bearings
- `[01:34]` — Why FDM printers print spheres poorly (analogue-to-digital stepping problem)
- `[02:32]` — Proposal: use cylinders instead of spheres for a better 3D-printed bearing
- `[02:42]` — TinkerCAD demo begins; creating the cylindrical roller with bevel
- `[03:16]` — Explanation of elephant's foot and how the bevel eliminates it
- `[04:01]` — Exporting a cube as SVG and using SVG Revolver to create the race
- `[04:39]` — Rotating the sketch 45° to produce a diamond-profile race groove
- `[05:34]` — Pythagoras calculation: race groove height = 14.14 mm
- `[07:02]` — Assembly demonstration: inserting rollers at alternating 90° angles
- `[07:36]` — Adding snap-and-socket clips to hold the assembly together
- `[09:47]` — Final assembled bearing demo and spin test
- `[10:06]` — Summary: bearing handles radial, axial, and moment forces; ideal for turntables
- `[10:43]` — Files uploaded to Thingiverse; closing remarks on designing for 3D printing strengths

## Robert's Own Replies
Several substantive clarifications emerged from his comment replies:

- **This is a known bearing type:** He explicitly identifies the design as a **cross roller bearing** — a well-documented precision bearing class known for high load capacity and accuracy in both radial and axial directions. He pushed back on commenters who questioned the design's validity.
- **TinkerCAD choice is intentional:** He uses TinkerCAD in tutorials because its interface is less intimidating for beginners; for his own work he still uses **OnShape**.
- **Snap fitting is optional:** The snap-and-socket clip is purely to keep the halves together; the bearing functions without it.
- **Conical vs. cylindrical rollers depend on size:** At smaller diameters, rollers should be conical (to account for tangent geometry); at larger diameters, plain cylinders work fine.
- **No cage needed if rollers fill the race:** A cage is only necessary if the rollers don't fill the full circumference; in this design it is not required.
- **Crossing cylinders approximates a sphere:** Having the rollers cross at 90° makes them collectively behave like an approximate sphere for load distribution.
- **Turntable application confirmed:** He agreed the bearing would work particularly well for turntables.
- **Seam line tip:** Recommended using the **staggered setting** for the seam line when slicing, to improve print quality.
- **Personal note:** He mentioned his wife Patti passed away on 5 April 2024, responding warmly to condolences throughout the comments.