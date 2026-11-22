# Edition Verification & Run Audit — *Recent Economic Developments in the Punjab*

- **Book ID**: `recent-economic-developments-punjab-wilson-1910` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`88.0 / 100`** (`community`)
- **Reader**: Read by gemini-4-hydrogen on 60 of 60 pages. Declared reader profile: tables (new readings use gemini-4-hydrogen).
- **Pages**: `60` extracted, `2` blank/tissue, `0` failed (of `62` PDF leaves)
- **Tracked API Spend**: **`$1.3091`** (`2.4%` cached input tokens: `18,312` / `779,093` in, `114,592` out, `72,605` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **13.0 / 25.0** | -12.0: 4 column total arithmetic mismatch(es) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 60 | `$1.1688` |
| `blind_totals_strip` | 6 | `$0.0716` |
| `continuation_arbiter_batch` | 9 | `$0.0686` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 60 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `57, 58`
- **450-DPI Blind Totals Strip Disagreements (`2`)**:
  - Leaf `54` `p0054-b0042`: full-page `['Average of eighteen years ending 1890', '—', '—', '19.4', '20.0', '41.9']` vs blind-strip `['Average of eighteen years ending 1890', '—', '—', '19·4', '20·0', '41·9']`
  - Leaf `54` `p0054-b0043`: full-page `['Average of nineteen years ending 1909', '—', '—', '15.5', '21.9', '29.0']` vs blind-strip `['Average of nineteen years ending 1909', '—', '—', '15·5', '21·9', '29·0']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`7` — catches smudged dates/figures in prose)**:
  - Leaf `8` `p0008-b0007`: VLM read `1886` vs PDF OCR witness `['1887']`
  - Leaf `8` `p0008-b0007`: VLM read `1908` vs PDF OCR witness `['1901']`
  - Leaf `9` `p0009-b0003`: VLM read `195` vs PDF OCR witness `['198']`
  - Leaf `12` `p0012-b0004`: VLM read `8,000,000` vs PDF OCR witness `['6000000']`
  - Leaf `38` `p0038-b0003`: VLM read `60,000` vs PDF OCR witness `['40000']`
  - Leaf `45` `p0045-b0003`: VLM read `6,000,000` vs PDF OCR witness `['0000000']`
  - Leaf `56` `p0056-b0006`: VLM read `12,897` vs PDF OCR witness `['12397']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `32` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `5` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`22` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"HC 437 P8W5"*
  - Leaf `1` `p0001-b0002` (`scanner_residue`): *"UC-NRLF $B 691 361"*
  - Leaf `1` `p0001-b0003` (`scanner_residue`): *"Orange circular library sticker"*
  - Leaf `1` `p0001-b0004` (`scanner_residue`): *"YD 06248"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"University of California bookplate (SIGILLVM · VNIVERSITATIS · CALIFORNIENSIS MDCCCLXVIII "*
  - Leaf `3` `p0003-b0003` (`scanner_residue`): *"UNIV. OF CALIFORNIA"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"HC437 P8 W5"*
  - Leaf `4` `p0004-b0003` (`scanner_residue`): *"Perforated library accession stamp"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"UNIV. OF CALIFORNIA"*
  - Leaf `5` `p0005-b0004` (`scanner_residue`): *"M43399"*
  - Leaf `6` `p0006-b0004` (`scanner_residue`): *"Perforated library stamp"*
  - Leaf `7` `p0007-b0007` (`noise`): *"B"*
- **Unattested Line-Wrap Hyphenation Decisions (`9` unique words out of `96` total wraps)**: `Lieutenant-Governor` (p.6), `harnessed` (p.6), `excluding` (p.11), `whatever` (p.16), `attaining` (p.19), `trainload` (p.21), `shopkeeping` (p.36), `indebtedness` (p.43), `instruction` (p.45)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 90,322 chars
- **Distinct Non-ASCII Glyphs (`4` across `28` leaves)**: · ⁄ ⅓ ⅛
- **Corrections Replayed**: `2` applied, `0` orphaned/unmatched
