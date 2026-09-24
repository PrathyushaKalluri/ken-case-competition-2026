# Round 2: One Vision, Eight Strategies

**Team TripleIT · Opening 11 · Due Fri 25 Sep 2026, 11:59 PM IST**
Supporting research: `round2_strategy.md` (API notes, ideation, tests) · `phase2_research.md` (rail chain)

---

## THE VISION

> ### **Every technician visit arrives ready.**
> **Tayyar** makes sure the right technician, the right part and a ready household meet in the same time window, so the first visit is a repair, not a discovery.

**What that one line means, in three parts** (every answer below comes back to one of these):

| | For the household | For the technician / agency | For India's rails |
|---|---|---|---|
| **The problem** | Every extra visit is another day of waiting and disruption (our Round 1 insight) | Discovery visits and parts runs waste paid hours | Voice, money and parcels each work, but **nothing commits a person, a part and a time window as one unit** |
| **What Tayyar does** | Gathers the evidence before anyone comes; pays only within the household's limit | Sends a prepared job: a known machine, a likely fault, the part in hand | Joins Gnani, Pine Labs and Delhivery around one repair case |
| **What's still missing** | — | — | **A Machine Passport**: truth about the machine that no rail holds |

**The story in one breath:** *People protect their routine, so the first visit shouldn't be for discovery (Round 1). To make that happen, the part, the person and the household have to arrive together, and no rail can promise that today (the headline gap). Tayyar promises it, pays only within the household's limits, and gets better with every repair because each one builds a Machine Passport (the fourth rail). Households lose one day instead of a week, and agencies turn wasted visits into paid jobs.*

**The through-line, from question to question:**
Q1 is the outcome (a machine working after a prepared visit) → Q2 is the autonomy the agent needs to deliver it → Q3 is how it stays on track when things fail → Q4 is what each rail gives and lacks → Q5 is the missing truth about the machine → Q6 is how real people use it → Q7 is the name that carries the promise → Q8 is who could get there first, and why they haven't.

**Three rules for every answer:**
1. **Use the vision's words:** "ready," "first visit," "the part, the person and the household together." Judges should hear the same idea eight times.
2. **Put one piece of our own evidence in each answer:** an interview quote, a test-call result, a crew number, or an exact endpoint. The AI baseline can't have these.
3. **Keep the owner of every action clear:** Gnani transcribes, *we* diagnose. Delhivery gives travel times, *we* match technicians. Pine Labs caps amounts, *we* check scope.

---

## Q1. What outcome is the agent accountable for? (one sentence)

**What the judges are testing:** whether the outcome is checkable, and whether the agent owns a *result* or just an activity.
**Strategy:** name a checkable end state (a functional test passes) plus the two things the household protects (their routine, measured as visits, and their money, measured as the limit). This sentence is the promise every later answer has to deliver on.
**Trap to avoid:** activity words ("helps," "coordinates," "books"), or promising one visit even for faults that truly need an inspection first.

> **Draft:** *"A household's broken appliance is confirmed working by a functional test, on the first technician visit wherever the fault allows, without spending more than the household approved."*

Keep in reserve (for follow-up questions or Round 3): how we'd measure it. The first-visit fix rate counts every case, including honest diagnostic visits. Also: hours from report to repair, and follow-up calls the household had to make.

---

## Q2. Autonomy level (L1–L4)

**What the judges are testing:** do we know the level is set by *the most consequential thing done without asking*?
**Strategy:** claim **L4** (it owns the outcome end to end, which matches Q1) and immediately **bound it with L3 money limits**. Name the single riskiest unasked action. Give a short "acts alone / always asks" list. Say when it deliberately drops a level.
**Trap to avoid:** claiming L4 and then listing ten approvals, which reads as L2. Keep the ask-first list short and principled: **money above the limit, people through the door, machines out of the house, risk to life.**

> **Draft:** *"L4. Tayyar owns the repair from report to a passed functional test. It plans the visit, sources and ships the part, books the technician, re-plans when a part is late or a technician doesn't show, and checks its own work before closing. The most consequential thing it does without asking is spend inside the limit the household approved in their UPI app: the visit fee, the part and the labour. It always asks before any spend above that limit, a technician entering the home, the machine leaving the home, or risky work. For life-critical devices (such as an oxygen concentrator) it drops to L2: it prepares everything and a human decides."*

---

## Q3. States: happy and unhappy flows

**What the judges are testing:** thoroughness and realism. The organiser's email said it directly: *imagined failures are the polite ones.*
**Strategy:**
1. **One state machine** with a **"Ready gate"** at its centre (the vision as a state). The visit is only confirmed when address ✓, skilled technician ✓, part ✓ and household present and consenting ✓.
2. **Unhappy flow in two layers:** (a) failures **found in our own Gnani test calls** (label them "found in testing"); (b) failures from **our interviews** (wrong part, price creep, no-show).
3. For each failure give **how the agent detects it → what it does → which state it ends in**. Never end in silence.

**Happy flow:**
```
1 Reported (voice/photo) → 2 Machine known (label, Passport) → 3 Evidence ready (symptoms, code, sound)
→ 4 Limit approved (UPI) → 5 Planned (technician + part + slot held) → 6 READY GATE ✓ (all four meet)
→ 7 On site → 8 Repaired → 9 Functional test passed → 10 Settled (capture ≤ limit, release rest)
→ 11 Closed (Passport updated)
```

**Unhappy flow** (fill in the G-rows from tomorrow's calls):

| Failure | Detected by | Agent does | Ends in |
|---|---|---|---|
| Evidence too thin | Low diagnosis confidence | One more question or video; else a diagnostic visit, **honestly labelled** | 4 |
| Code or model misheard | Read-back not confirmed | Repeat slowly; keypad entry | 3 |
| *[G1–G8 test findings: code-switching, silence, talking over, noise, conditional promise]* | *call log* | *…* | *…* |
| Part late or lost | Delhivery tracking push / failed delivery | Release the slot; van stock or local shop; reattempt; new window | 5 |
| Technician no-show | No check-in by window + tolerance | Reassign; tell the household | 5 |
| Wrong or extra fault found on site | Technician tells the household in person, then **reports it to Tayyar by voice** (Telugu call from his job card: part + price, read back, press 1; photo by SMS link). Accepted only from the assigned technician's number. | Checks the usual price range, remaining limit and approved scope. Small and in scope → auto-approve. Otherwise → payer approves in their UPI app (a Gnani call first if the payer is remote). Declined → visit fee only. **The technician's voice is a claim, never an approval.** | 8 or 10 |
| Part or price misheard on the technician's call | No keypad confirmation of the read-back | Repeats; asks for the amount on the keypad | 7 |
| Payer unreachable | Approval timeout | No work beyond scope; hold the slot, then re-book | 4 |
| Payment times out | No receipt | Look up the original order reference **before** retrying (no double charge) | 10 |
| Repair fails the test / dispute | Failed test or complaint | Hold capture; re-visit; partial refund | 9 |
| Caller distressed / technician abused | Negative-sentiment handoff (Gnani Workforce) / technician's "unsafe" button | Human callback; move the job up; visit fee protected | human |
| Life-critical device | Device class from the label | Human now; backup device first | human (L2) |

---

## Q4. Each rail: what exists vs. what must be built

**What the judges are testing:** did we read the docs (endpoints, what comes back), and can we name the gaps precisely?
**Strategy:**
1. **Open with the headline:** *"None of the three rails has a concept of a person."*
2. For each rail: **what we call (endpoint → what it returns) | what's missing (in the shape we need) | what we do meanwhile.**
3. **Logistics goes deepest**, because it's the rail we chose to innovate on in Round 1. The co-arrival ask to Delhivery is our depth piece.
4. End each rail with **one precise ask** to its owner (these ideas get tested in Round 3).

**Trap to avoid:** crediting our own logic to a partner, or listing fifteen gaps with no headline.

> **Draft (compress to fit the form):**
>
> **The headline: none of the three rails has a concept of a person.** Nothing commits a technician, a part and a customer's time window as one unit, and that's why the first visit so often ends up being for discovery.
>
> **Voice (Gnani).**
> - *Uses:* Agent Builder phone agent in Telugu/Hindi/English; STT `POST /stt/v3` → transcript (clips ≤60 s) and streaming; TTS `/tts/inference` reads back amounts and codes; DTMF keypad capture; on-call custom HTTP actions to our backend; post-call logs and recordings; Workforce handoff to a human on negative sentiment.
> - *Missing:* (1) Machine sound as evidence: the background-noise filter removes exactly the grinding or clicking we need. (2) Photo input: agents take only text or number variables, so the model label can't be captured by voice. (3) Any way to tell a firm technician promise from a conditional one ("I'll come after 5 if the part arrives").
> - *Meanwhile:* our own sound classifier on call recordings; an SMS link for photos; read-back plus "press 1 to confirm."
> - *[Add one test finding here.]*
>
> **Payments & Authorisation (Pine Labs).**
> - *Uses:* P3P: the household approves a UPI One-Time Mandate or Reserve Pay block by QR in their UPI app (`POST /mpp/v1/mandate`); Grantex scope `mpp:payment:max_txn_paise` caps each charge; the agent pays through the 402 challenge → `P3P-Credential` → `Payment-Receipt` flow; `GET /mpp/v1/balance` shows what's left; capture below the blocked amount; refunds; split settlement to the agency and parts shop.
> - *Missing:* (1) **P3P pays for a digital request; there's no capture that fires on a real-world event** (a part-delivered scan, a passed test), so the agent must either pay before proof or ask every time. (2) Limits cover amount only, not merchant or repair scope. (3) No delegate payer (a child in another city approving for a parent at home). (4) Revocation isn't documented.
> - *Meanwhile:* our backend waits for the event, then captures; we run our own scope check; the approval goes to the payer's number.
>
> **Logistics (Delhivery), our innovation rail.**
> - *Uses:* Maps geocoding for messy Indian addresses; distance matrix (two-wheeler) to rank technicians by travel time; pincode serviceability; forward and reverse shipments; tracking push webhook; failed-delivery actions.
> - *Missing:* **Delivery goes to an address, not to a person by a deadline.** There's no technician, skill, slot or job anywhere, and no multi-stop batching by skill and time window. **Our ask: appointment-bound delivery.** Consignee = a technician, deadline = job start minus a buffer, and an "at risk" webhook.
> - *Meanwhile:* our Ready gate confirms a slot only after the delivered scan; our own matcher (skill first, then travel time); batching only when every customer's window survives.

---

## Q5. A fourth rail, and which Indian company should build it

**What the judges are testing:** can we spot missing infrastructure, specify it, and reason about who builds it?
**Strategy:** start from the **business problem**. Round 1's business move was fewer visits, and wrong diagnosis or the wrong part is the root cause of extra visits. The fourth rail is the one piece **no partner will ever own: truth about the machine.** Use the India-stack analogy (Aadhaar for people, FASTag for vehicles, nothing for household machines) and the Right to Repair policy direction. Sketch 3–4 endpoints. Say what we do meanwhile.
**Trap to avoid:** a "WhatsApp rail" or a "data rail" (these already exist, or are too vague), or repeating the Q8 company.

> **Draft:** *"Yes: a **Machine Passport** rail. Voice, money and movement exist; truth about the machine does not. Every repair today starts from zero: the technician asks the model, guesses the fault, and often fetches the right part on a second visit. The rail gives each appliance a permanent, consented ID (serial or QR) holding its model, warranty, past repairs, parts fitted and test results, readable by any technician or agent the household authorises (`resolve machine`, `get history`, `record repair`, `check warranty`). Our agent would know the machine before the phone rings, ship the exact part, and give a local technician the verified track record a brand service centre has. We'd want **Servify** to build it, since it already connects brands, service centres and logistics. Until then, Tayyar builds each passport one repair at a time from label photos and technician job cards."*

*(Check Servify's current scope before submitting.)*

---

## Q6. How a human interacts with the agent

**What the judges are testing:** specificity. Real people, real moments, real channels.
**Strategy:** describe **one repair told as moments**, then list **each person's interface**. Include the insight that sets us apart: **the person using the machine and the person paying for it are often different people** (a parent at home, a child in another city). Make it voice-first for older users. The agency sees exceptions only.
**Trap to avoid:** "a mobile app with a chatbot."

> **Draft:**
> - **Household (often an elderly parent):** calls or is called by Tayyar in Telugu, Hindi or English. It asks short questions, reads back every code and amount, and texts one link to upload the model-label photo and a 10-second sound clip. Updates arrive in the same thread: technician's name and photo, arrival window, "your part has reached him." The call ends with a functional test: *"Is it running? Say yes or press 1."*
> - **Payer (often an adult child elsewhere):** approves one plain limit in their UPI app ("Tayyar can never spend more than ₹3,000") and gets a timeline. Any higher amount goes to their UPI app, never to a voice "yes."
> - **Technician:** one job card by WhatsApp or SMS: the evidence, likely cause, part marked "with you / arriving 2 PM," the customer window, check-in, a "stop: unsafe" button, and a test-video upload. **Everything works by voice:** if he finds another fault, he explains it to the household in person, then presses "Call Tayyar" and says in Telugu, "capacitor burnt, ₹650." Tayyar reads it back, he presses 1, and the payer approves in UPI. No typing and no app to learn. Paid as soon as the test passes, and only logged work carries the repair warranty.
> - **Agency owner:** an exception queue only (no-show, wrong part, dispute, life-critical), plus a daily count of visits saved.
> - **Parts shop:** needs no app. Tayyar phones them, asks for stock in Telugu, holds the part, and pays through Pine Labs.
> - **Anyone upset or who can't use voice:** "Talk to a person" always works; there's a text channel for those who can't speak or hear.

---

## Q7. Name

**Strategy:** one word, easy to say on a phone call, carries the vision.

> **Draft:** ***Tayyar*** *(ready): the technician arrives ready, the part arrives ready, the household is ready.*

Backups: SahiVisit, PehlaFix. Check that Tayyar sounds natural in Telugu, and check for name clashes.

---

## Q8. Which Indian company has the best chance of building an agent like this

**What the judges are testing:** understanding of incumbents: their assets, incentives, and why they haven't built it yet.
**Strategy:** **stay consistent with Round 1 (Urban Company) but go deeper.** Name the assets it has for **each rail** and **the one it lacks** (the Machine Passport). Then the incentive tension: its model earns on owning the visit, so it would build a *closed* version for its own technicians, not one that makes independent local agencies ready. That's the gap we fill.
**Trap to avoid:** repeating the Round 1 text, or stating unverified user numbers.

> **Draft:** *"Urban Company. It already runs most of what Tayyar needs: households booking by app, a trained technician network with skills and schedules, in-app payments, and a service record for every job. The missing pieces are truth about the machine (every booking still starts from the customer's description) and parts arriving with the technician. Our bet is that it will build a closed version, where its own technicians arrive ready. Its model earns on owning the visit, so it has no reason to make the local agencies and independent technicians that most Indian households still call arrive ready. That open, agency-friendly version is Tayyar."*

---

## Tomorrow's plan (Friday)

| Time | Task | Feeds |
|---|---|---|
| Morning | Gnani G1–G9 test calls (screenshots and notes). **G9:** a technician-style call from a noisy spot (machine or TV running) with Telugu-English part names ("capacitor", "PCB", "inlet valve") and amounts ("six-fifty" vs "sixteen-fifty"); do the part and amount come through, and does keypad confirmation work? **G2 matters more now:** if a backend reply can't be spoken back during the call, the fair-price flag has to go by SMS afterwards. | Q3 unhappy rows, Q4 voice, Q6 technician |
| Morning | Carpenter crew call (second-visit %, reasons, parts markup) | Q1 measure, Q5 business case, Q8 |
| Morning | Eluru parts-shop call | Q6 parts shop, Q4 logistics |
| Midday | Delhivery Maps via MCP: geocode an Eluru address + distance matrix | Q4 logistics |
| Afternoon | Rewrite every draft **in your own words**; add one piece of our own evidence per answer | All |
| Evening | Check form limits; paste; attach the AI chat links; submit **before 9 PM** as a buffer | — |
