# System Map — Keeping the Machines Running

## 0. Purpose of this document

This is the single reference for **what is known vs. hypothesized** about this problem space, synthesized from three sources: the two local context files (`Keeping_Machines_Running_Context.md`, `keeping_the_machines_running_context.md`), the raw team brainstorm (`01_group_braindump.md`), and the resource-scan test-drive (`context.md` Part 5). It replaces the need to re-read all four source documents to reconstruct the current state of understanding — read this first; go to the sources only for verbatim detail.

**Labeling convention used throughout:** every claim is tagged —
- **[CASE]** — stated in the competition's own case material (secondary evidence, real but not yours)
- **[LAW]** — an independently documented external fact (e.g. legal/market data found via resource-scan)
- **[TEAM]** — the team's own prior reasoning/brainstorm (braindump, context files)
- **[HYPOTHESIS]** — inference or pattern-matching done by Claude; not yet evidenced by anyone talking to a real person
- **[NEEDS INTERVIEW]** — explicitly unknown, flagged rather than invented

This mirrors the discipline already established earlier in the session (see `decisions.md` #6): nothing here should be mistaken for a finding until real interviews confirm it.

---

## 1. Problem space

### 1.1 Working thesis **[TEAM, from context files]**

> The household has become the integration layer for an industry that never integrated itself.

Every household asset creates a fragmented operational workflow: **invoice → warranty → diagnosis → service centre → technician → scheduling → parts → payment → follow-up → closure** — and the household is the only party that touches every step. A second framing, used interchangeably: **households behave like manual "dispatch desks."** **[CASE]** — the case material's own respondents used this phrase.

### 1.2 Stakeholders **[TEAM, from braindump]**

- Technicians (independent and OEM-affiliated)
- Homeowners / machine owners
- Service providers (named examples: Urban Company, Pronto)
- Store support (retailer-side)
- Warranty providers / OEMs
- Customer support (call centres, chatbots)
- Tenants
- Society/RWA management
- Enterprises (colleges, hospitals, restaurants, offices) — a distinct, larger-scale segment
- Companies that rent out equipment

### 1.3 Segments **[TEAM, from braindump — unscored]**

Geography: metro / tier 1 / tier 2 / tier 3. Demographic: age. **Not yet scored against each other** — the braindump explicitly notes these are dimensions to test, not conclusions ("just the 1st round of possibilities, need not be the full set"). **Correction, per `team_reconciliation.md` §6**: do not treat any claim that machines has the highest repetition rate among 18-24-year-olds as established — a teammate's independent audit found the one local file that stored such a score (`The_Ken_2026_Case_Selection_Playbook.html`) doesn't match the live competition chart, and its own source files were never in the workspace to verify.

### 1.4 Universal failure taxonomy **[TEAM, from context files]**

The context files break "what can fail" into 18 named categories, independent of which object/machine is involved: Discovery, Information, Handoff, Coordination, Commitment, Responsibility, Payment, Authorisation, Communication, Status, Verification, Recurrence, Scheduling, Escalation, Records, Trust, Incentives, Delegation.

This is the taxonomy the 17+1 candidate pain-threads in `notes.md` §2 are drawn from — every thread maps to one or more of these 18 failure types. Use this taxonomy as the checklist when a new incident surfaces in an interview: which of these 18 did it actually fail on?

### 1.5 Case-documented example workflows — the only real (if secondary) evidence available before interviews **[CASE]**

These six examples are named explicitly in the competition's own case material. They are the strongest evidence available *right now*, because real people said them to The Ken's team — but they are still secondary (you didn't collect them), so they inform the divergence map, they don't replace primary research.

| Example | Workflow / what happened | What it reveals |
|---|---|---|
| **RO/water purifier installation** | chatbot → service centre call → service agent call → OTPs → forms → installation | Fragmented handoffs; repeated explanation; context loss at each transfer; nobody owns the workflow end-to-end |
| **AC repair** | Became a multi-day tenant-vs-landlord responsibility dispute | Responsibility/authority failure, not a discovery failure — finding a technician was never the hard part |
| **Carpenter (kitchen trolley work)** | Needed → find carpenter → contact → explain → agree time → **wait** → no-show/delay → follow up → reschedule → completion | The physical task itself may be short; management + waiting time dominates. Worth separating *work time* / *management time* / *waiting time* in any incident log |
| **Plumber** | Repeatedly says "coming," requires multiple follow-up calls | The job isn't finding a plumber — it's enforcing a commitment someone already made |
| **Lift AMC** | Requires residents to chase for it to actually happen | Recurring/contractual obligation, diffuse ownership (no single resident personally accountable) |
| **Pest control** | Vendor calls to sell renewal | Incentive mismatch — vendor's goal (sell more service) and household's goal (pest-free home) diverge; household has no independent way to judge if renewal is actually needed |

Also directly quoted in the case: households connect *"appliance service, car service, and Amazon errands"* as **"many similar stuff"** requiring time and effort — i.e., respondents themselves generalize past appliances into a broader errand-coordination burden. And: the experience is described as **"solving the chase problem with hope."**

---

## 2. Solution space

### 2.1 What already exists, by category **[LAW, from resource-scan — full detail and links in `notes.md` §4 and `links.md`]**

| Category | Examples | What it solves | What it leaves unsolved |
|---|---|---|---|
| Field Service Management (FSM) software | ServiceTitan, Salesforce Field Service, Jobber; open-source: Beveren FSM, Resgrid | Dispatch, scheduling, technician coordination — **but for the business**, not the household | The household-side mirror of this exact software category doesn't exist |
| Home services marketplaces | Urban Company (India), Thumbtack, TaskRabbit | Discovery + booking + trust/vetting of a provider | Stops at booking — post-booking coordination (no-shows, parts, disputes, warranty routing) is still the household's problem |
| Voice AI for appliance repair | FieldCamp, ElevenLabs, Voiceflow, appliancerepairaiagent.com | Inbound call handling **for repair businesses** | Nothing found that places outbound, on-the-household's-behalf calling |
| Agentic payments infra | Pine Labs P3P + Grantex (the actual rail partner) | UPI settlement + delegated spend limits + identity + audit trail, revocable | Not appliance/household-specific — it's generic infrastructure your agent would sit on top of |
| Household asset/warranty tools | Warracker, HomeZada, GoCodes | Passive record storage of warranties/purchases | None of them *act* — no agent-side execution |
| PropTech tenant-maintenance | MicroRealEstate, Rentvine | Landlord-side property/tenant/maintenance record-keeping | Not India-specific; doesn't resolve the responsibility-ambiguity problem, just records requests |
| Gig/technician platforms | BigFix, GigPe | Real, reachable technician labor pool in India | Supply-side tooling only; no household-facing coordination layer |

### 2.2 The explicit whitespace **[HYPOTHESIS, built from 2.1 — needs interview confirmation]**

Nothing found sits on the **household's side, after booking, across multiple vendors**. The market is dense at both edges (enterprise FSM software; consumer discovery marketplaces) and empty in the middle — a household-facing operations layer that owns coordination *after* a request is placed, across whichever provider/OEM/AMC/landlord is actually involved.

### 2.3 What NOT to build **[TEAM, from context file — a settled guardrail, not up for re-litigation without new evidence]**

If the eventual solution collapses into any of these, treat it as too shallow: appliance reminder app · digital warranty wallet · technician marketplace · "Urban Company but with AI" · generic troubleshooting chatbot · home-management dashboard · nearby-technician finder · AMC reminder system · app that only stores bills/warranty dates · chatbot that just tells the user whom to call. Any of these may be a **feature** inside the real product; none should be the thesis.

### 2.4 Candidate agent shape **[TEAM, from context file — a working draft, not locked]**

Loop: **Observe → Decide → Act → Verify → Recover.** If a candidate design only observes and recommends, it isn't agentic enough for this competition's bar. Three rails (voice / payments+authorisation / logistics) each need a genuine bottleneck they solve — not decorative integration. See `plan.md` Stage 3 for how this maps onto the actual Q3-Q5 answers.

---

## 3. Per-object map: workflow, current workarounds, and downstream problems

*(See §5 below for real, named-source data on immediate workarounds and non-breakdown behaviour, added later from the Household Service Memory Supplementary Note — several `[HYPOTHESIS]` cells below turn out to be directionally right, and §5 has the sourced version.)*

This is the direct answer to "for each household issue, when a machine or chore gets stopped, map what these other problems are." Built from the braindump's own machine/errand list, clustered for scannability. **Almost none of the "current workaround" cells are evidenced yet** — they're reasoned, plausible guesses, explicitly marked, meant to be *checked* in interviews, not trusted as fact.

**Columns:** Object · Typical failure trigger · Case evidence (if any) · Plausible interim workaround **[HYPOTHESIS unless marked otherwise]** · Downstream/adjacent problems it tends to create · Relevant failure type(s) (§1.4) · Rail relevance (V=voice, P=payments, L=logistics)

### Cluster 1 — Small/personal electronics

| Object | Trigger | Case evidence | Plausible workaround | Downstream problems | Failure type(s) | Rails |
|---|---|---|---|---|---|---|
| Mobiles | Screen/battery/hardware fault | None | Use a second phone, or a family member's, until fixed | OEM vs local repair choice; data backup risk; warranty voidance if opened by non-authorised shop | Discovery, Trust, Warranty | V, P |
| Clocks | Stops working | None | Use phone as clock — likely trivial, low emotional stakes | Probably not a meaningful wedge object | — | — |
| Laptops | Hardware/software fault | None | Borrow, use phone/tablet instead, delay work | Data loss risk, work disruption if primary work device | Discovery, Trust | V, P, L (parts) |
| Electric toothbrush | Battery/motor fault | None | Revert to manual toothbrush | Low stakes, unlikely wedge | — | — |
| Bulbs/lights | Burns out / fixture fault | None | Self-replace bulb; call electrician only if fixture/wiring | Usually self-resolved — only escalates if wiring-level | Minor, self-resolving | — |

**Read on this cluster [HYPOTHESIS]:** most of these are low-stakes, self-serviceable, or short-cycle purchases — unlikely to be where the coordination burden concentrates. Flag as probably **not** the wedge unless interviews say otherwise.

### Cluster 2 — Major kitchen/home appliances

| Object | Trigger | Case evidence | Plausible workaround | Downstream problems | Failure type(s) | Rails |
|---|---|---|---|---|---|---|
| Geyser | No hot water | None | Cold showers, boil water | High urgency in winter; safety risk if gas-based | Urgency, Safety | V, P |
| Oven/microwave | Won't heat | None | Use stovetop, order food | Moderate disruption to daily routine | Discovery | V, P |
| Washing machine | Won't run/leaks | None | Handwash, laundromat, delay laundry | Recurring daily-life disruption; **[CASE]**-adjacent to "how to get the task done without the machine" framing from braindump's own workflow notes | Discovery, Recurrence | V, P, L (parts) |
| TV | Display/connectivity fault | None | Use phone/laptop for entertainment | Low urgency, high frequency of ownership | Discovery | V, P |
| Instapot/kitchen electric | Malfunctions | None | Revert to traditional cooking method | Low stakes | — | — |
| Dishwasher | Won't run | None | Handwash dishes | Low-moderate disruption; less common in India than other markets — likely lower incidence overall | Discovery | V, P |
| Refrigerator | Won't cool | None | Buy ice, eat out, risk food spoilage | **High urgency** — food-spoilage risk makes this time-sensitive in a way most other appliances aren't | Urgency, Discovery | V, P |
| AC | Won't cool | **[CASE]** — the case's own headline example; became a multi-day tenant/landlord dispute | Use fan, another room, or tolerate heat | Responsibility ambiguity is **[LAW]**-documented for AC specifically (Indian rent law leaves it a named grey zone — see §1.5 and `notes.md` §4) | Responsibility, Authority, Payment | V, P |
| Water purifier/motor | Leaking/stops filtering | **[CASE]** — the case's own RO installation example (see §1.5) | Buy bottled water temporarily; risk drinking unfiltered water | Multi-handoff installation/service process is CASE-documented | Handoff, Communication | V, P, L (parts) |

**Read on this cluster:** the two objects with actual case-level evidence (AC, water purifier) are also the two with the clearest failure-type signature (responsibility ambiguity; handoff/communication breakdown). Refrigerator stands out as the one **[HYPOTHESIS]**-only object with a plausible urgency signal (food spoilage) worth testing directly — nobody has said this to the case team yet, but it's a testable, sharp candidate.

### Cluster 3 — Home infrastructure & recurring services

| Object | Trigger | Case evidence | Plausible workaround | Downstream problems | Failure type(s) | Rails |
|---|---|---|---|---|---|---|
| Plumbing | Leak/blockage | **[CASE]** — the plumber example (see §1.5) | Use bucket/manual workaround; avoid using the fixture | Commitment enforcement is **[CASE]**-documented as the core failure here, not discovery | Commitment | V |
| Pest control | Infestation, or recurring contract | **[CASE]** — the pest-control example (see §1.5) | Tolerate, or use retail pest products | Incentive mismatch is **[CASE]**-documented (vendor sells renewal, not need) | Incentives, Recurrence | V, P |
| Gas connections | Supply issue/leak | None | Use induction/electric alternative if available; **safety-critical if leak** | Safety escalation — likely a "never fully autonomous" category | Safety, Escalation | V |
| Power (electrical) | Outage/wiring fault | None | Inverter/generator backup if available | Can cascade into other appliance failures (e.g. fridge spoilage risk compounds) | Safety, Urgency | V |
| DTH/Wifi/Landline | Connectivity loss | None | Mobile data hotspot as substitute | Moderate disruption, high frequency of ownership; recurring-service billing complexity | Recurrence, Records | V, P |
| Generator | Won't start | None | Rely on grid power / inverter | Enterprise/society-level more than individual household | Recurrence | V, P |
| Painter (house painting) | Scheduled/needed work | None | Delay indefinitely — likely highly postponable | Low urgency, project-based not "broken" — different job shape from repair | Scheduling | V, L |
| Welding | Needed repair/fabrication | None | Unclear — likely delayed or substituted with alternative fix | Low frequency; unclear if meaningful volume for a household wedge | — | — |
| Carpentry | **[CASE]** — the kitchen-trolley example (see §1.5) | Delay, or DIY temporary fix | Waiting/management time dominates over actual work time — **[CASE]**-documented | Commitment, Scheduling | V, L |

**Read on this cluster:** plumbing, pest control, and carpentry all have direct case evidence, and all three point at the **same underlying failure type** — commitment enforcement / incentive misalignment — rather than discovery. Gas and power stand out as the two objects where safety escalation, not coordination convenience, is the dominant concern — worth explicitly scoping out of "routine autonomous handling" in any agent design (ties to the guardrails already listed in the local context files).

### Cluster 4 — Vehicles

| Object | Trigger | Case evidence | Plausible workaround | Downstream problems | Failure type(s) | Rails |
|---|---|---|---|---|---|---|
| Car/vehicles | Service due / breakdown | **[CASE]** — named alongside appliance service and Amazon errands as "many similar stuff" (see §1.5) | Use cab/public transport/another vehicle temporarily | Service centre scheduling, parts, insurance claims can all stack together | Handoff, Records, Payment | V, P, L |

**Read:** vehicles are explicitly named by a real respondent as structurally similar to appliance service — worth treating as a serious adjacent-object candidate rather than assuming "machines" means only in-home appliances.

### Cluster 5 — Recurring financial/admin obligations (braindump-flagged, likely adjacent rather than core)

| Object | Trigger | Case evidence | Plausible workaround | Downstream problems | Failure type(s) | Rails |
|---|---|---|---|---|---|---|
| Insurance | Renewal/claim needed | None | Auto-renewal (often overpriced) or lapse coverage | Claims process is itself a multi-party coordination workflow | Records, Payment | P |
| Hospital bills/pharmacy recurrence | Recurring need | None | Manual reordering/repeat visits | Similar recurring-obligation shape to AMC | Recurrence, Records | P, L |
| Tax claims | Filing deadlines | None | Delay/rely on an accountant | Deadline-driven, high-consequence-if-missed | Escalation, Records | P |

**Read:** these are structurally similar (recurring, easy to postpone, coordination-heavy) but are **not physical repair** — different enough in kind that they're a plausible **annexation target (Q7)** rather than part of the initial wedge. See `r1.md` Q7.

---

---

## 4. Cross-cutting synthesis

**Where the evidence (case-level) and the resource-scan (market-level) agree:** AC, water purifier/RO, plumbing, carpentry, and pest control are the five objects with *any* real evidence at all — three of them (plumbing, pest control, carpentry) point at the same failure type (commitment enforcement / incentive misalignment), and two (AC, RO) point at responsibility ambiguity and handoff/communication breakdown respectively. That's a real, if secondary-evidence, signal: **the coordination pain concentrates in trades/services with a human back-and-forth (plumber, carpenter, pest control), not in appliance categories that are pure product-warranty transactions** (TV, oven, dishwasher) where the workflow is more linear.

**Where resource-scan adds a fact case evidence didn't have:** the AC/landlord-tenant ambiguity is not just a felt frustration — Indian rent law genuinely leaves it undefined (§1.5, `notes.md` §4). That's a rare case where secondary research turned a "hypothesis" into something closer to "documented fact," though it's still not a *customer* insight (per Q2's rule that the insight must come from a real person you talked to, not a legal document).

**What this map does NOT yet tell you:** which object/segment combination has the *strongest* pain, not just the most case-mentions. Refrigerator's urgency hypothesis, vehicles' cross-category framing, and the recurring-obligations cluster's annexation potential are all real candidates with **zero current evidence** — exactly the kind of thing the interview plan in `plan.md` is designed to surface or kill.

**How this feeds Phase 1:** this document is the input layer; `plan.md` Stage 2-3 is where interview evidence gets tested against it and an insight gets locked; `r1.md` is where resource-scan's specific Q-by-Q suggestions live. Update this file's "[HYPOTHESIS]"/"[NEEDS INTERVIEW]" tags to "[EVIDENCED]" as real interviews confirm or kill each row — that's the fastest way to see, at a glance, how much of this map is still speculative as the deadline approaches.

---

## 5. New section — Household Service Memory Supplementary Note (PDF): immediate workarounds & the non-breakdown segment

Source: `Household-Service-Memory-Supplementary-Note.pdf` (`/files/`), "prepared for Atharv," a follow-up to a **"main dossier" not otherwise present in this session** — see the open gap flagged in §5.4. Tag mapping used here to stay consistent with §0's convention: the PDF's **[D]** (published/named source) → **[LAW]**, its **[A]** (consumer-facing/commentary) → kept as **[A]** (weaker than [LAW], stronger than [HYPOTHESIS]), its **[H]** (author's own reasoning) → **[HYPOTHESIS]**.

### 5.1 Immediate workarounds — sourced version of §3's guesses **[HYPOTHESIS, per the note's own admission — no Indian study measures this]**

| Appliance | Immediate workaround (not a fix) |
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

**Comparison against §3's original guesses**: directionally aligned on refrigerator (ice/neighbour's fridge — §3 guessed this), washing machine (laundromat/handwash — §3 guessed this), AC (fan/other room — §3 guessed "another room," this note adds the specific "wet towel + cooler" and "mall/relative's place" detail), and water purifier (bottled water — §3 guessed this). New information §3 didn't have: the **local informal-service pattern** (dhobi, press-wallah, neighbour's connection) as a named, recurring category of workaround, not just "delay" or "substitute."

**The pattern this note draws out [HYPOTHESIS]**: nearly every workaround is either (a) a local informal service or (b) a cheaper, failure-tolerant substitute — neither registers as a "service memory." This is a resilience layer the household has already built independently of any app or agent.

**Design implication**: don't compete with this layer or try to be the first-hours fix. The agent's value is in owning the *coordination that follows*, on a timeline the household can tolerate precisely because the workaround is already holding the gap.

### 5.2 The non-breakdown segment — four real mechanisms, not "personal memory"

The note traces a commonly-cited "70%" AC-servicing figure to CEEW's 2023 survey of 369 RAC *technicians* — supply-side (about customer calling patterns), meaning the other 30% is genuinely unexplained by that source. Four separate, real mechanisms found instead:

- **(a) Maintenance contracts [LAW]** — LocalCircles, April 2026 (27,000+ responses, 289 districts): 7% brand AMC, 17% brand ad hoc, 13% dealer, 44% local provider, 13% organised third-party, 3% "working fine." The 7% on contract don't remember anything — the AMC's renewal cycle does it for them. *Caveat in the source*: a different survey wave than a 76%-figure apparently cited in the unseen main dossier — don't treat as the same measurement.
- **(b) Economic awareness beats reminders [LAW]** — an RCT on Indian AC owners (India Cooling Action Plan research; PubMed PMID 33458437) found awareness campaigns raised general awareness but not technical know-how, while understanding the *economic* benefit (lower electricity bills) predicted actual preventive servicing.
- **(c) Seasonal norm, formalised [LAW]** — the same CEEW report recommends preventive servicing twice a year (pre/post AC season) as an industry-recommended cadence.
- **(d) Diwali/festival deep-cleaning [A]** — an existing, unowned cultural calendar hook (fridges/microwaves/stoves explicitly called out for pre-festival cleaning in consumer content); anecdotal, not a stat, but a date the product wouldn't need to manufacture.

### 5.3 What this changes about the map

1. **Reinforces §2.3's "don't build a reminder app" guardrail with actual data**: of the four known non-breakdown mechanisms, reminder-style memory isn't even one of them — vendor contracts, economic incentive, and cultural/seasonal calendars all outperform "personal memory" in explaining who avoids waiting for a breakdown. A pure reminder app is evidenced as the weakest plausible mechanism, not just intuitively thin.
2. **Sharpens the Solution Space (§2.4) business-model thinking**: an agent riding an *existing billing relationship* (AMC, builder/RWA handover, utility partner) is closer to a mechanism that's already proven to work than one that relies on the household initiating and remembering. Relevant to Q7/Q9 — see `r1.md` addendum.
3. **Refines urgency framing for Cluster 2 objects (§3)**: since a resilience workaround is already firmly in place within hours for most appliances (per §5.1), the agent doesn't need to compete on speed-to-fix — its differentiation is coordination quality and certainty over the following days, not emergency response.
4. **Adds a testable trigger set beyond "breakdown"**: seasonal norms (twice-yearly) and cultural calendar events (Diwali) are pre-existing hooks the agent could ride rather than invent — worth testing directly in interviews (see `plan.md`'s three new probes).

### 5.4 Open gap — the "main dossier" this note follows up on

This supplementary note repeatedly references material this session has not seen: a "workaround ladder" (its Section 2.3), a "seasonal shock" trigger (its Section 3.1), a business-model "decision framework" (its Section 6), and a 76% AC-servicing figure attributed to a 2022 survey. **None of this has been shared in this session.** Treat everything in §5.1-5.3 above as correct on its own terms but incomplete relative to whatever that main dossier already establishes — recommend obtaining it before finalizing Q2 or Q9 (see `decisions.md` #21, `plan.md`, `progress.md`).

---

## 6. Independent secondary research — task-substitution theory & service-tracking mechanisms

Done on explicit instruction to self-inform via papers/articles/blogs/market reports/open-source examples, in parallel with (not instead of) the planned interviews. Full source list in `links.md`. Two questions this section answers: **(1)** when a machine breaks, how do people get the underlying *job* done another way, and is there existing research on this beyond the household-specific table in §5.1; **(2)** what mechanisms — outside personal memory — currently exist for households to track when a service is due, and how do they compare across categories.

### 6.1 Task substitution — the academic grounding behind §5.1's table

Three separate bodies of research describe what §5.1 catalogued anecdotally:
- **Compensatory consumption theory [LAW]** — the formal marketing/consumer-research term for using a substitute product or service to fill a functional gap left by an unavailable one; research shows people with fewer resources growing up are *more* likely to devalue a substitute once they learn the original is unavailable — i.e., substitution isn't emotionally neutral, it can carry a felt loss even when functionally adequate.
- **Bricolage / "making do" [LAW]** — the academic term (from anthropology, now used in consumer and entrepreneurship research) for resourcefully recombining whatever is at hand rather than acquiring the "correct" input. Recent work frames it as a *mindset of resourcefulness*, not just scarcity — relevant framing if the product's job is partly to preserve, not replace, a household's own resourcefulness.
- **Jugaad — India-specific and directly on-topic [LAW]** — a large, India-focused literature (frugal innovation research; the book *Jugaad Innovation* by Radjou, Prabhu & Ahuja) with concrete household examples: charging a phone from a bulb socket, an old bicycle wheel repurposed as a fan, a pressure cooker used as a steriliser. This is the *exact same word* your own braindump already used ("Do jugaad if not understood or if delayed") — worth citing directly in Q1/Q2, since it grounds your team's own vocabulary in an actual research tradition rather than slang, and signals cultural fluency to judges.
- **India-specific utility-outage data [LAW]** — Statista (2022): 41% of Indian households use an inverter as their primary power-outage coping strategy; 33% reported facing no outages; only 2% had no backup at all. A concrete, citable number for one category's workaround rate — worth checking whether an equivalent number exists (or can be generated from your own interviews) for appliance/service breakdowns specifically, since none currently does (per §5.1's own admission).

### 6.2 Repair vs. replace — India-specific market data (existing global stats were US-only; searched separately)

- **[LAW]** India's appliance repair sector is described as one of the fastest-growing repair markets globally, with rising penetration in tier-2/3 cities and a shift from an informal, technician-led ecosystem toward organised, tech-enabled service networks.
- **[LAW]** Average appliance repair costs have risen roughly 25% over the past five years in India; nearly one-third of devices now require specialised (not general-handyman) intervention.
- **[LAW]** EMI/BNPL financing is specifically named as a driver pushing Indian consumers toward *replacement* over repair — a real, structural incentive worth weighing against your product's implicit assumption that people want repair-coordination help (if EMI-driven replacement is rising, the addressable "repair coordination" moment may be shrinking for some segments/appliances — worth a direct interview question).
- **[LAW, but US-sourced — not yet confirmed for India]** Consumer Reports: 58% of US consumers replace (rather than repair) a large appliance, 87% replace small appliances; the "50% rule" (repair only if cost is under 50% of replacement) is the standard heuristic; refrigerators are the single most-repaired-or-replaced appliance category (~54% of respondents' most recent incident). Flagging clearly: **no India-specific version of this exact repair/replace ratio was found** — treat the US figures as a hypothesis to test, not a fact to cite for India.

### 6.3 Service-tracking mechanisms — what already exists, compared across categories

This is the most useful comparative finding of this research pass: **India's reminder infrastructure is wildly uneven across categories that are structurally similar** (a recurring, easy-to-forget household obligation with a hard consequence if missed).

| Category | What currently reminds the household | How mature/institutional is it |
|---|---|---|
| **Vehicle (PUC / insurance / fitness / road tax)** | Official government SMS-alert programs (e.g. Punjab Transport Dept, coordinated with IRDAI, PUC centres, and NHAI); the official **mParivahan** app reminds before insurance/PUC/fitness/road-tax expiry; multiple third-party apps (PitSync, CarInfo, Agenex) send automated WhatsApp reminders in 10 Indian languages | **High** — multi-institution government coordination plus a competitive private app layer on top |
| **LPG/gas cylinder refill** | WhatsApp keyword booking, missed-call booking, IVRS, apps — across Indane/HP/Bharat Gas | **Medium for booking, ~zero for reminding** — booking is frictionless once you decide to act, but no source found describing a *proactive* "you're probably running low" nudge; it's a pull system, not a push one |
| **RO/water purifier (branded)** | Livpure and Kent both have dedicated service apps (view service history, log requests); **Kent's IoT-enabled "SUPREME" line auto-detects a fault and auto-registers a service call** | **Medium, but brand-siloed** — the most "agentic" thing found in this whole research pass (auto-detect + auto-register) already exists, just scoped to one brand's premium product line, not across a household's mixed-brand appliance set |
| **AC / general appliance AMC (industry-wide, not consumer-facing)** | On the **vendor's own side**: renewal dates are commonly tracked in Excel, with reminder calls made "from memory" — industry commentary states IT/CCTV/AC service companies lose **20-30% of AMC renewals simply because nobody remembered to call in time** | **Low, and the failure is on the supply side, not just the household** — see §6.4, this is a significant finding |
| **General appliance service (unbranded/local technician)** | A physical sticker, applied by the technician at the last visit, handwritten with the next service date — a real, commercially standardised product (printable sticker sheets exist for this exact purpose); separately, paper "service log books" are sold on Amazon for consumers to self-track warranty/serial/service data by hand | **Lowest** — the household's own system of record is a sticker on the machine or a notebook, if it exists at all |

### 6.4 The sharpest new finding: the vendor doesn't remember either

**[LAW, high-confidence]** — Industry commentary on Indian AMC/service businesses states plainly that renewal tracking is done in Excel with reminder calls "made (or not made) from memory," and that this causes IT/CCTV/AC service companies to lose 20-30% of AMC renewals to simple forgetting.

This reframes a piece of the problem: the "household forgets" framing (the case's own framing, and this project's working thesis) assumes the **vendor's system is the reliable half** and the household is the weak link. This data suggests the opposite may sometimes be true — **the vendor's own reminder system is just as informal (Excel + memory) as the household's.** If real interviews confirm this from the supply side, it changes Q2's candidate insight meaningfully: the coordination failure isn't one-sided, and an agent that only fixes the household's memory problem while the vendor's Excel sheet still silently drops the renewal wouldn't actually solve the incident. Worth a direct supply-side interview question: *"When a maintenance contract is close to renewal, what actually reminds you to call the customer — and how often does that step fail?"*

### 6.5 The sharpest comparative angle: vehicles vs. appliances

**[HYPOTHESIS, built from §6.3's real data — needs interview confirmation]**: India has already fully solved this exact class of problem — a recurring, easy-to-forget, consequence-bearing household obligation — for one category (vehicles), via multi-institution government coordination (transport department + insurer + PUC centre) plus a competitive private-app layer. Nothing equivalent exists for appliances or home services, despite the underlying shape of the problem (recurring obligation, diffuse ownership, real consequence for missing it — safety for gas/electrical, cost for AC efficiency, health for RO) being structurally the same.

This is a genuinely strong candidate for Q9 framing: rather than asking "why hasn't an appliance company built this," the sharper question may be **"why hasn't the mechanism that already works for vehicles (institutional coordination + third-party reminder layer) been extended to appliances?"** — and a testable hypothesis for why not: vehicles have a single national numbering/registration authority (RTO) that every insurer/PUC-centre/reminder-app can hook into; appliances have no equivalent shared identifier across brands, so no single party has the natural "anchor" data the way RTO registration numbers anchor the vehicle ecosystem. If true, this also directly informs **Q6** (the customer asset you ask for) — your agent may need to become the *de facto* shared identifier/anchor across a household's appliances that no institution currently provides, the way RTO registration already does for vehicles.

### 6.6 What was searched but came back thin — flagged rather than padded

- India-specific repair-vs-replace ratios (the "50% rule" equivalent for India) — not found; US data only (§6.2).
- A direct India study on first-hours task substitution during an appliance breakdown — confirmed, per the PDF in §5, that none exists; this research pass didn't find one either, independently.
- HCI/academic research specifically on *appliance service reminders* (as opposed to general family-calendar coordination, §6.7) — not found as a distinct literature; family-calendar research is the closest adjacent field.

### 6.7 Adjacent, well-established research worth citing directly

- **"Life Admin" (Elizabeth Emens) [LAW]** — a book grounded in empirical interviews/focus groups with 100+ people, defining "life admin" as the secretarial/managerial work of running a household. This is the academic term for exactly what the working thesis (`context.md` Part 1, `system_map.md` §1.1) calls the household's "dispatch desk" role — worth citing by name in Q1/Q2 to show the team's framing sits inside a real research tradition, not just an internal metaphor.
- **Family-calendar HCI research [LAW]** — multiple recent papers (e.g. "Double Incomes, Single Calendar," "FamilyCanvas," "The Calendar is Crucial") document that shared household coordination tools consistently under-serve real family dynamics, and that coordination labor is frequently concentrated on one family member (a typology of "Monocentric/Pericentric/Polycentric" family calendar involvement is used in this literature). This independently corroborates thread #17 in `notes.md` §2 ("the household member who owns this work never chose the role") with real academic research, not just this project's own inference — still needs your own interview confirmation, but it's no longer an unsupported hypothesis in the literature sense.

### 6.8 What this changes about the map, in one line

The problem isn't unsolved because it's unsolvable — India has already built and normalised a working version of this exact reminder/coordination infrastructure for one adjacent category (vehicles). The open question your interviews need to answer is whether appliances/home-services lack it for a structural reason (no shared identifier/anchor, per §6.5) or simply because nobody's tried — those imply very different products.
