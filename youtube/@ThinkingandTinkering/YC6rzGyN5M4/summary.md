## Overview
Robert Murray-Smith explores the history and physics of springs before demonstrating how to design and 3D print a spring-loaded latch mechanism using Tinkercad. He walks through modelling a leaf-style compression spring from scratch, then assembles a multi-part latch with a push-button release, showing that 3D-printed filament has sufficient elasticity and rigidity to function as a practical spring.

## Key Topics
- The importance of springs in human history (from the bow to Roman artillery)
- Classification of springs by type (V, coil, leaf, involute) and by load (compression, extension, torsion)
- 3D printer filament as a viable spring material
- Designing a serpentine leaf spring in Tinkercad step by step
- Print orientation and grain direction for spring strength
- Designing and assembling a multi-part spring-loaded latch
- The push-bar release mechanism and its locking logic
- Real-world applications: carabiner releases, bumper latches, card readers, child locks

## Materials and Chemicals Mentioned
- **3D printing filament (PLA implied; ABS noted in comments)** — used as the spring and structural material throughout; Robert notes in comments that many people dislike the smell of ABS
- **Superglue / adhesive** — used to assemble the printed parts (plates, springs, guides, button cap)

## Techniques and Methods
- **Tinkercad 3D modelling** — constructing a semicylinder primitive, hollowing it to create a thin leaf band, mirroring and repeating sections to build a serpentine compression spring; using rotation handles, work-plane tool, and center/lineup keys
- **Controlled print orientation** — printing the spring so the extrusion grain follows the serpentine path, preventing layer-delamination fracture
- **Boolean subtraction (hole operation)** — cutting the hollow centre of the spring band
- **Mirror/copy operations** — duplicating and flipping spring segments to build up full spring length
- **Glue assembly** — bonding printed sub-assemblies with marker notches for alignment

## Notable Timestamps
- `[00:08]` — Introduction: springs as one of humanity's most important inventions
- `[00:56]` — Classification of spring types (V, coil, leaf, involute, etc.)
- `[01:21]` — Compression, extension, and torsion springs explained; Roman ballista and onager as torsion examples
- `[02:23]` — 3D filament as a spring material; existing examples (catapults, clockwork cars, Nerf guns)
- `[03:01]` — Introduction to latches and the motivation for adding springs
- `[03:29]` — Tinkercad walkthrough begins: placing and orienting the semicylinder primitive
- `[04:21]` — Hollowing the semicylinder to form a thin spring band
- `[05:02]` — Adding the straight breadth section and aligning with the work-plane tool
- `[05:44]` — Mirroring and repeating sections to complete the spring; grouping
- `[06:22]` — Printing advice: importance of correct grain orientation for a compression spring
- `[07:23]` — Overview of the additional latch components (slides, trapezoid lock, push bar)
- `[08:13]` — Push-bar release mechanism explained: prongs push lock bars outward against springs
- `[09:00]` — Second (bottom) compression spring added to automate lock ejection
- `[09:13]` — Full automatic operation demonstrated
- `[09:46]` — Gluing the assembly together with guides and top plate
- `[10:20]` — Final demonstration: locking and unlocking the completed spring-loaded latch
- `[11:03]` — Real-world applications and suggestion for use as a child lock

## Robert's Own Replies
The comments are largely social acknowledgements ("cheers mate"). The substantive clarifications Robert added are:

- **Software used:** confirmed this model was made in **Tinkercad**, though he uses a variety of tools.
- **ABS vs PLA:** acknowledged that ABS works for springs but noted many people dislike its smell.
- **Child-lock intent:** confirmed the push-bar indentations are deliberately small to make the mechanism hard for little fingers — the difficulty is a feature, not a flaw.
- **Automotive application:** noted that a viewer's comment about car bumper latches resonated — a friend at a Ford dealership confirms this type of latch failure is a common real-world problem.
- **Living hinges:** briefly discussed living hinges as a related concept, observing they are mostly suited to laser cutters rather than FDM printing.