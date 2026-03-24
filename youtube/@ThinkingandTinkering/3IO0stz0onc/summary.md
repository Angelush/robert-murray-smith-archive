## Overview
In Part 2 of his human hamster wheel generator build, Robert Murray-Smith attaches a NEMA stepper motor to the existing wheel via a longboard wheel friction drive, achieving a 100:1 gear ratio. Testing produces 68–77 volts and roughly 50–60 watts from a single motor, and Robert concludes that matching gear ratio to available human torque — not the choice of motor — is the critical factor in generator performance.

## Key Topics
- Selecting and mounting a motor to convert the hamster wheel into a generator
- Gear ratio design (100:1 total: 25:1 big wheel to longboard wheel, then 4:1 to stepper)
- Live voltage and current measurements under two load types
- Comparison of stepper motor vs. hoverboard motor performance
- Projections for scaling output with multiple motors (up to ~240W with four)
- The physics of weight-driven vs. muscle-driven machines
- Human power limits: ~200W for an average person, ~300W for an athlete

## Materials and Chemicals Mentioned
- **NEMA stepper motor** — used as the generator; ~90% efficient
- **Hoverboard motor** — considered but not used; ~80% efficient; only achieved ~12W at 12:1 gear ratio
- **Longboard wheel** — intermediate friction drive element
- **Flexible coupling** — connects stepper motor shaft to longboard wheel
- **Rubber tape** — wrapped around the coupling for grip
- **Stacked wood** — used to raise the motor to the correct height
- **LED string (~35V)** — used as one test load
- **Filament light bulb** — used as a resistive test load
- **DC-DC converter board** (~£1.30, handles 70V→12V) — mentioned in comments as a way to stabilise output voltage

## Techniques and Methods
- Friction drive coupling (motor pressed against spinning longboard wheel)
- Gear ratio calculation and matching to human torque output
- Stacking wood blocks for rapid motor height adjustment
- Live load testing with voltage and current meter (phone camera recording meter display)
- Comparative motor benchmarking (stepper vs. hoverboard motor at different gear ratios)

## Notable Timestamps
- `[00:10]` — Decision to add a generator; overview of motor options including hoverboard motor
- `[00:28]` — Chooses NEMA stepper motor; describes flexible coupling and rubber tape grip
- `[00:49]` — Shows completed motor mount (stepper glued to wood stack, pressed against longboard wheel)
- `[01:06]` — Explains the 100:1 gear ratio (25:1 × 4:1)
- `[01:47]` — First live spin: voltage reads 68–77 V
- `[02:16]` — Current measurement: ~0.8 A; estimates ~50–60 W output
- `[02:35]` — Speculates on adding 2–4 motors for up to ~240 W
- `[02:50]` — Explains why gear ratio is the dominant factor
- `[03:00]` — Compares to hoverboard motor: 12:1 ratio → ~12 W (~1/5 of stepper output)
- `[03:42]` — Wraps up: gear ratio + torque matching = good generator design

## Robert's Own Replies
Robert added several important clarifications in the comments:

- **The real lesson is about torque, speed, and gearing:** *"This video isn't really about a hamster wheel — it's really about the relationship between torque and speed and the role of gearing."*
- **It's a weight-driven machine:** The wheel's mass acts as its own flywheel, and the rider is largely moving their own weight rather than purely applying muscle power. *"Weight is doing a lot of the work."*
- **Human power, not motor choice, is the bottleneck:** Counter-torque limits output to ~200W for most people and ~300W for athletes, largely independent of which motor is used. *"You just couldn't turn it at 750 rpm to get 600W — no one has that strength."*
- **Motor efficiency matters, but not dramatically:** Brushed DC ~70%, hoverboard motor ~80%, stepper ~90%, axial flux ~93% — so upgrading from stepper to axial flux would only gain ~3%.
- **Voltage stabilisation:** A £1.30 DC-DC converter board (70V→12V) could smooth the variable output for practical use.
- **Diodes are essential** when connecting the generator output to a load/circuit.
- **Real-world precedent:** A similar human-powered wheel exists in the kids' playground at the Birmingham Science Museum.