# Cognitive pilot 2 of 2 — Visakhapatnam homemaker (Sujatha persona)

Run against survey_v1.md using the same cognitive-pretesting method as Pilot 1. This persona was built specifically to stress-test the "most recent time" framing (she has two candidate incidents in the same week) and whether the survey wrongly assumes drama/breakdown for a routine, low-effort incident.

**Persona**: Sujatha, 38, homemaker, Visakhapatnam. Newer, mid-sized gated community (~6 towers), husband works in the port/shipping sector, two school-age kids. More comfortable with English and apps than a baseline persona; has used a service marketplace app once (AC service via a festival offer). Real incident used for the pilot: her RO water purifier's filter needed changing about a month ago, alongside also getting her AC gas topped up in the same week — two possible incidents in mind when asked about "the most recent time." Both handled and paid for by her alone, without consulting her husband, since both were small routine amounts. Her building has no shared maintenance office, though there's a residents' WhatsApp group where people recommend technicians.

---

# Step 1 — Question-by-question cognitive pretest (as Sujatha)

**Form description:** Clear, reassuring, appropriately casual. No issues.

**Q1-Q3 (consent, age, city):** No confusion. Straightforward.

**Q4 (building name):** Understood as optional and low-stakes. Fine.

**Q5** ("who usually deals with getting things repaired…"): She picks "I usually do it myself" — matches her reality for both incidents. No issue.

**Q6** ("were you personally involved… in the last 3 months"): Yes. Fine.

**Q7 / Section 2 intro — THE key ambiguity flagged in the brief.**
The intro says "think of just one time, the most recent." Sujatha genuinely has two candidates from the same week ~1 month ago: the RO filter change and the AC gas top-up. Both qualify under Q6's wording. Nothing in the intro tells her whether "most recent" means strictly chronological order (and she may not even know which literally happened first within that week), or whether one type of event (routine/preventive) "counts less" than another (a repair). In practice, she will likely default to whichever incident is more *memorable* or feels more "service-like" (probably the AC, the bigger-ticket appliance) — not necessarily the one that was chronologically last. **This is the single most damaging issue in the draft for data quality** — it directly undermines a study about routine vs. dramatic servicing by systematically pulling respondents toward reporting the more "eventful" incident.

**Q8** ("Why did you need someone to come?"): For the RO filter change: not "stopped working," arguably "regular yearly service" but filter changes often aren't on an annual cycle. For the AC gas top-up: also doesn't fit "stopped working" (it still ran, just cooled less). **Missing option**: a "wasn't working as well as before" / "routine top-up, not broken" category. She'd end up jamming a non-breakdown, non-annual-service event into "Other" or misreporting it — bad data either way.

**Q9** (timing bands): Fine, normal recall fuzziness, not a real problem.

**Q10** (whose appliance): "Mine" — clear.

**Q11** (community office vs. self-arranged): Her building has no office but has a WhatsApp group where people recommend technicians. The options force a binary of "office exists" vs. "everyone arranges it themselves," with "a bit of both" as an escape hatch. A WhatsApp recommendation channel is **not** a maintenance office and doesn't "arrange" anything — but an unclear reader could be tempted toward "a bit of both" just because *some* informal community structure exists. The question conflates "formal coordination" with "informal social recommending."

**Q12** (how you got in touch): "Through the building/community office or WhatsApp group" bundles two very different channels — an official office/approved-vendor list vs. an informal social recommendation — into one option. For a building like hers, this loses exactly the distinction the study probably cares about.

**Q13:** Optional, no issue.

**Q14** ("how many more times did you have to call/message"): "None" is available and accurate for her filter change. Good design here.

**Q15** (minutes spent, numeric): Comprehension fine, but the mechanics of a numeric field co-existing with a "don't remember" checkbox is awkward to build cleanly in Google Forms — an implementation friction, not a respondent-confusion issue.

**Q16** (status now): "Fully fixed and working" — accurate, easy.

**Q17** ("From when you first noticed the problem to when it was actually working again…") — **flagged explicitly, and it's real.** This phrasing presupposes a *problem* was noticed — a breakdown narrative. For a routine filter change or a proactively-scheduled top-up, there was no "noticing a problem" moment; there was a "realized/decided it was time" moment. This is the second clearest case of the survey assuming a drama/breakdown script that a routine incident doesn't have.

**Q18** ("Overall, how much hassle did this take for you?"): "Very little" is present and is a fully legitimate, well-supported answer. **This one is done right** — the one question in this cluster that doesn't assume friction happened.

**Q19** (who had final say on spending): She'd pick "Me" — accurate. Minor note: "No real decision was needed" sits oddly close in meaning to "it was such a small/routine call I didn't think of it as a big decision" — she could second-guess between the two. Low severity.

**Q20-Q22:** Clear, no issues, fit her small routine jobs well (no price agreed in advance, nothing sent off-site).

**Q23** (notes/list/WhatsApp chat): "Yes, something like that" explicitly includes "WhatsApp chat" — matches her profile well. Good design.

**Q24** (AMC vs. call someone you know): "No, I just call someone I know" — accurate. Minor referent ambiguity: by this point the survey has drifted from "the one specific incident" toward general household habits, so "Is *this* a paid yearly contract" could be read as "this specific appliance" or "this appliance category in general." Low risk, worth a one-word fix.

**Q25:** Optional, interesting, no comprehension issue.

**Section 6 (Q26-29):** All optional, well-written. Q26 explicitly validates "if honestly nothing was difficult, that's a fine answer too" — exactly the kind of explicit permission Q17's structured version is missing. Good instinct, just not applied consistently earlier.

**Duplicate "Section 6" labeling bug:** Two different sections were both labeled "SECTION 6" in the draft — a drafting/numbering error, not respondent-facing confusion, but risks broken skip-logic when actually built.

**Q30-Q32:** Clear, standard, inclusive.

**Q33** ("who usually ends up handling appliance repairs and servicing"): Substantively the same question as Q5, using a *different, incompatible* response scale. For an attentive respondent, registers as "didn't I just answer this?" — and a real redundancy/data-consistency problem for the researchers.

---

# Step 2 — Does the routine/low-drama cluster hold up for a filter-change-type incident?

- **Q9, Q14, Q15, Q16, Q18**: No drama assumption — "None," a low time estimate, "fully fixed," and "Very little" hassle are all first-class, well-supported options for a smooth incident. **Well-designed.**
- **Q17**: **This is the one that breaks.** It hard-codes a breakdown narrative into a question everyone who reaches it must answer, including everyone whose situation was "regular yearly service" or a routine top-up (which, per Step 1, doesn't even have its own option yet).

Bottom line: the effort/outcome cluster is mostly fine; the one structural failure is Q17's "noticed the problem" framing, compounded by Q8 not yet having a routine-maintenance option to trigger a different Q17 wording off of.

---

# Step 3 — Proposed rewrites

**1. Section 2 intro** — add an explicit tie-breaker and broaden framing to include routine maintenance up front (see Survey_Plain_Language_v2.md for exact wording adopted).

**2. Q8** — add "It wasn't working as well as before" and "Routine maintenance or top-up, nothing broken" options.

**3. Q11** — disambiguate WhatsApp-recommendations from a real office.

**4. Q12** — split the bundled option into "official office/approved list" vs. "recommended in a resident WhatsApp/community group."

**5. Q15** — convert free numeric entry to bands (fixes both the mechanics issue and improves recall accuracy).

**6. Q17** — branch by the Q8 answer so it doesn't force breakdown language onto routine incidents.

**7. Q19** — soften the "Me" / "no real decision needed" boundary: "Me (even if it felt like a small, easy decision)."

**8. Q5 / Q33** — cut the duplicate; Q5 already captures this.

**9. Fix the duplicate "SECTION 6" label.**

**10. Q24** — tighten referent: "Is this specific appliance under a paid yearly service contract…"

---

# Step 4 — Completion time and drop-off risk for Sujatha specifically

The plain, simple phrasing does **not** read as patronizing to a more fluent, more digitally comfortable respondent — the tone is casual and conversational throughout. Her actual path is one of the fastest possible through the form (no follow-up calls, no price changes, nothing sent off-site). If she skips optional paragraphs, she could finish the structured path in 3-4 minutes; if she engages with a couple of the open questions (likely, given she's an active WhatsApp-group participant), 5-6 minutes — comfortably within the form's own estimate. Drop-off risk for her specifically is low; the main cost is a data-quality risk (the "most recent time" ambiguity), not an abandonment risk.

---

# Step 5 — Ready to send?

Not yet. Sent as-is into a real Vizag apartment WhatsApp group, this produces a dataset with a specific, hard-to-fix hole: the "most recent time" instruction has no tie-breaking rule, and Q8/Q17 are worded around a breakdown narrative with no proper slot for routine/preventive maintenance — so respondents with a quiet, low-drama service incident will either misreport it, get pulled toward describing a different, more dramatic incident from the same window, or get stuck answering "when did you notice the problem" for an event where nothing ever broke. None of this would be visible in the resulting spreadsheet — it would just look like clean data. That's a real threat to a study whose whole point is understanding how families handle routine coordination, not just breakdowns. The fixes above are all quick, low-effort edits, not a redesign — but they matter because they would otherwise quietly bias exactly the data point the case study cares about most.
