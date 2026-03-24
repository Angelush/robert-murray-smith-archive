## Overview
Robert Murray-Smith demonstrates how to convert a salvaged car alternator into a brushless motor, inspired by a viewer suggestion. He disassembles the alternator, removes unnecessary components (rectifier bridge, voltage regulator), solders new wires to the brushes and stator coils, and connects the result to an electronic speed controller. The video concludes with the converted motor successfully running, proving it's a cheap and practical way to obtain a capable motor.

## Key Topics
- How alternators differ from and relate to motors and dynamos
- The internal structure of an alternator (rotor, stator, slip rings, brushes, rectifier bridge)
- Difference between slip rings (alternator) and commutators (DC motor)
- Step-by-step disassembly and modification of a scrap alternator
- Delta vs. Y (star) winding configurations in alternators
- Connecting the converted motor to an electronic speed controller (ESC)
- Practical cost and hobbyist appeal of the conversion

## Materials and Chemicals Mentioned
- **Scrap car alternator** — the main component being converted (sourced for free)
- **DC power supply** — used to energise the rotor brushes (recommended ~12V, 2–3A)
- **Battery jumper cable wire** — used as heavy-gauge wire soldered to stator coils
- **Heat shrink tubing** — applied to soldered stator wire connections
- **Electronic speed controller (ESC)** — small helicopter ESC used to drive the three-phase stator (~1.5 kW recommended for serious use)
- **Capacitors** — mentioned in passing as a way to make an alternator a self-standing generator (not used in this conversion)
- **Zip tie** — used for strain relief on brush wires

## Techniques and Methods
- Disassembly of alternator casing and removal of rotor
- Desoldering and removal of the rectifier bridge and voltage regulator
- Brush retention using a 1.5 mm drill bit as a retaining pin to compress springs during reassembly
- Soldering DC feed wires to brush contacts and threading through the alternator housing
- Soldering three heavy-gauge wires to the three stator coil terminals
- Reassembly with rotor re-inserted using the retaining-pin trick to avoid snapping brushes
- Connecting three stator wires to a three-phase brushless ESC for speed control
- Applying 5V to rotor and 17V to stator for initial demonstration (recommended 12V/36–48V for full power)

## Notable Timestamps
- `[00:15]` — Introduction; credits viewer Ivan Rojas for the idea
- `[00:38]` — Overview of the scrap alternator and initial disassembly begins
- `[01:04]` — Explanation of how alternators work vs. dynamos and motors
- `[03:40]` — Close-up of the rotor, slip rings, and explanation of electromagnet principle
- `[05:00]` — Close-up of stator windings, three contact points, rectifier bridge, and brushes
- `[06:33]` — Stator removed; identifying the three coil wires; removing rectifier and voltage regulator
- `[08:38]` — Brush retaining-pin trick explained and demonstrated
- `[09:31]` — Soldering wires to brushes; threading through housing; brush modification complete
- `[10:30]` — Stator modification: soldering chunky wires to the three stator coils
- `[13:22]` — Final reassembly completed; confirms Delta configuration (post-1990 alternators)
- `[13:43]` — Motor rigged to ESC and demonstrated running
- `[15:04]` — Plans for the motor; cost and fun justification for the project

## Robert's Own Replies
- **ESC clarification:** The electronic speed controller he used is designed for brushless motors, which is appropriate here because a converted alternator is essentially a brushless motor in principle.
- **DC on the rotor is essential:** Without DC energising the rotor, running it as a motor would be very challenging — the rotor would likely need to be reconfigured.
- **How an alternator works as a generator (detailed explanation):** The DC current on the rotor creates a large electromagnet; as it rotates, the changing magnetic field induces current in the stator coils. At low speed, input power exceeds output, but above a threshold speed, output exceeds input and it becomes a generator. The same principle applies to converting any generator into a motor.
- **Future video teased:** He picked up a large generator and may do a video on converting that; also mentioned the PC fan generator videos share the same underlying principle.
- **Power source idea:** Considering using a battery pack and tapping off voltage in a transformer-like fashion to power the motor.
- **General enthusiasm:** Several replies affirm his love of hands-on exploration and learning by doing.