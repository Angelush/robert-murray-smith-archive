## Overview
This video is a step-by-step TinkerCAD tutorial showing how to model the Archimedes screw central section of the Liam F1 wind turbine blade. Robert walks through creating a three-blade helical shape using the SVG Helix tool combined with cookie-cutter subtraction, then extends the technique to add a 15° pitch angle to the blades, matching the original Liam F1 design.

## Key Topics
- The Liam F1 Archimedes screw wind turbine blade as design inspiration
- Using TinkerCAD's SVG Helix tool to create helical shapes
- Creating a three-blade symmetric helix by rotating copies 120°
- Applying the cookie-cutter (boolean subtraction) method to shape the turbine cone profile
- Modifying the base SVG profile to introduce a blade pitch angle (~15°)
- Scaling imported STL files to compensate for size reduction
- Broader applications: water turbines, Archimedes screw pumps, marble runs

## Materials and Chemicals Mentioned
- eSun filament (mentioned in comments as Robert's preferred brand)
- Elegoo filament (mentioned in comments as an alternative Robert uses)

## Techniques and Methods
- Creating a flat rectangular profile (60×1×1) in TinkerCAD as the helix cross-section
- Exporting the profile as an SVG file for use with the SVG Helix tool
- Configuring SVG Helix parameters: sketch height, number of sides, sketch rotation (90°), and number of windings (1.125 for 1⅛ turns)
- Duplicating and rotating helix bodies by 120° to produce a 3-blade assembly
- Merging all three helices into a single object
- Using a reference circle (250×10) as a centering guide for subsequent alignment
- Cookie-cutter subtraction: using an inverted cone (hole) merged with a cylinder to create the tapered outer boundary
- Adding a central axle cylinder, aligned to the reference circle center
- Rotating the base SVG profile by 15° and re-exporting to introduce blade pitch
- Re-importing the angled STL at 1000% scale to restore working dimensions

## Notable Timestamps
- `[00:00]` — Introduction; framing the question "how was the Archimedes screw section made?"
- `[00:25]` — Opening TinkerCAD; creating the base 60×1×1 rectangular block
- `[00:44]` — Exporting the profile as an SVG file
- `[00:51]` — Finding and dragging the SVG Helix tool into the workspace
- `[01:42]` — Adjusting SVG Helix parameters (sketch height, rotation, 1.125 windings)
- `[02:10]` — Zooming out to see the completed single helix (~250×250)
- `[02:18]` — Copying and rotating helix 120° to build the three-blade layout
- `[02:41]` — Merging all three helices
- `[03:00]` — Creating the 250×10 reference circle for centering
- `[03:41]` — Cookie-cutter cone construction and alignment
- `[05:23]` — Raising cookie cutter 10 mm, merging to cut the helix shape
- `[05:44]` — Adding and centering the central axle cylinder
- `[06:52]` — Deleting the reference circle; final merge
- `[07:07]` — Completed 3-blade 1⅛-turn helix shown
- `[07:22]` — Introducing the blade pitch angle requirement (~15°) from the original Liam F1 design
- `[08:00]` — Rotating the original SVG drawing by 15° and re-exporting
- `[09:05]` — Exporting the angled shape as STL, noting it is only 16×16 mm
- `[09:26]` — Reimporting at 1000% scale to reach ~160×160 mm
- `[09:47]` — Repeating the full procedure to produce the final angled turbine blade

## Robert's Own Replies
- **On filament brand:** He uses eSun or Elegoo filament.
- **On Archimedean vs. Archimedes screw (mathematical difference):** Clarified that strictly speaking they differ — one follows an arithmetic progression, the other geometric — but in most practical applications the distinction makes no real difference.
- **On the 15° angle specifically:** He doubts there is a strong aerodynamic reason for that exact angle; he simply copied it from the original Liam F1 design.
- **On dimensions used in the video:** Acknowledged that the dimensions shown were chosen for demonstration purposes; he relies on the community to pick up details and improve on what he presents, and genuinely values those contributions.
- **On 3D Builder being discontinued:** Expressed regret that Microsoft's 3D Builder was removed.
- **On early access:** Members received the video approximately one month before public release.
- **Personal note (off-topic but notable):** In response to a question about his personal life, Robert shared that his wife had passed away, describing it as a very difficult thing to answer.