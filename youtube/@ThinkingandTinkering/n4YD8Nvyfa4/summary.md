## Overview
Robert demonstrates a switchable permanent magnet (an electropermanent magnet) that can be toggled on and off with a brief current pulse, then explains how this device can be used as the basis for a magnetically assisted switched reluctance motor. Unlike a conventional electromagnet, the device retains its magnetic state without continuous current. The video introduces the concept as a planned project to drive a vehicle, combining the electropermanent magnet switching with standard switched reluctance motor topology.

## Key Topics
- Demonstration of a switchable/electropermanent magnet
- Explanation of magnetic reluctance and keeper paths
- How two dissimilar magnets (Neo and Alnico) interact under pulsed current
- Switched reluctance motor operating principle
- The "magnetically assisted" tweak: replacing electromagnets with electropermanent magnets for efficiency
- Application goal: driving a vehicle (motorbike) using this motor with an EESD

## Materials and Chemicals Mentioned
- **Neodymium (Neo) magnet** — hard magnetic material; holds polarity under pulse without switching
- **Alnico (AlNiCo) magnet** — soft magnetic material; changes polarity when pulsed, enabling switching
- **Transformer laminations (scrap steel)** — used as magnetic keepers/yokes
- **Copper wire** — wound as the coil (~200 turns for the demo unit)

## Techniques and Methods
- Pulsing DC current in alternating directions through a coil to switch the polarity of the Alnico magnet
- Using magnetic keepers to redirect flux internally (off state) or externally (on state) via path-of-least-reluctance routing
- Sequential switching of multiple stator poles to rotate a toothed rotor — switched reluctance motor drive
- Winding coils by hand (~100–200 turns depending on magnet size and supply voltage)
- Finite element modelling (mentioned as the next planned analysis step)

## Notable Timestamps
- `[00:06]` — Introduction; mentions a large-scale EESD drying in background
- `[00:27]` — First demonstration: device has no magnetism until pulsed
- `[00:48]` — Shows device retains magnetism after current is disconnected
- `[01:05]` — Reverses leads; pulse removes magnetism — confirming switchable behaviour
- `[01:54]` — Whiteboard/diagram explanation of internal flux paths and keeper operation
- `[02:25]` — Identifies the two magnet materials: Neodymium (hard) and Alnico (soft)
- `[03:32]` — Diagram of switched reluctance motor topology with toothed rotor
- `[04:04]` — Explains sequential pole switching to achieve continuous rotation
- `[05:11]` — States the goal: build a magnetically assisted switched reluctance motor to drive a vehicle
- `[06:37]` — Construction walkthrough: dimensions, assembly, and coil winding instructions

## Robert's Own Replies
- **Power supply**: Used a 6V supply for the demo; recommends 24V for larger magnets, with more turns and thinner wire to compensate (fewer volts → more turns).
- **Coil spec**: ~200 turns for a half-inch × 1/8-inch magnet; 100 turns at 12V was also mentioned as workable.
- **Motor classification**: Repeatedly clarified this is a **switched reluctance motor** with a hard/soft magnet tweak — not a permanent magnet motor, not an induction motor, and not over-unity. Drive system is similar to a **BLDC motor**.
- **Planned build**: ~50–100 poles; intends to drive it like a BLDC motor; planning to put it in a **motorbike**.
- **Known challenges**: Hard magnet demagnetisation and heat generation are the expected problem areas; gap distance is critical (inverse square law).
- **Next steps**: Finite element modelling before further build work; also exploring alternative soft magnetic materials.
- **Prior art**: Linked to the Wikipedia article on electropermanent magnets and an MIT master's thesis that thoroughly explored this motor type.
- **Open source intent**: Stated he plans to pursue this openly rather than seeking patents.