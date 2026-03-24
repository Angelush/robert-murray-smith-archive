## Overview
Robert Murray-Smith designs, 3D prints, and assembles a working pulse motor in a single afternoon, using a repurposed clock pendulum mechanism as the drive circuit. The video draws a historical parallel between modern pulse motors and the "hit and miss" flywheel engines of the 1880s–1950s, demonstrating that the same fundamental principle — a flywheel given periodic electromagnetic kicks — is alive in DIY electronics today. The finished device works as both a functional low-power motor and an attractive desk toy.

## Key Topics
- History of "hit and miss" (flywheel) engines and their operating principle
- The pulse motor as a modern electrical analogue to hit and miss engines
- Using a cheap clock pendulum module (£5 each, two for £10 on Amazon) as a ready-made pulse driver circuit
- Designing the flywheel and stand in TinkerCAD
- 3D printing all structural parts in an afternoon
- Magnet orientation and arrangement in the flywheel
- Bearing selection and axle construction for minimal friction
- Assembly with superglue
- Power options: standard battery vs. supercapacitor
- Reference to YouTuber "Lid Motor" as an expert source on pulse engines

## Materials and Chemicals Mentioned
- **Neodymium magnets (1 cm × 1 cm × 2 mm)** — fitted into square pockets in the flywheel to match pendulum magnet polarity
- **Smaller neodymium magnets (1 cm × 0.5 cm × 1 mm)** — folded in pairs to create north/south orientation; stacked two layers deep in the flywheel
- **Superglue** — used throughout for bonding 3D-printed parts
- **Skate/roller bearings** — used as guide bearings on the axle (ceramic replacements suggested in comments)
- **Household sewing needle** — forms the low-friction pivot point for the axle tip
- **Trimming knife blade (steel strip)** — provides the bearing surface the needle tip rests on
- **Battery (type unspecified)** — primary power source for the pendulum drive unit
- **Supercapacitor** — mentioned as an alternative power source for longer run times and more impressive performance

## Techniques and Methods
- **TinkerCAD CAD design** — modelling the flywheel (three-part: blue ring, pink ring, cream centre), axle, and stand before printing
- **FDM 3D printing** — printing all structural components on a small desktop printer
- **Repurposing a commercial module** — extracting the PCB/coil assembly from a clock pendulum mechanism and re-housing it as the pulse driver
- **Magnet folding trick** — folding thin magnets in half to automatically produce a north/south face pair replicating the pendulum magnet's polarity
- **Needle-point pivot bearing** — resting the axle tip on a needle seated on a steel plate for near-frictionless rotation
- **Coil proximity tuning** — positioning the drive coil as close to the flywheel magnets as possible to maximise coupling (noted in comments)
- **Positional sweet-spot finding** — holding the pulse unit in place by hand and testing slight angles before gluing, to find the optimal drive position

## Notable Timestamps
- `[00:00]` — Introduction to hit and miss engines; historical context (1880s–1950s)
- `[01:50]` — Transition to modern pulse motors; reference to YouTuber "Lid Motor"
- `[02:00]` — Explanation of how a pulse motor works (magnet → reed switch / sense coil → transistor → drive coil)
- `[02:53]` — Introduces the clock pendulum module bought from Amazon as the ready-made drive circuit
- `[04:00]` — TinkerCAD design walkthrough of the flywheel and stand
- `[04:57]` — 3D printing begins / assembly sequence starts
- `[05:28]` — Extracting and modifying the pendulum circuit board
- `[05:28]` — Magnet orientation explained; folding trick demonstrated
- `[06:22]` — Flywheel final assembly (ring + centre piece)
- `[06:39]` — Axle construction with needle pivot; bearing placement
- `[07:09]` — Completed motor running ("chugging away")
- `[07:30]` — Battery vs. supercapacitor discussion; mention of a unit run for ~6 years
- `[08:04]` — Closing remarks; files to be posted on Thingiverse

## Robert's Own Replies
- **Coil distance is critical** — get the drive coil as close to the flywheel magnets as physically possible.
- **Bearing setup matters** — the axle must rest *only* on the needle point; the top two bearings are guides only and must spin freely. Ceramic skate bearings are a cheap upgrade worth trying.
- **Finding the sweet spot** — rather than gluing the pulse unit immediately, hold it with a finger and try slight angular adjustments until the motor runs reliably, then glue it in place. The motor is sensitive to friction and alignment because of its very low power.
- **Motor/generator efficiency factors** — build quality is the dominant factor; coil length, rotational speed, input torque, and magnetic field strength all matter; coil geometry is relatively minor.
- **Supercapacitor upgrade** — he confirmed interest in exploring this further, with magnetic bearings mentioned as another potential enhancement.
- **Audio quality** — acknowledged ongoing issues with sound recording and is experimenting with recording audio separately to improve it.
- **Not a perpetuum mobile** — explicitly clarified in comments that this is not a perpetual motion machine.
- **Files on Thingiverse** — confirmed the STL files would be uploaded.
- **Inspiration credit** — confirmed that "Lid Motor" on YouTube inspired the project and praised him as "an awesome guy."
- **Self-starting** — confirmed the motor did self-start.