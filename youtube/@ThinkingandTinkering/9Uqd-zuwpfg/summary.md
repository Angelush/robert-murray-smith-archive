## Overview
Robert Murray-Smith explains why magnets (and springs) produce non-linear force — dropping off with the square of distance — and introduces the fusee, a historic clockmaker's device that compensates for this by acting as a variable transmission. He demonstrates how to design a conical fusee spiral in FreeCAD, export it as STL, and finish it in Tinkercad for 3D printing.

## Key Topics
- Non-linear force behaviour of magnets and springs (inverse square law)
- History and function of the fusee (variable torque compensator used in clocks since the 1400s)
- Designing a conical helix in FreeCAD using the Helix tool and sketch constraints
- Exporting from FreeCAD and finishing the model in Tinkercad
- 3D printing the fusee cone
- Plans to use the fusee with a magnetic "battery" (magnets-as-spring system from a previous project)

## Materials and Chemicals Mentioned
- Magnets (used as springs in opposition, like-pole vs like-pole)
- String / chain (for winding around the fusee)
- 3D printed PLA/filament (implied by printing the fusee cone)

## Techniques and Methods
- FreeCAD sketch on the XZ plane with coincident and distance constraints
- Using FreeCAD's Helix tool with height/turns/angle mode to generate a conical spiral (45–60°, 100 mm tall, 10 turns)
- Adjusting parametric model values directly in FreeCAD after creation
- Exporting geometry as STL from FreeCAD
- Importing STL into Tinkercad, combining with a cone primitive, cutting a groove, flattening the top, and adding an 8 mm axle hole
- Using boolean hole/group operations in Tinkercad
- 3D printing the finished fusee

## Notable Timestamps
- `[00:00]` — Introduction: revisiting the Da Vinci catapult with magnets as springs
- `[01:05]` — Explanation of the inverse-square law for magnetic force
- `[02:06]` — Why non-linear force is a problem for consistent mechanical output
- `[02:32]` — Introduction of the fusee and its history (Leonardo da Vinci, 1400s crossbows and clocks)
- `[03:28]` — Starting the FreeCAD tutorial: new file, sketch on XZ plane
- `[05:25]` — Using the Helix tool; setting height (100 mm), turns (10), angle (60° then 45°)
- `[06:31]` — Completed conical spiral shown in FreeCAD
- `[07:09]` — Exporting STL and importing into Tinkercad
- `[08:07]` — Merging spiral with cone, making the spiral a hole, grouping
- `[09:12]` — Adding axle hole (8 mm) and finalising the fusee shape
- `[09:43]` — Printed fusee shown; note that a true fusee is hyperbolic, not purely conical
- `[10:05]` — Acknowledgement that no one has done this with magnets before; trial and error needed

## Robert's Own Replies
Robert's comments are mostly brief acknowledgements, but a few add useful context:
- He confirms he **has plans** to develop the fusee concept further (likely integrating it with the magnetic spring/catapult project).
- He agrees that even with mathematical optimisation, **trial and error will still be needed** to find the best curve shape for a magnetic fusee.
- He endorsed the idea of making a fusee **in wood** as a valid alternative approach.
- He clarified for a commenter that the force drop-off follows the **square of the distance**.
- He expressed enthusiasm for someone collaborating on the idea and hoped they would find a partner to work with.