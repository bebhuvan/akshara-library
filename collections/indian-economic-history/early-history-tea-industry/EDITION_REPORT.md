# Edition Verification & Run Audit — *The Early History of the Tea Industry in North-East India*

- **Book ID**: `early-history-tea-industry` | **Run ID**: `g38-canonical-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`97.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 40 of 40 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `40` extracted, `4` blank/tissue, `0` failed (of `44` PDF leaves)
- **Tracked API Spend**: **`$0.2455`** (`77.4%` cached input tokens: `306,240` / `395,631` in, `41,477` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **22.0 / 25.0** | -3.0: 1 unresolved footnote callout/body mismatch(es) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Resolve 1 unmatched footnote marker(s) via anchor-matched corrections.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract` | 40 | `$0.2455` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 40 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `44`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`5` — catches smudged dates/figures in prose)**:
  - Leaf `38` `p0038-b0006`: VLM read `1853` vs PDF OCR witness `['1852']`
  - Leaf `38` `p0038-b0007`: VLM read `1854` vs PDF OCR witness `['1852']`
  - Leaf `38` `p0038-b0008`: VLM read `1855` vs PDF OCR witness `['1852']`
  - Leaf `38` `p0038-b0009`: VLM read `1856` vs PDF OCR witness `['1852']`
  - Leaf `38` `p0038-b0010`: VLM read `1856` vs PDF OCR witness `['1852']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `28` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `45` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`8` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"HD 9198 M 28"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Cornell University Library HD 9198.M28 The early history of the tea industry in 3 1924 013"*
  - Leaf `3` `p0003-b0005` (`noise`): *"CS"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"@ HD9198 M28"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"@ 83248"*
  - Leaf `5` `p0005-b0006` (`scanner_residue`): *"X."*
  - Leaf `10` `p0010-b0004` (`noise`): *"—"*
  - Leaf `12` `p0012-b0010` (`noise`): *"—"*
- **Unattested Line-Wrap Hyphenation Decisions (`11` unique words out of `32` total wraps)**: `opportunities` (p.5), `expedition` (p.9), `situation` (p.13), `Gubru-purbut` (p.13), `inundations` (p.13), `plantation` (p.14), `excellent` (p.16), `twentynine` (p.17), `approximate` (p.20), `calculations` (p.30), `inevitable` (p.34)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 55,786 chars
- **Distinct Non-ASCII Glyphs (`3` across `6` leaves)**: · é „
- **Corrections Replayed**: `7` applied, `0` orphaned/unmatched
