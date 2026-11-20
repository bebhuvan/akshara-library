# Edition Verification & Run Audit — *India at the Death of Akbar*

- **Book ID**: `india-at-the-death-of-akbar` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 352 of 353 pages, gemini-3.6-flash on 1 of 353 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `353` extracted, `1` blank/tissue, `0` failed (of `354` PDF leaves)
- **Tracked API Spend**: **`$1.4652`** (`76.9%` cached input tokens: `2,733,500` / `3,554,976` in, `476,830` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 4.8% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 351 | `$1.3655` |
| `pro_table_adjudicate` | 1 | `$0.0367` |
| `page_extract` | 3 | `$0.0200` |
| `continuation_arbiter_batch` | 13 | `$0.0199` |
| `secondary_gemini_rescue` | 1 | `$0.0120` |
| `blind_totals_strip` | 2 | `$0.0071` |
| `page_extract_batch_vetoed` | 1 | `$0.0039` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 1 pp., `gemini-3.8-flash`: 352 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `220`
- **Surgical Table Adjudications (`gemini-4-argon` / complex rescue)**:
  - Leaf `149` (`gemini-4-argon`): accepted=`True`, mismatches `1` -> `1`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`6` — catches smudged dates/figures in prose)**:
  - Leaf `45` `p0045-b0009`: VLM read `520` vs PDF OCR witness `['620']`
  - Leaf `45` `p0045-b0009`: VLM read `245` vs PDF OCR witness `['246']`
  - Leaf `277` `p0277-b0007`: VLM read `595` vs PDF OCR witness `['695']`
  - Leaf `337` `p0337-b0013`: VLM read `270` vs PDF OCR witness `['271', '273', '277']`
  - Leaf `338` `p0338-b0042`: VLM read `135` vs PDF OCR witness `['105', '130', '132']`
  - Leaf `341` `p0341-b0059`: VLM read `175` vs PDF OCR witness `['105', '115', '125']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `244` prose joins, `9` split footnotes stitched, `0` multi-page tables unified, `158` total footnotes.
  - Stitched cross-page footnotes: p.29->p.30 (`1`), p.42->p.43 (`1`), p.43->p.44 (`1`), p.115->p.116 (`1`), p.146->p.147 (`1`), p.206->p.207 (`1`), p.223->p.224 (`1`), p.225->p.226 (`2`), p.285->p.286 (`2`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`44` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 01718397 1"*
  - Leaf `7` `p0007-b0003` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `7` `p0007-b0005` (`scanner_residue`): *"157076 6.11.20."*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"LIBRARY OF TORONTO UNIVERSITY embossed stamp"*
  - Leaf `17` `p0017-b0006` (`noise`): *"B"*
  - Leaf `23` `p0023-b0001` (`noise`): *"I"*
  - Leaf `33` `p0033-b0006` (`noise`): *"C"*
  - Leaf `43` `p0043-b0001` (`noise`): *"I"*
  - Leaf `49` `p0049-b0006` (`noise`): *"D"*
  - Leaf `57` `p0057-b0001` (`noise`): *"ii"*
  - Leaf `59` `p0059-b0001` (`noise`): *"ii"*
  - Leaf `65` `p0065-b0007` (`noise`): *"E"*
- **Unattested Line-Wrap Hyphenation Decisions (`50` unique words out of `703` total wraps)**: `byepaths` (p.11), `huntinggrounds` (p.23), `surmount` (p.37), `distributors` (p.40), `weakness` (p.49), `tranquillity` (p.56), `latepassed` (p.60), `gooseherd` (p.60), `peculiarities` (p.65), `informing` (p.66), `compromise` (p.70), `economised` (p.80), `vagueness` (p.89), `practising` (p.99), `worthless` (p.102), `revenuedefaulters` (p.108), `withdraw` (p.109), `superfluities` (p.110)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 595,829 chars
- **Distinct Non-ASCII Glyphs (`17` across `101` leaves)**: · ã ç é ô õ ö ú Ā ā ī ş ť ū „ ⅓ ⅛
- **Corrections Replayed**: `7` applied, `0` orphaned/unmatched
