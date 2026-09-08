# Narrowing the Problem Statement — Phase 1 / Round 1 (Solution Assembly)

**Purpose of this file**: converge from "Keeping the machines running" (opening #02, broad) to one specific, defensible, interview-ready problem statement — a specific object × specific segment × specific geography/context × specific mechanism — chosen because it has the highest realistic potential to win Round 1, not because it's the first idea that came up. Built from `best_practices.md`, `system_map.md`, `notes.md`, `links.md`, `decisions.md`, `plan.md`, `r1.md`, `team_reconciliation.md`, and Sricharan's `research/` files. This is a live document — the decision log in §4 grows as you answer questions; §5 gets filled in only once real convergence happens.

---

## 1. Why narrowing changes everything — the mechanism, stated plainly

Every axis you pick changes three things simultaneously, not just one:

1. **What already exists (whitespace).** In all of Hyderabad/India broadly, AC repair has Urban Company, brand apps, and a mature informal-technician market — dense competition. Narrow to "AC servicing for renters in a specific IIITH-adjacent neighborhood, coordinated with an absent landlord" and the existing solutions mostly stop applying — nobody built a product for that exact intersection. **Narrower is not automatically better — it's better only when it moves you from a crowded whitespace to an empty one.**
2. **What evidence claims you're allowed to make.** `best_practices.md` §6 is explicit: a convenience sample licenses *mechanism* claims, never *prevalence* claims. If your team's real access is Hyderabad-based (per `team_reconciliation.md` — professors on campus, nearby relatives, local service centres), claiming "Indian households" is already an overclaim; claiming "Hyderabad renters near a tech campus" is honest and defensible. **The geography you actually have access to should usually become the geography you claim, not a broader one you're hoping generalizes.**
3. **Which rail actually matters.** A ritual/festival-calendar angle needs voice + a shared calendar/trigger, barely any logistics. A spare-parts-heavy trade-service angle (carpentry, AC compressor swaps) needs logistics for real. A payment-dispute-heavy angle (landlord/tenant, quote changes) needs the payments/authorisation rail to actually matter, not just voice. **The object you pick determines whether your Q4/Q5 rail answer is genuine or decorative** — this is exactly the "don't force all three rails if a rail adds no value" rule already in `Keeping_Machines_Running_Context.md`.

This is why your own example — Hyderabad vs. all-India, or a home-pooja axis vs. a generic-appliance axis — isn't a stylistic choice. It's a different competitive landscape, a different evidence ceiling, and a different rail story, every time.

## 2. The narrowing algorithm — 4 sequential filters

Applied in order; each filter's output becomes the next filter's input. Each filter is scored against `best_practices.md`'s actual winning criteria (Evidence, Creativity, Clarity, Feasibility, Thoroughness) plus the systems-thinking leverage-point test (`best_practices.md` §3) and real interview feasibility in the next ~24-30 hours.

**Filter 1 — Object/domain.** Which machine/service category (from `system_map.md` §3's clusters) has (a) real case-document evidence behind it, (b) genuine team access, (c) a mechanism that maps to a *high-leverage* system point (information flow / rules — leverage points #5-#6) rather than a low-leverage one (a parameter tweak — #12), and (d) whitespace once narrowed?

**Filter 2 — Segment/persona.** Given the object(s) that survive Filter 1, which specific population (renter vs. owner, multi-appliance household, remote-family-managing-parents' home, etc.) has the strongest combination of: pain intensity signal (from the 17+1 pain-threads), real team access, and delegatability (would they plausibly hand this off to an agent)?

**Filter 3 — Geography / cultural context.** Does narrowing to a specific place or cultural practice (a) match your team's real, defensible evidence base, (b) change the competitive landscape (fewer or more existing apps/solutions), and (c) create a genuinely non-obvious framing — per `best_practices.md` §1.2's warning that judges can tell when a solution is generic — rather than just shrinking the sample for no strategic reason?

**Filter 4 — Mechanism / insight-thread.** From the 17+1 candidate pain-threads (`notes.md` §2), which one is both testable within 3-6 interviews *and* survives the systems-thinking leverage-point test (`best_practices.md` §3) *and* has already-real case-document backing (`system_map.md` §1.5)?

Output: 2-3 ranked candidate problem statements (object × segment × geography × mechanism), each with an explicit "why this could win" and "why this could fail," for you to pick from or veto.

---

## 3. Going through all 10 questions — what's expected, what interview evidence is needed, how narrowing changes each answer

*(Exact question text and word limits: `context.md` Part 1.3. Resource-scan-specific suggestions already logged: `r1.md`. Sricharan's answer scaffolds: `research/report-source.md` Pages 14, 17-18.)*

| Q | What's actually being asked | Evidence/interviews required before it can be answered honestly | How narrowing changes it |
|---|---|---|---|
| **Q1** — Team & right-to-win | One line per member's personal connection + 50-word team statement on distinctive access | Each member's own real incident (yours and Atharv's still pending — `progress.md`); a real, checkable access claim (which households/technicians/landlords can you actually reach *today*) | A narrow, specific object/geography makes the access claim checkable and credible ("we can observe AC servicing among IIITH-adjacent renters") — a broad claim ("we understand household pain") fails the page's own "any three students" test |
| **Q2** — The one insight | 60 words, one non-obvious mechanism, evidence optional but scored, judges read this first | 3-6 real interviews + survey responses, independently corroborated (per the convergence protocol in `plan.md`) | The narrower the object/segment, the more likely 3-6 interviews actually saturate on a real, corroborated pattern instead of scattering across unrelated incidents |
| **Q3** — Six-step loop | Six ≤15-word steps: trigger, prior knowledge, action, counterparty, human check-in, completion | Enough real incidents to know what a *typical* trigger/counterparty/completion signal actually looks like for this specific object | A narrow object makes every step concrete and specific (a real IVR, a real named counterparty type) instead of generic placeholder language |
| **Q4** — Rail roles | One sentence per rail (voice/payments/logistics); a rail can have no role if justified | Interview evidence on where money, physical movement, and voice calls actually enter the real workflow for this object | The object choice directly determines whether all three rails are genuine or whether one is honestly absent (§1.3 above) |
| **Q5** — Rail to innovate on | 40 words, one rail, a specific missing capability | Confirmation from real incidents that the named capability gap is the actual bottleneck, not a guess | A narrow, well-evidenced mechanism (Filter 4) is what makes this claim defensible instead of speculative — see the leverage-point test in `best_practices.md` §3 |
| **Q6** — Customer asset | 30 words, the one thing the customer hands over, why they'll agree | Evidence on what data/access the household actually has, actually trusts a third party with, and actually struggles to retrieve today | Directly shaped by Filter 1's object choice — e.g. a warranty document (appliances) vs. a service-history relationship (recurring trade services) are different assets |
| **Q7** — Annexation | 30 words, next use-case subsumed, why it falls to you | Nothing new required beyond Q2's insight — this is reasoning from the locked mechanism, not new fieldwork | A narrow starting wedge with a *natural adjacent* use-case (e.g. AC servicing → other seasonal appliance servicing) is easier to defend than a wedge with no natural next step |
| **Q8** — Never delegate | One opening, one sentence, personal values | None — a team judgment call, explicitly stated to have "no right answer" | Unaffected by narrowing — this is about the 16 openings, not your chosen one |
| **Q9** — Incumbent counterfactual | One Indian company, 60 words, best guess why they haven't built this | Enough understanding of the real competitive landscape *for your narrowed segment specifically* — not the generic national picture | This is the sharpest place narrowing matters: "why hasn't Urban Company built this" is a different, weaker answer nationally than "why hasn't Urban Company built this for the specific renter/landlord/multi-appliance segment we found" |
| **Q10** — Track | Select Product Strategy | Already decided | Unaffected |

**The pattern across this table**: Q2, Q3, Q5, Q6, and Q9 all get *sharper and more defensible* the narrower and more evidenced your object/segment/geography choice is. Q1 gets more credible. Only Q8 and Q10 are unaffected. This is the concrete argument for narrowing now, before interviews, rather than after.

---

## 4. Live decision log

### Decision 1 — Filter 1 (Object/domain): deliberately left open

You correctly refused to pick an object cluster blind — nobody has evidence yet for which machine/service category is strongest. **Decision: do not pre-select.** Every interview stays unprimed ("tell me about the last time this happened," never "tell me about your AC") and the object is left to surface from what respondents actually bring up. Revisit after 3-4 interviews, when a real pattern either appears or doesn't (per the convergence protocol already in `plan.md`).

### Decision 2 — Filter 2 (Segment/persona): the real axis is service-network structure, not renter/owner

Your correction replaced a wrong assumption (a ritual/pooja axis) with a much sharper, evidenced one: **whether a household's repairs are routed through a managed community's own service network, or the household has to self-source a technician every time.** This is not the same variable as renter-vs-owner or age — a homeowner in an independent house and a homeowner in a large managed community face structurally different problems even with identical appliances.

**Confirmed access** (your direct answers):
- **My Home** (Hyderabad builder group, large gated-community developer) — **you live there, or immediate family does.** Direct access, no intermediary needed. This is the candidate "smooth/managed" case.
- **Independent households** (standalone house or small building, no managed service network) — confirmed accessible today. This is the candidate "painful/self-sourced" case — the contrast.
- **IIITH campus** — professors/staff living on campus (corroborates Sricharan's own brief).
- **Bonus, volunteered by you**: technicians in **tier-3 cities**, reachable by phone. Genuine supply-side access from a different market tier than Hyderabad metro — very few competing teams will have anything like this.

**Why this matters beyond just "more people to interview"**: `best_practices.md` §5 (UX researcher section) explicitly flags *"recruit for a negative/smooth case, not just painful ones... to stress-test whether the hypothesized mechanism is real or just a sampling artifact"* as a core good practice. You already have a real, live version of that exact contrast — My Home (candidate smooth case) vs. independent households (candidate painful case) — without having to go looking for it. That's not a minor convenience; it's the single hardest thing to arrange in a 2-day sprint, and you already have it.

**This also updates the divergence map.** `notes.md` §2's thread #8 ("society/RWA-owned assets fail because 'resident' is a diffuse, unaccountable owner") assumed society/RWA ownership is uniformly bad for accountability. Your access suggests a needed nuance — call it **thread #19**: *large, professionally-managed communities may partially solve the accountability-diffusion problem via an internal approved-vendor system, while smaller or informally-managed buildings inherit all of thread #8's diffusion problem with none of the professional-management fix.* Two real possible outcomes, both valuable: either My Home residents report genuinely smoother coordination (then the insight is *what specifically* the community's system does that an individual household's agent should replicate — a facility manager who owns the outcome? pre-negotiated vendor contracts? a shared ticketing system?), or they report their *own* version of friction (then the insight is that "managed" doesn't actually mean "solved," which is an even sharper, more counterintuitive Q2 candidate — per `best_practices.md` §1.2's warning that judges reward non-obvious findings, and "even the well-managed case still struggles, here's why" is about as non-obvious as this project has found so far).

### Decision 3 — Filter 3 (Geography): Hyderabad, confirmed by real access, not chosen abstractly

Every access channel above is Hyderabad-based (plus the tier-3 phone contacts as a bonus supply-side data point). Per `best_practices.md` §6, claim exactly the geography you have real evidence for — Hyderabad — rather than a broader claim the sample can't support.

## 5. Recruitment plan — ready to execute today

Six interview slots (the confirmed 3-6 target, using the full range since real access supports it), allocated to maximize the smooth/painful contrast plus the bonus supply-side angle:

| # | Segment | Channel | Who reaches out | Priority |
|---|---|---|---|---|
| 1-2 | My Home community (candidate smooth case) | Family/household directly, or the community's resident channel if one exists (WhatsApp group, notice board) | You, directly — no intermediary | High — do these first, they're your fastest possible access |
| 3-4 | Independent household (candidate painful case, the contrast) | Your existing independent-household contacts | You | High — needed early to compare against 1-2 while both are fresh |
| 5 | IIITH campus professor/staff | Sricharan's stated access | Sricharan | Medium — corroborates whichever pattern emerges from 1-4, and may itself be a third "institutional-managed" data point worth comparing against My Home's "community-managed" structure |
| 6 (bonus) | Tier-3 city technician, supply-side | Phone | You | High-value if time allows — almost no competing team will have a real technician conversation from outside metro Hyderabad; even a short call is a genuine differentiator for Q2/thoroughness |

**Interview guide to use**: Sricharan's household guide (`research/report-source.md` Page 7-8, 14 questions) is still the base — nothing about it needs to change for this segmentation, since it already asks "who owned this machine, who could approve the work, who paid" separately, which will surface the managed-vs-independent distinction naturally without needing to ask about it directly. Add one direct probe for slots 1-2 and 3-4 specifically:

> *"When this happened, who actually resolved it — did you contact someone yourself, or did it go through the building/community?"* — asked neutrally, without presupposing which answer is "better," right after Sricharan's question 3 ("could you walk me through the contacts you made").

For the tier-3 technician call (slot 6), use Sricharan's technician/service-centre guide (`report-source.md` Page 8) as-is — it's counterparty-agnostic and doesn't assume metro conditions.

## 6. Final narrowed problem statement

*(Pending real interview evidence — not filled in yet. Once slots 1-4 are done, revisit this file: name the object that actually recurred, state whether the smooth/painful contrast held or inverted, and lock the problem statement from what was actually found, not from this plan's hypotheses.)*
