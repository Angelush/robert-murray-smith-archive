## Overview
Robert Murray-Smith presents the final version of his "Wind Cube" — a 150×150×150mm modular wind generator designed to be stacked into a "wind wall." The video focuses on the improved coil and magnet design, then walks through the complete AC-to-DC conversion circuit needed to produce usable power output. The key takeaway is that with just a bridge rectifier and a smoothing capacitor, the turbine's AC output can be converted to a relatively clean DC suitable for charging or powering small devices.

## Key Topics
- Final Wind Cube design: cube form factor, stackable for a "wind wall"
- Improvements over earlier prototypes: tighter magnet-to-coil tolerances and 1,000-turn coil
- Inverse-square relationship between magnetic field strength and distance
- Demonstrating open-circuit AC voltage output with a fan at ~4–4.5 m/s (UK average wind speed)
- AC-to-DC conversion using a bridge rectifier
- Smoothing DC output with an electrolytic capacitor
- Estimating energy storage and wattage using the capacitor energy formula (½CV²)
- Further regulation options (DC-DC buck/boost converters) for practical applications

## Materials and Chemicals Mentioned
- **Neodymium/permanent magnets** — mounted on a rotating cylinder, brought closer to the coil to improve field strength
- **SWG 32 wire (sg32)** — used to wind the 1,000-turn coil
- **Bridge rectifier module** (2A, 1,000V rating) — converts AC to DC; bought in bulk from eBay (~£2 for 30)
- **Electrolytic capacitor** (1,000 µF / 50V) — smooths the rectified DC output

## Techniques and Methods
- **Tightening magnet-to-coil air gap** — reducing distance to exploit the inverse-square law and increase induced voltage
- **Increasing coil turns** — winding 1,000 turns of SWG 32 to raise output voltage
- **Full-wave bridge rectification** — connecting the coil's two AC leads to the "squiggly line" inputs of the rectifier module
- **Capacitive smoothing** — placing an electrolytic capacitor across the DC output to store charge and even out voltage fluctuations
- **Energy estimation** — using E = ½CV² to calculate joules stored and infer watt-level output
- **Fan bench testing** — simulating ~4 m/s wind with a fan to measure open-circuit and loaded DC voltage

## Notable Timestamps
- `[00:00]` — Introduction to the Wind Cube design (150mm cube, stackable wind wall concept)
- `[00:29]` — Explanation of tighter magnet-coil tolerances and the inverse-square magnetic field law
- `[01:01]` — Description of the 1,000-turn SWG 32 coil and its effect on voltage output
- `[01:38]` — Live demonstration: spinning by hand produces 2.5–5V; fan turned on
- `[02:25]` — Open-circuit AC voltage climbs shown on meter after fan test
- `[03:06]` — Introduction to bridge rectifier; component selection rationale
- `[04:03]` — Wiring diagram explained: AC leads to squiggly inputs, DC out to capacitor
- `[05:27]` — Live DC test: spinning by hand, watching capacitor charge and slowly discharge
- `[06:31]` — Capacitor energy formula explained (E = ½CV²) to estimate wattage
- `[07:02]` — Final fan run measuring DC output
- `[08:24]` — Closing remarks: principles apply to any generator; series conclusion

## Robert's Own Replies
- **Output won't simply double:** Higher turns give higher voltage but lower current — the power trade-off must be considered.
- **Maximum power is ~80 mW** for this small machine; he confirms the capacitor can power a small load "for absolutely ages" at that ceiling.
- **Coil potting suggested:** He agreed with a viewer suggestion to pot (encapsulate) the coil and electronics, noting it as a good protection idea.
- **Linking multiple units:** For a wind wall, units past the rectifier stage can simply be linked together on the DC side.
- **Flywheel effect:** Larger magnets would act partly as a flywheel and also add to voltage, but increasing flywheel inertia requires higher wind velocity to overcome it.
- **2,000 turns possible:** He believes he could have fitted 2,000 turns on the same coil, which would further increase voltage.
- **Regulator recommendation:** Suggested the LM5296 buck/boost regulator board (~£1 on Amazon) for regulated output.
- **Magnet arrangement:** Advised viewers to physically try different magnet arrangements to intuitively understand how to position them.
- **Drum surface tip:** Suggested balancing the drum and coating it in rubber.
- **Noise acknowledgement:** Admitted the machine is noisy and was already thinking about solutions himself.