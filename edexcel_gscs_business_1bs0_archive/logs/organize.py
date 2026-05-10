#!/usr/bin/env python3
"""Organize downloaded 1BS0 PDFs into /organized/<year>/ with normalized names + build catalog."""
import csv
import hashlib
import json
import re
import shutil
from pathlib import Path

ARCHIVE = Path("/Users/chris/STUDY/edexcel_gscs_business_1bs0_archive")
RAW = ARCHIVE / "raw_downloads"
ORGANIZED = ARCHIVE / "organized"
CATALOG = ARCHIVE / "catalog"
CATALOG.mkdir(exist_ok=True)

# Map raw filename -> (year_dir, series, paper, doctype, normalized_name)
DOCTYPE_FROM_CODE = {"que": "QuestionPaper", "rms": "MarkScheme", "msc": "MarkScheme", "pef": "ExaminerReport"}
DATE_TO_SERIES = {
    "20190525": ("2019", "June2019", "01"),
    "20190605": ("2019", "June2019", "02"),
    "20190822": ("2019", "June2019", None),  # MS/ER, paper inferred from filename
    "20201110": ("2020", "Nov2020", "01"),
    "20201117": ("2020", "Nov2020", "02"),
    "20210211": ("2020", "Nov2020", None),
    "20211123": ("2021", "Nov2021", "01"),
    "20211127": ("2021", "Nov2021", "02"),
    "20220224": ("2021", "Nov2021", None),
    "20220521": ("2022", "June2022", "01"),
    "20220614": ("2022", "June2022", "02"),
    "20220825": ("2022", "June2022", None),
    "20230519": ("2023", "June2023", "01"),
    "20230613": ("2023", "June2023", "02"),
    "20230824": ("2023", "June2023", None),
    "20240515": ("2024", "June2024", "01"),
    "20240606": ("2024", "June2024", "02"),
    "20240822": ("2024", "June2024", None),
}

EXAM_RE = re.compile(r"1bs0[_-](\d{2})[_-](que|rms|msc|pef)[_-](\d{8})\.pdf$", re.IGNORECASE)

records = []
for raw in sorted(RAW.glob("*.pdf")):
    name = raw.name
    sha = hashlib.sha256(raw.read_bytes()).hexdigest()[:16]
    size = raw.stat().st_size

    year_dir, series, paper, doctype, normalized = None, None, None, None, None

    # Exam materials
    m = EXAM_RE.search(name)
    if m:
        paper = m.group(1).zfill(2)
        code = m.group(2).lower()
        date = m.group(3)
        doctype = DOCTYPE_FROM_CODE[code]
        info = DATE_TO_SERIES.get(date)
        if info:
            year_dir, series, _ = info
            normalized = f"Edexcel-GCSE-Business-1BS0-{series}-Paper{paper}-{doctype}.pdf"

    # Specimen Set 2
    elif "specimen_papers_set_2" in name.lower():
        year_dir, series = "specimen", "SpecimenSet2"
        if "paper_1" in name.lower() or "paper-1" in name.lower():
            paper = "01"
        elif "paper_2" in name.lower() or "paper-2" in name.lower():
            paper = "02"
        if "question" in name.lower():
            doctype = "SpecimenQuestionPaper"
        elif "mark_scheme" in name.lower() or "mark-scheme" in name.lower():
            doctype = "SpecimenMarkScheme"
        if paper and doctype:
            normalized = f"Edexcel-GCSE-Business-1BS0-SpecimenSet2-Paper{paper}-{doctype}.pdf"

    # Specimen Set 1 paper 2 mark scheme
    elif "specimen_1_paper_2_mark_scheme" in name.lower():
        year_dir, series, paper, doctype = "specimen", "SpecimenSet1", "02", "SpecimenMarkScheme"
        normalized = f"Edexcel-GCSE-Business-1BS0-SpecimenSet1-Paper02-{doctype}.pdf"

    # Specification & main SAMs
    elif name == "gcse-business-spec-2017.pdf":
        year_dir, series, doctype = "specimen", "Specification", "Specification"
        normalized = "Edexcel-GCSE-Business-1BS0-Specification.pdf"
    elif "business-sams" in name.lower() or "business_sams" in name.lower():
        year_dir, series, doctype = "specimen", "SpecimenSet1", "SpecimenQuestionPaper"
        normalized = "Edexcel-GCSE-Business-1BS0-SpecimenSet1-SAMs-Combined.pdf"

    # Teaching/learning materials
    elif name.startswith("gcse-business-studies-paper-"):
        m2 = re.match(r"gcse-business-studies-paper-(\d)-case-study-(\d)\.pdf", name)
        if m2:
            paper = m2.group(1).zfill(2)
            cs = m2.group(2)
            year_dir, series, doctype = "teaching", "PracticeCaseStudy", "OtherMaterial"
            normalized = f"Edexcel-GCSE-Business-1BS0-PracticeCaseStudy-Paper{paper}-CS{cs}.pdf"
    elif "newformat" in name.lower():
        year_dir, series, paper, doctype = "teaching", "PracticePaper", "01", "OtherMaterial"
        normalized = "Edexcel-GCSE-Business-1BS0-2021NewFormatPracticePaper-Paper01.pdf"
    elif "9-mark_modelanswers" in name or "9-mark-modelanswers" in name:
        year_dir, series, doctype = "teaching", "ModelAnswers", "OtherMaterial"
        normalized = "Edexcel-GCSE-Business-1BS0-9MarkModelAnswers.pdf"
    elif "exemplars" in name.lower():
        year_dir, series, doctype = "teaching", "Exemplars", "OtherMaterial"
        normalized = "Edexcel-GCSE-Business-1BS0-Exemplars.pdf"
    elif "getting-started" in name.lower():
        year_dir, series, doctype = "teaching", "GettingStarted", "OtherMaterial"
        normalized = "Edexcel-GCSE-Business-1BS0-GettingStartedGuide.pdf"
    elif "subject_guide" in name.lower():
        year_dir, series, doctype = "teaching", "SubjectGuide", "OtherMaterial"
        normalized = "Edexcel-GCSE-Business-1BS0-SubjectGuide.pdf"
    elif "switching-guide" in name.lower():
        year_dir, series, doctype = "teaching", "SwitchingGuide", "OtherMaterial"
        normalized = "Edexcel-GCSE-Business-1BS0-SwitchingGuide.pdf"
    elif "resource-bank" in name.lower():
        year_dir, series, doctype = "teaching", "ResourceBank", "OtherMaterial"
        normalized = "Edexcel-GCSE-Business-1BS0-ResourceBank-22-23.pdf"
    elif "booklet-guidance" in name.lower():
        year_dir, series, doctype = "teaching", "BookletGuidance", "OtherMaterial"
        normalized = "Edexcel-GCSE-Business-1BS0-BookletGuidance.pdf"
    elif "resource-map" in name.lower():
        year_dir, series, doctype = "teaching", "ResourceMap", "OtherMaterial"
        normalized = "Edexcel-GCSE-Business-1BS0-ResourceMap.pdf"

    # Grade boundaries / timetables
    elif "grade-boundaries" in name.lower():
        year_dir, series, doctype = "support", "GradeBoundaries", "OtherMaterial"
        normalized = f"Edexcel-GCSE-{name}"
    elif "gcse-summer-" in name.lower():
        year_dir, series, doctype = "support", "Timetable", "OtherMaterial"
        normalized = f"Edexcel-{name}"

    if not year_dir or not normalized:
        print(f"WARN: could not classify {name}")
        continue

    out_dir = ORGANIZED / year_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / normalized
    shutil.copy2(raw, dest)

    records.append({
        "raw_filename": name,
        "organized_path": str(dest.relative_to(ARCHIVE)),
        "year_dir": year_dir,
        "series": series,
        "paper": paper or "",
        "doctype": doctype,
        "size_bytes": size,
        "sha256_16": sha,
    })

# Write catalog files
csv_path = CATALOG / "files.csv"
with csv_path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(records[0].keys()))
    writer.writeheader()
    writer.writerows(records)

json_path = CATALOG / "files.json"
json_path.write_text(json.dumps(records, indent=2))

print(f"\nCataloged {len(records)} files.")
print(f"  CSV:  {csv_path}")
print(f"  JSON: {json_path}")
print(f"\nBy year_dir:")
from collections import Counter
for k, v in Counter(r["year_dir"] for r in records).most_common():
    print(f"  {k}: {v}")
print(f"\nBy doctype:")
for k, v in Counter(r["doctype"] for r in records).most_common():
    print(f"  {k}: {v}")
