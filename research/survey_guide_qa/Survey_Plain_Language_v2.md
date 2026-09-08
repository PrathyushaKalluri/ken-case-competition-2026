# Household Repair & Servicing Survey — v2 (tested, Google Forms-ready)

**What changed from v1, from two cognitive pilot tests (a Hyderabad homemaker, a Visakhapatnam homemaker):**
1. Section 2's "most recent time" instruction had no tie-breaking rule — a respondent with two candidate incidents in the same week (routine + a repair) would inconsistently pick whichever felt more "dramatic," quietly biasing the whole dataset toward breakdowns over routine servicing. Added an explicit tie-breaker and broadened the framing to include routine maintenance up front.
2. Q8 had no option for "wasn't working as well as before" or "routine top-up, nothing broken" — a real, common case was being forced into "Other" or misreported as "regular yearly service."
3. Q17 assumed a breakdown ("first noticed the problem") for everyone, including people whose incident was a scheduled filter change with no problem to notice. Now branches its wording based on the Q8 answer.
4. "PUC" was used with no explanation at all — a hard comprehension failure for a respondent who doesn't handle the family vehicle. Spelled out in full.
5. Q23's options didn't include the single most common way ordinary people actually track a technician's number — a saved phone contact. Added explicitly.
6. Q19 secretly asked two different questions at once ("who decided to proceed" and "who approved the price") as if they were the same decision — split into two.
7. Q11/Q12 conflated an official community office with an informal WhatsApp recommendation — these are structurally different and now have separate options.
8. Q33 duplicated Q5 almost exactly, with a different, incompatible answer scale — cut.
9. Q15's free numeric-entry mechanic was awkward to build cleanly in Google Forms and invited overthinking — converted to time bands.
10. Fixed a duplicate "Section 6" label (drafting error), moved the "hardest part" question earlier (right after the hassle question) so all the richest qualitative content isn't stacked in one four-question block at the very end, and added a framing line before the remaining open-text block.

**Target respondents**: residents of gated communities/apartments in Hyderabad and Visakhapatnam — mostly housewives, plus other household members. Distributed via WhatsApp group links. Plain, everyday English throughout, no jargon left unexplained. Estimated time: 4-6 minutes core path; well under a minute for someone screened out early.

---

## FORM DESCRIPTION (top of Google Form, before any question)

> Hi! We are a student team (Invictus, IIIT Hyderabad) doing a short study on how families in apartment communities handle getting things repaired or serviced at home — things like the AC, fridge, washing machine, geyser, water purifier, and so on. This includes both breakdowns and routine things like a filter change or a gas top-up.
>
> This survey takes about 5 minutes. It's completely voluntary — you can skip anything or stop anytime — and your answers are anonymous; we only keep your rough age group and city, never your name. Your anonymised answers may be used in a student case-competition submission (The Ken 2026) and, if selected, seen by the competition's judges.
>
> We are not selling anything and we will never ask for money, OTPs, or bank details.
> Questions? Contact: [insert a real team phone/email before launch].

---

## SECTION 1 — A couple of quick questions first

**Q1.** Do you agree to answer this survey on the basis explained above?
*Multiple choice.* Yes / No
*Branching: No → end of form.*

**Q2.** Are you 18 years or older?
*Multiple choice.* Yes / No / Would rather not say
*Branching: only Yes continues.*

**Q3.** Which city do you currently live in?
*Multiple choice.* Hyderabad / Visakhapatnam / Other (please type)

**Q4.** What is the name of your apartment community/building? (This just helps us understand which areas we're reaching — it won't be shared with anyone, and it's fine to skip.)
*Short answer, optional.*

**Q5.** In your home, who usually deals with getting things repaired or serviced — calling someone, following up, and so on?
*Multiple choice.* I usually do it myself / Someone else in my home usually does it, but I know what happens / I don't really know much about this in my home

**Q6.** In the last 3 months, were you personally involved in getting any appliance or home service fixed, serviced, or newly installed — this includes routine things like a filter change or gas top-up, not just breakdowns?
*Multiple choice.* Yes / No / Not sure
*Branching: No/Not sure → skip to Section 6 (About you) → end. Yes → continue to Section 2.*

---

## SECTION 2 — Tell us about one specific time

*Intro text shown to respondent:* Think about the most recent time in the last 3 months that you personally were involved in getting an appliance or home service repaired, serviced, or installed. **If more than one thing happened around the same time — say, two different things in the same week — please pick whichever one happened last, even if it was only a day or two after the other.** It doesn't need to be the bigger or more complicated one. Please keep that one specific time in mind for all the questions below.

**Q7.** Which appliance or service was this about?
*Multiple choice, "Other" allows free text.* AC / Fridge / Washing machine / Water purifier / Geyser / Kitchen appliance (mixer, chimney, etc.) / Some other home service (pest control, plumbing, electrical) / Other

**Q8.** What was the situation?
*Multiple choice, "Other" free text.* It stopped working completely / It wasn't working as well as before (for example, not cooling properly, or weak water flow) / New installation / Regular yearly service / Routine maintenance or top-up, nothing broken (like a filter change or gas refill) / Following up on an earlier repair that didn't fully work / Other / Don't remember

**Q9.** Roughly when did this happen?
*Multiple choice.* In the last week / 2-4 weeks ago / 1-3 months ago / Don't remember

**Q10.** Whose appliance is it, technically?
*Multiple choice, "Other" free text.* Mine or my household's / My landlord's / It belongs to the community/building / Other / Not sure

**Q11.** Does your community/building have an official maintenance office or an approved list of people to call, or does everyone arrange repairs on their own?
*Multiple choice.* Yes, there's an official community service/office or approved list we're expected to use / No, everyone arranges it themselves, even if people sometimes recommend technicians informally (like in a WhatsApp group) / A bit of both, depends on the issue / Not sure

**Q12.** How did you first get in touch with whoever came to help?
*Multiple choice, "Other" free text.* Called the brand's service centre / Called a technician I already knew / Used an app (like Urban Company, Housejoy) / Through the building/community's official office or approved list / Someone was recommended in a resident WhatsApp/community group / Asked a shop / Don't remember

**Q13.** In your own words — what happened after you first reached out? (Totally optional, write as much or as little as you like.)
*Paragraph, optional.*

---

## SECTION 3 — How much this took from you

**Q14.** After you first got in touch, how many more times did you have to call or message about this same issue?
*Multiple choice.* None / 1 / 2 / 3-4 / 5-7 / 8 or more / Don't remember

**Q15.** Roughly how much of your own time did this take in total — calls, messages, or looking things up (not counting the actual repair time)?
*Multiple choice.* Hardly any (0-5 minutes) / A few minutes (6-15) / About 15-30 minutes / About 30-60 minutes / More than an hour / Don't remember

**Q16.** What is the situation now?
*Multiple choice, "Other" free text.* Fully fixed and working / They said it's done but the problem is still there / Still waiting / We cancelled/gave up / Turned out nothing needed fixing / Other
*Branching: "Fully fixed and working" → show Q17. Others → skip to Q18.*

**Q17.** (only if fully fixed — wording depends on the Q8 answer)
*If Q8 = "stopped working," "wasn't working as well," or "following up on earlier repair":*
> From when you first noticed something was wrong to when it was actually working again, how long did it take?
*If Q8 = "regular yearly service," "routine maintenance/top-up," or "new installation":*
> From when you decided to get this done to when it was actually completed, how long did it take?
*Multiple choice (same options either way).* Same day / 1-2 days / 3-7 days / 8-14 days / 15 days or more / Don't remember

**Q18.** Overall, how much hassle did this take for you?
*Multiple choice.* Very little / A little / A moderate amount / A lot / A huge amount / Would rather not say

**Q19.** Looking back, what was the most difficult or annoying part of the whole thing, if anything? (If honestly nothing was difficult, that's a completely fine answer too.)
*Paragraph, optional.*

---

## SECTION 4 — Who decided, and who paid

**Q20.** Who decided to go ahead and get it fixed — that is, who made the call to contact someone or let the work start? (This counts even if it felt like a small, easy decision.)
*Multiple choice, "Other" free text.* Me / Another person in my household / My landlord / The building/community office / We decided together / No real decision was needed / Not sure

**Q21.** If the cost came up at all, who had the final say on whether the price was okay?
*Multiple choice, "Other" free text.* Me / Another person in my household / My landlord / The building/community office / No cost discussion happened / Not sure

**Q22.** Who actually paid for it?
*Multiple choice, "Other" free text.* Me / Another person in my household / My landlord / The building/community office / Not paid yet / Nothing to pay / Not sure

**Q23.** Did the price change after it was first agreed?
*Multiple choice.* Yes / No / No price was agreed in advance / Don't remember
*Branching: Yes → Q23a*

**Q23a.** (only if price changed) What happened then?
*Paragraph.*

**Q24.** Did any part, or the whole appliance, have to be picked up, sent somewhere, or delivered from somewhere else?
*Multiple choice.* Yes / No / Not sure
*Branching: Yes → Q24a*

**Q24a.** (only if yes) Who arranged that?
*Multiple choice, "Other" free text.* I did / The technician/company did / Someone else / Not sure

---

## SECTION 5 — Remembering and keeping track

**Q25.** Do you keep track of servicing dates or technician numbers in any way — like a saved phone contact, a note, a notebook, a sticker on the appliance, or a WhatsApp chat?
*Multiple choice.* Yes — a saved contact/number in my phone / Yes — a note, list, or notebook / Yes — something else / No, I don't keep track of it / I just remember it in my head
*Branching: any "Yes" → Q25a*

**Q25a.** (only if any "Yes" above and it isn't just a phone contact) Could you briefly describe it — what it is, and how you made it?
*Paragraph, optional.*

**Q26.** Is this specific appliance under a paid yearly service contract (sometimes called an "AMC," or annual maintenance contract), or do you just call someone you know when something breaks?
*Multiple choice.* Yes, I pay a yearly fee for regular servicing / No, I just call someone I know when needed / No fixed arrangement either way / Not sure

**Q27.** Do you get automatic reminders for anything else at home — like renewing vehicle insurance, your vehicle's pollution certificate (PUC), or booking your cooking gas cylinder? How is that different from how (or whether) you get reminded about appliance servicing? (Totally optional.)
*Paragraph, optional.*

---

## SECTION 6 — A few more in your own words

*Intro text shown to respondent:* Just a few optional questions left where we'd love to hear it in your own words. Skip anything you don't feel like answering.

**Q28.** Has there ever been a small repair at home that you just never got around to calling anyone about — you either lived with it, fixed it yourself, or asked a friend/family member instead? Tell us briefly what happened.
*Paragraph, optional.*

**Q29.** If someone you fully trusted could handle all of this for you next time, which part would you happily hand over to them, and which part would you always want to decide yourself?
*Paragraph, optional.*

**Q30.** Is there anything about this whole experience we haven't asked about, but you think we should know?
*Paragraph, optional.*

---

## SECTION 7 — About you *(shown to everyone, including those screened out at Q6)*

**Q31.** What is your age group?
*Multiple choice.* 18-24 / 25-34 / 35-44 / 45-54 / 55-64 / 65 or older / Would rather not say

**Q32.** Which of these best describes you?
*Multiple choice.* Woman / Man / Prefer to self-describe / Would rather not say

**Q33.** Which of these best describes your home?
*Multiple choice, "Other" free text.* Own home / Rented / Staying with family / PG or shared accommodation / Other / Would rather not say

---

## CLOSING SCREEN

> Thank you so much for your time! If you'd be open to a short 20-30 minute conversation about your experience (completely optional, separate from this form), you can leave your contact here: [separate optional link] — nobody will contact you unless you fill this in yourself.

---

## Google Forms build notes

- Use "Sections" (the Forms feature) for every branch point, not just headers: Q1→end, Q2→end, Q6→Section 6, Q16→Q17 skip, Q23→Q23a, Q24→Q24a, Q25→Q25a.
- Turn OFF "Shuffle question order" — the ordering is deliberate (unprimed open questions before structured ones, general before specific), per the anti-priming principle both this project's own prior survey audit and Pew Research's question-order guidance rely on.
- Do NOT turn on "Limit to 1 response" (which requires Google sign-in) — this would break the anonymity promise made in the form description and reduce willingness to respond in a WhatsApp-forwarded context. Instead, catch duplicates at the analysis stage (see the false-positive section in the main document).
- Q17's branch-by-Q8-wording needs two near-identical question objects in Forms (one per wording), each shown only for the relevant Q8 answers via section branching — Forms cannot conditionally swap question *text* within one question object.
