# The Ken 2026 — Case #1 Context File
## Keeping the Machines Running

### Purpose
Working context for deep problem discovery, primary research, divergence, synthesis, and eventual agent concept development for Case #1 of The Ken’s Case Build Competition 2026.

**This is not a final problem statement or product proposal.** The goal is to understand the problem space deeply before narrowing it.

---

# 1. Competition Context

The competition asks teams to discover a meaningful consumer problem and assemble an agent around three rails:

1. **Voice**
2. **Payments & Authorisation**
3. **Logistics**

For this case, possible rail roles include:

- **Voice:** call technicians, vendors, service centres, landlords, residents; explain requirements; follow up; schedule; escalate.
- **Payments & Authorisation:** approve service, approve quotes, pay, handle OTP/authorisation, manage recurring payments/AMC.
- **Logistics:** schedule physical visits, coordinate technician arrival, arrange replacement/repair/pickup/disposal.

The important principle is: **do not find an AI problem merely because AI can answer it.** Find a real-world workflow where an agent can meaningfully take action.

---

# 2. Case Framing

The case describes the burden households face in keeping machines and household services running.

Examples in the case include:

- RO installation requiring multiple handoffs between chatbot, service centre, service agent, OTPs and forms.
- AC repair becoming a tenant-landlord responsibility dispute.
- Kitchen trolley work waiting on a carpenter.
- A plumber repeatedly saying they are coming, requiring multiple calls.
- Lift AMC/service requiring residents to chase.
- Pest-control vendors calling to sell renewals.
- A respondent connecting appliance service, car service and Amazon errands as “many similar stuff” that require time and effort.
- Households describing themselves as **“dispatch desks.”**
- People holding purchase dates, warranty periods and technician numbers in memory.
- The experience being described as **“solving the chase problem with hope.”**

The case should therefore NOT immediately be interpreted as an appliance-maintenance app.

---

# 3. Working Problem Space

## Current working definition

> **Household execution and service orchestration: the work households perform to get physical-world tasks, services and recurring obligations completed across fragmented vendors, people and systems.**

“Machines” are the **entry point**, not necessarily the final problem boundary.

The eventual wedge could be:

- appliance servicing
- household repairs
- vendor reliability
- recurring household obligations
- service coordination
- responsibility disputes
- household operations
- physical-world task execution
- delegated household administration
- or something else discovered through research.

---

# 4. Decode the Case

## “Every machine has a service date, warranty and technician”

Surface interpretation:
- reminder problem
- information-management problem

Deeper hypotheses:
- households maintain operational information about physical assets.
- invoices, warranties, technician numbers and service history may be fragmented.
- the deeper issue may not be remembering; it may be that nobody else owns the lifecycle.

Research:
- Who remembers warranty expiry?
- Where are invoices?
- Who knows the technician?
- Who knows whether AMC exists?
- What happens if the normal household operator is unavailable?

---

## RO installation: multiple handoffs

The workflow involves chatbot → service centre → service agent → OTPs/forms → installation.

Possible failures:

- fragmented handoffs
- repeated explanations
- context loss
- authorisation friction
- lack of status visibility
- nobody owning the workflow end-to-end

Key research question:

> **Who owns the workflow from request to completion?**

If the answer is “the customer,” that may be the deeper problem.

---

## AC repair: responsibility dispute

The AC example is not simply “find a technician.”

Potential workflow:

1. identify problem
2. determine whether repair is needed
3. decide responsibility
4. decide who pays
5. obtain approval
6. find technician
7. schedule
8. repair
9. verify
10. pay/settle

This suggests a possible broader problem around **responsibility + authorisation + execution**.

---

## Carpenter: waiting on another person

Possible workflow:

Need → find carpenter → contact → explain → agree time → wait → no-show/delay → follow up → reschedule → completion.

The actual physical task may be short; the management time can be much larger.

### Important hypothesis

> **The hidden consumer cost may be the management overhead required to make physical work happen.**

Separate:
- work time
- management time
- waiting time.

---

## Plumber: commitment enforcement

The plumber says “coming,” but repeated calls are required.

Possible deeper job:

> **Getting another person to do something they already agreed to do.**

This may involve:
- commitment tracking
- follow-up
- escalation
- rescheduling
- replacement-provider search.

Research whether this pattern appears across:
- plumbers
- carpenters
- electricians
- technicians
- delivery/installations
- repair vendors
- other household services.

---

## Lift AMC: recurring obligations

This introduces a different class:

- recurring contracts
- scheduled maintenance
- vendor obligations
- missed service
- payment
- escalation
- safety/compliance.

Potential category:

> **Recurring household/service obligations**

Examples to investigate:
- appliance AMC
- pest control
- RO service
- chimney cleaning
- vehicle service
- internet renewal
- water-tank cleaning
- society maintenance.

Question:

> Who makes sure the obligation actually happens?

---

## Pest control: possible incentive mismatch

The vendor calls to sell renewal.

Potential mismatch:

- vendor objective: sell another service
- household objective: maintain a pest-free home

Hypothesis:

> The household may need an independent operator that optimises for the household outcome rather than the vendor’s sales outcome.

Questions:
- How does the household know when service is actually needed?
- Who decides the schedule?
- What evidence determines renewal?
- Who keeps service history?
- How does the household compare providers?
- Who owns the outcome?

---

## “Many similar stuff which require time and effort to get things/errands done”

This may be a major clue.

The respondent connects multiple categories:
- appliance service
- car service
- Amazon
- other errands.

Possible meta-problem:

> Individually small physical-world tasks collectively create a large household management burden.

This suggests exploring **household execution**, not just appliance maintenance.

---

## “Machines multiplied”

As households acquire more machines, each creates another operational relationship:

- purchase
- invoice
- installation
- warranty
- technician
- service history
- AMC
- payment
- replacement.

Potential insight:

> Households have accumulated an asset-management burden without an equivalent operational layer.

But do NOT assume that the answer is a digital inventory. Ask why the household has to manage this information at all.

---

## “Households have become dispatch desks”

This is one of the strongest clues.

A dispatch desk:
- receives requests
- assigns tasks
- contacts people
- schedules
- tracks status
- follows up
- handles exceptions
- escalates failures.

Possible hypothesis:

> **There is no operational layer between households and a fragmented physical-service ecosystem.**

This should be validated through interviews.

---

## “Holding purchase dates, warranty periods, technician numbers in memory”

This sounds like a memory problem, but may actually indicate:

> People are forced to become the system of record for relationships they do not want to manage.

The household member becomes:
- memory
- coordinator
- reminder system
- negotiator
- authoriser
- verifier
- escalation manager.

Potential product principle:

> **The user specifies the desired outcome; the agent owns the execution state.**

---

## “Solving the chase problem with hope”

Possible layers:

### Effort
“I had to make five calls.”

### Uncertainty
“I don't know whether they will actually come.”

### Trust
“They said they would come, but I don't believe them.”

### Ownership
“If I don't chase, nobody will.”

Do not collapse all of these into “frustration.” Research which one is actually dominant.

---

# 5. Divergence Framework

Do not brainstorm product ideas randomly. Explore the space systematically.

## A. WHAT OBJECT?

### Appliances
- AC
- refrigerator
- washing machine
- dishwasher
- RO/water purifier
- microwave
- oven
- chimney
- hob
- TV
- air purifier
- geyser
- inverter
- dryer
- vacuum cleaner
- mixer/grinder

### Home infrastructure
- plumbing
- electrical
- internet
- water tank
- lift
- generator
- drainage
- pest control
- carpentry
- painting
- locks
- doors/windows

### Other assets
- car
- bike
- furniture
- electronics
- smart-home devices
- children's equipment

### Recurring services
- cleaning
- pest control
- appliance AMC
- vehicle servicing
- water delivery
- gas
- internet
- security
- home maintenance.

---

# 6. WHAT JOB?

Break the lifecycle down.

## Before purchase
- identify need
- research
- compare
- decide
- buy

## Setup
- delivery
- installation
- registration
- warranty activation
- configuration

## Ownership
- operate
- clean
- maintain
- refill consumables
- monitor

## When something goes wrong
- notice
- diagnose
- search
- contact
- explain
- schedule
- authorise
- repair
- pay
- verify

## Recurring lifecycle
- service
- AMC
- renewal
- inspection
- replacement

## End of life
- repair vs replace
- dispose
- sell
- recycle
- uninstall

---

# 7. WHAT CAN FAIL?

Use this failure taxonomy.

| Failure | Example |
|---|---|
| Discovery | Don't know whom to call |
| Information | Don't know warranty status |
| Handoff | Service centre → technician breaks |
| Coordination | Timing does not work |
| Commitment | Provider says yes but does not arrive |
| Responsibility | Tenant vs landlord |
| Payment | Who pays / how much |
| Authorisation | OTP / approval |
| Communication | Repeatedly explain issue |
| Status | No idea what is happening |
| Verification | Don't know whether work is complete |
| Recurrence | Same issue keeps returning |
| Scheduling | Multiple parties must align |
| Escalation | Don't know when/how to escalate |
| Records | Invoices/history scattered |
| Trust | Vendor promise is unreliable |
| Incentives | Vendor benefits from selling more |
| Delegation | Nobody else can take over |

---

# 8. WHO ARE THE ACTORS?

## Household
- self
- spouse
- parent
- child
- domestic help
- household manager

## External
- manufacturer
- authorised service centre
- technician
- local technician
- carpenter
- plumber
- electrician
- pest-control provider
- delivery company
- marketplace
- landlord
- tenant
- society/RWA
- building manager
- security desk
- insurance/service provider.

### Critical question

> **Who actually owns household operations?**

Possibilities:
- one spouse
- both
- parent
- whoever has more time
- whoever is at home
- nobody consistently.

---

# 9. WHAT DOES THE USER DO?

For each errand, count:

1. notice problem
2. search
3. compare
4. call
5. message
6. explain
7. send photo/video
8. provide details
9. schedule
10. wait
11. follow up
12. reschedule
13. authorise
14. pay
15. verify
16. complain
17. escalate
18. record information
19. remember future action
20. repeat.

### Useful metric hypothesis

> **Management actions per successful outcome**

A short physical repair can create a surprisingly long management workflow.

---

# 10. EMOTIONAL MAP

Do not label everything “frustration.”

Look for:

- uncertainty
- irritation
- helplessness
- powerlessness
- anxiety
- guilt
- distrust
- mental load
- conflict
- exhaustion
- relief.

The strongest wedge may be the emotion attached to a particular workflow.

---

# 11. Machine → Errand → Workflow → Meta-Problem

Use this funnel.

### Level 1 — Machine
Example: AC.

### Level 2 — Errand
“Get the AC repaired.”

### Level 3 — Workflow
Find technician → explain → schedule → wait → follow up → approve quote → pay → verify.

### Level 4 — Underlying problem
“No one reliably owns execution from problem to completion.”

### Level 5 — Generalisable insight
“Households are acting as manual dispatch desks for fragmented physical services.”

Only after reaching this level should product design begin.

---

# 12. Primary Research Plan

## Errand inventory

Ask respondents to recall the last **3 months**.

Prompt:

> “Tell me every household thing you had to get done that required someone outside your home.”

Capture:

| Field | Record |
|---|---|
| Errand/task | What needed to happen? |
| Object | AC, RO, plumbing, car, furniture, etc. |
| Trigger | Why did it start? |
| Initiator | Who noticed/requested it? |
| Executor | Who did the physical work? |
| Actors | How many people/organisations? |
| User actions | Calls/messages/follow-ups |
| Active time | Time personally spent |
| Waiting time | Time waiting |
| Failures | What went wrong? |
| Repetition | One-off/recurring |
| Payment | Who paid? |
| Authorisation | Approval/OTP? |
| Responsibility | Who owned it? |
| Workaround | What did they do today? |
| Emotion | How did it feel? |
| Outcome | Completed/not completed |
| Escalation | Required? |

---

# 13. Critical Interview Question

For every workflow ask:

> **“Who owns making sure this actually gets done?”**

Then:

> **“If you don't follow up, what happens?”**

This may reveal the real problem more effectively than simply asking whether the task was frustrating.

---

# 14. Interview Guide

## Warm-up
1. Tell me about the last time something at home needed fixing, servicing or arranging.
2. What happened from the moment you noticed it?
3. Walk me through everything you personally did.

## Workflow
4. Who did you contact first?
5. How did you find them?
6. How many people did you talk to?
7. How many times did you follow up?
8. Did you repeat information?
9. Did anyone fail to show up/respond?
10. Did the timing change?

## Ownership
11. Who was responsible for making sure it happened?
12. What happened when that person did not act?
13. Could another household member have handled it?

## Information
14. Where did you find the invoice/warranty/service number?
15. Did you search old messages?
16. Do you know when the next service is due?

## Money
17. Who decided to spend money?
18. Who paid?
19. Was approval/OTP required?
20. Did responsibility or price become an issue?

## Emotion
21. What part was most annoying?
22. What part made you uncertain?
23. What part did you least want to do yourself?
24. Did you postpone it because you didn't want to deal with it?

## Counterfactual
25. If someone else could completely take care of this, what would you want them to own?
26. What would you still want to approve?
27. What would make you trust them?

---

# 15. Avoid Leading Questions

Do NOT begin with:

- “Would you use an AI assistant to manage your appliances?”
- “Would you pay someone to chase technicians?”
- “The problem is reminders, right?”

Instead:

> **“Tell me about the last time this happened.”**

Reconstruct real behaviour first.

---

# 16. Research Hypotheses

These are hypotheses, not conclusions.

### H1 — Household operations layer
Households lack a system that coordinates physical-world tasks.

### H2 — User as integration layer
Vendors have systems, but the consumer connects them manually.

### H3 — Commitment enforcement
The hardest part is getting another party to honour a commitment.

### H4 — Management time
The management effort is much larger than the physical work itself.

### H5 — Fragmented household information
Purchase dates, warranties, invoices, technician numbers and service history are scattered.

### H6 — Responsibility ambiguity
Tasks become difficult because it is unclear who should act/pay/authorise.

### H7 — No reliable physical-world state
A ticket can say “open” while the household still has no confidence that the real-world job will happen.

### H8 — Default household operator
One person absorbs most coordination work.

### H9 — Vendor vs household incentives
Vendor workflows optimise for vendor goals rather than household outcomes.

### H10 — Outcome ownership
The strongest agent may own the outcome rather than simply remind the user about a task.

---

# 17. Rail Mapping

## Voice

Potentially useful when the agent must:
- call providers
- explain an issue
- collect information
- schedule
- follow up
- negotiate
- escalate
- confirm completion.

Voice is strongest when the external workflow is genuinely voice-based.

## Payments & Authorisation

Potentially useful for:
- approving quotes
- service payments
- recurring payments/AMC
- OTPs
- responsibility/payment decisions
- charge verification.

Payment should be a real workflow bottleneck, not an artificial feature.

## Logistics

Potentially useful for:
- technician visits
- pickups
- replacements
- deliveries
- multiple visits
- physical completion tracking
- no-show recovery.

The best concept should use the rails because the workflow requires them.

---

# 18. Agentic vs Chatbot Test

### Weak
User: “When should I service my AC?”

AI: “Every X months.”

Informational, not meaningfully agentic.

### Stronger
User:

> “Make sure my AC is serviced before summer.”

Potential agent workflow:

1. check service history
2. check warranty/AMC
3. determine required service
4. contact provider
5. schedule
6. request approval if necessary
7. handle payment/authorisation
8. track technician
9. follow up if delayed
10. verify completion
11. update records
12. schedule next action.

The final workflow must be derived from research.

---

# 19. Problem Spaces to Explore

These are directions, not recommendations.

1. Appliance lifecycle management
2. Household repair orchestration
3. Vendor commitment management
4. Recurring household obligations
5. Household service coordination
6. Responsibility arbitration
7. Household asset operations
8. Delegated household operations
9. Exception management
10. Household “dispatch desk”

---

# 20. Do Not Overgeneralise

### Too narrow
> AI assistant for appliance servicing.

Problem:
- small conceptual space
- potentially commoditised
- may miss deeper insight.

### Too broad
> AI assistant for everything in your home.

Problem:
- vague
- difficult to validate
- difficult to demonstrate
- weak competition story.

### Potential sweet spot

Start with:

> **How do households get physical-world tasks completed?**

Then use primary research to identify the narrowest repeated job with the strongest evidence.

---

# 21. Research Matrix

Build this after interviews.

| Workflow | Frequency | Frustration | Management effort | Actors | Failure rate | Emotional stakes | Current workaround | Voice | Payment/Auth | Logistics | Agent potential |
|---|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| AC repair | | | | | | | | | | | |
| RO service | | | | | | | | | | | |
| Plumber | | | | | | | | | | | |
| Carpenter | | | | | | | | | | | |
| Pest control | | | | | | | | | | | |
| Car service | | | | | | | | | | | |
| Appliance AMC | | | | | | | | | | | |
| Electrical repair | | | | | | | | | | | |
| Furniture repair | | | | | | | | | | | |
| Internet issue | | | | | | | | | | | |

Do not score before collecting evidence.

---

# 22. Opportunity Scoring

After primary research, score each discovered problem on:

- **Pain:** How bad is it?
- **Frequency:** How often?
- **Repetition:** Does it recur?
- **Management burden:** How much coordination?
- **Emotional depth:** Anxiety/conflict/helplessness/guilt?
- **Agentability:** Can an agent execute rather than advise?
- **Rail fit:** Are voice, payment/auth and logistics naturally involved?
- **Right to win:** Can the team create a differentiated solution?
- **Evidence:** Do multiple interviews independently show the pattern?
- **Competition whitespace:** Is the space underserved?

---

# 23. Strong vs Weak Evidence

### Weak
> “Everyone hates calling technicians.”

### Better
> “Most respondents described multiple follow-ups for household services.”

### Strong
> “Across interviews, the same household member consistently owned service coordination, spent significant time on calls/messages, and described uncertainty about whether the provider would actually arrive as the biggest frustration.”

### Strongest
Repeated behavioural pattern + measurable burden + emotional consequence + willingness to delegate + clear agentic execution opportunity.

---

# 24. Hidden Insights to Hunt For

Potential discoveries to test:

- The household has no operations layer.
- The physical owner is not the operational owner.
- The most painful job is getting another person to act.
- Small household tasks create disproportionate management time.
- The consumer is the integration layer between disconnected companies.
- The problem is not remembering; it is ownership and execution.
- Digital ticketing creates the appearance of progress without guaranteeing physical completion.
- Households may need an advocate optimising for their outcome rather than vendor revenue.
- Exceptions create the most pain: no-show, dispute, wrong part, repeated repair, unclear responsibility, unexpected cost.
- The ideal agent may be judged by outcomes completed rather than conversations answered.

---

# 25. Core Metrics to Collect

1. Number of calls/messages/interactions
2. Active time
3. Waiting time
4. Number of follow-ups
5. Number of handoffs
6. Number of repeated explanations
7. Number of failed commitments
8. Number of decisions/authorisations
9. Number of escalations
10. Point at which the user trusted that the task would actually be completed

---

# 26. The Why Ladder

Example:

**Why was the AC repair difficult?**

→ Because I had to call the technician.

**Why?**

→ They didn't come.

**Why?**

→ They kept postponing.

**Why?**

→ I had no reliable way to make them commit.

**Why?**

→ No one owns the outcome except me.

This moves the investigation from:

> “Technician discovery”

toward a potentially deeper hypothesis:

> **Outcome ownership / execution assurance.**

Do not assume this is the final insight; validate it.

---

# 27. Primary Research Goal

The objective is NOT:

> “Prove that appliance servicing is painful.”

The objective is:

> **Discover the most repeated, emotionally meaningful and agentically solvable household execution problem hiding underneath the examples in the case.**

We should be willing to discover that:
- appliances are not the best wedge,
- repair is not the best wedge,
- reminders are not the problem,
- or the problem is broader/narrower than expected.

---

# 28. Decision Gate Before Building

Do not build until we can answer:

1. What exact user segment has the problem?
2. What exact recurring job are they trying to accomplish?
3. How often does it happen?
4. What does the workflow look like?
5. Which steps create the most work?
6. What workaround exists?
7. Why do current solutions fail?
8. What emotional consequence exists?
9. What can an agent autonomously execute?
10. Where do voice, payment/auth and logistics naturally enter?
11. What evidence supports the problem?
12. What is the sharpest non-obvious insight?
13. Why is it a meaningful business opportunity?
14. Why is our agent uniquely suited to solve it?

---

# 29. One-Line Working Thesis

> **“Keeping the Machines Running” may be less about machines and more about the invisible operational work households perform to make physical-world tasks happen.**

Treat this as the current exploration thesis — **not the final answer**.

---

# 30. Final Research Mindset

Do not ask:

> “What AI product can we build?”

Ask:

> **“What is the household forced to do today that it should never have had to do?”**

Then:

> “Why does that work exist?”

> “Why hasn't software removed it?”

> “What part can an agent actually own?”

> “Can it act through voice, payments/authorisation and logistics?”

And finally:

> **“What did we discover through primary research that nobody could have written down from the case alone?”**

That final question is critical.

**The winning insight should come from the research, not from the case title.**
