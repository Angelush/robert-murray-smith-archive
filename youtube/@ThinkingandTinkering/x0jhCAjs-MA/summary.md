## Overview
Robert Murray-Smith presents a mechanical motor controller (external commutator) for brushless DC motors, arguing that silicon-based electronic speed controllers become prohibitively expensive at high power levels. He demonstrates the device working with both a small 240V motor and an adapted alternator, positioning this ~£10 prototype as a cheaper, more repairable alternative to controllers costing £400–£1000 for electric vehicle applications like his Renault Twizy.

## Key Topics
- Limitations of silicon-based motor controllers at high power
- The case for mechanical commutation as a cost-effective alternative
- Demonstration of the device controlling a small 240V brushless motor
- Demonstration with an adapted alternator converted to act as a brushless motor
- Repairability and accessibility of mechanical vs. electronic controllers
- Price comparison: ~£10 mechanical prototype vs. £400–£1000+ electronic speed controllers (e.g., Sevcon)

## Materials and Chemicals Mentioned
- Resin (used in commutator construction; noted as unsuitable — caused carbon shedding, needs replacement with a better formulation)
- Carbon brushes (heavy-duty, rated for washing machine use at 240V)
- Copper/conductive commutator segments (implied by construction)

## Techniques and Methods
- External mechanical commutation of a brushless DC motor
- Adapting a car alternator into a brushless motor
- Speed slaving: using a small DC motor to drive the commutator, which in turn controls the speed of a larger brushless motor
- 3D printing (briefly referenced — "that's the 3D sorry, that's the brushless DC motor")
- Proof-of-concept prototyping with a bench power supply (limited to ~3A)

## Notable Timestamps
- `[00:14]` — Introduction; Robert describes the device as a mechanical motor controller for brushless DC motors
- `[00:47]` — Explains the concept: it is essentially an external commutator
- `[01:10]` — Argues silicon works well at low power but becomes expensive at high power
- `[03:14]` — States the prototype cost ~£10 to build; compares to £400–£500 electronic controllers
- `[04:34]` — Live demonstration with a small 240V brushless motor driven by a drill
- `[05:19]` — Demonstration with an adapted alternator as a larger brushless motor
- `[06:00]` — Acknowledges this is a rough proof of concept; explains the control principle (small motor speed → large motor speed)
- `[06:26]` — Notes the heavy-duty brushes and the resin issue with the commutator

## Robert's Own Replies
- **Drive belt for large motors:** For very large motors, Robert suggests running a drive belt from the big motor to the commutator rather than a direct shaft coupling, which would handle synchronisation.
- **Proof of concept acknowledgement:** He repeatedly acknowledges the device is proof-of-concept level and is actively pondering engineering challenges raised by commenters.
- **Part 2 promised:** Construction/build details were to be covered in a follow-up video published the next day.
- **Keeping motors separate:** He recommends keeping the control motor and output motor mechanically separate — control the small motor's speed to govern the large motor via the commutator.
- **Cost argument vs. MOSFETs:** He notes that six MOSFETs alone for an electronic controller would cost ~$90 before any other components, reinforcing the cost advantage of the mechanical approach.
- **Self-aware about the concept's age:** He freely admits the idea is "as old as the hills" — it is essentially just putting a commutator back on a brushless motor — and doesn't claim novelty, only a practical cost/complexity advantage.
- **Scope clarification:** He clarifies he is not positioning this as a competitor to silicon, but as an alternative mechanical solution better suited to high-power, cost-sensitive applications.