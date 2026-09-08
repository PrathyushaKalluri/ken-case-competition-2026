# Research Plan — Interviews, Survey, and Evidence Capture Across Stakeholders

Built from `best_practices.md` (all 20 textbooks + 3 years of Ken winner patterns), `system_map.md` (resource-scan + Household Service Memory synthesis), `narrowed_problem.md` (the confirmed access map and whitespace prior), and Sricharan's `research/report-source.md` + `Fieldwork_Templates.md`. Re-verified against the live competition page (`files/ken_case_competition_2026_page.txt`) before writing this — nothing new found there beyond what's already documented, confirming this plan is grounded in the actual, current rules.

## 0. What every piece of this plan is actually for

The competition's own Q2 instructions, quoted exactly, because every design choice below traces back to one line in it:

> *"Evidence. Did a real person tell you this? Interviews, recordings, and **what you found that you weren't looking for** while designing the solution."*
>
> *"What you can attach (optional): an audio/video recording with a timestamp marking the moment the insight surfaced; a photograph of the workaround itself; a survey with the raw answers and a line on which answer you did not expect; your team's working notes; chat logs, including logs of you working the problem through with an AI."*

Five attachment types, one explicit reward for serendipity. This plan is organized so all five get captured systematically, across every stakeholder, not left to chance in the moment.

**Compliance re-check (re-verified again this turn — full-file grep, not memory)**: every section of the live page — the 10 questions and their exact word limits, ground rules, judging criteria, eligibility, partners, timeline — is captured in `context.md` Part 1.3 and threaded through `narrowed_problem.md`/`research_plan.md`. The one real gap found this pass was the workaround-artifact probe being narrower than the page's own examples (fixed in §3 and §4 below — see the correction). Nothing else missing.

---

## 1. The full stakeholder map

### Confirmed access

| # | Stakeholder | Segment | Side | Location | Status | Who reaches out |
|---|---|---|---|---|---|---|
| 1-2 | Eluru household(s) | Tier-3, presumably independent (to confirm, not assume) | Demand | Eluru, AP | Confirmed, 1-2 | You |
| 3 | Eluru electrician | Tier-3, independent | Supply | Eluru, AP | Confirmed | You |
| 4 | Eluru institutional technician | Tier-3, institutional (school/office) | Supply | Tier-3 city (unconfirmed which) | Uncertain — stretch only | You |
| 5 | My Home household | Metro, managed-community | Demand | Hyderabad | Confirmed — you live there or immediate family does | You |
| 6 | My Home technician | Metro, managed-community's own service network | Supply | Hyderabad | Confirmed (per this turn) | You |
| 7 | Standalone apartment household | Metro, independent | Demand | Hyderabad | Confirmed (new, this turn) | You |
| 8 | IIITH campus professor/staff | Metro, institutional-managed | Demand | Hyderabad | Confirmed | Sricharan |

### Recommended additions — my own call, per your instruction to design this fully; each flagged by how to get it

| Stakeholder | Why it matters | How to get it |
|---|---|---|
| **Standalone-Hyderabad technician** | Completes the demand+supply pair for the independent-metro segment — right now My Home and Eluru both have a household+technician pair, standalone Hyderabad only has the household side | **Snowball from #7**: ask the standalone household who they actually call, and ask if that person is reachable for a short conversation. This is the single highest-value addition to the design and costs nothing new to arrange. |
| **IIITH campus maintenance/facility technician** | Completes the pair for the institutional-managed segment, and is a natural comparison to My Home's technician (both "managed," different kind of institution) | Ask Sricharan if campus facilities staff are reachable — same snowball logic as above. |
| **A landlord** (if reachable through any of the above households) | The case's own strongest piece of evidence (`system_map.md` §1.5) is the AC tenant-landlord dispute, and Indian rent law leaves it a documented grey zone (`system_map.md` §4) — a real landlord conversation would be the single hardest-to-get, highest-value data point in this whole plan | Ask every household respondent, especially any renter, whether their landlord would be willing to talk for 10 minutes. Don't force it — a "no" is fine, but always ask. |

**This is now 8 confirmed + up to 3 recommended = 8-11 possible interviews.** That's a real change from the earlier 3-6 target — see §2.

---

## 2. Revised interview volume: 6-9, up from 3-6

The original 3-6 target (`team_reconciliation.md` §4) was set before this much real access was confirmed. With 8 stakeholders already confirmed across a genuinely comparative design, artificially capping at 6 would mean cutting a real, already-arranged contact for no reason. **Recommendation: do all 8 confirmed interviews if time allows (they cost nothing extra to arrange — no new recruitment), treat the 3 recommended additions as stretch goals pursued only via the free snowball-referral method above, not through new cold outreach.** This directly serves the Thoroughness and Evidence judging criteria (`best_practices.md` §1.1) without adding real recruitment risk, since every one of the 8 is already-arranged access, not a new ask.

If time genuinely runs short, priority order if you must cut: keep all of #1-3, #5-7 (the core comparative structure); #4 and #8 are the two most droppable without breaking the design (though #8 also serves the de-confounding purpose from `narrowed_problem.md` §4 Decision 3, so cut #4 first if forced to choose).

---

## 3. Per-stakeholder interview guides

Base guides remain Sricharan's (`research/report-source.md` Page 7-8: 14 household questions, 8 technician questions, plus a landlord/PG-manager addendum already written there). Every stakeholder below gets the base guide for their type (household or technician) **plus** the specific deltas listed — don't re-derive a new guide from scratch per person, layer these additions on.

### Household stakeholders (#1-2, 5, 7, 8) — base: Sricharan's 14 questions

**Universal additions, all household interviews** (from `narrowed_problem.md` Decision 1 and this project's earlier probes):
- *"When this happened, who actually resolved it — did you contact someone yourself, or did it go through a building/society/management system of some kind?"* (asked after Sricharan's Q3)
- *"Is this a formal contract/AMC, or more of an ongoing relationship with someone specific you call?"*
- *"Do you already get automatic reminders for anything else — like vehicle insurance/PUC, or gas cylinder booking? How does that compare to how you're reminded, or not, about this?"*
- *"Is there anything you've personally built to keep track of this — a note on the fridge, a notebook, a folder of documents, a WhatsApp chat you keep with just yourself, a sticker on the machine, anything like that? Could I see it?"* — deliberately broadened to match the competition page's own examples verbatim (*"the whiteboard on the fridge, the notebook, the folder of medical reports, the WhatsApp chat someone keeps with themselves"*), not just stickers/log books. **Always ask to see and photograph it, with consent — don't accept a verbal description as a substitute.** This is the single most under-collected evidence type across most teams' submissions, per the page's own framing (*"the systems people build by hand say more than what they tell you about them"*).
- **Landlord ask** (renters only): *"Would your landlord be open to a 10-minute conversation about how repairs get decided?"*

**Segment-specific deltas:**
- **Eluru households (#1-2)**: add *"Does your building or area have any kind of shared maintenance service, or does everyone arrange their own?"* — tests the "presumably independent" assumption directly rather than taking it for granted (`narrowed_problem.md` §4 Decision 3).
- **My Home household (#5)**: add *"When you raise a request with the community, what actually happens step by step — who do you contact, how long does it usually take, and has it ever not worked the way you expected?"* — the community's own system is the "smooth case" hypothesis; the goal here is to find where it's *not* actually smooth, since a partial failure in the managed case is a sharper finding than either "it's perfect" or "it's broken" would be.
- **Standalone Hyderabad household (#7)**: add *"Have you ever wished you had access to something like a building management service? What would you actually want it to do?"* — this is the direct counterfactual question against My Home's real system, asked to someone who's never had it.
- **IIITH campus (#8)**: add *"Is this handled through campus facilities, or do you arrange it yourself even though you live on campus?"* — campus "managed" status shouldn't be assumed any more than Eluru's "independent" status should.

### Technician stakeholders (#3-4, 6) — base: Sricharan's 8 questions

**Universal additions, all technician interviews**:
- *"When a customer is due for a follow-up or repeat service, what actually reminds you to reach out — and how often does that step fail?"* (tests the AMC-vendor-forgetting finding, `system_map.md` §6.4) — **ask without assuming a formal AMC concept exists**; "we don't really have that here" is itself the finding for Eluru specifically.
- *"When a part was needed, how long did it actually take to arrive, and from where?"* — the direct **logistics-rail-completeness probe** (`narrowed_problem.md` Decision 1b). Answers from this question, tagged by location, are what let synthesis actually compare part-availability/delivery speed between Eluru and Hyderabad rather than assume it.

**Segment-specific deltas:**
- **Eluru electrician (#3)**: add *"How do most of your customers find you — word of mouth, repeat customers, something else? Has that changed over the years?"* — tests whether tier-3 technician-customer relationships are structurally different (more personal, less app-mediated) per the whitespace prior in `narrowed_problem.md` Decision 1.
- **My Home technician (#6)**: add *"How does a job reach you through the community — is there a fixed panel of vendors, a rotation, something else? What happens if you're not available?"* — the single most valuable question in the whole plan for understanding *what the community's system actually does mechanically*, which is exactly what an agent would need to replicate if My Home turns out to be the smoother case. Also add *"Are prices/rates for common jobs pre-agreed with the community, or negotiated fresh each time?"* — the **payments/authorisation-rail-completeness probe** (`narrowed_problem.md` Decision 1b), testing whether My Home's system already partly substitutes for delegated spend authority in a way standalone/Eluru households can't access.

---

## 4. Survey plan

Base instrument: Sricharan's S0-S30 (`research/report-source.md` Pages 10-12), already audited and cleared (`best_practices.md` §6). Two additions, both minimal and consistent with the existing audit's own good practice:

**Addition 1 — one new screening item**, insert immediately after S7 ("Who owned this machine?"):

> **S7a. "Does your home/building have a dedicated facilities or maintenance service you can raise a request with (e.g. through a builder or community management office), or do you arrange repairs yourself each time?"** Options: A dedicated community/facility management service / I arrange it myself each time / Some of both, depends on the issue / Don't know.

This operationalizes the managed-vs-independent axis (thread #18) as a self-report variable for *every* respondent, regardless of which channel they came from — important because a survey link can travel beyond its original distribution group.

**Addition 2 — channel tagging**, using a field the survey plan already calls for (`report-source.md` Page 9: *"record survey version, date, language, recruitment channel"*) — just make the values specific:

> Recruitment channel options: My Home community channel / Standalone-household network / Eluru network / IIITH campus / Other (specify).

This turns the survey from a single undifferentiated pool into a dataset cuttable by the same comparative structure as the interviews — a 30-50 response survey segmented this way is a genuinely rare piece of evidence for a 2-day sprint.

**Addition 3 — a workaround-artifact question, currently missing entirely.** The survey had no question asking about this at all — a real gap, since it's explicitly one of the 5 attachment types the competition names (`context.md` Part 1.3, §0 above). Insert in the optional module (`report-source.md` Page 12, right after S20 — "what did you do to make the arrangements easier"):

> **S20a. "Do you keep any personal record for this — a note, a notebook, a folder, a WhatsApp chat with just yourself, a sticker on the appliance, anything like that? If you're comfortable sharing a photo of it, tell us how to reach you."** Free text for the description, plus an optional contact field (kept separate from the anonymous response export, per the existing consent/data-handling rules on Page 9).

This is a direct survey-side counterpart to the broadened interview probe above — the same evidence type, captured at scale instead of one conversation at a time. Even a handful of people volunteering a photo this way is real evidence you wouldn't get from interviews alone.

**Distribution — revised for open WhatsApp sharing, not four closed channels.** You confirmed the plan is to float this directly into WhatsApp groups, where anyone can see and answer it, forward it, or have it reach people well outside the four planned channels (My Home, standalone, Eluru, campus). **This is fine, and arguably better for reaching the 30-50 response target — but it changes what the "recruitment channel" tagging in Addition 2 can promise.** Treat it as: post into the four known channels as planned (still record which one it was posted into), but **add a 5th value — "Other / forwarded / unknown" — to the channel field**, and rely on **S7a (managed-vs-independent) plus S22/S23 (age band, city)** to actually classify each response after the fact, not on the posting channel alone. A response from an unexpected city or an unplanned community is not a problem — it's bonus signal — but keep it visibly tagged as outside the core Hyderabad+Eluru claim (per the convenience-sample honesty discipline in `best_practices.md` §6) rather than silently folded into the main count.

**Stakeholders this open distribution might surface, worth being ready to recognize and tag (not actively recruited for, since none of these are confirmed access — just don't discard the data if it shows up)**:
- A renter specifically, distinct from an owner even within the same managed/independent structure — S7 already captures ownership, cross-tab it against S7a.
- Someone managing an elderly parent's household remotely, rather than their own — an ICP already named in the original context files (`keeping_the_machines_running_context.md` ICP D) but never actively pursued; if a response describes this, flag it specifically rather than folding it into the general household pool, since it's a structurally different coordination problem (the coordinator and the resident are different people).
- A respondent from a different managed community altogether (Hyderabad has several large builder-groups besides My Home — Aparna, Prestige, Rajapushpa, and others) — S7a's generic wording ("a dedicated community/facility management service") already captures this without needing to name every builder, so no survey change needed, just don't assume every "managed" response is My Home specifically when writing up findings.

**No technician survey.** With only 3-4 technician contacts total, a survey adds no statistical value a direct conversation doesn't already give better — per `best_practices.md` §6's own construct-validity logic, don't build an instrument for an N too small to need one. Use Sricharan's `Fieldwork_Templates.md` participant/incident record instead, filled in identically for every technician conversation, so they stay comparable to each other even without a formal survey.

---

## 5. Evidence capture matrix — the 5 attachment types, made concrete per stakeholder

| Attachment type (from the competition page) | What to actually do |
|---|---|
| **Recording with a timestamped insight moment** | For every interview (household or technician) where consent is given: record, and the moment someone finishes their answer to the "who actually resolved it" or "what actually reminds you" questions, note the timestamp immediately — don't rely on finding it later in a long file. |
| **Photograph of the workaround itself** | Ask explicitly, every household interview: any sticker, log book, WhatsApp thread, warranty card, or notebook — per §3's added probe. This is the single most under-collected evidence type in most teams' submissions because it requires asking, not just listening. |
| **Survey with raw answers + one unexpected result** | Already covered in §4 — but explicitly assign someone to flag, after the survey closes, which single answer nobody on the team predicted. Don't skip this step; it's literally named in the judging criteria. |
| **Team's working notes** | Use Sricharan's own prescribed sessions (`report-source.md` Page 13: a 35-minute pre-interview ideation session, a 60-90 minute synthesis session) — and actually **photograph the whiteboard/sticky notes from those sessions**. Easy to do the session and forget to capture it as evidence. |
| **Chat logs, including AI logs** | You already have this, and it's substantial: the entire documented Claude Code session pushed to `github.com/PrathyushaKalluri/ken-case-competition-2026` — `context.md` alone is a full verbatim record of the problem-solving process with an AI, already public in your repo. Remember to actually reference/attach this, not just treat it as internal working material. |

---

## 6. Turning the comparative structure into the "unique insight" Q2 needs

The design in §1 isn't just "more interviews" — it's a genuine comparative structure most teams won't have: **3 segments (My Home managed / standalone independent / Eluru tier-3) × 2 sides (household / technician) × a triangulation point (IIITH campus)**, per `narrowed_problem.md` §4. The insight most worth chasing during synthesis is specifically a *difference across cells*, not a pattern within just one:

1. **If My Home households report smoother coordination than standalone Hyderabad households** (same metro, same market maturity, different only in managed-vs-independent) — the insight is *what specifically* the community's system does (from #6's mechanical-detail question) that an individual household's agent should replicate.
2. **If Eluru looks different from both Hyderabad segments** in a way that tracks with §1's whitespace prior (less app-mediated, more relationship-based) — the insight is about market maturity, and the vehicle-reminder-comparison probe (§3) becomes the sharpest supporting evidence.
3. **If My Home and Eluru technicians describe the "vendor forgets too" pattern differently** (or one has no AMC concept at all) — that's a genuinely non-obvious finding neither the case brief nor any competing team's likely single-city research would surface.
4. **Actively log anything that surprises you**, per §0's Evidence-criterion quote — keep a running list titled "what we weren't looking for," updated after every interview, separate from the hypothesis-confirmation notes. This is where the most-rewarded kind of finding tends to hide.

Do not force a finding into this structure if the data doesn't support it — an honestly narrower insight from 2-3 corroborating cells beats an overstated one stretched across all 8, per the evidence discipline already established throughout this project (`system_map.md` §0, `best_practices.md` §6).

### 6a. Rail-build potential is now a required synthesis step, not optional

Per direct instruction: the insight alone isn't enough — whichever object/mechanism the interviews converge on must also genuinely support **all three rails** (Voice; Payments & Authorisation, one combined rail; Logistics — not four separate things, see `narrowed_problem.md` Decision 1b), since this is what Round 2 actually builds on if you're shortlisted. Add this as an explicit, required step in the synthesis session (§0's Team's-working-notes evidence, `report-source.md` Page 13's 60-90 minute session):

1. **Tag every incident's Q9-equivalent answer** ("did any item need to move somewhere") for logistics-completeness — this question is already in every household interview; the only new work is tagging the answers during synthesis instead of letting them sit unused.
2. **Tag every incident's role-separation answers** (coordinator/owner/approver/payer/access-provider, already in Sricharan's guide) for payments/authorisation-completeness — a real approval-vs-payer split is what makes delegated authority (`Keeping_Machines_Running_Context.md` §7B) a genuine mechanism, not decoration.
3. **Score the object that actually emerged against `narrowed_problem.md` Decision 1b's table** — if it lands on a logistics-weak candidate (most likely trade/repair services), actively check whether any specific incident within it involved a real part, before concluding the rail is absent. A logistics rail can be honestly absent with a stated reason (the competition allows this), but check before defaulting to that.
4. **Use the two new rail-completeness probes** (technician guides, §3) to compare whether payments/authorisation matters more for independent households than My Home, and whether logistics is genuinely worse in Eluru than Hyderabad — both are testable, free byproducts of the comparative design already built, not separate work.

---

## 7. Readiness checklist before starting

- [ ] Confirm with My Home technician contact (#6) and get a rough sense of their availability
- [ ] Ask standalone household (#7) for a technician referral (the snowball addition from §1)
- [ ] Ask Sricharan about campus facilities-technician access (the other snowball addition)
- [ ] Insert S7a into the survey instrument and update the channel-tagging field before distribution
- [ ] Assign one person to own the "working notes" photography for both ideation and synthesis sessions
- [ ] Assign one person to own tracking "what we weren't looking for" across all interviews
- [ ] Reconfirm consent script covers recording, photography, and the specific quote-publication rule (age-band + city, never a name) before the first interview
