## Overview
Robert Murray-Smith explains how to run brushless hard drive disc (HDD) motors by treating them as three-phase stepper motors, driven from a single-phase AC supply. The video covers both the theory of Delta and Y (Wye) motor wiring configurations and a live demonstration using a sound card signal generator and amplifier. The key takeaway is that adding a capacitor across the free leg of a Y-configured HDD motor converts it to self-starting and smoother-running, with direction controlled by which leg the capacitor is bridged across.

## Key Topics
- HDD motors as three-phase stepper motors
- Delta vs. Y (Wye) wiring configurations for three-phase motors
- Running a three-phase motor from single-phase AC supply
- Using a capacitor to create a phase shift and enable self-starting
- Start capacitor vs. run capacitor for high-torque starting
- Identifying the common contact on a 4-pin HDD motor using an ohmmeter
- Speed control via frequency (using a sound card signal generator)
- Practical alternatives: transformer + capacitor, or RC ESC digital controller
- Application to a large Tesla disc drive turbine build

## Materials and Chemicals Mentioned
- 400 nanofarad capacitor (run capacitor bridged across the free leg)
- Start capacitor (switched, for high start torque)
- Transformer (to step mains voltage down to ~3–12 V range for the motor)

## Techniques and Methods
- Identifying the common pin on a 4-wire HDD motor using an ohmmeter (lowest resistance = common)
- Single-phase AC drive of a Y-configured three-phase motor (two legs energised, one dropped out)
- Capacitor phase-shift technique: bridging a capacitor across the free coil leg to create a synthetic third phase
- Direction reversal by switching which leg the capacitor bridges to
- Capacitor sizing rule of thumb: `78 × motor kilowatt draw` gives a target capacitance value
- Voltage balancing across coils: measure voltage across each coil and adjust capacitance until roughly equal
- Using a freeware sound card oscilloscope/signal generator (Zelscope/"snits" software) as a variable-frequency AC source
- Amplifying the signal card output with a Pro 200 amplifier (~12 W) to drive the motor
- Alternative digital control via RC car ESC (Electronic Speed Controller)

## Notable Timestamps
- `[00:04]` — Introduction: context of the Tesla disc turbine project and why Robert needed to learn to run HDD motors
- `[01:10]` — Whiteboard theory: three-phase motor basics, 120° coil spacing
- `[01:44]` — Delta configuration explained
- `[02:14]` — Y (Wye) configuration explained
- `[02:39]` — Running a three-phase motor from single-phase AC; the "lumpy" dropout problem
- `[03:18]` — Capacitor phase-shift solution to smooth out dropout
- `[04:46]` — Start capacitor + run capacitor for overcoming low starting torque
- `[05:42]` — Practical look at real HDD motors; identifying 3-pin vs. 4-pin variants
- `[06:06]` — Ohmmeter method to find the common pin
- `[07:06]` — Live demo: motor spinning without capacitor at 50 Hz (not self-starting, ~3,600 RPM)
- `[07:54]` — Capacitor (400 nF) added; direction-control explanation
- `[08:40]` — Live demo: motor self-starts at 45 Hz with capacitor in place
- `[09:09]` — How to work out and fine-tune capacitor value; transformer-based mains alternative
- `[09:47]` — Mention of RC ESC digital controller as an alternative drive method
- `[10:06]` — Plans to scale up to a large Tesla disc drive

## Robert's Own Replies
- **Controller board for automation:** Suggests a Raspberry Pi or Arduino as a controller board for driving the motor digitally.
- **Software identification:** Confirms the oscilloscope/signal generator software is a freeware program (referred to as "scope").
- **Safety disclaimer:** Explicitly states that attempting this is at the viewer's own risk and the video is for information only, not advice.
- **Hall effect sensor interest:** Mentions considering a hall effect latch for motor position sensing in a follow-up implementation.
- **Design philosophy:** Describes his approach as deliberately "super simple, non-frightening, almost plug and play" — technical complexity is deferred to later videos.
- **Off-topic but notable:** Discusses phosphorene and molybdenum disulphide as interesting 2D sheet-like materials in an unrelated comment thread, showing his broader materials science interests.