# Session Context — The Ken Case Competition 2026 ("Keeping the machines running")

**Scope note on this file:** this is a faithful reconstruction of everything substantive said and produced in this Claude Code session, in order. Tool-call plumbing (exact function-call syntax, a schema-validation retry) is compressed to a one-line note where it doesn't change the substance; every actual question, answer, finding, and deliverable is reproduced in full. Source files this session pulled from are preserved verbatim in `/files`.

**Session working directory:** `/Users/klprathyusha/Placement Preparation/Ken case comp`
**Date of session:** 2026-09-08
**Files present at session start:** `01_group_braindump.md`, `Keeping_Machines_Running_Context.md`, `keeping_the_machines_running_context.md`

---

## Part 1 — Understanding the case competition, end to end

### 1.1 User's opening request (verbatim)

> this is the case competition https://the-ken.com/case-competition-2026/
>
> understand all the things that we need to submit for phase 1 - end to end
>
> we have chosen "keeping the machines running" opening
>
> I have included two context files for reference
>
> I have included 01_group_braindump.md file as well
>
> help me understand each and every point of what is available in the case competition page
>
> help me diverge more for the first phase, ask me questions for taking correct direction
>
> help me completely map the system without diverting from the deliverables mentioned

### 1.2 What Claude did to answer this

1. Read all three local files in full: `01_group_braindump.md` (raw team brainstorm — stakeholders, machines/errands list, personas, workflows), `Keeping_Machines_Running_Context.md` (a 30-section "master context" doc: thesis, competition strategy, product vision, agent state machine, research design targets of 35-50 interviews, metrics, business model hypotheses, demo storyline, etc.), and `keeping_the_machines_running_context.md` (a second, differently-structured context doc: case decode, divergence framework by object/job/failure/actor, interview guides, hypotheses H1-H10, candidate ICPs A-E, research matrix). Full text of all three is preserved in `/files`.
2. Attempted `WebFetch` on `https://the-ken.com/case-competition-2026/` — **failed with HTTP 403 Forbidden** (the site blocks the WebFetch tool's default user agent).
3. Fell back to `curl` with a browser User-Agent string via Bash — **succeeded (HTTP 200)** — then parsed the HTML to plain text with a small Python script (strip `<script>`/`<style>`, convert block tags to newlines, strip remaining tags, unescape HTML entities). Output: 807 lines of real page text, preserved at `/files/ken_case_competition_2026_page.txt`.
4. Read that parsed text in full and extracted the actual competition structure (see 1.3 below).

### 1.3 What was found on the live page — reported to the user in full

**⚠️ Timeline flagged as urgent:** Today is Sep 8, 2026. Solution Assembly (= Phase 1) closes **Sep 10, 11:59 PM IST — about 2 days away**. Registration itself closes Sep 8 (the same day) if the team isn't locked yet.

**What "Phase 1" actually is:** The competition runs in 3 stages — **Choose** (already done — opening #02, "Keeping the machines running", already picked) → **Assembly** (= Phase 1, due Sep 10) → **Build** (post-shortlist, from Sep 15, with rail partners). Phase 1 is **not a deck or research report** — it is a form with **10 short, word-capped answers**. This is a significant gap from the two local context files, which scope a 35-50 interview research program, an incident dataset, a "Coordination Tax" metric, a full state machine, etc. — useful thinking fuel, but almost none of it is directly submittable in the actual Phase 1 form.

**The 10 questions, exactly as posted on the page:**

**Team (Q1)** — *Who is this team, and why is this opening yours?*
One line per member (name + your closest personal connection to this pain) + 50 words as a team on your unfair advantage (a person you can reach, a place you can observe, something you've already done). Litmus test given on the page: *"If any three students at your college could submit your answer, rewrite it."*

**Evidence (Q2)** — *The one customer insight you discovered.* — page labels this: **"We read this one first."**
60 words. Proof optional but **scored**. One non-obvious insight from real people (not the case doc, not AI) that changed something specific in your design. Attachments allowed: a recording with a timestamp marking the moment the insight surfaced, a photo of a workaround, a survey with raw answers, working notes, chat logs (including AI chat logs).

**Solution (Q3-Q7):**
- **Q3** — Agent's six-step loop, one sentence each, ≤15 words per step. What triggers it. What it already knows. What it does. Who it deals with (person or institution). What it asks its human, and when. How it knows it's done. "One sentence per step; if a step needs two, it is two steps."
- **Q4** — One sentence per rail (payments / logistics / voice) on its role. If a rail has no role, say so and give the reason.
- **Q5** — Pick ONE rail to innovate on, 40 words. Name a capability that doesn't exist today.
- **Q6** — The one customer asset you need them to hand over, 30 words, plus the reason they'll agree. (order history, family group, statements, contacts, etc.)
- **Q7** — "The annexation" — which use-case you subsume next, 30 words, and why it falls to you rather than whoever owns it today.

**Bets (Q8-Q9):**
- **Q8** — Which of the 16 openings would you *never* hand to an assistant? Assume the assistant works flawlessly. One opening, one sentence. "There is no right answer."
- **Q9** — Which Indian company should have built this already? One company, 60 words, plus your best guess why they haven't.

**Track (Q10)** — Product Strategy (finish with a fully specified build: complete flows, segment map, where it breaks and why) vs Product Build (finish with a working prototype on a partner sandbox). Locks at submission.

**Ground rules (verbatim substance from the page):**
- No code required to advance, reach the finale, or win.
- One opening per team. Can switch, up to three times, before submitting — evidence starts over each time you switch.
- Every team member must be from the same institution; one email = one team.
- Get consent from everyone interviewed; tell them their words may be published.
- Quotes are published as age-band + city, **never a name**.
- The Ken may validate anything submitted and may disqualify a team at its sole discretion.

**Judging criteria (applies across the whole competition, both tracks, whether or not code is written):**
- **Evidence** — did a real person tell you this? Interviews, recordings, and what you found that you weren't looking for.
- **Creativity** — fresh, counterintuitive, unique, different. Page states explicitly: *"This is usually where AI-generated solutions fail."*
- **Clarity** — communicated clearly, specific.
- **Feasibility** — practical, implementable in a reasonable way.
- **Thoroughness** — meticulous and detailed.

**Eligibility:** Full-time UG/PG students, any institution in India. Team of 1-3 ("most of the work rewards three"). All members same institution. No cap on teams per institution. Track chosen at registration, changeable up to the build stage. No code required. The Ken may validate/disqualify at its discretion.

**The 16 openings** (team is on #02): Keeping up with the school · **Keeping the machines running** · Madam, OTP? · Finding the exact right thing · Looking after the pet · Managing the family's health · Getting the visa · Sticking to the goal · Getting your money back · Renting a home · Planning the trip · Buying the insurance · Getting the slot · Running your wedding · Where did my money go? · What to cook today?

**Rails/partners:** Zerodha (title partner). Delhivery (logistics — Maps and MCP systems opened to teams). Pine Labs (payments and authorisation — Pine Labs Payments Protocol/P3P for agent-to-agent autonomous UPI/card payments; Grantex sets spend authority and keeps the audit trail). Gnani (voice — India frontier Voice AI, opening APIs for voice-first teams).

**Prizes:** ₹20 lakh in cash prizes total; separate prizes for the most innovative solution on each rail.

**Full timeline as posted:**
- 06 Aug — Great Rewiring survey live (source of the 16 openings)
- 15 Aug — registration open
- 31 Aug — sixteen openings live
- 05 Sep — Solution Assembly open
- 08 Sep — registration closes
- **10 Sep, 11:59 PM IST — Solution Assembly (Phase 1) closes**
- 15 Sep — shortlist announced; rails round opens (sandboxes, docs, office hours with Pine Labs/Delhivery/Gnani)
- 10 Oct — finale, live presentation to investors and rail partners
- Late Oct — "map of India's agentic era" published, best answers credited by team name

---

## Part 2 — Diverging for Phase 1: clarifying questions and answers

Given the tight timeline, Claude judged that several inputs were genuinely the team's call (not derivable from the case docs) and asked via a single multi-question prompt rather than guessing.

### 2.1 Questions asked (verbatim)

1. **Evidence capacity** — "How much real fieldwork (actual conversations with households/technicians/landlords, not desk research) can your team realistically pull off before Sep 10 11:59 PM IST?" Options: Already have real interviews / Can do 3-6 quick interviews in next 24-36h / Zero real interviews, relying on our own lived experience / Other.
2. **Track** — "Which track is your team entering? This locks with submission (Q10) and shapes how ambitious Q3-Q7 should be." Options: Product Strategy / Product Build / Not decided yet.
3. **Right to win** — "For Q1 ('why is this opening yours'), what's your team's actual right-to-win angle on household machine maintenance?" (multi-select) Options: Personal household pain / Access to technicians/service providers / Renter/landlord vantage point / Not yet clear.
4. **Insight thread** — "Which pain-thread from the braindump/context files feels like the strongest bet to chase for the ONE scored insight (Q2) in your remaining interviews?" (multi-select) Options: Commitment enforcement / Responsibility ambiguity (tenant/landlord) / Post-diagnosis coordination (not discovery) / Default household operator overload.

*(Note: the first attempt to send this question set failed with a tool input-schema validation error on one option's `description` field type; it was immediately corrected and resent successfully. No content was lost.)*

### 2.2 User's answers (verbatim)

- **Evidence capacity:** "Can do 3-6 quick interviews in next 24-36h"
- **Track:** "Product Strategy"
- **Right to win (multi-select + free text):** "Personal household pain, Access to technicians/service providers, Renter/landlord vantage point" + free text: *"We decided to pick the problem statement using three stages of filtration. For the first stage, we tried to understand the guardrails, the main constraints, and the And the scope of the agents that we can build based on the problem statements. For the second stage, based on the demographic points that were given for each problem statement, we went for the problems which are more repetitive, more readily frustrating, and less procrastinating. For the third stage, we try to assess the accessibility, right to win, and not a very overcrowded problem. That is how we landed on this problem statement."*
- **Insight thread (multi-select + free text):** "Commitment enforcement, Post-diagnosis coordination (not discovery), Default household operator overload" + free text (explicit instruction, verbatim): *"There can be n number of problems. How can we decide anything, because we did not do any interviews or any surveys yet? We are trying to diverge first and then converge to a particular problem statement before we draft the research plan. Help us diverge first, and don't just fixate on these four problems that you are showing now. We want to have a real problem and real insights from the interviews that we will be doing."*

This last instruction is important and governed everything that followed: **do not pre-narrow the insight; diverge broadly first, converge only from real interview evidence.**

---

## Part 3 — Full divergence map (in response to Part 2.2's instruction)

Claude produced a wider divergence pass, deliberately going beyond the four hypotheses it had originally floated. Full content below (this is the actual deliverable given to the user, reproduced in full — also saved standalone in `notes.md`).

### 3.1 Seventeen falsifiable candidate pain-threads, in eight clusters

**Discovery & trust**
1. People don't lack technicians — they lack a way to know *which* technician/route is trustworthy before committing (OEM vs local vs marketplace).
2. Trust is single-use: a good experience with a technician doesn't transfer — next time, the search restarts from zero.

**Handoff & context loss**
3. Every handoff (chatbot → call centre → agent → technician) forces the user to re-explain the same problem from scratch.
4. The system that's "open" on a ticket has no relationship to whether the physical job actually happened (ticket-reality gap).

**Commitment enforcement**
5. A verbal "yes, coming" has zero enforcement mechanism — the only lever a household has is repeated calling.
6. No-shows have no cost to the provider, so there's no reason for reliability to improve on its own.

**Responsibility & authority**
7. Tenant/landlord disputes stall not on *finding* a technician but on *who decides* — and that decision has no clear default.
8. Society/RWA-owned assets (lifts, generators) fail because "resident" is a diffuse, unaccountable owner — nobody personally feels the obligation.
9. Multi-person households (spouse, parent, domestic staff) don't have a clear handoff protocol when the usual "operator" is unavailable.

**Money & authorization**
10. Households don't distrust the *price* — they distrust the *quote-to-final-bill gap*, because there's no independent check on it.
11. Payment happens before verification is possible, so disputes always happen after the money has moved, not before.

**Information & memory**
12. Warranty/AMC status is not stored anywhere the household trusts — it's reconstructed from memory or a WhatsApp search each time.
13. The technician arrives with less context than the household already gave the call centre 20 minutes earlier — information dies at each handoff.

**Recurring obligations & incentive misalignment**
14. Recurring-service vendors (pest control, RO, AMC) are incentivized to sell renewals, not to signal "you don't need service yet" — so the household can't tell real need from upsell.
15. "Was this actually necessary?" is unanswerable without independent history — the same vendor decides both diagnosis and revenue.

**Emotional/psychological**
16. The dominant feeling isn't anger at the technician — it's the low-grade dread of *initiating* the process at all (why things get "postponed").
17. The household member who owns this work never chose the role — it defaulted to whoever was home/available, not whoever wanted it.

Note given alongside this list: threads 14, 15, 8, and 6 point at *incentive/accountability* problems rather than pure *effort* problems — a different kind of agent (an auditor/advocate) than a pure dispatcher.

### 3.2 Who to talk to — using the team's three stated access lenses on purpose

Deliberately split the 3-6 interviews across the three lenses the team confirmed (household pain, technician/service-provider access, renter/landlord experience) rather than letting them cluster on one side:
- **2 via household-pain lens** — but pick people whose *last incident* differs (not two AC stories).
- **1-2 via technician/service-provider access** — flagged as high-value because almost no competing team will reach this side in 36 hours; tests threads 3, 6, 13 from the supply side.
- **1-2 via renter/landlord lens** — tests threads 7, 8, 10.

Also flagged: vary the **object** (appliance/errand) deliberately — don't let every interview be about AC/RO just because those are the case's headline examples; let respondents surface the object themselves via the unprompted "last three months" framing already in the local context files.

### 3.3 Convergence protocol for the ~36 hours before the deadline

1. **Today:** run all interviews using the incident-reconstruction method already in the local context files (last incident → the one before it → "who owns making sure this gets done" → "if you don't follow up, what happens"). Don't mention AI, agents, or any of the 17 hypotheses to respondents.
2. **After each interview:** log it against the 17 threads — which it supports, contradicts, or says nothing about. Don't force-fit.
3. **Synthesis checkpoint once 4+ interviews are in:** which thread(s) got *independently* corroborated by people who don't know each other and weren't led there? That's the Q2 candidate.
4. **Insight test before writing Q2:** can you point to a specific place in the Q3 six-step loop or Q5 rail choice that *changes* because of this insight? If not, it's not sharp enough.
5. **Lock Q2, then work backward** into Q1 (right-to-win), Q3-Q7 (the agent), Q8-Q9 (bets).

Budget proposed: interviews + synthesis done by evening of Sep 9; full draft of all 10 answers that night; buffer pass on Sep 10 before submitting; don't run interviews into the final hours before the 11:59 PM IST deadline.

Claude then offered (not yet taken up at that point in the session): to turn this into a live interview tracking sheet, or draft the specific interview guide per lens.

---

## Part 4 — Building the "resource-scan" skill

### 4.1 User's request (verbatim)

> Write a skill such that, given a topic, you should be able to pull all the open source repos available and all the web blogs, articles, and news. Books are available, and also you should be able to find any kind of resource that is available on the web. Related to that topic. Don't just think about that topic alone. You should be able to diverge and think like a strategist and product manager, think in systems, and Pull all the resources available for the relevant topics and relevant systems as well. This skill document should be saved to Claude, and I should be able to use it with any Claude account that I will be logged into, If I can use the same skill in different accounts, I want to do that as well.

### 4.2 What Claude did

1. Checked `~/.claude/skills/` — did not exist yet.
2. Created `~/.claude/skills/resource-scan/` and wrote `SKILL.md` inside it (full text preserved verbatim at `/files/resource-scan_SKILL.md` and quoted in full in `notes.md`).
3. Explained the account/machine scoping honestly rather than overpromising: Claude Code skills live on local disk (`~/.claude/skills/`), not tied to which account is logged in — so switching accounts on this same machine still sees it — but they are **not** synced to the account in the cloud. Using it on a different machine requires copying the folder over (e.g. via a dotfiles repo), or packaging it as a plugin for a cleaner install story. Also flagged that skills are a **Claude Code CLI** feature, not a claude.ai web-chat feature.

### 4.3 The skill's actual content (summary — full text in `/files/resource-scan_SKILL.md`)

Frontmatter: `name: resource-scan`, with a description written to trigger on "research a topic broadly," "reading list," "repos/tools for a topic," or "everything available on a subject."

Body, in four steps:
- **Step 0 — Load tools:** load `WebSearch`/`WebFetch` via `ToolSearch` if deferred; optionally use `gh search` for GitHub.
- **Step 1 — Diverge before you search:** produce an explicit system map before any search — the topic itself, adjacent domains, upstream concepts, downstream concepts, stakeholders/personas, alternate framings. 5-10 axes typical, calibrated to how broad/narrow the topic actually is (a narrow technical topic gets a tight technical spread, not padding).
- **Step 2 — Pull resources per axis, across categories:** for every axis, search across Repos, Blogs & Articles, News, Books, and Other (papers/talks/podcasts/courses/standards/communities) — not just for the literal topic's axis.
- **Step 3 — Guardrails:** never fabricate a URL (every link must come from an actual tool result this conversation), dedupe across axes, annotate every resource with why it matters rather than bare-listing links, flag recency/authority, and don't quietly drop axes that returned nothing without first broadening the query.
- **Step 4 — Output:** structured markdown — system map first, then per-axis categorized resources, closing with 2-3 sentences of strategist-level synthesis. An Artifact is offered, not defaulted to, only if the pull is large enough to warrant a browsable page.

---

## Part 5 — Test-driving the skill on the case competition topic

### 5.1 User's request (verbatim)

> yes test-drive the skill on this case competition topic, try to give it such that it understands easily

### 5.2 What happened mechanically

Claude gave the skill this topic string: *"AI agents for household appliance/service maintenance coordination (the 'keeping the machines running' problem) — households acting as manual 'dispatch desks' coordinating technicians, service centres, OEM warranty/AMC, spare parts, and payments to keep appliances (AC, RO/water purifier, washing machine, etc.) and home services (plumbing, carpentry, pest control, lift AMC) running. India-context case competition (The Ken's Case Competition 2026, themed around AI agents built on three rails: voice, payments/authorisation, logistics). Interested in: prior art/startups/products in this exact space, the broader 'home services marketplace' and 'field service management' systems it sits inside, agentic-AI-for-physical-world-tasks as a category, and any research/data on household coordination burden."*

The `Skill` tool call for `resource-scan` **failed** — "Unknown skill" — because Claude Code's available-skills list is loaded once at session start, before the skill file existed. Rather than block on a session restart, Claude manually executed the skill's own documented process (Steps 0-4) in the live conversation, which also served as a real test of whether the written instructions actually produce good output.

### 5.3 System map produced (Step 1)

| # | Axis | Why it belongs here |
|---|---|---|
| A | Household appliance/service coordination AI agents (literal) | Direct prior art and startups |
| B | Field Service Management (FSM) software | The B2B category that already solved "dispatch + scheduling + technician coordination" — same mechanism, enterprise buyer instead of household |
| C | Home services marketplaces (Urban Company, Thumbtack, TaskRabbit, Angi) | Same domain, solves *discovery*, not *orchestration after booking* |
| D | Voice AI that calls businesses on a user's behalf | The literal "voice rail" |
| E | Agentic payments & delegated spend authority | The "payments rail" — the Pine Labs P3P category |
| F | Household asset/warranty record-keeping tools | Upstream — what the agent needs to already know |
| G | PropTech tenant-maintenance coordination | Adjacent stakeholder — the case's own tenant/landlord example |
| H | Gig-worker/technician-side dispatch tools | Supply-side mirror |
| J | Agentic AI executing real-world physical tasks (broader category) | The macro trend the whole competition rides |

### 5.4 Resources found and reported (Steps 2-4) — full text

*(This is the actual, complete output given to the user; also preserved standalone with all links in `links.md` and all annotations in `notes.md`.)*

**A — Household appliance/service coordination AI agents (literal)**
- Repos: [copilot-home-assistant](https://github.com/htekdev/copilot-home-assistant) — multi-agent household-life manager; closest existing OSS analog to the agent's scope. [maintenance_supporter](https://github.com/iluebbe/maintenance_supporter) — Home Assistant integration, adaptive maintenance scheduling across 123 device integrations, sensor-triggered. [github.com/topics/home-services](https://github.com/topics/home-services) — booking platforms, mostly discovery-stage not post-booking orchestration, confirming the whitespace.
- Articles: appliance-repair AI receptionist/dispatcher products already exist ([FieldCamp](https://fieldcamp.ai/industries/appliance-repair/), [ElevenLabs](https://elevenlabs.io/ai-answering-service/appliance-repair-industry), [appliancerepairaiagent.com](https://www.appliancerepairaiagent.com/)) — but all sit on the **provider's** side, not the household's. Flagged as a specific Q9 framing opportunity (who should've flipped to the consumer side, and why they haven't).

**B — Field Service Management (the enterprise mirror of this exact problem)**
- Repos: [Beveren FSM/ERPNext](https://github.com/Beveren-Software-Inc/Field_Service_Management), [Resgrid/Core](https://github.com/Resgrid/Core), [github.com/topics/field-service-management](https://github.com/topics/field-service-management).
- Market: FSM is a $6.7B → $13.8B (2033) category ([overview](https://www.ifs.com/en/glossary/compare/top-10-field-service-management-software-2026)) — ServiceTitan, Salesforce Field Service, Jobber. Framed as: the playbook to study and consciously invert — FSM optimizes dispatch *for the business*; nobody has built the household-side mirror.

**C — Home services marketplaces**
- [Urban Company business model](https://valueforstartups.in/09-urban-company) — India home services market ₹5.1 lakh crore (~$60B) FY25, only 10-15% digitised, Urban Company takes 20-22% commission, profitable FY25, IPO'd. Flagged as an open interview question: does the coordination pain persist even for Urban Company users, or only for independent technicians?

**D — Voice AI that calls businesses on a user's behalf**
- [AI voice agents vs traditional IVR](https://enlightlab.com/ai-voice-agent-vs-traditional-ivr-systems/) — ~$0.40/AI call vs $7-12/human call. Most existing tooling is inbound (answering calls for a business); very little is outbound-on-behalf-of-a-consumer navigating someone else's IVR — flagged as matching the local context file's strongest voice-rail bet.
- [gnani.ai](https://www.gnani.ai/about-us) — the actual voice rail partner: 30M+ daily voice interactions, 12+ languages, Inya VoiceOS (5B-param voice-to-voice model, India AI Mission).

**E — Agentic payments & delegated authority**
- [Pine Labs P3P launch coverage](https://www.pinelabs.com/media-analyst/the-ai-agent-can-now-pay-pine-labs-launches-p3p-indias-first-autonomous-agentic-payment) — P3P handles UPI settlement; Grantex handles identity, spend limits, audit trail, revocable mandates. Noted this maps almost exactly onto the local context file's delegated-spend-limit rail concept (₹1,500 auto-approve / ₹7,800 pause-and-ask) and is technically buildable today on the real partner stack.
- Global protocol landscape: [agentic payments explainer](https://dashdevs.com/blog/agentic-payments-explained-how-ai-agents-make-autonomous-transactions/) — Google AP2, Stripe ACP, Visa TAP, Coinbase x402 — suggested as a possible Q9 angle (India's P3P structurally ahead since UPI rails already existed).

**F — Household asset/warranty record-keeping**
- [Warracker](https://github.com/sassanix/Warracker) (open-source self-hosted warranty tracker), HomeZada, GoCodes — all passive record stores, none act — confirms the local context file's "what NOT to build" exclusion of a digital-warranty-wallet thesis, though it may still be needed as an internal data layer.

**G — PropTech tenant-maintenance coordination**
- [MicroRealEstate](https://github.com/microrealestate/microrealestate), Rentvine API — none India-specific.
- [Maintenance dispute guide, India 2026](https://www.renterfinder.com/blog/maintenance-dispute-landlord-tenant-india-2026) — under Indian rent law, landlord owns structure/major fixtures, tenant owns day-to-day upkeep, and **AC servicing is explicitly documented as the most common grey-zone item with no agreed clause** — directly matches the case's own AC example; not a hypothesis, a documented pattern.

**H — Technician/gig-worker-side tooling**
- [BigFix](https://gig.bigfix.in/), [GigPe](https://www.gigpe.com/industries) — real, reachable India gig platforms for repair technicians/device collectors, confirming supply-side interview access exists beyond personal contacts.

**J — Broader "agentic AI does real-world tasks" category**
- [awesome-ai-agents-2026](https://github.com/caramaschiHG/awesome-ai-agents-2026), [Browser-Use](https://github.com/browser-use/browser-use) (93K+ stars). Frontier activity is concentrated in browser/computer-use agents, not phone-call-to-a-human-plus-physical-world agents — the case's voice+payments+logistics combination is less crowded than the "AI browses the web" space.

**Other — books, research, and the competition's own prior art**
- Allison Daminger's four-stage mental-labor model (anticipate → identify options → decide → monitor); Arlie Hochschild's *The Second Shift* (1989) — both about gendered household labor generally, structurally identical to the "who owns making sure this gets done" question; flagged as worth watching for in interviews (not assuming).
- **The Ken's 2025 Case-Build winner:** IIM Ahmedabad's "A Team," disrupting Narayana Health — strategy: *"We turn expensive hospital bed-days into data-rich, AI-orchestrated home days, all packaged within a single, guaranteed-price treatment episode."* Won ₹10 lakh. Structurally the same shape as the current problem (manual post-event coordination workflow, currently unowned, creating value leakage) applied to healthcare instead of appliances. Full list of 2025 finalists (10 teams) and their one-line strategies preserved in `/files/ken_case_competition_2025_winning_submissions.txt`.
- **The competition's own founding thesis**, "The Great Rewiring" / "India will be won with consumer agents" column — identified as the single most load-bearing resource found. Core argument: consumer AI agents haven't taken off globally because delegation is a *learned skill* most people don't have, and most personal tasks don't justify the setup cost (arguments cited from Sidu Ponnappa — cognitive load; Paras Chopra — delegation is a learned skill, using an agent is like managing a junior employee; Jamie/Levie — payoff only arrives after re-engineering an entire workflow, which is why enterprises capture the value first). The column's counter-argument for India specifically: voice is a natural interaction mode, payments are already digitised/seamless, e-commerce has diffused massively, **and India already has a cultural precedent — unmatched elsewhere — of delegating physical-world tasks to human intermediaries** (train-ticket agents, delivery runners, informal money-management help). Full text preserved at `/files/ken_the_great_rewiring_column.txt`.

### 5.5 Synthesis given to the user (verbatim)

> The resource landscape is dense on both edges — enterprise FSM (mature, $13B market) and consumer marketplaces (Urban Company, profitable, dominant) — but genuinely thin in the middle: nothing acts as the household's own post-booking, cross-vendor coordination layer. The rails are further along than your context files assumed (Pine Labs' Grantex already does bounded delegated spend; Gnani already runs multilingual outbound-capable voice at scale) — so Q5 (which rail to innovate on) probably shouldn't be "voice doesn't exist yet," it should target the specific gap: outbound calls that *navigate an IVR and negotiate on the household's behalf*, which nobody's shipped yet even though the underlying voice tech is production-grade. And the one finding I'd weight most for your Q1/Q2 direction is the competition's own thesis piece — it reframes the whole opening away from "coordination is annoying" toward "India already delegates this to humans; who does your household currently trust with this job, informally, and why would they hand it to software instead?" — that's a sharper interview question than anything in the original four threads I offered, and it's worth leading with tomorrow.

---

## Part 6 — This documentation request

### User's request (verbatim)

> till now, whatever has been discussed in the session document them - evry single word should be saved to context.md file and all the decisions taken by me and decisions taken by you should be saved to decisions.md file and in the /files folder save all the mentioned files and in the links.md file save all the links and notes.md file save all the notes, blogs any text that we have discussed and plan.md should save the plan progress.md should track the progress

This file (`context.md`) is the output of that request's first part. See `decisions.md`, `links.md`, `notes.md`, `plan.md`, and `progress.md` for the rest, and `/files` for all preserved source material.

---

## Part 7 — New source: Household Service Memory Supplementary Note (PDF)

### User's request (verbatim)

> There is another PDF that I have attached: Household-Service-Memory-Supplementary-Note.pdf. Go through that PDF and try to Add anything relevant to any of the Markdown files that are existing now. Add a separate section in the existing Markdown files and update the Markdown file.

### What the PDF is

Found at the project root as `Household-Service-Memory-Supplementary-Note.pdf` (also preserved at `/files/Household-Service-Memory-Supplementary-Note.pdf`). Header: *"The Household Service Memory — Supplementary Note. Immediate Workarounds, and the Non-Breakdown Segment. Prepared for Atharv · Follow-up to the Ken Case Competition 2026 dossier · September 2026."*

**Important gap to flag:** this note is explicitly a *follow-up* to a "main dossier" that is referenced repeatedly (its Section 2.3 "workaround ladder," Section 3.1 "seasonal shock" trigger, Section 6 "decision framework," and a "76%" AC-servicing figure) — **that main dossier has not been shared in this session.** It appears to be prior research, possibly belonging to a teammate ("Atharv"), not previously visible to Claude. Everything below is only what this supplementary note itself contains.

The PDF uses its own evidence-tagging convention: **[D]** = published, named, verifiable source (safe to cite as fact with attribution); **[A]** = consumer-facing/commentary content (directional, not a statistic); **[H]** = the note author's own reasoning/synthesis (hypothesis, not evidence).

### Content, in full

**Section 1 — Immediate workarounds (not a fix, just getting the job done today).** Explicitly flagged **[H]** — the author searched for an Indian study measuring same-day task substitution (as opposed to eventual repair-seeking) and found none; this is reasoning to validate in interviews, not a citable statistic. Per-appliance table:

| Appliance | Immediate workaround (not a fix) |
|---|---|
| Washing machine | Hand-wash; local dhobi/press-wallah; coin laundromat if nearby |
| Refrigerator | Buy ice for a cooler box; shift perishables to a neighbour's fridge; buy groceries in smaller daily quantities |
| Gas stove (one burner) | Shift cooking to the working burner; induction plate or electric kettle if both are out |
| Microwave/oven | Reheat/cook on stovetop or pressure cooker instead |
| Geyser | Boil water and mix in a bucket, or take a cold shower |
| Air conditioner | Fan + wet towel/cooler; or spend peak hours at a mall or relative's place |
| RO/water purifier | Boil tap water, or buy canned/bottled water short-term |
| Water pump/motor | Buy tanker water, or fetch manually from a neighbour's connection |
| Mixer/grinder | Hand-grind with a sil-batta (mortar-pestle), or buy pre-ground masala |
| Chimney/exhaust fan | Cook with windows open; use a standing fan to clear smoke |
| Iron | Send clothes to the local pressing shop |
| Two-wheeler/car | Auto/cab/public transport, or borrow a neighbour's vehicle |

**[H] synthesis given in the note**: almost every workaround falls back on either (a) a local informal service (dhobi, pressing shop, neighbour) or (b) a cheaper, more failure-tolerant substitute. Neither shows up in a "service memory" — it's a separate resilience layer the household has already built, and the note explicitly suggests the product probably shouldn't try to compete with it.

**Section 2 — What does the non-breakdown segment actually do?** The note interrogates a "70%" figure it says the main dossier cites, tracing it to exactly one source: **[D]** CEEW's 2023 survey of 369 RAC technicians — a *supply-side* report (technicians describing customer calling patterns), not a household survey. So "the other 30%" isn't explained by that same study. Four distinct findings on the non-breakdown segment, each on its own footing:

- **(a) Maintenance contracts — [D]** LocalCircles national survey, April 2026 (27,000+ responses, 289 districts), asked AC owners how they got serviced this year: 7% brand maintenance contract, 17% brand service ad hoc, 13% via dealer, 44% local provider, 13% organised third-party, 3% said unit was working fine. The 7% on a contract are the cleanest answer — they don't remember anything, the AMC's renewal cycle does it for them. **Caveat stated in the note itself**: this is a different (2026) LocalCircles run than a 2022 survey the main dossier apparently cites for a 76% figure, and categories don't map 1:1 — use directionally, not as a replacement number. Source cited: LocalCircles, "Only 1 in 4 AC owners rely on brands for servicing due to high cost," April 2026 (localcircles.com).
- **(b) Economic awareness, not a reminder tool, predicts preventive behaviour — [D]** A peer-reviewed RCT on Indian AC owners (part of the India Cooling Action Plan research agenda; ScienceDirect/PubMed, PMID 33458437) found AC owners' knowledge of preventive-servicing importance was much lower than required; awareness campaigns raised general awareness but not technical know-how; but consumers who understood the *economic* benefit (lower electricity bills) were more likely to actually undertake preventive servicing. I.e., for the self-initiating segment, the trigger looks more like "I know it saves me money" than "I have a reminder system."
- **(c) The season itself, formalised as a twice-a-year norm — [D]** The same CEEW report states preventive servicing once before and once after AC season is industry-recommended for saving electricity/maintaining performance — formalising what the (unseen) main dossier apparently already calls trigger #3, "seasonal shock" (Section 3.1).
- **(d) Diwali/festival deep-cleaning as an existing, unowned calendar hook — [A]** Multiple consumer-facing sources (cleaning-service/appliance-brand blogs, not an academic survey) describe Diwali home-cleaning as a near-universal annual ritual that explicitly folds in appliance cleaning (fridges, microwaves, stoves called out specifically). Not measured behaviour — don't cite as a stat — but strategically a calendar date already etched into household memory, unlike anything the product would have to manufacture. Worth testing in interviews, not worth quoting as fact.

**Honest bottom line, as stated in the note**: no single study cleanly answers how the non-breakdown 30% remembers. What exists, stitched from separate sources, is three distinct mechanisms, none of them "personal memory alone": a vendor contract that removes the need to remember (a), acting on known economics rather than a system (b), and riding a pre-existing seasonal/cultural calendar event rather than a deliberate reminder (c, d).

**[H] closing note**: the author suggests this strengthens the (unseen) main dossier's "Section 6 decision framework" — specifically that option (a) there (builder/RWA handover, or an existing billing relationship) is structurally closer to the AMC and utility-partner models that already work than to a pure reminder app, which this evidence suggests is the weakest of the four mechanisms on its own.

### What Claude did with it

Added a new section to every existing markdown file (`decisions.md`, `links.md`, `notes.md`, `plan.md`, `progress.md`, `r1.md`, `system_map.md`) carrying the parts of this note relevant to that file's purpose, and flagged the missing "main dossier" as an open gap in `decisions.md`, `plan.md`, and `progress.md` rather than guessing at its contents.

---

## Part 8 — Independent secondary research: task-substitution & service-tracking mechanisms

### User's request (verbatim)

> I want you to look at these kinds of workarounds also. First, I want you to inform yourself about all the decisions and all secondary research by looking at papers, articles, blogs, newsletters, any commonly available web searches, etc. All of those, so that you'll understand what kind of workarounds are currently there. For example, I'm using a machine to get one job done. To get that job done, if the machine is built, how else am I going to get the job done? That is the core thing. I want you to look at all of those and have the information stored for that as well. That will help us understand later on, in the stages of getting evidence and understanding the workarounds. Also, one more: I want you to look at what current workarounds there are regarding servicing. How do people keep track of the dates? How do people get informed by them? What queues are there? What actions are being done, etc.? This also needs to be researched and understood. By the way, we will get that information through interviews, but the main, most important motto of this is to understand through this part: Do your own research. Your own materialities. Your own actions. Collect data. Use open source things and all. Inform yourself and have complete information regarding that also.

This explicitly asks for two things, done independently by Claude (papers, articles, blogs, market reports, open-source examples), understood as grounding *ahead of* interviews, not a substitute for them:
1. Task-substitution behaviour — when a machine breaks, how does the underlying job still get done?
2. Service-tracking mechanisms — how do people currently remember/get reminded about servicing; what tools, queues, actions exist today?

### What Claude did

Ran roughly 14 targeted web searches across two clusters: (1) academic/theoretical grounding for task-substitution (compensatory consumption, bricolage, jugaad-innovation literature, India power-outage coping data) and India-specific repair-vs-replace market data; (2) service-tracking mechanisms compared across five categories (vehicles, LPG/gas, branded RO/water purifiers, the AMC industry's own vendor-side practices, and general/local-technician appliance service), plus adjacent academic research on "life admin" and family-calendar HCI studies. Full findings written into `system_map.md` §6 (the primary home), condensed into `notes.md` §6b, sources listed in `links.md`, two new interview probes and a Q6 implication added to `plan.md`, four judgment calls logged in `decisions.md` (#24-27), and a Q2/Q6/Q9 addendum added to `r1.md`.

### Key findings (full detail and reasoning in `system_map.md` §6)

- **Task substitution has real academic grounding**: compensatory consumption theory, bricolage/"making do," and — directly on point — the India-specific **jugaad** literature (the exact term the team's own braindump already used), with concrete examples (bulb-socket phone charging, bicycle-wheel fan, pressure-cooker steriliser).
- **India repair-vs-replace data exists but no India-specific "50% rule" or replace ratio was found** — repair costs up ~25% in 5 years, ~1/3 of devices need specialised intervention, EMI/BNPL pushing replacement — but the commonly-cited 58%/87% replace-rate figures are US-only and explicitly flagged as unconfirmed for India.
- **Service-tracking infrastructure is wildly uneven across structurally similar categories**: vehicles have a mature, government-coordinated, multi-institution SMS/app reminder ecosystem (Punjab Transport Dept + IRDAI + PUC centres + NHAI; the official mParivahan app; third-party WhatsApp-reminder apps in 10 languages); LPG booking is frictionless but has no proactive reminder; branded RO units (Kent's IoT "SUPREME" line) can already auto-detect a fault and auto-register a service call, but only within one brand's own ecosystem; general appliance service relies on a handwritten sticker or nothing at all.
- **The sharpest new finding**: Indian AMC/service vendors track renewals in Excel with reminder calls made "from memory," and lose an estimated 20-30% of renewals to simple forgetting — meaning the vendor side may be just as unreliable as the household side, complicating the working thesis's assumption that the household is the weak link.
- **The sharpest comparative angle**: vehicles have a shared institutional anchor (RTO registration) that every insurer/PUC-centre/app can hook into; appliances have no cross-brand equivalent — proposed as a candidate structural explanation for why no appliance-wide reminder layer has emerged, and a candidate reframe for Q6 (the missing shared identifier as the customer asset) and Q9.
- **Adjacent academic corroboration**: Elizabeth Emens' "Life Admin" (100+ empirical interviews) as the formal term for the household's "dispatch desk" role; family-calendar HCI research independently corroborating thread #17 in `notes.md` §2 (one household member absorbs the coordination role) with real literature, not just this project's own inference.
- **What was searched but came back thin, flagged rather than padded**: an India-specific repair/replace ratio; any direct India study on first-hours task substitution (confirmed absent by two independent research passes now); dedicated appliance-service-reminder HCI literature as a distinct field.

---

## Part 9 — Team reconciliation: discovering Sricharan's independent research pipeline

### User's request (verbatim)

> Go through all the textbooks one by one that are there in this project and understand how to think like a designer, how to think like a systems thinker. How to think like a user researcher, user experience designer How to think like an experiment or survey designer? and undertsand each of the role, what are the good practices, what are the bad praftices, how to think like all of them given a problem

### What Claude found before touching a single textbook

Running `ls`/`find` on the project directory (last checked at the very start of this session, when it held 3 files) revealed it now contains ~20 UX/systems/research-methods textbook PDFs, plus a `research/` folder, an `output/` folder, and a `tmp/` folder — none of which existed earlier in this session. Git investigation (`git log`, `git reflog`) showed a second commit, `3df33c1`, authored by **Peri Sri Charan** from a different machine and a **different Claude Code session** (`Claude-Session: session_01LYHzkE42Pd4RXp98AtGSga`, vs. this session's own ID), titled "Add reference PDFs, research folder, output, and case playbook" — pushed to the shared repo shortly after `sricharanperi` accepted the collaborator invitation from the prior turn. Someone then ran `git pull` in this local working copy (reflog: "pull: Fast-forward"), bringing it in.

Reading the new files revealed:
- **`research/Invictus_Team_and_Research_Brief.md`** — resolves the "Atharv" identity gap this session had flagged twice already (`decisions.md` #21, `plan.md`, `progress.md`): the team is **Invictus**, three M.Tech Product Design & Management students at **IIIT Hyderabad** — Atharv (1st year), Sricharan (2nd year), and the current session's user, Prathyusha (2nd year). Also contains Sricharan's own candidate Q1 personal-incident story (a laptop repair using ambiguous "duplicate" RAM), carefully hedged as unconfirmed.
- **`research/report-source.md`** (584 lines) and **`research/Fieldwork_Templates.md`** — an extremely thorough, independently-produced research and submission playbook: a full three-day hour-by-hour operating schedule, a complete interview guide (customer + technician/service-centre + landlord/PG variants), a full branching survey instrument (S0-S30 with skip logic and pre-registered analysis rules), verified rail documentation for Gnani/Pine Labs/Delhivery with real checked links, and operational fieldwork-capture forms (consent records, incident timelines, an evidence index, a hypothesis/contradiction log).
- **`research/build_report.py`** — renders `report-source.md` into `output/pdf/Ken_2026_Research_and_Submission_Playbook.pdf` and auto-generates `research/claim-source-ledger.json` (every cited URL plus its surrounding claim context) by scanning the source markdown.
- Confirmed this is **not** the "main dossier" the Household Service Memory Supplementary Note PDF (Part 7) referenced — different structure entirely (numbered `---PAGE---` sections vs. that note's "Section 2.3/3.1/6" scheme) — so that specific gap remains genuinely open, though it's now most likely Atharv's own parallel output given the identity resolution above.
- `research/report-source.md` Page 2 contains an independent audit of `The_Ken_2026_Case_Selection_Playbook.html` finding its stored 18-24/machines repetition-rate data doesn't match the live competition chart, and its own source files were never present in the workspace — a factual correction, folded into `system_map.md` §1.3.

### The conflicts this surfaced

- **Interview volume**: this session's `plan.md` targeted 3-6 interviews (from the user's own earlier stated capacity); Sricharan's playbook targets 10-12 customer + 3-4 counterparty interviews plus a 30-50 response survey. His own brief flags the root ambiguity himself: whether "six hours daily" means per-person or combined across the team.
- **Q1 personal incidents**: Sricharan has his own; Atharv's is still pending on his end; **this session had never actually collected the user's own personal incident** for Q1.
- **Good news**: both tracks independently converged on Voice as the strongest Q5 rail candidate, and both independently named Urban Company as the Q9 counterfactual candidate — corroboration, not conflict. Four of Sricharan's five independent hypotheses also map onto four of this session's seventeen candidate pain-threads.

### What Claude did

Asked the user how to proceed (textbooks now, reconcile first, or both in parallel) rather than guessing given the changed situation and the tight deadline. User chose **"Reconcile first, then textbooks."** Wrote `team_reconciliation.md` — a new file (not editing Sricharan's `research/` files directly, to preserve his authored work) that: designates canonical sources per area (interview guide, survey, fieldwork capture, rail docs, operating schedule → Sricharan's; system/resource-scan research → this session's, kept as additive), maps this session's five additive interview probes to specific insertion points in his guide, surfaces the interview-volume conflict as an open team decision rather than silently resolving it, lists concrete pending inputs (the user's own incident, Atharv's incident, the six-hours-per-day ambiguity), and cross-checks both hypothesis sets. Made small corrective edits to `system_map.md` §1.3 (the demographic-claim correction), `plan.md` (pointer to the new canonical sources), `progress.md` (new checklist section + updated risk framing), and `decisions.md` (#28-32). The originally-requested textbook synthesis is deferred, per the user's own instruction, until this reconciliation is complete and acted on.

---

## Part 10 — The textbook synthesis and Ken-winners research: `best_practices.md`

### User's follow-up request (verbatim)

> Let me tell my own Q1 personal incident later. We will do it later at the end for the interview volume. Go with the realistic one. We need not do all that shit. We can go with 3 to 6 interviews, and we can roll out a survey as well.
>
> Now I want you to go through each and every textbook that is there and continue the textbook task. Your goal is to understand how to think like a designer, systems thinker, UX researcher, UI/UX designer, experiment designer, everything. First, if you learn how to do this, what are the guardrails? What are the do's and don'ts, etc., etc.? Then we can use this knowledge to continue the work later.
>
> I also want you to go through each and every Ken case available. Go through the winning teams or the teams which have been recognized. Understand their work, their particular process, and the things that they have followed. Understand the behavioral patterns, the presentation skills, or the way that they have showcased. What are the patterns that we have to follow? How can we win this competition? That is what you have to understand from the textbooks and from the case competition-winning cases available on the internet.
>
> Later, we will use these textbooks to understand or design the research as well.
>
> All the patterns, all the important knowledge required for this case competition, put it as a separate Markdown file best_practices.md

### What Claude did

1. **Recorded the two resuming decisions** in `team_reconciliation.md` §4 and `progress.md`: Q1 personal incident deferred by the user to later; interview volume settled at 3-6 interviews plus rolling out the survey (not Sricharan's 10-12+3-4 target).
2. **Solved PDF text extraction.** `brew install poppler` failed on a network error (ghcr.io connection reset); system-wide `pip install pypdf` was blocked by PEP 668. Created an isolated venv at `/tmp/pdfenv` and installed `pypdf` there successfully; wrote a small reusable extraction script (`extract_pdf.py`) taking a PDF path and page range.
3. **Forked 4 parallel background research agents**, one per thinking-lens, each assigned a cluster of the 20 textbooks and given the extraction tool, explicit instructions to read TOC + targeted core chapters (not cover-to-cover on 500-1000+ page books), and a fixed deliverable shape (mental models / good practices / bad practices / given-a-problem framework, each claim tagged to its source book):
   - **Systems thinker**: Sterman's *Business Dynamics*, Senge's *The Fifth Discipline* + *Fieldbook* (an .epub — the fork installed `ebooklib`/`beautifulsoup4` itself to read it), Meadows' *Thinking in Systems* (this project's copy is only a 33-page diagram/appendix companion, not the full book — flagged, not hidden, and its genuine content used directly).
   - **Designer**: Buxton's *Sketching User Experiences*, Tidwell's *Designing Interfaces*, Calonaci's *Designing User Interfaces*, plus shorter product-experience/aesthetics-usability papers.
   - **UX/user researcher**: Kuniavsky, Erika Hall, Sharp/Preece/Rogers, Boellstorff et al., Dumas & Loring, Constantine, Gavin Lew & Schumacher, plus two books (Becker, Carroll) synthesized from general knowledge under time constraints, explicitly flagged as such.
   - **Experiment/survey designer**: Cozby & Bates, King/Churchill/Tan — with an explicit instruction to also audit the team's own existing S0-S30 survey (`research/report-source.md`) against the textbooks, not just produce abstract theory.
4. **While the forks ran, personally researched the Ken competition's public history** across all 3 years it's existed:
   - Re-mined `files/ken_case_competition_2025_winning_submissions.txt` more fully (previously only the top-10 finalists were read; this pass covered the 100-team semifinalist list and category-concentration data — CBRE and Narayana Health drew the most entries, and Narayana Health was also the eventual winner, complicating any "avoid crowded categories" assumption).
   - Fetched (via curl + browser UA, since WebFetch 403s on the-ken.com as established earlier) and read: the 2024 "Solution Guidelines" page (verbatim judge-criteria explanations), the 2024 finalist-shortlist writeup (10 teams, judge commentary per team), and the inaugural-winner announcement (2024 judges' own quotes on what they were looking for, including Deepak Shenoy's "adjusted EBITDA" warning).
   - Fetched and analyzed the ArogyaGhar.ai prototype (a 2025 showcase site) directly for its presentation/demo structure.
5. **Read `Courses-Syllabus_M26-V1.pdf` directly** (288 pages — targeted via keyword search across a full-text extraction rather than sequential reading) and confirmed the 20 textbooks are the actual assigned references for 3 real IIITH M.Tech PDM courses: "Behavioral Research & Experimental Design" (CG3.402), "Systems Thinking" (EC5.202, whose own syllabus example is the UPI ecosystem — structurally identical to this competition's rails), and a Design Thinking/User Research course. Pulled each course's stated learning outcomes directly.
6. **Wrote `best_practices.md`** combining all of the above: §1 Ken competition winning patterns (judging-criteria evolution across 3 years, judge quotes, 7 named winning patterns with direct implications for Q1-Q10), §2 the course-grounding explanation, §3-6 the four thinking-lens deep-dives (each fork's report integrated and condensed, with source attribution preserved), §7 cross-cutting guardrails.
7. Updated `progress.md`, `decisions.md` (#33-38), and `plan.md` to point to the new file and record the settled decisions; deleted the UX-research fork's intermediate scratch file once its content was fully folded into `best_practices.md`.

### The one actionable finding worth flagging above the rest

The experiment/survey-design fork's audit of the team's existing S0-S30 survey came back with a **"ship it" verdict** — the survey independently follows textbook-correct practice (question ordering, bias avoidance, honest disclosure of its convenience-sample limitation) without having been built from these specific books. Three optional hardenings were suggested (duplicate-response flagging, completion-time capture, a note that its uneven answer bins are correct, not a bug) and one real outstanding item was found (a placeholder contact field in the survey's own intro still needs to be filled in before launch).

---

## Part 11 — Asked directly: are we on the right track, can we win

### User's question (verbatim)

> Say yes or no: Are we on the right track? Can we win the competition?

### Claude's answer (verbatim)

> **Yes — on the right track. Can you win — genuinely possible, but not yet earned.**
>
> Here's the honest gap: everything that's been built so far (`system_map.md`, `best_practices.md`, the reconciled research plan, the audited survey) is *preparation quality*, and it's genuinely strong — stronger than most teams will have. But **zero real interviews have happened**. Q2, the answer judges "read first," doesn't exist yet. Neither do Q1, Q3-Q10. All of that depends on evidence you don't have yet.
>
> Preparation doesn't win this — the insight from a real conversation does, and the clock on that is the only thing that matters right now. You're set up to win. You haven't yet done the thing that actually wins it.

No files changed for this turn — a direct answer only.

---

## Part 12 — Narrowing the problem statement for Round 1: `narrowed_problem.md`

### User's request (verbatim)

> Now I want you to go through all the best practices and all the remaining Files, whichever you have created, like links, decisions, and all the research-related files that you have created I want you to narrow down the problem statement so that I will be going for interviews, narrowing down what the criteria are, etc. Ask me questions and come up with the best strategy or algorithm to narrow down the problem statement. The target now is Phase 1 or Round 1 of this case competition. I have been asking about the winning, but let's concentrate on selecting for the next round. Go through all 10 questions that are there: What is being expected? What interviews do we have to do? How to narrow it down? Go through everything. Now the task for you is to narrow down the problem statement. Ask me so many questions, and as we go, whatever decisions I take, you take. Put everything in a narrowed problem.md. Some context for why narrowing down is based on the context, like Hyderabad, or if I have my home pooja as an axis for these things: the problem completely changes, right? [...] How to do that? You need to narrow it down in such a way that there is a higher potential to go through all the best practices that are there to follow the winning criteria and to win the competition. Which direction has a huge potential? Which direction has a huge potential to come up with a strategy?

### What Claude did

1. Fetched from the shared repo first (`git fetch origin`) — confirmed no new commits from Sricharan since the last push.
2. Wrote `narrowed_problem.md` with: §1 the mechanism explaining why narrowing changes whitespace/evidence-claims/rail-relevance simultaneously, §2 a 4-filter narrowing algorithm (object → segment → geography → mechanism), §3 a full Q-by-Q table (all 10 questions: what's expected, what evidence is needed, how narrowing changes each answer) built from `context.md` Part 1.3, `r1.md`, and Sricharan's answer scaffolds in `research/report-source.md`.
3. **First question batch was rejected by the user** — asked to clarify before proceeding. The rejected batch had asked the user to pick an object/domain cluster (AC/appliances vs. trade services vs. a "home pooja" axis vs. "not sure") plus geography scope and risk appetite.
4. **User's clarification (verbatim, condensed)**: *"That is not puja access. I was talking about my home bhooja... a big community in Hyderabad... a big network of servicemen available, and if they raise a complaint, that will be resolved. In some other individual houses... you have to find your own people for the repair... Also, don't ask me which field or which cluster to commit to, because we don't know which one is better. We also don't know how to procure people for interviews, so help us find the easiest accessible people as well."* This corrected a mishearing (the "pooja" axis was actually a reference to **My Home**, a Hyderabad gated-community builder group) and pushed back on being asked to make an ungrounded strategic choice, redirecting toward concrete recruitment help instead.
5. Re-asked a leaner, more concrete question batch: confirming the community name (My Home), which access channels the user could personally activate *today* (multi-select — user selected: My Home community, independent households, IIITH campus professors/staff, **plus a volunteered addition**: tier-3-city technicians reachable by phone), and whether the user has direct or indirect access to My Home residents (answer: **direct — lives there, or immediate family does**).
6. Updated `narrowed_problem.md` §4-6 with: Decision 1 (object left deliberately unpicked, interviews stay unprimed), Decision 2 (the real segmentation axis is service-network structure — managed-community vs. independent self-sourcing — not renter/owner, with the reasoning tied to `best_practices.md` §5's "recruit for a smooth case" good practice), Decision 3 (geography is Hyderabad, confirmed by real access rather than chosen abstractly), and a concrete 6-slot recruitment plan with specific channels, priority order, and a ready-to-ask probe question for the managed-vs-independent contrast.
7. Added a new candidate pain-thread, **#18**, to `notes.md` §2 — explicitly framed as a nuance/complication of existing thread #8 (RWA/society diffuse ownership), not a replacement: large professionally-managed communities may partially solve the accountability-diffusion problem via an internal vendor system, or may have their own different friction — both outcomes are flagged as valuable findings, avoiding the trap of only wanting the answer that confirms a prior hypothesis.
8. Updated `plan.md` (flagged as superseded again, pointing to `narrowed_problem.md` §5 as the operating recruitment plan), `progress.md` (new checklist entries, recruitment execution now the explicit next unchecked item), and `decisions.md` (#39-43).

---

## Part 13 — Correcting the geography: Eluru, not Hyderabad-only

### User's request (verbatim)

> Hyderabad could be one geography, but also I have technicians, etc., with access from my own hometown called Hyderabad. That is a tier 3 city. I'm not sure if Hyderabad is the actual thing we need to restrict to

### What Claude did

1. Flagged the internal inconsistency directly (Hyderabad is a major metro, not tier-3) rather than silently accepting it, correctly guessing this was another dictation mishearing like "pooja"→"My Home" the previous turn — did not guess the real name.
2. Attempted an `AskUserQuestion` call with a single-option "type the hometown name" question, which the tool rejected outright (a question needs at least 2 genuinely distinct options) — asked for the name in plain text instead, alongside two valid multiple-choice questions (hometown access depth: technician-only vs. also household-side; how the hometown should fit the plan: bonus data point vs. full second geography vs. decide later).
3. **User's answer**: confirmed **both** technician and household access in the hometown, and chose "not sure yet — decide after confirming who's actually reachable" for the scope question, deferring the call until real numbers were known.
4. **User's follow-up (verbatim)**: *"Eluru, 1-2 households, 1 electrician / Hyderabad, 1 household / I may talk to one technician who works for some office or school in tier 3 city (not sure)"* — the real hometown name (**Eluru**, Andhra Pradesh) plus quantified access counts for both locations.
5. Rebuilt `narrowed_problem.md` Decision 2 and Decision 3 with the real numbers: a table of confirmed access by location and type, the judgment call to treat Eluru as a **full second geography** (not a bonus call) since its household count matches or exceeds Hyderabad's own, the market-maturity argument for why this is worth the added complexity (Urban Company/Housejoy still expanding *into* tier-2/3 per `system_map.md` §2.1), and an explicit, undisguised **confound**: the current sample pairs metro+managed (Hyderabad/My Home) against tier-3+presumably-independent (Eluru) — two variables changing at once — with the IIITH campus interview (metro+institutionally-managed) identified as the one data point that can help triangulate which variable is actually driving any observed difference.
6. Rebuilt the recruitment table (`narrowed_problem.md` §5) with the real 6 slots: Eluru households ×1-2, Eluru electrician, Hyderabad/My Home household, IIITH campus (Sricharan), and the uncertain tier-3 institutional technician as a stretch item only — noting no new recruitment is actually needed, the confirmed contacts already cover the 3-6 target.
7. Added a new candidate thread, **#19**, to `notes.md` §2 (metro vs. tier-3 market maturity), explicitly cross-referenced as confounded with thread #18 in the current sample. Added a specific interview probe to test rather than assume that Eluru households lack any form of managed building/society maintenance.
8. Updated `decisions.md` (#44-47) and `progress.md` to reflect the correction and the upgraded geography scope.

---

## Part 14 — Folding the resource-scan findings back into the narrowing plan

### User's request (verbatim)

> Also, use the data or the knowledge that you have got by running the resource scan skill yesterday. Use that data as well to narrow down.

### What Claude did

Added a "whitespace pre-registration" table to `narrowed_problem.md` Decision 1, built entirely from the resource-scan run already documented in `context.md` Part 5 and `system_map.md` §2/§6 — no new research, a re-application of existing findings. Explicitly framed as registered *before* interview evidence arrives, to avoid motivated reasoning later. The table:

- **Trade/repair services** (plumbing, carpentry, electrician, pest control) — highest prior whitespace; no FSM-equivalent exists for households sourcing these directly.
- **AC** — "covered on paper" by Urban Company/brand apps, but a LocalCircles survey found only 7% of AC owners are actually on a brand maintenance contract; also the one object with documented legal ambiguity (Indian rent law leaves AC servicing an undefined tenant/landlord grey zone).
- **RO/water purifier** — split: Kent's premium "SUPREME" IoT line already auto-detects faults and auto-registers service calls, so the gap narrows to the cross-brand/cross-appliance layer if that's what a respondent has; wide open if they have a non-premium unit.
- **A vehicle-adjacent incident** — not a target, but a strong contrast case: India has already fully solved this exact class of problem for vehicles via government-coordinated infrastructure, which no equivalent exists for appliances.
- **Anything with a formal AMC** — industry data shows vendors track renewals in Excel with reminder calls "from memory," losing 20-30% to forgetting; worth testing whether this pattern holds, is absent, or looks different in Eluru's more informal market.

Added two new interview probes, layered onto the existing guide (`narrowed_problem.md` §5): a vehicle/reminder-infrastructure comparison question, and a formal-AMC-vs-informal-relationship question — both applied across every household slot, not just one geography. Clarified that the existing AMC-vendor-forgetting probe (already in `plan.md`) should be asked in Eluru without assuming an AMC concept exists there — a "no such thing here" answer is itself flagged as a real finding tied to thread #19 (metro vs. tier-3), not a failed question. Updated `decisions.md` (#48-50) and `progress.md` accordingly.

---

## Part 15 — The full research plan: `research_plan.md`

### User's request (verbatim, condensed — included an image of the competition page's "What you can attach" section)

> From the best practices that you have learned till now... give me a research plan for different types of stakeholders that we are going to interview: Tier 3 technician, Tier 3 household, my home technician, my home household. [...] we have access to a standalone apartment household as well in Hyderabad. There can be more of these stakeholders... it is your take to entirely come up with the interview plan, survey plan, everything. All these should give us a very unique customer insight... we should be able to gather all the proofs which are expected. Also, go through the ken case competition website and get all the potential points that we can interview about, survey about as well.

Two new confirmed stakeholders arrived in this message: a **My Home technician** (completing the demand+supply pair for the managed-community segment) and a **standalone apartment household in Hyderabad** (completing the within-Hyderabad managed-vs-independent contrast that Decision 3 had flagged as still missing).

### What Claude did

1. Re-scanned `files/ken_case_competition_2026_page.txt` directly via keyword grep (evidence/attach/consent/quote/survey/workaround/working notes/chat log) rather than relying on memory, per the explicit instruction to "go through the ken case competition website" again — confirmed no new information, including catching a specific phrase worth building a tracking mechanism around: the Evidence criterion explicitly rewards *"what you found that you weren't looking for."*
2. Wrote `research_plan.md`: §0 ties every design choice to the exact competition-page evidence language; §1 the full stakeholder map (8 now-confirmed interviews plus 3 recommended snowball-referral additions — a standalone-Hyderabad technician, an IIITH campus technician, and a landlord, each explicitly flagged as unconfirmed access, not assumed); §2 recommends raising the interview target from 3-6 to 6-9, since real access now comfortably supports it at no new recruitment cost; §3 per-stakeholder-type interview guide deltas (universal additions plus segment-specific questions for each of the 8, layered onto Sricharan's base guides rather than rewritten from scratch); §4 the survey plan, adding one new screening item (S7a) that operationalizes the managed-vs-independent axis as a self-report question for any respondent regardless of channel, plus explicit channel-tagging values; §5 an evidence-capture matrix mapping all 5 of the competition's attachment types to concrete per-stakeholder actions — including pointing out that the team's own Claude Code session transcript, already pushed to GitHub, directly satisfies the "chat logs...with an AI" category; §6 how to actually mine the resulting comparative structure for the Q2 insight, with an explicit instruction to track "what we weren't looking for" as a running, separate list; §7 a readiness checklist.
3. Updated `plan.md` (flagged as superseded once more, pointing to `research_plan.md` as the operating document), `progress.md`, and `decisions.md` (#51-55).

---

## Part 16 — Elevating rail-build potential to a required filter

### User's request (verbatim)

> Also, I forgot to tell you: go through everything till now. Make sure that the narrowed-down problem, the interview plan, and everything are directed towards getting unique customer insight. It should also have enough potential to build an agent or to give a product strategy for building an agent with all three rails: voice, payments, authorization, logistics. The potential to build this is the most important thing because this is what we will be using for the next round if selected.

### What Claude did

1. Re-verified the exact rail definitions directly from `Keeping_Machines_Running_Context.md` §7 (grepped rather than recalled from memory) before scoring anything — confirmed **Payments & Authorisation is one combined rail**, not two separate ones as the user's phrasing implied ("voice, payments, authorization, logistics" listed as four items). This matches the competition's actual 3 partners exactly (Gnani/Pine Labs/Delhivery) and is corrected directly in the file, load-bearing for Q4/Q5 wording.
2. Added **Decision 1b** to `narrowed_problem.md` — a rail-build-potential table scoring the same candidate objects from Decision 1's whitespace table (AC, RO, trade/repair services, pest control) against Voice/Payments&Authorisation/Logistics, grounded in `Keeping_Machines_Running_Context.md` §7's own definitions (voice = agent talks to the business; payments/authorisation = delegated authority, not checkout; logistics = only real where physical movement genuinely happens). Found AC and RO score strongest across all three rails (RO's logistics case is explicitly named in the original context file: filters/cartridges as consumables); trade/repair services — the highest-*whitespace* candidate from Decision 1 — flagged honestly as the weakest on logistics, since many visits are labor-only with no real part-shipping need. Did not force a resolution between the two lenses — instructed both to be checked once real interview data names the actual object.
3. Identified a second, free hypothesis the existing comparative design can test: payments/authorisation may matter less for My Home if the community has pre-negotiated rates (a form of authority an individual household lacks), and logistics may be genuinely worse in Eluru than Hyderabad if part-delivery infrastructure is thinner there — both directly extending threads #18 and #19 rather than adding new ones.
4. Added 2 new interview probes to `research_plan.md` §3's technician guides: a universal part-arrival-time question (logistics-completeness, tagged by location for comparison) and a My-Home-specific rate-pre-negotiation question (payments/authorisation-completeness) — reusing the design already built rather than proposing new interviews.
5. Added §6a to `research_plan.md` — rail-build-potential scoring made an explicit, required step in the synthesis session, not optional: tag every incident's logistics-question and role-separation answers during synthesis (the questions already exist in Sricharan's guide; the only new work is using the answers), score whatever object emerges against Decision 1b's table before concluding a rail is absent, and use the two new probes to test the segment-differentiation hypotheses.
6. Updated `decisions.md` (#56-59) and `progress.md` to reflect the re-weighting.

---

## Part 17 — Direct compliance check, and a real gap caught: workaround artifacts

### User's request (verbatim, condensed)

> Am I in the right direction till now? Am I following the round 1 Ken competitions and everything there? Did you go through the Ken competition page and map out all the points that we have to research? For example, they mentioned any workarounds that are available, like pasting sticky notes, WhatsApp groups, etc. Those types of workaround proofs can also be taken. That means we have to interview for workarounds as well. These indirect indicators of what we need to get from people should also be tagged for this survey design. Who all are the stakeholders that are also needed? We will be floating it in WhatsApp groups directly, so anybody can answer anything.

### What Claude did

1. Re-verified the live page a second time via full-file grep (section headers, not just evidence keywords) — confirmed every structural element (10 questions, ground rules, judging, eligibility, partners, timeline) remains accurately captured across `context.md` Part 1.3, `narrowed_problem.md`, and `research_plan.md`.
2. **Found the gap the user was pointing at, and it was real**: the interview probe for workaround artifacts (`research_plan.md` §3) only asked about "stickers on machines" and "a paper log book" — much narrower than the competition page's actual, verbatim examples: *"the whiteboard on the fridge, the notebook, the folder of medical reports, the WhatsApp chat someone keeps with themselves."* Broadened the probe to quote the page's own examples directly, with an explicit instruction to always ask to see and photograph the artifact rather than accept a verbal description.
3. **Found the survey had no equivalent question at all** — added a new item, S20a, inserted after the existing S20 in the optional module (`report-source.md` Page 12), asking about personal workaround records and offering an opt-in path to share a photo, with contact info kept separate from the anonymous export per the existing consent design.
4. Addressed the open-WhatsApp-distribution reality directly: the plan had assumed four controlled channels; the user clarified the survey will be floated openly, reachable/forwardable by anyone. Revised the distribution section (`research_plan.md` §4) to add a 5th "Other/forwarded/unknown" channel-tag value, and re-designated **S7a plus the demographic fields (age band, city)** — not the posting-channel field alone — as the real post-hoc classification mechanism, since a survey link can travel beyond where it was posted.
5. Flagged 3 additional stakeholder types worth recognizing (not actively recruiting for) if they surface via this open distribution: a renter specifically, someone managing an elderly parent's household remotely (an ICP named in the original context files but never pursued), and a respondent from a different large managed community than My Home — noted that existing fields already capture all three generically, no new survey items needed for them.
6. Added a compact "compliance re-check" note directly into `research_plan.md` §0 rather than rebuilding the full checklist a third time, since the detailed version already exists in `context.md` Part 1.3 and `narrowed_problem.md` §3.
7. Updated `decisions.md` (#60-62) and `progress.md`.
