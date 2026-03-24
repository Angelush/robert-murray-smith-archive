## Overview
This video introduces the fundamental design principles of wind turbines, focusing specifically on the rotor — the bladed component responsible for capturing wind energy. Robert explains that the primary performance metrics for a rotor are rotational speed and torque (not volts or amps), and walks through how to calculate, model, or measure these values to evaluate rotor efficiency against theoretical limits.

## Key Topics
- The three essential components of a wind turbine: rotor, generator, and tower
- Wind power fundamentals: force proportional to area and the cube of wind speed
- Why rotor design is evaluated in terms of torque and RPM, not electrical output
- Static vs. dynamic torque, and how to measure each
- Using online calculators (specifically Omni Calculator) for theoretical torque/RPM targets
- Methods for measuring rotor performance: calculation, finite element modelling, and physical testing
- The Prony brake as a DIY tool for measuring dynamic torque
- The two design "camps": rotor/mechanical capture vs. generator/electrical conversion
- Overview of advanced capture concepts: shrouded turbines, Power Pod, buffeting-wind designs, and effective aperture vs. physical aperture

## Materials and Chemicals Mentioned
- Wood (a lump of wood used to demonstrate wind push/drag; an 8×4 sheet, 2.4 × 1.2 m, as an extreme example)
- A small DC motor (used as a low-resistance demonstration)
- A treadmill DC motor (used to demonstrate high starting torque requirements)

## Techniques and Methods
- **Theoretical calculation from first principles** — deriving torque and RPM mathematically
- **Online calculator (Omni Calculator)** — used to find theoretical torque/RPM targets (example result: 0.25 N·m at 500 RPM)
- **Finite element analysis (FEA) modelling** — modelling rotor performance before building
- **Physical testing** — measuring wind speed, shaft RPM (with an RPM meter), and torque in real conditions
- **Static torque measurement** — bolting a rod to the shaft and pressing against a weighing scale to derive N·m
- **Prony brake** — a DIY device for measuring dynamic (rotational) torque
- **Efficiency comparison** — comparing measured torque/RPM against theoretical calculator values

## Notable Timestamps
- `[00:15]` — Introduction: wind turbines are simple at their core; three essential components explained
- `[01:25]` — Wind push demonstrated with a piece of wood; force proportional to area
- `[02:44]` — Key insight: available wind power is fixed by wind speed and capture area
- `[03:37]` — Rotor design goal stated: maximise capture of push and convert it to turning force (torque)
- `[04:09]` — Treadmill motor demonstrated; starting torque as the minimum rotor requirement
- `[05:16]` — Four methods for determining rotor speed and torque introduced
- `[06:06]` — Omni Calculator example: 0.25 N·m at 500 RPM as theoretical target
- `[07:02]` — Static vs. dynamic torque explained; Prony brake introduced
- `[08:56]` — Two design camps: mechanical wind capture (rotor side) vs. electrical conversion (generator side)
- `[09:51]` — Wind power scales as the cube of wind speed; effective capture area discussion
- `[10:47]` — Outro; generator topic deferred to a future video

## Robert's Own Replies
- **On connecting a BLDC motor as the generator:** Robert notes that fitting a BLDC (brushless DC) motor in the generator position yields three-phase output.
- **On tail fins:** He believes a tail would still be needed even in alternative designs.
- **On location:** Confirms that turbine siting/location does matter.
- **On blade design:** Advises building what you think is good and then testing it empirically — "make what you think is good then try it."
- **On voltage/amps vs. torque/speed:** Clarifies that while electrical output matters, you first need to understand torque and speed or the electrical figures are meaningless.
- **On shrouding/enclosure:** Notes it is "sometimes" relevant but "not a crucial element."
- **On a commercial turbine shared by a commenter:** Acknowledges it produces 120–250 W at 24 V.