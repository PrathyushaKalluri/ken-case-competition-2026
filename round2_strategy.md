# Round 2 Strategy — What to Submit, How to Win, What to Test

**Team TripleIT · Opening 11 "Keeping the machines running" · written 24 Sep 2026**
**Deadline: Friday 25 Sep 2026, 11:59 PM IST, about 36 hours from now.** The portal isn't live yet; The Ken will email when it opens.

Evidence tags used in this file:
- **[V]** I read it on the partner's official docs page today (24 Sep).
- **[T]** It's in our teammate draft `round2.pdf` (21 Sep); I haven't re-checked it.
- **[I]** From our own interviews.
- **[U]** Our inference or design. Not verified.

Related files: `phase2_research.md` (the three-rail chain), `~/Downloads/round2.pdf` (teammate draft: "co-arrival", L3), `~/Downloads/Ken_Round2_Assembly_Master.md` (other AI draft: RepairGraph, L4).

---

## 0. The short version

1. **The deliverable** is eight typed answers plus an optional AI chat log. There's no build and no presentation.
2. **The baseline we're graded against is a frontier AI.** Both drafts we already have are roughly what that baseline looks like. Being thorough won't set us apart. What will:
   - **our own sandbox tests** (Gnani is open right now with ₹1,000 of credits);
   - **our own supply-side evidence** (the carpenter's ten-person crew, the Eluru parts shop);
   - **one precise ask to each rail owner.**
3. **Be creative in the design and exact in the claims.** The FAQ says: *"don't scale your agent down to fit what already exists."* Design the agent you actually want. Then, for every capability, say clearly whether it exists (with the endpoint) or has to be built (with its shape and a stopgap).
4. **Proposed headline finding: none of the three rails has a concept of a person.** Delhivery moves parcels, Gnani talks, Pine Labs moves money. Nothing commits *a skilled technician + the right part + the customer's time window* as one unit ("co-arrival"). That gap is what causes repeat visits. Repeat visits cost the household its routine (our Round 1 insight) and cost the agency technician hours (the business case).
5. **Base the three rail asks on that gap (§6.2). The fourth rail is the piece no partner will ever build: truth about the machine** (the Machine Passport, §6.7).

---

## 1. What Round 2 is and how it's judged

| Item | Detail |
|---|---|
| What you submit | Eight typed answers + optional link to the AI conversation(s) you used |
| When | By **Fri 25 Sep, 11:59 PM IST** |
| Judged on | Evidence, creativity, clarity, feasibility, thoroughness |
| Compared against | (a) other teams in **the same opening** (Opening 11 had about 5% of teams [T]); (b) **The Ken's own frontier-AI answer** for this opening |
| AI use | Allowed. Logs are used to separate **human from machine** contribution, so show your work. |
| Missing capabilities | *"Finding it, specifying it, and saying what your agent does in the meantime is one of the highest-scoring things you can do."* |
| APIs | *"Name specific endpoints… what comes back."* Saying "uses the voice rail" counts as incomplete. |
| Level (Q2) | Score the agent **as designed**, including capabilities still to be built |
| Next round | Build track builds the agent. Strategy track gets a *different problem statement*. Both test "where India's agentic infrastructure bends and breaks, and what should change." |

### The eight questions and what each is really testing

| # | Question | What it's really testing | What a generic AI will write | How we beat it |
|---|---|---|---|---|
| 1 | Outcome, one sentence | Is it checkable? Does the agent own the result or just an activity? | "Help households get appliances repaired quickly" | A **verifiable end state** plus the **two things the household protects** (routine, money), with the agency benefit implied |
| 2 | Autonomy L1–L4 | Do we understand that the level is set by the **most consequential unasked action**? | "L3 with human in the loop" | Name the exact riskiest action taken unasked, the exact list of things it asks first, and when it drops a level (life-critical devices) |
| 3 | States: happy and unhappy | Real failures vs. polite imagined ones | A 6-step happy path and 3 generic errors | A state machine **plus failures found in our own Gnani test calls** (Adhavan's email says this outright) |
| 4 | Each rail: exists vs. must be built | Did we read the docs? | "Gnani for voice, Pine Labs for payments, Delhivery for logistics" | Endpoints, what they return, **documented contradictions**, and each missing capability with its shape and a stopgap |
| 5 | Fourth rail + Indian company | Can we spot a missing piece of infrastructure? | "A WhatsApp rail" / "a data rail" | A rail that follows directly from our headline gap, with its API sketch and a reasoned builder |
| 6 | Human interface | Real people, specific moments | "A mobile app with chat" | Household (voice-first, elderly), **payer ≠ user** (child approves for parent), technician, agency, parts shop |
| 7 | Name | Memorable, matches the insight | English compound words | Short, speakable on a phone call, carries the insight |
| 8 | Indian company most likely to build it | Understands incumbents and incentives | Urban Company | Reasoned choice; don't reuse the Q5 company |

---

## 2. Your direct questions, answered

### 2.1 Can we be creative, or do we have to stay within the APIs?
**Be creative about what the agent should do. Be exact about what already exists.** The organisers explicitly reward missing capabilities and explicitly say *don't scale the agent down*. What loses marks is a *false* claim that an API already does something. The winning pattern for every capability:

> **Need →** what exists today (endpoint, what it returns) **→** the gap (in the shape we need) **→** what the agent does in the meantime.

### 2.2 "Never attribute your own model's diagnosis, a marketplace's technician supply, or the household's authorisation policy to a partner API that doesn't provide it." What does that mean?
It means: don't give a partner credit for work *our* system does. Three concrete traps:

| ❌ Wrong (a judge who read the docs will catch it) | ✅ Right |
|---|---|
| "Gnani **diagnoses** the fault from the call" | "Gnani **transcribes** the call (`POST /stt/v3` → `transcript`). **Our** model turns the transcript into likely faults." |
| "Delhivery **assigns the nearest technician**" | "Delhivery `/matrix` returns **travel times**. **Our** matcher (skills + availability) picks the technician. Delhivery has no technician concept." |
| "Pine Labs **approves only repair-related spends**" | "Grantex enforces a **per-transaction cap** (`mpp:payment:max_txn_paise`). **Our** backend checks that the spend matches the approved repair scope." |

The gaps (who does the diagnosis, the matching, the scope check) are exactly where our marks are. If we credit them to a partner, we give those marks away.

### 2.3 Should we integrate the agent into repair agencies too?
**Yes. It's already in our Round 1 answer.** Round 1 Q3 step 4 coordinates "local agencies", and Round 1 Q9 says Urban Company lacks "pre-dispatch intelligence **for local agencies**." Your business point (fewer visits per repair → technicians free for more jobs → more agency revenue) is the second half of our value, and it's where the money comes from.

**Recommendation: one repair case, two faces.**
- **Household side** protects the household's money, time, consent and preferred technician.
- **Agency side** is a dispatcher copilot: pre-visit evidence, job batching, parts readiness, technician job card.

Both sides read and write **one shared repair case**. The household's limits can never be overridden by the agency. This gives us a two-sided evidence base (we're both the customer and people who know the workers, as in Round 1 Q1). It also makes the unit economics real (technician-hours per completed repair).

### 2.4 Sign language → voice, and machine noise → diagnosis: valid or a distraction?

| Idea | Fits our insight? | Judging effect | Verdict |
|---|---|---|---|
| **Machine noise → evidence** | **Yes, directly.** It's pre-visit evidence (a grinding motor, a clicking relay, a compressor that won't start). | Creativity + a real missing capability. **Doc finding:** Gnani's ASR has a *background-noise filter* [V] meant to suppress non-speech sound, which is exactly the signal we want. Gnani stores call recordings [V], so our own sound classifier can run on them. | **Include as a supporting evidence channel and a specific ask to Gnani** ("a raw-audio / noise-filter-off capture mode for non-speech evidence"). Not the headline, because the accuracy is unproven. |
| **Sign language → voice** | Weak. None of our interviews involved deaf users. It's an accessibility feature, not our mechanism. | Judges may read it as a detour: it hurts clarity and has no evidence behind it. | **One line in Q6 accessibility only** ("text and video channel; sign-language interpretation is a separate capability we haven't designed"). Don't build around it. |

**General rule for any extra idea:** does it make the **first visit a repair visit instead of a discovery visit**? If yes, it belongs. If not, it's for the appendix or the chat log.

### 2.5 Emotional situations (customer crying, technician abused)
- **Documented hook [V]:** Gnani "Workforce" (multi-agent) routes between agents on **natural-language conditions**, and its docs give *"sentiment is negative and mentions cancel"* and *"user requests supervisor"* as examples. So the handoff to a human exists. Emotion *accuracy* is not documented.
- **Customer crying** (for example, food spoiling in a dead fridge, or an elderly parent alone):
  - acknowledge what they actually said;
  - slow down, and summarise the next concrete step and its time;
  - **treat distress as an urgency signal, not a mood to manage** (move the job up);
  - offer a human callback.
  - Never label someone's mental state. Never push risky do-it-yourself fixes to calm them down.
- **Technician abused:**
  - an "end visit / unsafe" button or voice command on the job card;
  - the visit fee is still captured for time spent (Pine Labs capture of the visit-fee portion);
  - the agency is alerted;
  - the incident is logged without assigning blame;
  - the household's rating of that technician is frozen until a person reviews it.
- **Life-critical devices** (Atharv's nursing-home equipment): drop to L2, alert a human immediately, and arrange a backup device first.
- Where this goes: Q3 unhappy flow (U-states) and Q6 (interface).

### 2.6 The payment wallet idea
Round 1 Q4 already says "repair wallet," so we keep it, but it has to be built properly:
- **A wallet that *holds* customer money needs an RBI prepaid-instrument (PPI) licence.** A startup can't just add one.
- **Three legal ways to get the same user experience:**
  1. **UPI Reserve Pay (SBMD)** [V: listed in P3P as GA]: money is blocked in the customer's own bank account, with several debits against it. This fits a multi-step repair (visit fee → part → labour). The other draft cites ₹10,000 / 90 days [unverified].
  2. **UPI One-Time Mandate (OTM)** [V: GA in P3P]: block once, capture the actual amount, the rest is released. Teammate draft [T]: up to ₹1 lakh, 60 days, one capture.
  3. **Pine Labs' own prepaid products**: the docs index lists *Brand Wallet, Gift Cards, Reloadable Cards* under "Prepaid & Issuance" [V: index only; the Brand Wallet page returned a 404, so this needs checking]. Pine Labs is the issuer, so the app doesn't need its own licence. **This is worth an office-hours question.**
- **Auto-pay under a threshold** is built on Grantex scope `mpp:payment:max_txn_paise:*` [V]: the agent pays without asking below the cap. Above it, a UPI approval request goes to the **payer**.

Creative payment directions to consider (pick 2–3 for Q4 and keep the rest in reserve):

| Idea | What it does | Exists? |
|---|---|---|
| Tiered auto-approve by category | Consumables (RO filter, AC gas) auto-approved; compressor or motherboard always asks | Cap exists [V]; category rules are ours [U] |
| **Payer ≠ user** | An adult child in another city approves; the elderly parent only sees status (Maggi's aunt, Prathyusha's mom) | **No household-delegate concept documented** [T] → gap |
| **Pay on proof** | Capture fires on a physical event (Delhivery "delivered" scan, functional-test video) | P3P pays for an **HTTP request** (402 → retry → receipt) [V]. **Nothing native triggers capture from a real-world event** → gap |
| Pay to reserve | The agency's booking endpoint returns 402; the agent pays the visit fee through P3P to lock the slot | **Buildable on P3P as designed** [V + U] |
| Split settlement | One customer payment split between agency, parts shop and technician | Split settlement documented [T/V in other draft] |
| Instant technician payout | Technician is paid the moment the functional test passes | Payouts API exists (IMPS/NEFT) [T]; UPI-ID payouts to informal workers unclear |
| Fair-price guard | Compares a mid-job quote with the usual range and pauses if it's out of range (RK Sir had to phone a friend to check) | Ours [U] |
| Refund on returned part | Unused part picked up → Delhivery scan → partial refund | Refund API documented [T]; the link between them is ours |
| EMI for a big repair | Offer EMI on a compressor or motherboard | Affordability Suite in the Pine Labs index [V: index only] |
| Service subscription (AMC) | Annual servicing, with reminders (Sai Kakki: *"I would like them to schedule the annual servicing"*) | Subscriptions API [V: index only] |

---

## 3. Verified API notes: what each rail actually offers (checked 24 Sep)

### 3.1 Gnani (voice): open now, ₹1,000 credits
**Two layers.**

**(a) Speech APIs** [V]
- STT REST: `POST https://api.vachana.ai/stt/v3`
  - sends: multipart `audio_file`, `language_code`, header `X-API-Key-ID`
  - returns: `success, request_id, transcript, model`
  - limits: **≤60 s**; WAV/MP3/OGG/FLAC/AAC/M4A, 8–44.1 kHz
- STT streaming: `wss://api.vachana.ai/stt/v3/stream` (16-bit mono PCM, 8/16 kHz, 1,024-byte frames). **Batch STT** handles long files, with speaker labels (per the use-case page).
- TTS: `POST https://api.vachana.ai/api/v1/tts/inference` (text, voice, model `timbre-v2.5`, language, speed, audio_config → audio), plus SSE `/api/v1/tts/sse` and WebSocket. A text-normalisation guide covers numbers, currency, dates and IDs.
- Voice cloning: `POST /api/v1/tts/voice-clone/embeddings`.
- Plugins for **LiveKit and Pipecat**, so a custom agent pipeline is possible.

**(b) Agent Builder platform** [V]
- System prompt (Jinja2 templates) and a knowledge base.
- Test by chat, browser voice and **real phone calls to whitelisted numbers**.
- **Workforce:** multi-agent handoff on natural-language conditions (for example, sentiment).
- DTMF (keypad) capture, voicemail detection.
- Advanced ASR settings: barge-in, silence timeouts, **background-noise filtering**.
- Dynamic variables; disposition prompt.
- **Language switch prompt** (it detects "switch to Telugu"-style requests from the output of multiple STT engines).
- Integrations: Twilio SMS, Zoho CRM/Desk, email, **custom HTTP actions** (On-Call or Post-Call), Webex.
- Import a Twilio number; conversation logs and call audio; dev/action logs; analytics.
- **Platform REST API:** create/list/update agents, trigger test calls, get conversation logs and audio, manage FAQs, chat widget.

**Findings that matter**
1. **The docs contradict themselves.** The Actions page says *"API response storage in variables"* is **work in progress** [V]. The Custom Integration page says On-Call actions support **"After API Call Variables"** and "Speak During Action" [V].
   - Why it matters: if a mid-call lookup can't be spoken back, the agent can't say "your part arrives Thursday, shall I book Friday?" during the call.
   - **Test T2 settles it.**
2. **No image, video or file input in voice agents** [T, consistent with the variable types I saw: bool/int/float/string only]. The model-label photo needs a second channel (an SMS/WhatsApp link).
3. **No confidence score is documented for STT**, so error codes and model numbers need **read-back plus DTMF**.
4. **The noise filter works against sound evidence** (see §2.4).
5. **Telephony is Twilio-import only** [V]. Whether Indian numbers can be provisioned natively isn't documented. TRAI rules on commercial calls are a real constraint in India [U, verify].
6. We didn't check whether agents are capped at three languages (teammate draft [T]). **Test it.**

### 3.2 Pine Labs (payments and authorisation): sandbox "coming soon"
**P3P (Pine Labs Payments Protocol)** [V]
- Flow:
  1. The merchant server returns `402 Payment Required` with `WWW-Authenticate: Payment <challenge>`.
  2. The agent creates a one-time token from the customer's mandate.
  3. The agent retries with `P3P-Credential: Payment` and `X-Grantex-Token`.
  4. The server verifies, captures, and returns `Payment-Receipt`.
- Grantex scopes: `mpp:payment:initiate`, `mpp:payment:max_txn_paise:*`.
- Mandates: **UPI ReservePay (GA), OTM (GA), Cards (GA)**; stablecoin is future.
- Endpoints: `POST /mpp/v1/mandate` → `deep_link` (QR for the UPI app) or `checkout_url` (card + OTP); `GET /mpp/v1/balance`.
- **Revocation and mandate expiry aren't documented** (the docs say "confirm with your Pine Labs integration owner").

**Core payment API** [from the other draft; not re-read by me]
- Base `api.pluralpay.in`, UAT `pluraluat.v2.pinepg.in`; token `POST /api/auth/v1/token`.
- Orders: `POST /api/pay/v1/orders`; lookup by id or by `merchant_order_reference` (idempotent).
- Pre-auth capture/cancel: `PUT …/orders/{id}/capture|cancel`.
- Refunds: `POST /api/pay/v1/refunds/{order_id}`.
- Split-settlement release/cancel; payouts; payment links (pre-auth, part payment, split_info); subscriptions.

**Also listed** [V: index only]
- MCP server (payment links, orders, refunds, settlements over natural language).
- Agent Skills and Agent Enablement Toolkit.
- Agentic Commerce page (marketing: *"live on ChatGPT/UPI"*).
- Affordability (BNPL/EMI), UPI Autopay, Brand Wallet, Gift Cards, Reloadable Cards.

**Findings that matter**
1. **P3P is built to pay for a *digital* resource** (an HTTP request that returns 402). A repair is a *physical* outcome. There's no native way to say "capture when the part is delivered and the machine passes its test."
   - **This is our clearest new finding: P3P for physical-world services needs capture conditioned on events.**
2. **The cap is on amount only.** It doesn't cover merchant, category, or "matches the approved quote," so scope has to be enforced by us.
3. **No payer-delegate concept** (child pays for parent) [T].
4. **Voice can't authorise money.** Approval happens in the UPI app (QR or deep link). This is a design constraint.
5. Regulation (from a secondary article [T]): extra authentication for e-mandates above ₹15,000; liability for a wrong agent payment is undefined.

### 3.3 Delhivery (logistics): Maps open (log in to get a token); shipping sandbox "coming soon"
**Maps** [V]
- 10 APIs: geocoding (Delhivery's "GeoNaksha" address model), reverse geocoding, address validation / verification / standardisation, routing (traffic-aware), distance matrix, tolls, autosuggest, map tiles.
- **MCP server** at `https://gateway-maps-pub-int.delhivery.com/mcp`, with 9 tools: `geocode_address, reverse_geocode, standardize_address, validate_address, verify_address, auto_suggest, route, compute_distance_matrix, calculate_tolls`. Works with **Claude Code**. The token comes from a signed-in browser session.
- Other draft (not re-read): `POST /geocode`, `/route`, `/matrix`, bearer JWT, motorcycle mode, 40k matrix pairs.

**Shipping (B2C)** [T]
- Pincode serviceability (includes `max_weight` and an out-of-delivery-area flag).
- Forward and reverse orders.
- Pickup request `POST /fm/request/new/`.
- Tracking pull plus a **push webhook**.
- **NDR** (failed-delivery) actions: reattempt / defer.
- QC on reverse pickup.
- GST/HSN required; e-waybill above ₹50,000.

**Findings that matter**
1. **No concept of a person.** No technician, skill, availability, appointment window or job [T, consistent with the Maps API list].
2. **No multi-stop optimiser.** Route plus matrix exist; batching jobs by skill and time window is ours to build.
3. **Delivery goes to an address, not to a person at a time.** You can't say "deliver to technician Ravi before his 3 PM job at this house."
4. Large appliances (fridge, washing machine) may exceed parcel `max_weight`, which is relevant for "take the machine to the workshop."

---

## 4. Partner goals: what each company gets from our solution

| Partner | What they're pushing (from their docs/launches) | What our problem gives them | Our "new depth" for them |
|---|---|---|---|
| **Gnani** | Agent Builder, Workforce, Indic STT/TTS; wants voice agents doing real transactional work beyond call centres | A new vertical: after-sales and repair service lines, **outbound calls to informal businesses** (parts shops, technicians) | **"Voice is the API for the informal economy."** The Eluru parts shop has no inventory API; our agent *calls it* and turns the answer into data. Plus a sound-evidence mode. |
| **Pine Labs** | P3P, Grantex, agentic commerce, MCP; wants agent payments to become normal | Repair is a high-frequency, **multi-party, multi-step** payment (visit fee → part → labour; agency + shop + technician) | **Event-conditioned capture** (pay on physical proof) and **delegate payer**. These take P3P from "paying for APIs" to "paying for the physical world." |
| **Delhivery** | Maps + MCP (launched June 2026 [T]), address intelligence, parcels, reverse logistics | Spare-parts traffic (small, high-value, urgent) and returns, especially in tier-2/3 where parts are scarce | **Appointment-bound delivery to a person** (co-arrival). This moves Delhivery from "deliver a parcel to an address" to "make a service visit succeed." |
| **Agencies / technicians** (not a sponsor, but the buyer) | Fewer wasted trips | **More completed jobs per technician-day** | Evidence brief, part ready, fair and instant payment |

**Your business point, quantified.** Fill these numbers in from the carpenter crew today. They're our evidence that no AI baseline has.
- Extra visits per repair = visits ÷ completed repairs − 1.
- Hours freed per week = jobs/week × extra visits avoided × (travel + on-site hours per visit).
- Extra jobs per week = hours freed × share of those hours actually refilled ÷ hours per job.
- *Illustrative only:* 40 jobs/week, 1.3 → 1.15 visits per job, 75 min per visit → about **7.5 technician-hours/week freed per crew** → about 2–3 extra jobs/week.

---

## 5. Diverge: every kind of agent this problem could hold

Grouped by **whose agent it is** and **when it acts**. ★ marks ideas that fit our Round 1 insight and the headline gap best.

**A. Household side**
1. ★ **Evidence collector.** Voice intake, label photo, sound clip, error code read-back.
2. ★ **Repair coordinator (our core).** Owns the case from report to a verified fix.
3. **Remote-family guardian.** A child in Bangalore manages the parent's Eluru home: approvals, visit monitoring, updates. (Payer ≠ user.)
4. **Quote checker.** Compares the technician's quote with the usual range and flags creep (RK Sir).
5. **Parts witness.** Old part vs. new part photo, brand check (Maggi's "only this part" order).
6. **Machine memory.** Service dates, AMC renewals, warranty, a reminder before failure (Sai Kakki).
7. **Repair-or-replace advisor.** Mixer costs ₹2,400, repair costs ₹1,700 → advise (Sarala interview [T]).
8. **Society/RWA agent.** Pooled vendors and shared machines (lifts, pumps, borewell motor; Sarala's water-tank motor).
9. **Landlord–tenant arbiter.** Who pays for the AC service (documented grey zone, in `narrowed_problem.md`).

**B. Supply side**
10. ★ **Agency dispatcher copilot.** Batching by skill and travel time, parts readiness, no-show recovery.
11. ★ **Technician job-card agent.** Voice notes in Telugu → structured report; check-in; functional-test proof; instant payout.
12. **Parts-shop agent.** Answers stock calls from other agents; reserves a part; paid by P3P.
13. **Crew-lead subcontracting agent.** The carpenter who subcontracts plumbers and electricians: a routing brain for a ten-person crew.
14. **Training / second-opinion agent.** A junior technician on site asks a senior (or a model) using photos.

**C. Between parties (agent-to-agent)**
15. ★ **Household agent ↔ agency agent negotiation.** Slot, price, parts, all pre-agreed before the visit.
16. **Warranty/OEM claim agent.** Pulls entitlement and routes to the authorised centre. Right-to-Repair portal data.
17. **Reverse-logistics agent.** Old part back for warranty, unused part return, e-waste.

**D. Before failure (predictive)**
18. **Infrastructure-stress agent.** Power fluctuations, hard water, water scarcity (Maggi's geyser in Vizag) → predicts failures. *This is the "aging infrastructure" angle: India's grid and water conditions cause the failures.*
19. **Seasonal agent.** AC servicing before summer, RO filters before the monsoon.

**E. Institutions**
20. **Nursing-home / clinic equipment agent** (Atharv): L2, backup device first.
21. **Small business agent** (a shop's fridge or freezer, where downtime means lost stock).

**Which ones should shape the submission?** Core = 2 + 10 + 11 + 15 (two-sided coordinator). Supporting features = 1, 3, 4, 5, 12. Q7 expansion (from Round 1) = parts marketplace. 6, 7, 18 and 19 are good "what's next" lines. 8, 9, 13, 16, 20 and 21 stay in reserve.

---

## 6. Recommended spine for the submission

### 6.1 Headline gap: co-arrival (from teammate draft; confirmed by my doc read)
A repair visit succeeds only when **four things meet inside one window**:
1. a verified address;
2. a technician with the right skill;
3. the right part (with the technician or already at the house);
4. the customer present, with entry approved.

The rails supply pieces of this: Maps for the address, scans for the part, Gnani for the customer, Pine Labs for the money. **Nothing commits them as one unit.** When one piece slips, the visit becomes a discovery visit, and the household loses a day.

### 6.2 One precise ask per rail (the organisers score "specificity of the ask" [T])

| Rail | Our ask to the rail owner | Why our flow stops without it | What we do meanwhile |
|---|---|---|---|
| **Gnani** | (1) A **non-speech audio capture mode** (noise filter off, raw clip saved as evidence). (2) **Structured commitment extraction**: "Ill come after 5 if the part comes" becomes `{accepted: conditional, condition: part_arrival, time: 17:00}`. | We can't use machine sound as evidence, and we can't tell a firm technician promise from a maybe | Recordings from call logs go to our own classifier; read-back plus a DTMF "press 1 to confirm" |
| **Pine Labs** | **Capture conditioned on an event**: "capture ₹X to merchant M when event E (a signed delivery scan or a functional-test attestation) arrives, before the mandate expires." Plus a **delegate payer**. | Without it the agent must either pay before proof (risky) or ask a human every time (L2, which brings back the follow-up burden) | Our backend waits for the event, then calls capture on the OTM / ReservePay debit; payer = the child's number (to test) |
| **Delhivery** | **Appointment-bound delivery to a person**: consignee = technician ID, deadline = job start minus buffer, plus a webhook for "at risk of missing the job." | We can only confirm a slot once the part has *landed*, which wastes slack time; a late part is found out too late | Our scheduler confirms the slot on the "delivered" push; NDR (failed-delivery) triggers a re-plan |

### 6.3 Fourth rail: worked out from the business problem (see §6.7 for the full ideation)
**Recommendation: the Machine Passport rail** (a permanent digital identity and repair history for every appliance), with the Capacity rail as runner-up. Reasoning in §6.7.

### 6.4 Autonomy: L3 or L4? (a decision for the team)
- **L3 argument** (teammate draft): the most consequential unasked action is charging up to the customer's limit, which is word-for-word the L3 definition. It's safe and hard to attack.
- **L4 argument** (other draft): the agent plans many steps, re-plans when a part is late or a technician doesn't show, checks the functional test, and is judged on whether the machine works. That's word-for-word the L4 definition. The FAQ says to score the agent as designed.
- **My recommendation: L4 with L3 money limits.** Say it in one line: *"L4: it owns the repair end to end (plans, re-plans, verifies, comes back when stuck), but every rupee and every door stays inside limits the household set."* Our Q1 is an outcome ("confirmed working"), which only makes sense at L4. Claiming L3 while being accountable for an outcome is internally inconsistent.

### 6.5 Draft answers (reconciled; edit them in your own words, because logs are compared)
- **Q1:** *"A household's broken appliance is confirmed working by a functional test on the first repair visit, within the spending limit the household approved."* Variant: add "…or, when discovery is unavoidable, by the second, with the household told why."
- **Q7 name options:** Tayyar ("ready"), SahiVisit, PehlaFix, Mistri Mate. Tayyar matches "arrive ready" best.
- **Q8:** With the Machine Passport as the fourth rail (built by Servify, §6.7), **Q8 stays Urban Company**, which is consistent with our Round 1 Q9 answer. Two different companies, and no change of story between rounds.

### 6.7 Fourth rail: ideated from the business problem

**The method: start from a business outcome, not a technology.** Round 1's strategic move was *"cut the number of technician visits per repair."* The same test applies to the fourth rail: **which money problem in the repair economy can none of the three rails ever fix, however well they're used?**

#### Step 1: follow the chain Round 1 started
```
Fewer visits per repair  →  technician hours freed  →  hours refilled with paid jobs  →  agency earns more
        ▲                         ▲                          ▲                               ▲
  needs: know the machine    needs: part + person       needs: demand reaches          needs: households trust
  and fault BEFORE visiting  arrive together            small agencies                 local technicians enough to pay
  (diagnosis truth)          (co-arrival)               (capacity)                      (trust)
```
Each link has its own missing rail. The question is which link is the **bottleneck** and which **no partner will build**.

#### Step 2: the candidates, each framed as a business need

| # | Fourth rail | Business problem it solves (₹ terms) | Our evidence | Could a partner build it instead? | Generality (beyond repairs) | Proposed Indian builder |
|---|---|---|---|---|---|---|
| **1** | **Machine Passport rail**: a permanent ID for every appliance (QR/serial) holding model, warranty, full repair history, parts fitted, test results; readable by any consenting technician or agent | **Second visits due to wrong diagnosis or wrong part.** Every call starts from zero today. With the machine's history, the first visit is prepared. Also: warranty leakage, fake parts, resale value. | Sai Kakki's technician asked the model number first and got it right in one visit; RK Sir: *"once repaired… gets spoiled again"* (no history); Maggi wants proof of which part was fitted | **No.** Gnani talks, Pine Labs pays, Delhivery moves; none of them holds *truth about the machine*. Pure whitespace. | Medium-high: every machine (appliances, vehicles, medical equipment, farm pumps) | **Servify** (after-sales platform between brands, service centres, logistics) [verify coverage] |
| **2** | **Capacity rail**: technicians' freed hours published as bookable slots across agencies (skills, area, time) | **Freed hours are worth ₹0 unless refilled.** Round 1 saves visits; this turns saved hours into paid jobs. It's the missing half of our own business case. | Carpenter's crew does urgency triage by hand; households complain about no-shows | Partly. Delhivery could build "appointments" but not a labour marketplace | High: any service opening (salon, tutor, pet care…) | **Urban Company** (has the supply, but its incentive is to keep it closed) |
| **3** | **Household consent rail**: who in a family can approve what, for whom (child approves for parent; the maid can open the door; the landlord pays for the AC) | **Jobs stall waiting for the right approver**; technician arrives and nobody's authorised | Maggi's aunt handles her Vizag house; Prathyusha's mom relies on intermediaries | Partly. Grantex handles agent grants; **UPI Circle** (NPCI) already allows family payment delegation [U, verify]. It doesn't cover *non-money* authority (entry, removal) | Very high: all 16 openings need "who can authorise for whom" | NPCI / an Account Aggregator-style consent layer |
| **4** | **Parts-availability rail**: live stock and holds across small parts shops | **Second visit to fetch a part**; technician's lost hours on parts runs | Vidya Sagar: *"incorrect parts… three trips"*; technician buys parts himself | Partly (Delhivery could list the stock of warehouses it serves) | Low-medium | Servify / a distributor |
| **5** | **Proof-of-work / trust rail**: signed record that a verified technician did X, fitted part Y, and it passed test Z | **Local technicians can't charge fairly because they aren't trusted** (households trust brand centres "blindly" and question local technicians) | RK Sir: brand centre *"whatever they say I follow"*, local one *"definitely doubts"* | No | Medium | Folded into #1 (the repair history *is* the proof) |
| **6** | **Machine telemetry / sound rail**: machines report their own state | Catch failures before breakdown | None directly (no smart appliances in our interviews) | No | Low for India now (few connected appliances) | OEMs |

#### Step 3: recommendation, **#1 Machine Passport rail** (with #5 folded in), because:
1. **It's the root of our Round 1 promise.** "The first visit should not be for discovery" is impossible at scale unless the machine's identity and history already exist before the call. Co-arrival (§6.1) needs to know *which* part; the passport provides that.
2. **None of the three partners will ever build it.** Co-arrival can be handled as an *extension* of Delhivery (our Q4 ask). The machine's truth belongs to nobody, which makes it the cleanest fourth-rail argument: *"voice, money and movement exist; truth about the machine doesn't."*
3. **It's the asset the household owns and hands over.** The Ken's brief rewards *"asking users to hand over something they own."* Our Round 1 Q6 asset (model label, symptom evidence) **becomes permanent** here instead of being re-collected for every repair.
4. **It lets local agencies compete.** A verified repair history gives a local technician the trust a brand centre has (#5 solved), which brings demand back to small agencies (partly #2).
5. **It powers the Round 1 Q7 parts marketplace.** The history of which parts fail on which models is the demand forecast.
6. **It fits the India-stack pattern and has policy support.** *Aadhaar for people, FASTag for vehicles, DigiLocker for documents — nothing for household machines.* The Government's **Right to Repair portal** already pushes brands to share repair and parts information [RR1], so the policy direction is there; the missing piece is a machine-level ID agents can read.
7. **Each partner benefits:** Gnani asks fewer questions (shorter calls, better answers); Pine Labs can underwrite EMI or repair insurance using machine history; Delhivery ships the *exact* SKU (fewer returns).

**Live-signal layer (merged from #6, added 24 Sep):** a smart-home API isn't the fourth rail on its own, but it makes the Machine Passport **update itself**:
- **Connected appliances** (Matter, Google Home APIs, LG ThinQ, Samsung SmartThings) write their error codes and state into the passport automatically.
- **Older appliances** (most of India): a low-cost **energy-monitoring smart plug** records the power pattern. A compressor that struggles to start or a motor drawing too much current may show up *before* the breakdown. This is an India-specific retrofit idea and unproven.
- *Why only a layer:* low connected-appliance penetration in India (none among our interviewees); Google isn't Indian; smart-home APIs mostly expose on/off and mode, not detailed faults, and each brand's data stays in its own cloud; "smart home" is a predictable idea the baseline will likely suggest. [U: check the Google Home API and Matter appliance docs before claiming specifics.]
- *What it enables:* the "before failure / predictive" agents (#18, #19 in §5) become a natural next step.

**Runner-up: #2 Capacity rail.** Choose it if we want the business story to lead ("we free hours, and the rail sells them"). Weakness: Urban Company is the obvious builder, and many teams will say "a technician marketplace."

#### Step 4: Q5 paste-ready draft (Machine Passport)
> **Yes: a Machine Passport rail.** Voice, money and movement exist; truth about the machine does not. Every repair today starts from zero: the technician asks the model, guesses the fault, and often returns with the right part on a second visit. The rail gives each appliance a permanent consented ID (serial/QR) with model, warranty, repairs done, parts fitted and test results, readable by any authorised technician or agent. Our agent would then know the machine *before* the call, send the exact part, and give a local technician a verified track record. **Servify**, which already sits between brands, service centres and logistics, is best placed to build it. Until then, our agent builds the passport one repair at a time from label photos and job cards. The passport can also update itself: connected appliances (Matter, Google Home, LG ThinQ) report their own error codes, and older machines can do the same through a low-cost energy-monitoring plug.

*(Check the Servify claim before submitting; keep it hedged.)*

**API sketch (proposed, not existing):** `POST /machines/resolve` (label photo or serial → machine ID) · `GET /machines/{id}/history` (consented) · `POST /machines/{id}/repairs` (a signed job record: technician, part SKU, test result) · `GET /machines/{id}/entitlements` (warranty/AMC: valid / expired / unknown) · `POST /consents` (the household grants read access to an agent or technician for one case).

---

## 7. Competitive analysis: India's agentic infrastructure vs. abroad
*(Only publicly known features; no performance benchmarks were run. Items marked [U] should be checked before we quote them.)*

### 7.1 Voice
| | India (Gnani; Sarvam) | Abroad (ElevenLabs Agents, Vapi, Retell, Bland) |
|---|---|---|
| Strength | Indic languages, 8 kHz phone audio, code-mixed speech, Indian names and numbers [V for Gnani; Sarvam documents 22 languages per the other draft] | Mature agent tooling: tool calls, transfers, test suites, analytics [other draft] |
| Limits that matter to us | No image input in agents; noise filter hides machine sound; no STT confidence; Twilio-only number import; one doc says mid-call API responses are "WIP" [V] | Weaker Indic accuracy and code-mixing [U]; Indian telephony compliance not native |
| **India-specific constraint** | TRAI rules on commercial/unsolicited calls and number series; outbound calls to *businesses* on a consumer's behalf are a grey area [U, verify] | — |

### 7.2 Payments
| | India (Pine Labs P3P + Grantex, UPI mandates) | Abroad (Stripe agentic/ACP, Visa Intelligent Commerce, Mastercard Agent Pay, Google AP2, Coinbase x402) [names U, verify] |
|---|---|---|
| Strength | **Agent payments on bank rails (UPI) are GA** [V]. The block-and-debit (ReservePay) model suits multi-step jobs. | Card-network tokens for agents; x402 uses the same "HTTP 402" pattern as P3P |
| Limits that matter to us | Amount-only scope; no event-conditioned capture; no delegate payer; revocation undocumented [V]; e-mandate extra authentication above ₹15k [T]; liability undefined [T]; PPI licence for a stored wallet | Card-centric; weak for India's UPI-first users |
| **Finding** | *India is ahead on agent payment rails and behind on agent payment rules* (who is liable, delegation, scope). | |

### 7.3 Logistics / field service
| | India (Delhivery) | Abroad (field-service platforms: ServiceTitan, Salesforce Field Service, ServiceNow FSM; parts-to-technician programmes by large carriers) [U, verify names] |
|---|---|---|
| Strength | Indian address intelligence (GeoNaksha), tier-2/3 reach, reverse pickup, an MCP server agents can call [V] | Technician scheduling + parts + appointments in one system, but sold to *enterprises* |
| Limits that matter to us | No people, no appointments, no multi-stop solver [T/V] | Built for formal enterprises; doesn't fit India's informal ten-person crews |
| **Finding** | India's repair market is mostly informal (the other draft cites 44% using a local informal provider for AC, per LocalCircles, in `narrowed_problem.md`), so **field-service software doesn't reach it. The co-arrival gap is bigger here than abroad.** | |

### 7.4 "Aging infrastructure": two readings, both usable
1. **Physical infrastructure causes the failures:** voltage fluctuation, hard water, water scarcity (Maggi's geyser). Good for the "predictive / what's next" line.
2. **An aging population:** elderly parents alone at home while the payer lives elsewhere, which drives the payer ≠ user design.

---

## 8. Trade-offs, risks, guardrails (short form for Q3 and Q6)

| Risk | Guardrail |
|---|---|
| Wrong remote diagnosis → wrong part | Send the top-2 parts and return one; low confidence → an *honestly labelled* diagnostic visit |
| Agent overspends | Grantex cap + our own scope check; above the cap → the payer approves in their UPI app; voice never authorises money |
| Duplicate charge or shipment on a timeout | Look up by original reference before retrying (idempotent `merchant_order_reference`) |
| Unsafe DIY advice (gas, wiring) | Banned; route to a qualified technician |
| Stranger at the door | Entry needs explicit approval; technician identity shown beforehand |
| Technician loses the parts markup → resists | A fixed parts-handling fee in the split, or the technician's own shop is the supplier |
| Agency interest vs. household interest | The household's limits and preferred technician can't be overridden by the agency side |
| Privacy (recordings, photos, location) | Purpose-limited retention; technician location only during a job |
| Emotional calls | §2.5 |
| Life-critical devices | L2 + human + backup device |

**Trade-offs to state openly:**
- Speed vs. certainty: a diagnostic visit is sometimes the honest answer.
- Autonomy vs. consent friction.
- Agency-first (faster to start) vs. household-first (neutral).
- Pre-shipping parts (fewer visits) vs. return logistics cost.

---

## 9. What to test in the next 30 hours (this is our evidence advantage)

### 9.1 Gnani: do it today
Sign up with a **personal email**, create an agent (system prompt = intake job description; knowledge base = a short appliance-fault FAQ), whitelist your numbers, and call it. For each test record: what you said, what the agent did, pass/fail, and a screenshot or clip.

| ID | Test | What it tells us |
|---|---|---|
| G1 | Say a model number ("LG FHM1207ZDL") and an error code ("E-4-2") in Telugu-English, 5 tries each | Entity accuracy; read-back and DTMF needed? |
| G2 | Custom On-Call action returns a fake "part ETA Thursday"; can the agent say it in the same call? | **Settles the doc contradiction** |
| G3 | Switch language mid-sentence (Telugu → English → Hindi) | Code-mixing; language-switch behaviour; any 3-language cap |
| G4 | 10 s silence; talk over the agent; call from a noisy kitchen | Silence timeout, barge-in, noise filter |
| G5 | Play a mixer or washing-machine sound into the call; then send the same clip to `POST /stt/v3` | Is the sound filtered out or kept? Is the recording usable for our classifier? |
| G6 | Conditional promise: "I'll come after 5 only if the part arrives" | Does it log this as confirmed (bad) or conditional? |
| G7 | Crying or angry script; "I want a human" | Does the Workforce sentiment/supervisor handoff fire? |
| G8 | An elderly-style slow speaker; amounts ("eighteen fifty rupees") | TTS number normalisation; comprehension |
| G9 | Technician-style scope-change call from a noisy spot: "capacitor burnt, six-fifty" in Telugu-English; confirm by keypad | Are the part and amount captured correctly? Does read-back + DTMF work? Is the technician's voice reporting path feasible? |

This becomes the **Q3 unhappy flow**: "found in our calls," which the AI baseline can't have.

### 9.2 Delhivery Maps: today, if someone logs in
Log in at delhivery.com/maps → copy a session token → I can connect the **Maps MCP server to Claude Code** in this session and run:
- `geocode_address` on a messy real Eluru address (with landmark-style directions);
- `compute_distance_matrix` for 3 technicians → 4 jobs (motorcycle mode).

This gives real outputs for Q4.

### 9.3 Pine Labs: docs only for now
If sandbox access arrives before Friday: create an OTM, capture less than the blocked amount, try raising the amount, try a mandate on another person's number. Otherwise, cite the P3P doc flow exactly (done in §3.2).

### 9.4 Field evidence: 2 calls today (highest value, lowest cost)
1. **The carpenter crew lead** (10 minutes):
   - jobs per day;
   - % of jobs that needed a second visit, and why (part? diagnosis? customer absent?);
   - who buys the parts and at what markup;
   - how long a parts run takes in Eluru;
   - would they accept a job card with photos and a pre-sent part?
2. **One Eluru parts shop:** do they keep a stock list? Would they answer a call from an AI or reply to an SMS to hold a part? Do they have a card/UPI terminal?

These fill in the §4 business-case formula and support the "voice as the API for informal shops" idea.

### 9.5 Log everything
Keep this Claude conversation and your other AI chats; submit the links. **Write the final answers in your own words**, because the logs are used to weigh human vs. machine contribution.

---

## 10. Foundation for Round 3: a log of where the rails bend or break
Start now and add every test result. Round 3 is *"where India's agentic infrastructure bends and breaks, and what should change."*

| # | Rail | What we tried | What happened | Bends or breaks? | Recommended change | Source |
|---|---|---|---|---|---|---|
| 1 | Gnani | Mid-call API response | Docs contradict (WIP vs. supported) | ? | Clarify / ship response variables | [V] → G2 |
| 2 | Gnani | Machine sound as evidence | Noise filter built to suppress it | Bends | Raw non-speech capture mode | [V] → G5 |
| 3 | Pine Labs | Pay only after physical proof | P3P captures on an HTTP retry, not on a real-world event | Breaks | Event-conditioned capture | [V] |
| 4 | Pine Labs | Child pays for parent | No delegate concept | Breaks? | Delegate-payer mandate | [T] → test |
| 5 | Pine Labs | Revoke a mandate | Undocumented | ? | Documented revocation | [V] |
| 6 | Delhivery | Deliver a part to a technician before a job | Address-only consignee | Breaks | Appointment-bound delivery to a person | [T/V] |
| 7 | Delhivery | Batch 4 jobs by skill + window | Matrix only, no solver | Bends | Constraint-based multi-stop solver | [T] |
| 8 | All | Commit technician + part + window as one | No rail owns it | **Breaks** | Co-arrival / Work rail | Headline |

---

## 11. Decisions
**Made (24 Sep):**
1. ✅ **Level:** L4, with L3 money limits.
2. ✅ **Who the agent serves:** two-sided, one repair case (household guardian + agency copilot).
3. ✅ **Tests:** the team will run Gnani G1–G8, Delhivery Maps MCP, the carpenter crew call and the Eluru parts-shop call.

**Still open:**
4. **Fourth rail:** Machine Passport (recommended, §6.7) or Capacity rail (runner-up).
5. **Q5 / Q8 companies:** Servify (fourth rail) + Urban Company (whole agent, consistent with Round 1). Verify the Servify claims.
6. **Name:** Tayyar / SahiVisit / other.
7. **Who runs which test, and by when.** Aim for Friday afternoon so there's time to write the answers.
