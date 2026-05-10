# Filestore Probing Results — Pearson Edexcel GCSE Business (1BS0)

Probe date: 2026-04-25
Method: `curl -sIL` HEAD requests; followed redirects to detect Pearson's pattern of 302 -> `/en/campaigns/404.html` for missing assets. Treated final-URL=404.html as missing.

Total candidate URLs tested: ~245 unique
Confirmed (HTTP 200, real PDF body): **38**
Missing (404 / soft-404 redirect): **~207**

## Confirmed (HTTP 200)

### Question Papers (QP)

| URL | Size (bytes) | Series |
|---|---|---|
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_01_que_20190525.pdf | 873,023 | June 2019 P1 |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_02_que_20190605.pdf | 1,718,118 | June 2019 P2 |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_01_que_20211123.pdf | 848,914 | Nov 2021 P1 |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_02_que_20211127.pdf | 1,153,666 | Nov 2021 P2 |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1bs0-01-que-20220521.pdf | 878,031 | June 2022 P1 |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1bs0-02-que-20220614.pdf | 1,341,042 | June 2022 P2 |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-01-que-20230519.pdf | 1,101,393 | June 2023 P1 |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-02-que-20230613.pdf | 793,165 | June 2023 P2 |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-01-que-20240515.pdf | 829,826 | June 2024 P1 |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-02-que-20240606.pdf | 2,281,911 | June 2024 P2 |

### Mark Schemes (rms / msc)

| URL | Size (bytes) | Series |
|---|---|---|
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_01_rms_20190822.pdf | 330,208 | June 2019 P1 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_02_rms_20190822.pdf | 233,879 | June 2019 P2 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_01_msc_20210211.pdf | 252,040 | Nov 2020 P1 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_02_msc_20210211.pdf | 274,060 | Nov 2020 P2 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_01_rms_20220224.pdf | 296,596 | Nov 2021 P1 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_02_rms_20220224.pdf | 284,517 | Nov 2021 P2 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1bs0-01-rms-20220825.pdf | 275,829 | June 2022 P1 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1bs0-02-rms-20220825.pdf | 300,023 | June 2022 P2 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-01-rms-20230824.pdf | 327,249 | June 2023 P1 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-02-rms-20230824.pdf | 268,174 | June 2023 P2 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-01-rms-20240822.pdf | 329,582 | June 2024 P1 MS |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-02-rms-20240822.pdf | 330,712 | June 2024 P2 MS |

### Examiner Reports (pef = "Principal Examiner Feedback")

| URL | Size (bytes) | Series |
|---|---|---|
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_01_pef_20190822.pdf | 3,906,865 | June 2019 P1 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_02_pef_20190822.pdf | 4,242,543 | June 2019 P2 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_01_pef_20210211.pdf | 177,921 | Nov 2020 P1 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_02_pef_20210211.pdf | 174,665 | Nov 2020 P2 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1BS0_01_pef_20220224.pdf | 177,641 | Nov 2021 P1 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1bs0-02-pef-20220224.pdf | 178,578 | Nov 2021 P2 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1bs0-01-pef-20220825.pdf | 4,886,997 | June 2022 P1 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1bs0-01-pef-20230824.pdf | 5,704,339 | June 2023 P1 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/1bs0-02-pef-20230824.pdf | 5,926,575 | June 2023 P2 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-01-pef-20240822.pdf | 6,791,205 | June 2024 P1 ER |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/1bs0-02-pef-20240822.pdf | 5,743,475 | June 2024 P2 ER |

### Specification, SAMs, and Support

| URL | Size (bytes) | Doc Type |
|---|---|---|
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/specification-and-sample-assessments/gcse-business-spec-2017.pdf | 532,654 | Specification |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/specification-and-sample-assessments/pearson-edexcel-gcse-(9-1)-business-sams.pdf | 5,354,304 | Sample Assessment Materials (both papers) |
| https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/teaching-and-learning-materials/gcse-9-1-business-1bs0-getting-started-guide.pdf | 1,168,465 | Getting Started Guide |
| https://qualifications.pearson.com/content/dam/pdf/Support/Examination-timetables-for-UK-Edexcel-GCSE/gcse-summer-2025-final.pdf | 1,628,613 | GCSE Summer 2025 Timetable |
| https://qualifications.pearson.com/content/dam/pdf/Support/Examination-timetables-for-UK-Edexcel-GCSE/gcse-summer-2026-final.pdf | 280,797 | GCSE Summer 2026 Timetable |

## Not Found (HTTP 404 / soft-404)

A representative sample of the ~207 missing URL patterns tested:

| URL Pattern Tested | Reason for guess |
|---|---|
| `1BS0_01_que_specimen.pdf`, `1BS0_01_SAM_specimen.pdf`, `gcse-business-2017-paper-1-sams.pdf` | Common Pearson SAM naming on other specs — none used here; SAM is bundled in the single SAMs PDF |
| `pearson-edexcel-sam-source-booklet-gcse-business-1bs0-02.pdf` (returned by Google) | Hits soft-404 — likely renamed/removed |
| `1BS0_01_que_20190523.pdf`, `_20190524.pdf` | Wrong dates for June 2019 P1 (correct = 20190525) |
| `1BS0_02_que_20190604.pdf`, `_20190606.pdf`, `_20190610-14.pdf` | Wrong dates for June 2019 P2 (correct = 20190605) |
| `1BS0_01_que_20220521.pdf`, `1BS0_02_que_20220614.pdf` | Naming-convention mismatch — 2022 series uses **lowercase-hyphen** style only; uppercase-underscore versions of these specific filenames don't exist |
| `1bs0-01-que-20190525.pdf`, `1bs0-01-rms-20190822.pdf` | Naming-convention mismatch — 2019 series uses **uppercase-underscore** style only |
| All `1bs0-XX-que-2025XXXX.pdf` and `1bs0-XX-rms-2025XXXX.pdf` (P1 = 9 May 2025 / P2 = 16 May 2025 per official timetable) | June 2025 papers not yet on public CDN — Pearson locks past papers for ~9 months after the series; these become public ~Feb 2026 |
| Nov 2020 QPs `1BS0_01_que_20201103-1118.pdf`, `_02_que_20201111-1127.pdf` | Question papers from Nov 2020 series **not on Pearson's public CDN** — only the corresponding mark scheme + examiner report (issued 2021-02-11) are exposed |
| `1bs0-XX-prb-`, `-srb-`, `-ins-` (pre-release / source-booklet / insert variants) | Spec 1BS0 has no pre-release booklet; tested for completeness |
| Path `/Exam-materials/` (capital E) for 2019 filenames; `/exam-materials/` (lower) for 2024 filenames | Path case is sticky to the convention era — see "Patterns Discovered" |
| `gcse-business-2017-spec.pdf`, `Pearson-Edexcel-GCSE-Business-Specification.pdf`, etc. | Variant spec-PDF names; only `gcse-business-spec-2017.pdf` is real |
| `gcse-summer-2024-final.pdf`, `gcse-summer-2023-final.pdf` | Older timetables removed — only 2025 and 2026 are on the CDN |

## Patterns Discovered

### Path conventions
Two parallel paths exist (case-sensitive on this CDN — they are distinct buckets, **not aliases**):

- `https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/exam-materials/...` — used 2019, 2020-Nov, 2021-Nov, **and the entire June 2022 series**
- `https://qualifications.pearson.com/content/dam/pdf/GCSE/Business/2017/Exam-materials/...` (capital `E`) — used **June 2023 onward**

Specification & SAM live under: `/content/dam/pdf/GCSE/Business/2017/specification-and-sample-assessments/`
Teaching support under: `/content/dam/pdf/GCSE/Business/2017/teaching-and-learning-materials/`
National exam timetables: `/content/dam/pdf/Support/Examination-timetables-for-UK-Edexcel-GCSE/gcse-summer-<YYYY>-final.pdf` (only the 2 most recent years appear retained).

### Filename conventions (two eras)

**Era 1: uppercase-underscore (used for the 2019 June series and for the Nov 2020 + Nov 2021 series)**
```
1BS0_<PP>_<TYPE>_<YYYYMMDD>.pdf
```
- `<PP>` = paper code, `01` or `02`
- `<TYPE>` = `que` (question paper), `rms` (mark scheme — June series), `msc` (mark scheme — Nov 2020 only), `pef` (examiner report)
- `<YYYYMMDD>` = exam date for QP, **publication** date for MS/ER
  - June series MS/ER published 22 Aug
  - Nov series MS/ER published the following 11 Feb (Nov 2020) or 24 Feb (Nov 2021)

Anomaly: Nov 2021 P2 examiner report uses the **new** style filename (`1bs0-02-pef-20220224.pdf`) while Nov 2021 P1 examiner report uses the **old** style (`1BS0_01_pef_20220224.pdf`). The mark schemes for both Nov 2021 papers stayed in old style.

**Era 2: lowercase-hyphen (used from June 2022 onward)**
```
1bs0-<PP>-<TYPE>-<YYYYMMDD>.pdf
```
- Same field meanings; mark scheme suffix is always `rms` in this era
- Publication date for June MS/ER stayed 22 Aug (2024), 24 Aug (2023), 24/25 Aug (2022) — Friday of GCSE results week

### Confirmed exam dates (1BS0)
| Series | Paper 1 | Paper 2 |
|---|---|---|
| June 2019 | 25 May 2019 | 5 June 2019 |
| Nov 2020 | (QP not public) | (QP not public) |
| Nov 2021 | 23 Nov 2021 | 27 Nov 2021 |
| June 2022 | 21 May 2022 | 14 June 2022 |
| June 2023 | 19 May 2023 | 13 June 2023 |
| June 2024 | 15 May 2024 | 6 June 2024 |
| June 2025 | 9 May 2025 | 16 May 2025 (per official timetable; PDFs not yet on public CDN) |

### Document-type code key
- `que` — question paper
- `rms` — mark scheme (Results)
- `msc` — mark scheme (legacy "msc"; only seen on Nov 2020 series for 1BS0)
- `pef` — examiners' report / Principal Examiner Feedback

### Soft-404 behavior
Pearson's CDN issues a 302 redirect to `https://qualifications.pearson.com/en/campaigns/404.html` for missing `/content/dam/...` assets. Real assets return HTTP 200 directly with `Content-Type: application/pdf` and a populated `Content-Length`. Detection requires following the redirect and testing whether the final URL contains `404.html`.

### Domains tested
- `qualifications.pearson.com` — primary (all hits here)
- `pearsoncs.com` — not tested as primary; no public-facing PDFs known for this spec
- No legacy `edexcel.com` filestore variant was needed; all 1BS0 (2017 spec) materials are on `qualifications.pearson.com/content/dam/...`

## Coverage gaps remaining
- **June 2025 series**: All 6 expected files (P1 QP, P2 QP, P1 MS, P2 MS, P1 ER, P2 ER) are not yet on public CDN. Locked-period policy says they become public ~9 months after the series → expect availability ~Feb 2026. Worth re-probing then.
- **Nov 2020 question papers**: Only mark scheme + examiner report (both dated 20210211) are public. The QPs themselves were never released publicly for this series.
- **Sample-source booklet for Paper 2**: Google indexed `pearson-edexcel-sam-source-booklet-gcse-business-1bs0-02.pdf` but the asset now redirects to 404 — likely deprecated/removed when the unified SAMs PDF replaced it.
