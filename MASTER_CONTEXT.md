# MASTER CONTEXT — The Ken Case Competition 2026 ("Keeping the Machines Running") — Team Invictus

**This file was generated on 2026-09-10 by reading every file in this repository plus its full git history.** It does not replace `context.md`, `decisions.md`, `notes.md`, `plan.md`, `progress.md`, `r1.md`, `system_map.md`, `team_reconciliation.md`, `best_practices.md`, `narrowed_problem.md`, `research_plan.md`, `interview_guide.md`, `survey_guide.md`, or anything in `research/` or `evidence/` — those remain the git-tracked originals and the record of who actually decided what. This is a synthesized index/superset built so that a brand-new agent or a new terminal, with zero prior context, can read **this one file** and understand what happened, why, and what to do next, without having to open 30+ other files first. Every claim below is sourced to a specific file or git commit hash so it can be verified rather than taken on faith — nothing here is invented; where something is genuinely unknown, it says so.

**⚠️ URGENT, read this first**: The competition's Phase 1 ("Solution Assembly") deadline is **10 September 2026, 11:59 PM IST** — that is **today**. **This file was originally written on 2026-09-10 when the repo was still at commit `358c8b4` (2026-09-08) with zero interviews done; it has since been updated the same day after pulling 2 new commits (`300159a`, `57156c0`) that added 7 real, transcribed interviews. See §16 (appended, bottom of file) for the current, accurate state — treat §14 below it as historical/superseded where the two disagree.** **A third update, §17, was appended later the same day: a survey WAS fielded (19 responses) — §16.1's claim that no survey data exists is now wrong, and §17 supersedes it. `answers_draft.md` was also rewritten in that pass, changing four answers.** As of §17: 7 interviews plus a 19-response survey are done and a second, evidence-tight draft of all 10 answers exists, but a real compliance gap (no consent/age-band/city metadata for the interviews; one recording with no consent at all) and 2 personal/values answers (parts of Q1, all of Q8) are still open. Run `git log -1` and `git status` before acting on anything here — check for changes since 2026-09-10 too.

---

## 1. Purpose of this file

A new agent or a new terminal session, dropped into this repository with no memory of any prior conversation, should be able to read this single file and come away knowing: what the competition actually requires, what problem the team chose and why, what research has (and hasn't) been done, what mistakes were made and corrected along the way, what the current best-guess strategy is, and exactly which files are canonical for which purpose. Everything else in the repo is either a primary source (read it for full detail/exact wording) or now superseded (kept for history, not to be treated as current).

---

## 2. The competition, exactly as it exists

**Source: `files/ken_case_competition_2026_page.txt`** (806 lines, fetched directly from `https://the-ken.com/case-competition-2026/` via `curl` with a browser user-agent, since the WebFetch tool gets HTTP 403 from this site — recorded as decision #10 in `decisions.md`), cross-checked against `context.md` Part 1.3.

The Ken's Case Competition 2026 runs in three stages: **Choose** (pick 1 of 16 "openings" — done, the team picked **#02, "Keeping the machines running"**) → **Assembly** (= Phase 1, the actual deliverable right now — a 10-question form, not a deck or report) → **Build** (post-shortlist, from 15 Sep, with real rail-partner sandboxes).

**The 10 Phase 1 questions, exact requirements** (full verbatim text: `context.md` Part 1.3):
- **Q1 (Team)** — one line per member (name + closest personal connection to the pain) + a 50-word team statement of unfair advantage. Litmus test on the page itself: *"If any three students at your college could submit your answer, rewrite it."*
- **Q2 (Evidence)** — 60 words, one non-obvious customer insight from a real conversation, proof optional but scored. **Judges read this one first.**
- **Q3 (Agent loop)** — six steps, ≤15 words each: trigger, what it knows, what it does, who it deals with, what/when it asks its human, how it knows it's done.
- **Q4 (Rail roles)** — one sentence per rail (voice / payments & authorisation / logistics — **3 rails, not 4**; a rail may have no role if you say why).
- **Q5 (Rail to innovate on)** — pick one rail, 40 words, name a capability that doesn't exist today.
- **Q6 (Customer asset)** — 30 words: the one thing you need the customer to hand over, and why they'll agree.
- **Q7 (Annexation)** — 30 words: which adjacent use-case you take over next, and why it falls to you.
- **Q8 (Never-automate)** — one opening (of the 16) you'd never hand to an assistant, one sentence, no right answer.
- **Q9 (Incumbent counterfactual)** — one Indian company that should have built this already, 60 words, your best guess why they haven't.
- **Q10 (Track)** — Product Strategy or Product Build; **locks at submission.**

**Ground rules**: one opening per team, switchable up to 3× before submitting (evidence restarts each switch); every member same institution; informed consent required from everyone interviewed; quotes published as age-band + city, **never a name**; The Ken may validate/disqualify at its sole discretion; fabricated evidence is explicitly disqualifying (`research/report-source.md` Page 6, citing the competition's own terms).

**Judging criteria** (same 5, all 3 years, wording evolved — see §5 below): Evidence, Creativity, Clarity, Feasibility, Thoroughness. The 2026 page explicitly warns: *"This is usually where AI-generated solutions fail"* (on Creativity).

**Rails/partners**: Zerodha (title partner, no rail role stated), **Delhivery** (logistics — Maps/MCP), **Pine Labs** (payments **and** authorisation, one combined rail — P3P protocol + Grantex for identity/spend-limits/audit-trail), **Gnani** (voice — Inya VoiceOS, 30M+ daily interactions, 12+ languages). Prize pool: ₹20 lakh total, plus per-rail innovation prizes.

**Timeline**: 06 Aug openings survey live → 15 Aug registration open → 31 Aug openings live → 05 Sep Assembly open → 08 Sep registration closes → **10 Sep 11:59 PM IST Assembly closes** → 15 Sep shortlist + rails round → 10 Oct finale → late Oct results published.

**The chosen opening, "Keeping the machines running," as described in the case material** (source: `Keeping_Machines_Running_Context.md`, `keeping_the_machines_running_context.md`, `system_map.md` §1.5 — these are `[CASE]`-tagged, i.e. real but secondary evidence, not the team's own findings): households describe themselves as **"dispatch desks"** for their own appliances. Six named example workflows in the case material: a water-purifier install with chatbot→service-centre→agent→OTP handoffs; an AC repair that became a multi-day tenant/landlord dispute; a carpenter job dominated by waiting, not work; a plumber who says "coming" with no enforcement mechanism; a lift AMC that only happens if residents chase it; a pest-control vendor calling to sell a renewal. A respondent explicitly generalized past appliances to "appliance service, car service, and Amazon errands" as "many similar stuff," and described the whole experience as **"solving the chase problem with hope."**

---

## 3. Team & workspace

**Team name: Invictus.** Institution: **IIIT Hyderabad (IIITH), M.Tech Product Design and Management (PDM).** Members: **Atharv** (1st year), **Sricharan** (2nd year), **Prathyusha** (2nd year). (Source: `research/Invictus_Team_and_Research_Brief.md`, `team_reconciliation.md` §1 — this resolved a gap the earlier session had flagged twice, `decisions.md` #21.) Track: **Product Strategy**, confirmed independently by two separate research tracks with no conflict (`decisions.md` #3, `team_reconciliation.md` §1).

**Repository**: `github.com/PrathyushaKalluri/ken-case-competition-2026`, cloned locally at `/Users/Shared/Files From e.localized/Ken case comp/ken-case-competition-2026`. Set up as a shared git workspace specifically so the team's documentation/strategy/research persists across separate Claude Code sessions run by different teammates on different machines — which is exactly what happened (see §4 and §9).

**A real oddity in the git history, worth knowing about**: several commits show author **name** "Prathyusha Kalluri" but author **email** `sricharanperi27@gmail.com` (visible via `git log --format='%h|%an|%ae|%s'`) — i.e., a local git config on one machine had the wrong `user.name` set relative to the account's email. This doesn't change authorship in practice (the two research "tracks" are clearly distinguishable by content and are both described accurately in §4 and §9 below), but don't take the `author` field at face value if you need to know who physically typed a commit — check the content and the `Claude-Session:` trailer in the commit body instead.

---

## 4. Full commit-by-commit timeline (what was done, in order, and why)

Source: `git log`, `git log --stat`, and each commit's own message, cross-checked against `progress.md`/`decisions.md`'s own narration of the same events.

1. **`0e3b319`** — *Initial commit: The Ken Case Competition 2026 - Keeping the machines running.* Added the three pre-existing local files the team had before any AI session touched the repo: `01_group_braindump.md` (raw team brainstorm — stakeholders, a 30-item machine/errand list, personas, workflow notes), `Keeping_Machines_Running_Context.md` (a 30-section "master context" — thesis, competition strategy, a full Observe→Decide→Act→Verify→Recover agent state machine, 35-50-interview research targets, a "Coordination Tax" metric concept, ICP candidates A-E, business-model hypotheses, a full demo storyline), and `keeping_the_machines_running_context.md` (a second, independently-structured context file — a "decode the case" walkthrough of all 6 case examples, a 6-axis divergence framework: object/job/failure/actor, a 30-item interview guide, hypotheses H1-H10). **Both context files explicitly instruct any future reader: "do not treat the current thesis as truth," "do not invent statistics," "separate facts/findings/hypotheses," "prefer observed behaviour over stated preference."**

2. **`3df33c1`** — *Add reference PDFs, research folder, output, and case playbook* (authored by Peri Sri Charan, from a **different machine and a different Claude Code session** than the one that produced most of this repo's files — session ID `session_01LYHzkE42Pd4RXp98AtGSga`, discovered via `git log`/`git reflog` mid-project, see §9). Added the 20 reference textbook PDFs, `research/` (Sricharan's own interview guide, survey, fieldwork templates — see §9), `output/`, and `The_Ken_2026_Case_Selection_Playbook.html` (the original case-selection deck used before the opening was picked).

3. **`7e6b0ac`** — *Reconcile with Sricharan's independent research pipeline.* Wrote `team_reconciliation.md` after discovering commit 2's contents mid-session — see §9 for the full reconciliation.

4. **`70a1186`** — *Add best_practices.md: textbook synthesis + 3 years of Ken competition patterns.* See §5.

5. **`940083d`** — *Narrow the problem statement for Round 1: narrowed_problem.md.* See §6.

6. **`74c69f7`** — *Correct geography: Eluru (tier-3), not "Hyderabad" - real second geography.* A real correction — see §11 (the "corrections and mishearings" section) for the full story.

7. **`1a4dc65`** — *Fold resource-scan findings into the narrowing plan as a whitespace prior.* Re-applied the earlier resource-scan run (§9.5 below) into `narrowed_problem.md`'s object-selection reasoning — no new research, a re-application of existing findings.

8. **`5317873`** — *Add research_plan.md: full stakeholder interview + survey + evidence plan.* See §7.

9. **`7d8987b`** — *Elevate rail-build potential to a required filter alongside the insight.* Added Decision 1b to `narrowed_problem.md` — scoring candidate objects against actual rail-build potential (voice/payments&authorisation/logistics), not just whitespace. Also corrected a real terminology error: the user's phrasing implied 4 rails; the competition has **3** (payments and authorisation are one combined rail, matching one partner, Pine Labs).

10. **`05a736d`** — *Fix workaround-artifact gap; handle open WhatsApp survey distribution.* A real gap the user caught by re-reading the competition page — see §11.

11. **`8c42a08`** — *Add secondary research options and a Mom Test audit of the interview guide.* See §8 and §11.

12. **`7140f26`** — *Add evidence archive, interview_guide.md, survey_guide.md.* See §7 and §8.

13. **`a349a76`** — *Add tested plain-language household interview guide (Word doc + evidence)* (authored by Peri Sri Charan). This is the `research/interview_guide_qa/` QA pass — see §10.

14. **`98ad30a`** — *Add tested Google Form survey guide for Hyderabad/Vizag WhatsApp distribution* (authored by Peri Sri Charan). The `research/survey_guide_qa/` QA pass, v2 (33 questions) — see §10.

15. **`358c8b4`** — *Redesign survey to 17 questions after field feedback (was 33)* (authored by Peri Sri Charan). **The most recent commit in the repo.** See §10 for what changed and why.

Untracked: `output/.DS_Store` (a macOS artifact, not project content — safe to ignore or gitignore, not evidence of missing work).

---

## 5. Research methodology — how the team's approach was designed, and where it came from

**Primary source: `best_practices.md`** (written after commit 7e6b0ac's reconciliation, per the user's own sequencing instruction "reconcile first, then textbooks" — `decisions.md` #29). This file has two halves.

### 5.1 What actually wins the competition (3 years of evidence)

Judging criteria evolved: 2024 used Innovation/Clarity/Feasibility/Thoroughness/**Context**; 2025 swapped **Context → Evidence** (the single biggest formal shift — proof a real person told you something, not just sharp company analysis); 2026 kept the same 5 as 2025 with an explicit warning that AI-generated solutions "usually fail" on Creativity. Direct judge quotes found and used: **Deepak Shenoy** (2024 judge, Capitalmind CEO) on financial hand-waving — *"I'll ask about where's the money... will we get that without using the words 'adjusted' and 'ebitda'"*; The Ken's own 2025 commentary flagging *"we will leverage AI/ML"* as a liberally-overused, superficial phrase across most submissions. Seven named winning patterns across 30+ reviewed teams (2024-2025), the most load-bearing being: **bold claims always paired with rigor, never alone** (Metamorphosis, the 2024 winner, literally wrote "don't mistake bold with reckless"); **first-principles reframing beats more features** (Illuminaire's "rent out the infrastructure" inversion); **specificity beats scale** (winning pitches always attach real numbers, never bare adjectives). A demo-structure template worth copying, extracted from the 2025 ArogyaGhar.ai prototype: problem in plain language → the insight as one line → hard evidence *before* the product is shown → concrete before/after numbers → role-specific validation.

### 5.2 The course grounding

The 20 reference textbook PDFs in this repo's root are not a random reading list — `Courses-Syllabus_M26-V1.pdf` (IIITH's own 288-page M.Tech PDM syllabus, read directly, keyword-searched not skimmed) confirms they are the actual assigned texts for three real courses: "Behavioral Research & Experimental Design" (Cozby & Bates), "Systems Thinking" (Meadows, Senge — whose own course example is the UPI ecosystem, structurally identical to this competition's 3-rail setup), and a Design Thinking/User Research course. `best_practices.md` treats this as applied coursework, not supplementary reading.

### 5.3 The four thinking-lens syntheses (this is "the information gathered from reading the books")

Produced by 4 parallel forked research agents, each reading a cluster of the textbooks directly via a local `pypdf` extraction tool (see §11 for why this was needed), each citing which book/chapter grounds which claim:

- **Systems thinker** (Sterman's *Business Dynamics*, Senge's *The Fifth Discipline* + *Fieldbook*, Meadows' *Thinking in Systems*): core tools — event vs. feedback view, reinforcing vs. balancing loops, stocks/flows, Meadows' 12 leverage points (weakest #12 "tweak a number" → strongest #1 "transcend the paradigm," with the counterintuitive lesson that most people default to the weakest one), Meadows' 8 system traps with named "ways out." **Applied to this project directly**: named a candidate reinforcing loop, "the self-fulfilling distrust loop" (less reliable follow-through → more personal verification → less delegation → less context reaches the technician → less reliable follow-through); flagged several of the 17 pain-threads (below) as textbook Shifting-the-Burden patterns; explicitly cited Sricharan's own `report-source.md` line *"do not count reminders sent or calls placed as customer value"* as an independent, correct instance of guarding against Meadows' "seeking the wrong goal" trap.
- **Designer** (Buxton, Desmet & Hekkert, Tidwell, Hassenzahl): core idea — problem-setting is a distinct, often-skipped job from problem-solving (Buxton citing Schön, and Tidwell independently converging on the identical principle); usability is instrumental to a "do-goal," never terminal on its own; experience composition changes over time (week-1 usability-and-stimulation vs. week-4 identity-and-classiness) — meaning a concept that wows in a first demo and one that holds up after a month need different design decisions.
- **UX/user researcher** (Kuniavsky, Erika Hall, Constantine, Sharp/Preece/Rogers, Boellstorff, Dumas & Loring, Lew & Schumacher): core distinction — **say vs. do** (what people report is systematically unreliable; the one real past incident is the signal); "right-sized" research (a 3-6 interview sprint isn't a compromised version of real research, it's correctly-sized for a 2-day decision window, as long as its limits are disclosed); personas/segments are compressed hypotheses to organize recruitment, never facts a single interview can "confirm."
- **Experiment/survey designer** (Cozby & Bates, King/Churchill/Tan): core distinction — construct validity vs. reliability; convenience samples license *mechanism* claims, never *population-prevalence* claims. **This lens also performed a real line-by-line audit of the team's own survey instrument and gave it a "ship it" verdict** — see §8.

### 5.4 Cross-cutting guardrails (stated explicitly in `best_practices.md` §7, apply to every answer drafted)

Never fabricate evidence (the competition's own terms make this disqualifying). Label every claim by evidence tier (`[CASE]`/`[LAW]`/`[TEAM]`/`[HYPOTHESIS]`/`[NEEDS INTERVIEW]`, the convention used throughout `system_map.md`). A technology name is never a mechanism — say the specific thing it does. A financial claim needs a real number or an explicit "unknown."

---

## 6. Narrowing the problem statement — the 4-filter algorithm and where it landed

**Primary source: `narrowed_problem.md`.** The core argument (§1 of that file): narrowing isn't a stylistic choice — every object/segment/geography choice simultaneously changes (a) what already exists competitively, (b) what evidence claims are honestly licensed, and (c) which rail is genuinely load-bearing vs. decorative.

**The 4-filter algorithm**: Object/domain → Segment/persona → Geography/cultural context → Mechanism/insight-thread, each filter's output feeding the next, each scored against the actual judging criteria plus a leverage-point test.

**Decision 1 (Object)**: deliberately **left unpicked**. The user correctly refused to choose an object blind — nobody has evidence yet for which machine/service category is strongest. Interviews stay unprimed ("tell me about the last time this happened," never "tell me about your AC"); the object is meant to surface from what respondents actually bring up. A **whitespace pre-registration table** was built anyway, from the earlier resource-scan run (§9.5), specifically so evidence can be checked against a pre-committed prior once it arrives (avoiding motivated reasoning): trade/repair services (plumbing, carpentry, electrician) score **highest whitespace** — no FSM-equivalent exists for households sourcing these directly; AC is "covered on paper" (Urban Company, brand apps) but a LocalCircles survey found only **7%** of AC owners are actually on a brand maintenance contract, and it's the one object with **documented legal ambiguity** (Indian rent law leaves AC servicing an undefined tenant/landlord grey zone — `system_map.md` §1.5, §4); RO/water purifier is split (Kent's premium "SUPREME" IoT line already auto-detects faults, but only for that one brand); a vehicle-adjacent incident is a strong **contrast case**, not a target (India has already fully solved this exact reminder-infrastructure problem for vehicles).

**Decision 1b (rail-build potential — added later, per commit `7d8987b`, once the user said this mattered more than whitespace alone for what carries into Round 2)**: scored the same candidates against Voice/Payments&Authorisation/Logistics. AC and RO score strongest across all three rails; trade/repair services — the highest-*whitespace* candidate — is honestly flagged as **weakest on logistics** (many jobs are labor-only, no real part-shipping need). This tension was not resolved by picking one — both lenses are meant to be checked once real interview data names the actual object.

**Decision 2 (Segment)**: the real axis, after a correction (see §11), is **service-network structure** — whether a household's repairs route through a managed community's own vendor system (e.g. **My Home**, a Hyderabad gated-community builder group the user has direct/family access to) versus self-sourcing every time — not renter/owner, not age. This gives the team a real, already-available "smooth case vs. painful case" contrast, which `best_practices.md` §5 explicitly names as one of the hardest things to arrange in a 2-day sprint.

**Decision 3 (Geography)**: after a second correction (see §11), the confirmed real access is **Hyderabad (My Home, metro/managed) + Eluru, Andhra Pradesh (tier-3, presumably-independent, to be confirmed not assumed) + IIITH campus (metro/institutionally-managed, via Sricharan)**. This is an honest, explicitly-flagged **confound**: Hyderabad access = metro+managed, Eluru access = tier-3+independent — two variables changing at once. The IIITH campus interview is the one data point that can help triangulate which variable (market maturity vs. management structure) is actually driving any observed difference.

**Decision 4 (Mechanism)**: not yet made — explicitly blocked on real interview evidence (`narrowed_problem.md` §6: *"Pending real interview evidence — not filled in yet"*). See §14 (Open questions).

---

## 7. Research instruments actually built

**The canonical, ready-to-use interview guide**: `interview_guide.md` — a merged, per-stakeholder, ordered question sequence (base questions from Sricharan's `research/report-source.md` Pages 7-8, plus every additive probe this project's second track built), covering: household interviews (5 segment variants: Eluru ×2, My Home, standalone Hyderabad, IIITH campus) and technician/service-centre interviews (3 variants), plus a landlord addendum. Two questions are explicitly marked **[HARDENED]** after a direct Mom Test audit found them to be hypothetical-future questions — see §8.

**The canonical, ready-to-launch survey**: `survey_guide.md` — a full Google-Forms-ready adaptation of Sricharan's S0-S30 instrument (question type, branching logic, section breaks spelled out so building the form is copy-paste, not redesign), with two project-added questions inserted at their exact points: **S7a** (self-report managed-vs-independent screening) and **S20a** (a workaround-artifact capture question the original instrument was missing entirely — see §11).

**A second, complementary, city-agnostic survey exists**: `research/survey_guide_qa/Survey_Plain_Language_v2.md` — this is the **actually field-tested, redesigned** version (see §10), cut from 33 to **17 questions** after real field feedback that the original was too long and too narrowly scoped to two named cities. It is generic to any Indian household and maps every remaining question explicitly to a rail or one of the 10 competition answers. **Both survey documents draw on the same underlying design and don't contradict each other** — `survey_guide.md`'s 30-item version was built for the original four named channels; the 17-question version is built for open WhatsApp forwarding to any city. Use whichever fits the actual distribution channel.

**The full stakeholder map**: `research_plan.md` §1 — 8 confirmed interview slots (Eluru households ×1-2, Eluru electrician, an uncertain tier-3 institutional technician, My Home household, My Home technician, a standalone Hyderabad household, IIITH campus staff via Sricharan) plus 3 recommended snowball-referral additions (a standalone-Hyderabad technician, a campus facilities technician, a landlord). Interview-volume target was revised upward once real access was confirmed: from 3-6 (`team_reconciliation.md` §4, the original realistic-capacity decision) to **6-9** (`research_plan.md` §2, once 8 stakeholders were confirmed at no new recruitment cost). Sricharan's own, separately-authored playbook (`research/report-source.md` §5) targets a larger **10-12 customer + 3-4 counterparty** interview volume plus a 30-50-response survey — this is a real, still-only-partially-resolved tension; the operating decision as of the last commit is 6-9 interviews + survey, not his larger target (§9.4 below has the full reconciliation history).

**Evidence-capture discipline**: `research/Fieldwork_Templates.md` is the operational blank-forms workbook — team inventory, per-session research log, consent record, participant/incident record, incident timeline, evidence index, hypothesis/contradiction log, insight→product trace, survey administration log, and the exact Q1-Q10 word-limited answer sheet. **This is the canonical evidence-of-record template — use it starting with the very first real interview, not a summary written after the fact.**

---

## 8. The Mom Test audit and the survey "ship it" verdict — direct answers to "are we doing this right"

Two separate, explicit quality audits were run because the user asked point-blank whether the process avoids leading questions and whether the survey is methodologically sound.

**Survey audit (`best_practices.md` §6, run by the experiment/survey-design research lens against Cozby & Bates + King/Churchill/Tan)**: verdict **"SHIP IT."** The original S0-S30 instrument independently reproduces textbook-correct practice without having been built from these specific books — age/city correctly placed last, open text placed before structured follow-ups (anti-priming), "cannot recall/NA" offered throughout, zero double-barreled or leading questions found across a full read, the convenience-sampling limitation explicitly and correctly disclosed. Three **optional** hardenings suggested (duplicate-response flagging, completion-time capture, a note that the uneven answer bins in one question are correct, not a bug — don't "fix" them later). One **real** outstanding item: a `[team-controlled contact]` placeholder needs a real contact before launch.

**Mom Test audit (`research_plan.md` §9, run directly against Sricharan's 14-question base guide + every additive probe)**: the base guide **passes cleanly** — every core question is already a past-specific reconstruction, not an opinion/hypothetical question. **Two real risks were found, not zero**: (1) Sricharan's own Q15 ("if a trusted person handled this, which actions could they take without checking with you") is a hypothetical-future question — fixed by always following it with a grounding question asking for a real past precedent; (2) this project's own standalone-household delta ("what would you want a building management service to do") was replaced entirely with a past-behavior question ("tell me about a time you tried to solve this some other way"). Both fixes are already incorporated into `interview_guide.md`.

---

## 9. Team reconciliation — two independent research pipelines, discovered and merged

This is the most important "what went wrong and how it was corrected" event in the whole project, and it happened because **two teammates ran independent Claude Code sessions on the exact same repository without initially coordinating.**

### 9.1 What happened

Mid-session, a `find`/`ls` on the project directory revealed ~20 new textbook PDFs, a `research/` folder, an `output/` folder, and a `tmp/` folder that hadn't existed a few turns earlier in the same conversation. `git log`/`git reflog` traced this to commit `3df33c1`, authored by **Peri Sri Charan (Sricharan)** from a different machine and a **different Claude Code session** (`Claude-Session: session_01LYHzkE42Pd4RXp98AtGSga`), pushed shortly after Sricharan accepted a GitHub collaborator invite — the current session then discovered a `git pull` (visible in reflog as "Fast-forward") had silently brought this in.

### 9.2 What Sricharan's independent pipeline contained

`research/report-source.md` (584 lines, rendered to `output/pdf/Ken_2026_Research_and_Submission_Playbook.pdf` via `research/build_report.py`) — an extremely thorough, independently-produced research-and-submission playbook: a full three-day hour-by-hour operating schedule (Day 1 Evidence, Day 2 Design, Day 3 Submission), a complete interview guide (customer + technician/service-centre + landlord/PG-manager variants, with a stated "purpose" per question), a full branching S0-S30 survey instrument with skip logic and analysis rules decided in advance, verified rail documentation for Gnani/Pine Labs/Delhivery distinguishing "documented capability" from "verified working integration," and operational fieldwork-capture forms. Also `research/Invictus_Team_and_Research_Brief.md` (Sricharan's own confirmed team facts, his personal Q1 incident — a laptop RAM repair, deliberately left with an unresolved detail: whether the RAM was described as "duplicate," "counterfeit," "compatible," "refurbished" or "unbranded" is explicitly flagged as **unconfirmed, do not guess**), and `research/research-plan.md` (an internal gap ledger from that same pipeline, notably self-disciplined: *"No customer discovery claimed... remaining unknowns require actual interviews, team facts or authenticated access. No customer discovery claimed."*).

**Note on tone**: Sricharan's pipeline's own writing style is markedly more hedged/conservative than the rest of this repo (e.g. `research/report-source.md` explicitly states *"This is a research and execution plan, not a completed customer study or final competition entry"* on its first page, and flags its own supplied case-selection HTML's demographic scores as **unverifiable** — see §11). Treat this as a genuinely independent, differently-calibrated second opinion, not noise.

### 9.3 A real factual correction this pipeline surfaced

Sricharan's own audit of `The_Ken_2026_Case_Selection_Playbook.html` (`research/report-source.md`, page 2) found its stored demographic scores for "machines" among 18-24-year-olds (F=4, R=3, P=1) **do not match the live competition chart**, and the file's own two underlying source files (`Case studies.docx`, `Pasted markdown(1).md`) were never present in the workspace to verify the extraction. **Do not claim "machines has the highest repetition rate among 18-24-year-olds" — no current source in this repo supports it.** (`system_map.md` §1.3, `team_reconciliation.md` §6.)

### 9.4 The reconciliation itself

Written to `team_reconciliation.md` (a **new** file, deliberately not editing Sricharan's `research/` files directly, to preserve his authored work intact). Canonical-source designation: Sricharan's interview guide/survey/fieldwork-capture/operating-schedule are canonical; this project's own resource-scan findings, Household Service Memory PDF synthesis, and task-substitution/service-tracking secondary research are **kept as fully additive**, since his pipeline doesn't cover any of that. The **interview-volume conflict** (his 10-12+3-4 vs. this session's 3-6) was surfaced explicitly as an open team decision, not silently resolved — **resolved 2026-09-08 by the user directly: go with the realistic 3-6 target, plus roll out the survey as well** (later revised up to 6-9 once more real access was confirmed, per §7). A **hypothesis cross-check** found 4 of Sricharan's 5 independent hypotheses map onto 4 of this project's 17 candidate pain-threads — independent convergence from two people who hadn't seen each other's work, a reasonable signal the divergence work wasn't off track.

### 9.5 The resource-scan skill and its test-drive (a separate, tooling side-track, also part of this history)

Per a direct user request ("save it so I can use it with any Claude account"), a reusable Claude Code skill (`~/.claude/skills/resource-scan/SKILL.md`, also preserved in `files/resource-scan_SKILL.md`) was written: given a topic, diverge into a system map (adjacent domains, upstream/downstream, stakeholders, alternate framings) *before* searching, then pull repos/blogs/news/books/other across every axis, never fabricating a URL. It was test-driven live on this exact case (`context.md` Part 5) and surfaced several genuinely load-bearing findings folded throughout this repo: India's home-services market (₹5.1 lakh crore FY25, only 10-15% digitised), the Field-Service-Management industry as the enterprise "mirror" of this same problem (nobody has built the household-side version), Pine Labs P3P+Grantex already being close to production-ready for delegated spend limits, Gnani's voice infra already production-grade (the real gap is *outbound, on-behalf-of-consumer* IVR navigation — the leading Q5 candidate, see `r1.md`), and — flagged as the single most load-bearing find — **the competition's own founding thesis column** ("The Great Rewiring," `files/ken_the_great_rewiring_column.txt`), which argues India may be first to consumer AI agents because it already has a cultural precedent of delegating physical-world tasks to human intermediaries — reframing the interview question from "coordination is annoying" to "who does this household already informally trust with this job, and what would it take to trust software instead."

---

## 10. Iteration and QA on the instruments — what was tested, what broke, what changed

This section directly answers "what methodology worked and what didn't," using only what's actually documented.

**Interview guide QA** (`research/interview_guide_qa/`): a separate, plain-language, word-for-word 40-minute household script was built and pressure-tested against **3 simulated personas** (`Test_Personas.md` — "The 3%" a busy managed-community household with a real private tracking system, "The 1%" a household where the nominal owner knows almost nothing and the real coordinator is household staff — a deliberate trap for an interviewer who doesn't ask "who actually handles this," and a renter needing landlord approval with a real landlord-WhatsApp evidence trail). The resulting v2 script's own changelog lists **10 concrete fixes made because of what the simulations revealed**, including: added a 30-second screening question up front specifically because the "1%" persona showed that skipping it produces 20 minutes of thin, useless answers from the wrong person; split one question in two because in testing the combined version let a respondent's most interesting behavior (quietly bypassing her building's official vendor list) almost go uncaught; fixed one question that had accidentally been phrased as "what usually happens" instead of "tell me about one time," which produced visibly weaker answers than every other question around it in testing; added an explicit "don't sympathize, just ask the next question" reminder at the exact point testing showed interviewers were tempted to go off-script.

**Survey QA and the 33→17 question redesign** (`research/survey_guide_qa/`): the original v2 (33 questions) was piloted with **2 simulated cognitive-pretest respondents** (`Pilot_1_Hyderabad_homemaker.md`, `Pilot_2_Vizag_homemaker.md`) and was city-specific (Hyderabad/Vizag gated communities). **Real field feedback said it was too long to realistically get completed, and too narrowly scoped.** It was redesigned down to a **generic, any-city, 17-question version** (`Survey_Plain_Language_v2.md`, commit `358c8b4`, the most recent commit in the repo) — every remaining question explicitly justified by which rail or which of the 10 competition answers it feeds; every place the original chained 3-4 related sub-questions in sequence (decision role / approval role / payer role / access role) was collapsed into a single grid question instead; age/consent merged into one checkbox instead of two separate screens; no city or community name appears anywhere in the form or its distribution message, so the same link works everywhere it's shared.

**A rate-limit failure, handled honestly rather than hidden**: two forked research agents (one for review-mining, one for government-data + social-listening + contracts) both failed against an account-wide session rate limit. One left genuinely usable partial output (16 real verbatim Urban Company review quotes) before dying; the session salvaged that output, chose **not** to relaunch forks against the same limit, and continued the highest-value remaining work directly instead (`decisions.md` #67-68, `evidence/secondary_research/_SUMMARY.md`).

**A self-caught overstatement, corrected transparently**: an earlier claim in `system_map.md` §7.1 (that household appliance servicing sits in India's National Consumer Helpline top-5 complaint categories, with 6 specific buckets) was sourced to a WebSearch AI-synthesis, not a primary document. When a real primary government press release was later fetched and text-extracted (`evidence/secondary_research/government_data/nch_pib_press_release_oct2025.txt`), it verified NCH's overall complaint-volume growth but named **e-commerce**, not appliances, as its own top category. **The confidence tag on the original claim was downgraded directly and visibly in `system_map.md` §7.1 rather than left silently overstated** — this correction is itself presented in `system_map.md` and `progress.md` as an example of the project's evidence discipline working as intended, not a failure to hide.

**Lesson worth generalizing from this section**: every instrument in this repo that reached a second version did so because of a *specific, named, testable failure* found by simulation, pilot, or field feedback — never a vague "let's improve this." That is the methodology to keep repeating; conversely, the one clear anti-pattern was relaunching a failed parallel-agent approach against a known constraint (the rate limit) instead of checking constraints before retrying — avoid that specific mistake going forward.

---

## 11. Corrections, mishearings, and misconceptions caught along the way (the "what worked / what didn't" ledger the user asked for)

Every item below is a real, named, sourced correction — not a hypothetical mistake.

- **"Home pooja" → "My Home"** (`context.md` Part 12, `decisions.md` #40-41): a first attempt at asking the user to pick an object/domain cluster blind was itself rejected by the user as the wrong question to be asking (nobody has evidence yet). In the same exchange, a mishearing of "**My Home**" (a real Hyderabad gated-community builder group) as "pooja"/"home bhooja" was corrected directly by the user rather than guessed at further.
- **"Hyderabad" as a tier-3 hometown → Eluru** (`context.md` Part 13, `decisions.md` #44-47): the user's own phrasing called their hometown "Hyderabad, a tier-3 city" — an internal contradiction (Hyderabad is a major metro) that was flagged directly rather than silently accepted, correctly guessed to be a second dictation mishearing, and resolved by asking for the plain-text name rather than guessing it. The real hometown, **Eluru, Andhra Pradesh**, was then upgraded from a "bonus data point" framing to a **full second geography**, since real numbers showed its household access matched or exceeded Hyderabad's.
- **"Voice, payments, authorization, logistics" (4 items) → 3 rails** (`decisions.md` #57): the competition has 3 rails; payments and authorisation are **one combined rail**, matching one partner (Pine Labs). Re-verified directly from `Keeping_Machines_Running_Context.md` §7 rather than assumed, and corrected in `narrowed_problem.md` before it could propagate into a wrong Q4/Q5 draft.
- **The workaround-artifact interview probe was narrower than the competition's own examples** (`decisions.md` #60, commit `05a736d`): the probe only asked about "stickers on machines" and "a paper log book," while the competition page's own verbatim examples include *"the whiteboard on the fridge, the notebook, the folder of medical reports, the WhatsApp chat someone keeps with themselves."* The user caught this by re-reading the page directly; the interview probe and the survey (which had **no equivalent question at all**) were both fixed.
- **The NCH top-5-complaint-category claim** — see §10 above (a secondary-source claim later found not fully verified against a primary document, and downgraded transparently rather than left overstated).
- **A demographic claim about "machines" and 18-24-year-olds** — see §9.3 above (found unverifiable by an independent audit; do not repeat this claim).
- **The interview-volume target changed three times, honestly, as real information changed**: 35-50 (the original, aspirational context-file target, never operative) → 3-6 (the user's own realistic-capacity answer, `decisions.md` #4) → 6-9 (once 8 real stakeholders were confirmed at no new recruitment cost, `research_plan.md` §2) — vs. Sricharan's separately-maintained, never-fully-reconciled 10-12+3-4 target. **Current operating number, as of the last commit: 6-9 interviews + a survey.** Don't collapse this history into a single "the target is X" claim without the caveat that it moved as access was clarified, not as a correction of an error.
- **A single vivid persona/incident was never treated as sufficient on its own** — the convergence protocol (`plan.md` Stage 2) explicitly requires independent corroboration across interviews before locking Q2, and the Mom Test audit exists precisely because "does this sound compliant" was checked directly rather than assumed.

---

## 12. Secondary/evidence research collected so far

**`evidence/secondary_research/_SUMMARY.md`** is the index. What's real and usable: 8 verbatim Urban Company complaint quotes from PissedConsumer (`reviews/urban_company_pissedconsumer.txt`, including one Hyderabad-specific and one Telangana-regional — the same region as Eluru) and 8 from Trustpilot (`reviews/urban_company_trustpilot.txt`, including real rupee figures — e.g. a ₹9,500 AC repair that didn't hold, and a documented case of Urban Company deducting 40% of a booking as a "cancellation" charge when the *provider*, not the customer, failed to show — a real, sourced instance of exactly the kind of payments-authorisation failure the delegated-spend-cap concept is meant to prevent). One genuine primary government document (`government_data/nch_pib_press_release_oct2025.txt`, PIB Oct 2025, fetched and text-extracted directly). **What was searched but came back thin, and is flagged rather than padded**: Reddit/social-listening for Hyderabad-specific complaint threads (returned only business listings); AMC/warranty contract text analysis (queued, never attempted — the assigned fork failed before reaching it); Kaggle dataset previews (also queued, not attempted).

**Independent secondary research on task-substitution and service-tracking mechanisms** (`system_map.md` §6, `notes.md` §6b — ~14 web searches run on direct user instruction to self-inform before interviews): grounded the team's own "jugaad" vocabulary in real academic literature (frugal-innovation research, compensatory-consumption theory, bricolage); found India's vehicle-reminder ecosystem (government-coordinated SMS alerts, the mParivahan app) to be far more mature than anything for appliances, because vehicles have a shared institutional anchor (RTO registration) that appliances lack across brands — a strong candidate reframe for **Q6** (the customer asset may be the *role* of becoming that missing shared anchor, not a data export) and **Q9**; found that Indian AMC/service vendors themselves track renewals in Excel with reminder calls "from memory," losing an estimated 20-30% of renewals to forgetting — which complicates the working assumption that the *household* is the unreliable half of the relationship, not the vendor.

**Boundary that governs all of the above, stated repeatedly throughout the repo and worth restating here**: none of this secondary research can be submitted as the Q2 insight itself — the competition explicitly requires that to come from a real conversation the team had. It exists to sharpen Q9, ground Q5/Q6, and give interviews something concrete to corroborate or contradict.

---

## 13. Deliverables produced so far

- `output/docx/Ken_2026_Household_Interview_Guide.docx` — the polished Word rendering of the tested plain-language interview script (`research/interview_guide_qa/Household_Interview_Guide_Plain_Language_v2.md`), including the decision-maker map and the three test-persona simulation summaries.
- `output/docx/Ken_2026_Household_Survey_Google_Form_Guide.docx` — the polished Word rendering of the tested plain-language survey (originally the 33-question, city-specific v2; the repo's current `Survey_Plain_Language_v2.md` markdown source has since been redesigned down to 17 questions per commit `358c8b4` — **check whether this docx has been re-rendered from the 17-question version before treating it as current**, since the docx render date (Sep 8, 17:35) may predate or postdate the final markdown edit).
- `output/pdf/Ken_2026_Research_and_Submission_Playbook.pdf` (129,117 bytes, 21 pages, verified by `tmp/pdfs/qa-report.json` — "All 21 pages visually inspected; corrected section reference on page 11; structural boundary checks passed") — Sricharan's full independent research/submission playbook, rendered from `research/report-source.md` via `research/build_report.py`. `research/claim-source-ledger.json` auto-tracks every URL this document cites alongside its surrounding claim text, for verification.
- **None of the actual 10 submission answers (Q1-Q10) have been drafted anywhere in this repository as of the last commit.** They are explicitly blocked on real interview evidence per the team's own standing instruction not to pre-narrow Q2 (`decisions.md` #6).

---

## 14. Current state and open questions (as of the last commit, 2026-09-08 — **verify this is still current, see the urgent flag at the top**)

*(Everything in §14 is historical as of 2026-09-08 and is superseded by §16 and §17 — 7 interviews and a 19-response survey have since been completed. Kept for the record of what was true then, not as current state.)*

**From `progress.md`, the authoritative live checklist**: research/planning work is extensive and complete through instrument design; **zero real interviews have been conducted**; the survey has not been launched (or may have been launched between the last session and now — not recorded here). Stage 2 (synthesis) and Stage 3 (drafting Q1-Q10) are both explicitly blocked on Stage 1 (fieldwork) actually happening.

**Concrete open items, each with a specific pending action**:
- **The user's own personal Q1 incident has never been collected** in any session captured in this repo — deferred by the user "to later, at the end" (`team_reconciliation.md` §4, `progress.md`). Atharv's personal incident is also still pending on his end.
- **Confirm the exact meaning of "duplicate" RAM** in Sricharan's own Q1 incident before it's used in any answer draft — he flagged this as unconfirmed himself (`research/Invictus_Team_and_Research_Brief.md`).
- **Whether "six hours daily for three days" (the team's stated availability) means per-person or combined** is explicitly unresolved (`research/Invictus_Team_and_Research_Brief.md` line 14, `team_reconciliation.md` §4).
- **Object/domain (Filter 1) and Mechanism/insight-thread (Filter 4) are deliberately still open** — by design, waiting on real interview data (`narrowed_problem.md` §6).
- **The "main dossier" referenced by `Household-Service-Memory-Supplementary-Note.pdf`** (its own Section 2.3 "workaround ladder," Section 3.1 "seasonal shock" trigger, Section 6 "decision framework," and a 76% AC-servicing figure) has never been shared or located in any session — most likely belongs to Atharv, per the team-identity resolution in §9, but this remains an open, unconfirmed gap (`decisions.md` #21, `system_map.md` §5.4).
- **Whether `output/docx/Ken_2026_Household_Survey_Google_Form_Guide.docx` reflects the 17-question redesign or the earlier 33-question version** — flagged in §13 above, worth checking before using it.
- **The `[team-controlled contact]` placeholder** in the survey's own intro must be filled with a real contact before any launch (`best_practices.md` §6, `survey_guide.md`'s own distribution checklist).
- **17-1 (now 20) candidate pain-threads remain unconfirmed hypotheses**, per the standing instruction not to pre-narrow — see `notes.md` §2 for the full, current list with sourcing tags.

---

## 15. How to resume — practical instructions for whoever picks this up next

1. **Run `git log -1` and `git status` first.** If there are commits after `358c8b4` (2026-09-08), or uncommitted changes, this file's "current state" section (§14) may be stale — re-read `progress.md` and `decisions.md` directly for anything newer than what's summarized here.
2. **Check the actual date against the deadline** (10 Sep 2026, 11:59 PM IST) before doing anything else — see the urgent flag at the top of this file.
3. **Canonical vs. superseded files**, so you don't act on an outdated version:
   - `plan.md` is explicitly marked superseded, three times over, by `narrowed_problem.md` then `research_plan.md` — **use `research_plan.md` as the operating document for fieldwork**, not `plan.md`.
   - `interview_guide.md` (the compact per-stakeholder reference card) and `research/interview_guide_qa/Household_Interview_Guide_Plain_Language_v2.md` (the full tested plain-language script) are **complementary, not conflicting** — same underlying questions, different formats for different moments.
   - `survey_guide.md` (30 items, 4 named channels) and `research/survey_guide_qa/Survey_Plain_Language_v2.md` (17 items, generic to any city) are likewise complementary — the 17-question version is the more recently field-corrected one and is likely the better default for open WhatsApp distribution.
   - Do not treat `research/report-source.md` (Sricharan's independently-authored playbook) as superseded by anything in the repo root — per `team_reconciliation.md`, his interview guide, survey, fieldwork templates, and operating schedule are the **canonical** sources for those specific areas; this repo root's own files (`system_map.md`, `notes.md`, `best_practices.md`, etc.) are additive research, not a replacement.
4. **If real interviews still haven't happened**: that is the single blocking item for everything downstream (Q2, and therefore Q1/Q3-Q10). Start with `research_plan.md` §11's prioritized 24-hour action list, using `interview_guide.md` in the field and `research/Fieldwork_Templates.md` to actually record what happens — a filled-in template is evidence; an empty one is not (the template file's own header says this explicitly).
5. **When synthesizing evidence**: use the convergence protocol in `plan.md` Stage 2 (independent corroboration required before locking Q2), tag every incident against the candidate threads in `notes.md` §2, and run the required rail-build-potential scoring step (`research_plan.md` §6a) before concluding any rail is absent.
6. **Before submitting**: check every answer against the trap table in `research_plan.md` §10, the litmus tests the competition page states explicitly (Q1's "any three students" test, Q2's "changed your design" test), and the exact word limits per question (`context.md` Part 1.3).
7. **This document's own limits**: it does not include the full verbatim text of the competition page, the 2025 winners list, the Great Rewiring column, the 20 textbook PDFs, the three interview-guide simulation transcripts, or the two survey pilot transcripts — those are real, substantial, and preserved verbatim in `files/`, `research/interview_guide_qa/`, and `research/survey_guide_qa/` respectively; read them directly if you need exact wording rather than the summary given here.

---

## 16. UPDATE — 2026-09-10: real interviews conducted, a first answers draft exists, current true state

**This section supersedes §14 wherever they disagree.** Everything below was pulled directly from `git log`/`git show` on the 2 new commits, the actual interview transcripts, 2 photographed evidence artifacts, and a fresh read of `progress.md` as it now stands — nothing here is inferred beyond those sources.

### 16.1 What changed since the last write of this file

Two new commits landed on `origin/main` and were pulled: `300159a` ("Add interview evidence, transcripts, and Whisper transcription pipeline") and `57156c0` ("Transcribe remaining Telugu interviews; mark unrecoverable audio explicitly"). Together they added: 7 interview audio files (`evidence/Interviews/*.m4a`), 7 human-readable transcripts (`evidence/Interviews/Transcripts/*.txt`), the raw + speaker-labeled Whisper/GPT-4o JSON output per call (`evidence/Interviews/_raw/`), and a full transcription pipeline (`scripts/transcribe/`: `robust_transcribe.py`, `robust_translate.py`, `step2_label_speakers.py`, `step3_format.py`, plus dedup/repetition/run-check utilities and an `interview_guide.txt`/`core_guide.txt` the pipeline scores transcripts against). A `.gitignore` was added in the same commit. ~~**No survey response data was added** — none exists anywhere searched (this repo, the parent folder, or a separate non-git working folder at `~/Downloads/ken-case-competition/`, checked explicitly).~~ **CORRECTED, see §17: a survey had in fact been fielded and was collecting responses at the time this was written. It was not findable from the filesystem because it lived in Google Sheets/Forms and had never been exported. The claim above was true of the local files searched and false about the world — a good example of why "I searched X and found nothing" must not be written up as "nothing exists."**

### 16.2 The 7 interviews, what each actually contains

All 7 are in `evidence/Interviews/Transcripts/`, transcribed via OpenAI Whisper (verbatim, segment-timestamped; Telugu calls translated to English) with GPT-4o assigning INTERVIEWER/RESPONDENT/THIRD SPEAKER roles against the interview guide (Whisper itself does not voice-diarize). Several Telugu-language segments across multiple calls are marked `[AUDIO UNCLEAR]` by the pipeline itself — tested at 4 temperatures against both translation and original-language passes, every attempt either hallucinated or produced unstable output; the transcript honestly flags these rather than guessing, and recommends a Telugu speaker review the source audio directly.

1. **`Call Amma`** (25:02, 2026-09-08) — a household respondent who alone handles all repairs. Ongoing incident at time of call: a RO/water purifier under repair for 3+ days via a WhatsApp-chat-based service flow, still unresolved. States she spends "more than an hour every day" chasing it. Explicitly contrasts how insurance/vehicle renewals get external reminders ("digitalized... it tells you") against appliances, which don't ("you can't mark the washing machine or RO... the machine tells you, I have to mark it"). Uses the building's maintenance office only occasionally ("they come only occasionally"); found a washing-machine drum-cleaning service via an Instagram reel.
2. **`Call Sai Kakki`** (22:36, 2026-09-08) — washing machine inlet-pipe repair, resolved same-day by calling an already-known technician directly (not through a company) after self-troubleshooting steps failed. Names the company-helpline route as categorically slower and more frustrating than the direct-technician route: "if it's for the washing machine they don't connect you to the technician easily, there's a whole long process." Her husband decides spend; she'd delegate annual-servicing *scheduling* to a trusted person but not the final price-and-availability confirmation.
3. **`Call Rk Sir`** (24:26, 2026-09-09) — AC servicing booked via Urban Company after switching away from the brand (Lloyd), because the brand routed him to local franchisees who "behave in a chaotic way... charge more than what company prescribed... come late." The Urban Company technician quoted ₹3,000-4,000 for a chemical wash claiming only 60-70% of the problem was fixed by the initial foam-jet clean; Rk Sir independently cross-checked via a friend's own mechanic contact, who quoted ₹2,500-3,000 for the same job — a real instance of a household verifying price through its own informal network rather than trusting the first quote. Separately and unprompted, states some mechanics ask for money beyond the official company charge as an informal "tip," which he calls "really annoying."
4. **`Call Sarala Aunty`, two calls** (17:03 and 08:15, both 2026-09-09) — manages two remote properties (Vijayawada and Eluru) she doesn't live at, entirely through one trusted intermediary, "Vishnu Carpenter," who has his own network of other tradespeople (plumbers, electricians, painters) and is paid an unsolicited referral commission she describes giving him unprompted, not because he asked. Diagnoses issues over video call through this network. Explicitly says she keeps a physical diary of contact numbers when a phone isn't available ("I will note it in a diary and keep it") — later confirmed by a photographed artifact, see §16.3. The second call describes an explicit sequential fallback when her first-choice contact isn't available: call Basha, then Krishna, then Rana, in that order, before resorting to asking neighbors or a shop for a new number.
5. **`Call 6128maggi`** (24:54, 2026-09-09) — a young respondent who splits time between Bangalore (renting alone) and a hometown. In Bangalore, all appliances (AC, washing machine, furniture) are rented through the RentMozo app, which bundles repairs in for free as part of the rental — she never personally sources a technician for those items. At her (presumably family-owned) hometown residence, by contrast, she describes self-arranged AMCs (RO every 6 months, AC) and Urban Company bookings. Independently reports technicians padding "transportation charges" and part costs beyond the originally quoted amount without asking first — a second, independent instance of the same undisclosed-cost pattern Rk Sir described.
6. **`Technician`** (12:59, language: Telugu, translated) — a carpenter who runs a team of roughly 10 people. Allocates jobs by self-assessed urgency (a stated 2-day tolerance for non-urgent work vs. immediate dispatch for "emergency" cases) and by worker seniority (new workers are kept alongside him for 1-2 years before being sent out alone). Keeps no written job-tracking system — relies on personal memory ("I have a memory power... even if it is 2-3-4 months back, I have all the measurements in my mind"). Has an informal WhatsApp group among peer workers for passing along jobs neither can take, with roughly a 10% referral commission when that happens. **Confirms, unprompted and from the supply side, that some workers ask customers for money beyond what the booking company shows** — directly corroborating what Rk Sir and 6128maggi described independently from the customer side. When a mistake happens (wrong part installed), his stated recovery mechanism is personal: he calls the customer, explains it was an error, and either replaces the part free or removes the charge — an informal, relationship-based resolution with no formal process behind it.

### 16.3 Two photographed evidence artifacts (not yet in this git repo)

Found in a separate, non-git working folder the user also uses, `~/Downloads/ken-case-competition/evidence/notes/` (this folder also contains `00-PLAN.md`/`01-INTERVIEW-KIT.md`/`02-SURPRISE-LOG.md`/`03-ANSWERS.md` — a strategy/template kit, further described in §16.5 — plus `Workflows/` team-ideation photos not detailed here):
- **"Padmaja RO service date.jpeg"** — a Havells RO purifier's own factory AMC sticker, with the *next* service date handwritten in marker directly onto the sticker ("NEXT 15/M/26"), plus a separate, brightly-colored "Contact for Service" card taped to the machine body listing 4 phone numbers for "Kumari Agencies Visakhapatnam." This is a real, physical instance of exactly the reminder-marking gap Call Amma described verbally — no digital reminder exists, so the household writes the date directly onto the machine and keeps the service contact taped to it.
- **"Sarala aunty notes 2/3/4.jpeg"** — handwritten diary/ledger pages (Telugu) recording job amounts, balances, and a tradesperson's phone number for Eluru work (e.g., a total/balance breakdown around ₹13,500 with a ₹2,000 advance, and a separate page listing amounts against "Pandu" and "Kasulu" with the number 9618390470). This directly corroborates what Sarala Aunty described verbally: keeping a physical diary of technician contacts and running balances when there's no formal system.

These have not yet been copied into this git repo's `evidence/` folder or given consent/attribution metadata — see §16.4.

### 16.4 The real, unresolved compliance gap

The competition's ground rules require informed consent and require every published quote to be tagged **age-band + city, never a name**; fabricated or misattributed evidence is stated as explicitly disqualifying. The team's own consent-tracking table (`~/Downloads/ken-case-competition/01-INTERVIEW-KIT.md`, rows 1-8) is **completely blank** — no age-band, city, or consent checkbox filled in for any interview, even though verbal consent is audible on-recording for at least the Amma and Sai Kakki calls ("Is it okay if I take notes and would you be okay if I also record the call?" → "Yes, it's okay"). This is a real, fixable gap (listen back to each call's opening ~90 seconds and fill in the table), not yet closed as of this write. Because of it, `answers_draft.md` (§16.6) paraphrases findings rather than attributing verbatim quotes to invented demographics.

### 16.5 A second, separate working folder exists outside this git repo

`~/Downloads/ken-case-competition/` (not a git repository, not the canonical shared workspace) contains a self-contained strategy kit apparently built in an earlier session: `00-PLAN.md` (a detailed day-by-day competition plan — interview priorities, a rail-decision-gate scoring table, pre-written seed drafts for several answers, a "how teams lose this round" section, and a verification checklist), `01-INTERVIEW-KIT.md` (printable per-role interview scripts + the blank consent log referenced in §16.4), `02-SURPRISE-LOG.md` (a blank "things we did not expect" tracker meant to be filled after every interview — never filled in), `03-ANSWERS.md` (a blank fill-in-the-blank template for all 10 answers, with the exact word-limit structure and pre-written seed language for several answers), and an `evidence/` folder whose `survey/` and `interviews/` subfolders contain only `.gitkeep` placeholders (empty), while `Workflows/` and `notes/` contain real photos (see §16.3). **This folder's plan content is consistent with, and in some places more detailed than, this git repo's own planning docs (`narrowed_problem.md`, `research_plan.md`) — treat the two as complementary, not conflicting; `00-PLAN.md`'s rail-decision-gate table and pre-written seed answers were used directly as a starting structure for `answers_draft.md`.**

### 16.6 `answers_draft.md` — the first real, evidence-grounded draft of Q1-Q10

New file, repo root: `answers_draft.md`. Built directly from the 7 transcripts above, not from any hypothesis in `narrowed_problem.md`'s hypothesis bank (H1-H6) — those hypotheses were probes to ask about, not findings, per that file's own instruction, and the actual insight that emerged (below) wasn't one of them.

**The Q2 insight actually chosen, and why**: once a repair is booked through an app or a brand, households assume the quoted/booked price is the whole transaction — but technicians routinely ask for a separate, undocumented cash top-up after the official payment clears. This is the strongest candidate in the dataset because it is **corroborated three independent ways**: two households (Rk Sir, 6128maggi) describe it from the customer side without prompting each other (separate interviews), and the technician interview confirms the same practice exists, unprompted, from the supply side. No other candidate pattern in these 7 interviews has three-way independent corroboration. It also passes the deletion test against the drafted Q3 loop (step 5, "confirms the final price before release," stops making sense without it) and does not restate anything in The Ken's own published opening document.

**What's genuinely drafted and evidence-backed**: Q2 (58 words), Q3 (all 6 cells within the 15-word limit, step 5 marked as carrying the insight), Q4 (Payments and Voice evidence-backed; Logistics explicitly flagged as thin — no interview surfaced a parts-shipping delay), Q5 (39 words), Q6 (29 words, ties to the Padmaja photo), Q9 (59 words, uses the team's own RentMozo finding as a real counterfactual data point, not just desk research), Q10 (Product Strategy, already locked).

**What's explicitly NOT drafted, and why — do not fill these in from inference**:
- **Q1's three per-member personal-connection lines** — these must come from Sricharan, Prathyusha, and Atharv's own lives; nothing in the 7 interviews substitutes for them. (The team-asset half of Q1 — "we got a working carpenter running a 10-person crew on the phone" — is drafted, since that's a real, checkable claim.)
- **Q8** — deliberately left blank; the team's own planning materials describe this as a personal-values call for one team member to make honestly, not something to reason into from evidence.
- **Q7** — drafted but explicitly flagged inside `answers_draft.md` as less evidenced than the others and needing more team discussion before finalizing.

### 16.7 Current real state of `progress.md` (as of this same update)

`progress.md` was rewritten in the same pass to reflect all of the above: all 7 interviews now checked off with one-line summaries, the artifact photos noted, Stage 2 (synthesis) marked done for the corroboration/deletion-test steps, Stage 3 (drafting) marked done for 8 of 10 answers with the 2 exceptions above called out explicitly, and a rewritten "Known open risk" section leading with the consent-metadata gap (§16.4), followed by the 2 missing personal answers, the same-day deadline, the fact that no survey exists, and the thin Logistics answer — in that priority order. **Two of those five have since changed: the survey does exist (§17), and the Logistics answer moved twice before landing (§17.4). `progress.md` was rewritten again in the §17 pass.** Read `progress.md` directly for the exact current checklist state; it is the authoritative live tracker, this file is a snapshot synthesis.

### 16.8 Immediate next actions, in priority order, for whoever reads this next

1. Fill in the consent log (§16.4) — real, fast, and a hard submission blocker if skipped.
2. Get Sricharan, Prathyusha, and Atharv to each write their one-line Q1 personal connection, and have one of them write Q8.
3. Read `answers_draft.md` as a team, decide whether the Q2 insight is the one to lock, and cut every answer to its exact word limit against the live form (not just the public page).
4. If time allows, do one more pass on the transcripts (or a quick follow-up message to the technician) specifically hunting for any parts-shipping/logistics detail, since Q4's Logistics answer is currently the weakest-evidenced of the four drafted rail/mechanism answers.
5. Move the 2 photographed artifacts (§16.3) into this git repo's `evidence/` folder before assembling the final evidence pack, and decide whether they're used with a name/consent tag or anonymously.

---

## 17. UPDATE — 2026-09-10 (later same day): the survey exists, and the answers were rewritten

**This section supersedes §14 and §16 wherever they disagree, and specifically corrects §16.1's claim that no survey data exists.** Everything below was pulled from the live Google Sheet, all 7 transcripts re-read in full, the raw Whisper JSON, all 16 evidence photographs viewed directly, The Ken's founding column, and `research/report-source.md` p.16.

### 17.1 A survey was fielded — 19 responses

Provided by the user as two Google links and retrieved via the sheet's CSV export endpoint (the Forms `/edit#responses` view requires the owner's login and is not reachable; it was not needed, because the response sheet carries both the exact question wording and every response).

- Sheet: `docs.google.com/spreadsheets/d/1soCnQVNXd7TwVzjXAKX3Jb9TAr_S98wF4K6G1__Lo8Q`
- Form: `docs.google.com/forms/d/1-Nozi-zEWcabocXyEBPJnIWcmYWo7xk4YfoWosbU-h4`
- **19 responses, 8 Sep 22:12 → 10 Sep 09:50 IST. 12 qualified (arranged a repair in the last 6 months), 7 screened out.**
- 21 questions plus timestamp. This is a **third** survey instrument, distinct from both `survey_guide.md` (30 items) and `research/survey_guide_qa/Survey_Plain_Language_v2.md` (17 items) described in §7 — it is closest to the 17-question version but not identical. The fielded wording is now the only one that matters; the other two are design artefacts.

Archived to **`evidence/survey/`**: `Ken2026_Survey_Responses_RAW.csv`, `.xlsx`, `Ken2026_Survey_Response_Table.md` (all 19 responses rendered per-respondent plus verbatim question wording), and `README.md` (analysis).

**Compliance: clean, and better than the interviews.** No name, no email, no phone collected. Q1 is a combined age-and-consent gate — *"I am 18 or older, and I agree to answer this survey voluntarily and anonymously"* — all 19 agreed. Age band and city captured for all 19, which is exactly the competition's publishing format. **Do not back-fill names.** The `[team-controlled contact]` placeholder flagged in §14 is moot; the survey has closed.

**Sample, stated honestly**: 45–54 ×9, 35–44 ×6, 65+ ×3, 25–34 ×1; Woman 11, Man 7, prefer-not-to-say 1; Hyderabad 9, Visakhapatnam/Vizag 6, Bengaluru 2, Munich 1, Gandhinagar 1. Convenience sample — licenses mechanism claims only, never prevalence. **No Eluru respondents at all**, despite `narrowed_problem.md` §4 Decision 3 building the whole comparative design on Hyderabad + Eluru. The tier-3 leg of the argument now rests on the interviews alone.

### 17.2 The two survey findings that changed answers

1. **7 of 12 qualified incidents split the four roles** — decide / approve the cost / pay / give home access — **across more than one person.** Only 5 of 12 had one person holding all four. This is the strongest single number the team has and it converts the delegated-authority (Payments) argument from an assumption into a measurement. It also generalises Sai Kakki's interview remark (*"my husband decides… availability I decide"*) from a quirk into the majority pattern.
2. **0 of 12 incidents involved a part or appliance being moved** — 10 "no", 2 "not sure", none "yes". **This disconfirms the Logistics rail from the demand side.** See §17.4.

Supporting: 7 of 12 keep no service record at all (*"I don't track it, I just call when needed"*); mean effort 2.17/5 with 8 of 12 rating 1–2; 6 of 12 needed at least one follow-up and 2 needed three or more; the single effort-5 case is also the one where a promised time was broken *and* three-plus follow-ups were needed. Free-text on what respondents would always keep for themselves names cost and verified outcome — never the booking or the calling.

**The "one answer you did not expect" line** the page explicitly asks for is drafted in `evidence/survey/README.md`.

### 17.3 `answers_draft.md` was rewritten, not patched

Four answers changed materially from the §16.6 version:

- **Q2** — broadened from "undocumented cash top-up" (real, but one symptom, and resting partly on a shaky Telugu translation where "app" was rendered "Apple") to the mechanism beneath it: *households already delegate the chasing; what they never delegate is verification, because the price is set after the technician is inside and the machine is open — so they keep ledgers of people and money, not machines.* Corroborated by 5 households + the technician on leg 1, 5 more on leg 2, the survey on leg 3, and both photographs on leg 4. It inverts The Ken's own published question (*"how does the service memory get built without data entry?"*) rather than answering it as posed — households are already doing the data entry, just about counterparties rather than assets.
- **Q5** — the previous framing targeted spend caps. `research/report-source.md` p.16 is explicit that *"'let an agent pay under a cap' is already a documented capability, not a defensible missing-capability claim."* Retargeted at what that page lists as genuinely unverified: escrow / conditional hold / milestone release, **and a payee who is nobody's registered merchant** (Vishnu Carpenter, Basha, the 10-person crew).
- **Q6** — changed from SMS-inbox read access to the service contacts plus the UPI payments already sent to those numbers. This resolves a real conflict between two canonical sources: `00-PLAN.md` recommended the inbox, `report-source.md` p.17 explicitly warns against asking for it. The evidence broke the tie — what households keep is a counterparty ledger.
- **Q4** — see §17.4.

Q9 switched from Bajaj Finserv to Urban Company (we have first-hand evidence about the latter from two respondents and none about the former), with the inaction explanation labelled a hypothesis per p.18's rule. All twelve word-capped answers were verified programmatically against their limits.

### 17.4 The Logistics position moved twice — record it, don't hide it

§16.6 called Q4's Logistics answer "honestly thin." A re-read of the transcripts found that was wrong: the parts friction was there and had been missed (6128maggi billed ₹200 "transportation" plus a marked-up part for a sourcing trip she never asked for [18:06–18:27], explicitly contrasted by her against Amazon/Blinkit same-day [17:47]; Sai Kakki's technician predicting the part from a photo of the model number, the replacement proving poor quality only after use [15:45]; Sarala Aunty carrying a four-burner stove to the repair shop; Rk Sir noting car, laptop and phone all require household transport), and the team's own Miro technician journey map names the breakpoint outright.

Then the survey disconfirmed it: **0 of 12.** The landing, now in `answers_draft.md`: the sourcing trip is real on the supply side but **invisible to the person financing it**, which is a sharper claim than "logistics matters" — stated as an interpretation, not as corroboration. This makes choosing Payments for Q5 evidenced rather than assumed: logistics was tested and it failed.

### 17.5 Consent — the real submission gate, now documented

**`evidence/consent/CONSENT_LOG.md`** (new) holds the full status table, the exact retrospective-consent message to send, and artefact-redaction instructions. Summary, verified against the raw Whisper segments rather than the transcripts alone:

- Recording consent is audible in **6 of 7** calls, and Rk Sir, Sai Kakki and 6128maggi each explicitly reconfirmed anonymised use at the close — **better than §16.4 recorded.**
- **The Technician recording has no consent capture at all.** It opens cold at *"Hello, Uncle."* Under `research/Fieldwork_Templates.md` §3's own rule (*"If relevant consent is absent, mark the evidence NOT CLEARED FOR SUBMISSION"*) it cannot currently be used — and he is the respondent Q1's team statement is built on.
- **Nobody was told their words may be published by The Ken.** Consent was for recording and anonymous research use, which is not the same thing as the ground rule requires.
- **No age band or city for any of the 7.** Three granted follow-up contact, so this is a message away.

### 17.6 Two factual corrections to this document's own sources

- **`best_practices.md` §1.2–§1.3 cites material that is not in the file it names.** The Deepak Shenoy "adjusted/ebitda" quote, the "we will leverage AI/ML" commentary, and the Metamorphosis / Illuminaire / Ken-spiracy Theorists / Kenith / ArogyaGhar.ai / ROI Rangers examples are all attributed to `files/ken_case_competition_2025_winning_submissions.txt`. A direct grep returns **zero hits for every one of them**, and Tek-Ken and Voldemort are 2025 teams in that file, not the 2024 quick-commerce finalists §5.1 describes. That material may have come from web sources never captured to `files/`. It is internal guidance, not a submitted claim, so nothing breaks — but it cannot be verified against the source it cites, and §5.1 above should be read with that caveat.
- **Opening numbering.** The `~/Downloads/ken-case-competition/` kit (§16.5) calls this "Opening 01" and misnumbers every other opening it cites — its Q7 seed calls "Getting your money back" Opening 02 when the live page numbers it 09; its Q8 seeds misnumber "Sticking to the goal" (08, not 14) and "Running your wedding" (14, not 07). `report-source.md` p.2 explains the confusion: the picker lists this opening second while its image asset still carries number 11. **Select by title, never by position.** Q8 requires naming an opening, so copying those seeds names the wrong one. The live-page list is reproduced in `answers_draft.md` §Q8.

### 17.7 Immediate next actions, superseding §16.8

1. **Verify in the live form that the registered opening is "Keeping the machines running" by title.** The curl'd page shows a chosen opening of "Keeping up with the school," almost certainly an unauthenticated template default — but switching resets evidence, so check before anything else.
2. **Send the retrospective consent message** in `evidence/consent/CONSENT_LOG.md` to all seven, and get the Technician's consent specifically. Collect age band and city.
3. **Sricharan, Prathyusha and Atharv each write their Q1 line; one of them writes Q8.** Nothing else is blocking those.
4. **Redact before pushing**: the artefact photographs show third-party tradespeople's phone numbers (9618390470, 8106529187, a partial 9912788…) and a device serial number. The repo is shared. The survey data is safe to push as-is.
5. **Resolve the ownership of `Padmaja RO service date.jpeg`** — the name in the filename is not one of the seven interviewees, so whose machine it is and whether that person consented is unresolved.
6. **Assemble the evidence pack**: all five attachment types the page names are now available — recordings (cut clips around the §Q2 timestamps; 133 MB of full audio is too large), workaround photographs, the survey with raw answers plus the unexpected-answer line, team working notes (`evidence/Workflows/`), and AI working logs (this repo).
7. **Submit by 6 PM**, not 11:59 PM. (`00-PLAN.md` says 6 PM, `report-source.md` says 8 PM — take the earlier.)
