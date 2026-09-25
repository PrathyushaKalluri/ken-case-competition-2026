# Phase 2 — Assemble Your Agent · Paste-ready answers

**Team TripleIT · Opening 11 "Keeping the machines running" · Due Fri 25 Sep 2026, 11:59 PM IST**
Diagrams: `PHASE2_DIAGRAMS.html` (published as an artifact). Supporting research: `round2_strategy.md` (verified API notes), `phase2_research.md`, `files/user_journey.md`.

**What changed from the Tayyar drafts (read this first).** We moved the buyer from the household to the **service agency** (B2B2C). The household still gets the same promise: one visit, within an approved budget. But the agency pays us, runs our agent inside its own phone number, WhatsApp and ticket book, and keeps the customer relationship. We kept everything from `round2_vision.md` that still holds: the Ready gate, the rail gaps, the "voice never approves money" rule and the Machine Passport.

**Evidence tags:** **[V]** read in partner docs on 24 Sep · **[I]** our interviews or survey · **[A]** our assumption, stated so a judge can change it.

---

## The one idea every answer returns to

> **Any brand. Any machine. One trip.** Kokila works inside a local service agency. She finds out what's wrong inside the machine *before* anyone leaves the shop, so the technician's first visit is a repair and never a discovery.

**Why agencies, not households.** Agencies pay for every wasted trip. Households stay loyal to the technician they already know **[I: 3 of 12 survey incidents went to a known technician; the carpenter's crew runs on referrals]**. So we sell the fix to the people who lose money on the problem, and reach the household through a name it already trusts.

---

## Q1. What outcome is the agent accountable for? *(one sentence, ≤30 words)*

> **For India's tier-2 and tier-3 repair agencies: any brand, any machine, fixed on the first visit within the customer's approved budget, or the second trip is on us.**
*(28 words)*

**Business proof, one line (use it as a subtitle or in Q2 if the form allows):**
*A 10-technician agency that saves one trip per technician a day saves about ₹1.3 lakh a month, or about ₹7.8 lakh in six months.*

| Line | Maths **[A]**: every input can be changed |
|---|---|
| Trips saved | 10 technicians × 1 trip a day = 10 trips a day |
| Cost of one wasted trip | ₹500 (about 1.5 technician-hours, fuel, and a paid visit given up) |
| Per day | 10 × ₹500 = **₹5,000** |
| Per month (26 working days) | **₹1,30,000** |
| Six months | **₹7.8 lakh** (or ₹4–5 lakh at a more cautious 0.6 trips a technician a day) |

**Why "one trip saved per technician per day" is plausible:** a technician does about 4–6 visits a day **[A]**. In our survey, **6 of 12 incidents needed follow-up calls, and 2 needed 3 or more [I]**. Vidya Sagar: a wrong part means *"he might have to make three trips" [I]*.

**What "the second trip is on us" means in practice:** the promise only applies to jobs the agent marks **Ready** (Q3, Ready gate). If a Ready job needs a second trip, we waive our fee on that job and credit the agency ₹500. Honest diagnostic visits are labelled up front and don't carry the promise. That's how the promise stays checkable, and how we avoid going broke on it.

---

## Workings behind Q2–Q4: the product-sense path (stakeholders → pains → options → the one we chose)

**Stakeholders (8)**

| # | Stakeholder | Top pain | What they need | Evidence |
|---|---|---|---|---|
| 1 | **Agency owner** (the buyer) | Paid for trips that earn nothing; technicians do side jobs for cash | More paid jobs per technician-day; control without being on the phone | Carpenter crew: triage by hand, *"many people call me at the same time"* [I] |
| 2 | Dispatcher / front desk | Phones every customer twice; no idea if the part is ready | One list of exceptions | [A] |
| 3 | **Technician** | Discovery visit, then a parts run, then an argument over price | Know the job before leaving; get paid on the spot | Vidya Sagar: *"come first to diagnose, then go get back the parts"* [I] |
| 4 | **Customer at home** (often elderly) | A day lost waiting; explaining the problem again and again | One call, one visit | Maggi: urgent repairs take *"half of the day or one day"* [I] |
| 5 | **Payer** (often a child elsewhere) | Surprise charges they can't check | A limit set once; a fair-price check | RK Sir checked a quote through a friend [I] |
| 6 | Parts shop / distributor | Calls with vague part names; unsold stock | Exact part numbers; paid on pickup | [A] |
| 7 | Brand (OEM) | Warranty claims with missing evidence | A complete evidence packet | [A] |
| 8 | Rail partners | Need real transactional use cases | Multi-step, multi-party jobs | `round2_strategy.md` §4 |

**The agency's leaks, in rupees** (the ones we go after first):

| Leak | Today | Kokila's fix | ₹ at a 10-technician agency **[A]** |
|---|---|---|---|
| **Repeat trips** (wrong part, unknown fault) | About 1 per technician a day | Ready gate | **About ₹1.3 lakh a month** |
| Missed calls after hours → lost jobs | The owner can't pick up at 9 PM | 24×7 intake in the agency's name | 2–3 jobs a week |
| Unbilled extra work and side cash | Paid in cash, off the books | Voice report → UPI approval → logged | Hard to size; this is the owner's trust problem |
| Parts runs | The technician rides to the shop mid-job | Part secured before the slot | About 45 minutes a trip |
| Rejected brand warranty claims | Photos and serial numbers missing | Evidence packet built at intake | Claim revenue kept |

**Five paths we considered, and why we chose one**

| Path | What it does | Agency ₹ value | Build effort | Evidence | Verdict |
|---|---|---|---|---|---|
| **A. Ready-to-Repair** (intake → diagnose → part → Ready gate → one visit) | Cuts repeat trips | 🔴 Highest | Medium | Strongest | ✅ **The deep path** |
| B. Revenue fill (AMC and seasonal outreach calls) | Fills the slots path A frees up | High | Low | Sai Kakki: *"schedule the annual servicing"* [I] | ✅ **Second path**, human-approved first (L2 → L3) |
| C. Collections and approvals only | Stops price disputes | Medium | Low | RK Sir [I] | Folded into A (U10) |
| D. On-site technician copilot | Helps juniors diagnose on site | Medium | High | Crew trains juniors for 1–2 years [I] | Later (uses RepairGraph) |
| E. Cross-agency capacity exchange | Sells spare hours across agencies | High | Very high | Weak | Parked |

**Why A:** it's the only path that makes money for the agency **and** keeps the household's promise on day one, and every other path runs on the data it creates (RepairGraph, the Passport).

**Metrics**
- **North star:** first-visit fix rate on Ready jobs.
- **Business:** trips saved per technician a day; ₹ saved per agency a month; paid jobs per technician a day.
- **Customer:** hours from ticket to fix; calls the customer had to make (goal: 1).
- **Guardrails:** budget overruns = 0; share of jobs labelled "diagnostic" (watch for gaming); disputes; share of jobs sent to a human.

**Trade-offs we accept openly**
- **Speed vs. certainty:** waiting for the part can push the visit to the next day. One sure visit beats two quick ones.
- **Shipping two likely parts vs. return costs:** we send two only for parts under ₹500.
- **Technicians lose their parts markup:** we pay a fixed parts-handling fee through the split, or order from the technician's own shop.
- **White-label vs. our brand:** the agency owns the customer; we grow through the "Kokila Certified" badge.

**Guardrails:** voice never approves money · spending is capped by the customer's UPI budget and the agency's cap · no DIY advice on gas or wiring · life-critical devices go to L2 · always offer "talk to a person" · no always-on microphone in the home · every action is logged.

---

## Q2. Autonomy level

> **L3: Kokila acts on her own inside limits two people set.** The **agency** sets the rules: which jobs she can book, which parts she can order, and the most she can spend per job. The **customer** sets the budget in their UPI app. The most consequential thing she does without asking is **spend inside that budget**, on the visit fee, the part and the labour. She always asks first before spending above the budget, before a technician enters a home for the first time, before a machine leaves the home, and before any gas or electrical work. For **life-critical devices** (oxygen concentrators, clinic fridges) she **drops to L2**: she prepares everything and a human decides.

**Why L3, not L4:** some steps are still **human today and become agent later**. Claiming L4 while a dispatcher still confirms parts would be dishonest. The roadmap:

| Step | Pilot (weeks 1–6) | Month 3 | Month 6+ |
|---|---|---|---|
| Customer intake call | Agent (L3) | L3 | L3 |
| Diagnosis (top-2 faults) | Agent proposes, **senior technician confirms** (L2) | L3 above a confidence threshold | L3 |
| Ordering the part | **Dispatcher** orders | Agent orders up to ₹1,500 (L3) | L3, up to the agency's cap |
| Picking the technician | Agent proposes, **owner taps OK** (L2) | L3 | L3 |
| Spend inside the budget | L3 | L3 | L3 |
| Spend above the budget | L2 (payer approves in UPI) | L2 | **L2 always** |
| AMC and seasonal outreach calls | Owner approves the list (L2) | L3 within a monthly quota | L3 |

---

## Q3. States: happy flow and unhappy flow

**The whole design in one sentence:** a ticket becomes a visit only when **four things are ready at the same time**: the machine is known, the fault is likely, the part is in hand and the customer is approved and present. That's the **Ready gate**.

**Happy flow** (every state reads from or writes to a table in brackets; see the diagram in `PHASE2_DIAGRAMS.html`):

1. **Ticket in**: the agency's phone, WhatsApp or brand portal logs a job → Kokila picks it up *(Tickets)*
2. **Intake**: she calls the customer **in the agency's name**, in Telugu, Hindi or English; gets the symptom and error code (read back, then "press 1"); sends a WhatsApp link for a label photo and a 10-second video *(Tickets, Evidence)*
3. **Machine known**: the label photo gives the model; she checks the Machine Passport and warranty *(Machines, Passport)*
4. **Diagnosed**: RepairGraph gives the top-2 faults, the parts, a price range and a confidence score *(RepairGraph)*
5. **Approved**: the payer approves a budget in their UPI app (Pine Labs mandate) *(Mandates)*
6. **Part secured**: from the agency's own stock, a local shop (she phones and holds it) or Delhivery *(Inventory, Shipments)*
7. **READY GATE ✓**: the technician is matched on skill, brand and travel time, and the slot is confirmed only now *(Technicians, Schedule)*
8. **On site**: the technician checks in and the visit fee is captured *(JobCards, Payments)*
9. **Repaired and tested**: the customer says "yes" or presses 1, and the technician uploads a test video *(JobCards)*
10. **Settled**: money is captured up to the budget and split between agency, shop and technician; the rest is released *(Payments)*
11. **Learned**: the Passport and RepairGraph are updated; a 7-day "still working?" call is made; an AMC is offered *(Passport, RepairGraph, Campaigns)*

**Unhappy flow.** Every branch ends in a named state, never in silence.

| # | What goes wrong | How Kokila finds out | What she does | Ends in |
|---|---|---|---|---|
| U1 | Model or error code misheard | Read-back not confirmed | Repeats slowly; keypad entry; label photo | 2 |
| U2 | No label photo (elderly user, no smartphone) | Link not opened after 30 min | Asks a family member on the ticket; otherwise the technician reads the label at the visit | 3 |
| U3 | **Low diagnosis confidence** | Top-1 below threshold | **An honest diagnostic visit**: labelled as one, lower fee, no one-trip promise, or a 5-minute video call with a senior technician | 5 |
| U4 | Machine under brand warranty | Warranty lookup | If the agency is the authorised centre, a brand claim with a full evidence packet; if not, tells the customer honestly and logs a lead the agency didn't lose | 5 / closed |
| U5 | Payer unreachable (child in another city) | No approval in 2 hours | Nothing is spent; reminder by call and WhatsApp; slot held, then released | 5 |
| U6 | Customer wants to pay cash | Declines UPI | Quote acknowledged by WhatsApp OTP; cash logged on the job card; **the one-trip promise still holds** | 5 |
| U7 | Part not in any local shop (tier-3) | Shops say no; Delhivery pincode check | Delhivery next-day or two-day; tells the customer the real date; no visit before the part arrives | 6 |
| U8 | Part late or lost | Delhivery tracking push or failed-delivery update | Releases the slot; retries a local shop; new window | 6 |
| U9 | Technician doesn't show | No check-in 20 min after the window opens | Reassigns; owner alerted; customer told why | 7 |
| U10 | **Extra fault found on site** | Technician calls Kokila: "pipe also worn, one-eighty" | Checks the price range and remaining budget. Small and in scope → approves. Otherwise → the payer approves in UPI. **The technician's voice is a claim, never an approval** | 9 |
| U11 | Technician asks for side cash | Customer mentions it on the 7-day call; amount differs from the job card | Flag to the owner; the customer's warranty only covers logged work | owner |
| U12 | Fake or wrong part fitted | Part code in the test video doesn't match the SKU | Hold payment; replacement at the agency's cost | 9 |
| U13 | Fails the test | Customer says no, or the video fails | Hold capture; re-visit **counts against our promise** (₹500 credit if the job was Ready) | 8 |
| U14 | Same fault again within 30 days | Passport shows a repeat | Free re-visit; RepairGraph lowers that diagnosis's confidence | 8 |
| U15 | Payment times out | No receipt | Look up by order reference **before** retrying, so no double charge | 10 |
| U16 | Customer upset or abusive; technician unsafe | Negative sentiment (Gnani Workforce handoff) / technician's "unsafe" button | Human callback within 15 min; visit fee protected; job moved up | human |
| U17 | Life-critical device | Device class from the label | L2; human now; arrange a backup device first | human |
| U18 | Two machines in one home | Customer mentions a second machine | Adds it to the same visit if the budget and skills allow (one trip, two fixes) | 4 |

---

## Q4. Each rail: what exists vs. what must be built

**Headline:** *none of the three rails knows what a technician, a job or a machine is.* Voice talks, money moves, parcels travel, but **nothing commits the right part, the right person and a ready customer to one time slot**. That's the gap that causes second trips, and the gap Kokila fills.

| Rail | What we send it | What comes back | When it fails | What it must never do | What exists today | Build status |
|---|---|---|---|---|---|---|
| **Voice: Gnani** (intake and updates) | Agent Builder phone agent, calling as the agency; STT `POST /stt/v3` (clips ≤60 s); TTS `/api/v1/tts/inference` for read-backs | Transcript; filled variables (`model`, `symptom`, `error_code`); keypad (DTMF) digits; call recording; post-call log | Code-mixed model numbers misheard; noisy kitchens; no documented STT confidence score | Diagnose (Gnani **transcribes**; **our** RepairGraph diagnoses); take a spoken "yes" as approval to spend | STT/TTS, Agent Builder, DTMF, Workforce handoff on sentiment, Zoho CRM/Desk integration, custom HTTP actions **[V]** | ✅ Exists. Test mid-call API replies (the docs contradict each other) |
| **Voice: Gnani** (outbound to parts shops, technician reports) | Call a parts shop: "Do you have an LG inlet valve, part number X?"; technician says "capacitor, six-fifty" | Stock yes/no and price, captured as data; part and amount read back and confirmed with press 1 | The shop says "maybe tomorrow" (a conditional promise) | Treat "I'll try" as a firm yes | Outbound calls, variables **[V]**; no way to extract a *conditional commitment* | 🟡 Exists, plus **our ask**: structured commitment extraction |
| **Voice: machine sound** | A 10-second clip of the running machine | Nothing useful. The noise filter removes it | Always, by design | — | Background-noise filter **[V]** | 🔴 **Ask**: a raw non-speech capture mode. Meanwhile, a WhatsApp video goes to our classifier |
| **Payments: Pine Labs** (the budget) | `POST /mpp/v1/mandate` for a UPI One-Time Mandate or Reserve Pay; Grantex scope `mpp:payment:max_txn_paise` = budget | `deep_link` / QR for the payer's UPI app; mandate status; `GET /mpp/v1/balance` | Payer doesn't approve; e-mandate extra authentication above ₹15k **[A: verify]** | Spend above the budget; let voice authorise money | P3P, Grantex, UPI OTM and Reserve Pay listed as GA **[V]** | ✅ Exists |
| **Payments: Pine Labs** (capture and split) | Capture at events: check-in → visit fee; test passed → part and labour; split between agency, shop and technician | `Payment-Receipt`; settlement; refund | Timeout → possible double charge | Capture before proof of work | Capture, refunds, split settlement, payouts **[T: from teammate draft, re-check]** | 🟡 Exists, plus **our ask**: **capture triggered by a real-world event** (P3P pays for an HTTP request, not a passed test); **a delegate payer** (a child pays for a parent) |
| **Logistics: Delhivery Maps** | Customer address (messy tier-3 landmarks); technicians' locations | Geocode, cleaned-up address, two-wheeler travel-time matrix | Landmark-only addresses | Pick the technician (Delhivery gives **travel times**; **our** matcher picks on skill + brand + time) | 10 Maps APIs + MCP server (`geocode_address`, `compute_distance_matrix`…) **[V]** | ✅ Exists |
| **Logistics: Delhivery shipping** | Part from a distributor to the agency or technician; reverse pickup of an unused part | Pincode serviceability; tracking push webhook; failed-delivery event | Tier-3 pincodes, 2-day delivery; parcel weight limits | Deliver "to an address" when the job needs "to Ravi before 10 AM" | Forward/reverse shipping, tracking push, failed-delivery actions **[T]** | 🟡 Exists, plus **our ask**: **delivery to a person by an appointment deadline**, with an "at risk" webhook |
| **Our own: agency connector** | Ticket from the agency's WhatsApp, Google Sheet, Zoho Desk or brand portal | A normalised ticket; status written back | The agency types tickets inconsistently | Change the agency's records without a log | WhatsApp Business API, Sheets API, Zoho Desk API | 🔨 **We build** (simple) |
| **Our own: RepairGraph** (Q5) | Model + symptom + code + video | Top-2 faults, parts, labour time, price range, confidence | New model, never seen | Claim certainty it doesn't have | Nothing shared across brands | 🔨 **We build**: the moat |

**What we do until the partners fill their gaps:** our backend waits for the "test passed" event, then calls capture. The payer's number is set as the approver. The slot is confirmed only after Delhivery's "delivered" push. Machine sound comes in through a WhatsApp video.

**Where AI is used in this path** (the rest is rules and APIs, deliberately):

| # | AI integration point | Model type | Autonomy |
|---|---|---|---|
| 1 | Understand the customer's Telugu, Hindi or English description | Gnani STT + LLM slot-filling | L3 |
| 2 | Read the model label from a photo | Vision / OCR | L3 (read back to confirm) |
| 3 | **Diagnose: top-2 faults and parts** | RAG over RepairGraph + a video/sound classifier | L2 → L3 |
| 4 | Phone parts shops and turn the answers into data | Gnani outbound + commitment extraction | L3 |
| 5 | Check whether an on-site quote is fair | Price range from past jobs | L3 |
| 6 | Turn the technician's Telugu voice note into a job report | STT + LLM | L3 |
| 7 | Check the test video | Video classifier | L2 (human reviews failures) |
| 8 | Learn from every closed job | Outcome → RepairGraph confidence update | Offline |

---

## Q5. Does the agent need a fourth rail?

> **Yes: a *Repair Truth rail*. Voice, money and parcels exist; knowledge of what fails inside the machine doesn't.** Every repair in India starts from zero. The technician asks for the model, guesses the fault, and comes back with the right part on a second trip. The rail has two parts: (1) **RepairGraph**, a shared, brand-neutral knowledge base covering every consumer machine in India: model → components → how each one fails → the symptom customers describe (in Telugu, Hindi or English) → the test that confirms it → the part number and compatible alternatives → labour time → a fair price range; and (2) a **Machine Passport**, a consented ID for each machine with its warranty, past repairs and parts fitted. **We build it and give it free to certified agencies**, starting simple (TV, microwave, RO, washing machine), then AC and fridges, then laptops. In return, every job they close teaches it something. That's how agencies cut their costs, and how our data compounds. Long-term it should be an open standard, like Aadhaar for people, FASTag for vehicles and DigiLocker for documents. The Government's Right to Repair portal already asks brands to share this information; the rail is what makes it usable by an agent.

**The modules and layers of the full solution** (diagram in `PHASE2_DIAGRAMS.html`):

| Layer | Modules | Owner |
|---|---|---|
| **1. Channels**: where the work already happens | Agency phone number (IVR/call forwarding), agency WhatsApp Business number, ticket connectors (WhatsApp group, Google Sheet, Zoho Desk, brand portal) | Ours, on partner APIs |
| **2. Brain**: the master agent | **Kokila Orchestrator**: owns each case and its state machine; **policy engine** (agency rules, customer budget, safety list); audit log | Ours |
| **3. Sub-agents**: one job each | Intake (voice) · Identify (vision) · Diagnose (RAG) · Quote & Approve (payments) · Parts Sourcing (voice + logistics) · Dispatch (matching) · Field Assist (technician copilot) · Close & Settle · Revenue (AMC/seasonal calls) | Ours |
| **4. Modules** (the rails) | Voice module (Gnani) · Authorisation & Payments module (Pine Labs) · Location & Logistics module (Delhivery) · Messaging module (WhatsApp Business) | Partners |
| **5. Truth**: the data | **RepairGraph** · **Machine Passport** · agency ops database (tickets, technicians, stock, schedule) · price book | Ours → open standard |

**How RepairGraph gets built** (give to get):

| Phase | Categories | Why this order | Sources |
|---|---|---|---|
| **1 (months 0–3)** | TV, microwave, RO purifier, washing machine | High volume, few failure modes, cheap parts, 3 of our survey categories | Public service manuals, brand error-code lists, the Right to Repair portal, **every job card from pilot agencies** |
| **2 (months 3–9)** | AC, fridge, geyser | Seasonal spikes; gas and compressor work needs L2 safety rules | Plus distributor part catalogues |
| **3 (months 9+)** | Laptops, phones | Board-level faults; brand-locked parts | Plus refurbishers |

**Why agencies give us their data:** they get the whole graph free; a certified badge ("Kokila Certified: one-trip guaranteed") that households see; and fewer wasted trips. Agencies' data stays theirs; only anonymised fault → part → outcome links go into the shared graph.

**Next revenue stream (not in the pilot):** RepairGraph knows which parts fail on which models, and which pulled parts still work. That's the base for a **graded refurbished-parts marketplace**: working parts harvested from scrapped machines, sold to agencies with a RepairGraph grade. It's cheaper for tier-3 customers, and brings in revenue beyond SaaS.

**Who should build the rail, if not us:** the open standard should sit with the Department of Consumer Affairs' **Right to Repair portal**, with brands contributing through their industry body. Until then, we build it one job at a time.

---

## Q6. How a human interacts with the agent: their interface

> **No new app. Kokila lives inside what the agency already uses, and speaks in the agency's name.** A ticket lands wherever it lands today: a phone call to the shop, a WhatsApp message, a line in the register sheet, or a job from a brand's portal. Kokila picks it up and does the rest from inside the agency's own system.

| Who | Their interface | What they see or hear | What they never have to do |
|---|---|---|---|
| **Customer** (often an elderly parent) | A call from **the agency's own number**, plus WhatsApp from **the agency's WhatsApp Business number** | *"Namaste, this is Kokila from Sri Sai Electronics. Your washing machine: is it showing an error code?"* Read-backs; one link for the label photo and video; the technician's name, photo and time; *"Is it working? Say yes or press 1."* | Download an app; explain the problem twice; chase the technician |
| **Payer** (often a child in another city) | UPI app + WhatsApp | One plain budget: *"Sri Sai can spend up to ₹2,500."* Approval requests with the part photo and a fair-price range; the receipt shows which part went in | Pay above the budget without a fresh UPI approval |
| **Technician** | WhatsApp job card + one "Call Kokila" number | Telugu voice summary of the job: machine, likely fault, part "with you" or "arriving 9 AM", customer window. Check in, press "unsafe", upload the test video. **Reports extra work by voice** ("pipe also worn, one-eighty") → read back → press 1. Paid when the test passes | Type; learn an app; argue about money at the door |
| **Dispatcher / front desk** | The agency's existing sheet or Zoho Desk, with Kokila's status written into each row | Only exceptions: no-show, part stuck, dispute, life-critical | Call every customer twice a day |
| **Agency owner** | A WhatsApp message every evening | *"Today: 14 jobs, 11 first-visit fixes, 9 trips saved, ₹4,500 saved. 2 need you."* | Log in to a dashboard |
| **Parts shop** | An ordinary phone call | Kokila asks for stock in Telugu, holds the part, pays by UPI | Install anything |

**How we connect to each kind of agency:**

| Agency type | Where tickets live today | How Kokila connects | Setup time **[A]** |
|---|---|---|---|
| Small crew (like our carpenter's 10 people) | Owner's phone + a WhatsApp group | Agency number forwarded to Gnani; Kokila joins the WhatsApp Business inbox | 1 day |
| Mid-size multi-brand agency | Excel / Google Sheet | Sheet connector reads new rows and writes status back | 2–3 days |
| Established agency / brand-authorised centre | Zoho Desk, Freshdesk, or a brand portal | API/webhook (Gnani has a Zoho Desk integration **[V]**); brand portal job emails read automatically | 1–2 weeks |

---

## Q7. Name

> ## **Kokila**
> *(yes, that Kokila, from "Rasode mein kaun tha?")*
> Kokilaben's famous question was about the kitchen. Ours is ***"Machine mein kya tha?"*** Kokila won't let anyone leave the shop until she knows what's wrong inside the machine. The technician arrives with the answer and the part.

**Why it works:** it's a real name, easy to say on a phone call ("this is Kokila from Sri Sai Electronics"), and white-labels cleanly. Everyone in India gets the joke, and the joke *is* the product: ask first, then send someone.
**Tagline for agencies:** *"Pehli trip mein fix. Baaki Kokila dekh legi."* (Fixed on the first trip. Kokila handles the rest.)
**Backups:** *Ek Trip Baburao* (Hera Pheri: *"yeh trip bachana, Baburao ka style hai"*, "saving this trip is Baburao's style"), *Paisa Hi Paisa* (for the pitch to agency owners).

---

## Q8. Which Indian company has the best chance of building an agent like this?

> **Servify, not Urban Company.** Urban Company, NoBroker and Housejoy sell repairs **to households** and own the technician, so helping independent agencies works against their business. Servify already runs after-sales for brands like Apple and Samsung, coordinating about 18,000 service centres and about 8 million service transactions a year, so it holds the device data, the service-centre connections and the logistics links. **Why it hasn't built Kokila:** its customers are the brands, and brands have no reason to make **multi-brand, independent** agencies better at fixing their machines, or to share fault data with them. That gap, where most tier-2 and tier-3 repairs actually happen, is ours.

| Competitor | Type | Who pays them | Why they won't build Kokila | Threat |
|---|---|---|---|---|
| **Servify** | Direct (closest) | Brands | Serves brands, not multi-brand independents | 🔴 High |
| **Urban Company** | Indirect (competes for the same customer) | Households; commission from technicians | Owns the technician and the visit; independent agencies are its competitors | 🟠 Medium |
| **NoBroker Home Services** | Indirect | Households (bundled with rentals) | Metro, rental-led; repairs are a cross-sell | 🟢 Low |
| **Housejoy** | Indirect | Households | Same marketplace model as UC, smaller | 🟢 Low |
| **Pronto** | Indirect (instant house help) | Households | Cleaning and cooking in under 10 minutes, not diagnosis-led repair; but it shows investors back speed in home services | 🟢 Low |
| **Brand service networks / Onsitego** | Indirect | Brands / warranty buyers | Single-brand or warranty-led | 🟠 Medium |
| **Justdial / Sulekha** | Indirect (agencies' lead source today) | Agencies pay for leads | Sells leads, doesn't fulfil jobs; we make the agency's paid leads convert | 🟢 Low |

**Our edge in one line:** they own the customer or the brand. We make **the agency** the best version of itself, under its own name.

---

## How judges' criteria map onto this (for our own check before pasting)

| Criterion | Where we earn it |
|---|---|
| **Evidence** | Survey (6 of 12 incidents needed follow-ups), Vidya Sagar's *"three trips"*, the carpenter crew's own dispatch habits, verified endpoints |
| **Creativity** | White-label agent inside the agency's system; RepairGraph given away free (give to get); Kokila |
| **Clarity** | One promise (one trip) repeated in all 8 answers |
| **Feasibility** | Every piece exists except RepairGraph and three precise partner asks; the pilot starts with one 10-person crew we already know |
| **Thoroughness** | 18 unhappy states, an autonomy roadmap, the rail table, competitors |
| **Business value** | About ₹1.3 lakh a month for a 10-technician agency **[A]**; our fee is about ₹1,000 per technician a month **[A]** → about 13× return |

## How to build it (the feasibility story, in case a judge asks "how hard?")

| Week | What gets built | With what |
|---|---|---|
| 1–2 | Intake agent in the agency's name; WhatsApp link for photo and video; Google Sheet connector | Gnani Agent Builder, WhatsApp Business API, Sheets API |
| 2–4 | RepairGraph v0 for washing machines and RO (manuals + error codes); top-2 diagnosis with a confidence score | An LLM with RAG over a small graph database |
| 3–5 | Budget mandate + capture on job events | Pine Labs P3P sandbox (when it opens) |
| 4–6 | Technician matching + part tracking; evening digest for the owner | Delhivery Maps MCP; WhatsApp |
| 6 | **Pilot with the carpenter's 10-person crew**: measure first-visit fix rate before and after | Our Round 1 contact |

**The metric that matters:** **first-visit fix rate on Ready jobs**. Guardrail metrics: the share of jobs honestly labelled "diagnostic" (if it climbs, the promise is being gamed), customer budget overruns (must be 0), and payment disputes.
