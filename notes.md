# Notes — The Ken Case Competition 2026 ("Keeping the machines running")

Reference notes organized by topic, not by conversation order (see `context.md` for the chronological transcript). Pulls together every fact, quote, and hypothesis surfaced this session.

---

## 1. Phase 1 (Solution Assembly) — key facts to keep in view

- Deadline: **Sep 10, 2026, 11:59 PM IST**. Registration closes Sep 8.
- It's a 10-question form with hard word/format limits — not a deck, not a report.
- Q2 (the one customer insight) is explicitly the one judges "read first."
- Judging is on **Evidence, Creativity, Clarity, Feasibility, Thoroughness** — and the page explicitly warns Creativity is "usually where AI-generated solutions fail."
- Quotes from interviews get published as age-band + city, never a name — plan interview consent language accordingly.
- One opening per team; switching resets evidence — so don't switch off "Keeping the machines running" casually.
- Full Q-by-Q text is in `context.md` Part 1.3 (verbatim from the live page).

## 2. The 17 candidate pain-threads (the divergence map)

Status: **none of these are confirmed** — per explicit user instruction, they are candidates to test against real interviews, not conclusions. Grouped by mechanism:

**Discovery & trust**
1. People don't lack technicians — they lack a way to know *which* route (OEM/local/marketplace) is trustworthy before committing.
2. Trust is single-use — a good experience with one technician doesn't transfer to the next incident; the search restarts from zero.

**Handoff & context loss**
3. Every handoff (chatbot → call centre → agent → technician) forces the user to re-explain the same problem from scratch.
4. A ticket that shows "open" has no real relationship to whether the physical job actually happened (ticket-reality gap).

**Commitment enforcement**
5. A verbal "yes, coming" has zero enforcement mechanism — the only lever a household has is repeated calling.
6. No-shows have no cost to the provider, so reliability has no built-in reason to improve.

**Responsibility & authority**
7. Tenant/landlord disputes stall not on *finding* a technician but on *who decides* — and there's no clear default. (Note: this is not just a hypothesis — see §4 below, Indian rent law explicitly leaves AC servicing as an undefined grey zone.)
8. Society/RWA-owned assets (lifts, generators) fail because "resident" is a diffuse, unaccountable owner.
9. Multi-person households don't have a clear handoff protocol when the usual "operator" is unavailable.

**Money & authorization**
10. Households don't distrust the price itself — they distrust the *quote-to-final-bill gap*, because nothing independently checks it.
11. Payment happens before verification is possible, so disputes always land after the money has already moved.

**Information & memory**
12. Warranty/AMC status isn't stored anywhere trusted — it's reconstructed from memory or a WhatsApp search each time.
13. The technician arrives with less context than the household already gave the call centre 20 minutes earlier — information dies at each handoff.

**Recurring obligations & incentive misalignment**
14. Recurring-service vendors (pest control, RO, AMC) are incentivized to sell renewal, not to signal "you don't need service yet" — the household can't distinguish real need from upsell.
15. "Was this actually necessary?" is unanswerable without independent history — the same vendor decides both diagnosis and revenue.

**Emotional/psychological**
16. The dominant feeling isn't anger at the technician — it's low-grade dread of *initiating* the process at all (why things get postponed).
17. The household member who owns this work never chose the role — it defaulted to whoever was home/available.

**Service-network structure** *(added after `narrowed_problem.md`'s recruitment planning surfaced real, personal access to this exact contrast)*
18. Large, professionally-managed residential communities (e.g. My Home in Hyderabad) may partially solve thread #8's accountability-diffusion problem via an internal approved-vendor system — while independent households and informally-managed buildings inherit the full diffusion problem with none of the professional-management fix. **Two possible real findings, both valuable**: managed communities are genuinely smoother (then the insight is *what specifically* their system does that an individual household's agent should replicate), or they have their own, different friction (then "managed doesn't mean solved" is itself a sharp, counterintuitive finding). See `narrowed_problem.md` §4 Decision 2 for the full reasoning and the confirmed interview plan testing this directly.
19. **Metro vs. tier-3 market maturity** *(added once real access to Eluru, a tier-3 AP city, was confirmed alongside Hyderabad)*: app-mediated service coverage (Urban Company, Housejoy) is still expanding *into* tier-2/3 cities per existing market research (`system_map.md` §2.1) — meaning the coordination pain in a place like Eluru may be sharper and less app-mediated than in Hyderabad, or may look completely different (e.g. smaller-scale, more relationship-based technician trust). **Confounded with thread #18** in the current sample (Hyderabad access = metro+managed; Eluru access = tier-3+presumably-independent) — see `narrowed_problem.md` §4 Decision 3 for the full reasoning and how the IIITH campus interview helps triangulate which variable is actually driving any observed difference.

**Extended unavailability** *(added from National Consumer Helpline government data, `system_map.md` §7.1)*
20. Appliances are sometimes kept "for testing" for weeks with no resolution timeline communicated — a distinct failure mode from a single missed appointment (threads #5-6) or a quote dispute (thread #10). This is one of six recurring complaint buckets in official, Parliament-tabled national consumer-complaint data specifically for household appliance servicing — meaning it's a documented pattern at national scale, not a hypothesis. Worth a direct probe: *"Was there ever a point where the appliance/technician was gone and you had no idea when it would be resolved?"*

**A sharper, 18th candidate that emerged later (from the resource-scan test-drive, see §5):**
18. India already has a cultural precedent of delegating physical-world tasks to trusted human intermediaries (a building's go-to electrician, a family's regular repair contact, a domestic helper who "handles" this). The real design question may not be "will households delegate to an agent" but "who does this household already informally delegate this exact job to, and what would it take to trust software in that specific role instead?"

Threads 6, 8, 14, 15 are specifically flagged as *incentive/accountability* problems (needing an advocate/auditor agent) rather than pure *effort* problems (needing a dispatcher agent) — worth keeping this distinction alive when scoring interview evidence, since it implies two different product shapes.

## 3. Interview method reminders (already in the local context files, restated for quick use)

- Never open with "would you use an AI agent / would you pay for X" — leads the witness.
- Start with: "tell me about the last time this happened," then "the one before that."
- The single highest-leverage question across every workflow: **"Who owns making sure this actually gets done?"** followed by **"If you don't follow up, what happens?"**
- Ask to see evidence where comfortable: WhatsApp threads, call logs, service tickets, invoices, warranty cards, screenshots.
- Vary the object/errand across interviews — don't let every conversation default to AC/RO just because those are the case's headline examples.

## 4. Grounded facts (not hypotheses) found via resource-scan

- **India's home services market**: ₹5.1 lakh crore (~$60B) FY25, growing toward ~$100B by FY2030; only 10-15% digitised. Urban Company: 20-22% commission typical, turned profitable FY25, IPO'd, operates 50+ Indian cities.
- **Field Service Management (the enterprise version of this same coordination problem)** is a $6.7B → $13.8B (by 2033) global market (ServiceTitan, Salesforce Field Service, Jobber, etc.) — proof the coordination/dispatch problem is real and monetizable, just not yet solved from the household's side.
- **Indian tenant/landlord repair law**: landlord is responsible for structure/walls/roof/major fixture failure from normal use; tenant is responsible for day-to-day upkeep and minor repairs (bulbs, taps, fuses). **AC servicing is explicitly documented as the most common grey-zone item with no agreed clause** — matches the case's own AC example exactly; this is documented legal ambiguity, not just a felt frustration.
- **Pine Labs P3P + Grantex** (the actual payments/authorisation rail partner): P3P handles UPI settlement for agent-initiated payments (no per-transaction MPIN after one upfront authorisation); Grantex is the separate layer handling identity verification, delegated spend limits, and audit trail, revocable anytime by the consumer. This is close to production-ready for the "₹1,500 auto-approve, ₹7,800 pause-and-ask" delegated-authority concept in the local context files.
- **Gnani.ai** (the actual voice rail partner): processes 30M+ voice interactions daily, 12+ Indian languages, 200+ enterprise customers, just launched Inya VoiceOS (5B-parameter voice-to-voice foundational model under the India AI Mission) — genuinely production-grade voice infra already exists; the gap is specifically in *outbound, on-behalf-of-a-consumer* calling that navigates someone else's IVR, not in voice quality itself.
- Nearly all existing "AI + appliance repair" products found (FieldCamp, ElevenLabs, Voiceflow, appliancerepairaiagent.com, Ciela AI) sit on the **repair business's** side (answering calls, dispatching their own technicians) — none sit on the household's side coordinating across multiple providers. This is the clearest documented whitespace.

## 5. The competition's own founding thesis (from "The Great Rewiring" column) — why this matters for Q1/Q2

Core debate the column surfaces: why hasn't consumer AI-agent adoption taken off despite the tech being ready?
- **Sidu Ponnappa** (Realfast): agents promise productivity but demand real setup effort — "products that demand increased cognitive load rarely take off in the mainstream."
- **Paras Chopra** (Lossfunk): delegation to another entity is a *learned skill*; using an AI agent is like managing a junior employee — most people aren't equipped for that, and for most personal-life tasks the benefit doesn't outweigh the cost.
- **Jamie/Levie's argument** (as cited): the payoff from an agent only arrives once you re-engineer an entire workflow around it, which takes years — this is why enterprises capture the value first, and why consumers will mostly meet agents *wrapped invisibly inside end-to-end services*, not as a standalone assistant they manage.

The column's counter-argument for why **India specifically** is different, and may go first: voice is a natural interaction mode here, payments are already digitised/seamless (UPI), e-commerce has diffused broadly, **and — most distinctively — India already has a widespread cultural practice of delegating physical-world tasks to human intermediaries** (train-ticket agents, delivery runners, informal money-management helpers) that no other market has at this scale. Paras Chopra's "delegation is a learned skill" barrier may already be culturally crossed in India, just not yet with software.

**Practical implication flagged for interviews**: ask directly whether the household already has an informal *human* "agent" for this exact appliance/service job (a go-to electrician, a building's regular technician, a relative who handles this) — and if so, what would make them trust software in that same role. This reframes the insight-hunt away from generic "coordination is annoying" toward something the competition's own thesis explicitly rewards.

## 6. The Ken's own prior-year output — tone/precision reference

2025's competition ("Disrupt the Incumbents") was structured differently (pick an incumbent to disrupt, not an opening) but the *quality bar* transfers. Winner: IIM Ahmedabad's "A Team," disrupting Narayana Health — one-line strategy: *"We turn expensive hospital bed-days into data-rich, AI-orchestrated home days, all packaged within a single, guaranteed-price treatment episode."* Structurally: an unowned, manual, post-event coordination workflow creating "massive value leakage" — the same shape as the appliance-repair coordination problem, just in healthcare. Full list of 10 finalists and their one-line strategies preserved in `/files/ken_case_competition_2025_winning_submissions.txt` — useful for calibrating how specific and numbers-driven a winning one-liner should be.

## 6a. Household Service Memory Supplementary Note (PDF) — grounded facts

Source: `Household-Service-Memory-Supplementary-Note.pdf`, "prepared for Atharv," a follow-up to a "main dossier" not otherwise present in this session (see `decisions.md` #21 and `plan.md` for the flagged gap). Uses its own tags: **[D]** published/named source, **[A]** consumer-facing/commentary, **[H]** author's own reasoning.

**Immediate workarounds [H]** — no Indian study exists measuring first-hours task substitution (as distinct from eventual repair-seeking), so this whole table is reasoning to validate, not evidence:

| Appliance | Immediate workaround |
|---|---|
| Washing machine | Hand-wash; local dhobi/press-wallah; coin laundromat |
| Refrigerator | Ice/cooler box; neighbour's fridge; smaller/more frequent grocery trips |
| Gas stove (one burner) | Shift to working burner; induction plate/electric kettle |
| Microwave/oven | Stovetop/pressure cooker instead |
| Geyser | Boiled water in a bucket, or cold shower |
| Air conditioner | Fan + wet towel/cooler; mall/relative's place during peak hours |
| RO/water purifier | Boil tap water; canned/bottled water short-term |
| Water pump/motor | Tanker water; manual fetch from neighbour's connection |
| Mixer/grinder | Hand-grind (sil-batta); pre-ground masala |
| Chimney/exhaust fan | Cook with windows open; standing fan |
| Iron | Local pressing shop |
| Two-wheeler/car | Auto/cab/public transport; borrow a neighbour's vehicle |

**The pattern this note draws out [H]**: nearly every workaround is either (a) a local informal service (dhobi, pressing shop, neighbour) or (b) a cheaper, failure-tolerant substitute. Neither registers as a "service memory" — it's a resilience layer the household has already built on its own. **Design implication**: the product likely shouldn't try to be the first-hours fix; its value is in owning the *coordination that follows*, on a timeline the household can already tolerate because the workaround is holding.

**The non-breakdown segment — four real mechanisms, not "personal memory"**: the note traces a commonly-cited "70%" AC-servicing figure to CEEW's 2023 survey of 369 RAC *technicians* (supply-side, about customer calling patterns) — meaning the other 30% is genuinely unexplained by that source. Separately found:
- **(a) Maintenance contracts [D]** — LocalCircles, April 2026 (27,000+ responses, 289 districts): 7% brand AMC, 17% brand ad hoc, 13% dealer, 44% local provider, 13% organised third-party, 3% "working fine." The 7% on contract don't remember anything — the AMC's own renewal cycle does it. *Caveat in the source note*: a different survey wave than a 76%-figure survey apparently cited elsewhere (in the unseen main dossier) — don't treat these as the same measurement.
- **(b) Economic awareness beats reminders [D]** — an RCT on Indian AC owners (India Cooling Action Plan research; PMID 33458437) found awareness campaigns raised general awareness but not technical know-how, while understanding the *economic* benefit (lower electricity bills) predicted actual preventive servicing. Self-initiators act because they know the money math, not because they were reminded.
- **(c) Seasonal norm, formalised [D]** — the same CEEW report recommends preventive servicing twice a year (pre/post AC season) — an industry-recommended cadence, not just a felt "seasonal shock."
- **(d) Diwali/festival deep-cleaning [A]** — an existing, unowned cultural calendar hook (fridges/microwaves/stoves explicitly called out for pre-festival cleaning in consumer content) — anecdotal, not a stat, but a date the product wouldn't need to manufacture.

**Bottom line [H, from the source note]**: no single mechanism is "personal memory alone" — three real alternatives already work in the market (vendor contract, economic awareness, calendar/cultural hook). The note argues this favors a business-model direction built on an **existing billing relationship** (builder/RWA handover, AMC, utility partner) over a **pure reminder app** — which this evidence suggests is the weakest of the four known mechanisms on its own. This directly reinforces the "what NOT to build" guardrail already in `system_map.md` §2.3, now with actual data behind it rather than just prior team intuition.

**Open gap**: the note repeatedly references a "main dossier" (its own Section 2.3 "workaround ladder," Section 3.1 "seasonal shock" trigger, Section 6 decision framework, and a 76% figure) that has not been shared in this session. Treat everything above as correct on its own terms, but incomplete relative to whatever that main dossier already contains.

## 6b. Independent secondary research — task-substitution & service-tracking mechanisms

Done on explicit instruction to self-inform via papers/articles/blogs/market reports, in parallel with (not instead of) planned interviews. Full detail and reasoning in `system_map.md` §6; sources in `links.md`. Condensed here for quick reference.

**Task substitution has real academic grounding**: compensatory consumption theory (substituting a product to fill a functional gap — not emotionally neutral, can carry felt loss even when functionally adequate), bricolage/"making do" (resourcefulness, not just scarcity), and — directly on-topic — the India-specific **jugaad** literature, which is the exact word your own braindump already used. Concrete jugaad examples from the literature: charging a phone via a bulb socket, an old bicycle wheel repurposed as a fan, a pressure cooker used as a steriliser.

**India repair-vs-replace**: repair costs up ~25% over 5 years, ~1/3 of devices now need specialised (not general handyman) intervention, EMI/BNPL is pushing consumers toward replacement over repair. **No India-specific "50% rule" or repair/replace ratio was found** — the US figures (58% replace large appliances, 87% replace small ones) are not confirmed for India; flag as untested.

**Service-tracking mechanisms compared across categories — the standout finding**: India's reminder infrastructure is wildly uneven across structurally similar recurring-obligation categories.
- **Vehicles**: government-coordinated (Punjab Transport Dept + IRDAI + PUC centres + NHAI), official mParivahan app, competitive third-party WhatsApp-reminder apps in 10 languages — the most mature, institutional reminder ecosystem found in this entire research pass.
- **LPG/gas**: frictionless multi-channel *booking* (WhatsApp/missed-call/IVRS/app) but no proactive "you're probably low" reminder found — a pull system, not a push one.
- **Branded RO (Kent/Livpure)**: real service apps exist; Kent's IoT "SUPREME" line already auto-detects a fault and auto-registers a service call — the single most "agentic" existing capability found, but brand-siloed, not cross-appliance.
- **AMC industry (vendor side)**: renewal dates tracked in Excel, reminder calls made "from memory" — industry commentary states this causes **20-30% of AMC renewals to be lost simply because nobody remembered to call in time.**
- **General/local-technician appliance service**: a handwritten sticker (a real, commercially standardised product) applied by the technician noting the next service date, or a paper log book — the household's actual system of record, where one exists at all.

**Sharpest new finding — the vendor doesn't remember either [LAW]**: this flips a piece of the working thesis. The assumption so far has been that the household is the unreliable half of the relationship and the vendor's system is fine. Industry data on Indian AMC businesses says the opposite may often be true — the vendor's own tracking is just as informal. **New interview probe**: ask supply-side respondents directly what actually reminds them to call a customer before renewal, and how often that step fails.

**Sharpest comparative angle — vehicles vs. appliances [HYPOTHESIS, needs interview confirmation]**: India has already fully solved this exact class of problem for vehicles via a shared institutional anchor (RTO registration numbers), which every insurer/PUC-centre/reminder-app can hook into. Appliances have no equivalent shared identifier across brands — which may be *why* no appliance-wide reminder layer has emerged, structurally, not just because nobody's tried. This is a strong candidate reframe for Q9 (`r1.md` addendum) and directly informs Q6 (the agent may need to *become* the missing shared identifier/anchor, the way RTO numbers already are for vehicles).

**Adjacent research worth citing directly**: "Life Admin" (Elizabeth Emens) — the academic term for the household's "dispatch desk" role, grounded in 100+ empirical interviews. Family-calendar HCI research (e.g. "Double Incomes, Single Calendar," "FamilyCanvas") independently corroborates thread #17 in §2 above (one household member absorbs the coordination role) — this is now backed by real academic literature, not just this project's own inference, though it still needs your own interview confirmation.

**What was searched but came back thin, flagged rather than padded**: an India-specific repair/replace ratio; a direct India study on first-hours task substitution (confirmed absent, independently, by two separate research passes now — this project's own interviews may be the first to actually measure it); dedicated appliance-service-reminder HCI literature as a distinct field (family-calendar research is the closest adjacent body of work).

## 7. The `resource-scan` skill — design notes

Saved at `~/.claude/skills/resource-scan/SKILL.md` (user-level, this machine, all Claude Code projects — not account-cloud-synced; full text in `/files/resource-scan_SKILL.md`). Four-step process it encodes:
1. **Diverge before searching** — build an explicit system map (topic + adjacent domains + upstream + downstream + stakeholders + alternate framings) before running a single query, calibrated to topic breadth.
2. **Search per axis, across categories** — repos, blogs/articles, news, books, other (papers/talks/podcasts/standards/communities) — for every axis, not just the literal topic.
3. **Guardrails** — never fabricate a URL; dedupe; annotate why each resource matters instead of bare-listing; flag recency/authority; don't silently drop a thin axis without first broadening the query.
4. **Output** — system map, then per-axis categorized resources, then 2-3 sentences of strategist-level synthesis; an Artifact only offered (not defaulted to) if the pull is big enough to warrant a browsable page.

Test-drive result (see `context.md` Part 5 for full output): the process worked as designed on a real, broad, ambiguous topic — it surfaced two genuinely high-value finds a plain "search the topic" approach likely would have missed: the FSM-market-as-inverse-mirror framing, and the competition's own founding thesis column (via a targeted "Ken case competition" search axis added specifically because the topic was *about* a case competition, not just about appliances).
