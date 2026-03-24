## Overview
Robert shares a practical methodology for achieving precise tolerances in FDM 3D printing without endlessly reprinting large, time-consuming parts. Using an Archimedes drive teaching model as the example — where rollers must contact a drive ring with near-perfect fit — he demonstrates a sleeve-based iteration technique. Instead of reprinting a 5.5-hour part multiple times, a small adjustable sleeve (printed in ~20 minutes) is used to dial in the exact fit.

## Key Topics
- The tolerance problem in FDM printing (~0.2mm accuracy limit)
- The Archimedes drive as a real-world case requiring tight tolerances
- Deliberately printing the main part slightly wrong (hole too big or outside too small)
- Using a thin, quickly-printable sleeve to achieve the precise final fit
- Iterating sleeve wall thickness in fractions of a millimeter
- Time and filament savings from iterating on small parts vs. large ones

## Materials and Chemicals Mentioned
- FDM filament (unspecified material)
- Super glue — used to fix the correctly-fitted sleeve in place permanently

## Techniques and Methods
- Print main structural part intentionally oversized (hole) or undersized (exterior) by 1–2mm
- Design and print a separate sleeve whose inner/outer diameter can be tuned by small increments
- Adjust sleeve wall thickness by tenths of a millimeter between iterations
- Test fit by sliding sleeve into/onto the main part
- Lock final position with a spot of super glue once correct contact is achieved

## Notable Timestamps
- `[00:08]` — Introduction: sharing a methodology prompted by a friend's problem
- `[00:22]` — Description of the Archimedes drive and why tolerances are critical
- `[00:50]` — FDM printer limitation: ~0.2mm accuracy, and why that's problematic here
- `[01:03]` — The cost of the naive approach: 5.5 hours per print, days of iteration
- `[01:17]` — Core technique introduced: intentionally print the hole too big (or exterior too small)
- `[01:40]` — The sleeve concept explained: a separately printed adjustable insert
- `[01:55]` — Sleeve wall thickness varied by fractions of a millimeter between prints
- `[02:15]` — Time comparison: 5.5 hours for the main part vs. ~20 minutes per sleeve iteration

## Robert's Own Replies
- **Seam position in OrcaSlicer:** Robert notes he clicks "random" for seam position in OrcaSlicer, rather than leaving it on the default "aligned" setting — a useful slicer tip shared in response to a comment.
- **On credit for the technique:** He clarifies he wouldn't claim to have *discovered* the method, but is making practical use of it — and acknowledges that "easy is a relative term."
- **Specific dimension:** In one reply he states **"0.1mm smaller"**, likely clarifying the incremental step size he uses when adjusting sleeve dimensions.
- **On community sharing:** "That's why we share on here mate — it's not possible to think of everything by yourself but having others to help — always helps!" — reflecting his broader ethos around open knowledge exchange.
- Most other replies are brief acknowledgments ("cheers mate", "hope it helps") with no additional technical content.