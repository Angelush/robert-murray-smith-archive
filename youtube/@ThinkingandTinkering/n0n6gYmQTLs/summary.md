## Overview
Robert Murray-Smith received 1,000 Samsung phone batteries (circa 2016–2017) from a local PC recycling company and explains how to test, recover, and reuse them as direct replacements for 18650 lithium cells. The key insight is that batteries discarded by the electronics industry typically retain around 80% of their original capacity and have several more years of useful life. By removing the built-in protection circuit, these flat phone batteries can be handled and tested identically to standard 18650 cells.

## Key Topics
- How phone batteries compare to 18650 cylindrical cells and how to convert them for equivalent use
- Why "dead" consumer batteries still hold significant charge (~80% capacity after ~500 cycles)
- Where to source free or cheap old phone batteries (phone repair shops, recycling companies)
- Voltage-based triage: identifying good, recoverable, and dead cells
- Charging methods: constant-current charging on a benchtop supply
- Reconditioning low-voltage cells (2.5 V and above) with reduced charge current
- Proper disposal of failed batteries
- Plans for a future multi-battery charging rig and capacity-testing project

## Materials and Chemicals Mentioned
- **Samsung lithium polymer phone batteries** (2016–2017 production) — the subject of the video; flat-pouch format
- **18650 lithium-ion cells** — used as the reference/comparison format
- **Lithium** — discussed mechanically as internal "pillars" that collapse if over-discharged, explaining why cells below ~2 V are unrecoverable

## Techniques and Methods
- **Protection circuit removal** — slicing the tape holding the plastic end cap, folding it back, and desoldering the two tabs connecting the circuit board to the battery tabs
- **Open-circuit voltage testing** — placing desoldered cells on a multimeter to triage condition (>4 V = excellent, ~3.7 V = good, 2.5–3 V = recoverable, <2 V = discard)
- **Constant-current charging** — applying 500 mA with voltage left open on a benchtop supply; charge complete when voltage reaches 4.4 V (as printed on the battery)
- **Low-current reconditioning** — charging degraded cells (2.5 V+) at 100–200 mA to safely restore them
- **Spin test** (mentioned in comments) — a bloated/swollen battery takes on a barrel shape and spins freely; a flat battery that spins fast may still be good but requires further testing
- **Capacity testing** — planned follow-up: charge, then discharge to measure actual stored energy
- **Self-discharge stability test** — planned follow-up: charge cells, leave for two weeks, re-measure voltage

## Notable Timestamps
- `[00:02]` — Intro; Robert explains how he received 1,000 Samsung phone batteries from a local recycling company
- `[01:07]` — Comparison to 18650 cells; explains the protection circuit and why it needs to be removed
- `[01:30]` — Background on the 18650 second-hand battery market and the ~80% residual capacity argument
- `[03:39]` — Close-up demonstration: slicing the tape and removing the plastic protection circuit cap
- `[05:00]` — Soldering iron used to desolder the protection circuit tabs from the battery tabs
- `[05:50]` — First voltage reading on a bare cell: 3.7 V — confirms excellent condition
- `[06:14]` — Results from first 10 cells: 8 at 4+ V, 2 at 3.7 V
- `[06:42]` — Constant-current charging explained: 500 mA, voltage open, stop at 4.4 V
- `[07:22]` — Reconditioning low-voltage cells at 100–200 mA; explanation of lithium "pillar" collapse below ~2 V
- `[08:20]` — Summary of voltage thresholds and triage rules
- `[09:09]` — Estimate of total energy received: ~10–12 kWh of storage

## Robert's Own Replies
- **Correct charge voltage is 4.4 V** — Robert clarifies this multiple times, stressing that the charge voltage is printed directly on the battery label: *"the charge voltage is printed on the front of the battery! … don't go by random guesses … check it first before you do anything"*
- **Nominal voltage is 3.85 V**, not 3.7 V — he notes this is printed on the battery
- **Bloated battery spin test clarification** — a swollen battery takes a barrel shape and spins freely, which guarantees it is bad; a flat battery that doesn't spin might still be good, but the spin test alone is not sufficient — all other checks still apply
- **Why remove the protection circuit before testing?** — connecting to the outer tabs tests the battery *plus* the circuit together; if you get a bad result you can't tell whether the battery or the circuit failed, so removing the circuit first gives a clean reading of the cell itself
- **Chemistry can be reclaimed** — Robert confirms it is possible to reclaim the chemistry and materials from dead cells, though it is "a little involved"
- **Flat vs. cylindrical packs** — responds to a commenter suggesting flat cells behave differently at high current: Robert disagrees, noting they are mechanically and chemically identical to other lithium cells of this type; the only practical difference is that flat packs have no inherent air passages for cooling, which may need to be addressed in a built-up pack
- **Twitch stream mention** — notes they started a Twitch stream called "TnT — Thinking and Tinkering"