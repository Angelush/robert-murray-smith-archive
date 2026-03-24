## Overview
Robert Murray-Smith introduces the circumferential flux motor/generator — a third category of electromagnetic machine alongside the more familiar radial and axial flux designs. He explains the underlying principle (surrounding the magnetic field with a coil, rather than the reverse) and builds a working 3D-printed prototype using serpentine coils and neodymium magnets, demonstrating ~11V open-circuit output. His main takeaway is that the design offers a high power-to-weight ratio with no steel core and extremely simple construction, and he plans to develop it into a wind turbine generator.

## Key Topics
- The three types of electromagnetic machines: radial flux, axial flux, and circumferential flux
- How a solenoid relates to circumferential flux — and how spinning it creates a circumferential motor/generator
- Motion Robotics' claim of building the first practical circumferential flux motor
- Design tradeoff: serpentine coils instead of trapezoidal coils for ease of construction, accepting a small gap in field coverage
- Why the two coils must be rectified before connecting (north/south polarity cancellation)
- Plans to attach a wind turbine rotor to the prototype
- Publishing the design on Thingiverse as a work in progress

## Materials and Chemicals Mentioned
- **Neodymium magnets** (5 mm × 15 mm, arranged north–south alternating) — used as the magnetic rotor
- **Silicon steel** — mentioned as what conventional motors use (and what this design avoids)
- **3D-printed PLA/plastic parts** — five printed components form the entire frame and rotor
- **Skateboard bearings** (22 × 8 × 7 mm) — used in the coil holders
- **Downing needle** — used as the main thrust/pivot bearing on the axle
- **Enamelled copper wire** — 0.2 mm cross-sectional area, 1,000 turns per coil (confirmed in comments)
- **Black plastic tape** — used to mark and shape the serpentine coil star bends
- **Metal washer / trimming knife blade** — glued to the base as a bearing surface for the needle

## Techniques and Methods
- **Serpentine coil winding** — coils wound flat using a serpentine coil winder (covered in a separate video)
- **Star-shaping the coil** — bending the flat serpentine coil into a star form to fit the circular coil holder
- **Bridge rectification** — fitting a rectifier bridge to each coil output before connecting them in series or parallel
- **3D printing** — entire mechanical structure (frame, foot, magnet disc rotor, coil holders, axle) produced by FDM printing
- **Needle-point bearing** — using a darning/downing needle pressed into a metal plate as a low-friction pivot
- **Open-circuit voltage testing** — spinning the rotor by hand and reading voltage with a multimeter (11 V demonstrated)

## Notable Timestamps
- `[00:00]` — Introduction: motors and generators as simple coil-and-magnet machines
- `[01:28]` — Explanation of radial flux motors
- `[01:43]` — Introduction of axial flux motors
- `[02:17]` — Introduction of circumferential flux as the third motor type; solenoid analogy
- `[03:03]` — Spinning the solenoid to create a circumferential motor/generator; mention of Motion Robotics
- `[03:57]` — Robert's decision to design a circumferential flux generator in Tinkercad
- `[04:38]` — Overview of the five 3D-printed parts
- `[05:34]` — Assembly: bearings, magnet rotor, coil holders
- `[06:01]` — Serpentine coil winding and star-shaping process
- `[07:57]` — First spin test with voltmeter reading ~11 V
- `[08:18]` — Conceptual comparison: axial flux surrounds coil with field; circumferential surrounds field with coil
- `[09:32]` — Discussion of why rectifiers are needed before combining the two coils
- `[10:01]` — Benefits summary: no steel, no Halbach arrays, high power density, fully 3D-printable
- `[10:37]` — Future plan: wind turbine rotor attachment; Thingiverse publication

## Robert's Own Replies
Robert was active in the comments and added several important clarifications:

- **Core conceptual distinction (repeated multiple times):** "Axial flux attempts to surround the coil with a magnetic field; circumferential flux attempts to surround the magnetic field with a coil of wire — that's it really." He used this phrasing repeatedly to correct misunderstandings.
- **Why the prototype differs from a true circumferential design:** He acknowledged his serpentine-star coil does not fully wrap around the field (there is a gap for the axle) but defended the tradeoff: *"the ease of construction of this way is actually worth the little bit that we are in fact losing."* He noted Motion Robotics' design also doesn't fully encircle the field.
- **Coil winding spec:** confirmed 1,000 turns per coil of 0.2 mm CSA wire.
- **Power clarification:** told a commenter the design won't magnify power — output depends entirely on the input driving it.
- **Making it 3-phase:** noted it would be *"stunningly easy"* to make the design 3-phase, pointing to his existing serpentine coil 3-phase video.
- **Adding commutation for motor use:** acknowledged commutation would be needed to run it as a true motor.
- **Heating copper with rotating magnets:** confirmed that quickly rotating magnets under a copper plate will cause heating, but speed is critical.
- **On the value of actually building things:** repeatedly encouraged commenters to build rather than just theorise: *"do you know mate — you really should just try building some of your ideas, it says so much more and answers so many more questions."*
- **His honest assessment of Motion Robotics' claims:** *"I suspect there isn't that much difference between what they have made and an axial flux design"* — taking a pragmatic, sceptical but fair view.