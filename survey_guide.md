# Survey Guide — Exact Questions, Google-Forms-Ready

**Honest limitation first**: I don't have a tool that can directly create or deploy a live Google Form — there's no Google Forms API access in this environment. What follows is the exact question-by-question script, in Google Forms' own terms (question type, section breaks, branching logic), so building the actual form is a copy-paste job, not a redesign — should take about 15-20 minutes.

Base instrument: Sricharan's S0-S30 (`research/report-source.md` Pages 10-12, verified verbatim against the source this pass), plus this project's two additions — **S7a** (managed-vs-independent screening) and **S20a** (workaround-artifact capture) — inserted at their exact points below. Already audited and cleared (`best_practices.md` §6: "ship it," 3 minor hardenings, all incorporated here).

**Google Forms setup notes**: use "Sections" (the Forms feature, not just headers) everywhere a skip/branch is needed — S0/S1/S2 gate the whole survey, S13→S14 is conditional, S16/S19/S24/S25 each have a conditional follow-up. Turn on "Shuffle question order" = **off** (question order matters here, per the anti-priming design). Turn on response validation (numeric-only) for S12 and S26.

---

## Section 1 — Intro (Google Forms: a text/description block, no question)

> *[Your team names], students researching household repair coordination for The Ken's 2026 competition. Participation is voluntary — you can skip questions or stop anytime. Your anonymised answers may be submitted to The Ken and its judges/partners, and may appear (age band + city only, never your name) in their published map of India's agentic era. Contact: [insert a real team contact here before launch — this is a placeholder, don't launch with it blank].*

## Section 2 — Consent gate

**S0.** *"Do you agree to participate under the explanation above, including submission and the stated organiser use of your anonymised answers?"*
*Type: Multiple choice.* Options: **Yes** / **No**.
*Branching: "No" → jump to a final "Thank you" section, end form. "Yes" → continue.*

**S1.** *"Are you 18 or older?"*
*Type: Multiple choice.* Options: **Yes** / **No** / **Prefer not to say**.
*Branching: only "Yes" continues; "No"/"Prefer not to say" → jump to end.*

## Section 3 — Screening

**S2.** *"In the past 90 days, have you personally helped arrange installation, servicing or repair of a household machine?"* (Arrange = contacting a provider, coordinating a visit, obtaining approval, arranging parts, or handling payment.)
*Type: Multiple choice.* Options: **Yes** / **No** / **Cannot recall**.
*Branching: "No"/"Cannot recall" → jump to Section 9 (S22-S23) then end. "Yes" → continue.*

## Section 4 — Incident facts *(intro text: "For the next questions, think only about the most recent episode.")*

**S3.** *"How many separate installation, service or repair episodes did you help arrange in those 90 days?"* (Several calls about the same unresolved issue count as one episode.)
*Type: Multiple choice.* Options: **1 / 2 / 3 / 4 / 5 or more / Cannot recall**.

**S4.** *"What machine was involved?"*
*Type: Multiple choice, with "Other" free-text option enabled.* Options: **AC / Refrigerator / Washing machine / Water purifier / Geyser / Kitchen appliance / Other**.

**S5.** *"What was the main reason for arranging service?"*
*Type: Multiple choice, "Other" enabled.* Options: **Installation / Scheduled maintenance / Fault or breakdown / Follow-up on a previous repair / Other / Cannot recall**.

**S6.** *"Approximately when did this episode begin?"*
*Type: Multiple choice.* Options: **Within 7 days / 8-30 days ago / 31-60 days ago / 61-90 days ago / Cannot recall**.

**S7.** *"Who owned this machine?"*
*Type: Multiple choice, "Other" enabled.* Options: **Me / Someone else in my household / Landlord or PG operator / Shared community or building / Other / Do not know**.

**S7a** *(added this project, testing thread #18)*: *"Does your home/building have a dedicated facilities or maintenance service you can raise a request with (e.g. through a builder or community management office), or do you arrange repairs yourself each time?"*
*Type: Multiple choice.* Options: **A dedicated community/facility management service / I arrange it myself each time / Some of both, depends on the issue / Don't know**.

**S8.** *"Which actions did you personally take?"*
*Type: Checkboxes (select all that apply), "Other" enabled.* Options: **Contacted provider / Arranged visit / Supplied records / Approved work / Paid provider / Arranged parts or transport / Admitted provider / Checked completion / Other**.

**S9.** *"Which channel did you use first to arrange this episode?"*
*Type: Multiple choice, "Other" enabled.* Options: **Brand service centre / Independent technician / Service marketplace such as Urban Company / Landlord or PG manager / Building staff / Retailer / Other / Cannot recall**.

**S10.** *"What happened after that first contact?"* (Optional — ask before the structured effort questions, deliberately unprimed.)
*Type: Paragraph, marked optional.*

## Section 5 — Effort, outcome, segmentation

**S11.** *"After the first contact, how many follow-up contacts did you initiate about this same episode?"* (Distinct call attempts or message exchanges, not every message bubble.)
*Type: Multiple choice.* Options: **0 / 1 / 2 / 3-4 / 5-7 / 8 or more / Cannot recall**.

**S12.** *"About how many minutes did you actively spend arranging this episode in total?"* (Calling, messaging, finding records, approvals — exclude passive waiting and hands-on repair.)
*Type: Short answer, response validation = number.* Add "Cannot recall" as a checkbox option below it, or a separate optional multiple-choice fallback.

**S13.** *"What is the episode's current status?"*
*Type: Multiple choice, "Other" enabled.* Options: **Completed and machine usable / Provider finished but issue remains / Still waiting for service or repair / Cancelled or abandoned / No service needed after assessment / Other**.
*Branching: "Completed and machine usable" → show S14. All other answers → skip S14, go to S15.*

**S14.** *(only if S13 = completed)* *"About how long passed between the first request and the machine becoming usable?"*
*Type: Multiple choice.* Options: **Same day / 1-2 days / 3-7 days / 8-14 days / 15 or more days / Cannot recall**.

**S15.** *"Overall, how frustrating was arranging this episode?"*
*Type: Linear scale or Multiple choice (not a diagnostic scale, just reported experience).* Options: **Not at all / Slightly / Moderately / Very / Extremely / Prefer not to answer**.

**S16.** *"Was there a time you decided to leave the next action until later?"*
*Type: Multiple choice.* Options: **Yes / No / Cannot recall**.
*Branching: "Yes" → show S16a.*

**S16a.** *(only if S16 = Yes)* *"What was the main reason at that time?"* (No suggested laziness/procrastination framing.)
*Type: Paragraph, optional.*

**S17.** *"Who had final authority to approve repair spending?"*
*Type: Multiple choice, "Other" enabled.* Options: **Me / Another household member / Landlord or PG manager / Building or association representative / Joint approval / Other / No spending decision was needed / Do not know**.

**S18.** *"Who paid the provider?"*
*Type: Multiple choice, "Other" enabled.* Options: **Me / Another household member / Landlord or PG operator / Building or association / Other / Not paid yet / No payment required / Do not know**.

**S19.** *"Did a physical item need to be transported for this episode?"*
*Type: Multiple choice.* Options: **Yes / No / Do not know**.
*Branching: "Yes" → show S19a, S19b.*

**S19a.** *(only if S19 = Yes)* *"What moved?"*
*Type: Checkboxes, "Other" enabled.* Options: **Part or consumable / Whole machine / Other**.

**S19b.** *(only if S19 = Yes)* *"Who arranged that movement?"*
*Type: Multiple choice, "Other" enabled.* Options: **Me / Provider / Another person (please specify role) / Do not know**.

**S20.** *"What, if anything, did you do to make the arrangements easier?"*
*Type: Paragraph, optional.*

**S20a** *(added this project — the workaround-artifact evidence type, `context.md` Part 1.3's attachment guidance)*: *"Do you keep any personal record for this — a note, a notebook, a folder, a WhatsApp chat with just yourself, a sticker on the appliance, anything like that? If you're comfortable sharing a photo of it, tell us how to reach you."*
*Type: Paragraph for the description, optional, plus a separate Short-answer field for contact info — keep this contact field's responses split from the anonymous export at analysis time, per the existing consent design.*

**S21.** *"What was the most important thing you wanted to avoid during this episode?"*
*Type: Paragraph, optional.*

## Section 6 — Demographics *(always shown, including to S2=No/Cannot-recall respondents)*

**S22.** *"What is your age band?"*
*Type: Multiple choice.* Options: **18-24 / 25-34 / 35-44 / 45-54 / 55-64 / 65+ / Prefer not to say**.

**S23.** *"Which city do you currently live in?"*
*Type: Short answer.* Add **"Prefer not to say"** as an alternative — either a checkbox or accept it as free text.

**S23a.** *(optional)* *"Living arrangement:"*
*Type: Multiple choice.* Options: **Family home / Rented alone / Shared rental / PG-hostel / Other / Prefer not to say**.

**Channel tag** *(not shown to respondent — set by whoever posts the link, per distribution channel; or add as a final admin-only multiple choice if self-report is more reliable given open WhatsApp forwarding, per `research_plan.md` §4)*: **My Home community channel / Standalone-household network / Eluru network / IIITH campus / Other/forwarded/unknown**.

## Section 7 — Optional module *(only offered to S2 = Yes respondents: "Would you answer a few more questions about the same episode?" Yes/No — "No" skips to end)*

**S24.** *"Was warranty or an AMC relevant to this episode?"*
*Type: Multiple choice.* Options: **Yes / No / Unsure**.
*Branching: "Yes" → show S24a.*

**S24a.** *"How did you find the relevant information?"*
*Type: Multiple choice, "Other" enabled.* Options: **Paper document / Email / Message or photo / Provider told me / Someone else found it / Could not find it / Other**.

**S25.** *"Did the quoted amount change after you first agreed to it?"*
*Type: Multiple choice.* Options: **Yes / No / No quote agreed / Cannot recall**.
*Branching: "Yes" → show S25a.*

**S25a.** *"What happened next?"*
*Type: Paragraph.*

**S26.** *"About how much did your household actually pay for this episode so far?"*
*Type: Short answer, numeric, optional* — with alternatives **Nothing / Do not know / Prefer not to say** as a fallback multiple-choice.

**S27.** *"Did you pay anyone separately to handle the arrangements?"*
*Type: Multiple choice.* Options: **Yes / No / Do not know**. If Yes, optional numeric follow-up for amount.

**S28.** *"Which one action would you most want another person to handle next time?"*
*Type: Paragraph, with a "None" option available.*

**S29.** *"Which one decision would you keep for yourself?"*
*Type: Paragraph, with "None" / "Unsure" options available.*

**S30.** *"Is there anything about this experience we have misunderstood or missed?"*
*Type: Paragraph, optional.*

## Section 8 — End

> *Thank you. If you'd be willing to discuss this experience further for 20-30 minutes, [insert a separate opt-in link/contact here] — no one will be auto-enrolled from this survey alone.*

---

## Distribution checklist before you actually launch

- [ ] Replace the `[team-controlled contact]` placeholder in Section 1 with a real one (this was flagged as the one real outstanding item in the original audit, `best_practices.md` §6)
- [ ] Post into all channels per `research_plan.md` §4: My Home, standalone-household network, Eluru network, IIITH campus (via Sricharan) — same form, not four different ones
- [ ] Confirm Forms' branching/sections match the conditional logic above (S13→S14, S16→S16a, S19→S19a/b, S24→S24a, S25→S25a) — test the flow yourself once before sharing
- [ ] Set response destination to a Sheet, and separate the S20a/contact-info field from the rest at export time
