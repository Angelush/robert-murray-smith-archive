## Overview
Robert Murray-Smith presents a novel magnetic cycloidal gear he designed and 3D printed, combining two previous projects: a cycloid gear and a magnetic gear set. The result is a compact 12:1 gear reduction device that eliminates the slippage problem of traditional magnetic gears while requiring no rubbing contact between parts, making it exceptionally well-suited to 3D printing. He shares the TinkerCAD files openly for others to build upon.

## Key Topics
- Recap of cycloidal gears and their advantages over planetary gears for 3D printing
- Recap of magnetic gear sets and their 3:1 gear ratio
- The slippage problem inherent in magnetic gears under high torque
- Design and operation of the combined magnetic cycloidal gear (12:1 ratio)
- Gear ratio calculation: (13 − 12) / 12 = 1/12
- Advantages of magnets touching vs. an air gap in torque transfer
- Open-source sharing of TinkerCAD design files

## Materials and Chemicals Mentioned
- PLA (polylactic acid) — used for 3D printing the gear components
- Neodymium magnets — arranged in north-south alternating patterns on inner and outer rings
- Spray grease — suggested as lubrication between touching magnets

## Techniques and Methods
- FDM 3D printing (PLA) for gear body and cam components
- Cycloid gear mechanism adapted to magnetic drive (cam-driven eccentric output plate)
- Pole-pair counting to calculate magnetic gear ratio
- Prototype construction with 0.5 mm plastic retaining wall to prevent magnets popping out
- Open-source CAD design sharing via TinkerCAD

## Notable Timestamps
- `[00:07]` — Introduction and recap of the previous cycloid gear (video 1987), 11:1 ratio, printed in PLA
- `[00:48]` — Recap of the magnetic gear set, 3:1 ratio, and the slippage problem explained
- `[01:35]` — Concept introduced: combining cycloid and magnetic gears to eliminate slippage
- `[01:47]` — Reveal of the magnetic cycloid gear with 12:1 gear ratio
- `[01:56]` — Gear ratio calculation explained (13 pole pairs outer, 12 pole pairs inner)
- `[02:29]` — Physical disassembly showing cam mechanism and output plate
- `[03:19]` — Live demonstration of the gear in operation
- `[03:40]` — TinkerCAD files announced as freely available
- `[04:04]` — Discussion of torque transfer advantages over traditional magnetic gear designs

## Robert's Own Replies
- **Back-drivability**: The current prototype cannot be back-driven due to high friction; replacing the cam and drive pins with roller bearings would fix this and make it reversible (speed increase in reverse).
- **Two-ring improvement**: Acknowledged that two rings phase-shifted 180° would be an improvement over the single-ring prototype.
- **Magnet sourcing**: Recommends Amazon or Magnets4U for sourcing the neodymium magnets.
- **Magnet longevity**: Neodymium is a hard magnetic material — loses approximately 1% magnetisation per 100 years, so effectively permanent.
- **Magnet directional strength**: Notes magnets are very strong along the axis of attraction but surprisingly weak at 90° to that axis.
- **Potential application**: Considering using the design to build a hoist.
- **Cam alternative**: Acknowledges the cam was chosen for ease of printing but an offset roller bearing would be a better long-term solution.
- **Use case**: Can be used anywhere a planetary gear would fit.
- **Build material**: PLA is used to work out ideas cheaply; a stronger build would use a different material.