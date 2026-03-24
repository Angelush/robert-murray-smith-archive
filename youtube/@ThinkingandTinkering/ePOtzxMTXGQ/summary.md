## Overview
Robert Murray-Smith disassembles the 100 kg, 6 kWh, 48V battery pack from a Renault Twizy electric quadricycle to inspect its internals and salvage reusable components. The goal is to understand the existing battery management system (BMS) so it can be replaced with custom open-source electronics, enabling a third-party battery to be fitted to the Twizy. He follows the open-source XtoEG GitHub project as his guide for building the virtual BMS replacement.

## Key Topics
- Overview and safety precautions for working with a high-voltage EV battery pack
- Internal anatomy of the Renault Twizy battery (cells, busbars, control electronics, power electronics, connectors)
- Why a custom battery cannot be dropped directly into the Twizy without replacing the BMS
- The XtoEG GitHub project as a resource for building a virtual/replacement BMS using Arduino
- Planned workflow: bench-test with standard batteries first, then install custom batteries
- Funding model explanation (shop sales rather than donations)

## Materials and Chemicals Mentioned
- **Aluminium chassis/frame** — structural support frame inside the battery enclosure to which cells and electronics are mounted
- **Rubber gloves (double set)** — safety PPE used during disassembly of the live 48V pack

## Techniques and Methods
- Manual disassembly of a large-format EV battery pack using insulated tools
- Visual inspection and identification of internal components (busbars, cell modules, control/power electronics boards)
- Component salvage — extracting reusable connectors and electronics from the original pack
- Bench-testing approach: validating replacement BMS electronics with standard batteries before committing to custom cells
- Arduino-based BMS replacement using an Arduino Star/Prime board, CAN bus shield, relay shield, and optional temperature extension board

## Notable Timestamps
- `[00:12]` — Introduction to the Twizy battery pack; weight (100 kg), capacity (6 kWh), voltage (48V), and safety warnings
- `[00:47]` — Explanation of ongoing Twizy project and funding model (shop sales)
- `[01:31]` — Introduction to the XtoEG GitHub project and its Arduino-based virtual BMS approach
- `[03:21]` — Beginning of physical disassembly; lid removed, first look inside the battery enclosure
- `[04:42]` — Identification of individual cell modules, busbars, control electronics, and power electronics
- `[08:14]` — Summary of extracted components: aluminium frame, cover plate, control electronics, retaining plate, battery modules
- `[08:41]` — Explanation of why a virtual BMS replacement is required to run a custom battery in the Twizy
- `[09:14]` — Relay specification noted (450V, 40A) as a reference for replication
- `[10:14]` — Planned next steps: assemble replacement electronics, bench-test with standard batteries, then install custom pack

## Robert's Own Replies
Robert's comment replies are mostly brief social exchanges, but a few contain useful clarifications:
- He confirmed that after the project is complete he will likely **reassemble the pack and return it to Renault**.
- He noted that the **Twizy motor uses a Sevcon controller** which can be accessed but is fairly complex, and that the BMS also needs to be cracked to access the rest of the Twizy operating system.
- He acknowledged he was **nervous** during the disassembly.
- He clarified to a commenter that the **Twizy is an electric quadricycle produced by Renault**.
- On the question of Renault's openness: he noted they **"have changed their attitude a lot and now support open source"**, leaving the door open for future collaboration.