## Overview
Robert Murray-Smith presents a hybrid high-ratio gearbox he calls the "Frankenstein drive" — a combination of two gear systems he has previously featured: the **perpetual wedge** and the **cycloidal drive**. By borrowing the small tooth-difference ratio principle from the perpetual wedge and the eccentric pin-disc output mechanism from the cycloidal drive, he creates a 3D-printable gearbox that achieves high gear reduction (20:1 in the demo) without complex mathematics. The key takeaway is that two simple rules govern the entire design: the gear ratio equals the tooth difference formula, and the pin diameter equals the hole diameter minus the eccentric throw.

## Key Topics
- Review of the perpetual wedge gear system (high reduction via small tooth-count difference)
- Review of the cycloidal drive (lobe-and-pin mechanism)
- Motivation for combining both: robustness, adaptability, ease of design
- Gear ratio formula: `gear teeth ÷ (ring teeth − gear teeth)` — demonstrated as 80 ÷ (84 − 80) = 20:1
- Designing the eccentric cam: throw = half the gap between inner and ring gear (2.5 mm in the demo)
- Designing the pin output disc: pin diameter = hole diameter − eccentric throw (20 − 5 = 15 mm)
- Pressure angle adjustment (30°) for smoother rotation of the inner gear
- Possible upgrades: replacing pins with skate bearings, using herringbone gears instead of spur gears
- Output options: axle or gear teeth around the output disc

## Materials and Chemicals Mentioned
- **PLA/3D-printed parts** — all components are designed for FDM 3D printing (implied by Thingiverse upload and printing references)
- **Skate bearings (22 mm OD)** — mentioned as a drop-in replacement for the sliding pins to reduce friction

## Techniques and Methods
- **Online gear designer tools** — used to generate spur gear profiles with specified tooth counts and pressure angles
- **CAD design in Tinkercad (implied)** — merge, group, ungroup, center, copy/rotate operations described step by step
- **Pressure angle modification** — changed from standard 20–25° to 30° to ease inner gear rotation
- **Eccentric cam design** — circle with offset rod hole (offset = throw = half the total movement gap)
- **Pin placement via gear template** — inner gear ungrouped and used as a positional guide for drilling pin holes in the output disc
- **FDM 3D printing** — all parts printed; files shared on Thingiverse

## Notable Timestamps
- `[00:00]` — Introduction; recap of the perpetual wedge gear system
- `[00:34]` — Recap of the cycloidal drive and its limitations
- `[01:03]` — Concept: combining both systems into a hybrid drive
- `[01:46]` — Gear tooth counts (84 ring / 80 inner) and ratio formula explained
- `[02:38]` — Eccentric design: measuring the gap and calculating the throw (2.5 mm)
- `[03:56]` — Output pin disc design walkthrough in CAD
- `[05:38]` — Rotating pin holes by 60° to place six pins
- `[07:05]` — Pin diameter calculation: hole size minus throw = 15 mm
- `[08:06]` — Assembly: clip and handle added; completed "Frankenstein drive"
- `[08:25]` — Live demonstration confirming 20:1 ratio (dot moves ~1/20th per full handle turn)
- `[09:00]` — Notes on friction; suggestion to use skate bearings and herringbone gears

## Robert's Own Replies
- **Balancing**: To balance the gearbox, place two inner gears in the ring — Robert notes the viewer likely already knew this.
- **Second disc / vibration reduction**: Offset a second eccentric at 180° and add a second disc — Robert admits he forgot to mention this in the video.
- **Backdrive**: The gearbox **cannot be backdriven** — confirmed twice in replies.
- **Herringbone gears**: Robert is interested in a herringbone version and encourages anyone who builds one to share it with him.
- **DIY scanner plans**: In an off-topic thread, Robert mentions a contact who has plans for a DIY scanner and will post videos on their channel.
- **Eccentric clarification**: Pushes back gently on a commenter who claimed to have "invented" the eccentric — notes they are common and were used in steam engines.
- **Cycloidal drive research**: Defends the design against a skeptical comment, noting well-established research on multi-disc cycloidal configurations.