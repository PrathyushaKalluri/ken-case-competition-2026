# Progress Tracker — The Ken Case Competition 2026

Last updated: 2026-09-10. **Update the checkboxes as work actually happens — this file should always reflect current real state, not the plan's aspirational state (that's what `plan.md` is for).**

**Deadline: Sep 10, 2026, 11:59 PM IST — today.**

**2026-09-10 update: 7 real interviews were conducted (2026-09-08 to 2026-09-09) and pulled into this repo via git commits `300159a` and `57156c0` (audio + Whisper transcripts + a `scripts/transcribe/` pipeline the team built). This section below was rewritten from the actual transcripts, not from the plan. A first real draft of Answers 1-10 now exists at `answers_draft.md`, grounded in this evidence — it is NOT submission-ready; see its §0 for a real, unresolved compliance gap (no age-band/city/consent metadata was logged for any interview, even though verbal consent was captured on-recording for at least 2 calls). ~~No survey was fielded~~ — **wrong, corrected later the same day: a survey WAS fielded and collected 19 responses (12 qualified) between 8 and 10 Sep. It lived in Google Sheets/Forms and had simply never been exported, so it was invisible to a filesystem search. Raw data and analysis now in `evidence/survey/`; see risk item 5 below and `MASTER_CONTEXT.md` §17.** `survey_guide.md` and `research/survey_guide_qa/` remain design artefacts — the fielded instrument is a third, 21-question version, and its wording is the only one that matters now.**

---

## Phase 1 (Solution Assembly) — overall status: fieldwork done, drafting in progress, consent metadata outstanding

### Understanding & setup
- [x] Read all local context files (`01_group_braindump.md`, both `*context.md` files)
- [x] Fetched and parsed the live competition page — full Phase 1 requirements extracted and understood
- [x] Confirmed track: Product Strategy
- [x] Confirmed realistic fieldwork budget: 3-6 interviews in ~24-36h
- [x] Confirmed team's right-to-win access lenses (household / technician / landlord)
- [x] Produced a broad, unlocked divergence map (17+1 candidate insight threads) — explicitly not yet narrowed, per instruction
- [x] Grounded the divergence map with real external research (market facts, prior art, the competition's own founding thesis) via the resource-scan skill test-drive
- [ ] Interview guide finalized per lens (offered, not yet drafted)
- [ ] Interview tracking sheet set up (offered, not yet built)
- [x] Read and integrated Household Service Memory Supplementary Note (PDF) — added 3 new interview probes to `plan.md`, grounded facts to `notes.md` §6a, sources to `links.md`
- [ ] **Obtain the "main dossier"** referenced throughout that PDF (its own workaround ladder, seasonal-trigger section, and Section 6 decision framework) — not yet in this session's possession; flagged as a priority gap in `decisions.md` #21 and `plan.md`

### Stage 1 — Fieldwork
- [x] Household interview — **Call Amma** (25:02), 2026-09-08 — RO purifier, 3-day-pending repair, sole handler, "putting more than an hour every day" chasing it
- [x] Household interview — **Call Sai Kakki** (22:36), 2026-09-08 — washing machine inlet-pipe repair, known-technician-first, husband decides spend
- [x] Household interview — **Call Rk Sir** (24:26), 2026-09-09 — AC servicing via Urban Company, switched from brand (Lloyd) after franchisee chaos, cross-checked quote via a friend's contact
- [x] Household interview — **Call Sarala Aunty**, part 1 (17:03), 2026-09-09 — manages Vijayawada + Eluru properties remotely via a trusted carpenter-broker (Vishnu) who has his own tradesperson network
- [x] Household interview — **Call Sarala Aunty**, part 2 / follow-up (08:15), 2026-09-09 — drainage-issue deep dive, explicit sequential-fallback calling (Basha → Krishna → Rana)
- [x] Household interview — **Call 6128maggi** (24:54), 2026-09-09 — young Bangalore renter, appliances rented via RentMozo (repairs bundled free); contrast case for owned-appliance friction
- [x] Technician/supply-side interview — **Technician** (carpenter, 12:59) — runs a ~10-person crew, job allocation by urgency/seniority, confirms informal side-payments from his own side of the transaction

**7 of 7 recorded interviews now transcribed** (Whisper + GPT-4o role-labeling, per `scripts/transcribe/`), audio + full transcripts in `evidence/Interviews/`. Landlord/tenant-lens and a second technician-lens interview were planned but not reached — not fabricated as done.

**Real, unresolved gap**: none of these interviews has a filled consent log (age-band, city, audio/photo consent confirmed) — see `answers_draft.md` §0. Verbal consent is audible on at least the Amma and Sai Kakki recordings but was never transcribed into a tracker. This blocks using verbatim quotes with proper attribution in the final submission.

**Artifact photos captured** (in `~/Downloads/ken-case-competition/evidence/notes/` and `Workflows/`, not yet moved into this git repo's `evidence/`): a Havells RO purifier with its next service date handwritten in marker directly on the AMC sticker ("NEXT 15/M/26") plus a taped-on "Contact for Service" number card; Sarala Aunty's handwritten diary pages tracking payments/balances/phone numbers for Eluru tradespeople — both real, both corroborate what was said verbally in interview.

### Stage 2 — Synthesis
- [x] Interviews reviewed for a corroborated, non-obvious pattern (done directly against the 7 transcripts, not yet cross-tagged into `notes.md` §2's 17+1 thread table — that cross-tagging is still open)
- [x] Independent-corroboration check run: the "informal cash side-payment beyond the official/app price" pattern is corroborated **three ways** — two households (Rk Sir, 6128maggi) independently report it, and the technician interview confirms it unprompted from the supply side
- [x] Insight passes the deletion test against the drafted Q3 loop (see `answers_draft.md`)
- [x] Q2 insight drafted (58 words) — **not locked**, pending the team's own read and the consent-metadata fix before any quote is attached to it

### Stage 3 — Drafting — first real draft exists, see `answers_draft.md`
- [ ] Q1 — team & right-to-win — **team asset paragraph drafted; the 3 per-member personal-connection lines are still blank, only the team can write these**
- [x] Q2 — the one insight — drafted, 58 words, evidence-backed (see above)
- [x] Q3 — six-step agent loop — drafted, all 6 cells within the 15-word limit
- [x] Q4 — rail roles — drafted; Payments and Voice are evidence-backed, **Logistics is honestly thin** (no interview surfaced a parts-shipping delay)
- [x] Q5 — rail to innovate on — drafted, 39 words, Payments-led
- [x] Q6 — customer asset requested — drafted, 29 words, ties to the Padmaja RO-sticker photo
- [x] Q7 — the annexation — drafted, 29 words, **flagged as needing more team discussion, less evidenced than Q2-Q6**
- [ ] Q8 — which opening you'd never automate — **deliberately not drafted**, this is a personal values call for one team member to write
- [x] Q9 — which Indian company should've built this — drafted, 59 words, uses the team's own RentMozo finding as a real counterfactual data point alongside Bajaj Finserv
- [x] Q10 — track — Product Strategy, already locked

### Stage 4 — Review & submit
- [ ] Full draft reviewed against judging criteria (Evidence/Creativity/Clarity/Feasibility/Thoroughness)
- [ ] Reviewed against page's own litmus tests (Q1 "any three students" test, Q2 "changed your design" test)
- [ ] Consent log filled in for all 7 interviews (age-band, city, audio/photo consent) — **hard blocker, see `answers_draft.md` §0**
- [ ] Q1's 3 personal-connection lines written by the actual team members
- [ ] Q8 written by one team member
- [ ] Word counts re-verified against the live Solution Assembly form fields (not just the public page)
- [ ] Submitted with buffer before Sep 10, 11:59 PM IST — **today; the team's own plan recommends targeting 6PM, not 11:59PM, to leave room for upload failures**

---

## Side track — `resource-scan` skill

- [x] Skill written and saved to `~/.claude/skills/resource-scan/SKILL.md`
- [x] Scoping explained to user (machine-local via Claude Code, not account-cloud-synced)
- [x] Test-driven live (manual walkthrough, since the skill wasn't yet recognized mid-session)
- [ ] Skill available via `/resource-scan` in a **fresh** Claude Code session (should work automatically next session — not yet confirmed by the user)
- [ ] Decision on copying to another machine / packaging as a plugin (not yet requested)

---

## Documentation task (original request)

- [x] `context.md` — full session transcript
- [x] `decisions.md` — decisions log, split user vs. Claude
- [x] `/files/` — all source files copied/preserved (3 pre-existing local docs + 3 fetched web pages + the skill file)
- [x] `links.md` — all URLs surfaced, grouped by source/axis
- [x] `notes.md` — all notes/facts/quotes, organized by topic
- [x] `plan.md` — forward plan
- [x] `progress.md` — this file

## Follow-up documentation requests

- [x] `r1.md` — resource-scan suggestions mapped to each Phase 1 question (Q1-Q10)
- [x] `system_map.md` — reorganized problem space / solution space / per-object workaround map, synthesizing resource-scan + both context files + the braindump
- [x] Household Service Memory Supplementary Note (PDF) read and integrated — new section added to all 8 markdown files (`context.md` Part 7, `decisions.md`, `links.md`, `notes.md` §6a, `plan.md`, `progress.md` — this section, `r1.md`, `system_map.md` §5), PDF preserved to `/files/`
- [x] Independent secondary research on task-substitution theory (compensatory consumption, bricolage, jugaad) and service-tracking mechanisms (vehicle SMS-reminder infra, AMC vendor practices, RO brand apps, physical stickers/log books) — ~14 web searches, synthesized into `system_map.md` §6, `notes.md` §6b, sources in `links.md`, 2 new interview probes added to `plan.md`

## Team reconciliation (new — see `team_reconciliation.md`)

- [x] Discovered teammate Sricharan's independent research pipeline (`research/` folder: interview guide, survey instrument, fieldwork capture templates, rail documentation, 20 reference textbooks) pushed to the shared repo
- [x] Reconciled both tracks into `team_reconciliation.md` — canonical sources designated per area, additive probes mapped to insertion points, hypothesis sets cross-checked (4 of 5 independently overlap)
- [x] Corrected `system_map.md` §1.3 based on Sricharan's audit finding (18-24/machines repetition-rate claim is not supported by any current source)
- [x] **Interview volume decided**: 3-6 interviews + survey rollout (Sricharan's S0-S30 instrument), not the 10-12+3-4 target (`team_reconciliation.md` §4)
- [ ] **Your own personal incident for Q1** — deferred by you to later ("at the end"); still needed alongside Atharv's (also still pending)
- [x] **`best_practices.md` written**: all 20 textbooks read (targeted extraction, not cover-to-cover) via 4 parallel background research threads, plus 3 years of Ken competition winner/judge research (2024 inaugural, 2025, 2026). Covers how to think like a designer/systems-thinker/UX-researcher/experiment-designer, with good/bad practices and given-a-problem frameworks for each, grounded in the actual IIITH M.Tech PDM course syllabi that assign these exact books.
- [x] **Survey audited and cleared for launch**: `best_practices.md` §6 gives the team's existing S0-S30 survey a "ship it" verdict against Cozby & Bates + King/Churchill/Tan, with 3 optional hardenings and one real outstanding item (fill in the `[team-controlled contact]` placeholder before launch)
- [x] **Problem statement narrowing — `narrowed_problem.md` written**: 4-filter narrowing algorithm, Q-by-Q breakdown of what's expected per answer, and a real recruitment plan (6 interview slots against confirmed access: My Home community — direct/family access — vs. independent households, IIITH campus, plus a bonus tier-3-city technician phone contact). Object/machine category deliberately left open, to emerge from unprimed interviews. New candidate thread #18 added to `notes.md` §2 (managed-community vs. independent-household service-network structure).
- [x] **Geography corrected and quantified**: Eluru (tier-3, AP) confirmed as a real second geography — not "Hyderabad," an earlier mishearing — with real household+technician counts driving a rebuilt recruitment table (`narrowed_problem.md` §4 Decision 3, §5). New candidate thread #19 added to `notes.md` §2 (metro vs. tier-3 market maturity), explicitly flagged as confounded with thread #18 in the current sample.
- [x] **Resource-scan findings folded into the narrowing plan**: a whitespace pre-registration table added to `narrowed_problem.md` Decision 1 (trade/repair services rank highest whitespace; AC "covered on paper," 7% actual brand-AMC; RO split by brand; vehicles as contrast case, not target) — plus 2 new interview probes across all household slots, both derived from resource-scan (vehicle/reminder comparison; formal-AMC-vs-relationship)
- [x] **`research_plan.md` written**: full stakeholder map (8 confirmed interviews — added My Home technician and standalone-Hyderabad household as new confirmed contacts this turn — plus 3 recommended snowball additions), per-stakeholder-type interview guide deltas, a survey plan with a new S7a segmentation question, and an evidence-capture matrix mapping every interview to the competition's 5 attachment types
- [ ] **Execute the research plan** — 8 confirmed interview slots + survey distribution outlined in `research_plan.md`, none conducted yet. Recommended interview target raised from 3-6 to 6-9 given confirmed access.
- [x] **Rail-build potential added as a required second lens**: `narrowed_problem.md` Decision 1b scores AC/RO/trade-services/pest-control against Voice/Payments&Authorisation/Logistics (3 rails, not 4 — terminology corrected). AC and RO score strongest all-around; trade/repair services (the highest-whitespace candidate) flagged as logistics-weak. 2 new rail-completeness probes added to the technician guides; `research_plan.md` §6a makes scoring this a required synthesis step, not optional.
- [x] **Compliance re-verified a second time, gap found and fixed**: full-page re-grep confirmed everything else already covered; the workaround-artifact probe was too narrow (stickers/log books only vs. the page's actual "whiteboard/notebook/folder/WhatsApp-chat-with-self" examples) — broadened in `research_plan.md` §3, and a missing survey question for this exact evidence type added (S20a, §4). Open WhatsApp distribution reality addressed: channel tagging gets a 5th "Other/forwarded/unknown" value, S7a + demographics become the real post-hoc classification mechanism.
- [x] **Secondary research beyond interviews+survey, plus a Mom Test audit**: found real, usable National Consumer Helpline government data (top-5 national complaint category, 6 buckets, new thread #20) and Urban Company review-mining sources (`system_map.md` §7, `links.md`). Audited the interview guide against the Mom Test directly — base guide passes, 2 hypothetical-future-question risks found and hardened. Consolidated every trap across the project into one table (`research_plan.md` §10) and a prioritized 24-hour action list (§11).
- [x] **Evidence archive built**: `evidence/secondary_research/` — 16 real verbatim review quotes (Urban Company, PissedConsumer/Trustpilot, including one Hyderabad-specific and one Telangana-regional) and one genuine primary government document (PIB, Oct 2025). One earlier claim (`system_map.md` §7.1's specific top-5-category figure) downgraded in confidence after the primary source didn't independently verify it — corrected transparently, not left overstated. Two forked agents failed on an account-wide rate limit; work continued directly rather than relaunching forks.
- [x] **`interview_guide.md` and `survey_guide.md` written**: fully merged, per-stakeholder interview question sequences (base + every additive probe, in the actual order to ask them) and a Google-Forms-ready survey script (exact question types, section breaks, branching) — no tool exists here to literally deploy the form, so this is copy-paste-ready instead.
- [ ] Confirm with Sricharan the exact meaning of "duplicate" RAM in his incident before it's used in any answer draft

## Known open risk (updated 2026-09-10, second pass)

Fieldwork is done (7 interviews). `answers_draft.md` was **rewritten** on 2026-09-10 after a full re-read of every transcript, the raw Whisper JSON (for exact timestamps), all 16 evidence photographs, The Ken's founding column, and `research/report-source.md` p.16's rail documentation. Four answers changed materially — see that file's header for what changed and why. **Today's real risks, in priority order:**

1. **Consent is the hard gate, and it is worse than the first pass recorded.** Recording consent is audible in 6 of 7 calls, and 3 respondents explicitly reconfirmed anonymised use at the close — better than previously logged. But: (a) **the Technician recording has no consent capture at all** — verified against the raw segments, it opens cold at "Hello, Uncle" — and he is the respondent Q1's team statement is built on; (b) **nobody was told their words may be published by The Ken**, which is what the ground rule actually requires; (c) no age band or city for any of the 7. Full status table, the exact message to send, and artefact-redaction instructions: **`evidence/consent/CONSENT_LOG.md`**.
2. **Q1's three personal-connection lines and Q8 are not written** — personal/values answers only Sricharan, Prathyusha and Atharv can write.
3. **Opening-number error, submission-breaking if copied.** The `~/Downloads/ken-case-competition/` kit calls this "Opening 01" and misnumbers every other opening it cites. It is **#02 by title**; `report-source.md` p.2 explains the picker lists it second while its image asset still carries number 11. **Select by title, never position.** Q8 names an opening — use the live-page numbering listed in `answers_draft.md` §Q8. Also verify in the live form that the registered opening is actually #02 before touching anything else; switching resets evidence.
4. **The deadline is today, 11:59 PM IST.** `00-PLAN.md` says target 6 PM, `report-source.md` says 8 PM — take 6 PM.
5. ~~No survey was ever fielded~~ — **resolved 2026-09-10. A survey WAS fielded: 19 responses (12 qualified, 7 screened out), 8–10 Sep, anonymous, age band + city captured for all.** Raw CSV/XLSX, full per-respondent table, and analysis now in **`evidence/survey/`**. Two findings changed answers: **7 of 12 incidents had decide/approve-cost/pay/give-access split across more than one person** (the strongest number the team has — it makes the Payments rail load-bearing), and **0 of 12 involved a part or appliance moving**, which disconfirms the Logistics rail from the demand side. `answers_draft.md` §Q4 was rewritten against both. Note the sample has **no Eluru respondents** despite `narrowed_problem.md` planning for Hyderabad + Eluru — the real spread is Hyderabad 9, Vizag 6, Bengaluru 2, plus one Munich response to exclude from any India claim.
6. **Evidence-pack size.** ~133 MB of audio is too large to attach. Cut 60–90 second clips around the timestamps tabulated in `answers_draft.md` §Q2.
7. ~~Logistics rail is evidence-thin~~ — **resolved, and it was a first-draft error.** The parts evidence was in the transcripts and in the team's own Miro technician journey map all along. See `answers_draft.md` §Q4.

## Correction to log against this project's own evidence discipline

`best_practices.md` §1.2–§1.3 attributes several judge quotes and team examples (Deepak Shenoy's "adjusted/ebitda" line, the "we will leverage AI/ML" commentary, Metamorphosis, Illuminaire, Ken-spiracy Theorists, Kenith, ArogyaGhar.ai, ROI Rangers, and Tek-Ken/Voldemort as 2024 quick-commerce finalists) to `files/ken_case_competition_2025_winning_submissions.txt`. **None of them appear in that file** — a direct grep returns zero hits for every one, and Tek-Ken and Voldemort are 2025 teams in it, not 2024 ones. That material may have come from other web sources during the session that were never captured to `files/`, but it cannot be verified against the source it cites. It is internal strategy guidance, not a submitted claim, so it breaks nothing — but per this project's own standing rule, it is recorded here rather than left silently overstated.
