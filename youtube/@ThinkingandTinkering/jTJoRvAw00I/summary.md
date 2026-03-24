## Overview
Robert Murray-Smith tests a 3D-printed toroidal (toroid-shaped) desktop fan blade, comparing a version without tubercles to an identical version with tubercles added to the blade edges. The results show the tubercle version draws less current (~153–155 mA vs ~165–166 mA) while producing slightly higher airflow (2.1 m/s vs 2.0 m/s) at a fixed 3V supply, demonstrating a meaningful efficiency gain from the biomimetic feature.

## Key Topics
- Toroidal fan blade design and its efficiency characteristics
- Tubercles (bumps modelled on humpback whale fins) applied to fan blades
- Comparative testing: airflow (m/s) and current draw (mA) with and without tubercles
- Higher starting torque but lower running current observed with tubercles
- Contrast between toroid shape performance as a fan vs. as a wind turbine
- Files shared on a 3D-printing file platform for community reproduction and improvement

## Materials and Chemicals Mentioned
- 3D-printed plastic (implied FDM/PLA; Robert notes in comments he avoids resin due to smell and keeping printers indoors)
- Small DC motor sourced from Amazon (fitted into the fan body)
- 3V battery supply (two cells in series)

## Techniques and Methods
- 3D printing of fan components (5 parts: toroid blade, body, cap, foot, motor)
- Press-fit and glue assembly of fan parts
- Airflow measurement using an anemometer (m/s)
- Current draw measurement (milliamps) at fixed 3V to assess efficiency
- Controlled comparative testing (same motor batch, same voltage, same geometry — only tubercles varied)

## Notable Timestamps
- `[00:07]` — Introduction: context from a previous rough comparison, motivation for a fairer test
- `[00:25]` — Description of the toroidal "pidal" blade design and its claimed efficiency/noise benefits
- `[00:50]` — Fan assembly walkthrough: 5 components, Amazon motor
- `[01:28]` — Setup: 3V battery, current measurement explained
- `[01:43]` — Result for fan **without** tubercles: ~165–166 mA, ~2.0 m/s airflow
- `[01:54]` — Switch to fan **with** tubercles; same test conditions
- `[02:28]` — Result for fan **with** tubercles: ~153–155 mA, ~2.1 m/s — lower draw, higher airflow
- `[02:43]` — Observation of higher starting torque with tubercles vs. lower running current
- `[03:11]` — Discussion: toroid shape performs poorly as wind turbine; tubercles perform well on turbines
- `[03:31]` — Files uploaded to a 3D file-sharing platform for community use

## Robert's Own Replies
- **Noise**: He did not measure decibels as he didn't have a dB meter at the time.
- **Weight**: The extra plastic from the tubercles added less than 1 gram — not enough to meaningfully affect motor load.
- **Tubercle placement**: They are on the **leading edge** of the blade; he notes that a fan runs "backwards" relative to a turbine, so leading/trailing edge orientation differs between the two applications.
- **Motor equivalence**: Both tests used motors from the same batch with the same specs; he pushed back on concerns about motor variation being a confounding factor.
- **Voltage vs. amps**: He clarified he displayed current (amps), not voltage — voltage was held constant at 3V throughout.
- **Optimal tubercle ratio**: He acknowledged there will be an ideal tubercle size/spacing ratio to find.
- **Resin printing**: He avoids resin printers due to the smell and keeping his printers indoors, but acknowledges they produce finer detail.
- **Scale**: If results seem underwhelming, his suggestion was simply to make the fan bigger.