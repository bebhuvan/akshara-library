# Edition Verification & Run Audit — *The Indian Craftsman*

- **Book ID**: `the-indian-craftsman` | **Run ID**: `g38-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 153 of 153 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `153` extracted, `7` blank/tissue, `0` failed (of `160` PDF leaves)
- **Tracked API Spend**: **`$0.4521`** (`77.1%` cached input tokens: `1,239,845` / `1,607,177` in, `139,842` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 7.2% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 151 | `$0.4181` |
| `continuation_arbiter_batch` | 11 | `$0.0151` |
| `primary_quality_retry` | 2 | `$0.0113` |
| `page_extract_batch_vetoed` | 2 | `$0.0076` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 153 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`1` — catches smudged dates/figures in prose)**:
  - Leaf `67` `p0067-b0004`: VLM read `111` vs PDF OCR witness `['112']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `93` prose joins, `4` split footnotes stitched, `0` multi-page tables unified, `63` total footnotes.
  - Stitched cross-page footnotes: p.25->p.26 (`*`), p.33->p.34 (`†`), p.92->p.93 (`†`), p.94->p.95 (`†`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`25` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 01594448 1"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2007 with funding from Microsoft Corporation"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"http://www.archive.org/details/indiancraftsman00coomuoft"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"HD 2346 I 5 C 6"*
  - Leaf `8` `p0008-b0002` (`scanner_residue`): *"LIBRARY MAR 27 1972 UNIVERSITY OF TORONTO"*
  - Leaf `10` `p0010-b0002` (`noise`): *"—"*
  - Leaf `21` `p0021-b0006` (`noise`): *"B"*
  - Leaf `24` `p0024-b0006` (`noise`): *"2"*
  - Leaf `37` `p0037-b0006` (`noise`): *"C"*
  - Leaf `53` `p0053-b0006` (`noise`): *"D"*
  - Leaf `69` `p0069-b0010` (`noise`): *"E"*
  - Leaf `85` `p0085-b0007` (`noise`): *"F"*
- **Unattested Line-Wrap Hyphenation Decisions (`48` unique words out of `148` total wraps)**: `thoughtlessness` (p.13), `shortsighted` (p.13), `constitutions` (p.14), `somehow` (p.15), `unconsciously` (p.16), `Pre-Raphaelites` (p.16), `reconstruction` (p.18), `greensickness` (p.20), `composed` (p.30), `Chautano-Seth` (p.31), `helpless` (p.31), `sentiment` (p.33), `condemnation` (p.34), `gemcutters` (p.36), `shebuffaloes` (p.39), `Mabinogion` (p.42), `footsteps` (p.44), `Musalmān` (p.46)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 143,670 chars
- **Distinct Non-ASCII Glyphs (`11` across `65` leaves)**: æ é ñ ü Ā ā ē ī ō ś ū
- **Corrections Replayed**: `21` applied, `0` orphaned/unmatched
