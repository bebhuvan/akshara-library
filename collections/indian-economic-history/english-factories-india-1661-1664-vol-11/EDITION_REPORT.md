# Edition Verification & Run Audit — *The English Factories in India, 1661–1664*

- **Book ID**: `english-factories-india-1661-1664-vol-11` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`97.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 438 of 438 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `438` extracted, `8` blank/tissue, `0` failed (of `446` PDF leaves)
- **Tracked API Spend**: **`$2.0249`** (`74.4%` cached input tokens: `3,502,686` / `4,707,611` in, `711,865` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **22.0 / 25.0** | -3.0: 1 script/codepoint anomaly(ies) |

### Recommended Operator Next Actions
- Ready to ship as Community Edition! Human page-proof coverage is 0.0% (pages re-read 2.3%) toward Source-Certified.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 427 | `$1.7242` |
| `primary_quality_retry` | 10 | `$0.1409` |
| `page_extract_batch_vetoed` | 10 | `$0.0460` |
| `continuation_arbiter_batch` | 25 | `$0.0397` |
| `recitation_band_bot` | 2 | `$0.0205` |
| `recitation_band_top` | 2 | `$0.0201` |
| `recitation_retry` | 1 | `$0.0198` |
| `page_extract` | 1 | `$0.0125` |
| `page_extract_batch_failed` | 1 | `$0.0011` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 438 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `18` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `25` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`191` — catches smudged dates/figures in prose)**:
  - Leaf `43` `p0043-b0005`: VLM read `4,000` vs PDF OCR witness `['2000']`
  - Leaf `45` `p0045-b0007`: VLM read `2894` vs PDF OCR witness `['2893']`
  - Leaf `48` `p0048-b0006`: VLM read `15,000` vs PDF OCR witness `['65000']`
  - Leaf `60` `p0060-b0003`: VLM read `100` vs PDF OCR witness `['150']`
  - Leaf `74` `p0074-b0007`: VLM read `2896` vs PDF OCR witness `['2899']`
  - Leaf `105` `p0105-b0007`: VLM read `1662` vs PDF OCR witness `['1663']`
  - Leaf `130` `p0130-b0006`: VLM read `327` vs PDF OCR witness `['337']`
  - Leaf `134` `p0134-b0006`: VLM read `1662` vs PDF OCR witness `['1663']`
  - Leaf `152` `p0152-b0004`: VLM read `108` vs PDF OCR witness `['138']`
  - Leaf `158` `p0158-b0005`: VLM read `101` vs PDF OCR witness `['102']`
  - Leaf `163` `p0163-b0006`: VLM read `1660` vs PDF OCR witness `['1661', '1663']`
  - Leaf `171` `p0171-b0005`: VLM read `1661` vs PDF OCR witness `['1662']`
  - Leaf `172` `p0172-b0007`: VLM read `1661` vs PDF OCR witness `['1662']`
  - Leaf `182` `p0182-b0004`: VLM read `100,` vs PDF OCR witness `['200']`
  - Leaf `195` `p0195-b0007`: VLM read `1661` vs PDF OCR witness `['1662']`
  - Leaf `195` `p0195-b0007`: VLM read `1200` vs PDF OCR witness `['1000']`
  - Leaf `207` `p0207-b0004`: VLM read `100,` vs PDF OCR witness `['103', '109']`
  - Leaf `213` `p0213-b0003`: VLM read `300` vs PDF OCR witness `['200']`
  - Leaf `225` `p0225-b0003`: VLM read `100` vs PDF OCR witness `['110']`
  - Leaf `257` `p0257-b0005`: VLM read `110` vs PDF OCR witness `['112']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `329` prose joins, `8` split footnotes stitched, `0` multi-page tables unified, `398` total footnotes.
  - Stitched cross-page footnotes: p.94->p.95 (`1`), p.123->p.124 (`2`), p.144->p.145 (`2`), p.185->p.186 (`2`), p.191->p.192 (`1`), p.195->p.196 (`2`), p.203->p.204 (`1`), p.210->p.211 (`3`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`90` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 08381414 5"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2010 with funding from University of Toronto"*
  - Leaf `7` `p0007-b0002` (`scanner_residue`): *"http://www.archive.org/details/englishfactories11fost"*
  - Leaf `9` `p0009-b0002` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `9` `p0009-b0006` (`scanner_residue`): *"194274 16.2.25"*
  - Leaf `10` `p0010-b0001` (`scanner_residue`): *"LIBRARY OF THE UNIVERSITY OF TORONTO"*
  - Leaf `15` `p0015-b0009` (`noise`): *"2597"*
  - Leaf `15` `p0015-b0010` (`noise`): *"B"*
  - Leaf `17` `p0017-b0008` (`noise`): *"B 2"*
  - Leaf `31` `p0031-b0012` (`noise`): *"2597"*
  - Leaf `31` `p0031-b0013` (`noise`): *"C"*
  - Leaf `33` `p0033-b0009` (`noise`): *"C 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`90` unique words out of `758` total wraps)**: `Manuscripts` (p.12), `chyrurgion` (p.25), `disguised` (p.29), `feasibility` (p.30), `comparison` (p.31), `Precidency` (p.33), `dominereing` (p.36), `treacherously` (p.52), `dispeopled` (p.54), `ungrateful` (p.54), `conjectured` (p.72), `preposterous` (p.73), `procurie` (p.76), `enterteined` (p.81), `frightful` (p.83), `commendable` (p.101), `industrious` (p.103), `subsistance` (p.103)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 835,567 chars
- **Distinct Non-ASCII Glyphs (`27` across `306` leaves)**: ­ À à ã ç é í ó ô õ Ā ā ē Ġ ġ Ī ī ı ō ū ſ ′ ⁄ ⅔ ⅛ ⅜ ⅝
- **Corrections Replayed**: `130` applied, `0` orphaned/unmatched
