## Overview
Robert Murray-Smith demonstrates how to build a functional stepper motor from 3D-printed parts, neodymium magnets, a hand-wound solenoid, and skater bearings. He explains the core electromagnetic principles behind motor operation and shows how an H-bridge relay circuit can automate the reversal of current to drive rotation. The video concludes with a working motor controlled by a manually-triggered relay, and previews a follow-up video on automated timing signals.

## Key Topics
- 3D-printed motor construction (parts available on Thingiverse)
- Electromagnetic principles of motor operation (solenoid magnetism, pole attraction/repulsion)
- H-bridge circuit using a relay to swap current direction
- Ratchet-and-pawl mechanism for ensuring consistent rotational direction
- Stepper motor fundamentals: step angle (30° per step with 12 magnets), duty cycle, timing
- Future timing signal options: 555 timer, Arduino, pendulum
- Applications: clocks, robots, 3D printer motor controllers

## Materials and Chemicals Mentioned
- **Neodymium (nearium) magnets** — 15 mm × 5 mm, 12 used, arranged N-S alternating around rotor ring
- **Skater bearings** — 22 mm × 8 mm × 7 mm, pressed into stand
- **M10 bolt** — 70 mm long, used as the solenoid core
- **Copper wire** — wound around the bolt to form the solenoid coil
- **Super glue** — for securing magnets in the ring
- **Rubber band** — used as a return spring for the ratchet pawl
- **Relay (DPDT)** — acts as H-bridge switches; any DPDT relay is suitable
- **DC power supply** — 6 V DC (later clarified in comments as 12 V DC bench supply)

## Techniques and Methods
- **3D printing** — printing rotor ring, stand, cradle, ratchet, and pawl from Thingiverse files
- **Solenoid winding** — wrapping copper wire around an M10 bolt to create an electromagnet
- **H-bridge wiring** — using a DPDT relay to reverse polarity across the solenoid coil
- **Ratchet-and-pawl mechanism** — aligning tooth to magnet position to lock clockwise-only rotation
- **Manual switch triggering** — pressing a button to pulse the relay coil as a timing signal

## Notable Timestamps
- `[00:08]` — Introduction; overview of printed parts needed
- `[00:18]` — Installing neodymium magnets into rotor ring (N-S alternating pattern)
- `[00:30]` — Assembling stand with skater bearings and rotor components
- `[01:06]` — Introducing the solenoid (M10 bolt with copper wire winding)
- `[01:16]` — Explaining solenoid magnetism and DC current direction
- `[02:02]` — Demonstrating pole attraction/repulsion causing rotation
- `[03:14]` — Introducing the H-bridge concept using a relay
- `[04:23]` — Introducing the ratchet-and-pawl mechanism for directional control
- `[05:08]` — Full assembly with H-bridge relay and ratchet in place
- `[06:01]` — Live demonstration of the motor stepping under manual switch control
- `[06:25]` — Confirming the stepper motor works; explaining 30° steps and 50% duty cycle
- `[07:03]` — Discussing alternative timing signals (555 timer, Arduino, pendulum)
- `[07:27]` — Closing remarks on applications (clocks, robots, 3D printers)

## Robert's Own Replies
- **Component flexibility:** Robert emphasises using any DPDT relay, any gauge of copper wire (up to ~0.5 mm), any suitable bolt, and any similarly-sized magnets. He intentionally avoids specifying exact part numbers because availability varies globally and goes out of production.
- **Omitted refinements (deliberate simplification):** He notes he left out a freewheeling diode across the solenoid coil (to suppress back-EMF spikes) and snubber circuits (to reduce contact arcing) to keep the build simple, but acknowledges these would improve reliability.
- **Ratchet necessity:** Without the ratchet, rotor inertia causes a "bounce" effect that mis-positions the magnets relative to the solenoid, so the locking mechanism is essential.
- **Rotor direction:** The slight bounce from inertia actually pushes the ratchet tooth just past dead centre, so the path of least resistance is always clockwise — ensuring consistent rotation.
- **Power supply:** The bench supply is set to 12 V DC (not a special or exotic source).
- **Timing control:** He confirms an Arduino is the recommended next step for automated timing, and plans a dedicated follow-up video on timing signals.
- **3D-printed ratchet:** He tried printing the ratchet but found tolerances too loose, causing the rotor to lose position; a commercially manufactured ratchet with tighter tolerances may work better.
- **Broader potential:** Robert agrees with commenters that the design has applications well beyond clocks — including robots and precision positioning systems.