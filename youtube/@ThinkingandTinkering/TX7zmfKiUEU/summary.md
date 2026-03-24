## Overview
Robert Murray-Smith demonstrates how to convert salvaged PC cooling fans into mini DC generators. He disassembles several fan types (2-wire, 3-wire, and 4-wire), identifies the relevant coil connections (V1 and V2) using the Hall-effect sensor pins, strips away unnecessary electronics, and adds a diode bridge rectifier to produce usable DC output. The video concludes with a successful demonstration lighting an LED using airflow from a hairdryer.

## Key Topics
- Salvaging PC cooling fans as a source of free motors/generators
- Internal structure of BLDC (brushless DC) fans: magnets, coils, Hall-effect sensors
- Disassembly techniques for 2-wire, 3-wire, and 4-wire fan variants
- Identifying V0, V1, and V2 connections via the Hall latch (sensor) circuit
- Building a full-wave bridge rectifier from discrete diodes
- Reassembly and demonstration as a working DC generator

## Materials and Chemicals Mentioned
- PC power supply and laptop cooling fans (2-wire, 3-wire, and 4-wire variants)
- 1N4007 diodes — used to construct the full-wave bridge rectifier
- LED — used as the output load in the demonstration
- Hairdryer — used to simulate wind and spin the fan/generator
- Circlip, O-ring, washers, bearings — internal fan hardware encountered during disassembly

## Techniques and Methods
- Fan disassembly: removing plastic clips, circlips, and washers to separate the rotor (magnet) from the stator (coil board)
- Coil removal: using pliers carefully to twist and press the coil yoke off the central boss without crushing the windings
- Circuit tracing: following Hall-effect sensor (Hall latch) pins 2 and 3 on the PCB to identify V1 and V2 output nodes
- Electronics stripping: snipping or desoldering unwanted components from the stator PCB, leaving only the two required coil output traces
- Bridge rectifier construction: hand-twisting and soldering four 1N4007 diodes into a full-wave rectifier bridge
- Generator testing: driving the fan with a hairdryer and observing LED illumination

## Notable Timestamps
- `[00:15]` — Introduction; Robert describes his collection of scavenged PC fans
- `[01:02]` — Disassembly begins; explains plastic ring, O-ring, and circlip removal
- `[02:17]` — Lifting the rotor off the stator; reveals coil board and spindle magnet
- `[03:00]` — Removing the coil yoke from the central spindle; breaks one before finding the right technique
- `[05:52]` — Explains the common wiring scheme across all fan types (V0, V1, V2)
- `[06:05]` — Schematic description of the Hall-effect sensor connections
- `[09:50]` — Notes the output is AC and explains the need for rectification
- `[10:10]` — Begins building the 1N4007 diode bridge rectifier
- `[12:36]` — Connects LED and hairdryer for the live demonstration
- `[12:57]` — LED lights up — successful demonstration
- `[14:48]` — Summary: all three fan types (2, 3, 4-wire) successfully converted

## Robert's Own Replies
- **Low voltage-drop rectifier recommendation:** Robert advises that using 1N34 (germanium) diodes instead of 1N4007s would be better due to their lower forward voltage drop.
- **Efficiency improvement teaser:** He mentions he has already been looking into improving generator efficiency and found something "fascinating" — a follow-up video is planned.
- **Minimum speed observation:** He agrees with a commenter's observation that the fans seem to have a minimum operational speed, speculating it may relate to inertia.
- **Redundant array of fans (RAID joke):** He humorously endorses the idea of a "redundant array of inexpensive fans," likening it to RAID storage.
- **Arduino integration:** He suggests a digital speed readout using an Arduino as an interesting extension project.
- **General philosophy:** He encourages hands-on experimentation, noting that "if you mess around with stuff then you discover — if you just sit and say oh no… you discover nothing."