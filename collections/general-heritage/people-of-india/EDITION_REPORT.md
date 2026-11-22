# Edition Verification & Run Audit — *The People of India*

- **Book ID**: `people-of-india` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 575 of 576 pages, gemini-3.8-flash on 1 of 576 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `576` extracted, `106` blank/tissue, `0` failed (of `682` PDF leaves)
- **Tracked API Spend**: **`$10.4115`** (`9.2%` cached input tokens: `638,976` / `6,913,683` in, `880,505` out, `641,360` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 8.0% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 575 | `$10.1016` |
| `continuation_arbiter_batch` | 57 | `$0.1262` |
| `recitation_band_top` | 2 | `$0.0997` |
| `recitation_band_bot` | 2 | `$0.0260` |
| `tertiary_gemini_rescue` | 1 | `$0.0234` |
| `secondary_gemini_rescue` | 1 | `$0.0174` |
| `recitation_retry` | 1 | `$0.0087` |
| `page_extract_batch_failed` | 1 | `$0.0086` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 1 pp., `gemini-4-hydrogen`: 575 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `8, 40, 168, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406 (+32 more)`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`213` — catches smudged dates/figures in prose)**:
  - Leaf `20` `p0020-b0004`: VLM read `1911` vs PDF OCR witness `['1901', '1910', '1913']`
  - Leaf `20` `p0020-b0005`: VLM read `1891` vs PDF OCR witness `['1890', '1899']`
  - Leaf `21` `p0021-b0006`: VLM read `1911` vs PDF OCR witness `['1910']`
  - Leaf `24` `p0024-b0004`: VLM read `1911` vs PDF OCR witness `['1914']`
  - Leaf `24` `p0024-b0005`: VLM read `1911` vs PDF OCR witness `['1914']`
  - Leaf `25` `p0025-b0007`: VLM read `1905` vs PDF OCR witness `['1909']`
  - Leaf `26` `p0026-b0006`: VLM read `1911` vs PDF OCR witness `['1901', '1912', '1913']`
  - Leaf `26` `p0026-b0009`: VLM read `1911` vs PDF OCR witness `['1901', '1912', '1913']`
  - Leaf `26` `p0026-b0009`: VLM read `1911` vs PDF OCR witness `['1901', '1912', '1913']`
  - Leaf `30` `p0030-b0035`: VLM read `101` vs PDF OCR witness `['100', '102', '103']`
  - Leaf `30` `p0030-b0043`: VLM read `111` vs PDF OCR witness `['114', '121']`
  - Leaf `30` `p0030-b0044`: VLM read `113` vs PDF OCR witness `['103', '114']`
  - Leaf `31` `p0031-b0047`: VLM read `152` vs PDF OCR witness `['132', '142']`
  - Leaf `32` `p0032-b0020`: VLM read `185` vs PDF OCR witness `['165', '182', '183']`
  - Leaf `33` `p0033-b0036`: VLM read `253` vs PDF OCR witness `['223', '233', '243']`
  - Leaf `33` `p0033-b0038`: VLM read `255` vs PDF OCR witness `['225', '235', '245']`
  - Leaf `33` `p0033-b0041`: VLM read `257` vs PDF OCR witness `['217', '227', '237']`
  - Leaf `33` `p0033-b0042`: VLM read `258` vs PDF OCR witness `['218', '228', '238']`
  - Leaf `33` `p0033-b0043`: VLM read `259` vs PDF OCR witness `['219', '239', '249']`
  - Leaf `33` `p0033-b0044`: VLM read `261` vs PDF OCR witness `['231', '262']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `299` prose joins, `8` split footnotes stitched, `0` multi-page tables unified, `216` total footnotes.
  - Stitched cross-page footnotes: p.101->p.102 (`*`), p.219->p.220 (`†`), p.244->p.245 (`*`), p.247->p.248 (`*`), p.262->p.263 (`†`), p.438->p.439 (`*`), p.446->p.447 (`*`), p.460->p.461 (`*`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`68` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"ASIA"*
  - Leaf `1` `p0001-b0003` (`scanner_residue`): *"LIBRARY ANNEX 2"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"CORNELL UNIVERSITY LIBRARY (bookplate with university seal)"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"Cornell University Library DS 421.R59 1915 The people of India, 3 1924 024 114 773 ech"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Cornell University Library"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"The original of this book is in the Cornell University Library."*
  - Leaf `4` `p0004-b0003` (`scanner_residue`): *"There are no known copyright restrictions in the United States on the use of the text."*
  - Leaf `4` `p0004-b0004` (`scanner_residue`): *"http://www.archive.org/details/cu31924024114773"*
  - Leaf `9` `p0009-b0006` (`scanner_residue`): *"UNBINDABLE"*
  - Leaf `10` `p0010-b0002` (`scanner_residue`): *"387110 B. GN"*
  - Leaf `23` `p0023-b0010` (`noise`): *"R, PI"*
  - Leaf `23` `p0023-b0011` (`noise`): *"b"*
- **Unattested Line-Wrap Hyphenation Decisions (`98` unique words out of `952` total wraps)**: `reproductions` (p.15), `outlive` (p.46), `Architectura` (p.58), `adjustment` (p.59), `projecting` (p.66), `Mediterranean` (p.68), `endowment` (p.80), `lawlessness` (p.96), `depopulated` (p.97), `wormeaten` (p.105), `Hobson-Jobson` (p.109), `Robinson` (p.111), `bloodkindred` (p.112), `precautions` (p.115), `interbreeding` (p.125), `Khāngār-Mūndā` (p.125), `pointing` (p.128), `Bundelkhand` (p.143)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 963,699 chars, `greek`: 186 chars
- **Distinct Non-ASCII Glyphs (`86` across `393` leaves)**: · Æ É à á â ã ä æ ç è é ê ë í î ï ô ö ù û ü Ā ā Ē ē Ī ī ō ŏ œ Ś Ū ū Α ά έ ή ί α γ δ ε ζ η θ ι κ λ μ ν ξ ο π ρ ς σ τ υ φ
- **Corrections Replayed**: `129` applied, `0` orphaned/unmatched
