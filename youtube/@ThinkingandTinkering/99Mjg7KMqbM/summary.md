## Overview
Robert Murray-Smith explores a novel external cycloid gear design inspired by Leonardo da Vinci's peg-and-lantern gearing system. He demonstrates a 3D-printed prototype consisting of two lantern discs (12 and 13 pegs) driven by a simple gear riding on an elliptical path, achieving a 13:1 gear ratio. The key takeaway is that this external cycloid approach is geometrically simpler to design and fabricate than traditional internal cycloid gears, making it accessible for hobbyists and promising for compact, high-torque applications in robotics and prosthetics.

## Key Topics
- Leonardo da Vinci's peg-and-lantern gear system and its historical context
- Rolling friction vs. sliding friction, and why peg-and-lantern gears can transmit more torque
- Internal vs. external cycloid gears — the distinction and the novel external approach
- How a one-tooth-per-revolution advancement produces a 13:1 gear ratio
- Design simplicity: using TinkerCAD's built-in "useful gear" primitive and simple geometry
- Construction method: calculating disc circumferences from pin count and spacing
- Potential for improvement using rollers instead of fixed pins to reduce friction
- Applications in prosthetics and robotics (compact, high-ratio gearboxes for small motors)

## Materials and Chemicals Mentioned
- PLA or similar FDM filament (implied by 3D printing, not explicitly named)
- 8 mm diameter cylindrical pins (3D-printed)

## Techniques and Methods
- FDM 3D printing of gear components (discs, pins, lanterns)
- TinkerCAD design using the "useful gear" primitive with pitch set to 8
- Circumference-based layout: pin spacing = pin diameter (8 mm) + gap (10 mm) = 18 mm per pin; total circumference = pin count × 18 mm
- Physical test-fitting (printing, aligning lanterns, measuring centre-to-centre distance) to determine the elliptical drive path
- Proposed upgrade: replacing fixed pins with rollers to minimise friction

## Notable Timestamps
- `[00:07]` — Introduction: da Vinci's catapult and the peg-and-lantern gear system
- `[01:14]` — Pros and cons of peg-and-lantern gears (torque, rolling friction, wear)
- `[01:50]` — Rolling vs. sliding friction explained with the car-pushing analogy
- `[02:26]` — Introduction to cycloid gears and their resurgence in robotics
- `[03:08]` — The core idea: moving the lantern from internal to external position
- `[03:33]` — Live demonstration of the 12- and 13-peg lantern prototype, 13:1 ratio explained
- `[04:40]` — TinkerCAD design walkthrough and Thingiverse file link mentioned
- `[05:05]` — Dimensional details: pin diameter, spacing, and circumference calculation
- `[06:05]` — Print-and-align process to find the ellipse centre distance
- `[06:42]` — Future improvements: shrinking the design, using rollers
- `[06:53]` — Applications: prosthetics and robotics

## Robert's Own Replies
Robert's comments are brief and conversational, mostly good-humoured banter with viewers. One technically relevant reply stands out:

- **Backdrivability**: Robert notes that the current prototype cannot be backdriven, and clarifies that *"being able to back drive is all about the backlash ratio"* — implying that reducing slop in a refined version could make backdrivability achievable.
- He also mentions he has **already built a follow-up version** ("I have made one already — I must post it"), suggesting iteration on the design was underway at the time.
- He explicitly states he **would not patent it**, indicating he intends it to remain open and freely usable.