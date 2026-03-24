## Overview
This video explains how to determine the correct wire gauge and number of turns when designing a coil for a small wind turbine generator. Robert demonstrates the reasoning process — starting from expected power output and working through voltage, current, and wire capacity — and introduces a simple custom-built coil winding machine he designed to handle very fine wire at high turn counts.

## Key Topics
- How to calculate expected power output from a small wind turbine using Omni Calculator
- Faraday's law of electromagnetic induction as the basis for voltage generation
- The relationship between number of turns and output voltage (volts per turn)
- Why wire thickness affects current capacity but not voltage
- Choosing wire gauge based on expected current (milliamps), not voltage
- Design and use of a custom laser-cut coil winding machine for thin wire
- Serpentine coil geometry and how coil dimensions are derived from magnet spacing
- Design recap: a step-by-step rule-of-thumb workflow for generator coil design

## Materials and Chemicals Mentioned
- **32 SWG (Standard Wire Gauge) enamelled copper wire** — very thin "hair-thin" wire chosen for its ability to carry ~300 mA while allowing many turns
- **Thicker wire (unspecified gauge)** — used in earlier 200-turn prototype coil
- **Electrician's tape (19 mm width)** — used to bind the finished serpentine coil
- **8 mm bolt (~30 mm long)** — axle for the coil winding machine
- **22 mm skate bearing** — pivot for the winding machine spindle
- **Rectifier diodes (3 A, 1000 V)** — mentioned in comments as protection for generator coils on a shared bus

## Techniques and Methods
- **Empirical volts-per-turn measurement** — winding a test coil, running it at known wind speed, and measuring output voltage to derive a volts-per-turn constant
- **Power-first coil design** — estimating expected wattage, dividing by target voltage to find required current, then selecting wire gauge accordingly
- **Serpentine coil winding** — winding wire around a circular former to produce a flat, circular coil rather than a solenoid
- **Custom coil winding machine (laser-cut)** — a hand-cranked device with a guide hole, coil former, and skate-bearing pivot; designed for fine wire at 1000+ turns
- **Coil dimension calculation** — multiplying (tape width + magnet center-to-center spacing) by the number of magnets/lugs to get the required coil circumference
- **Tape-and-peel coil removal** — wrapping finished coil in tape through the former gaps, removing the former top, and peeling the coil off

## Notable Timestamps
- `[00:00]` — Introduction: working on a redesigned generator prototype
- `[00:41]` — Using Omni Calculator to estimate wind turbine power output (~80 mW for a 100 mm turbine at 4.5 m/s)
- `[01:16]` — Faraday's law explained; voltage calculation per turn
- `[01:36]` — Empirical test: 200-turn coil produces ~4 V → ~0.02 V/turn
- `[02:36]` — Key insight: wire thickness affects current capacity only, not voltage
- `[03:21]` — Choosing 32 SWG wire (rated ~300 mA) for 1000-turn coil targeting ~20 V output
- `[04:14]` — Introduction of the coil winding assistant designed by "Peter / Grelle"
- `[05:11]` — Walkthrough of Robert's custom coil winding machine design (TinkerCAD)
- `[07:01]` — Live demonstration of threading and winding hair-thin wire
- `[09:00]` — Explaining how coil dimensions are calculated from magnet count and tape width
- `[09:33]` — Design recap: power → volts/turn → turn count → amps → wire gauge

## Robert's Own Replies
- **Three-phase vs. single-phase**: Robert confirms he has built three-phase generators; single-phase is used mostly for simplicity of demonstration. Three-phase is simply three identical coils placed 120 electrical degrees apart.
- **Dump load / sand battery**: A turbine can be connected to a resistive heater as a standard "dump load" to prevent battery overcharging in high wind. An electric heating element in a bucket of sand is effectively a sand battery.
- **Bus protection for multiple generators**: With 25 generators at 10 mA each, the bus carries only 250 mA max. Each coil is protected by a 3 A / 1000 V rectifier (diode bridge), so the bus cannot back-feed a coil. An additional diode can be added if desired.
- **Soldering fine wire**: Robert dislikes soldering hair-thin wire; his technique is to abrade the surface with very fine grit sandpaper and coat it in flux before soldering.
- **Counter idea from a commenter**: A commenter suggested a hub-based counter; Robert confirmed this solved a problem he was already pondering and plans to add one.
- **Microinverters**: Mentioned as a growing trend in solar worth looking into.
- **General encouragement**: Repeatedly encouraged commenters to just build something — learning principles through practice, even at small scale, transfers to larger projects.