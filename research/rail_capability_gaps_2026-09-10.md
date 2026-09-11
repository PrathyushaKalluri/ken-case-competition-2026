# Rail capability gaps — verified 2026-09-10

Research pass run for Q4/Q5. Every claim below is either sourced or explicitly marked unverifiable. **Nothing here should be asserted to a rail partner without the caveats attached.** This file matters beyond Phase 1: if the team is shortlisted on 15 Sep, the rails round is exactly this conversation with Pine Labs, Gnani and Delhivery.

---

## 1. Payments — Pine Labs P3P / Grantex

**What exists.** P3P launched 11 June 2026, extending UPI's existing mandate rails (One Time Mandate + Reserve Pay) so an agent can browse, negotiate and pay within a pre-authorised mandate. Grantex adds identity, delegated authorisation, spend caps, audit trail. HTTP 402 for payment discovery. Live with Gullak; PoC with Vijay Sales; L&T Finance PLANET announced at GFF 2026.

**What does not exist, per public documentation:**

| Capability | Status |
|---|---|
| Escrow | Not documented anywhere |
| Conditional hold | Not documented |
| Milestone release | Not documented |
| Service-quality dispute / chargeback | Not documented |

**Nearest primitive is NPCI UPI Reserve Pay (Single Block Multiple Debits), and its constraints disqualify it for household services:**
- **P2M only** — "verified online merchants"
- **Max block ₹10,000, up to 90 days**
- One block per merchant per customer
- Merchants "must ensure instant debit before delivery" — **debit *before* service, the inverse of escrow**

**Paying a non-onboarded individual: effectively impossible.** UPI mandates are P2M constructs requiring a verified merchant. NPCI **sunset UPI Collect effective 28 Feb 2026** — customers can no longer initiate payments *or register mandates* by typing a VPA, UPI ID or mobile number. Whether NPCI's small-merchant **P2PM** category can carry a mandate: **not verifiable.**

**The sharpest single gap — mid-transaction re-authorisation.** Any modification to a UPI mandate (amount or validity) **requires the human's UPI PIN**. The moment a repair's scope or price changes after work starts, autonomy collapses and the customer must be present with their phone.

**Disputes.** UPI chargebacks exist for P2M via URCS/UDIR — capped at 10 per customer/30 days, 5 per payer-payee pair — covering credit-not-received and cancelled/returned goods. **No deficiency-of-service quality chargeback.** P2P is effectively irrevocable once funds move.

> ⚠️ **`grantex.dev` and `github.com/mishrasanjeev/grantex` are an UNRELATED project. Do not cite them as Pine Labs' Grantex.** Pine Labs' Grantex has **no public developer documentation**. The only safe citation for what Grantex does is the competition page's own wording.

## 2. Regulatory — why consumer escrow-for-services is genuinely hard

Four independent constraints. **This is the strongest material in this file**, because a capability missing for regulatory reasons is a finding, not a feature request — and the competition page says Round 2 is about "testing the limits of India's agentic infrastructure, where it bends and breaks, and making recommendations about what needs to be changed and why."

1. **Only a licensed PA may hold third-party funds, and only in a bank escrow.** RBI (Regulation of Payment Aggregators) Directions 2025, dated 15 Sept 2025: non-bank PAs must hold collections in escrow with a scheduled commercial bank, deemed a "designated payment system" under **s.23A, Payment and Settlement Systems Act 2007**. Escrow credits and debits are a closed list. Non-banks (Castler, Escrowpay) orchestrate only; banks custody.
2. **The escrow presupposes an onboarded, KYC'd merchant.** A neighbourhood carpenter on a personal VPA is not one. The 2025 Directions add a turnover-based proportionality carve-out (CKYCR-first, PAN/contact-point verification for small merchants) — **cite this as the narrow legal path, not as an existing product.**
3. **UPI's own hold primitive is capped** — see §1.
4. **NPCI has publicly ruled out agent-approved payments.** At GFF on **10 Sept 2026**, NPCI director Ajay Kumar Choudhary said AI agents *may recommend* UPI payments but **authentication and final settlement must remain deterministic and auditable**. NPCI's Unified Agent Protocol leans on UPI Circle Full Delegation limits (**₹15,000/month, ₹5,000/transaction**), targets low-value high-frequency use, is **unconfirmed and pending RBI approval**, liability unresolved.

Card fallback is also weak: India's tokenisation rules permit card-data retention for pre-auth/delayed capture for **only 4 days**.

**Concrete against our own evidence:** Rk Sir's ₹3,000–4,000 chemical wash fits under the ₹5,000/transaction UAP cap. A ₹7,800–9,000 compressor replacement does not.

## 3. Voice — Gnani

Full 94-page doc index at `docs.gnani.ai/llms.txt` read directly.

- **Consumer-side outbound: not documented.** Only outbound endpoint is Trigger Test Call — **whitelisted numbers only**, registered via an account manager, explicitly "for testing, not production campaigns." Docs state: *"Currently, Gnani Agents does not have a built-in campaign manager."* Every framing is enterprise → its own customers.
- **Third-party IVR navigation: not documented.** The sole DTMF page is **inbound digit capture**. No DTMF emission, hold detection, or phone-tree traversal.
- **Cross-call memory: not in the docs.** Zero hits for "memory", "cross-session", "context persistence". Only per-call variables, a static KB, read-only logs. Marketing blogs claim persistent memory but are 403-blocked and unsupported by any API — **unverified**.
- Telephony: Twilio number import, Webex CC, LiveKit/Pipecat. **No SIP trunking, no call transfer.** Zero mentions of TRAI or DLT. TCCCPR/DLT structurally requires commercial outbound via a registered telemarketer on 140/160 series; whether a *consumer's personal agent* falls in scope is **not resolved by any TRAI text — not verifiable.**

### Can a Gnani voice session bind a visual artifact mid-call?

**Not in the documentation.** The index has SMS, Email, CRM, Ticketing and Custom Integrations — so an agent *can* fire an SMS mid-call — but **no page on images, photos, video, media, attachments, file upload, WhatsApp, multimodal or vision.** The only file-upload surface is batch STT ingest of *audio*. Gnani markets "multimodal AI agents" on its blog, but those pages 403 and nothing in the API corroborates them. **Treat the multimodal claim as unverified marketing contradicted by the docs.**

**⚠️ This answer has a live competitor.** VocaLoop markets precisely mid-call photo capture — a form generated at runtime, sent over WhatsApp/SMS, answers "injected back mid-call," collecting ID and document photos. Caveats: pure marketing, no case studies or deployment evidence, and **VocaLoop's provenance is not verifiable as Indian** (it is *not* VocalLabs, Bengaluru). Adjacent Indian vendors advertise mid-call *link* actions (payment links, V-CIP via Hyperverge/IDfy/Signzy) — document capture via a KYC vendor, not a general proof primitive.

**Consequence for Q5:** the broad claim *"no voice stack can receive a photo mid-call"* is **falsifiable — do not make it.** The defensible narrowing is that **capture exists but evidentiary binding does not**: nothing in any documented stack ties a photo to the specific spoken claim it evidences, timestamps it against that utterance, and carries it forward as a disputable record into a later call or payment decision. **Verify this with a Gnani engineer rather than asserting it.**

## 4. Logistics — Delhivery Maps / MCP

Endpoint `gateway-maps-pub-int.delhivery.com/mcp`, **exactly 9 tools**: `geocode_address`, `reverse_geocode`, `standardize_address`, `validate_address`, `verify_address`, `auto_suggest`, `route`, `compute_distance_matrix`, `calculate_tolls`, plus Map Tiles and tolls-by-polyline in the REST reference.

**Absent: serviceability, ETA, tracking, rate calculation, manifest, shipment creation.** The MCP surface is **read-only — nothing can book, manifest or cancel a shipment.** Auth is a browser-session-derived bearer token; no published rate limits, quotas, pricing or SLA; `/reference/authentication` and `/reference/overview` return 404. No public GitHub repo or MCP-registry listing.

- **Routing to a person rather than an address: not documented.** Consumer app accepts lat/long or Plus Codes — a static point, not a live handoff.
- **Same-day part to a technician in transit: not documented.** Same-Day Delivery covers 15 cities, 3pm cutoff, dependent on pre-stocked in-city SKUs. Delhivery Direct is hyperlocal intracity, Delhi-NCR and Bengaluru only. No public booking API.

**Conclusion: logistics cannot be the innovation rail.** It can hold a supporting role in Q4 only.

## 5. Spare-part warranty — the "3 months" claim is NOT defensible as stated

Amma [17:30] says a genuine part carries ~3 months warranty and a duplicate also survives ~3 months, so "we won't know if the part is duplicate or original." **There is no single Indian norm:**

| Model | Example | Effect on replaced part |
|---|---|---|
| Tiered by part | LG India | 3 mo floor / 6 mo / 12 mo |
| Flat 90 days | Samsung India (self-repair parts) | 90 days from delivery |
| Inherits remainder only | Bosch India (**in-warranty repairs only**) | no fresh period at all |
| Explicitly none | Blue Star | "shall not carry any fresh warranty" |
| Silent | Urban Company, Whirlpool, Voltas, Godrej, IFB, Haier, Onsitego, OneAssist, Servify | undisclosed |

**Defensible version:** where a figure is published at all, 90 days is the floor; most players publish nothing; at least two OEMs grant no fresh warranty on a replaced part.

**The "warranty window = counterfeit survival window" observation remains undocumented anywhere** — genuinely original to this interview, but an *interview hypothesis, not a citable fact*. It is weakened from two directions: LG's 6/12-month tiers cover exactly the high-value parts most worth faking, and Bosch/Blue Star mean there is sometimes no 3-month window at all. **If used, scope it explicitly to the unorganised/local-technician channel the interviews actually cover, where no published warranty exists** — which is the more honest and stronger framing anyway.

---

## Ranked "we genuinely don't have that" candidates

1. **Mid-job mandate re-authorisation without the human's UPI PIN** — regulatory, not merely unbuilt. Maps directly onto the strongest interview finding (price set after work starts).
2. **Conditional/milestone hold above ₹10,000 to a non-onboarded individual payee** — and note this is exactly the team's own supply-side contacts.
3. **Service-quality dispute recourse on UPI.**
4. **Evidentiary binding of a visual artifact to a spoken commitment** (narrowed; verify with Gnani).
5. **A delivery primitive addressed to a moving person.**
