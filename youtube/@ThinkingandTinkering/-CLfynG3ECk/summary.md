## Overview
Robert presents Cadex battery analyzer results for four distinct battery prototypes his team has developed, ranging from a carbon-coated car-tire electrode to a high-performance prototype by collaborator Steve. The video demonstrates that these home-lab devices achieve energy densities competitive with or exceeding lithium-ion, at a fraction of the cost, and emphasizes that all quoted figures are conservative Cadex-verified measurements within the machine's voltage window limitations.

## Key Topics
- Setup and calibration of the Cadex battery analyzer alongside a Ryol meter for cross-checking
- Four battery types at different performance/cost tiers, each suited to different applications
- Voltage window limitations of the Cadex machine (1.8 V–0.4 V vs. the devices' actual 2.4 V–0 V range), and why reported figures are intentionally conservative
- C-rate methodology (C/5 discharge) and how milliamp-hour results are normalized per gram
- The philosophy that "best" battery is meaningless — only "appropriate for the application" matters
- Plans for independent third-party verification of results

## Materials and Chemicals Mentioned
- **Structured carbon from recycled car tires** — active electrode material for the lowest-cost battery (~$4/kWh)
- **Stainless steel mesh** — used as current collector substrate, carbon-coated to resist corrosion (clarified in comments)
- **Separator** — mentioned as part of cell construction
- **Electrolyte** — mentioned as part of cell construction; specific chemistry not disclosed
- **Active material (undisclosed)** — used in the mid-range, top-end, and prototype devices; Robert declines to specify without NDA

## Techniques and Methods
- **Cadex battery analyzer testing** — calibrated discharge at set C-rate (C/5) with crocodile clip connections
- **Ryol cross-measurement** — simultaneous voltage and current measurement at the cell terminals to cross-check Cadex readings
- **Gravimetric normalization** — milliamp-hour output divided by active material mass (0.1–0.2 g) to derive Wh/kg figures
- **Tab soldering onto stainless steel current collectors** — cell assembly at bench/lab scale
- **Discharge curve shape analysis** — distinguishing capacitive vs. pseudo-capacitive vs. battery-like discharge profiles
- **Scale-up fabrication** — moving from practice scale to larger test cells for proper construction validation

## Notable Timestamps
- `[00:12]` — Introduction; test equipment setup (Cadex + Ryol) and why both are used
- `[01:28]` — Construction overview: stainless steel current collectors with soldered tabs, separator, electrolyte
- `[02:01]` — Four battery types introduced; "no best battery, only appropriate battery" philosophy
- `[02:19]` — **Battery 1 (tire carbon):** ~35 Wh/kg, comparable to lead-acid, costs ~$4/kWh
- `[03:43]` — **Battery 2 (mid-range):** ~126 mAh/g (~126 Wh/kg), lithium-ion equivalent, costs ~$26/kWh
- `[04:09]` — **Battery 3 (top-end):** ~258–300 mAh/g, outperforms lithium-ion
- `[04:25]` — **Battery 4 (Steve's prototype):** 300–400 mAh/g currently; projected ~600 mAh/g after optimization
- `[05:35]` — Voltage window limitation explained: Cadex caps at 1.8 V, devices capable of 2.4 V; all figures are floor estimates
- `[08:48]` — Live data walkthrough for tire battery: 422-second discharge, 3.5 mAh, 35 Wh/kg calculated
- `[10:28]` — Mid-range device discharge curve: pseudo-capacitor asymmetric design, 126 Wh/kg
- `[11:22]` — Top-end device: extended flat region before capacitive fall-off, 258 Wh/kg
- `[11:51]` — Steve's prototype: very flat discharge curve to 0.6 V, ~300 Wh/kg; high internal resistance identified as issue
- `[13:02]` — Summary of Cadex-verified results and call for independent witness verification

## Robert's Own Replies
- **Specific energy vs. energy density:** Robert prefers Wh/kg (gravimetric specific energy) over Wh/L because weighing is easier than estimating volume in his lab setup; he acknowledges Wh/L is useful but notes he is primarily interested in home storage and grid applications where volume is less critical.
- **Current collector clarification:** The stainless steel mesh is carbon-coated; he uses it specifically because it resists corrosion.
- **What is being weighed:** Figures are based on the weight of active material only, not the full cell.
- **250 Ah/kg** — briefly noted as a relevant figure (likely for one of the devices).
- **Methodology is intentionally rough:** He explicitly acknowledges the fabrication method is "sloppy and poor practice" and that devices would improve significantly if made properly — but the point is to demonstrate what is achievable with kitchen-grade equipment.
- **Proprietary details:** Declines to share specific material compositions without an NDA and a formal contract; will not disclose to allow someone to assess a commercial opportunity.
- **Follow-up promised:** Committed to uploading an update with just the graphs and to crunching remaining data within a few days.
- **Open invitation:** Welcomes visitors to the lab.