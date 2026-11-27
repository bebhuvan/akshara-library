# Edition Verification & Run Audit — *The Imperial Gazetteer of India: The Indian Empire, Vol. III — Economic*

- **Book ID**: `imperial-gazetteer-of-india-vol-03-economic` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`84.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 561 of 561 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `561` extracted, `5` blank/tissue, `0` failed (of `566` PDF leaves)
- **Tracked API Spend**: **`$4.4444`** (`72.0%` cached input tokens: `5,170,465` / `7,181,804` in, `1,467,820` out, `194` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **9.0 / 25.0** | -12.0: 8 column total arithmetic mismatch(es); -4.0: 1 collapsed/jammed table row warning(s) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 552 | `$2.6690` |
| `page_extract` | 80 | `$1.3763` |
| `continuation_arbiter_batch` | 70 | `$0.1815` |
| `blind_totals_strip_batch` | 45 | `$0.0839` |
| `recitation_retry` | 5 | `$0.0801` |
| `primary_quality_retry` | 4 | `$0.0310` |
| `page_extract_batch_vetoed` | 4 | `$0.0168` |
| `page_extract_batch_failed` | 5 | `$0.0058` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 561 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `142, 143, 353, 354, 355, 454, 470, 487, 514, 515, 516`
- **450-DPI Blind Totals Strip Disagreements (`9`)**:
  - Leaf `296` `p0296-b0037`: full-page `['Grand Total', '1,00.15', '9,37.40']` vs blind-strip `['<sc>Grand Total</sc>', '1,00·15', '9,37·40']`
  - Leaf `297` `p0297-b0025`: full-page `['Grand Total', '38,68·15', '59,62·64']` vs blind-strip `['<sc>Grand Total</sc>', '38,68.15', '59,62.64']`
  - Leaf `351` `p0351-b0028`: full-page `['Grand Total of Imports', '. .', '143,92,07,204']` vs blind-strip `['Treasure . . . . .', '. . .', '6,48,66,452']`
  - Leaf `352` `p0352-b0053`: full-page `['Grand Total of Exports .', '...', '174,13,65,396']` vs blind-strip `['Treasure . . . . .', '...', '8,45,22,511']`
  - Leaf `355` `p0355-b0021`: full-page `['TOTAL', '6,41,48,898', '6,89,94,079', '6,14,20,422', '7,02,87,433', '7,06,00,314', '5,42,61,723', '6,02,61,390', '5,29,37,593', '5,37,07,076', '6,15,05,629']` vs blind-strip `['6,89,94,079', '6,14,20,422', '7,02,87,433', '7,06,00,314', '5,42,61,723', '6,02,61,390', '5,29,37,593', '5,37']`
  - Leaf `454` `p0454-b0011`: full-page `['Total', '5,658', '14,480', '124', '32', '1,536', '553', '868', '1,307', '236', '1,864', '1,322', '74', '6,479', '20,129', '1,446', '28,054']` vs blind-strip `['s.', '236', '']`
  - Leaf `470` `p0470-b0020`: full-page `['TOTAL', '15,403', '33,897*', '286,822,556', '272,523,104', '34,351,819', '34,262,838', '3,941,719', '631,902,126', '2.2', '39.7']` vs blind-strip `['Bengal . . . .', '1,977', '5,764', '46,219,637', '43,970,325']`
  - Leaf `514` `p0514-b0019`: full-page `['Average for all India', '6·2 to 6·4', '6·5 to 7·0', '6·2 to 6·6', '6·4 to 6·8', '6·3 to 6·8', '6·5 to 7·0', '6·7 to 7·3', '20·6']` vs blind-strip `['', 'JOINTLY']`
  - Leaf `515` `p0515-b0017`: full-page `['Average for all India .', '6·4 to 6·7', '6·4 to 6·8', '6·6 to 7·0', '6·6 to 7·1', '6·9 to 7·5', '6·9 to 7·5', '6·9 to 7·4', '9·5']` vs blind-strip `['to 6·4']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`285` — catches smudged dates/figures in prose)**:
  - Leaf `13` `p0013-b0006`: VLM read `180` vs PDF OCR witness `['100']`
  - Leaf `15` `p0015-b0004`: VLM read `101` vs PDF OCR witness `['102']`
  - Leaf `15` `p0015-b0006`: VLM read `128` vs PDF OCR witness `['127', '168']`
  - Leaf `15` `p0015-b0006`: VLM read `167` vs PDF OCR witness `['127', '168']`
  - Leaf `15` `p0015-b0014`: VLM read `503` vs PDF OCR witness `['502']`
  - Leaf `21` `p0021-b0035`: VLM read `111` vs PDF OCR witness `['101', '110', '112']`
  - Leaf `22` `p0022-b0005`: VLM read `115` vs PDF OCR witness `['113', '118', '119']`
  - Leaf `22` `p0022-b0006`: VLM read `116` vs PDF OCR witness `['113', '118', '119']`
  - Leaf `23` `p0023-b0032`: VLM read `143` vs PDF OCR witness `['140', '141', '142']`
  - Leaf `23` `p0023-b0033`: VLM read `143` vs PDF OCR witness `['140', '141', '142']`
  - Leaf `23` `p0023-b0034`: VLM read `143` vs PDF OCR witness `['140', '141', '142']`
  - Leaf `25` `p0025-b0029`: VLM read `173` vs PDF OCR witness `['163', '171', '172']`
  - Leaf `25` `p0025-b0039`: VLM read `177` vs PDF OCR witness `['167', '171', '172']`
  - Leaf `32` `p0032-b0004`: VLM read `281` vs PDF OCR witness `['282', '283', '284']`
  - Leaf `32` `p0032-b0005`: VLM read `281` vs PDF OCR witness `['282', '283', '284']`
  - Leaf `32` `p0032-b0018`: VLM read `290` vs PDF OCR witness `['291', '292', '293']`
  - Leaf `32` `p0032-b0019`: VLM read `290` vs PDF OCR witness `['291', '292', '293']`
  - Leaf `33` `p0033-b0036`: VLM read `1900` vs PDF OCR witness `['1904']`
  - Leaf `33` `p0033-b0037`: VLM read `1900` vs PDF OCR witness `['1904']`
  - Leaf `33` `p0033-b0038`: VLM read `313` vs PDF OCR witness `['303', '311', '312']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `384` prose joins, `3` split footnotes stitched, `4` multi-page tables unified, `141` total footnotes.
  - Stitched cross-page footnotes: p.508->p.509 (`1`), p.524->p.525 (`1`), p.539->p.540 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`193` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00114403 9"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2013"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"http://archive.org/details/imperialgazette03hunt"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"MICROFORMED BY PRESERVATION SERVICES DATE 2861. 9. 8. 0.3 ....."*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"In. 345"*
  - Leaf `7` `p0007-b0005` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY blind stamp"*
  - Leaf `7` `p0007-b0011` (`scanner_residue`): *"91303 2/9/08."*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `9` `p0009-b0002` (`scanner_residue`): *"University of Toronto embossed library stamp"*
  - Leaf `23` `p0023-b0048` (`noise`): *"vol. iii"*
  - Leaf `23` `p0023-b0049` (`noise`): *"b"*
  - Leaf `25` `p0025-b0040` (`noise`): *"b 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`94` unique words out of `1896` total wraps)**: `undesirable` (p.11), `skilfully` (p.48), `unequalled` (p.48), `disposing` (p.62), `purification` (p.63), `Leguminosae` (p.65), `substantiated` (p.89), `broadcasted` (p.95), `expeditions` (p.98), `rediscovered` (p.113), `Anacardium` (p.117), `strawberry` (p.117), `itinerating` (p.126), `oldestablished` (p.130), `inhabit` (p.147), `administra` (p.149), `compounded` (p.155), `unnecessarily` (p.156)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 1,047,213 chars
- **Distinct Non-ASCII Glyphs (`25` across `434` leaves)**: · â ç é ô ö ü Ā ā ġ ħ ī ū Ṭ „ ′ ″ ⁄ ⅓ ⅔ ⅛ ⅜ ⅞ ⎰ ⎱
- **Corrections Replayed**: `82` applied, `0` orphaned/unmatched
