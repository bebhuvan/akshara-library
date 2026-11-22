# Edition Verification & Run Audit — *The English Factories in India, 1665–1667*

- **Book ID**: `english-factories-india-1665-1667-vol-12` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`100.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 367 of 368 pages, gemini-3.6-flash on 1 of 368 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `368` extracted, `6` blank/tissue, `0` failed (of `374` PDF leaves)
- **Tracked API Spend**: **`$1.5993`** (`76.3%` cached input tokens: `2,913,088` / `3,819,776` in, `586,210` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Community Edition! Human page-proof coverage is 0.0% (pages re-read 1.6%) toward Source-Certified.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 365 | `$1.4711` |
| `recitation_retry` | 1 | `$0.0334` |
| `continuation_arbiter_batch` | 18 | `$0.0303` |
| `primary_quality_retry` | 2 | `$0.0257` |
| `secondary_gemini_rescue` | 1 | `$0.0126` |
| `recitation_band_top` | 1 | `$0.0098` |
| `blind_totals_strip` | 2 | `$0.0078` |
| `page_extract_batch_vetoed` | 2 | `$0.0075` |
| `page_extract_batch_failed` | 1 | `$0.0011` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 1 pp., `gemini-3.8-flash`: 367 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **450-DPI Blind Totals Strip Disagreements (`1`)**:
  - Leaf `86` `p0086-b0020`: full-page `['', '11,920', '2', '515']` vs blind-strip `['11,920', '2', '51 <sup>5</sup>']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`90` — catches smudged dates/figures in prose)**:
  - Leaf `24` `p0024-b0005`: VLM read `1663` vs PDF OCR witness `['1660', '1665']`
  - Leaf `30` `p0030-b0005`: VLM read `321` vs PDF OCR witness `['322', '323']`
  - Leaf `56` `p0056-b0007`: VLM read `101` vs PDF OCR witness `['100', '102']`
  - Leaf `70` `p0070-b0005`: VLM read `229,` vs PDF OCR witness `['259']`
  - Leaf `92` `p0092-b0003`: VLM read `100` vs PDF OCR witness `['200', '300']`
  - Leaf `139` `p0139-b0005`: VLM read `110` vs PDF OCR witness `['100']`
  - Leaf `145` `p0145-b0005`: VLM read `111` vs PDF OCR witness `['131']`
  - Leaf `150` `p0150-b0007`: VLM read `1,000` vs PDF OCR witness `['1500']`
  - Leaf `150` `p0150-b0008`: VLM read `1000` vs PDF OCR witness `['1500']`
  - Leaf `169` `p0169-b0004`: VLM read `110` vs PDF OCR witness `['100']`
  - Leaf `184` `p0184-b0003`: VLM read `100` vs PDF OCR witness `['170']`
  - Leaf `209` `p0209-b0005`: VLM read `211` vs PDF OCR witness `['214']`
  - Leaf `219` `p0219-b0003`: VLM read `5,000` vs PDF OCR witness `['1000']`
  - Leaf `277` `p0277-b0007`: VLM read `116` vs PDF OCR witness `['114']`
  - Leaf `284` `p0284-b0005`: VLM read `171` vs PDF OCR witness `['178']`
  - Leaf `288` `p0288-b0008`: VLM read `211` vs PDF OCR witness `['213']`
  - Leaf `295` `p0295-b0004`: VLM read `100` vs PDF OCR witness `['150']`
  - Leaf `298` `p0298-b0004`: VLM read `147` vs PDF OCR witness `['144', '148']`
  - Leaf `307` `p0307-b0007`: VLM read `110` vs PDF OCR witness `['100', '112']`
  - Leaf `314` `p0314-b0004`: VLM read `150` vs PDF OCR witness `['350']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `261` prose joins, `6` split footnotes stitched, `0` multi-page tables unified, `410` total footnotes.
  - Stitched cross-page footnotes: p.45->p.46 (`2`), p.134->p.135 (`4`), p.279->p.280 (`2`), p.298->p.299 (`2`), p.300->p.301 (`3`), p.320->p.321 (`2`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`77` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"22101437637"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2017 with funding from Wellcome Library"*
  - Leaf `5` `p0005-b0002` (`scanner_residue`): *"https://archive.org/details/b29352678_0002"*
  - Leaf `6` `p0006-b0002` (`scanner_residue`): *"HER MAJESTY'S STATE PAPER OFFICE"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"79156"*
  - Leaf `8` `p0008-b0002` (`scanner_residue`): *"WELLCOME LIBRARY INSTITUTE"*
  - Leaf `8` `p0008-b0003` (`scanner_residue`): *"O. Top. 125"*
  - Leaf `9` `p0009-b0004` (`noise`): *"A 2"*
  - Leaf `15` `p0015-b0008` (`noise`): *"2936"*
  - Leaf `15` `p0015-b0009` (`noise`): *"B"*
  - Leaf `17` `p0017-b0011` (`noise`): *"B 2"*
  - Leaf `31` `p0031-b0008` (`noise`): *"2936"*
- **Unattested Line-Wrap Hyphenation Decisions (`61` unique words out of `457` total wraps)**: `terminated` (p.10), `proselytizing` (p.12), `conveighing` (p.23), `disperse` (p.28), `stigmatized` (p.29), `uncerteyne` (p.32), `competition` (p.45), `Commandere` (p.47), `camphire` (p.48), `encorougement` (p.60), `instrumentall` (p.62), `mainteynance` (p.63), `dispatcher` (p.65), `abovementioned` (p.66), `accomplised` (p.67), `accomplisht` (p.78), `surface` (p.79), `independence` (p.94)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 713,623 chars, `han`: 4 chars, `hiragana`: 3 chars
- **Distinct Non-ASCII Glyphs (`29` across `207` leaves)**: · À à ã ç é ê ó û Ā ā ġ ģ ī ū ṇ ′ ⁄ ⅛ ⅜ ⅝ ⅞ し て を 使 描 用 笛
- **Corrections Replayed**: `20` applied, `0` orphaned/unmatched
