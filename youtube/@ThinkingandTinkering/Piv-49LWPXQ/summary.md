## Overview
Robert Murray-Smith demonstrates how to design a print-in-place hinge in Tinkercad — a hinge that prints as a single piece requiring no post-print assembly. The key insight is exploiting the 45° overhang rule in FDM slicers: a 45° cone angle prints without supports, yet the geometry locks the hinge together with a functional gap. He originally designed this for a wind harvester flapping mechanism.

## Key Topics
- Introduction to print-in-place hinge design as an alternative to multi-part assembled hinges
- Step-by-step Tinkercad modelling workflow for the hinge
- Explanation of why the 45° cone angle is critical for support-free printing
- Practical application: use in a wind harvester flapping unit requiring hundreds of hinges

## Materials and Chemicals Mentioned
None mentioned.

## Techniques and Methods
- **Tinkercad CAD modelling** — using cylinders, cones, and box primitives; aligning, grouping, and using boolean hole operations
- **Print-in-place FDM printing** — printing a fully assembled hinge in one print run with no support material
- **45° overhang rule exploitation** — cone angle chosen specifically so slicers do not generate supports, while still maintaining structural interlocking geometry
- **Gap clearance design** — moving mating cone parts 2 mm apart to create the functional hinge gap before grouping

## Notable Timestamps
- `[00:00]` — Introduction: hinges as essential components; two approaches contrasted
- `[01:03]` — Tinkercad workspace opened; cylinder creation begins (8 mm × 8 mm × 10 mm)
- `[01:32]` — Cone added (6 mm × 6 mm × 6 mm at 45°) and aligned to cylinder
- `[02:19]` — Base hinge unit merged; replicated to create multiple copies
- `[02:39]` — Units rotated 90° and placed on the base plane
- `[03:37]` — Internal hinge assembly grouped; flap plate (20 mm × 20 mm × 8 mm) added
- `[04:14]` — Cone inverted 180° and converted to a hole to create the socket recess
- `[05:00]` — Second socket unit created and aligned; 2 mm gap set between mating cones
- `[07:00]` — Outer arms joined with block shapes; full hinge grouped
- `[08:54]` — Completed hinge shown; real printed example demonstrated on wind harvester
- `[09:18]` — Explanation of why 45° is the critical angle for support-free printing

## Robert's Own Replies
No author replies found.