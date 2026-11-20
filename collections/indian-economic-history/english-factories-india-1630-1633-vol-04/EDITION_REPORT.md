# Edition Verification & Run Audit — *The English Factories in India, 1630–1633*

- **Book ID**: `english-factories-india-1630-1633-vol-04` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 396 of 400 pages, gemini-3.6-flash on 4 of 400 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `400` extracted, `4` blank/tissue, `0` failed (of `404` PDF leaves)
- **Tracked API Spend**: **`$1.9860`** (`72.2%` cached input tokens: `3,207,050` / `4,439,101` in, `620,615` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 1.8% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 380 | `$1.4464` |
| `primary_quality_retry` | 18 | `$0.2307` |
| `page_extract_batch_vetoed` | 18 | `$0.0726` |
| `recitation_band_top` | 7 | `$0.0726` |
| `recitation_retry` | 2 | `$0.0500` |
| `recitation_band_bot` | 4 | `$0.0432` |
| `secondary_gemini_rescue` | 4 | `$0.0418` |
| `continuation_arbiter_batch` | 18 | `$0.0264` |
| `page_extract_batch_failed` | 2 | `$0.0023` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 4 pp., `gemini-3.8-flash`: 396 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `403`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `146` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `162` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `261` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`188` — catches smudged dates/figures in prose)**:
  - Leaf `6` `p0006-b0004`: VLM read `1643` vs PDF OCR witness `['1043']`
  - Leaf `22` `p0022-b0003`: VLM read `160` vs PDF OCR witness `['150']`
  - Leaf `22` `p0022-b0004`: VLM read `100,` vs PDF OCR witness `['150', '700', '800']`
  - Leaf `24` `p0024-b0005`: VLM read `1615` vs PDF OCR witness `['1617', '1625']`
  - Leaf `25` `p0025-b0005`: VLM read `1631` vs PDF OCR witness `['1633']`
  - Leaf `35` `p0035-b0007`: VLM read `195` vs PDF OCR witness `['295']`
  - Leaf `40` `p0040-b0005`: VLM read `256` vs PDF OCR witness `['258']`
  - Leaf `46` `p0046-b0002`: VLM read `1615` vs PDF OCR witness `['1613', '1616', '1618']`
  - Leaf `48` `p0048-b0003`: VLM read `1631` vs PDF OCR witness `['1630']`
  - Leaf `66` `p0066-b0003`: VLM read `1,000` vs PDF OCR witness `['2000']`
  - Leaf `102` `p0102-b0005`: VLM read `4,000` vs PDF OCR witness `['5000']`
  - Leaf `136` `p0136-b0004`: VLM read `1,000` vs PDF OCR witness `['1600']`
  - Leaf `149` `p0149-b0006`: VLM read `101` vs PDF OCR witness `['100', '103']`
  - Leaf `149` `p0149-b0008`: VLM read `102` vs PDF OCR witness `['100', '103']`
  - Leaf `158` `p0158-b0003`: VLM read `200` vs PDF OCR witness `['300', '400']`
  - Leaf `165` `p0165-b0003`: VLM read `1631` vs PDF OCR witness `['1630']`
  - Leaf `177` `p0177-b0003`: VLM read `1631` vs PDF OCR witness `['1630']`
  - Leaf `186` `p0186-b0003`: VLM read `1634` vs PDF OCR witness `['1631']`
  - Leaf `189` `p0189-b0003`: VLM read `1634` vs PDF OCR witness `['1630', '1631']`
  - Leaf `207` `p0207-b0003`: VLM read `1634` vs PDF OCR witness `['1631']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `192` prose joins, `5` split footnotes stitched, `0` multi-page tables unified, `338` total footnotes.
  - Stitched cross-page footnotes: p.23->p.24 (`1`), p.29->p.30 (`1`), p.36->p.37 (`1`), p.227->p.228 (`1`), p.365->p.366 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`81` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 08381420 2"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2010 with funding from University of Toronto"*
  - Leaf `5` `p0005-b0002` (`scanner_residue`): *"http://www.archive.org/details/englishfactories04fost"*
  - Leaf `7` `p0007-b0009` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed library stamp of the University of Toronto"*
  - Leaf `23` `p0023-b0006` (`noise`): *"foster iv"*
  - Leaf `23` `p0023-b0007` (`noise`): *"b"*
  - Leaf `25` `p0025-b0006` (`noise`): *"b 2"*
  - Leaf `39` `p0039-b0004` (`noise`): *"FOSTER IV"*
  - Leaf `39` `p0039-b0005` (`noise`): *"C"*
  - Leaf `47` `p0047-b0006` (`noise`): *"Foster iv"*
  - Leaf `47` `p0047-b0007` (`noise`): *"B"*
- **Unattested Line-Wrap Hyphenation Decisions (`96` unique words out of `742` total wraps)**: `resultant` (p.9), `Ferguson` (p.10), `compiling` (p.10), `commencing` (p.13), `countermove` (p.14), `compelled` (p.16), `prematurely` (p.16), `consternation` (p.16), `Bādshāhnāma` (p.19), `Cowper` (p.21), `foodprices` (p.27), `comonwealth` (p.29), `temptation` (p.36), `overindulgence` (p.38), `modifications` (p.41), `indisputable` (p.44), `cacaroches` (p.55), `persisted` (p.59)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 713,356 chars
- **Distinct Non-ASCII Glyphs (`27` across `247` leaves)**: à á ã æ ç é ï ó û Ā ā ē ġ ī ō ū ṃ ṣ Ṭ ṭ ― ′ ₁ ₈ ⅔ ⅛ ⅝
- **Corrections Replayed**: `4` applied, `0` orphaned/unmatched
