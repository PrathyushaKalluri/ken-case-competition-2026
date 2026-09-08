# Secondary Research Evidence Archive — Summary

Built across two sessions: an initial forked agent that collected ~16 real verbatim quotes before hitting an account-wide rate limit (reset 3:30pm IST) and failing, plus direct follow-up research after the fork failure. Every quote/data point in this archive is real, sourced, and dated — nothing fabricated. Per this project's standing rule (`system_map.md` §0, restated in `research_plan.md` §8): **none of this is a substitute for the team's own primary interviews as the Q2 insight.** It supports Q9, provides context, and gives your interviews something concrete to corroborate or contradict.

## What's here

- **`reviews/urban_company_pissedconsumer.txt`** — 8 verbatim quotes from PissedConsumer, including one from Hyderabad specifically and one from the same Telangana region as Eluru.
- **`reviews/urban_company_trustpilot.txt`** — 8 verbatim quotes from Trustpilot, including several with real rupee figures (₹9,500 AC repair that didn't hold, a 40%-deduction-without-customer-action cancellation charge).
- **`government_data/nch_pib_press_release_oct2025.txt`** — a genuine primary government document (PIB, Oct 2025), fetched and text-extracted directly. Verifies NCH's overall scale and growth; does **not** independently verify the specific appliance-servicing top-5-category claim already in `system_map.md` §7.1, which remains sourced to a secondary WebSearch synthesis — flagged explicitly there, not hidden.

## What was searched but came back thin (flagged, not padded)

- **Social listening (Reddit r/hyderabad, Twitter/X)**: a direct search for Hyderabad-specific AC-repair complaint threads returned only business listings (AC repair service providers advertising themselves), no real Reddit discussion threads. Not pursued further given the account-wide rate-limit constraint hit mid-session — worth a manual search directly in Reddit's own search bar if time allows, since WebSearch's indexing of Reddit content is inconsistent.
- **Contracts (AMC/warranty/pest-control terms text)**: not yet attempted — queued, not abandoned.
- **Kaggle dataset previews, Kent/Livpure app reviews**: not yet attempted — the forked agent that was assigned this task failed before reaching it.

## The clearest patterns across the real evidence collected so far

1. **The quote-to-bill gap (thread #10) shows up repeatedly and specifically**, with real rupee figures — e.g. a customer paying ₹9,500 (₹6,500 cooling coil + ₹3,000 gas charging) for an AC that still wasn't fixed, and developed a new noise afterward.
2. **Extended unavailability with no resolution timeline (thread #20)** appears in an extreme form: a customer waiting 6 months for a water-purifier filter, and another whose washing machine motherboard was removed from the home and never returned.
3. **Payment moving without genuine customer consent or action** — the sharpest single find: a reviewer reporting Urban Company deducted 40% of a booking's value as a "cancellation" charge when the *provider*, not the customer, failed to show up. This is a real, documented instance of exactly the kind of payments/authorisation failure the delegated-spend-cap concept (`Keeping_Machines_Running_Context.md` §7B) is meant to prevent — a milestone-based-payment guardrail, not automatic deduction.
4. **A Hyderabad-specific complaint** (cancellation without notice, no refund) exists in the collected evidence — worth checking directly against whatever your own Hyderabad interviews find, since it's the same geography, same platform.
