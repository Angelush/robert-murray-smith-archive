## Overview
Robert Murray-Smith demonstrates how to design 3D-printable clips in Tinkercad using its SVG Revolver tool. The clips are motivated by his work on a spur gear differential, where he wanted a reversible assembly method that avoids permanent gluing. By combining simple Tinkercad primitives and boolean operations, he produces a clip-and-indent system that snaps onto printed rods.

## Key Topics
- Motivation: avoiding permanent glue joints on multi-hour 3D prints
- Creating a clip profile from a box and wedge primitive in Tinkercad
- Exporting a 2D profile as an SVG file
- Using Tinkercad's SVG Revolver ("SVG rotate") tool to revolve the profile into a 3D clip
- Tuning the revolve angle (300° → 240°) to create a sprung opening for easy clipping
- Creating a matching indent on a rod using a full-circle (360°) revolved hole and boolean merge
- Application to spur gear differential assembly

## Materials and Chemicals Mentioned
- PLA or similar FDM filament (implied; "quite a lot of plastic" printed over several hours)
- 12 mm diameter rod (3D-printed, used as the example bar)
- 2 mm clip geometry (height and bite depth)

## Techniques and Methods
- **Primitive modelling**: combining a box and a rotated wedge to form the clip cross-section
- **Work-plane alignment**: dropping objects onto a surface via workplane + D key to align primitives precisely
- **SVG export** from Tinkercad for use as a revolver profile
- **SVG Revolver** (Tinkercad community shape): importing an SVG and revolving it around an axis to create a solid of revolution
- **Sketch rotation adjustment**: correcting 180° orientation mismatch after import
- **Revolve angle tuning**: setting 240° instead of 360° to leave a gap for clip flex
- **Boolean hole + merge**: duplicating the clip shape, setting to 360° full circle, marking as a hole, then merging with the rod to cut a matching groove

## Notable Timestamps
- `[00:00]` — Introduction: spur gear differential project and motivation for clips over glue
- `[00:50]` — Overview of the Tinkercad workflow to follow
- `[01:07]` — Creating the clip profile using a box and wedge primitive (2×2×2 mm each)
- `[01:51]` — Using workplanes to align the two primitives
- `[02:11]` — Merging primitives, rotating 90°, and exporting as SVG
- `[02:41]` — Opening SVG Revolver tool from the Tinkercad search bar
- `[03:00]` — Importing the SVG file into SVG Revolver; correcting 180° sketch rotation
- `[03:32]` — Setting inside diameter to 8 mm for a 12 mm bar with 2 mm bite
- `[03:43]` — Creating the example 12 mm cylinder rod primitive
- `[04:14]` — Changing revolve angle from 300° to 240° for easier clipping
- `[04:33]` — Duplicating clip shape; setting to 360° full circle and converting to hole
- `[04:56]` — Merging hole with rod to create the matching clip indent groove
- `[05:05]` — Showing finished result on the actual spur gear differential rods

## Robert's Own Replies
Robert's replies in the comments are mostly brief acknowledgements, but two offer minor additional context:
- He notes that clips with the correct fit are **smoother and wear less** with repeated clipping and unclipping — suggesting tolerance tuning matters for longevity.
- He mentions the tutorial was somewhat spontaneous: *"it just occurred to me this might be useful to someone"* — consistent with his informal, share-as-you-go style.