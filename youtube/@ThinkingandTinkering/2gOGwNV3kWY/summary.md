## Overview
Robert provides an update on his experimental 1 cm² battery cell, demonstrating it powering a small motor via a Joule Thief circuit. The cell delivers a steady ~30 milliamps for approximately 6 minutes on a full charge, and Robert highlights that measuring power at the load — not inside the battery — is the meaningful metric. He closes by musing on a potential Kickstarter product: a near-instantly rechargeable e-cigarette-style device using the cell, a miniature Joule Thief, and resistive heating wire.

## Key Topics
- Update on the 1 cm² battery cell project
- Joule Thief circuit as a means to extract usable power at low voltages
- Distinction between power measured at the load vs. power inside the battery
- Performance characteristics: ~6 minutes runtime, ~30–33 mA output, voltage dropping to ~142–173 mV under load
- SMD (surface-mount) Joule Thief as a compact packaging option
- Concept for a fast-charging e-cigarette-style heat device as a potential Kickstarter product

## Materials and Chemicals Mentioned
- **Battery cell (1 cm² experimental cell)** — the primary device under test; chemistry not specified but capable of near-instant "tap charging"
- **Lithium** — mentioned as the chemistry used in commercial e-cigarettes, contrasted with Robert's cell
- **Resistive wire** — proposed as the heating element in the envisioned product

## Techniques and Methods
- **Joule Thief circuit** — used to step up and extract remaining energy from the low-voltage cell; a low-voltage variant rated down to ~0.03 V is shown
- **Load-side power measurement** — ammeter placed across the load (motor), voltmeter across the cell, to measure delivered power rather than battery capacity
- **Tap charging** — near-instantaneous recharging method specific to Robert's cell
- **SMD packaging** — surface-mount Joule Thief discussed as a way to miniaturise the circuit for integration into a product

## Notable Timestamps
- `[00:13]` — Introduction; 1 cm² cell running a motor at ~22–23 mA, ~173 mV
- `[00:34]` — Joule Thief introduced; reports ~6 min runtime and ~30 mA steady output on a full charge
- `[01:28]` — Joule Thief shown actively helping discharge the cell
- `[01:33]` — Key methodological point: measuring power at the load, not inside the battery
- `[02:38]` — Demonstrates discharge after only a ~20-second charge; still delivers ~20 mA at ~148 mV for over 2 minutes
- `[03:28]` — Shows the specific low-voltage Joule Thief module used (rated to ~0.03 V)
- `[03:48]` — Shows a tiny SMD Joule Thief; notes it could be glued to the side of the cell
- `[04:01]` — Proposes a Kickstarter product concept: fast-charging e-cigarette-style heater using the cell + Joule Thief + resistive wire

## Robert's Own Replies
The comment replies are brief and conversational, but a few contain substantive points:

- **On the e-cigarette market:** Robert defends the application choice with WHO data — roughly 1 in 5 people worldwide smoke; the e-cig market exceeded $6 billion in 2015 and was projected to reach $20 billion by 2020. He pushes back on adding extra complexity ("why would I integrate all that stuff — it just sounds like cost and unnecessary complexity").
- **On sticking with a decision:** He offers general encouragement to commit to a chosen direction — "it doesn't really matter what you produce, it only matters you produce something… having made a decision it's usually best to stick with it if you believe in it."
- **On a technical point (Joule Thief behaviour):** He defers to a commenter named Alan, noting "the real answer is to try it and see — which so often is quicker than arguing the pros and cons."
- He shares his email (`robertmurraysmith64@gmail.com`) in one reply, apparently in response to a collaboration or contact request.