## Overview
A short practical tutorial on using relay shields with Arduino boards to automate switching. Robert demonstrates how to identify the control pins on an undocumented cheap relay shield by inspecting PCB traces, then uses a freely available Arduino sketch to control the relays — part of his broader project to automate an electrode-making machine.

## Key Topics
- Arduino relay shields and how they stack onto Arduino boards
- Identifying control pins on undocumented/cheap relay shields by reading PCB traces
- Using the Arduino IDE (online and desktop) to upload sketches
- Modifying a sketch to toggle a relay on and off on a timed cycle
- Using a multimeter to verify relay operation (common vs normally open pins)

## Materials and Chemicals Mentioned
- Arduino board
- 4-relay shield (and mention of 2-relay shield variants)
- Multimeter

## Techniques and Methods
- Visual inspection of PCB traces on the underside of the shield to identify control pins
- Uploading and modifying Arduino sketches via the Arduino IDE
- Using a multimeter set to resistance mode to test relay switching (common to normally open)
- Iterating through pin assignments in code to map pins to relay LEDs

## Notable Timestamps
- `[00:15]` — Introduction: goal is to automate an electrode-making machine using Arduino
- `[00:33]` — Explanation of Arduino shields and the 4-relay shield being used
- `[01:09]` — Problem: cheap shields come without pin-out documentation
- `[01:39]` — Solution: flip the shield over and read PCB traces to find control pins (pins 4–7)
- `[02:37]` — Using a free public-domain sketch from the Arduino Hub
- `[03:31]` — Demo: changing pin in sketch lights up corresponding relay LED
- `[04:09]` — Using a multimeter to identify relay terminals if labels are absent
- `[05:01]` — Modifying the sketch to toggle the relay on and off repeatedly
- `[05:13]` — Final demo: relay cycling every couple of seconds

## Robert's Own Replies
No author replies found.