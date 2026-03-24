## Overview
Robert Murray-Smith introduces the "Twisted Serpent" generator, a 3D-printable axial-flux generator using a serpentine coil rotated 90 degrees to maximize the angle of wire cutting through the magnetic field. The redesign minimizes wasted wire and produces a more power-dense, cheaper, and easier-to-build generator than conventional wound coil designs. A pull-cord test demonstrates the generator producing 45 volts.

## Key Topics
- Vector quantities and Fleming's Right-Hand Rule as the physics foundation for generators
- How wire angle relative to the magnetic field affects generator output
- Limitations of circular serpentine coils (wrong-angle sections produce no EMF)
- The "Twisted Serpent" design: rotating the serpentine coil 90 degrees to straighten active wire sections
- 3D-printed housing and rotor design using a thrust bearing
- NSNS magnet arrangement around the rotor rim
- Live demonstration producing 45 volts via pull cord

## Materials and Chemicals Mentioned
- Neodymium magnets — M35 grade, 10mm × 2mm, arranged NSNS around the rotor rim (cost ~£3.60 in UK)
- Magnet wire (enamelled/coated) — 0.1mm diameter, 350 turns
- 35mm OD / 22mm ID / 10mm thick thrust bearing (sourced from Amazon)
- 8mm steel bar (rotor shaft)
- PLA or similar 3D-print filament (housing and rotor)
- Tape (to hold serpentine coil shape during assembly)

## Techniques and Methods
- 3D printing of housing and rotor components in TinkerCAD
- Serpentine coil winding and shaping by hand, using tape markers to align bend points
- Coil rotation/twist by 90 degrees to re-orient active wire segments parallel to the axis of rotation
- NSNS alternating magnet pole arrangement to maximise field reversal per revolution
- Pull-cord wrap test for voltage measurement
- LED as a quick-and-dirty output indicator

## Notable Timestamps
- `[00:00]` — Opening physics demo with Robert and Luke demonstrating vectors using string and a weight
- `[01:01]` — Explanation of scalar vs. vector quantities and Fleming's Right-Hand Rule
- `[03:10]` — Simplification of generator variables: motion, field strength, and wire angle
- `[05:17]` — Analysis of standard circular serpentine coil's angular inefficiencies
- `[06:10]` — Introduction of the Twisted Serpent concept — rotating the coil 90 degrees
- `[06:56]` — Assembly walkthrough: thrust bearing, 3D-printed housing, rotor, magnets
- `[07:57]` — Fitting the serpentine coil onto the rotor
- `[08:21]` — Quick LED test by hand spinning
- `[09:06]` — Pull-cord test result: **45 volts**
- `[09:48]` — Summary and availability of free TinkerCAD files

## Robert's Own Replies
- **Wire spec**: Confirmed 0.1mm magnet wire, 350 turns (vs. 200 turns in the previous coil, which alone roughly doubles voltage).
- **Magnet arrangement**: Explicitly NSNSNS — alternating poles give a 180° field flip per pole pair, far greater field change than a same-pole arrangement.
- **Field strength vs. distance**: Field strength is proportional to the square of distance; getting magnets closer to the wire significantly increases EMF (emf = BLv sinθ).
- **Wire vs. magnets cost**: Magnets cost ~£3.60; wire cost ~35p. He strongly favours adding more wire/turns over adding more magnets.
- **Why volts, not watts**: The demo is about comparing coil arrangements, so voltage is the relevant metric. Watts output is always less than watts input; he estimates 50–60% efficiency for the whole machine.
- **Output is always AC**: Confirmed this type of generator always produces AC.
- **Adding more magnets won't increase power beyond a point**: Output power is determined by input power and machine efficiency, not magnet count alone.
- **Cogging concern**: Adding an iron core would increase voltage but also introduce cogging and raise start torque — a deliberate trade-off.
- **Printed bearings**: He has tried them but doesn't use them much as they don't last.
- **Needs a cover**: He left it open for visibility in the video, but a cover or potting compound would be advisable.
- **Practical applications mentioned**: Roof whirlybird (turbine vent) adaptation, bike wheels, pairing with a "Darwin" wind wall design.
- **Conductive ink**: Would not work well here due to high resistance; better suited to electrostatic applications.
- **TinkerCAD files**: Freely available; search "Twisted Serpent" under his name — had 40 downloads at time of checking.