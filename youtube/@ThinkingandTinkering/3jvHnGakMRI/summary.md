## Overview
Robert Murray-Smith explores whether the "flying gyroscope" toy — a spinning ring that generates lift when thrown — could function as a wind turbine. He designs 3D-printed models in TinkerCAD using an NACA 2414 airfoil profile, tests variants with bumps on the outside vs. inside and with/without fins, and concludes that a simple cylinder with internal fins and bump on the outside shows the most practical promise for integration into a low-cost wind turbine.

## Key Topics
- The flying gyroscope toy and its lift-generating aerodynamics
- Designing a toroidal/ring-wing airfoil shape in TinkerCAD using SVG revolve
- Comparing bump-outside vs. bump-inside airfoil configurations
- Static torque measurements to evaluate performance
- The role of lift-induced drag vs. parasitic drag in ring-wing designs
- Adding fins to reduce turbulence and set rotation direction
- Practical considerations for converting the design into a functional wind turbine (magnets, coils, wind wall mounting)

## Materials and Chemicals Mentioned
- None mentioned.

## Techniques and Methods
- 3D modelling in TinkerCAD using the SVG Revolver tool to create a toroidal airfoil from an NACA 2414 profile
- Importing/exporting STL and SVG files with 100,000% scaling to avoid distortion
- Static torque measurement using a fan and gram-force readout to compare rotor variants
- Addition of fins (external and internal) to improve directional rotation and reduce turbulence
- Proposed integration with ring-mounted magnets and a coil for electricity generation

## Notable Timestamps
- `[00:08]` — Introduction to the flying gyroscope toy and its lift properties
- `[01:08]` — TinkerCAD modelling workflow begins using NACA 2414 airfoil from Thingiverse
- `[01:48]` — SVG Revolver technique demonstrated to create toroidal shape
- `[03:40]` — Two variants created: bump on outside vs. bump on inside
- `[04:18]` — Static torque test with fan; bump-outside scores 1.6, bump-inside scores 1.2
- `[04:44]` — Discussion of lift-induced drag vs. parasitic drag in ring-wing designs
- `[05:41]` — Fins added to the design; re-test shows ~5× increase in torque
- `[06:23]` — Internal-fin variant tested; performs slightly worse (~4×) than external-fin version
- `[07:40]` — Design favoured for wind turbine development: internal bump with fins, due to simplicity and lower manufacturing cost

## Robert's Own Replies
- Confirmed that the flying gyroscope ring-wing concept predates Dyson and is not his original idea — he is experimenting with an existing design.
- Pointed viewers to the **Flettner rotor** (https://en.wikipedia.org/wiki/Flettner_rotor) as a related and relevant concept.
- Noted that because the toy actually flies, lift must exceed drag, which validates its potential as a turbine rotor.
- Suggested using **guide rollers, a large bearing, or a Darwin structure** for mounting a scaled-up version.
- Endorsed the idea of adding **tubercles** (whale-fin-inspired leading-edge bumps) as a promising improvement.
- Acknowledged he cannot take on individual collaboration requests, receiving 400–500 messages/comments per day with 20–30 help requests among them.
- Encouraged commenters to build and test their own variations, consistently saying "go for it mate."