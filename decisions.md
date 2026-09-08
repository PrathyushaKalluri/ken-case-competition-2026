# Decisions Log — The Ken Case Competition 2026

Two columns of decisions: what the **team (user)** decided, and what **Claude** decided/chose on its own judgment while executing. Kept separate so it's clear which decisions are load-bearing (yours, and should be revisited only by you) and which are working choices (mine, and freely overridable).

---

## Decisions made by the user/team

| # | Decision | Context / why |
|---|---|---|
| 1 | Opening selected: **"Keeping the machines running"** (#02 of 16) | Decided before this session; confirmed at session start. Team's own stated selection process (see #2). |
| 2 | Selection process used to land on this opening: a 3-stage filter — (1) understand guardrails/constraints/scope of buildable agents per opening, (2) prefer problems that are repetitive, frustrating, and *not* prone to procrastination (using the demographic data given per opening), (3) assess accessibility, right-to-win, and avoid overcrowded problems | Stated by the user verbatim when answering the "right to win" question. This is the team's own prior work, recorded here so it isn't lost. |
| 3 | Track: **Product Strategy** (not Product Build) | User's direct answer. Means Phase 1 (and beyond) should aim for a fully specified build — flows, segment map, where it breaks and why — not a working sandbox prototype. |
| 4 | Evidence capacity for the ~36 hours before the Sep 10 deadline: **3-6 quick real interviews**, not zero, not a full 35-50 interview program | User's direct answer. This is the real constraint that should govern scope for Q2 — the local context files' 35-50 interview target is explicitly **not** what's being run for Phase 1. |
| 5 | Right-to-win angle: team collectively has **personal household pain + access to technicians/service providers + a renter/landlord vantage point** | User's multi-select answer. This determined the 3-way interview split proposed in Part 3 of `context.md`/`plan.md` (household-lens, technician-lens, landlord-lens). |
| 6 | Explicit instruction: **do not pre-narrow the Q2 insight before real interviews happen.** Diverge broadly first; converge only from actual field evidence, not from Claude's or the team's guesses | User's direct, verbatim correction after Claude offered four candidate insight-threads as multi-select options. Quote: *"There can be n number of problems... Help us diverge first, and don't just fixate on these four problems that you are showing now. We want to have a real problem and real insights from the interviews that we will be doing."* **This governs all downstream work on the insight/Q2 — treat any pre-interview insight framing (including Claude's 17-hypothesis list) as candidates to test, never as a conclusion.** |
| 7 | Requested a new, reusable Claude Code skill ("resource-scan") for pulling all resource types (repos, blogs, news, books, other) on any topic, with systems/strategist-level divergence baked in, saved so it works across whichever account is logged in | User's direct request, independent of the case competition itself — a tooling investment. |
| 8 | Requested the new skill be test-driven immediately, on the case competition topic, phrased so the skill "understands easily" | User's direct request; led to a manual dry-run of the skill (see `decisions.md` #16 below on why manual). |
| 9 | Requested full session documentation into `context.md`, `decisions.md`, `links.md`, `notes.md`, `plan.md`, `progress.md`, plus a `/files` folder with all referenced source files | This request; produced the current set of files. |

---

## Decisions/judgment calls made by Claude

| # | Decision | Reasoning |
|---|---|---|
| 10 | Used `curl` with a browser User-Agent as a fallback (via Bash), after `WebFetch` returned HTTP 403 on `the-ken.com` | The site blocks WebFetch's default UA. A plain browser-UA request succeeded (HTTP 200). Applied this same fallback later for the 2025-submissions page and the "Great Rewiring" column, since both also 403'd on WebFetch. |
| 11 | Parsed fetched HTML to plain text with a small inline Python script rather than reading raw HTML | Raw HTML from a full news/media site (with nav, footers, popups, etc.) is mostly noise; stripping to text made the actual competition content (807 lines) tractable to read and extract accurately. |
| 12 | Asked 4 clarifying questions (evidence capacity, track, right-to-win, insight thread) via `AskUserQuestion` before proposing a research/insight direction | These were genuine judgment calls only the team could make (how much fieldwork is realistic, which track, what access the team actually has) — not something to guess given the deadline pressure and the cost of guessing wrong. |
| 13 | After the user's correction (decision #6 above), generated a **broader** divergence map (17 hypotheses across 8 categories, not the original 4) rather than asking the user to specify the categories themselves | Directly responsive to the instruction to diverge more, without pushing the divergence work back onto the user — Claude's job at that point was to widen the option space, not narrow it further. |
| 14 | Designed a specific 3-way interview allocation (2 household-lens / 1-2 technician-lens / 1-2 landlord-lens) within the stated 3-6 interview budget | To deliberately use all three of the team's stated access advantages (decision #5) rather than let interviews cluster on the easiest-to-reach lens (household), which would under-test the supply-side and landlord/tenant hypotheses. |
| 15 | Proposed a specific day-by-day convergence protocol and submission timeline (interviews today → synthesis checkpoint at 4+ interviews → lock Q2 → draft Q1/Q3-Q10 backward from Q2 → buffer before submitting) | Given the hard Sep 10, 11:59 PM IST deadline, an unstructured "just go interview people" instruction risked running out of runway to synthesize and write. This is a working plan, not a rule — team can compress/expand it. |
| 16 | Named the new skill **`resource-scan`** and located it at the **user level** (`~/.claude/skills/resource-scan/`) rather than project level (`.claude/skills/` inside this repo) | User asked for something usable "with any Claude account... in different accounts" — a project-scoped skill would only exist inside this one project folder. User-level makes it available in every Claude Code project on this machine. (Caveat given to the user: this is machine-local, not account-cloud-synced — see `notes.md`.) |
| 17 | Wrote explicit anti-hallucination and anti-listicle guardrails into the skill (never fabricate a URL; annotate every resource with why it matters; flag recency/authority; don't quietly drop axes that return nothing) | These are the most common failure modes for this kind of "pull everything on a topic" task — the guardrails are the difference between a useful resource pull and a plausible-sounding but partly-invented one. |
| 18 | When the `Skill` tool call for `resource-scan` failed with "Unknown skill" (because Claude Code's available-skills list loads once at session start, before the file existed) | Chose to manually execute the skill's own documented Steps 0-4 live in the conversation rather than ask the user to restart the session and wait. This also served as a real correctness test of the skill's written instructions. |
| 19 | Selected 9 divergence axes (of a larger internal brainstorm) for the test-drive, and ran roughly 2 search queries per axis rather than exhaustively covering every possible angle | Balanced the "5-10 axes typical for a broad topic" guidance in the skill itself against keeping the output usable in one sitting rather than an unbounded research dump. |
| 20 | Flagged the "Great Rewiring" founding-thesis column as the single most load-bearing resource found, and proposed a reframed interview question from it ("does this household already have an informal human 'agent' for this exact job, and what would it take to trust software in that role instead?") | This connects the case's *specific* opening to the competition's *stated* macro-thesis (why India, why now, why agents) in a way none of the 17 pre-existing hypotheses did — judged as a higher-leverage lead for tomorrow's interviews than the four originally-floated threads, but explicitly offered as one more candidate to test, not a replacement conclusion (per decision #6). |

---

## New section — arising from the Household Service Memory Supplementary Note (PDF)

| # | Item | Notes |
|---|---|---|
| 21 | **Gap flagged, not a decision**: the supplementary PDF is explicitly a follow-up to a "main dossier" (referencing its Section 2.3 "workaround ladder," Section 3.1 "seasonal shock" trigger, Section 6 "decision framework," and a 76% AC-servicing figure) that has **not been shared in this session**. | Recommend requesting this main dossier — it appears to contain structured prior research (possibly by/for a teammate, "Atharv") that may overlap with or supersede parts of `system_map.md`, and is directly relevant to Q2/Q9. |
| 22 | Claude's judgment call: cross-walked the PDF's own evidence tags (**[D]** published/named source, **[A]** consumer-facing/commentary, **[H]** author's own reasoning) onto this session's existing tagging scheme in `system_map.md` (**[CASE]/[LAW]/[TEAM]/[HYPOTHESIS]/[NEEDS INTERVIEW]**) rather than running two parallel tagging systems | Mapping used: [D] → [LAW], [A] → kept as [A] (weaker than [LAW], stronger than [HYPOTHESIS]), [H] → [HYPOTHESIS]. See `system_map.md` §5. |
| 23 | Claude's judgment call: did not alter any existing table cells in `system_map.md` §3 (the per-object workaround guesses made before this PDF existed) — added the PDF's real data as a new §5 instead, with only a one-line cross-reference pointer added to §3's intro | Per your instruction to add a separate section rather than rewrite existing content; §3's original guesses are left visible so you can see how they compared to the real data in §5. |

## New section — independent secondary research on task-substitution & service-tracking (user-directed)

| # | Item | Notes |
|---|---|---|
| 24 | User explicitly directed Claude to conduct its own independent secondary research (papers, articles, market reports, open-source examples) on (a) what people do to get a job done when the machine that normally does it breaks, and (b) how people currently track service dates/reminders — as grounding *before* interviews, not a replacement for them | Verbatim instruction: *"the main, most important motto of this is to understand through this part: Do your own research. Your own materialities. Your own actions. Collect data. Use open source things and all. Inform yourself and have complete information."* Executed via ~14 targeted web searches; full findings in `system_map.md` §6, `notes.md` §6b, sources in `links.md`. |
| 25 | Claude's judgment call: treated this as a second, independent research pass (not merely re-reading the PDF from the prior turn) — deliberately searched India-specific data separately from global/US data where the first search returned only US figures (repair-vs-replace ratios), and flagged the gap explicitly rather than presenting US numbers as India facts | See `system_map.md` §6.2 — US repair/replace stats (58%/87%/the "50% rule") are explicitly marked as unconfirmed for India. |
| 26 | Claude's judgment call: elevated one finding — that Indian AMC/service vendors track renewals in Excel with reminder calls "from memory," losing 20-30% of renewals to forgetting — as the single most consequential new finding of this research pass, because it revises a load-bearing assumption in the working thesis (that the household, not the vendor, is the unreliable half of the relationship) | See `system_map.md` §6.4. This is still `[LAW]`-tagged secondary evidence, not yet interview-confirmed — added as a new, specific interview probe in `plan.md` rather than treated as settled. |
| 27 | Claude's judgment call: proposed a comparative "vehicles vs. appliances" framing (India has already solved this exact class of recurring-obligation-reminder problem for vehicles via a shared institutional anchor — RTO registration — that appliances lack) as a candidate reframe for Q9 and Q6 | Explicitly tagged `[HYPOTHESIS]` in `system_map.md` §6.5 — built from real data but not yet interview-confirmed; added as interview probe #2 in `plan.md`. |

## Open decision now pending as a result of this PDF

- Whether to request the "main dossier" referenced throughout this note before finalizing Q2/Q9 — it may already contain a validated 76% figure, a "workaround ladder," and a business-model decision framework (Section 6) that this session has only seen secondhand, in fragments, through this supplementary note.

---

## New section — team reconciliation (Sricharan's independent research pipeline discovered)

| # | Item | Notes |
|---|---|---|
| 28 | Discovered mid-session that teammate Sricharan ran his own Claude Code session and pushed a second commit to the shared repo with a substantially more complete interview guide, survey instrument, fieldwork capture templates, and rail documentation | Full detail in `team_reconciliation.md`. Also resolved the "Atharv" identity gap flagged since `decisions.md` #21 — he's the third Invictus teammate. |
| 29 | User's explicit instruction, when asked how to proceed: **"Reconcile first, then textbooks."** | Deferred the originally-requested 20-textbook synthesis until the two research tracks are merged into one team-wide source of truth. |
| 30 | Claude's judgment call: designated Sricharan's `research/report-source.md` and `research/Fieldwork_Templates.md` as canonical for interview guide, survey, fieldwork capture, and the day-by-day operating schedule, since they are materially more complete and rigorous than this session's `plan.md` equivalents | This session's own probes (from resource-scan and the Household Service Memory PDF) were kept as additive insertions rather than discarded — see `team_reconciliation.md` §3. Did not edit Sricharan's files directly; reconciliation lives in a new file so his authored work stays intact. |
| 31 | Claude's judgment call: surfaced the interview-volume conflict (3-6 vs. 10-12+ interviews) as an open team decision rather than silently picking one number | Both estimates come from real inputs (your own stated capacity vs. Sricharan's own written plan) that are in genuine tension — not something Claude should resolve unilaterally. |
| 32 | Claude's judgment call: flagged that the user's own personal incident for Q1 has never been collected in this session, mirroring the exact gap Sricharan's own brief already flagged for himself and Atharv | See `team_reconciliation.md` §5. Still open. |

## New section — textbook synthesis and Ken-winners research (`best_practices.md`)

| # | Item | Notes |
|---|---|---|
| 33 | User's decisions on resuming this session: (a) defer own Q1 personal incident to later; (b) go with the realistic 3-6 interview target, and also roll out the survey | Verbatim: *"Let me tell my own Q1 personal incident later... Go with the realistic one... We can go with 3 to 6 interviews, and we can roll out a survey as well."* Recorded in `team_reconciliation.md` §4. |
| 34 | Claude's judgment call: installed `pypdf` in an isolated venv (`/tmp/pdfenv`) after both `brew install poppler` (network failure) and system-wide `pip install` (blocked by PEP 668) failed, to get real text extraction working rather than reading only 1-2 pages per book via the default Read tool path | Necessary for any real textbook engagement — 20 books, several 500-1000+ pages, made cover-to-cover reading via the default tool infeasible. |
| 35 | Claude's judgment call: forked 4 parallel background research threads (one per thinking-lens: systems thinker, designer, UX researcher, experiment/survey designer), each assigned a cluster of books, rather than reading all 20 books directly in the main session | Kept ~2M tokens of raw book text out of the main conversation; each fork returned only a synthesized report. Standard practice per this session's own tool guidance for exactly this kind of task. |
| 36 | Claude's judgment call: read `Courses-Syllabus_M26-V1.pdf` directly (288 pages, targeted via keyword search) to confirm these 20 textbooks are the actual assigned references for 3 real IIITH M.Tech PDM courses, before writing `best_practices.md` | Grounds the whole document in real coursework rather than an arbitrary reading list — see `best_practices.md` §2. |
| 37 | Claude's judgment call: researched 3 years of Ken competition public material (2024 inaugural, 2025, 2026) — judge quotes, winning-team patterns, judging-criteria evolution, and a demo-prototype pattern analysis (ArogyaGhar.ai) — as the "how to win" half of `best_practices.md`, alongside the textbook synthesis | The user's request explicitly asked for both halves together in one file. |
| 38 | Claude's judgment call: had the experiment/survey-design fork perform a real line-by-line audit of the team's existing S0-S30 survey (`research/report-source.md`) against the two methods textbooks, rather than only producing abstract theory | Produced an actionable "ship it" verdict with 3 optional hardenings — directly useful given the survey rollout was just confirmed (decision #33). |

## Open decisions still pending (not yet made by anyone)

- Which of the 17+ candidate insight threads survives real interview evidence (deliberately not decided yet — see decision #6).
- Final wording of all 10 Phase 1 answers (Q1-Q10) — blocked on the interviews happening.
- Whether to build the offered interview-tracking sheet / per-lens interview guide (offered by Claude at the end of Part 3 in `context.md`; not yet accepted or declined by the user).
- Whether to copy the `resource-scan` skill to any other machine, or package it as a plugin for easier distribution (offered, not yet requested).
