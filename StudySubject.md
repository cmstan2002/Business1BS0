# StudySubject - Reusable Course/Exam Archive & Revision Vault Builder

You are a lead engineer running a multi-agent project to build a **complete revision system** for a single course/class/subject/exam. This prompt is a reusable template - fill in the `<<VARIABLES>>` at the top and the agents will do the rest.

---

## CONFIGURE THIS SECTION FIRST

```
<<QUALIFICATION>>: GCSE
<<SUBJECT>>: Business
<<BOARD_OR_INSTITUTION>>: Edexcel
<<SPEC_OR_COURSE_CODE>>: 1BS0
<<OFFICIAL_WEBSITE>>: https://qualifications.pearson.com/en/qualifications/edexcel-gcses/business-2017.html
<<PAPER_STRUCTURE>>: 
  - Theme 1: Investigating small business (Exam Paper Code: 1BS0/01)
    Written examination: 1 hour and 45 minutes
    50% of the qualification
    90 marks
  - Theme 2: Building a business (Exam Paper Code: 1BS0/02)
    Written examination: 1 hour and 45 minutes
    50% of the qualification
    90 marks
<<FIRST_EXAM_YEAR>>: 2019
<<ARCHIVE_DIR>>: /Users/chris/STUDY/edexcel_gscs_business_1bs0_archive
<<VAULT_DIR>>: /Users/chris/Business1BS0
<<STUDENT_NAME>>: Nicole
```

---

## PROJECT STAGES

Work through these five stages, using parallel agents whenever possible. Each stage builds on the previous one.

---

## STAGE 1: Past Paper Archive

**Goal:** Build a complete local archive of every publicly available past exam paper, mark scheme, examiner report, insert, and pre-release booklet for `<<SPEC_OR_COURSE_CODE>>`.

### Create directory structure

```
<<ARCHIVE_DIR>>/
  /raw_downloads/
  /organized/
    /specimen/
    /<<FIRST_EXAM_YEAR>>/
    /.../
    /<current_year>/
  /catalog/
  /reports/
  /logs/
```

### Launch Discovery Agents in Parallel

Launch 3 parallel agents:

**Agent 1: Official Website Crawl**
Fetch the main spec page, assessment resources page, and teaching resources page at `<<OFFICIAL_WEBSITE>>`. Try filter parameter combinations (by year, by resource type). Use `num_ranks=200` or similar pagination parameters to get all results. Extract every PDF URL with its title and metadata.

**Agent 2: Web Search for PDFs**
Run web searches:
- `<<BOARD_OR_INSTITUTION>> <<SPEC_OR_COURSE_CODE>> <<SUBJECT>> past papers`
- `site:<<board-domain>> <<SPEC_OR_COURSE_CODE>> pdf`
- `site:<<board-domain>> <<SUBJECT>> mark scheme`
- `site:<<board-domain>> <<SUBJECT>> examiner report`
- `site:<<board-domain>> <<SUBJECT>> specimen`

Find any official PDFs not already on the main pages (filestore directories, archive URLs, etc.).

**Agent 3: Direct Filestore Probing**
For UK exam boards, construct and test URLs like:
- `https://filestore.<<board-domain>>/sample-papers-and-mark-schemes/<year>/june/AQA-<<paper-code>>-QP-JUN<YY>.PDF`
- Try each year from `<<FIRST_EXAM_YEAR>>` to current. 404 = confirmed unavailable.

### Download Phase

Consolidate all URLs found, then run a bulk download script (bash + curl) to pull every PDF into `/raw_downloads/`. Log successes, failures, and HTTP codes.

### Unofficial Source Fallback

For any missing years (commonly the earliest years - boards often remove old papers), launch additional agents to search unofficial sources:
- `physicsandmathstutor.com` (PMT) - extensive GCSE/A-Level archive
- `papacambridge.com` - for examiner reports
- `savemyexams.com`, `mmerevise.co.uk`, `revisionworld.com`
- `web.archive.org` (Wayback Machine) - for recently removed papers

Download any found PDFs to `/raw_downloads/`.

### Organize & Catalog

Write a Python script that:
1. Parses each filename to extract: year, series, paper number, document type, modified/accessibility version
2. Copies files to `/organized/<year>/` with normalized names: `<<BOARD>>-<<QUAL>>-<<SUBJ>>-<<CODE>>-<YEAR>-<SERIES>-<PAPER>-<DOCTYPE>.pdf`
3. Builds `catalog/files.csv` and `catalog/files.json` with full metadata per file (checksum, size, source URL, etc.)
4. Document types to normalize: QuestionPaper, MarkScheme, ExaminerReport, Insert, PreRelease, SpecimenQuestionPaper, SpecimenMarkScheme, OtherMaterial

### Reports

Generate:
- `reports/inventory_summary.md` - what was found, by year/type
- `reports/missing_items.md` - gaps with evidence of where they were searched
- `reports/source_pages.md` - all URLs crawled and what each contributed
- `logs/download_log.txt` - every HTTP request

---

## STAGE 2: Cross-Year Analysis

**Goal:** Read every question paper across all years and find patterns.

Launch **one agent per paper** in parallel. Each agent reads all question papers for its paper (using page-range reads for PDFs >10MB to avoid size limits).

For each paper, produce `reports/paperN_analysis.md` covering:

1. **Question structure consistency** - marks, timing, sections
2. **Topic rotation grid** - which topics appear each year (year × topic table)
3. **Guaranteed question types** - what appears in every single exam
4. **Unique/one-off questions** - things that only appeared once
5. **9-mark extended response topics** - what the big essay asks about each year
6. **Case study patterns** - recurring locations/examples
7. **Mark allocation patterns**
8. **Command word trends** - what verbs the exam uses
9. **Statistical/mathematical skills tested**
10. **Graphical skills tested**

Then write `reports/cross_paper_analysis.md` synthesising findings across all papers:
- The "Almost Certain" list (90%+ appearance rate)
- The "Likely" list (60-80%)
- The "Cyclical" list (every 2-3 years)

---

## STAGE 3: Obsidian Vault Setup

**Goal:** Build a complete revision vault at `<<VAULT_DIR>>`.

First, symlink the archive into the vault:
```
ln -s <<ARCHIVE_DIR>> <<VAULT_DIR>>/
```

### Launch 3 Parallel Agents

**Agent A: Topic Notes**
Create one note per major topic in `<<VAULT_DIR>>/Topics/Paper N/`. Each note must include:
- YAML frontmatter: paper, section, topic, priority (high/medium/low based on analysis), confidence (not-started), tags
- Summary of what the topic covers
- Key terms & definitions (8-15 per topic)
- Year-by-year exam appearance history (from the analysis reports)
- Substantive revision content (actual knowledge, not placeholders) - 40-80 lines
- Wiki links `[[Other Topic]]` to related topics, skills, and case studies
- "Practice Questions" section citing specific past paper questions by year

Also create `<<VAULT_DIR>>/Skills/` notes for each assessed skill:
- OS Map Skills / Lab Skills / Mathematical Skills (as appropriate for subject)
- Graph/Chart Skills
- Statistical Skills
- Command Words (with mark expectations)

**Agent B: Dashboard & Trackers**
Create:
1. `<<VAULT_DIR>>/Dashboard.md` - homepage with:
   - Quick links to each paper's topics
   - Exam structure table (marks/timing per paper)
   - Priority Topics section (from analysis)
   - Revision Progress section with checkboxes
   - Obsidian callout blocks (`> [!tip]`, `> [!warning]`)
   - Links to analysis reports in the archive
2. `<<VAULT_DIR>>/Practice/Past Paper Tracker.md` - tracking table for every paper:
   - Year | Paper | Attempted | Score | % | Weak Areas | Link to PDF
   - Rows for every year from specimen to most recent
3. `<<VAULT_DIR>>/Strategy/Exam Strategy.md` covering:
   - Time management per paper (1 mark ≈ 1 minute rule)
   - How to structure 6-mark questions (e.g. PEEL)
   - How to structure 9-mark questions (intro + PEEL paragraphs + conclusion)
   - SPaG tips
   - Common mistakes to avoid
   - The "Almost Certain" topics list
4. `<<VAULT_DIR>>/Case Studies/Index.md` - every required case study organised by paper with what the exam typically asks
5. `<<VAULT_DIR>>/Practice/Revision Checklist.md` - every spec topic broken into 3-5 checkboxed subtopics
6. Delete the default `Welcome.md` if present

**Agent C: Flashcards & Canvas**

Create spaced repetition flashcards in `<<VAULT_DIR>>/Flashcards/` using standard Obsidian SR format (works with the Spaced Repetition community plugin):
```
Question
?
Answer

Next Question
?
Next Answer
```

Create these files:
- `Paper N - Key Terms.md` (~40 cards per paper on definitions/concepts)
- `Case Studies.md` (~20 cards testing case study recall)
- `Command Words.md` (~15 cards - each command word + mark expectation)

Also create `<<VAULT_DIR>>/Revision Map.canvas` - an Obsidian canvas (JSON format) with:
- Top-level nodes for each paper (color-coded)
- Section nodes branching out
- Topic nodes under each section
- Edges connecting the hierarchy

Canvas JSON structure:
```json
{
  "nodes": [
    {"id": "p1", "type": "text", "text": "# Paper 1\n...", "x": 0, "y": 0, "width": 300, "height": 120, "color": "1"}
  ],
  "edges": [
    {"id": "e1", "fromNode": "p1", "toNode": "p1a", "fromSide": "bottom", "toSide": "top"}
  ]
}
```

Colors: 1=red, 4=green, 6=purple (use different colors per paper for visual distinction).

---

## STAGE 4 (Optional): Physical Flashcards

If physical flashcards are wanted, the user has a tool at `/Users/chris/flashcards/` that converts markdown flashcards into print-ready duplex-printable A4 PDFs. Usage:

```bash
cd /Users/chris/flashcards
source venv/bin/activate
python make_flashcards.py --input <<VAULT_DIR>>/Flashcards/Paper\ 1\ -\ Key\ Terms.md --output physical_flashcards_p1.pdf
```

The tool expects this markdown format (different from Obsidian SR plugin):
```
# Topic Name
## Card
Term: The concept
Definition: The explanation
```

Convert Obsidian SR flashcards to this format before using.

---

## STAGE 5: Final Summary

Report back to the user with:

1. **Archive stats:** total files, size, years covered
2. **Known gaps:** what couldn't be found and why
3. **Analysis highlights:** the "Almost Certain" list for this exam
4. **Vault structure:** file counts per folder
5. **How to open in Obsidian:** set Dashboard.md as homepage, install Spaced Repetition plugin
6. **Quick start for revision:** suggested 4-week revision plan based on priority topics

---

## EXECUTION PRINCIPLES

- **Parallelise aggressively** - launch multiple agents at once when their work is independent
- **Be thorough with gaps** - if official sources don't have something, try unofficial sources and document the search
- **Use the analysis to drive priorities** - don't waste time on equal-weighted revision when the data shows tectonic hazards appear 6/9 years but fracking appeared once
- **Keep filenames consistent** - normalized naming scheme makes everything cross-referenceable
- **Substantive content, not placeholders** - topic notes must contain real revision material
- **Wiki-link liberally** - the power of Obsidian is the graph; every note should link to 5+ other notes
- **Don't ask questions unless essential** - make reasonable decisions and keep going

---

## KNOWN PITFALLS

1. **Large PDF files (>10MB)** - Use page-range parameter on Read tool: `pages="1-10"` then `pages="11-20"`. Fails silently without this.
2. **AQA's two hosting systems** - Older files on `filestore.aqa.org.uk`, newer on `cdn.sanity.io`. Check both.
3. **COVID years (2020-2022)** - Exam papers may have reduced marks, changed structure. Note this in analysis.
4. **First-year papers often removed** - Early spec years (year 1-2 of a spec) are frequently withdrawn from official sites. Check unofficial sources.
5. **Modified accessibility versions** - Papers often have A4 18pt and A3 36pt variants. Include but mark clearly.
6. **Pre-release vs preliminary material** - Same thing, naming changed around 2024.

---

## DELIVERABLES CHECKLIST

- [ ] Complete archive at `<<ARCHIVE_DIR>>` with organized/, catalog/, reports/, logs/
- [ ] `catalog/files.csv` and `catalog/files.json` with full metadata
- [ ] `reports/inventory_summary.md`, `missing_items.md`, `source_pages.md`
- [ ] `reports/paper1_analysis.md`, `paper2_analysis.md`, etc. (one per paper)
- [ ] `reports/cross_paper_analysis.md` (synthesis)
- [ ] Obsidian vault at `<<VAULT_DIR>>` with symlink to archive
- [ ] `Dashboard.md` (vault homepage)
- [ ] `Topics/Paper N/*.md` (topic notes with wiki-links)
- [ ] `Skills/*.md` (OS map, graphs, stats, command words)
- [ ] `Flashcards/*.md` (SR-plugin-ready cards)
- [ ] `Practice/Past Paper Tracker.md`, `Revision Checklist.md`
- [ ] `Strategy/Exam Strategy.md`
- [ ] `Case Studies/Index.md`
- [ ] `Revision Map.canvas`
- [ ] Final summary to user with stats, gaps, and revision plan
