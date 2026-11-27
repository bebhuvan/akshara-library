# Edition Verification & Run Audit — *The English Factories in India, 1646–1650*

- **Book ID**: `english-factories-india-1646-1650-vol-08` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 397 of 400 pages, gemini-3.6-flash on 3 of 400 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `400` extracted, `6` blank/tissue, `0` failed (of `406` PDF leaves)
- **Tracked API Spend**: **`$1.8144`** (`73.5%` cached input tokens: `3,215,299` / `4,375,190` in, `581,793` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 1.0% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 385 | `$1.4403` |
| `primary_quality_retry` | 15 | `$0.1699` |
| `recitation_band_top` | 6 | `$0.0622` |
| `page_extract_batch_vetoed` | 15 | `$0.0509` |
| `recitation_band_bot` | 4 | `$0.0423` |
| `secondary_gemini_rescue` | 3 | `$0.0308` |
| `continuation_arbiter_batch` | 14 | `$0.0179` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 3 pp., `gemini-3.8-flash`: 397 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `65` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `177` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `259` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`238` — catches smudged dates/figures in prose)**:
  - Leaf `74` `p0074-b0003`: VLM read `2,000` vs PDF OCR witness `['3000', '5000']`
  - Leaf `105` `p0105-b0007`: VLM read `000` vs PDF OCR witness `['200']`
  - Leaf `106` `p0106-b0003`: VLM read `000` vs PDF OCR witness `['100']`
  - Leaf `115` `p0115-b0003`: VLM read `500` vs PDF OCR witness `['200', '400']`
  - Leaf `121` `p0121-b0003`: VLM read `204` vs PDF OCR witness `['304']`
  - Leaf `132` `p0132-b0003`: VLM read `12,000` vs PDF OCR witness `['13000']`
  - Leaf `148` `p0148-b0005`: VLM read `1650` vs PDF OCR witness `['1657']`
  - Leaf `149` `p0149-b0004`: VLM read `101` vs PDF OCR witness `['105']`
  - Leaf `155` `p0155-b0006`: VLM read `134` vs PDF OCR witness `['130']`
  - Leaf `161` `p0161-b0003`: VLM read `122` vs PDF OCR witness `['123', '152']`
  - Leaf `161` `p0161-b0007`: VLM read `110` vs PDF OCR witness `['130']`
  - Leaf `170` `p0170-b0006`: VLM read `172` vs PDF OCR witness `['132']`
  - Leaf `177` `p0177-b0003`: VLM read `179` vs PDF OCR witness `['139']`
  - Leaf `214` `p0214-b0003`: VLM read `2057` vs PDF OCR witness `['3057']`
  - Leaf `216` `p0216-b0004`: VLM read `2060` vs PDF OCR witness `['3060']`
  - Leaf `230` `p0230-b0004`: VLM read `297` vs PDF OCR witness `['397']`
  - Leaf `244` `p0244-b0007`: VLM read `214` vs PDF OCR witness `['211']`
  - Leaf `244` `p0244-b0007`: VLM read `218` vs PDF OCR witness `['211']`
  - Leaf `270` `p0270-b0003`: VLM read `1000` vs PDF OCR witness `['5000']`
  - Leaf `323` `p0323-b0004`: VLM read `317` vs PDF OCR witness `['313']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `164` prose joins, `1` split footnotes stitched, `0` multi-page tables unified, `342` total footnotes.
  - Stitched cross-page footnotes: p.92->p.93 (`2`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`84` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 08381417 8"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2010 with funding from University of Toronto"*
  - Leaf `5` `p0005-b0002` (`scanner_residue`): *"http://www.archive.org/details/englishfactories08fost"*
  - Leaf `6` `p0006-b0003` (`noise`): *"Front. E. F. VIII."*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"⌊Vol. 8⌋"*
  - Leaf `7` `p0007-b0006` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY blind embossed stamp"*
  - Leaf `7` `p0007-b0010` (`scanner_residue`): *"135-395- 2/12/14"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Library embossing stamp of the University of Toronto."*
  - Leaf `9` `p0009-b0004` (`noise`): *"a 2"*
  - Leaf `22` `p0022-b0006` (`scanner_residue`): *"5"*
  - Leaf `23` `p0023-b0004` (`noise`): *"FOSTER VIII"*
  - Leaf `23` `p0023-b0005` (`noise`): *"b"*
- **Unattested Line-Wrap Hyphenation Decisions (`83` unique words out of `616` total wraps)**: `acknowledging` (p.11), `ambitions` (p.11), `a-bounding` (p.12), `absorbed` (p.16), `adventurous` (p.20), `conjoint` (p.28), `brightened` (p.33), `commendably` (p.41), `spoiltrade` (p.43), `commendations` (p.47), `undergone` (p.48), `flyboat` (p.60), `composition` (p.64), `pretendeing` (p.66), `acknowledgeth` (p.75), `disengagements` (p.76), `informacion` (p.77), `yourselfe` (p.77)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 710,310 chars
- **Distinct Non-ASCII Glyphs (`24` across `316` leaves)**: · â ã ç é ê Ā ā ē ġ ī ō œ ũ ū ̲ Ḥ ṣ „ ′ ⁄ ⅓ ⅝ ⅞
- **Corrections Replayed**: `12` applied, `0` orphaned/unmatched
