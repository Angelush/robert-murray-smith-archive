## Overview
Robert Murray-Smith introduces boost converters by first grounding the viewer in the physics of inductors — deriving the relationship V = L·dI/dt from Maxwell's equations — then explaining the boost converter circuit topology, and finally building a working prototype on a breadboard. The video demonstrates stepping 10V up to ~240V to light a mains-voltage LED, while candidly discussing the gap between theoretical calculations and real-world results.

## Key Topics
- Physics of inductors: magnetic permeability, magnetic flux, and inductance (Henry's)
- Derivation of V = L·dI/dt from Maxwell's equations
- How collapsing a magnetic field induces a high voltage spike
- Boost converter circuit topology (inductor, switch, diode, capacitor)
- Comparison to flyback transformers
- Component selection using an Adafruit boost converter calculator
- Arduino-controlled MOSFET switching at ~30 kHz
- Real-world vs. theoretical performance discrepancies
- Limitations of breadboard builds

## Materials and Chemicals Mentioned
- **221 µH inductors** (×3 in series, salvaged from old PCB, ~663 µH total)
- **IRFPF40 MOSFET** (900V VDS, used as the switching element)
- **2N2222A NPN transistor** (drives the MOSFET gate with inverted logic)
- **DS14508A diode** (900V reverse breakdown, used as the flyback diode)
- **0.22 µF, 275V AC capacitor** (output filter capacitor)
- **1K and 10K resistors** (gate drive and base pull-down)
- **220–250V LED** (used as the output load to visually confirm operation)
- **Arduino** (generates PWM switching signal via direct port writes)

## Techniques and Methods
- Deriving inductance and flux relationships algebraically from first principles (MIT 2006 course outline)
- Inverse-logic MOSFET drive: NPN transistor pulls gate low to turn MOSFET off, gate floats to Vin to turn it on
- Direct port manipulation in Arduino (bitwise OR/AND) to achieve 30 kHz switching — bypassing the slow `digitalWrite()` library calls
- Component value selection via the Adafruit boost converter online calculator (inputs: switching frequency, Vin, Vout, max current, acceptable ripple)
- Oscilloscope monitoring of MOSFET gate waveform to verify duty cycle (~95–98%) and frequency (~31 kHz)
- Multimeter measurement of output voltage and load current
- Breadboard prototyping with joined ground/power rails

## Notable Timestamps
- `[00:03]` — Introduction: inductors as the crucial element in boost converters and switch-mode supplies
- `[00:39]` — Physics of inductors: magnetic field equation B = µ·I(t)/L
- `[04:53]` — Magnetic flux Φ = B·A, leading to the definition of inductance in Henrys
- `[06:38]` — Maxwell's equations link: rate of change of flux equals voltage; derivation of V = L·dI/dt
- `[08:44]` — Collapsing magnetic field → high induced voltage; why infinite voltage doesn't actually occur
- `[09:51]` — Brief aside on flyback transformers and how they relate
- `[10:27]` — Circuit diagram walkthrough: boost converter schematic (Vin → inductor → switch → diode → capacitor → Vout)
- `[13:44]` — Component selection for the build (inductors, MOSFET, diode, capacitor, transistor driver)
- `[19:44]` — Breadboard assembly walkthrough
- `[25:00]` — Arduino code explanation and direct port write technique for 30 kHz
- `[25:32]` — Boost converter powered on; oscilloscope confirms ~31 kHz, output reads 240V
- `[26:23]` — LED successfully lit at 240V
- `[27:09]` — Current measurement: LED draws only 0.25 mA vs. 10 mA calculated; discussion of real-world losses
- `[28:28]` — Closing remarks and teaser for follow-up video (charging a 450V capacitor bank)

## Robert's Own Replies
- **On battery power consumption:** Clarifies to a commenter that using a boost converter draws more power from the battery — a battery has a fixed energy store ("a bag of marbles"), and running a higher-current load means you deplete it faster, not that you get more energy out.