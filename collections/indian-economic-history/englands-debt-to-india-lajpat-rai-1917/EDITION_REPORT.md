# Edition Verification & Run Audit — *England's Debt to India*

- **Book ID**: `englands-debt-to-india-lajpat-rai-1917` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`99.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 403 of 403 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `403` extracted, `5` blank/tissue, `0` failed (of `408` PDF leaves)
- **Tracked API Spend**: **`$1.5867`** (`72.3%` cached input tokens: `3,190,148` / `4,412,693` in, `518,494` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **24.0 / 25.0** | -1.0: 5 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Ready to ship as Community Edition! Human page-proof coverage is 0.0% (pages re-read 1.2%) toward Source-Certified.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 403 | `$1.3864` |
| `continuation_arbiter_batch` | 79 | `$0.1274` |
| `blind_totals_strip` | 18 | `$0.0729` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 403 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `211, 212`
- **450-DPI Blind Totals Strip Disagreements (`3`)**:
  - Leaf `134` `p0134-b0012`: full-page `['', '£6,080,172,021’']` vs blind-strip `['£6,080,172,021"']`
  - Leaf `315` `p0315-b0011`: full-page `['Average: less than 8%']` vs blind-strip `['188,145', '13,116']`
  - Leaf `346` `p0346-b0010`: full-page `['Total number pupils .....................................', '490,504']` vs blind-strip `['Total number institutions', '23,394']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`110` — catches smudged dates/figures in prose)**:
  - Leaf `23` `p0023-b0002`: VLM read `240,000,000` vs PDF OCR witness `['210000000']`
  - Leaf `38` `p0038-b0013`: VLM read `179` vs PDF OCR witness `['174', '175', '177']`
  - Leaf `38` `p0038-b0019`: VLM read `199` vs PDF OCR witness `['189']`
  - Leaf `40` `p0040-b0012`: VLM read `346` vs PDF OCR witness `['316', '341', '342']`
  - Leaf `40` `p0040-b0013`: VLM read `351` vs PDF OCR witness `['341', '357', '359']`
  - Leaf `87` `p0087-b0007`: VLM read `1710` vs PDF OCR witness `['1720']`
  - Leaf `117` `p0117-b0006`: VLM read `6,000,000` vs PDF OCR witness `['4000000']`
  - Leaf `120` `p0120-b0007`: VLM read `19,000,000` vs PDF OCR witness `['18000000']`
  - Leaf `131` `p0131-b0004`: VLM read `1860` vs PDF OCR witness `['1850']`
  - Leaf `136` `p0136-b0006`: VLM read `1913` vs PDF OCR witness `['1903', '1911']`
  - Leaf `138` `p0138-b0003`: VLM read `1900` vs PDF OCR witness `['1908', '1909', '1910']`
  - Leaf `138` `p0138-b0004`: VLM read `1913` vs PDF OCR witness `['1910', '1912']`
  - Leaf `146` `p0146-b0006`: VLM read `1878` vs PDF OCR witness `['1875']`
  - Leaf `146` `p0146-b0010`: VLM read `1810` vs PDF OCR witness `['1880']`
  - Leaf `146` `p0146-b0010`: VLM read `1860` vs PDF OCR witness `['1867', '1880']`
  - Leaf `146` `p0146-b0010`: VLM read `1860` vs PDF OCR witness `['1867', '1880']`
  - Leaf `150` `p0150-b0007`: VLM read `14,120` vs PDF OCR witness `['14121']`
  - Leaf `154` `p0154-b0004`: VLM read `1819` vs PDF OCR witness `['1879']`
  - Leaf `156` `p0156-b0004`: VLM read `1821` vs PDF OCR witness `['1824', '1831']`
  - Leaf `166` `p0166-b0005`: VLM read `1700` vs PDF OCR witness `['1708']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `266` prose joins, `3` split footnotes stitched, `12` multi-page tables unified, `173` total footnotes.
  - Stitched cross-page footnotes: p.184->p.185 (`8`), p.238->p.239 (`10`), p.313->p.314 (`6`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`21` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0003` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00290882 0"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Bookplate: 'EX LIBRIS' framed by foliate garland and open book motif, above books, inkwell"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"Handwritten pencil mark: 'R.'"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"(Proser"*
  - Leaf `3` `p0003-b0002` (`scanner_residue`): *"Digitized by the Internet Archive in 2007 with funding from Microsoft Corporation"*
  - Leaf `3` `p0003-b0003` (`scanner_residue`): *"http://www.archive.org/details/englandsdebttoin00lajpuoft"*
  - Leaf `6` `p0006-b0002` (`noise`): *"—"*
  - Leaf `6` `p0006-b0005` (`noise`): *"—"*
  - Leaf `6` `p0006-b0008` (`noise`): *"—"*
  - Leaf `6` `p0006-b0011` (`noise`): *"—"*
  - Leaf `7` `p0007-b0005` (`scanner_residue`): *"Faint oval library accession stamp."*
  - Leaf `8` `p0008-b0002` (`scanner_residue`): *"HC 435 L3"*
- **Unattested Line-Wrap Hyphenation Decisions (`190` unique words out of `2124` total wraps)**: `compilation` (p.12), `counsels` (p.14), `Theoretically` (p.16), `misstatements` (p.16), `announced` (p.20), `gratefully` (p.20), `advantageously` (p.20), `burdened` (p.21), `helping` (p.23), `burdening` (p.24), `challenge` (p.25), `stonehearted` (p.26), `courtesies` (p.27), `Edinburgh` (p.27), `frankness` (p.28), `behaviour` (p.28), `solicitations` (p.29), `marching` (p.29)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 475,667 chars
- **Distinct Non-ASCII Glyphs (`11` across `22` leaves)**: ¢ · æ é ô ü œ „ ⅓ ⅔ ⅙
- **Corrections Replayed**: `19` applied, `0` orphaned/unmatched
