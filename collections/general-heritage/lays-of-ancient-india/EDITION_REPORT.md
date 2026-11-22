# Edition Verification & Run Audit — *Lays of Ancient India*

- **Book ID**: `lays-of-ancient-india` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 254 of 254 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `254` extracted, `12` blank/tissue, `0` failed (of `266` PDF leaves)
- **Tracked API Spend**: **`$3.7162`** (`3.9%` cached input tokens: `114,688` / `2,934,912` in, `224,502` out, `203,718` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 2.4% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 254 | `$3.7072` |
| `continuation_arbiter_batch` | 4 | `$0.0091` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 254 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`6` — catches smudged dates/figures in prose)**:
  - Leaf `13` `p0013-b0009`: VLM read `408` vs PDF OCR witness `['208']`
  - Leaf `18` `p0018-b0012`: VLM read `318` vs PDF OCR witness `['398']`
  - Leaf `31` `p0031-b0004`: VLM read `1000` vs PDF OCR witness `['1400']`
  - Leaf `31` `p0031-b0005`: VLM read `1000` vs PDF OCR witness `['1400']`
  - Leaf `36` `p0036-b0020`: VLM read `118` vs PDF OCR witness `['112']`
  - Leaf `37` `p0037-b0007`: VLM read `147` vs PDF OCR witness `['177', '197']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `5` prose joins, `1` split footnotes stitched, `1` multi-page tables unified, `88` total footnotes.
  - Stitched cross-page footnotes: p.53->p.54 (`†`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`24` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Bookplate: SEAL OF THE UNIVERSITY OF CALIFORNIA 1868 / LET THERE BE LIGHT / THE LIBRARY OF"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"Walter E Clark"*
  - Leaf `3` `p0003-b0003` (`noise`): *"—o0o—"*
  - Leaf `11` `p0011-b0027` (`noise`): *"A 2"*
  - Leaf `22` `p0022-b0019` (`noise`): *"2000—27/10/93."*
  - Leaf `27` `p0027-b0001` (`scanner_residue`): *"PK 2978 E5D95"*
  - Leaf `27` `p0027-b0003` (`scanner_residue`): *"2004773"*
  - Leaf `39` `p0039-b0004` (`noise`): *"A"*
  - Leaf `55` `p0055-b0009` (`noise`): *"B"*
  - Leaf `71` `p0071-b0010` (`noise`): *"C"*
  - Leaf `87` `p0087-b0010` (`noise`): *"D"*
  - Leaf `103` `p0103-b0007` (`noise`): *"E"*
- **Unattested Line-Wrap Hyphenation Decisions (`17` unique words out of `75` total wraps)**: `unobtainable` (p.4), `adulterated` (p.4), `Water-Shed` (p.7), `paraphrases` (p.11), `tolerable` (p.11), `Unpublished` (p.18), `Unpublished` (p.18), `confined` (p.31), `observer` (p.52), `precedes` (p.72), `kindred` (p.91), `supplying` (p.117), `Charlemagne` (p.131), `lexicographer` (p.141), `disturb` (p.167), `determination` (p.167), `Drauadî` (p.192)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 191,863 chars
- **Distinct Non-ASCII Glyphs (`18` across `156` leaves)**: Â Æ Î Ü á â æ é î ñ ó ö ú û ü Ā ā ṃ
- **Corrections Replayed**: `5` applied, `0` orphaned/unmatched
