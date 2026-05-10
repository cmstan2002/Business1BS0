# Missing Items — Edexcel GCSE Business (1BS0) Archive

## Confirmed gaps

### June 2025 series — embargoed
- 1BS0/01 question paper (exam date 9 May 2025)
- 1BS0/02 question paper (exam date 16 May 2025)
- Both mark schemes (would publish ~21 Aug 2025 per pattern)
- Both examiner reports

**Why missing:** Pearson locks past papers behind centre login for ~9 months after the series. Probed all expected URLs (`1bs0-01-que-20250509.pdf`, `1bs0-01-rms-20250821.pdf`, etc.) — all return Pearson's soft-404. Free public release expected ~Feb 2026, but as of 25 April 2026 still not on the public CDN. Worth re-probing.

**Workarounds tested:** Available behind paywalls on Stuvia, Docsity, Scribd. Not downloaded automatically — would need a paid account.

### Summer 2020 series — never existed
- COVID-19 cancelled all summer 2020 GCSE exams in the UK. There is no June 2020 1BS0 paper to find. Pearson released the Nov 2020 series as a replacement instead.

### Summer 2021 series — never existed
- COVID-19 also cancelled summer 2021 exams. Teacher-Assessed Grades were used. Pearson released the **Nov 2021** series + a **2021 "new format" practice paper** for Paper 1 (downloaded — `Edexcel-GCSE-Business-1BS0-2021NewFormatPracticePaper-Paper01.pdf`). No equivalent Paper 2 practice paper exists.

### Nov 2020 examiner report for Paper 2 — confirmed downloaded
The 2020-Nov P2 examiner report URL `1BS0_02_pef_20210211.pdf` was unverified by Agent 2 but confirmed live by Agent 3. Downloaded successfully.

## Soft-404 URL guesses that did not exist

These URLs were guessed by Agent 1 but returned Pearson's HTML soft-404 page (152 KB):
- `GCSE Business SAMs_WEB.pdf` — duplicate of the main SAMs PDF; the main one is in archive
- `pearson-edexcel-sam-source-booklet-gcse-business-1bs0-01.pdf` — never existed; SAMs source material is bundled inside the unified SAMs PDF
- `pearson-edexcel-sam-source-booklet-gcse-business-1bs0-02.pdf` — same

## Resource types that don't exist for this spec
- **Pre-release / research booklet** — that's an A-Level 9BS0 feature only. GCSE 1BS0 has no advance materials.
- **Inserts** — the Paper 2 case study is bound into the question paper itself, not a separate insert booklet (until at least 2024).
- **Modified accessibility versions (A4 18pt / A3 36pt)** — not exposed publicly on Pearson's CDN for 1BS0; centres request these directly through their exams office.

## Search trail (for re-verification)
- ~245 candidate URLs probed against Pearson CDN by Agent 3
- Web searches across `qualifications.pearson.com`, `revisionworld.com`, `physicsandmathstutor.com`, `savemyexams.com`, `papersroom.com`, `myexampapers.uk`, `web.archive.org`, `papacambridge.com`, `kingsbridgeeducation.co.uk`, `studocu.com`, `stuvia.com`, `scribd.com`, `docsity.com`
- Detailed log in `logs/agent1_pearson_official.md`, `logs/agent2_web_search.md`, `logs/agent3_filestore_probing.md`
