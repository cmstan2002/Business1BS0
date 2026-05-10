# Source Pages — All URLs Crawled and What Each Contributed

## Pearson official (qualifications.pearson.com)
| URL pattern | Purpose | Yield |
|---|---|---|
| `/en/qualifications/edexcel-gcses/business-2017.html` | Main spec landing page | Spec PDF, subject guide, switching guide |
| `/en/qualifications/edexcel-gcses/business-2017.coursematerials.html` | Course materials (Angular SPA — needs Google site: queries to enumerate) | All 36 exam PDFs (via filename guessing once pattern was known) |
| `/en/qualifications/edexcel-gcses/business-2017/teaching-and-learning-materials.html` | Teaching support index | 15 teaching PDFs (case studies, model answers, exemplars) |
| `/content/dam/pdf/GCSE/Business/2017/exam-materials/` | Direct CDN bucket — used 2019, Nov 2020, Nov 2021, June 2022 | 24 exam PDFs |
| `/content/dam/pdf/GCSE/Business/2017/Exam-materials/` (capital E) | Direct CDN bucket — used June 2023 onward | 12 exam PDFs |
| `/content/dam/pdf/GCSE/Business/2017/specification-and-sample-assessments/` | Spec + SAMs | 2 PDFs (spec + main SAMs) |
| `/content/dam/pdf/GCSE/Business/2017/teaching-and-learning-materials/` | Teaching support PDFs | 15 PDFs |
| `/content/dam/pdf/Support/Grade-boundaries/GCSE/` | Grade boundaries | 4 PDFs (June+Nov 2024, June 2025 + notional) |
| `/content/dam/pdf/Support/Examination-timetables-for-UK-Edexcel-GCSE/` | Exam timetables | 2 PDFs (Summer 2025, Summer 2026) |

## Unofficial mirrors (used as fallback)
| Site | Used for | Yield |
|---|---|---|
| `revisionworld.com` | Nov 2020 question papers (not on Pearson CDN) | 2 PDFs |
| `businessbuddyonline.weebly.com` | Specimen Set 2 Paper 1 QP, Paper 2 MS | 2 PDFs |
| `gcsecs.com` | Specimen Set 2 Paper 1 MS, Specimen Set 1 Paper 2 MS | 2 PDFs |

## Search engines / aggregator pages consulted (no direct PDFs but informed URL guessing)
- `google.com` site: searches against `qualifications.pearson.com` for spec code `1BS0` + each year/series
- `savemyexams.com/gcse/business/edexcel/past-papers/` — index page
- `physicsandmathstutor.com/gcses/` — checked, no 1BS0 specific archive (PMT focuses more on STEM)
- `papersroom.com/gcse/gcse-edexcel/gcse-business-past-papers/` — index page
- `myexampapers.uk/past-papers/gcse/edexcel/business/` — index page
- `web.archive.org` — no useful 1BS0 snapshots (Pearson URLs are still live)
- `kingsbridgeeducation.co.uk` — curated 2020-2025 list (used for cross-checking)

## Filestore URL pattern (for future archive refresh)
**Era 1 (2019, Nov 2020, Nov 2021, June 2022):**
`https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_<PP>_<TYPE>_<YYYYMMDD>.pdf`

**Era 2 (June 2023 onward):**
`https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-<PP>-<TYPE>-<YYYYMMDD>.pdf`

Where:
- `<PP>` = `01` or `02`
- `<TYPE>` = `que` (question paper), `rms` (mark scheme, June series), `msc` (mark scheme, Nov 2020 only), `pef` (examiner report)
- `<YYYYMMDD>` = exam date for `que`; results-week Friday for June MS/ER; following Feb for Nov MS/ER
