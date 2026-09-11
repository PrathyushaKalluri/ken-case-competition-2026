# Survey Evidence — Invictus, The Ken Case Competition 2026

**This closes a gap that every other document in this repo says is open.** `progress.md`, `answers_draft.md` and `MASTER_CONTEXT.md` all state "no survey was fielded." **That is now out of date — a survey was fielded and 19 responses were collected between 8 and 10 September 2026.** Update those files before submitting.

## Provenance

| | |
|---|---|
| Instrument | Google Form, 21 questions + timestamp |
| Response sheet | `https://docs.google.com/spreadsheets/d/1soCnQVNXd7TwVzjXAKX3Jb9TAr_S98wF4K6G1__Lo8Q` |
| Form editor | `https://docs.google.com/forms/d/1-Nozi-zEWcabocXyEBPJnIWcmYWo7xk4YfoWosbU-h4` |
| Retrieved | 2026-09-10, via the sheet's CSV export endpoint |
| Responses | **19 total — 12 qualified, 7 screened out** |
| Window | 8 Sep 22:12 → 10 Sep 09:50 IST |

## Files here

| File | What it is |
|---|---|
| `Ken2026_Survey_Responses_RAW.csv` | Byte-for-byte export. The submission artefact. |
| `Ken2026_Survey_Responses_RAW.xlsx` | Same data, native format. |
| `Ken2026_Survey_Response_Table.md` | All 19 responses rendered per-respondent, plus exact question wording. Readable without a spreadsheet. |
| `README.md` | This file — analysis. |

## Compliance — this is clean, and better than the interviews

**The form collected no name, no email, no phone number.** Q1 is an explicit combined age-and-consent gate — *"I am 18 or older, and I agree to answer this survey voluntarily and anonymously"* — and all 19 respondents selected "I agree." Age band and city are captured for every respondent, which is exactly the tagging format the competition requires.

You asked for names to be stored. There are none to store, and that is the right outcome: the ground rule is *"quotes are published the way our openings document does it: age band and city, never a name."* This instrument cannot violate that rule. **Do not add names retrospectively.**

One caveat before this repo is pushed: `github.com/PrathyushaKalluri/ken-case-competition-2026` is a shared repo. The survey data is safe to push. The interview material is not — see `evidence/consent/CONSENT_LOG.md` for the phone numbers visible in the artefact photographs that still need redacting.

---

## Who answered

| Age | n | | Gender | n | | Home | n | | City | n |
|---|---|---|---|---|---|---|---|---|---|---|
| 45–54 | 9 | | Woman | 11 | | Rented | 8 | | Hyderabad | 9 |
| 35–44 | 6 | | Man | 7 | | Own home | 8 | | Visakhapatnam/Vizag | 6 |
| 65+ | 3 | | Prefer not to say | 1 | | Living with family | 3 | | Bengaluru | 2 |
| 25–34 | 1 | | | | | | | | Munich | 1 |
| | | | | | | | | | Gandhinagar | 1 |

**Honest scoping.** This is a convenience sample skewed older (12 of 19 are 45+) and female (11 of 19), concentrated in Hyderabad and Vizag. It licenses *mechanism* claims — "X co-occurs with Y in this group" — and **never prevalence claims**. Do not write "X% of Indian households" anywhere. One respondent is in Munich and should be excluded from any India claim; note the Vizag concentration means this sample is **not** the Hyderabad + Eluru geography `narrowed_problem.md` planned for — Eluru does not appear at all.

---

## The twelve qualified incidents

| Dimension | Result |
|---|---|
| **Appliance** | Washing machine 3 · Water purifier 3 · AC 2 · Other home service (plumbing/electrical/pest) 2 · Geyser 1 · Other kitchen 1 |
| **Situation** | Routine maintenance 5 · Degraded performance 3 · Stopped completely 1 · Part replacement 1 · New installation 1 · Water inlet issue 1 |
| **How they got help** | Brand service centre 4 · Technician they already knew 3 · App (Urban Company/Housejoy) 2 · Society office / resident group 2 · Local shop 1 |
| **Society maintenance available?** | Arrange it themselves 6 · A bit of both 3 · Shared office/approved list 2 · Not sure 1 |
| **Time promised and kept?** | Kept 9 · Promised but broken 2 · No clear time given 1 |
| **Follow-ups needed** | None 6 · 1–2 more times 4 · **3 or more times 2** |
| **Part or appliance moved?** | **No 10 · Not sure 2 · Yes 0** |
| **Effort (1–5)** | mean **2.17** — low (1–2) 8 · mid (3) 3 · high (5) 1 |

### Tracking method — multi-select, n=12

| Method | n |
|---|---|
| **"I don't track it, I just call when needed"** | **7** |
| A saved contact in my phone | 6 |
| We have an annual contract | 3 |
| A WhatsApp chat | 2 |
| A note, list or notebook | 1 |

---

## What this corroborates, and what it kills

### ✅ Strongly corroborates the Q2 insight and the Payments rail

**7 of 12 incidents had the four roles split across more than one person.** The form asked separately who was responsible for the Decision, the Cost approval, the Payment, and the Home access. In only 5 of 12 did one person hold all four.

| Pattern (Decision / Cost / Payment / Access) | n |
|---|---|
| Split across two people | **7** |
| All four held by one person | 5 |

This is the quantified backbone the delegated-authority argument was missing. Grantex-style delegated authority is not a decorative rail here — in more than half of real incidents, **the person who approves the cost is not the person who pays, or not the person who lets the technician in.** Sai Kakki said exactly this in interview ("my husband decides… availability I decide"); the survey shows it is the majority pattern, not her quirk.

**Q17 — "the one thing you'd always want to decide or approve yourself"** — the free-text answers land on cost and verified outcome, which is precisely the Q2 claim that what households refuse to delegate is verification:

> *"Cost approval and home access"* · *"Cost for the entire process"* · *"Cost"* · *"Decide"*
> *"Problem should be fixed once and for all."* · *"Good & genuine service"* · *"Service should be excellent and hasslefree"*

Three of ten substantive answers name cost explicitly; three more name outcome verification. Nobody asked to keep the booking, the calling, or the scheduling.

**Follow-up burden is real but not universal:** 6 of 12 needed at least one chase, 2 needed three or more. That matches the interviews rather than inflating them.

### ❌ Disconfirms the Logistics rail — and this is the honest finding to report

**Zero of twelve incidents involved a part or an appliance being picked up or delivered from somewhere else.** Ten said no outright, two said "not sure."

This directly contradicts the strengthened Logistics answer currently in `answers_draft.md` §Q4. **Q4 must be revised.** Two readings, and the difference matters:

1. The question measures *whether the household arranged any movement* — and 6128maggi's case (technician makes his own sourcing trip and bills ₹200 for it) would plausibly be answered "No," because she arranged nothing. The parts leg exists but is invisible to the person paying for it.
2. Or there genuinely is no parts leg in most household repairs, and the interview evidence is a minority case.

Either way, **the survey does not support a logistics rail, and the answer must say so.** Reading (1) is defensible and is actually a sharper claim — *the logistics leg is so invisible that households do not report it even when they are billed for it* — but it must be stated as an interpretation, not as corroboration. This also makes the choice of Payments for Q5 evidenced rather than assumed: we tested logistics and it did not hold up.

### ⚠️ Complicates the opening's own premise

**7 of 12 keep no service memory at all** — "I don't track it, I just call when needed" — and the mean effort score is **2.17 out of 5**, with 8 of 12 rating it 1 or 2.

The Ken's opening assumes households are straining under a coordination burden and need a service memory. Most of our qualified respondents are not straining, and are content not to track anything. **Do not overclaim universal pain.** The pain is concentrated, not distributed — and where it concentrates is instructive: the single effort-5 response is also the one where a time was promised and broken *and* three-plus follow-ups were needed. The one respondent who kept the richest records (saved contact + WhatsApp + annual contract) still needed three-plus follow-ups.

That is consistent with Q2 rather than damaging to it: the burden is not spread across every repair, it spikes at the moment a commitment or a price moves.

---

## The answer we did not expect

The competition asks for this explicitly — *"a survey you ran including the questions you asked and the raw answers, with a line on which answer you did not expect."*

> **We expected households to be quietly maintaining service records. Seven of twelve told us they keep nothing at all and just call when something breaks — and they rated the hassle 1 or 2 out of 5. The households with the most complete records were not the ones having the easiest time.**

Second candidate, if a rail-specific line is wanted instead:

> **Not one of twelve incidents involved a part being sent anywhere. We had gone looking for a parts-logistics problem after a technician described billing a customer for his own sourcing trips — the households never saw that trip as logistics at all.**

---

## What must now change elsewhere in the repo

1. **`progress.md`, `answers_draft.md` §0, `MASTER_CONTEXT.md` §16** all assert no survey exists. Correct them.
2. **`answers_draft.md` §Q4 Logistics** — rewrite against the 0/12 finding above. Do not leave the current strengthened claim standing unqualified.
3. **`answers_draft.md` §Q4/§Q5 Payments** — add the 7/12 role-split figure. It is the strongest single number the team has, and per `best_practices.md` §1.3.4 a number attached to a claim is what winning submissions do.
4. **Attach this folder** as the survey evidence type, with the "answer we did not expect" line above.
5. **The `[team-controlled contact]` placeholder** flagged in `best_practices.md` §6 is now moot — the survey has closed with 19 responses.
