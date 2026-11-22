# Edition Verification & Run Audit — *Early Travels in India, 1583–1619*

- **Book ID**: `early-travels-in-india-1583-1619` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`100.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 377 of 378 pages, gemini-3.6-flash on 1 of 378 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `378` extracted, `18` blank/tissue, `0` failed (of `396` PDF leaves)
- **Tracked API Spend**: **`$1.6103`** (`75.0%` cached input tokens: `3,000,416` / `3,997,935` in, `559,816` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Community Edition! Human page-proof coverage is 0.0% (pages re-read 2.4%) toward Source-Certified.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 370 | `$1.4055` |
| `primary_quality_retry` | 5 | `$0.0565` |
| `continuation_arbiter_batch` | 28 | `$0.0454` |
| `recitation_retry` | 3 | `$0.0337` |
| `recitation_band_top` | 2 | `$0.0211` |
| `page_extract_batch_vetoed` | 5 | `$0.0207` |
| `secondary_gemini_rescue` | 1 | `$0.0129` |
| `recitation_band_bot` | 1 | `$0.0110` |
| `page_extract_batch_failed` | 3 | `$0.0034` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 1 pp., `gemini-3.8-flash`: 377 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `10, 31, 45, 165, 171, 205, 285`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `40` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`57` — catches smudged dates/figures in prose)**:
  - Leaf `13` `p0013-b0005`: VLM read `1583` vs PDF OCR witness `['1383']`
  - Leaf `26` `p0026-b0003`: VLM read `1589` vs PDF OCR witness `['1581', '1584', '1585']`
  - Leaf `26` `p0026-b0005`: VLM read `1586` vs PDF OCR witness `['1581', '1584', '1585']`
  - Leaf `27` `p0027-b0005`: VLM read `1586` vs PDF OCR witness `['1583', '1588']`
  - Leaf `51` `p0051-b0006`: VLM read `176` vs PDF OCR witness `['170']`
  - Leaf `52` `p0052-b0004`: VLM read `1592` vs PDF OCR witness `['1502']`
  - Leaf `73` `p0073-b0006`: VLM read `164` vs PDF OCR witness `['104']`
  - Leaf `79` `p0079-b0004`: VLM read `9366` vs PDF OCR witness `['9866']`
  - Leaf `82` `p0082-b0005`: VLM read `1606` vs PDF OCR witness `['1603']`
  - Leaf `88` `p0088-b0005`: VLM read `111` vs PDF OCR witness `['114']`
  - Leaf `89` `p0089-b0004`: VLM read `1616` vs PDF OCR witness `['1610']`
  - Leaf `90` `p0090-b0004`: VLM read `1608` vs PDF OCR witness `['1008', '1607']`
  - Leaf `95` `p0095-b0004`: VLM read `1610` vs PDF OCR witness `['1611']`
  - Leaf `154` `p0154-b0003`: VLM read `167` vs PDF OCR witness `['107']`
  - Leaf `154` `p0154-b0007`: VLM read `286` vs PDF OCR witness `['280']`
  - Leaf `155` `p0155-b0003`: VLM read `1612` vs PDF OCR witness `['1012']`
  - Leaf `181` `p0181-b0006`: VLM read `116` vs PDF OCR witness `['110', '113', '316']`
  - Leaf `194` `p0194-b0005`: VLM read `108` vs PDF OCR witness `['104']`
  - Leaf `236` `p0236-b0003`: VLM read `160` vs PDF OCR witness `['100']`
  - Leaf `236` `p0236-b0003`: VLM read `300` vs PDF OCR witness `['100', '200', '400']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `255` prose joins, `13` split footnotes stitched, `0` multi-page tables unified, `614` total footnotes.
  - Stitched cross-page footnotes: p.50->p.51 (`2`), p.53->p.54 (`3`), p.55->p.56 (`5`), p.106->p.107 (`2`), p.129->p.130 (`2`), p.130->p.131 (`6`), p.175->p.176 (`4`), p.184->p.185 (`5`), p.189->p.190 (`5`), p.202->p.203 (`3`), p.210->p.211 (`1`), p.267->p.268 (`1`), p.365->p.366 (`2`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`53` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 01096999 6"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2008 with funding from Microsoft Corporation"*
  - Leaf `3` `p0003-b0002` (`scanner_residue`): *"http://www.archive.org/details/earlytravelsinin00fostuoft"*
  - Leaf `11` `p0011-b0001` (`scanner_residue`): *"Sticker/tape residue in upper-left corner."*
  - Leaf `11` `p0011-b0005` (`scanner_residue`): *"Library embossing stamp: UNIVERSITY OF TORONTO LIBRARY."*
  - Leaf `11` `p0011-b0008` (`scanner_residue`): *"168327 4.1.22."*
  - Leaf `23` `p0023-b0005` (`noise`): *"B"*
  - Leaf `25` `p0025-b0007` (`noise`): *"B 2"*
  - Leaf `41` `p0041-b0009` (`noise`): *"C"*
  - Leaf `43` `p0043-b0006` (`noise`): *"C 2"*
  - Leaf `59` `p0059-b0006` (`noise`): *"D"*
  - Leaf `61` `p0061-b0008` (`noise`): *"D 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`81` unique words out of `406` total wraps)**: `assimilated` (p.16), `Nizamaluco` (p.37), `Serringe` (p.41), `Blagden` (p.56), `workemanship` (p.57), `doubtfull` (p.66), `Junsalaon` (p.67), `contemplating` (p.74), `Additional` (p.79), `discontentment` (p.85), `usefulness` (p.91), `lastnamed` (p.97), `Houshaberchan` (p.112), `outrage` (p.117), `complainant` (p.117), `emptiehanded` (p.119), `adventuring` (p.120), `smallshot` (p.129)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 646,965 chars, `greek`: 111 chars
- **Distinct Non-ASCII Glyphs (`74` across `250` leaves)**: Æ à á â ã æ ç è é ê ñ ú û ü Ā ā ē ė ġ ģ ĥ ħ Ī ī ı ō œ š ť ū ʾ ʿ Ζ έ ή ί α β δ ε ζ η θ ι μ ν ο π ρ ς σ τ χ ψ ω ό ύ Ḥ ḥ ṇ
- **Corrections Replayed**: `19` applied, `0` orphaned/unmatched
