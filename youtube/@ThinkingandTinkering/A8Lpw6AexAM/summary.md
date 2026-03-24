## Overview
Robert Murray-Smith demonstrates how to convert a common brushed DC motor (like a drill motor) into a low-RPM, high-voltage brushless DC generator suitable for small wind turbines. By rewinding the rotor with more turns of thinner wire and adding a bearing that allows the motor body to rotate instead of the axle, he achieves approximately six times the original voltage output. The video is motivated by the high cost of purpose-built low-RPM BLDC generators and the desire to use cheap, widely available motors instead.

## Key Topics
- The problem with standard brushed DC motors for low-RPM wind turbine applications
- UK average wind speeds (~4.5 m/s) and their implication for available torque and RPM
- Disassembly of a common brushed DC motor and inspection of its internals
- Rewinding the rotor with more turns of thinner wire to increase voltage output
- Converting the motor from brushed to brushless by inverting the rotor/stator relationship
- Using a 3D-printed centering ring to fit the modified assembly
- Practical voltage output demonstration (~1.3 V from slow hand-spinning)
- Use case: DIY wind turbines requiring low-RPM, high-voltage generators

## Materials and Chemicals Mentioned
- **Ferrite magnets** — permanent magnets found inside the motor body (stator)
- **0.6 mm gauge copper wire** — original winding wire (24 turns per coil)
- **Thinner gauge copper wire** — replacement winding wire (150 turns per coil)
- **Bearing (21 mm × 15 mm)** — added over the commutator to allow body rotation
- **3D-printed centering ring** — used to center the rotor assembly inside the body

## Techniques and Methods
- Motor disassembly and inspection of brushes, commutator, and rotor coils
- Rotor rewinding: removing original windings and replacing with more turns of thinner wire in the same clockwise winding direction, terminated into commutator clips
- Bearing installation over the commutator to invert the rotor/stator relationship (body becomes rotor, axle becomes stator)
- 3D printing a plastic centering ring (noted as interchangeable with a cut piece of plastic)
- Open-circuit voltage testing by hand-spinning the body while holding the axle

## Notable Timestamps
- `[00:00]` — Introduction: context of low-RPM BLDC generators for wind turbines and motivation for DIY conversion
- `[00:49]` — Demo motor introduced; original low voltage output (~0.2–0.3 V) explained
- `[01:50]` — Motor disassembly; internals (magnets, rotor, brushes, commutator) examined
- `[02:25]` — Original winding traced and unwound (24 turns of 0.6 mm wire)
- `[03:02]` — New winding applied (150 turns of thinner wire)
- `[03:18]` — Bearing fitted over commutator; body/axle role reversal explained
- `[03:35]` — 3D-printed centering ring fitted and assembly completed
- `[03:51]` — Completed generator demonstrated; body spins around stationary axle
- `[04:08]` — Voltage output test: ~1.3 V achieved from slow hand-spinning
- `[04:49]` — Summary of why and when to use this conversion for wind turbines

## Robert's Own Replies
- **Wiring multiple generators in series:** Simply wire them in series — it works fine.
- **On low RPM:** Acknowledges the limitation but notes that for his intended wind turbine application, high RPM is not needed.
- **On contra-rotation:** Dismisses it as impractical (wire snarl-up or slip ring losses); suggests adding a gear to double rotation of one element instead. Mechanical simplicity is preferred.
- **On theoretical designs:** States he prefers working models over theory — if someone builds one, he'd be interested to see it.
- **On other motor types:** Confirms the technique works on different motor types, though each requires slightly different modification.
- **On UK household energy use:** Notes average UK consumption is 8.5–10 kWh/day; he personally uses ~3 kWh/day, so 6 × 500 W turbines would suffice for him.
- **On the 3D printer:** Describes it as just a tool, like a saw but more versatile — not essential.
- **On brushed vs. brushless:** Explains that brushed motors use carbon brushes and a commutator to switch polarity; brushless motors use electronics to do the same job.
- **Acknowledges an error in the video:** Admits he was in a rush and didn't check something properly.
- **On the "Wind Catcher" design:** Points viewers to look up this existing design as a related concept.