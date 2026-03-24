## Overview
Robert Murray-Smith demonstrates how to extract and repurpose the secondary coil from microwave oven transformers (MOTs) for DIY projects. He explains transformer theory (turns ratio, voltage and current relationships) and shows practically how a rewound MOT can function as a spot welder. The key takeaway is that with just 2 turns of wire through the core, a UK-supply MOT produces enough current (~100A at ~2V) to heat metal to welding temperatures.

## Key Topics
- Why microwave oven transformers are useful for DIY/maker projects and how to source them
- How to remove the secondary coil (the high-voltage thin-wire winding) efficiently
- Transformer theory: turns ratio, voltage step-up/step-down, and the inverse relationship between voltage and current
- Practical demonstration of voltage output per turn using a voltmeter
- Building a simple spot welder from a rewound MOT
- Voltage differences between UK (240V) and USA (110V) mains and how this affects the number of turns needed

## Materials and Chemicals Mentioned
- Microwave oven transformer (MOT) — the core subject, salvaged from scrap microwaves
- Stainless steel nail — used as a test workpiece in the spot welding demonstration
- Jumper cable wire (red) — used as the single/double-turn secondary winding
- Stripper steel (3mm thick, 1cm wide, flat-ended) — used as a punch to drive out the secondary coil

## Techniques and Methods
- Cutting the secondary coil flush with a hacksaw on both faces of the transformer core
- Drilling through the core window with an 8–10mm drill bit to clear compressed wire ends
- Driving out the remaining secondary windings using a flat steel bar (~3mm × 10mm) rather than a chisel or bolt, to avoid spreading and locking the wires
- Single-turn and double-turn rewinding to measure per-turn voltage output
- Spot welding demonstration using locking pliers as electrodes clamped to the new low-voltage secondary

## Notable Timestamps
- `[00:15]` — Introduction: MOTs described as "amazingly useful" and easy to salvage
- `[00:27]` — The two main problems: knowing what wire to use and how to remove the secondary
- `[00:49]` — Discussion of failed removal methods (cutting weld seam, chisel, bolt)
- `[01:13]` — Robert's preferred method: hacksaw both faces + drill + flat steel bar punch
- `[03:46]` — Explanation of transformer theory: turns ratio, voltage step-up, current step-down
- `[05:13]` — Live demo: single turn inserted, voltmeter reads ~0.9V from UK 230V supply
- `[05:59]` — Two turns inserted, voltmeter reads ~2.2V
- `[06:14]` — Spot welding demo with stainless nail: 1 turn produces slow heating; 2 turns produces rapid heating and smoke
- `[07:07]` — Conclusion: minimum 2 turns needed for UK supply; practical spot welder summary

## Robert's Own Replies
- **Other transformer sources:** MOT-style transformers can also be found in old welders; TVs use a flyback transformer instead.
- **Supercapacitor project:** Robert mentions he tried microwave oven capacitors for a flash graphene project (10 caps, no joy), and has ordered 12 × 500F 2.7V supercaps — a flash graphene video is in progress but taking time to assemble.
- **UK vs USA turns difference:** US supply is 110V so 1 turn is sufficient for spot welding; UK supply is 240V so a minimum of 2 turns is needed. The US primary has roughly twice the turns of a UK primary to generate the same ~2kV for the magnetron.
- **Output current estimate:** The rewound transformer produces approximately 100A at 2V; at 240V input it draws less than 1A.
- **Joule thief idea:** A commenter noted DC won't work in a transformer; Robert agrees the changing magnetic field is essential, but floats the idea of building a "massive joule thief" circuit to drive it from DC.
- **Current control:** To control output current, a liquid rheostat works well on the output (low-voltage) side for high-current "burn-off" control.
- **Winding technique:** Feeding turns through the core window is described as "a bit like sewing at scale — just feed it in and loop it round."
- **Safety note:** Robert clarifies the output side carries only ~2V (not a shock hazard); the 240V primary side is isolated from the user during operation, making the rewound transformer safer than the original.
- **Water explosion:** Robert mentions you can also use the transformer to make water explode (electrolysis/arc effect), acknowledging he hadn't tried that particular application.