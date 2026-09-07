# Keeping the Machines Running — Master Context File

**Project:** The Ken Case Competition 2026  
**Selected opening:** **Keeping the machines running**  
**Purpose of this file:** Give any future teammate, mentor, or AI enough context to continue the work without needing the full chat history.  
**Working ambition:** Do not merely qualify. Build a finalist-/winner-level submission with unusually strong evidence, a non-obvious insight, and a believable end-to-end agent that actually resolves household maintenance problems.

---

## 1. The selected problem

The selected case is **Keeping the machines running**.

### Source problem, in plain English
Urban households increasingly own many machines and service-dependent assets, but the management layer around them is fragmented. Each appliance has its own purchase record, warranty, AMC, service centre, technician, spare parts, service history, and escalation process. The household manually stitches this together.

### Evidence from the supplied case material
The supplied case describes:
- a water purifier installation involving a decision-tree chatbot, a service-centre call, a service-agent call, OTPs, and feedback forms;
- an AC repair turning into a multi-day tenant-vs-landlord coordination issue;
- carpenters and plumbers who must be chased repeatedly;
- lift AMC follow-ups depending on residents;
- households juggling multiple service providers simultaneously;
- people remembering purchase dates, warranty periods, technician numbers, and service dates themselves.

The strongest summary from the case is that households behave like **dispatch desks** for the machines they own.

### Demographic caution
Age-group rankings must be treated separately from overall case attractiveness. Never infer cohort strength from the overall business case. Use only the actual cohort evidence supplied in the demographic graphs.

---

## 2. Competition strategy

### Core rule
**“Best overall case” and “best case for an age group” are separate rankings.**

For the selected case, however, the work now shifts from case selection to **winning execution**.

### What is likely to separate a winning submission
The submission should excel on five dimensions:
1. **Evidence** — real behaviour, not hypothetical preference.
2. **Creativity** — a second-order insight, not a restatement of the prompt.
3. **Clarity** — one simple story and one clear wedge.
4. **Feasibility** — believable actions, boundaries, and exception handling.
5. **Thoroughness** — understand the full system: user, service centres, technicians, brands, spare parts, landlords, payments, logistics, and incentives.

### Pattern to emulate from prior strong/winning case submissions
The useful pattern from previous winning/finalist work is not “make a beautiful deck.” It is:
- deeply understand the entire system of alternatives, incentives, risks, and dependencies;
- prove the insight with evidence;
- choose a narrow wedge;
- show why the proposed product can actually operate in the real ecosystem;
- explain trade-offs and what the product deliberately will **not** do.

The current project should follow this standard.

---

## 3. The current strategic thesis

### Working thesis
> **The household has become the integration layer for an industry that never integrated itself.**

The problem is not simply that people forget service dates.

The deeper problem may be that every household asset creates a fragmented operational workflow:

**invoice → warranty → diagnosis → service centre → technician → scheduling → parts → payment → follow-up → closure**

The user becomes the person responsible for connecting all these steps.

### Strong product framing
> **Tell the agent what is wrong. It owns the problem until it is fixed.**

### Product category
**Household Reliability Agent** / **Household Asset Operations Agent**

Names are placeholders. Do not over-invest in naming before the insight is validated.

---

## 4. What NOT to build

If the solution becomes any of the following, it is likely too shallow for a winning case:
- appliance reminder app;
- digital warranty wallet;
- technician marketplace;
- “Urban Company but with AI”;
- generic troubleshooting chatbot;
- home-management dashboard;
- nearby-technician finder;
- AMC reminder system;
- app that only stores bills and warranty dates;
- chatbot that merely tells the user whom to call.

Any of these may be useful **features**, but none should be the main thesis.

---

## 5. The high-bar product vision

### Example trigger
User says:
> “My water purifier is leaking again.”

The agent already knows, or can recover:
- brand and model;
- serial number;
- purchase date;
- warranty status;
- invoice;
- last service;
- previous issue;
- parts replaced;
- preferred service route;
- household availability;
- user-authorised spend limits.

### Desired behaviour
The agent should:
1. understand the issue;
2. identify the relevant appliance;
3. assess urgency and safety;
4. determine warranty / AMC / ownership responsibility;
5. select the best resolution route;
6. contact the provider;
7. create the service request;
8. coordinate schedule and household availability;
9. follow up automatically;
10. recover from no-shows or failures;
11. coordinate parts if needed;
12. ask for approval only when the user must decide;
13. arrange authorised payment;
14. verify closure;
15. update the asset history.

The experience should reduce the user's job from **running the workflow** to **setting policy and approving exceptions**.

---

## 6. Why this problem fits an agent

The desired agent loop is:

**Observe → Decide → Act → Verify → Recover**

A winning solution should be evaluated against this loop.

If the product only observes and recommends, it is not agentic enough.

### Observe
- user complaint;
- appliance context;
- service history;
- warranty/AMC state;
- missed appointment;
- part-delivery state;
- payment request;
- closure status.

### Decide
- OEM vs AMC vs third-party repair;
- whether user approval is needed;
- whether landlord must approve;
- whether a repair is safe to attempt;
- whether to escalate a missed SLA;
- when to order a part;
- whether a quote is suspicious or outside authority.

### Act
- call service centre;
- navigate IVR;
- book/rebook;
- send evidence;
- arrange logistics;
- make authorised payment;
- escalate;
- message household members.

### Verify
- technician actually arrived;
- repair actually happened;
- right part was installed;
- amount charged matches approval;
- issue is resolved.

### Recover
- technician no-show;
- wrong technician;
- part unavailable;
- provider refuses warranty;
- quote exceeds budget;
- issue reappears;
- landlord refuses responsibility;
- service request incorrectly closed.

---

## 7. The three rails

The competition should not show the rails as decorative integrations. Each rail must solve a real bottleneck.

### A. Voice rail — potentially the strongest rail
Voice should **not** merely mean “the user talks to AI.”

The strongest use is:
> **The agent talks to service businesses for the user.**

Possible actions:
- call OEM support;
- navigate IVR;
- create a ticket;
- explain symptoms;
- confirm model and warranty;
- schedule technician;
- chase missed visits;
- escalate unresolved cases;
- confirm completion;
- call landlord/property manager where relevant.

A powerful demo would show the agent handling a service-centre call and then recovering from a no-show without asking the user to restart the process.

### B. Payments & authorisation rail
Do not use payments merely as checkout.

The interesting concept is **delegated authority**.

Example:
> “You may approve routine repairs up to ₹1,500 without asking me. Anything above that requires approval.”

Then:
- ₹850 capacitor replacement → can proceed if policy allows;
- ₹7,800 compressor replacement → pause and request approval.

Potential rules:
- spend cap by appliance/category;
- OEM-only under warranty;
- landlord approval required for landlord-owned assets;
- payment only after agreed milestone;
- quote tolerance range;
- explicit approval for high-risk repairs.

### C. Logistics rail
Use logistics only where physical movement genuinely exists:
- spare parts;
- replacement filters;
- consumables;
- failed-device pickup;
- replacement device;
- warranty returns;
- reverse logistics.

A strong workflow is:
**diagnosis → compatible part → delivery → technician visit**

This can eliminate wasted technician visits caused by missing parts.

---

## 8. The key discovery objective

Do **not** conduct research merely to validate the current thesis.

The objective is to discover something the supplied case material did not already tell us.

### The bar for the main insight
Weak:
> People hate chasing technicians.

Still weak:
> People forget warranties.

Better:
> Most frustration happens after the first service request, not before it.

Stronger:
> The real failure is not service discovery; it is multi-party coordination after diagnosis.

Potentially winning:
> A specific, quantified mechanism that explains where the coordination burden accumulates and why current systems cannot remove it.

The best final insight must come from the actual fieldwork.

---

## 9. Research design

### Target research volume — high-bar recommendation
These are internal quality targets, not competition requirements.

#### Consumer side
- **35–50 deep household interviews**
- ideally **75–150 reconstructed service incidents**

Each participant should discuss at least the most recent incident and, where possible, the one before that.

#### Supply side
Aim for roughly:
- **8–12 technicians/service professionals**;
- **5–8 service centres / appliance-service operators / OEM-side personnel**, if accessible;
- **5–10 landlords, property managers, RWAs, or building operators** where relevant.

The exact sample can change based on access and signal saturation.

---

## 10. Who to recruit

Recruit for **behavioural diversity**, not just demographic variety.

Useful household segments:
- renters;
- homeowners;
- people living with parents;
- people managing parents' homes remotely;
- families with multiple appliances;
- apartment residents;
- people with recent AC/purifier/washing-machine/fridge repairs;
- people using OEM service;
- people using local technicians;
- people with active AMCs;
- people with expired warranties;
- households with domestic staff who coordinate visits;
- households where one person is the “default operations person.”

Supply-side segments:
- OEM-authorised technician;
- independent electrician/plumber/repair technician;
- appliance service centre;
- spare-parts seller;
- building maintenance manager;
- landlord/property manager;
- home-services marketplace professional.

---

## 11. Interview method

### Never ask first
- “Would you use an AI agent?”
- “Would you pay ₹500?”
- “Do you want reminders?”
- “Would this feature be useful?”

These produce weak evidence.

### Start with the last real incident
Ask:
1. Tell me about the last appliance or machine problem you had.
2. What happened first?
3. What did you do next?
4. Who did you contact?
5. How did you find that person/provider?
6. How many times did you call/message?
7. Did someone come when promised?
8. What happened during the visit?
9. Was the issue resolved on the first visit?
10. Did a part have to be ordered?
11. Who decided whether the price was acceptable?
12. Did you know whether it was under warranty?
13. Did you have the invoice available?
14. Did a landlord/parent/spouse/other person need to approve anything?
15. How did you pay?
16. What happened after the technician left?
17. Did the issue recur?
18. What part of the process was most annoying?
19. What part took the most time?
20. What did you personally have to remember?

Then ask:
> “Tell me about the incident before that.”

This reveals repetition and stable patterns.

### Evidence request
Where participants are comfortable, ask to see:
- WhatsApp threads;
- call logs;
- service tickets;
- invoices;
- warranty cards;
- AMC messages;
- technician chats;
- screenshots;
- payment receipts;
- notes/reminders.

The project should build an anonymised evidence library.

---

## 12. Supply-side interview questions

Ask technicians/service centres:
- Why do visits get delayed?
- Why do technicians miss appointments?
- Why do customers need to repeat context?
- What information is usually missing before a visit?
- What causes second visits?
- How often is the correct spare part unavailable?
- How are jobs assigned?
- How are warranties verified?
- What makes a customer difficult to serve?
- What makes a service request easy to resolve?
- Why are tickets closed incorrectly?
- How are quotes created?
- What creates payment disputes?
- What causes technicians to avoid certain jobs?
- How much time is wasted coordinating with customers?
- What would help you resolve more jobs on the first visit?

This is essential because the winning solution must understand **both sides of the system**.

---

## 13. Build an incident-level dataset

Create **one row per real service incident**.

Suggested fields:
- incident_id
- respondent_id
- respondent_segment
- age_band
- city
- renter/homeowner
- asset_type
- brand
- model
- asset_age
- ownership (self/landlord/family/society)
- warranty_known (Y/N)
- warranty_status
- AMC_status
- trigger/problem
- urgency
- first_action
- provider_route (OEM/AMC/local/marketplace/etc.)
- people_contacted
- number_of_calls
- number_of_messages
- number_of_portal_steps
- handoff_count
- repeat_context_count
- active_user_minutes
- calendar_days_to_resolution
- technician_visits
- no_show_count
- resolved_first_visit (Y/N)
- part_required (Y/N)
- part_available_first_visit (Y/N)
- quote_amount
- final_amount
- approval_required (Y/N)
- approver
- payment_method
- dispute (Y/N)
- issue_recurred (Y/N)
- primary_pain
- emotional_language
- workaround
- evidence_available
- outcome

Do not fabricate missing fields. Leave them blank or mark unknown.

---

## 14. Create a “Coordination Tax” metric

A memorable research construct can help the case stand out.

### Coordination Tax — candidate framework
For each incident, measure:

**Human touches**  
Calls + messages + portals + approvals + follow-ups.

**Active effort**  
Minutes of actual human effort.

**Resolution latency**  
Elapsed time from problem reported to verified resolution.

**Repeat-context count**  
How many times the same issue was explained again.

**Handoff count**  
How many entities the user moved between.

**Failure-recovery count**  
How many times the process had to be restarted or escalated.

### Example of the kind of final statement we want
> “The average repair in our sample was not merely a ₹X expense. It was a 9-touch coordination problem.”

The exact numbers must come from research.

---

## 15. Hypotheses to test

These are hypotheses, **not findings**.

### H1 — Post-initiation pain dominates
Most frustration may occur **after** the user has already initiated service: chasing, rescheduling, repeat explanation, parts, and closure.

### H2 — First-visit resolution is a major driver
A significant portion of user effort may come from second/third visits caused by missing context or parts.

### H3 — The user values certainty more than lowest price
Users may accept slightly higher cost if they get a reliable appointment, transparent quote, and verified resolution.

### H4 — One household member becomes the operations bottleneck
A single family member may hold appliance history, service contacts, bills, and follow-ups in their head.

### H5 — Delegated authority is valuable if bounded
Users may be comfortable allowing an agent to autonomously take routine actions below clear spending/risk limits.

### H6 — Landlord/tenant ownership creates a distinct sub-workflow
Renters may face a high-friction approval and payment-allocation problem that homeowners do not.

### H7 — Service providers also suffer from missing context
Technicians may waste time because model, symptom, warranty, address, or part information is unavailable before the visit.

### H8 — The best wedge may be narrower than “all machines”
The strongest initial product may target a subset such as:
- water purifiers;
- ACs;
- high-frequency home appliances;
- rental-house appliances;
- AMC-heavy assets.

Research should determine the wedge.

---

## 16. Candidate ICPs to test

Do not decide the ICP purely from intuition.

Possible initial ICPs:

### ICP A — Urban renters managing landlord-owned appliances
Potential pain:
- ownership ambiguity;
- approval delays;
- vendor coordination;
- repair-cost disputes.

### ICP B — Dual-income urban households
Potential pain:
- low availability for calls and technician visits;
- one partner becomes default household operator;
- willingness to pay for saved time.

### ICP C — Families managing many appliances + AMCs
Potential pain:
- repeated maintenance cycles;
- multiple service providers;
- fragmented warranty history.

### ICP D — Adult children managing parents' households remotely
Potential pain:
- remote diagnosis;
- payment authorisation;
- trusted technician coordination;
- safety/trust.

### ICP E — Premium households with high reliability expectations
Potential pain:
- high value placed on time and certainty;
- may support subscription or membership.

Research should determine which cohort has the strongest combination of pain, repetition, delegatability, and willingness to pay.

---

## 17. Agent state machine — working version

### State 0 — Asset unknown / known
- identify asset;
- retrieve or create asset record.

### State 1 — Intake
- capture symptom;
- assess urgency/safety;
- request only minimum information.

### State 2 — Entitlement & responsibility
- warranty?
- AMC?
- landlord-owned?
- society-owned?
- consumer responsibility?

### State 3 — Resolution-route selection
- OEM;
- AMC;
- trusted local service;
- emergency service;
- replacement/parts route.

### State 4 — Booking
- contact provider;
- create ticket;
- schedule;
- capture commitment.

### State 5 — Pre-visit coordination
- ensure technician has context;
- ensure user/household availability;
- ensure needed part/evidence is available.

### State 6 — Visit
- arrival confirmation;
- diagnosis;
- quote;
- approval if required.

### State 7 — Parts/logistics
- verify compatibility;
- order/track;
- coordinate follow-up visit.

### State 8 — Payment
- evaluate against policy;
- obtain approval if needed;
- release authorised payment.

### State 9 — Verification
- confirm issue resolved;
- capture service outcome;
- capture part warranty/invoice.

### State 10 — Closure
- update asset history;
- schedule future service only if truly needed;
- no further user action.

### Recovery states
- provider no-show;
- service request rejected;
- wrong technician;
- missing spare part;
- quote exceeds authority;
- unsafe condition;
- landlord refuses;
- payment dispute;
- unresolved/recurrent issue.

---

## 18. Guardrails and trust boundaries

A high-quality submission must show where the agent **cannot** act autonomously.

| Risk | Guardrail |
|---|---|
| Wrong diagnosis | Physical repair decision confirmed by qualified technician where required |
| Safety-critical electrical/gas issue | Immediate escalation; no risky self-repair guidance |
| Excess spend | Delegated spend limits + explicit approval above threshold |
| Fraudulent provider | Verified/whitelisted provider strategy |
| Warranty invalidation | OEM-first routing when warranty conditions require it |
| Wrong spare part | Model/serial compatibility verification |
| Landlord-owned asset | Responsibility/approval rules |
| User unavailable | Pre-authorised household delegate |
| Provider no-show | Automatic escalation/rebooking |
| Payment dispute | Milestone-based or post-confirmation payment rules |
| Agent uncertainty | Ask user / route to human rather than guessing |

The exact guardrails must evolve with research and prototype testing.

---

## 19. Metrics

### Candidate North Star
**Autonomous Resolution Rate**

> % of maintenance incidents successfully resolved with no more than one required user intervention.

This is better than app opens, reminders sent, or assets added.

### Supporting metrics
- human touches per incident;
- active user minutes per incident;
- median time to resolution;
- first-visit resolution rate;
- repeat-context count;
- no-show recovery rate;
- agent recovery rate;
- approval-request rate;
- delegated-payment success rate;
- cost variance vs approved estimate;
- recurrence within X days;
- user confidence/trust score.

### Before/after experiment frame
Compare:
**Current workflow vs agent-assisted workflow**

Measure:
- number of user actions;
- time spent;
- elapsed days;
- number of calls;
- number of failures;
- cost transparency;
- successful closure.

---

## 20. Long-term data/defensibility thesis

Do not say “AI is our moat.”

Potential long-term asset:
## Household Asset Graph

It can include:
- assets owned;
- ownership/responsibility;
- purchase history;
- warranties;
- AMC status;
- repair history;
- parts replaced;
- recurring failures;
- providers used;
- quote history;
- reliability history;
- authorised household members;
- payment policies;
- household availability.

Across enough households, future intelligence could include:
- typical repair cost by model/problem;
- provider reliability/no-show rate;
- common failure patterns;
- part compatibility;
- expected resolution time.

These are **future hypotheses**, not current capabilities.

---

## 21. Business model hypotheses

Do not prematurely lock into a ₹299/month subscription.

Test:

### Model A — Consumer membership
User pays for an always-on household operations service.

### Model B — Resolution fee
Pay only when an incident is successfully resolved.

### Model C — B2B2C
Possible funders:
- appliance OEMs;
- extended-warranty providers;
- home insurers;
- property managers;
- landlords;
- premium housing communities.

### Strategic trust question
If service vendors pay commissions to be chosen, the agent may stop being perceived as representing the consumer.

Potential principle:
> **Do not auction repair recommendations to the highest-paying provider if delegated consumer trust is the core product asset.**

This is a hypothesis/strategic stance to test.

---

## 22. Competition demo — high-bar version

The demo should show a **failure case**, not a happy-path chatbot.

### Suggested demo storyline

#### Scene 1 — Trigger
User:
> “The AC isn't cooling.”

Agent:
- identifies AC;
- checks warranty/service history;
- chooses service route;
- calls provider;
- books technician.

#### Scene 2 — Failure
Technician misses appointment.

Agent:
- detects missed commitment;
- follows up automatically;
- escalates/rebooks.

#### Scene 3 — Expensive repair
Technician quotes ₹6,500.

Agent:
- sees autonomous spend cap is ₹1,500;
- pauses;
- asks user for approval;
- explains quote and alternatives.

#### Scene 4 — Missing part
Part unavailable.

Agent:
- verifies compatible part;
- coordinates delivery;
- books follow-up after part arrival.

#### Scene 5 — Closure
Repair completed.

Agent:
- verifies resolution;
- releases authorised payment;
- stores service record;
- records new part warranty;
- tells user no further action is required.

### Desired judge reaction
> “The agent actually did the work and handled the exception.”

---

## 23. Final narrative direction

The final story should remain simple even if the research and product are sophisticated.

### Opening line direction
> **The household bought machines. It accidentally inherited an operations department.**

### Story arc
1. One vivid real consumer incident.
2. Quantify the coordination tax.
3. Reveal the unexpected insight.
4. Show why existing alternatives fail.
5. Introduce the narrow initial wedge.
6. Show the agent owning resolution.
7. Show the three rails naturally.
8. Show exception handling and guardrails.
9. Show measured before/after improvement.
10. Show ecosystem incentives and business model.
11. Show expansion path.

### Core framing
> **We are not building a maintenance app. We are removing the household from maintenance operations.**

### Possible closing direction
> **Today every machine has a service network. Nobody runs the network for the household. We do.**

Treat these as narrative directions; refine them after primary research.

---

## 24. Research outputs that should exist before solution lock

Before committing to the final product, the team should have:
- interview repository;
- anonymised incident dataset;
- evidence screenshots/logs where consented;
- affinity map;
- service-journey maps;
- system map;
- pain-frequency matrix;
- cohort comparison;
- coordination-tax analysis;
- provider-side pain analysis;
- top 3 unexpected findings;
- ICP decision;
- problem wedge decision;
- agentability assessment;
- willingness-to-delegate evidence;
- trust/authority boundaries;
- business-model evidence.

---

## 25. Kill / promote rules

### Promote the concept if research shows
- repeated service incidents;
- high coordination burden;
- significant chasing after initial booking;
- users already delegate parts of the workflow to family/staff;
- users value certainty/time savings;
- meaningful tasks can be delegated safely;
- providers can be contacted through existing real-world channels;
- exception handling creates more value than reminders.

### Narrow the concept if
- one appliance category produces most signal;
- renters show dramatically stronger pain;
- remote family management dominates;
- first-visit-resolution problems dominate;
- spare-parts logistics dominate;
- only one rail is genuinely useful in the initial wedge.

### Kill or radically rethink if
- most pain is rare and low consequence;
- users prefer handling it themselves;
- service providers cannot be contacted/acted upon without proprietary integrations;
- users will not delegate calls/payments/approvals;
- the real pain is simply poor technician quality rather than coordination;
- the agent cannot materially reduce user actions or resolution time.

---

## 26. Suggested working plan

### Phase 1 — Discovery sprint
- 5–8 exploratory household interviews;
- 3–5 technicians/service-provider interviews;
- build first incident dataset;
- refine hypotheses.

### Phase 2 — Evidence expansion
- scale to 35–50 household interviews;
- collect 75–150 incidents if feasible;
- continue supply-side interviews;
- quantify coordination tax;
- identify strongest wedge.

### Phase 3 — Concept selection
- choose one ICP;
- choose one initial asset/service category if needed;
- define agent authority;
- define rail usage;
- define trust boundaries.

### Phase 4 — Prototype
- build state machine;
- prototype happy path + at least 3 failure paths;
- test with users;
- measure before/after effort.

### Phase 5 — Submission
- evidence-first narrative;
- one central insight;
- one clear wedge;
- end-to-end agent demo;
- feasibility + guardrails;
- system incentives;
- business model hypothesis;
- expansion logic.

---

## 27. High-bar quality checklist

Before submission, aim to have:

- [ ] 35–50 deep consumer interviews (high-bar target)
- [ ] 75–150+ reconstructed incidents if feasible
- [ ] 15–25 supply-side interviews across technicians/service centres/landlords/property managers
- [ ] substantial real-behaviour evidence library
- [ ] 1 primary unexpected insight + 2 supporting findings
- [ ] one narrow ICP
- [ ] one clear initial wedge
- [ ] complete agent state machine
- [ ] explicit exception/failure paths
- [ ] meaningful voice action
- [ ] meaningful payment/authorisation logic
- [ ] genuine logistics role where needed
- [ ] end-to-end prototype
- [ ] at least 3 tested workflows
- [ ] measured or experimentally estimated before/after metrics
- [ ] evidence-backed business model hypothesis
- [ ] full ecosystem/system map
- [ ] adversarial judge Q&A preparation

The numbers above are internal quality targets, not official competition rules.

---

## 28. Active monitoring

A scheduled monitoring task is active for:
- new official The Ken Case Competition 2026 updates;
- newly published strong public submissions;
- finalist/winner decks or write-ups;
- credible analyses worth studying.

The monitoring should notify only on meaningful developments and explain why they matter specifically for the **Keeping the machines running** strategy.

---

## 29. Source basis for this context file

### User-supplied material
1. **Case studies.docx** — contains the “Keeping the machines running” opening plus other case-study text and demographic visuals.
2. **Pasted markdown(1).md** — contains the case-selection framework and additional case descriptions from the competition material.

### Source-derived factual points used here
- household service workflows are fragmented;
- multiple calls/steps are common;
- service providers and technicians require chasing;
- households remember warranties/service dates/technician contacts themselves;
- the case is framed around repeated operational burden.

### Hypotheses/inferences in this file
Everything labelled as a thesis, hypothesis, candidate metric, candidate ICP, product concept, demo concept, business model, or future moat is **not a verified finding** until primary research confirms it.

---

## 30. Instruction to any future AI/teammate using this file

When continuing this project:

1. **Do not treat the current thesis as truth.** Use research to falsify it.
2. **Do not invent statistics.** Use only collected or source-backed data.
3. **Separate facts, findings, hypotheses, and recommendations.**
4. **Prefer observed behaviour over stated preference.**
5. **Do not force all three rails if a rail adds no value.**
6. **Optimise for an agent that does work, not an AI interface that talks.**
7. **Prioritise exception handling and recovery.**
8. **Keep the final story simple even if the backend/system analysis is deep.**
9. **Do not drift into a generic maintenance marketplace or reminder app.**
10. **The target is a very high-bar, competition-winning submission.**

---

# One-line project north star

> **Make household machine maintenance disappear as a coordination job for the consumer.**
