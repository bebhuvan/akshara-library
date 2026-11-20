# Edition Verification & Run Audit — *The Economic Life of a Bengal District*

- **Book ID**: `economic-life-bengal-district-faridpur-1916` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 162 of 162 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `162` extracted, `6` blank/tissue, `0` failed (of `168` PDF leaves)
- **Tracked API Spend**: **`$0.5716`** (`74.0%` cached input tokens: `1,284,906` / `1,737,413` in, `179,203` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 4.3% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 162 | `$0.5096` |
| `blind_totals_strip` | 9 | `$0.0355` |
| `continuation_arbiter_batch` | 16 | `$0.0266` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 162 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `28, 29, 124, 155, 156, 157, 158, 160, 161`
- **450-DPI Blind Totals Strip Disagreements (`5`)**:
  - Leaf `123` `p0123-b0012`: full-page `['Total       „', '15¼   „     „', '8¾    „     „']` vs blind-strip `['Local', ',,', '.', '.', '.', '6¾', ',,', ',,', '4', ',,', ',,']`
  - Leaf `155` `p0155-b0011`: full-page `['Total', '342,108', '1,861,183', '96,378,355\n(£6,425,223)', '256,681', '1,429,630', '71,326,876\n(£4,755,125)', '85,427', '431,553', '25,051,479\n(£1,670,098)']` vs blind-strip `['<unclear>6 16</unclear>', '841 167', '237 58', '928 901 12', '819 837 1', '189 918', '118 840 98', '281 198 1']`
  - Leaf `156` `p0156-b0010`: full-page `['Total', '215,733', '1,164,824', '58,511,452', '194,975', '1,067,835', '53,785,210', '20,758', '96,989', '4,726,242']` vs blind-strip `['Total']`
  - Leaf `157` `p0157-b0010`: full-page `['Total', '699', '4,391', '208,336', '608', '3,871', '185,105', '91', '520', '23,231']` vs blind-strip `['January', '2,010']`
  - Leaf `158` `p0158-b0012`: full-page `['Average of all\nclasses', '282', '18 16', '52', '69', '50', '67', '58', '77', '50', '49', '49', '61', '48', '45']` vs blind-strip `['41\n33', '43\n31', '43\n33', '38\n30']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`6` — catches smudged dates/figures in prose)**:
  - Leaf `16` `p0016-b0004`: VLM read `151` vs PDF OCR witness `['153', '154', '155']`
  - Leaf `119` `p0119-b0004`: VLM read `4,000` vs PDF OCR witness `['8000']`
  - Leaf `154` `p0154-b0014`: VLM read `115` vs PDF OCR witness `['105']`
  - Leaf `154` `p0154-b0024`: VLM read `101` vs PDF OCR witness `['103', '104', '105']`
  - Leaf `157` `p0157-b0007`: VLM read `157` vs PDF OCR witness `['153']`
  - Leaf `158` `p0158-b0013`: VLM read `104` vs PDF OCR witness `['154']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `96` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `2` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`38` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00116145 4"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2007 with funding from Microsoft Corporation"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"http://www.archive.org/details/economiclifeofbe00jackuoft"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"HIn J127e"*
  - Leaf `7` `p0007-b0007` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY embossed blind stamp"*
  - Leaf `7` `p0007-b0008` (`scanner_residue`): *"144033 23/10/17."*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed library stamp: UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `16` `p0016-b0012` (`noise`): *"————"*
  - Leaf `21` `p0021-b0005` (`noise`): *"1908"*
  - Leaf `21` `p0021-b0006` (`noise`): *"B"*
  - Leaf `23` `p0023-b0005` (`noise`): *"B 2"*
  - Leaf `23` `p0023-b0006` (`scanner_residue`): *"pencil mark"*
- **Unattested Line-Wrap Hyphenation Decisions (`36` unique words out of `330` total wraps)**: `comprehension` (p.12), `safeguard` (p.12), `analyse` (p.18), `Brahmaputra` (p.18), `constructive` (p.20), `concrete` (p.27), `waterjugs` (p.40), `innumerable` (p.47), `contrivances` (p.47), `grasshoppers` (p.47), `domeshaped` (p.48), `watermanship` (p.49), `autocrat` (p.53), `fomenting` (p.57), `oilcake` (p.67), `sumptuously` (p.69), `compelled` (p.69), `management` (p.82)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 196,283 chars
- **Distinct Non-ASCII Glyphs (`7` across `13` leaves)**: · ā ī „ ⁄ ⅓ ⅔
- **Corrections Replayed**: `32` applied, `0` orphaned/unmatched
