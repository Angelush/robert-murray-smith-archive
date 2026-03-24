## Overview
Robert reviews the Makera Carvera Air desktop CNC machine from the perspective of a complete beginner — someone with no prior CNC experience, coming from a 3D printing background. He documents his two-week learning journey from unboxing through mastering FreeCAD and MakerCAM, ultimately building a modified cycloidal gearbox (15:1 ratio) using aluminium, brass, and acrylic. His main takeaway is that the machine is capable and good value at ~£2,000, but works best as part of a broader workshop toolkit rather than a standalone solution.

## Key Topics
- Overview of Carvera Air specs: ~£2,000, ~35 kg, 200×300 mm bed, 200W spindle at ~12,000 RPM, 10W diode laser option
- Comparison to the full Carvera (£4,000, 50 kg, with auto tool-change)
- Robert's beginner learning curve: FreeCAD (from scratch), MakerCAM, the Maker app, and machine setup
- First project attempt: milling a custom 60:1 hybrid perpetual-wedge/eccentric gearbox — failed due to bit size limitations on fine gear teeth
- Pivot to a modified Stacked Cycloidal 15:1 gearbox design by Bordon Johansson (originally for 3D printing)
- Adapting the design to fixed aluminium stock thicknesses (3 mm, 5 mm, 10 mm)
- Combining CNC milling with a 55W CO2 laser cutter for efficient acrylic fabrication
- Control via Samsung Galaxy tablet (A9, ~£100) over Wi-Fi — no connection issues reported
- Dust extraction and air assist as optional but recommended add-ons
- Verdict: good all-rounder with a learning curve; best as part of a workshop arsenal

## Materials and Chemicals Mentioned
- **Aluminium plate** — 3 mm (inner ring, drive ring, eccentric), 5 mm (main drive output), used for structural gearbox parts
- **Brass** — turned into axles for the gearbox
- **Acrylic** — 5 mm and 10 mm sheets used for the visible cover plates (chosen for transparency)
- **Steel bolts** — bought hardware used in final assembly
- **Bearings** — 12 mm × 4 mm × 8 mm, used in the back plate pocket

## Techniques and Methods
- **CNC milling** — pocketing, profiling, and drilling in aluminium and acrylic using supplied end mills (2 mm, 6 mm) and engraving bits
- **CO2 laser cutting** — used to cut acrylic blanks in ~1 minute before finishing pockets on CNC (~10 min); combined workflow significantly faster than CNC-only
- **3D printing** — used for the original plastic gearbox prototype and potentially for a spacer
- **CAD design in FreeCAD** — learned from scratch to design parts suitable for fixed-thickness aluminium stock
- **CAM programming in MakerCAM** — used to generate toolpaths
- **Tab retention** — holding workpieces during milling; tabs manually sawn and filed flush after cutting
- **Air assist** — blowing air on metal workpiece to clear chips and cool the bit (Robert skipped this)
- **Dust extraction** — vacuum inlet on machine side to capture swarf (Robert skipped and cleaned manually)

## Notable Timestamps
- `[00:08]` — Introduction to the Carvera Air; comparison to the full Carvera in price and weight
- `[00:58]` — Robert explains his beginner credentials and rationale for a novice-perspective review
- `[02:07]` — Describes the original project goal: re-making his compact 60:1 hybrid gearbox in metal
- `[02:54]` — Machine features walkthrough: bed size, spindle motor, laser head, dust extraction, air assist
- `[04:49]` — Control tablet setup: Samsung Galaxy A9, Wi-Fi connectivity, Maker app
- `[06:43]` — Summary of the learning journey across the 7-video CNC playlist (FreeCAD → MakerCAM → app → practice)
- `[08:04]` — Failed attempt to mill fine ring gears (120/122 teeth) in aluminium — bit limitations caused rounded, unusable teeth
- `[09:33]` — Pivot to Bordon Johansson's stacked cycloidal gearbox design; design modifications for fixed stock thicknesses
- `[11:06]` — Acrylic tab failure snaps a bit; switches to CO2 laser for blank cutting — key lesson in using the right tool
- `[12:57]` — Gearbox assembly walkthrough: eccentric, bearings, acrylic plates, four bolts
- `[14:00]` — Achieved eccentric clearance of 0.05 mm (later corrected to 0.025 mm in comments)
- `[14:44]` — Final verdict: positive overall, learning curve noted, noise and mess as minor negatives
- `[15:50]` — Encouragement to embrace learning new skills, especially later in life

## Robert's Own Replies
- **Eccentric clearance correction:** In the video Robert states the eccentric hole is 0.05 mm larger than the eccentric; in the comments he corrects this to **0.025 mm**, indicating even tighter tolerances than stated.
- **On subtractive manufacturing mess:** Agrees it is "one of the issues with subtractive methods" and suggests a paint-box style enclosure as a practical solution for containing chips.
- **On acrylic fabrication time:** Confirms the combined laser + CNC approach took roughly the same time as if he had CNC'd the acrylic entirely — implying the hybrid workflow's advantage was mainly in cleanliness and convenience, not pure speed.
- **On having no prior CNC experience:** Confirms humorously — "me neither until they sent it lol."
- **On practice boards:** Acknowledges Makera did send sample boards with the machine and agrees using them first would be a good approach for new users.