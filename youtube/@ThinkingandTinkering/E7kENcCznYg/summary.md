## Overview
Robert demonstrates how to repurpose a cheap £7 optical mouse as a high-resolution position sensor for a friction-drive 3D printer mechanism. Because friction drives can slip — unlike gears or stepper motors — the print head position cannot be inferred and must be read directly. He shows that an optical mouse's tiny camera chip already does this work, outputting delta-X and delta-Y values that can be read via an Arduino with minimal wiring and a freely available library.

## Key Topics
- Friction drive mechanism for a novel 3D printer and its inherent slip problem
- Why slip makes position inference impossible, requiring a direct sensor
- How optical mice work: continuous image comparison to compute X/Y delta movement
- Disassembling a PS2 optical mouse and identifying the useful components
- Identifying PS2 connector pinout (data, clock, ground, 5V) using a multimeter
- Wiring the mouse to an Arduino (data → pin 2, clock → pin 3)
- Setting up the Arduino IDE with the "getis" PS2 mouse handler library
- Reading live X/Y movement data over the serial monitor
- Resolution analysis: ~0.024 mm per count (1000 DPI), well within 3D printing needs
- Establishing a home position and accumulating deltas to derive absolute position
- Repurposing the mouse's onboard switches as a homing microswitch
- Broader applications: gaming chairs, steering wheel sensors, and other position-sensing uses

## Materials and Chemicals Mentioned
- PS2 optical mouse (£7; brand noted in comments as FANACAN)
- Arduino microcontroller
- Multimeter (used in resistance mode for pin identification)
- Jumper wires with pin connectors
- Microswitch (proposed replacement for mouse buttons to act as a home switch)

## Techniques and Methods
- Disassembly of a PS2 optical mouse (single screw)
- Multimeter continuity/resistance testing to map wire colours to PS2 pins
- Cutting and re-soldering the PS2 cable with Arduino-compatible pin connectors
- Arduino IDE library installation via zip import (Sketch → Include Library → Add ZIP Library)
- Modifying example sketch pin assignments (changed from pins 5/6 to 2/3)
- Serial monitor readout at 9600 baud to observe real-time X/Y delta values
- Cumulative position tracking: home to zero, then sum incremental changes for absolute position
- Desoldering mouse switches and relocating a microswitch to serve as a homing trigger

## Notable Timestamps
- `[00:08]` — Introduction to the novel 3D printer drive mechanism
- `[00:31]` — Problem stated: friction drives can slip, making position inference unreliable
- `[01:43]` — Optical mouse introduced as the low-cost solution
- `[02:11]` — Mouse opened; camera and electronics explained
- `[04:04]` — PS2 connector pinout identified with a multimeter; wiring to Arduino described
- `[06:42]` — Arduino IDE setup: downloading the IDE and installing the getis mouse library
- `[08:47]` — Live demo: serial monitor shows 0,0 at rest, then live X/Y deltas on movement
- `[09:16]` — Resolution calculated: ~0.024 mm, an order of magnitude finer than a 0.2 mm print layer
- `[09:54]` — Home position concept explained; cumulative delta summation for absolute position
- `[10:57]` — Plans to integrate sensor into the 3D printer assembly via custom 3D-printed mount

## Robert's Own Replies
Robert's comment replies are mostly brief acknowledgements, but a few contain useful clarifications:
- **Homing and drift**: Confirmed that mechanical systems will drift, and that homing (returning to a known zero point) is the intended mitigation; noted that "gabriel has the answer to that" for managing drift.
- **Polling and accuracy**: Suggested that positional accuracy depends on two factors — how frequently the sensor is polled and how frequently the system returns to home.
- **Capacitive calipers**: Clarified (in response to a commenter) that many digital calipers use a capacitive sensor rather than a camera.
- **Mouse brand**: Identified his mouse as branded **FANACAN**.
- **Multiple sensors on one Arduino**: Confirmed it is possible to run multiple mouse sensors from a single Arduino.
- **Luke's gaming chair project**: Confirmed this sensor approach will be used by a collaborator (Luke) for a gaming chair with position and steering wheel sensors.