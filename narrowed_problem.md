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

**Whitespace pre-registration, using yesterday's resource-scan run (`context.md` Part 5, `system_map.md` §2 and §6, `links.md`) — a prior to weigh evidence against, not a pre-selection.** Not picking the object doesn't mean going in blind about what each object would mean competitively if it surfaces. Registering this *before* seeing interview data (not after, which would be motivated reasoning) means once real evidence comes in, whitespace strength can be checked against it immediately instead of researched from scratch under deadline pressure:

| If this object surfaces | What resource-scan already found | Whitespace read |
|---|---|---|
| **Trade/repair services** (plumbing, carpentry, electrician, pest control) | No FSM-equivalent exists for households sourcing these directly — almost entirely informal/relationship-based, no dominant platform found in the whole resource-scan run | **Highest** — this is the strongest prior, untouched even by Urban Company's coverage |
| **AC** | Urban Company + brand apps cover it, but a LocalCircles survey (`system_map.md` §6.3) found only **7% of AC owners are on a brand maintenance contract** — 44% still use a local, informal provider. Also the one object with **documented legal ambiguity** — Indian rent law leaves AC servicing an undefined tenant/landlord grey zone (`system_map.md` §1.5, §4) | **Moderate** — "covered" on paper, mostly informal in practice; strong if a landlord/tenant angle surfaces |
| **RO/water purifier** | Kent's premium "SUPREME" IoT line already auto-detects faults and auto-registers service calls (`system_map.md` §6.3) — genuinely agentic, but brand-siloed to one premium product line | **Split** — if the respondent has a non-premium/non-Kent unit, the gap is wide open; if they have Kent SUPREME, the sharper claim narrows to "the cross-brand/cross-appliance layer," which is a real but different pitch |
| **Vehicle-adjacent incident** (e.g. respondent volunteers a car/bike servicing story) | India has **already fully solved** this exact class of problem for vehicles — government-coordinated SMS alerts, the official mParivahan app, third-party WhatsApp reminders (`system_map.md` §6.3, §6.5) | Not itself the target, but an excellent **contrast case** if it comes up — "here's what already works for one category, why not this one" is a strong Q9 framing regardless of which object wins |
| **Anything with a formal AMC/contract** | Industry commentary found Indian AMC/service vendors track renewals in **Excel with reminder calls "from memory,"** losing 20-30% of renewals to forgetting (`system_map.md` §6.4) — the vendor side is not obviously more reliable than the household side | Worth testing explicitly on both Eluru technician contacts (§5) — especially interesting since tier-3, informal relationships may have *no* AMC concept at all, a genuinely different (not just weaker) version of this pattern |

**Correction on terminology, important for Q4/Q5 and Round 2**: the competition has **3 rails, not 4** — Voice; **Payments & Authorisation, one combined rail**, not two separate ones (`Keeping_Machines_Running_Context.md` §7B); and Logistics. This matches the 3 actual partners exactly: Gnani (voice), Pine Labs (payments *and* authorisation together), Delhivery (logistics). Keep this straight in every answer from here on.

### Decision 1b — Rail-build potential: the second pre-registered lens, now the priority one

You flagged that rail-build potential — can this genuinely support all three rails, since it's what gets used in Round 2 if selected — is now the most important filter, more important than whitespace alone. Scored the same candidates from Decision 1's whitespace table against `Keeping_Machines_Running_Context.md` §7's own rail definitions (voice = the agent talks to the business, not just the user; payments/authorisation = *delegated authority*, not checkout; logistics = only real if physical movement genuinely happens):

| Object | Voice | Payments & Authorisation | Logistics | Overall |
|---|---|---|---|---|
| **AC** | **High** — case-documented booking/dispute calls | **High** — the case's own AC example *is* a payments/authority dispute (who approves, who pays, landlord vs. tenant) | **Moderate-high** — compressor/part swaps are a real physical-movement need, plus possible old-unit pickup | **Strongest all-around candidate** |
| **RO/water purifier** | High — case-documented multi-handoff install/service flow | Moderate — AMC/service-fee decisions, less structurally dramatic than AC's landlord scenario | **High** — filters/cartridges are `Keeping_Machines_Running_Context.md` §7C's own named logistics example | Strong on all 3, logistics especially |
| **Trade/repair services** (plumbing, carpentry, electrician) | **High** — commitment-enforcement is the core case-documented mechanism here | Moderate — quote changes are plausible but less legally dramatic than AC's | **Low-moderate** — many visits are labor-only, no real part-shipping need unless hardware/fittings are involved | Voice-strongest, **logistics is the real risk** |
| **Pest control** | Moderate — renewal calls, but incentive-mismatch (not scheduling) is the core mechanism | Moderate — recurring subscription payment | **Low** — technician typically self-supplies chemicals, no real delivery need | Weakest logistics of the group |

**The honest tension this surfaces**: the highest-*whitespace* candidate (trade/repair services) is also the *weakest* on logistics — many jobs genuinely don't need a part shipped. The two strongest *all-three-rail* candidates (AC, RO) have more moderate whitespace. Don't resolve this by picking one now — per Decision 1, the object still comes from interviews, not a desk decision. Instead: **during synthesis, score whichever object actually surfaced on both lenses together** (whitespace from Decision 1 + rail-completeness from this table), and if the surfaced object is logistics-weak, actively check the interview notes for *any* sub-case within it that did involve a part or physical movement (Sricharan's own Q9 — *"did any item need to move somewhere?"* — already captures this in every interview; just make sure it gets explicitly tagged during synthesis rather than treated as a throwaway question). A logistics rail can also be honestly absent, with a stated reason — the competition's own rules allow that (`context.md` Part 1.3, Q4) — but a genuinely three-rail-engaged story is a stronger Round 2 setup, and you already have the tool (Q9) to check for it in every conversation.

**A second, sharper hypothesis this design can also test, for free**: the same comparative structure already built (My Home managed vs. standalone/Eluru independent; Hyderabad metro vs. Eluru tier-3) may make *different rails* differentially valuable by segment, not just make the base coordination problem differentially painful:
- **Payments & Authorisation** may matter *less* for My Home if the community already negotiates fixed rates/an approved-vendor panel (a form of pre-cleared authority that an individual household lacks) — meaning the delegated-spend-cap concept (`Keeping_Machines_Running_Context.md` §7B) may be *more* differentiated and valuable precisely for standalone Hyderabad and Eluru households, who face raw, ad-hoc negotiation every time. Worth asking directly in the My Home technician interview (#6, `research_plan.md` §3): *"Are prices/rates for common jobs pre-agreed with the community, or negotiated fresh each time?"*
- **Logistics** may be *worse* in Eluru than Hyderabad if part availability or courier infrastructure is genuinely thinner in a tier-3 city — which would make a logistics-led Q5 rail claim sharper and more specific if it's the Eluru data that surfaces it, tying directly into thread #19. Worth an explicit probe: *"When a part was needed, how long did it actually take to arrive, and from where?"* — add this to the technician guides for #3 (Eluru electrician) and #6 (My Home technician) specifically, to compare.

**Two new probes, worth adding to every interview regardless of which object comes up** (informed by the above, layered onto Sricharan's guide per §5):
1. *"Do you already get automatic reminders for anything else — like your vehicle's insurance or PUC, or gas cylinder booking? How does that compare to how you get reminded, or not, about this?"* — directly tests the vehicle-vs-appliance contrast (`system_map.md` §6.5) and is especially interesting to ask in **both** Eluru and Hyderabad, since it's plausible the vehicle-reminder infrastructure itself is more or less present depending on market tier.
2. *"Is this a formal contract/AMC, or more of an ongoing relationship with someone specific you call?"* — distinguishes formal vs. informal servicing, and for the Eluru electrician/technician slots specifically, tests whether the AMC-vendor-forgetting finding even applies where there's no formal AMC concept to begin with — which would itself be a finding, not a null result.

### Decision 2 — Filter 2 (Segment/persona): the real axis is service-network structure, not renter/owner

Your correction replaced a wrong assumption (a ritual/pooja axis) with a much sharper, evidenced one: **whether a household's repairs are routed through a managed community's own service network, or the household has to self-source a technician every time.** This is not the same variable as renter-vs-owner or age — a homeowner in an independent house and a homeowner in a large managed community face structurally different problems even with identical appliances.

**Confirmed access** (your direct answers, quantified in Decision 3 below):
- **My Home** (Hyderabad builder group, large gated-community developer) — **you live there, or immediate family does.** Direct access, no intermediary needed. This is the candidate "smooth/managed" case.
- **Eluru households** (1-2, tier-3, presumably independent/self-sourced — to be confirmed, not assumed, per the new probe question in §5) — this is now the primary "painful/self-sourced" contrast, not a generic placeholder.
- **IIITH campus** — professors/staff living on campus (corroborates Sricharan's own brief).
- **Eluru electrician** (confirmed) plus one uncertain institutional technician in an unconfirmed tier-3 city — genuine supply-side access from a different market tier than Hyderabad metro; very few competing teams will have anything like this.

**Why this matters beyond just "more people to interview"**: `best_practices.md` §5 (UX researcher section) explicitly flags *"recruit for a negative/smooth case, not just painful ones... to stress-test whether the hypothesized mechanism is real or just a sampling artifact"* as a core good practice. You already have a real, live version of that exact contrast — My Home (candidate smooth case) vs. independent households (candidate painful case) — without having to go looking for it. That's not a minor convenience; it's the single hardest thing to arrange in a 2-day sprint, and you already have it.

**This also updates the divergence map.** `notes.md` §2's thread #8 ("society/RWA-owned assets fail because 'resident' is a diffuse, unaccountable owner") assumed society/RWA ownership is uniformly bad for accountability. Your access suggests a needed nuance — call it **thread #19**: *large, professionally-managed communities may partially solve the accountability-diffusion problem via an internal approved-vendor system, while smaller or informally-managed buildings inherit all of thread #8's diffusion problem with none of the professional-management fix.* Two real possible outcomes, both valuable: either My Home residents report genuinely smoother coordination (then the insight is *what specifically* the community's system does that an individual household's agent should replicate — a facility manager who owns the outcome? pre-negotiated vendor contracts? a shared ticketing system?), or they report their *own* version of friction (then the insight is that "managed" doesn't actually mean "solved," which is an even sharper, more counterintuitive Q2 candidate — per `best_practices.md` §1.2's warning that judges reward non-obvious findings, and "even the well-managed case still struggles, here's why" is about as non-obvious as this project has found so far).

### Decision 3 — Filter 3 (Geography): revised — a real two-geography comparison, not just Hyderabad plus a bonus call

**Correction**: the tier-3 hometown is **Eluru** (Andhra Pradesh), not "Hyderabad" — an earlier mishearing, corrected directly by the user. Real, quantified access, as reported:

| Location | Type | Household/customer contacts | Technician/supply-side contacts |
|---|---|---|---|
| **Eluru** (tier-3) | Hometown | **1-2 households** | **1 electrician**, confirmed |
| **Hyderabad** (metro) | My Home community | **1 household** (assumed to be the My Home family from Decision 2 — flag if this is actually a different, independent household) | — |
| **Tier-3 city, unconfirmed** | Institutional (school/office maintenance) | — | **1 technician, uncertain** ("not sure") — treat as stretch, not core plan |
| IIITH campus (Hyderabad, metro) | Institutional | Professor/staff, via Sricharan | — |

**This changes the geography decision.** Eluru alone gives you as much or more confirmed household access than Hyderabad does from your own network — the original plan's assumption that Hyderabad was the obvious primary geography doesn't hold once the real numbers are in. **Decision: treat this as a genuine Hyderabad-vs-Eluru comparison**, not a Hyderabad-primary-plus-bonus-technician-call framing.

**Why this is worth the added complexity, not just more thorough for its own sake**: `system_map.md`'s own market research already establishes that Urban Company and Housejoy are still *expanding into* tier-2/3 cities — meaning app-mediated service coverage in a place like Eluru is genuinely thinner than in Hyderabad today. That's not a weaker version of the same story; it's a different market-maturity condition, which may produce a sharper, less-mediated version of the coordination pain (or a completely different one — e.g. Eluru's smaller scale might mean *more* personal, relationship-based technician trust, which is itself a finding). Either result is real signal, and almost no competing team will have a genuine tier-3 customer-side incident to compare against a metro one.

**Honest limitation to hold onto, not hide**: Hyderabad's data point (My Home) is *metro + managed-community*, and Eluru's is *tier-3 + presumably-independent* (smaller cities are less likely to have My Home-style large managed developments, but this is an assumption, not yet confirmed — worth asking Eluru respondents directly whether any kind of managed building/society maintenance exists in their case, rather than assuming there isn't one). This means the two variables from Decision 2 (managed vs. independent) and Decision 3 (metro vs. tier-3) are **confounded** in this sample — if Eluru and Hyderabad look different, you won't be able to say for certain which variable caused it from these two data points alone. The IIITH campus interview (metro + institutionally-managed) helps triangulate: if campus and My Home look similar to each other but both differ from Eluru, that points toward metro-vs-tier-3 (market maturity) as the driver; if My Home and campus differ from each other despite both being metro-managed, that points toward something else. State this limitation plainly in Q2 if it comes up — per `best_practices.md` §6, an honestly-scoped finding is more credible than an overclaimed one.

## 5. Recruitment plan — ready to execute today, built from contacts you already have

No new recruitment needed — the confirmed access above already covers the 3-6 interview target:

| # | Location | Segment | Contacts | Who reaches out | Priority |
|---|---|---|---|---|---|
| 1-2 | Eluru | Tier-3, household/demand-side | 1-2 households | You | **High — start here.** Strongest confirmed household count, and the sharpest available contrast to My Home. |
| 3 | Eluru | Tier-3, supply-side | 1 electrician | You | High — pairs directly with 1-2, gives you a demand+supply view of the *same* market in one city |
| 4 | Hyderabad | Metro, managed-community, household/demand-side | 1 household (My Home — confirm this is the My Home family, not a different contact) | You | High — the metro anchor point for the comparison |
| 5 | Hyderabad | Metro, institutional-managed | Professor/staff | Sricharan | Medium — the triangulation point that helps de-confound Decision 3's limitation above |
| 6 (stretch) | Tier-3 city (unconfirmed which) | Institutional supply-side | 1 technician, "not sure" | You, if it comes through | Low priority — pursue only if slots 1-5 are done with time to spare |

**Interview guide to use**: Sricharan's household guide (`research/report-source.md` Page 7-8, 14 questions) is still the base for slots 1-2 and 4 — it already asks "who owned this machine, who could approve the work, who paid" separately, which surfaces the managed-vs-independent distinction naturally. Add one direct probe right after his question 3 ("could you walk me through the contacts you made"):

> *"When this happened, who actually resolved it — did you contact someone yourself, or did it go through a building/society/management system of some kind?"* — asked neutrally, and specifically useful for the Eluru interviews to actually test the "presumably independent" assumption above rather than take it for granted.

For slots 3 and 6 (technicians), use Sricharan's technician/service-centre guide (`report-source.md` Page 8) as-is — it's counterparty-agnostic and doesn't assume metro conditions. For slot 5 (campus), the household guide applies, since a professor is a household respondent even though the property itself is institutionally managed.

**Full probe set per slot, combining both sources**:
- **Slots 1-2, 4, 5 (household interviews)**: Sricharan's 14 questions + the managed-vs-independent probe above + the two resource-scan probes from Decision 1 (vehicle/reminder comparison; formal-AMC-vs-relationship).
- **Slots 3, 6 (technician interviews)**: Sricharan's technician guide + the AMC-vendor-forgetting probe already in `plan.md` (*"when a maintenance contract is close to renewal, what actually reminds you to call the customer, and how often does that step fail?"*) — for Eluru specifically, ask this *without* assuming an AMC exists; let the respondent say so if it doesn't, since that itself is the finding per Decision 1's whitespace table.

## 6. Final narrowed problem statement

*(Pending real interview evidence — not filled in yet. Once slots 1-4 are done, revisit this file: name the object that actually recurred, state whether the smooth/painful contrast held or inverted, and lock the problem statement from what was actually found, not from this plan's hypotheses.)*
