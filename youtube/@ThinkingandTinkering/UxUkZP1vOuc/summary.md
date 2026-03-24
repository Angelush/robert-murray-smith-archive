## Overview
Robert demonstrates how to design accurate ring gears for 3D printing using a free online gear builder tool by Dr. Hesmer. He explains why the naive approach of inverting a gear profile in CAD is unreliable, and shows that generating proper internal gears with correct tooth geometry via the web app — then importing the SVG/STL into TinkerCAD — produces far better results. The key takeaway is that creating precise, meshable ring gears is straightforward once you use the right tool.

## Key Topics
- Why simple CAD boolean tricks for ring gears are inadequate for reliable meshing
- Introduction to Dr. Hesmer's free online gear builder app
- Configuring internal (ring) gears vs. standard spur gears using negative tooth counts
- Setting clearance values appropriate for FDM 3D printing (0.2 mm)
- Using circular pitch as a proxy for module (module 2 preferred)
- Exporting individual gears as SVG and reimporting into TinkerCAD

## Materials and Chemicals Mentioned
None mentioned.

## Techniques and Methods
- Online parametric gear generation (Dr. Hesmer's gear builder web app)
- Setting negative tooth count (e.g. −30) to generate internal/ring gear geometry
- Configuring clearance (0.2 mm) for FDM print tolerances
- SVG export of individual gear profiles for use in CAD software
- STL reimport into TinkerCAD for integration into larger assemblies

## Notable Timestamps
- `[00:00]` — Introduction: two physical ring gear examples shown, use cases listed (turntables, planetary gears, generator sets)
- `[00:29]` — Critique of the naive boolean approach (hollow gear profile merged with a circle)
- `[01:04]` — Introduction to gear builder apps; Dr. Hesmer's tool highlighted as free and easy
- `[01:34]` — Walkthrough of key parameters: clearance (0.2 mm), circular pitch (set to 8 → effective module 2)
- `[02:37]` — Demonstrating negative tooth count (−30) to generate a ring gear vs. positive for a spur gear
- `[02:58]` — Setting up the meshing pinion gear (10 teeth, 8 mm hole)
- `[03:07]` — Displaying both gears together; downloading each as SVG separately
- `[03:41]` — Reimporting SVG/STL into TinkerCAD; closing remarks

## Robert's Own Replies
- Mentioned considering a future video on 3D printing timing belts.
- Noted that Dr. Hesmer also makes other good gear generators, including a cycloid gear maker.
- Expressed interest in trying Inkscape (raised by a commenter) but admitted he hasn't used it yet.
- Generally encouraging toward commenters who shared their own ring gear projects.