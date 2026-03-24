## Overview
Robert Murray-Smith demonstrates how to design and build a friction-based planetary gear system using ping pong balls as the rolling elements. He walks through the CAD modelling process in Tinkercad (using torus and cylinder primitives) and assembles a physical prototype, showing that the system achieves approximately a 4:1 gear ratio and that torque capacity is governed by spring preload rather than the number of balls.

## Key Topics
- Friction drives and the concept of the normal force
- Applying friction drive principles to spheres (ping pong balls) instead of cylinders
- Tangent and normal geometry for spherical rolling contacts
- Designing a toroidal raceway in Tinkercad (and notes on equivalence in FreeCAD)
- Designing a planet carrier with three ball pockets
- Thrust bearings and spring preload for maintaining normal force
- Assembly of the complete planetary gear stack
- Gear ratio demonstration (~4:1 step-up or step-down depending on input/output)
- Relationship to CVT (continuously variable transmission) design

## Materials and Chemicals Mentioned
- Ping pong balls (40 mm diameter) — used as the rolling/planetary elements
- Thrust bearings (11 mm × 47 mm / 42 mm × 25 mm) — used top and bottom of the stack to handle axial spring load
- Springs — provide the normal force that enables friction drive engagement
- Axles — connect carrier and pressure plate; glued in place

## Techniques and Methods
- CAD modelling in Tinkercad using torus primitives to generate a toroidal raceway
- Boolean subtraction (hole/merge operations in Tinkercad; equivalent to boolean subtract in FreeCAD) to carve the raceway profile
- Sizing the torus tube radius to match the ball diameter (radius = 20 mm for a 40 mm ball)
- Using cylinder primitives to build up wall thickness on raceway and carrier parts
- Duplicating and rotating ball-pocket holes by 120° to place three evenly-spaced pockets in the carrier
- Adding 0.5 mm clearance (41 mm holes for 40 mm balls) for fit tolerance
- Spring-preload assembly: pressure plate compresses spring to lock the stack and apply normal force to the balls
- Physical assembly: stacking raceway, carrier, thrust bearings, pressure plate, and spring

## Notable Timestamps
- `[00:08]` — Introduction to friction drives; recap of the normal force concept
- `[00:51]` — Introduces the ping pong ball as a spherical rolling element
- `[01:00]` — Explains how the normal applies to a sphere (tangent/normal geometry)
- `[02:11]` — Introduces the raceway concept
- `[02:18]` — Begins CAD walkthrough in Tinkercad using the torus primitive
- `[03:30]` — Constructs the bottom raceway by merging torus hole into cylinder
- `[05:00]` — Explains spring indentation and thrust bearing placement in the raceway
- `[06:04]` — Designs the planet carrier cylinder with hollowed interior
- `[07:06]` — Creates ball-pocket cutouts, duplicated at 120° spacing
- `[08:30]` — Completes carrier design; begins physical assembly sequence
- `[10:15]` — Demonstrates gear ratio: ~1:4 step-up / 4:1 step-down
- `[10:33]` — Notes torque is limited by spring strength, not number of balls
- `[11:04]` — Notes proximity to a CVT design; files to be posted on Thingiverse

## Robert's Own Replies
- **Friction improvement:** In response to a comment about limitations, Robert acknowledges the design in its current form has limits but emphasises the principle — suggests using rubber balls to improve the coefficient of friction.
- **Rubber balls:** Confirms rubber balls "would work better for sure" as replacements for ping pong balls.
- **BLDC motor tip (off-topic reply):** Notes that a running capacitor is not needed with a BLDC motor; a link capacitor can be used with a rule of thumb of ~2 µF per watt.
- **Potential problems:** Challenges a commenter to not just point out a problem but propose a solution.
- **Teaser:** Hints at a follow-up video ("oh yes — wait until the next video lol"), likely extending the CVT/friction drive series.