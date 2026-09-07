---
name: resource-scan
description: Given a topic, expand it into its surrounding system like a strategist/PM (adjacent domains, upstream/downstream concepts, stakeholders, alternate framings) before searching, then pull open-source repos, blogs/articles, news, books, and other resources across that whole system, not just the literal topic. Use whenever the user asks to research a topic broadly, wants a reading list, wants repos/tools for a topic, or wants "everything available" on a subject.
---

# Resource Scan

Pull every useful resource on a topic — but only after diverging beyond the literal topic into the system it sits inside. A flat list of links for the exact phrase the user typed is the failure mode this skill exists to avoid.

## Step 0 — Load tools

This skill leans on live web search and fetch. If `WebSearch` and `WebFetch` are deferred, load them first:

`ToolSearch({query: "select:WebSearch,WebFetch", max_results: 5})`

Use `Bash` + `gh` (if authenticated) as a second path for GitHub search when useful — `gh search repos`, `gh search code` — but don't block on it; WebSearch with `site:github.com` works without auth.

## Step 1 — Diverge before you search

Do this thinking pass yourself, don't ask the user to do it. Take the given topic and produce a short **system map**, not just synonyms:

- **The topic itself** — the literal thing asked for.
- **Adjacent domains** — fields that share a mechanism, a user, or a failure mode with this topic, even if the name is different.
- **Upstream concepts** — what this topic depends on or is built out of (primitives, prerequisites, infrastructure).
- **Downstream concepts** — what this topic enables or feeds into (applications, consumers, follow-on problems).
- **Stakeholders/personas** — who touches this system and from what angle (builder, buyer, regulator, competitor, end user) — each often has a different resource trail (a builder reads repos and RFCs; a buyer reads market reports; a regulator reads policy briefs).
- **Alternate framings** — the same underlying problem as it's known in a different industry, era, or vocabulary (old term, academic term, industry jargon, competing school of thought).

Write out this map explicitly (5-10 axes is typical — fewer for a narrow technical topic, more for a broad strategic one) before running a single search. Each axis becomes a search thread in Step 2. This is the difference between "resources about X" and "resources about the system X lives in" — the second is what makes the output feel like a strategist's pull, not a keyword search.

Calibrate divergence to the ask: a narrow technical topic ("Rust async runtimes") still gets upstream/downstream/adjacent treatment but the axes stay tight and technical; a broad strategic topic ("household service coordination") earns the full spread including stakeholders and alternate framings. Don't pad a narrow topic with strategist axes it doesn't need just to hit a count.

## Step 2 — Pull resources per axis, across categories

For each axis from Step 1, search across all of these categories. Don't front-load only the literal topic's category results and skip categories for the adjacent axes — the adjacent axes deserve the same breadth.

- **Open-source repos** — `site:github.com`, `site:gitlab.com`, "awesome list" for the topic, GitHub Topics pages, and via `gh search repos <query> --sort stars` when available. Note stars/last-commit recency when visible — a dead repo from 2016 is a different kind of resource than an active one.
- **Blogs & articles** — engineering blogs, Substack/newsletter writeups, independent analysis. Prefer primary sources (the team that built the thing) over aggregator rehashes.
- **News** — recent developments, launches, funding, regulatory moves; bias toward the last 6-12 months unless the user wants historical context too.
- **Books** — search "best books on X", publisher catalogs, O'Reilly/Manning/university-press listings, well-regarded reading lists. State clearly these are found via search, not from memory — don't rely on your own training-data knowledge of "classic books" without verifying via search that they're still the standard recommendation.
- **Other resources** — papers (arXiv, Google Scholar, SSRN), conference talks, podcasts, courses, standards/RFCs, datasets, active forums or communities (Discord, subreddit, HN threads), company/product pages that define the space.

Run enough distinct queries per axis to surface real variety — a single query per axis under-covers it. Vary phrasing (jargon vs plain language) since different resource types use different vocabulary for the same concept.

## Step 3 — Guardrails

- **Never fabricate a URL.** Every link in the output must come from an actual search/fetch tool result in this conversation. If coverage on an axis or category is thin, say so plainly rather than padding with invented or half-remembered links.
- **Dedupe** across axes — the same repo or article often surfaces from multiple search threads; keep it once, under its strongest axis.
- **Annotate, don't just list.** Each resource gets one line on *why it matters* and *which axis/system-question it answers* — not a bare URL dump. A reader should be able to tell from the annotation alone whether it's worth opening.
- **Flag recency and authority** — distinguish a primary source / maintained repo from a stale mirror or low-effort aggregator post.
- **Don't over-fit to the obvious axis.** If every result is about the literal topic and none of the adjacent/upstream/downstream axes turned up anything, that's a signal to broaden the queries, not to quietly drop those axes from the output.

## Step 4 — Output

Default to a structured markdown response in the conversation, organized as:

1. **System map** — the axes from Step 1, one line each, so the reader sees the divergence logic before the link list.
2. **Per axis**: Repos / Articles & Blogs / News / Books / Other — only include categories that actually returned something.
3. **Close with 2-3 sentences of synthesis** — what the resource landscape as a whole suggests (where the activity is concentrated, where it's thin/whitespace, which axis turned out to matter more than expected) — the strategist read, not just the librarian pull.

Offer (don't default to) an Artifact only if the resource set is large enough that a browsable/filterable page would genuinely help, or the user says they want to share or revisit it — per artifact-design guidance, load that skill first if you go that route.
