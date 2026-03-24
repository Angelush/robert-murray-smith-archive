## Overview
Robert Murray-Smith demonstrates how to repurpose the brushless motors found inside old VCR/DVD combo units to build a simple micro wind turbine and energy harvester. He extracts the capstan pulley motor, attaches a three-phase bridge rectifier to convert the AC output to DC, and mounts a squirrel cage fan rotor on it to capture airflow. The main takeaway is that storing harvested energy in a supercapacitor is a valid and practical way to measure and use the output, contra common criticism of voltage-only readings.

## Key Topics
- Salvaging brushless DC motors from discarded VCR/DVD combo units
- Converting a brushless motor into a generator by adding a three-phase bridge rectifier
- Mounting a squirrel cage rotor for wind energy capture
- Using a supercapacitor as an energy store to demonstrate real usable output
- Alternative rotor designs (Pelton wheel, propeller, VAWT) for the same generator base

## Materials and Chemicals Mentioned
- **VCR/DVD combo unit** — donor device for salvaging motors
- **Brushless DC motor** (capstan pulley / flat pancake profile) — repurposed as generator
- **Three-phase bridge rectifier** (6 diodes) — converts three-phase AC from motor coils to DC
- **Squirrel cage fan rotor** — attached to generator shaft for wind capture
- **500 F, 2.7 V supercapacitor** — used as energy storage to demonstrate real output
- **Small DC motor** — used to demonstrate stored energy doing real work

## Techniques and Methods
- Disassembly of VCR/DVD unit to extract brushless motor components (capstan pulley, tape head drum)
- Identifying the three coil endpoints (Y-configuration) on the motor's circuit board
- Removing existing electronics and soldering three lead wires to the coil ends
- Wiring a three-phase bridge rectifier to the coil outputs to produce DC
- Mounting a squirrel cage rotor on the generator shaft using a pipe for handling
- Charging a supercapacitor from the generator output and measuring stored joules via capacitor voltage

## Notable Timestamps
- `[00:15]` — Introduction; shows the donor VCR/DVD recorder and explains where to find them
- `[00:31]` — Opens the unit; identifies the carriage return, tape head drum, and capstan pulley
- `[01:20]` — Explains that the capstan pulley is actually a flat pancake brushless motor
- `[02:10]` — Describes converting the motor into a generator; references his dedicated brushless motor video
- `[02:50]` — Shows the modified motor: circuit board removed, three coil wires soldered, rectifier attached
- `[03:15]` — Lists alternative rotor ideas: Pelton wheel, propeller, VAWT
- `[03:48]` — Reveals the assembled unit with squirrel cage rotor and pipe mount
- `[04:52]` — Hairdryer test produces ~1.6 V output
- `[05:34]` — Switches to supercapacitor demonstration; charges cap and watches voltage rise
- `[06:57]` — Discharges supercapacitor into a small motor to prove real stored energy
- `[07:15]` — Explains how to calculate stored joules from capacitor voltage

## Robert's Own Replies
- **Three-phase rectifier wiring:** Clarifies the rectifier circuit is 6 diodes in series/parallel and points to a specific timestamp (1:36) in his brushless DC motor video for the exact circuit.
- **On measuring generator output with a capacitor vs. a resistor:** Acknowledges the point that a resistor load is the standard method, but defends the capacitor approach — he is demonstrating a *principle*, not attempting to prove large power output, so precision load-matching is not the priority here.
- **On energy release and circuit load:** Notes that the energy released at any given moment depends on the load the circuit presents; the supercapacitor *is* the load in this demonstration.
- **On commercial wind turbine ratings:** Strongly endorses looking at the watts-at-a-given-wind-speed profile rather than trusting box claims; advises matching a generator's profile against your area's average windspeed for realistic lifetime estimates.
- **On using a store vs. direct load:** Confirms that in real-world generator systems, generators are almost always attached to a store and the load draws from the store — exactly what the supercapacitor demo models.