# Household Repair & Servicing Survey — v3 (redesigned: 17 questions, generic, rail-mapped)

**Why this redesign happened**: real feedback on v2 was direct — 33 questions is too long, nobody actually finishes a survey like that, and it was over-fitted to two named cities instead of being usable anywhere. This version cuts to **17 questions total** (down from 33), removes every Hyderabad/Visakhapatnam-specific framing so the same form works for any Indian household, collapses every place v2 asked a "chain" of related sub-questions (who decided / who approved the price / who paid / who let the technician in, asked as four separate items) into a single grid question, and drops every question that doesn't directly change a decision about the Q2 insight, the six-step loop, or which of the three rails (Voice / Payments & Authorisation / Logistics) to build on — since that mapping is the actual test each question has to pass now, not generic survey completeness.

**Design principles applied, and why:**
- **Every screen costs completions.** Each additional question is a chance for a self-administered, phone-filled, WhatsApp-distributed form to lose a respondent. The fix is not "make each question shorter" — it's "ask fewer questions," and cut anything that a live interview already captures in more depth (this project already runs 6-9 interviews; the survey's job is breadth and quick counts, not re-collecting the same depth from strangers on WhatsApp).
- **One tap beats one paragraph.** Almost everything is now multiple-choice or a single grid tap. Only two genuinely open questions remain, and both are placed where a one-line answer is realistically enough — not four paragraph boxes in a row.
- **No chained sub-questions.** Anywhere v2 asked three or four closely-related questions in sequence (decision role, approval role, payer role, access role), this version asks them as the rows of one grid question instead — one screen, one fast task, not three or four decisions in a row.
- **Every question earns its place by naming which rail or which of the competition's 10 answers it feeds** — see the mapping table in the main document. A question that doesn't move one of those answers was cut.
- **Nothing is tied to a specific city or named community.** City is a single free-text field; there is no community-name field, no city-specific screening logic, and the WhatsApp message and form description no longer name particular cities. The same form works wherever it's shared.

---

## CONSENT (a single checkbox, not a separate question — reduces friction)

At the top of the form, under the description: a single required checkbox:
> ☐ I am 18 or older, and I agree to answer this survey voluntarily and anonymously.

*(No separate age question, no separate consent question — combining both into one gate removes two full screens from the respondent's path without losing anything the team actually needs.)*

## FORM DESCRIPTION

> Hi! We're a student team researching how Indian families handle getting things repaired or serviced at home — the AC, fridge, washing machine, geyser, water purifier, and so on. This takes about 3-4 minutes. It's anonymous (we only keep your rough age group and city, never your name), voluntary, and we're not selling anything — we'll never ask for money, OTPs, or bank details. Your anonymised answers may be used in a student case-competition submission (The Ken 2026).
> Questions? [insert a real contact before launch].

---

## SECTION 1 — Quick check

**Q1.** In the last 3 months, did you personally help arrange a repair, service, or installation for any home appliance (AC, fridge, washing machine, geyser, water purifier, or similar)?
*Multiple choice.* Yes / No / Not sure
*Branching: No/Not sure → skip to Section 4 (About you) → end.*

---

## SECTION 2 — The most recent time

*Intro text: Think of the most recent time this happened, in the last 3 months. Keep that one time in mind for the next few questions.*

**Q2.** Which appliance or service was this about?
*Multiple choice, "Other" free text.* AC / Fridge / Washing machine / Water purifier / Geyser / Other kitchen appliance / Other home service (plumbing, electrical, pest control) / Other

**Q3.** What was the situation?
*Multiple choice, "Other" free text.* It stopped working completely / It wasn't working as well as before / New installation / Routine maintenance or top-up, nothing broken / Following up on an earlier repair / Other

**Q4.** How did you first get in touch with whoever helped?
*Multiple choice, "Other" free text.* Called a technician I already knew / Called the brand's service centre / Used an app (like Urban Company, Housejoy) / Through my building/society office, or a resident group recommendation / Asked a local shop / Other

**Q5.** Does your building/society have a shared maintenance office you can raise a request with, or does everyone arrange things on their own?
*Multiple choice.* Yes, a shared office or approved list / No, everyone arranges it themselves / A bit of both / Not sure / Not applicable (independent house)

**Q6.** *(Grid/matrix question — one screen, four quick taps)* For this specific time, who was mainly responsible for each of these?
*Type: Multiple-choice grid.*
*Rows:* Deciding to go ahead with the repair / Approving the cost, if it came up / Paying for it / Letting the technician into the home
*Columns:* Me / Another household member / Landlord or building office / Someone else / Not applicable

**Q7.** Was a specific date or time promised for the work, and was it kept?
*Multiple choice.* Yes, and it was kept / Yes, but it wasn't kept / No clear time was given / Don't remember

**Q8.** After your first contact, did you need to follow up more than once before it was resolved?
*Multiple choice.* No, resolved after first contact / Yes, 1-2 more times / Yes, 3 or more times / Don't remember

**Q9.** Did any part, or the whole appliance, need to be picked up or delivered from somewhere else?
*Multiple choice.* Yes / No / Not sure

**Q10.** How do you usually keep track of servicing dates, warranty, or technician numbers? *(Select all that apply)*
*Type: Checkboxes.* A saved contact in my phone / A note, list, or notebook / A WhatsApp chat / We have an AMC or annual contract / I don't track it, I just call when needed / Other

**Q11.** Overall, how much effort or hassle did this take for you?
*Multiple choice.* Very little / A little / A moderate amount / A lot / A huge amount

---

## SECTION 3 — In your own words *(both optional, but genuinely valuable)*

**Q12.** Has there been a small repair or issue at home that you just never got around to calling anyone about, or handled some other way instead of calling a professional? Briefly, what happened?
*Paragraph, optional.*

**Q13.** If a trusted person or service could handle this entire process for you next time, what's the one thing you'd always want to decide or approve yourself?
*Short answer, optional.*

---

## SECTION 4 — About you *(shown to everyone, including those screened out at Q1)*

**Q14.** What is your age group?
*Multiple choice.* 18-24 / 25-34 / 35-44 / 45-54 / 55-64 / 65 or older / Prefer not to say

**Q15.** Which of these best describes you?
*Multiple choice.* Woman / Man / Prefer to self-describe / Prefer not to say

**Q16.** Which of these best describes your home?
*Multiple choice, "Other" free text.* Own home / Rented / Living with family / PG or shared accommodation / Other

**Q17.** Which city do you live in?
*Short answer.* (free text, any city)

---

## CLOSING SCREEN

> Thank you! If you'd be open to a short follow-up conversation (completely optional), leave your contact here: [separate optional link] — nobody will contact you unless you fill this in yourself.

---

## Google Forms build notes

- The consent checkbox goes directly under the description, marked required, before Q1.
- Q6 must be built as a native "Multiple choice grid" question — do not split it into four separate questions.
- Branching: Q1 (No/Not sure) → Section 4 → end. All other flow is linear, no other skips needed — this is deliberate; v2's five separate conditional branches (S13→S14, S16→S16a, S19→S19a/b, S24→S24a, S25→S25a) are gone because the questions that needed them were cut.
- Turn OFF "Shuffle question order" and OFF "Limit to 1 response" (same reasoning as before — anonymity over forced sign-in; catch duplicates at analysis time instead).
