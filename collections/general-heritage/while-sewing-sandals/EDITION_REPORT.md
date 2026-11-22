# Edition Verification & Run Audit — *While Sewing Sandals*

- **Book ID**: `while-sewing-sandals` | **Run ID**: `g38-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 337 of 337 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `337` extracted, `25` blank/tissue, `0` failed (of `362` PDF leaves)
- **Tracked API Spend**: **`$0.9958`** (`76.7%` cached input tokens: `2,695,663` / `3,514,816` in, `312,325` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 0.6% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 337 | `$0.9566` |
| `continuation_arbiter_batch` | 29 | `$0.0354` |
| `blind_totals_strip` | 1 | `$0.0038` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 337 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `68, 191, 244`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`13` — catches smudged dates/figures in prose)**:
  - Leaf `77` `p0077-b0004`: VLM read `1000` vs PDF OCR witness `['1200']`
  - Leaf `349` `p0349-b0007`: VLM read `101` vs PDF OCR witness `['102', '105', '107']`
  - Leaf `349` `p0349-b0019`: VLM read `310` vs PDF OCR witness `['315']`
  - Leaf `349` `p0349-b0024`: VLM read `190` vs PDF OCR witness `['195']`
  - Leaf `350` `p0350-b0004`: VLM read `101` vs PDF OCR witness `['102', '103', '107']`
  - Leaf `350` `p0350-b0018`: VLM read `197` vs PDF OCR witness `['107', '187', '190']`
  - Leaf `350` `p0350-b0040`: VLM read `101` vs PDF OCR witness `['102', '103', '107']`
  - Leaf `350` `p0350-b0047`: VLM read `181` vs PDF OCR witness `['151', '185', '187']`
  - Leaf `350` `p0350-b0047`: VLM read `297` vs PDF OCR witness `['227', '247', '291']`
  - Leaf `351` `p0351-b0003`: VLM read `101` vs PDF OCR witness `['102', '104', '131']`
  - Leaf `353` `p0353-b0031`: VLM read `251` vs PDF OCR witness `['250', '281']`
  - Leaf `354` `p0354-b0010`: VLM read `101` vs PDF OCR witness `['100', '102', '103']`
  - Leaf `354` `p0354-b0051`: VLM read `120` vs PDF OCR witness `['100', '122', '127']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `232` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `0` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`50` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"University of California Library bookplate: Seal of the University of California, inscribe"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"2.50"*
  - Leaf `3` `p0003-b0002` (`noise`): *"Johannes Messiah John Hudson Howland Windsor Middlebury Vermont"*
  - Leaf `10` `p0010-b0001` (`scanner_residue`): *"CARPENTIER"*
  - Leaf `11` `p0011-b0001` (`scanner_residue`): *"DS 432 T4 C6"*
  - Leaf `11` `p0011-b0006` (`scanner_residue`): *"M860935"*
  - Leaf `19` `p0019-b0003` (`noise`): *"W.S.S."*
  - Leaf `19` `p0019-b0005` (`noise`): *"I"*
  - Leaf `35` `p0035-b0005` (`noise`): *"W.S.S."*
  - Leaf `35` `p0035-b0006` (`noise`): *"2"*
  - Leaf `51` `p0051-b0006` (`noise`): *"W.S.S."*
  - Leaf `51` `p0051-b0007` (`noise`): *"3"*
- **Unattested Line-Wrap Hyphenation Decisions (`91` unique words out of `535` total wraps)**: `AFFECTION-ATELY` (p.11), `differentiate` (p.22), `uplifting` (p.25), `structure` (p.26), `philological` (p.27), `introducing` (p.29), `abhorred` (p.29), `transplanted` (p.35), `admonishing` (p.35), `recorded` (p.36), `chieftains` (p.37), `greatness` (p.38), `conducive` (p.40), `pavilion` (p.41), `compilation` (p.44), `overshadowed` (p.51), `statistical` (p.51), `dishonour` (p.52)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 262,155 chars
- **Distinct Non-ASCII Glyphs (`6` across `12` leaves)**: æ é ô ö ā ‹
- **Corrections Replayed**: `6` applied, `0` orphaned/unmatched
