## Overview
Robert explains why the Elegoo Mars 2 Pro (and similar UV MSLA resin printers) show an "unrecognised file" error, and how to fix it. The root cause is attempting to print an STL file directly — the printer requires a sliced file specific to its LCD screen resolution. The solution is to correctly configure the slicer software (Chitubox) with the right printer profile before exporting.

## Key Topics
- How UV MSLA resin printing works (LCD masking, UV curing, layer-by-layer building)
- Why STL files cannot be used directly by the printer
- The role of slicing software in generating printer-specific mask images
- How to add and select the correct printer profile in Chitubox
- Why printer-specific slicing matters (screen size and pixel addressing differ by model)

## Materials and Chemicals Mentioned
- Resin (UV-curable, used in the MSLA printing process)

## Techniques and Methods
- UV MSLA (Masked Stereolithography) resin printing
- Slicing STL files in Chitubox to generate layer mask images
- Configuring a printer profile in Chitubox (Settings > Machine > Add Printer)

## Notable Timestamps
- `[00:16]` — Introduction to the problem: unrecognised file error on Elegoo Mars 2 Pro
- `[00:42]` — Explanation of how the LCD mask system works (white/black regions, UV exposure)
- `[01:18]` — Why printer-specific slicing is required (screen size and pixel addressing)
- `[01:50]` — Walkthrough of Chitubox: opening settings and selecting the correct printer profile
- `[02:08]` — Demonstration of the printer list (Elegoo, Epax, Flashforge, Peopoly, Creality, etc.)
- `[03:29]` — Summary: the fix is to slice the STL with the correct printer selected in Chitubox

## Robert's Own Replies
No substantive technical content in author replies — responses are brief acknowledgements ("Glad it was helpful!", "cheers", "lol - Thank you!") with no additional clarifications or follow-up insights.