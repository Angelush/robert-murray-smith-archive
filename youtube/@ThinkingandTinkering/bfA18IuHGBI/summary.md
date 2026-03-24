## Overview
Robert Murray-Smith demonstrates how to salvage ceramic magnets from old speakers and use them to scratch-build both a brushless DC (BLDC) motor and a simple AC generator. Using recycled parts throughout — speaker magnets, steel bar, and coils stripped from shaded-pole microwave fan motors — he proves the concept works by spinning the generator to produce approximately 30 volts with a hand drill.

## Key Topics
- Salvaging ceramic ring magnets from old speaker drivers
- Fabricating an 8-pole rotor by bending steel angle stubs to redirect magnetic flux
- Demonstrating magnetic field polarity with a compass
- Assembling a BLDC motor in a Heath Robinson arrangement with a Y-configured coil set
- Converting the same rotor into an AC generator using recycled shaded-pole motor coils
- Voltage addition by wiring coils in series with correct polarity
- Potential improvements and applications (wind turbine, water wheel)

## Materials and Chemicals Mentioned
- **Ceramic speaker magnets** — the primary magnetic source, salvaged from old speakers; polarised north–south on flat faces
- **1 cm steel strip** — used to fabricate L-bracket / angle stub poles
- **8 mm steel bar** — axle pressed into the drilled rotor hub
- **Builder's board / central board** — used as the generator housing drum
- **Shaded-pole motor coils** (from microwave oven fans) — pre-wound coils with iron cores, used as generator stator coils
- **30 A electronic speed controller (ESC)** — used to drive the BLDC motor

## Techniques and Methods
- Disassembly of speaker drivers to extract ceramic ring magnets (screwdriver and hammer)
- Drilling the rotor hub centre to 8 mm and press-fitting a steel axle
- Lathe-turning the rotor hub for concentricity (noted as optional)
- Welding (or screwing) steel angle stubs onto magnet plates to create discrete north–south poles
- Winding coils in a 3-phase Y configuration spaced 120° apart for the BLDC motor
- Stripping shaded-pole induction motors — squeezing the laminated core with a G-clamp to release the coil/core assembly intact
- Polarity testing individual generator coils by hand-spinning and reading voltage, then reversing connections where coils are wound in opposing directions
- Series connection of coils to sum output voltage

## Notable Timestamps
- `[00:00]` — Introduction: speaker drivers as a source of ceramic magnets
- `[00:40]` — Removing metal end-plates from the magnet assembly
- `[01:00]` — Drilling rotor hub and fitting the 8 mm axle
- `[01:36]` — Fabricating steel angle stubs to create 8 magnetic poles
- `[02:16]` — Compass demonstration showing redirected north–south pole arrangement
- `[03:10]` — Heath Robinson BLDC motor setup: Y-configured coils, 30 A ESC
- `[03:47]` — Motor run demonstration
- `[04:06]` — Builder's board housing for the generator
- `[04:20]` — Harvesting coils from shaded-pole microwave fan motors
- `[06:00]` — Single-coil voltage test (~1.1 V)
- `[06:30]` — Two-coil series test, polarity correction to achieve 2 V
- `[07:31]` — Full generator run with drill — approximately 30 V output
- `[07:38]` — Discussion of improvements and applications

## Robert's Own Replies
- **Output is AC:** Confirmed in comments that the generator output is alternating current; the meter was set to AC.
- **Y vs delta wiring:** Clarified that for the motor, the three coils are independent and fired sequentially by the ESC; Y and delta only refer to how the coil ends are joined — either works.
- **Path of least reluctance:** Noted the magnetic flux follows the path of least reluctance through the steel poles, which he finds reminiscent of the path of least resistance analogy.
- **Using speaker voice coils directly:** Advised against it — voice coil wire is very thin and hard to handle, the coils are too small to generate meaningful voltage, and you'd need to form iron slugs to centre them; more trouble than it's worth.
- **Switched reluctance:** Briefly noted the motor principle also relates to switched reluctance.
- **Self-assessment:** Acknowledged he was "a bit quick" in explaining the three-coil motor wiring and offered the clarification above.