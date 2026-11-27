# Edition Verification & Run Audit — *Life in an Indian Village*

- **Book ID**: `life-in-an-indian-village` | **Run ID**: `g38-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 215 of 215 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `215` extracted, `13` blank/tissue, `0` failed (of `228` PDF leaves)
- **Tracked API Spend**: **`$0.5669`** (`77.3%` cached input tokens: `1,727,784` / `2,234,287` in, `165,164` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 1.9% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 214 | `$0.5431` |
| `continuation_arbiter_batch` | 14 | `$0.0163` |
| `primary_quality_retry` | 1 | `$0.0049` |
| `page_extract_batch_vetoed` | 1 | `$0.0026` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 215 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`1` — catches smudged dates/figures in prose)**:
  - Leaf `15` `p0015-b0008`: VLM read `200` vs PDF OCR witness `['100']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `110` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `5` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`27` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UC-NRLF B 4 299 511"*
  - Leaf `11` `p0011-b0008` (`scanner_residue`): *"OXFORD UNIVERSITY"*
  - Leaf `12` `p0012-b0001` (`scanner_residue`): *"-Ⅲ-S"*
  - Leaf `12` `p0012-b0002` (`scanner_residue`): *"D500 428 R159"*
  - Leaf `12` `p0012-b0003` (`scanner_residue`): *"A-879462"*
  - Leaf `12` `p0012-b0004` (`scanner_residue`): *"Repl 559297"*
  - Leaf `12` `p0012-b0005` (`scanner_residue`): *"Reproduced by DUOPAGE process in the United States of America"*
  - Leaf `12` `p0012-b0006` (`scanner_residue`): *"MICRO PHOTO INC. Cleveland 12, Ohio"*
  - Leaf `13` `p0013-b0001` (`scanner_residue`): *"DS421 R3"*
  - Leaf `13` `p0013-b0003` (`noise`): *"————"*
  - Leaf `13` `p0013-b0012` (`scanner_residue`): *"389"*
  - Leaf `17` `p0017-b0002` (`noise`): *"——♦——"*
- **Unattested Line-Wrap Hyphenation Decisions (`70` unique words out of `302` total wraps)**: `fictitious` (p.19), `governmental` (p.26), `polluted` (p.28), `contentions` (p.31), `inhabiting` (p.36), `conspicuous` (p.37), `existence` (p.39), `Thondamandalam` (p.39), `subdivision` (p.41), `gatherings` (p.42), `broadchested` (p.44), `stumblingblock` (p.45), `representations` (p.47), `compound` (p.54), `degenerated` (p.60), `prescribing` (p.61), `Jivarakshamritham` (p.64), `grazing` (p.67)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 181,055 chars
- **Distinct Non-ASCII Glyphs (`9` across `79` leaves)**: Á É á è é ó ú ü ā
- **Corrections Replayed**: `6` applied, `0` orphaned/unmatched
