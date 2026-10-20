# LOGOS Growth System v1

Overseas lead generation for LOGOS WEB STUDIO (AU / SG / UK / US). Python stdlib only, no paid services, nothing is ever sent automatically.

Strategy: [PLAYBOOK.md](PLAYBOOK.md) · Research: [research/](research/) · Leads: [leads/master.csv](leads/master.csv) · Drafts: [outreach/drafts/](outreach/drafts/)

## Pipeline

```
discover (search research / OSM)  ->  leads/raw_*.csv
ingest   dedupe into leads/master.csv (lead_id, status=new)
audit    fetch each homepage once: HTTPS, mobile viewport, footer year, builder, form/booking, tap-to-call, PSI score*
score    0-100 + tier A/B/C using config/scoring.json
draft    tier-A -> outreach/drafts/<lead_id>.md  (status draft_pending_approval)
report   funnel snapshot
```
`python run.py` runs everything; `python run.py --no-audit` works offline. *PSI needs a free Google API key in `PSI_API_KEY`.

## Rules baked in
- Observations in drafts come only from recorded evidence or the audit. No invented facts.
- Drafts are never sent by code. Owner approves, then sends manually and sets `status=contacted`.
- Every draft carries sender identity, postal address and opt-out (AU Spam Act 2003, US CAN-SPAM, UK PECR, SG Spam Control Act).
- OSM / directory data: discovery stays polite (one request per site, delay, honest User-Agent). Google Maps and LinkedIn are not scraped.

## Status flow
`new > audited > qualified > draft_ready > approved > contacted > replied > call_booked > proposal_sent > won/lost` (or `skip`).

## Feedback loop
After every 25 contacted leads: compare reply rate by tier, niche, country and observation type (`report.py`), then move weight in `config/scoring.json` toward what actually produced replies and calls.

## Where it runs
- Cloud Claude session: ingest/score/draft (its network can't reach business websites).
- Laptop or GitHub Actions (`.github/workflows/weekly-leads.yml`, Mondays 06:00 MYT or manual "Run workflow"): full run incl. OSM discovery and audits. Optional repo secret `PSI_API_KEY` adds Google mobile speed scores.

## Skills
`.claude/skills/` holds 14 skills from [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) (MIT, reviewed 2026-10-20: markdown references plus client-side GTM snippets, no install hooks or network code). Commit pinned in `SOURCE-marketingskills.txt`.
