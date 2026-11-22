# Edition Verification & Run Audit — *The Imperial Gazetteer of India: The Indian Empire, Vol. IV — Administrative*

- **Book ID**: `imperial-gazetteer-of-india-vol-04-administrative` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`88.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 584 of 586 pages, gemini-3.6-flash on 2 of 586 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `586` extracted, `8` blank/tissue, `0` failed (of `594` PDF leaves)
- **Tracked API Spend**: **`$3.0384`** (`73.2%` cached input tokens: `4,866,239` / `6,646,414` in, `1,062,304` out, `2,612` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **13.0 / 25.0** | -12.0: 3 column total arithmetic mismatch(es) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 561 | `$2.3904` |
| `recitation_retry` | 10 | `$0.1423` |
| `primary_quality_retry` | 16 | `$0.1392` |
| `continuation_arbiter_batch` | 60 | `$0.1166` |
| `blind_totals_strip_batch` | 36 | `$0.0738` |
| `page_extract_batch_vetoed` | 15 | `$0.0630` |
| `recitation_band_top` | 6 | `$0.0466` |
| `recitation_band_bot` | 5 | `$0.0392` |
| `secondary_gemini_rescue` | 2 | `$0.0160` |
| `page_extract_batch_failed` | 10 | `$0.0113` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 2 pp., `gemini-3.8-flash`: 584 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 238, 418, 419, 444`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `102` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `319` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `565` via `recitation_2band_split` (`gemini-3.6-flash`)
  - Leaf `576` via `recitation_2band_split` (`gemini-3.8-flash`)
- **450-DPI Blind Totals Strip Disagreements (`8`)**:
  - Leaf `131` `p0131-b0018`: full-page `['TOTAL', '77,395', '8,510,317', '4,21', '', '', '']` vs blind-strip `['', 'Approxi-']`
  - Leaf `133` `p0133-b0013`: full-page `['TOTAL', '128,918', '9,841,765', '3,20', '', '', '']` vs blind-strip `['8,918', '9,841,765', '3,20']`
  - Leaf `134` `p0134-b0007`: full-page `['Total', '78,034', '428,640', '10', '', '', '']` vs blind-strip `['10']`
  - Leaf `137` `p0137-b0008`: full-page `['TOTAL', '5,079', '802,097', '36', '', '', '']` vs blind-strip `['Salute of Ruler in guns.']`
  - Leaf `139` `p0139-b0015`: full-page `['TOTAL (approximate)', '67,011', '1,177,987', '13 1/2', '', '', '']` vs blind-strip `['986', '184,799 Buddhists 2', 'Szechwan Shan · Buddhist', '', '6']`
  - Leaf `140` `p0140-b0013`: full-page `['TOTAL', '29,435', '1,996,383', '21']` vs blind-strip `['']`
  - Leaf `141` `p0141-b0008`: full-page `['Grand Total (approximate)', '824,283', '68,210,660', '25,29', '', '', '']` vs blind-strip `['Salute of Ruler\nin guns.', '<unclear>...</unclear>']`
  - Leaf `238` `p0238-b0018`: full-page `['Total', '1,54,93', '1,90,57', '2,18,89', '2,63,67', '2,80,47', '3,17,34', '3,17,96', '3,18,71', '3,21,35']` vs blind-strip `['<i>Debt.</i>', 'Sterling debt converted into rupees at Rs. 15 to the pound']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`381` — catches smudged dates/figures in prose)**:
  - Leaf `17` `p0017-b0013`: VLM read `307` vs PDF OCR witness `['306', '407']`
  - Leaf `17` `p0017-b0013`: VLM read `325` vs PDF OCR witness `['125', '326']`
  - Leaf `21` `p0021-b0004`: VLM read `106` vs PDF OCR witness `['116', '126']`
  - Leaf `21` `p0021-b0005`: VLM read `107` vs PDF OCR witness `['117', '127']`
  - Leaf `21` `p0021-b0006`: VLM read `107` vs PDF OCR witness `['117', '127']`
  - Leaf `21` `p0021-b0007`: VLM read `108` vs PDF OCR witness `['118', '128']`
  - Leaf `21` `p0021-b0008`: VLM read `108` vs PDF OCR witness `['118', '128']`
  - Leaf `21` `p0021-b0009`: VLM read `109` vs PDF OCR witness `['129']`
  - Leaf `21` `p0021-b0010`: VLM read `110` vs PDF OCR witness `['112', '116', '117']`
  - Leaf `21` `p0021-b0011`: VLM read `110` vs PDF OCR witness `['112', '116', '117']`
  - Leaf `21` `p0021-b0012`: VLM read `111` vs PDF OCR witness `['112', '116', '117']`
  - Leaf `21` `p0021-b0013`: VLM read `111` vs PDF OCR witness `['112', '116', '117']`
  - Leaf `21` `p0021-b0014`: VLM read `111` vs PDF OCR witness `['112', '116', '117']`
  - Leaf `21` `p0021-b0016`: VLM read `113` vs PDF OCR witness `['112', '116', '117']`
  - Leaf `22` `p0022-b0006`: VLM read `131` vs PDF OCR witness `['130']`
  - Leaf `22` `p0022-b0007`: VLM read `131` vs PDF OCR witness `['130']`
  - Leaf `22` `p0022-b0008`: VLM read `131` vs PDF OCR witness `['130']`
  - Leaf `22` `p0022-b0009`: VLM read `132` vs PDF OCR witness `['130']`
  - Leaf `22` `p0022-b0010`: VLM read `133` vs PDF OCR witness `['130']`
  - Leaf `22` `p0022-b0011`: VLM read `134` vs PDF OCR witness `['130']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `401` prose joins, `7` split footnotes stitched, `1` multi-page tables unified, `218` total footnotes.
  - Stitched cross-page footnotes: p.61->p.62 (`1`), p.70->p.71 (`1`), p.85->p.86 (`2`), p.198->p.199 (`2`), p.238->p.241 (`*`), p.261->p.262 (`1`), p.276->p.277 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`156` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00114404 7"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"MICROFORMED BY PRESERVATION SERVICES DATE FEB 2 6 1987"*
  - Leaf `9` `p0009-b0001` (`scanner_residue`): *"345"*
  - Leaf `9` `p0009-b0005` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `9` `p0009-b0011` (`scanner_residue`): *"91304 219108."*
  - Leaf `10` `p0010-b0001` (`scanner_residue`): *"Embossed circular library stamp of the University of Toronto"*
  - Leaf `23` `p0023-b0037` (`scanner_residue`): *"22"*
  - Leaf `23` `p0023-b0038` (`noise`): *"vol. iv."*
  - Leaf `23` `p0023-b0039` (`noise`): *"b"*
  - Leaf `25` `p0025-b0038` (`noise`): *"b 2"*
  - Leaf `39` `p0039-b0009` (`noise`): *"VOL. IV."*
  - Leaf `39` `p0039-b0010` (`noise`): *"B"*
- **Unattested Line-Wrap Hyphenation Decisions (`126` unique words out of `2495` total wraps)**: `undeveloped` (p.25), `evildoers` (p.40), `courtyards` (p.41), `potentates` (p.46), `founding` (p.46), `brotherhood` (p.50), `problematical` (p.59), `countersigned` (p.77), `Mymensingh` (p.86), `Collector-Magis` (p.87), `admirals` (p.104), `Gulbarga` (p.106), `enveloping` (p.114), `expiration` (p.162), `newcomers` (p.165), `messages` (p.174), `residencybazars` (p.179), `testamentary` (p.185)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 1,161,268 chars
- **Distinct Non-ASCII Glyphs (`26` across `389` leaves)**: · É ä ç è é ô ö ü Ā ā ē ġ ħ ī œ ū ḥ „ ′ ⁄ ⅓ ⅔ ⅗ ⅙ ⅛
- **Corrections Replayed**: `63` applied, `0` orphaned/unmatched
