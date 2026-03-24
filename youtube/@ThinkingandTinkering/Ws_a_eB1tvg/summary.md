## Overview
Robert Murray-Smith walks through designing a fully functional Yankee (spiral ratchet) screwdriver from scratch in Tinkercad, explaining both the mechanical principles behind the tool and the step-by-step CAD workflow to recreate it. The tutorial covers every major component — the spiral cam, follower, ratchet selector, grip, and handle — using basic Tinkercad primitives and the SVG Helix shape generator. Robert concludes that the plastic prototype demonstrates the mechanism correctly, though it may not be robust enough for heavy-duty use.

## Key Topics
- Explanation of how a Yankee screwdriver works (spiral cam and follower mechanism, ratchet direction switching)
- Designing the spiral cam shaft in Tinkercad using the SVG Helix tool
- Creating the cam follower pieces (left-hand and right-hand twist)
- Building the direction-selector ratchet assembly with beveled push buttons and ballpoint-pen springs
- Designing the knurled grip (using the "Useful Gear" shape), bit holder, handle, and retaining cage
- Assembly strategy using align, group, mirror, and hole primitives in Tinkercad
- Plans to upload the files to Thingiverse

## Materials and Chemicals Mentioned
- **PLA or similar 3D-printing plastic** — used for all printed components (implied throughout)
- **Superglue (cyanoacrylate)** — used to bond the two halves of the knurled grip; Robert notes it bonds printed plastic extremely strongly
- **Ballpoint pen springs** — four repurposed springs used to bias the follower halves open
- **Standard hex screwdriver bits** — fits into the printed bit holder at the business end

## Techniques and Methods
- **SVG Helix shape in Tinkercad** — used to generate the spiral groove profile, with custom sketch height, inside diameter, winding count, and separation settings
- **SVG export/import workflow** — exporting a plain box as SVG and re-importing it into the Helix tool to flatten and reshape the spiral cross-section
- **Hole primitive as a "cookie cutter"** — using cylinder hole primitives to trim spiral ends flush and cut follower rings to exact height
- **Mirror/rotate duplication** — copying and rotating 180° or mirroring to produce opposite-hand spirals and follower halves
- **Align and center tool** — used throughout to position all components concentrically
- **Group/ungroup workflow** — assembling sub-components step by step before merging into final parts
- **Workplane trick** — dropping objects to the plane (pressing D) and using workplanes to position elements flush or at specific heights
- **"Useful Gear" shape** — parameterised gear shape (pitch 0.5, 60 teeth, 30 mm length) used for the knurled hand grip
- **Cone primitives for chamfering** — adding decorative/functional cones to neaten the grip ends

## Notable Timestamps
- `[00:00]` — Introduction: demonstrating how a real Yankee screwdriver works (spiral cam, ratchet, direction lock)
- `[01:32]` — Starting the CAD: creating the base 14 × 14 × 149 mm cylinder in Tinkercad
- `[01:45]` — Using the SVG Helix tool; exporting an SVG block to reshape the spiral profile
- `[03:00]` — Adjusting helix properties: sketch height, inside diameter, number of sides (256), windings, and separation
- `[05:00]` — Trimming spiral ends with hole cylinder primitives; setting correct 149 mm length
- `[06:06]` — Duplicating and rotating 180° to get two same-direction spirals; mirroring for the opposite-hand pair
- `[06:45]` — Combining spirals as holes and grouping with the rod to complete the cam
- `[07:01]` — Building the bit holder (cone + hex hole + outer cylinder)
- `[09:13]` — Creating the knurled grip using the "Useful Gear" shape; splitting it in half for assembly
- `[10:45]` — Superglue note for bonding the two grip halves
- `[11:13]` — Designing the follower from the original spiral, adjusting inside diameter to 11 mm for clearance
- `[15:54]` — Chopping followers in half to enable direction engagement/disengagement
- `[17:52]` — Adding ballpoint-pen springs to bias the follower halves open
- `[18:20]` — Explaining the beveled push-button direction-selector logic
- `[20:37]` — Assembling the hollow handle over the full mechanism; demonstrating the completed screwdriver

## Robert's Own Replies
The author replies are brief conversational acknowledgements ("cheers mate", "glad you enjoyed it", etc.) with no substantive technical clarifications. A few hints at follow-up content:
- Confirms he **hasn't yet looked at something** a viewer suggested but says "watch this space" — likely a follow-up project.
- Agrees the Yankee screwdriver **"is a very clever design"** and calls it **"a tool of the age."**
- Notes the hammer is **"the most useful tool I have ever owned"** in a side comment.
- Hints that angling the tool incorrectly **"can be lethal"** (likely a joke about the spiral mechanism).
- No technical corrections or additional design details were provided in the replies.