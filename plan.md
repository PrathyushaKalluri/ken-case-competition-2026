# Plan — The Ken Case Competition 2026, Phase 1 (Solution Assembly)

**Deadline: Sep 10, 2026, 11:59 PM IST.** Today is Sep 8, 2026. This plan assumes roughly two days of runway.

This is a living document — update it as interviews happen and the insight converges. See `progress.md` for a lighter-weight status checklist against this plan.

**⚠️ Superseded in part — see `team_reconciliation.md`.** A teammate (Sricharan) independently built a more complete interview guide, survey instrument, and fieldwork capture system in `research/report-source.md` and `research/Fieldwork_Templates.md`. That is now the canonical operating guide; this file's probes below are additive (see `team_reconciliation.md` §3 for exactly where to insert them).

**Resolved**: interview volume is 3-6 interviews + survey rollout (`team_reconciliation.md` §4). The survey itself has been audited and cleared to launch — see `best_practices.md` §6 for the full verdict; only real outstanding item is filling in the `[team-controlled contact]` placeholder in the survey's own intro (`research/report-source.md` Page 10, question S0).

**New**: `best_practices.md` now exists — a synthesis of all 20 reference textbooks (how to think like a designer/systems-thinker/UX-researcher/experiment-designer) plus 3 years of Ken competition winner/judge research. Read it before drafting Q1-Q10; it directly reframes several of the probes and rail-choice reasoning below (e.g. §3's leverage-point test for Q5, §1's judge-quoted warnings against vague AI/financial claims for every answer).

**Superseded again — see `narrowed_problem.md`.** That file now holds the actual, real-access-based recruitment plan (6 interview slots, specific channels, ready to execute today) and the confirmed segmentation axis (managed-community vs. independent-household service-network structure — not renter/owner). The object/machine category is deliberately left unpicked, to emerge from unprimed interviews. Use `narrowed_problem.md` §5 as the operating recruitment plan; this file's Stage 1 interview-split (household/technician/landlord lenses) is now superseded by that more concrete channel-based plan.

---

## Objective

Submit all 10 Phase 1 answers (see `context.md` Part 1.3 for exact question text/limits), converged from **real interview evidence**, not from pre-existing hypotheses — per the team's explicit instruction not to lock an insight before talking to real people.

## Constraints locked in

- Track: **Product Strategy**
- Opening: **Keeping the machines running** (do not switch — switching resets evidence)
- Realistic fieldwork budget: **3-6 interviews** in the next ~24-36 hours
- Team's right-to-win access: personal household pain + technician/service-provider access + renter/landlord vantage point

## Step-by-step plan

### Stage 1 — Fieldwork (today, Sep 8, evening → Sep 9 daytime)

Run 3-6 real interviews, split across the team's three access lenses so all sides of the system get evidence, not just the easiest-to-reach one:
- **2 interviews via the household-pain lens** — pick two respondents whose *most recent* incident involves a *different* appliance/errand from each other (don't let both be AC stories).
- **1-2 interviews via technician/service-provider access** — high priority, since almost no competing team will reach this side in the time available. Use the supply-side questions in the local context files (`Keeping_Machines_Running_Context.md` §12, `keeping_the_machines_running_context.md`'s supply-side prompts).
- **1-2 interviews via the renter/landlord lens** — directly tests the responsibility/authority thread, which Indian rent law already leaves genuinely ambiguous for AC servicing specifically (see `notes.md` §4).

**Method for every interview** (household or supply-side): incident reconstruction, not opinion-gathering.
1. "Tell me about the last time something at home needed fixing, servicing, or arranging."
2. Walk through everything they personally did, step by step.
3. Then: "tell me about the incident before that" — reveals repetition.
4. Critical question for every workflow: **"Who owns making sure this actually gets done?"** then **"If you don't follow up, what happens?"**
5. New candidate probe from this session's research (see `notes.md` §5): **"Do you already have a person — not a company, a specific person — you call for this? How did you end up trusting them?"**
6. Ask to see evidence where comfortable (WhatsApp threads, invoices, call logs, screenshots) — consented, published only as age-band + city per the competition's own rule.
7. Do **not** mention AI, agents, or any of the 17 candidate threads in `notes.md` §2 to respondents — let the pain surface unprompted.

### Stage 2 — Synthesis checkpoint (once 4+ interviews are logged)

1. Log each interview against the 17 (+1) candidate threads in `notes.md` §2 — which it supports, contradicts, or is silent on. Don't force-fit an incident onto a thread it doesn't actually support.
2. Look for **independent corroboration** — the same thread surfacing from respondents who don't know each other and weren't led there. That's the real signal.
3. **Insight test before writing Q2**: can this insight be pointed at a specific place in the Q3 six-step agent loop or the Q5 rail choice that would *change* because of it? If not, it's not sharp enough yet — keep converging.
4. Lock the single sharpest insight in ≤60 words (Q2's hard limit).

### Stage 3 — Draft all 10 answers, working backward from the locked insight

Order to draft in (each should visibly follow from the Q2 insight, not float independently of it):
1. **Q2** (already locked in Stage 2)
2. **Q1** — team + right-to-win, using the access lenses in `decisions.md` #5, rewritten so it couldn't be submitted by "any three students at your college" (the page's own litmus test)
3. **Q3** — six-step agent loop (≤15 words/step): trigger → what it already knows → what it does → who it deals with → what it asks the human, and when → how it knows it's done
4. **Q4** — one sentence per rail (voice/payments/logistics); say plainly if a rail has no role and why
5. **Q5** — the one rail to innovate on (40 words) — current leading candidate from this session's research: **outbound voice that navigates a business's own IVR/call flow on the household's behalf** — the underlying voice tech (Gnani) is production-grade, but nobody has shipped the *outbound-on-behalf-of-a-consumer* version of it (see `notes.md` §4)
6. **Q6** — the one customer asset needed (30 words) + why they'd hand it over
7. **Q7** — the annexation / next use-case subsumed (30 words)
8. **Q8** — which opening you'd never hand to an assistant (one sentence)
9. **Q9** — which Indian company should have built this already (60 words) — candidates surfaced this session worth weighing: an existing home-services marketplace (Urban Company — has the users/data but is optimized for discovery+booking, not post-booking coordination) vs. a payments/voice infra player (has the rails but not the household relationship) — needs a real answer with a specific guess as to *why* they haven't
10. **Q10** — Product Strategy (already decided)

### Stage 4 — Buffer and submit

- Full draft complete by end of Sep 9.
- Sep 10: review pass against the judging criteria (Evidence / Creativity / Clarity / Feasibility / Thoroughness) and against the page's own litmus tests (Q1's "any three students" test, Q2's "changed something in your design" test).
- Submit with buffer before 11:59 PM IST — do not run interviews into the final hours.

## Update from the Household Service Memory Supplementary Note (PDF)

Three new interview probes worth adding to the Stage 1 method above, all justified by real gaps or findings in the note (full detail in `notes.md` §6a):

1. **"What did you do in the first few hours, before you even started trying to get it fixed?"** — the note explicitly flags that no existing Indian study measures same-day task substitution (as opposed to eventual repair-seeking). This is a genuinely original data point your own interviews could contribute — a real candidate for clearing Q2's "insight nobody else has" bar, not just a nice-to-have question.
2. For anyone who services proactively (not reactively): **"Did you know it would save you money, or were you just following a schedule/reminder?"** — tests the note's finding that economic awareness, not reminder tools, predicts preventive behaviour.
3. **"Do you think of appliance cleaning as part of any yearly ritual (e.g. Diwali)?"** — tests the festival-calendar-hook hypothesis (currently anecdotal/[A]-tier only).

**Implication for Stage 3 drafting**: the note's finding that immediate workarounds are a separate, already-functioning "resilience layer" (not a service memory) suggests the agent's value proposition should be framed around owning the *coordination that follows* the first few hours, not first-response/emergency triage — refine Q3's "how it knows it's done" and any urgency framing accordingly. Separately, the finding that reminder-only mechanisms are evidenced as the *weakest* of four known non-breakdown mechanisms reinforces (with actual data, not just intuition) the existing guardrail against building "an AMC reminder system" as the thesis.

**Flagged open item, high priority**: this PDF is explicitly a follow-up to a "main dossier" (its own Section 2.3 "workaround ladder," Section 3.1 "seasonal shock" trigger, Section 6 decision framework, and a 76% AC-servicing figure) that has not been shared in this session. Recommend obtaining that document **before** locking Q2 or Q9 — it may already contain more structured, validated research than this session has been able to reconstruct secondhand.

## Update from independent secondary research (task-substitution & service-tracking)

Full findings in `system_map.md` §6 / `notes.md` §6b. New interview probes worth adding to Stage 1:

1. **"Do you have any stickers on your machines with a handwritten next-service date, or a paper log book for warranties/services?"** — tests whether the physical-artifact system of record found in secondary research (a real, commercially standardised product) is actually present in respondents' homes, and whether they trust/use it.
2. **"How do you handle your vehicle's insurance/PUC renewal reminders — compare that to how (or whether) you get reminded about appliance servicing."** — directly tests the vehicles-vs-appliances comparative hypothesis (`system_map.md` §6.5). If respondents independently describe the vehicle side as "just handled" and the appliance side as "on me," that's a strong, specific, quotable version of the insight the competition wants.
3. **For any technician/AMC-provider interview**: "When a maintenance contract is close to renewal, what actually reminds you to call the customer, and how often does that step fail?" — tests the "vendor doesn't remember either" finding (§6.4) directly from the supply side; if confirmed, this measurably changes what Q2's insight should say (the failure isn't one-sided).
4. **For anyone with a branded RO unit (Kent/Livpure etc.)**: "Does your purifier's app ever tell you something's wrong before you notice it yourself?" — tests whether Kent's IoT auto-detect capability (§6.3) is actually experienced/trusted by real users, or is marketing more than lived reality.

**Implication for Q6 (customer asset)**: if the vehicles-vs-appliances structural read (§6.5) holds up in interviews — that vehicles work because RTO registration gives every party a shared anchor/identifier appliances lack — then the "customer asset" your agent asks for may not be data in the traditional sense (order history, contacts) but the *role of the missing anchor itself*: becoming the one place that holds a stable identifier per appliance across brands, the way an RTO number already does for a vehicle. Worth testing directly rather than assuming.

## Explicitly not part of this plan (per local context files' "what NOT to build" list, still valid)

Do not let the converged solution collapse into: an appliance reminder app, a digital warranty wallet, a technician marketplace, "Urban Company but with AI," a generic troubleshooting chatbot, a home-management dashboard, or a nearby-technician finder. These may be *features*, never the thesis.

## Open items / offers not yet taken up

- Claude offered to build a live interview-tracking sheet (so 2-3 people interviewing in parallel don't have to merge notes by hand) — not yet requested.
- Claude offered to draft the specific interview guide per lens (household vs technician vs landlord) — not yet requested.
- Whether to copy the `resource-scan` skill to another machine or package it as a plugin — not yet requested.
