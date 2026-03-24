## Overview
Robert Murray-Smith demonstrates how to design and 3D print a Geneva drive (Geneva mechanism) from scratch using Tinkercad. He explains the underlying geometry — based on a right-angled triangle derived from dividing 180° by the number of slots — and walks through the full CAD process step by step. The key takeaway is that anyone can construct a custom Geneva mechanism for any slot count without hunting for pre-made designs online.

## Key Topics
- What a Geneva mechanism is and how it works (intermittent motion via a pin engaging a slotted star wheel)
- Historical and modern applications (cine projectors, pick-and-place machines)
- The geometric principle: 180° ÷ number of slots = key angle for the right-angled triangle
- Step-by-step CAD construction in Tinkercad, including ruler, workplane, and midpoint/endpoint tools
- Deriving circle radii from measured coordinates on the construction geometry
- Creating the driven star wheel (with slots and locking arcs) and the driving wheel (with pin)
- 3D printing and assembling the three components

## Materials and Chemicals Mentioned
- None mentioned.

## Techniques and Methods
- Geometric construction using a right-angled triangle with angle = 180° ÷ slot count
- Use of Tinkercad's ruler tool (midpoint vs. endpoint modes) for precise coordinate measurement
- Workplane repositioning to align geometry to angled edges
- Semicircular cylinder primitive rotated to achieve an accurate 36° reference angle
- Boolean subtraction (hollow/hole primitives) to carve slots and locking arcs
- Alignment tool for centering and edge-aligning objects
- Rotation by derived angles (36°, 54°, 72°) to duplicate slots radially
- 3D printing the three final components (driven wheel, driving wheel, axle pins)

## Notable Timestamps
- `[00:08]` — Introduction to the Geneva mechanism and its applications
- `[01:14]` — Motivation for making your own rather than sourcing one
- `[01:31]` — Core geometric principle: right-angled triangle, 180° ÷ slots
- `[02:10]` — Tinkercad-specific tips: ruler tool, midpoint vs. endpoint, workplane tool
- `[04:37]` — Starting the CAD: placing the base 80 mm cylinder
- `[05:23]` — Creating the accurate 36° right-angled triangle using semicircular primitives
- `[08:10]` — Deriving the second circle radius (29.06 mm) from measured coordinates
- `[10:34]` — Measuring the third circle radius (49.44 mm hypotenuse, giving 40.76 mm diameter)
- `[12:56]` — Drawing the slot shape using cylinder and cube hole primitives
- `[19:00]` — Creating the cam cutout (80.2 mm) for clearance
- `[20:23]` — Replicating the slot five times by rotating 72° increments
- `[22:39]` — Constructing the driving wheel pin carrier and rotating by 54°
- `[26:18]` — Printing and assembling the finished Geneva drive

## Robert's Own Replies
Robert's replies in the comments are brief acknowledgements and thanks ("cheers mate," "glad you helped"). One notable reply pushes back on a critical comment, clarifying that **all his videos are about transferable principles** — the 3D printer is merely the illustration medium, and the geometry shown could equally be worked out with pencil and paper. No additional technical content or clarifications about the mechanism were provided.