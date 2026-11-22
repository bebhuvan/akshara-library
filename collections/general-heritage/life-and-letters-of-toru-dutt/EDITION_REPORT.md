# Edition Verification & Run Audit — *Life and Letters of Toru Dutt*

- **Book ID**: `life-and-letters-of-toru-dutt` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 398 of 398 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `398` extracted, `10` blank/tissue, `0` failed (of `408` PDF leaves)
- **Tracked API Spend**: **`$6.5664`** (`2.3%` cached input tokens: `106,496` / `4,572,385` in, `462,472` out, `396,787` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 0.8% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 398 | `$6.5572` |
| `continuation_arbiter_batch` | 6 | `$0.0092` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 398 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `185, 349`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`6` — catches smudged dates/figures in prose)**:
  - Leaf `400` `p0400-b0010`: VLM read `254` vs PDF OCR witness `['204', '234', '244']`
  - Leaf `401` `p0401-b0027`: VLM read `269` vs PDF OCR witness `['209', '239', '249']`
  - Leaf `401` `p0401-b0046`: VLM read `267` vs PDF OCR witness `['167', '217', '237']`
  - Leaf `401` `p0401-b0046`: VLM read `274` vs PDF OCR witness `['174', '204', '234']`
  - Leaf `404` `p0404-b0011`: VLM read `110` vs PDF OCR witness `['100', '111', '114']`
  - Leaf `404` `p0404-b0011`: VLM read `234` vs PDF OCR witness `['236', '237']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `239` prose joins, `1` split footnotes stitched, `0` multi-page tables unified, `72` total footnotes.
  - Stitched cross-page footnotes: p.359->p.360 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`58` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 06610619 6"*
  - Leaf `9` `p0009-b0001` (`scanner_residue`): *"D979 Yd"*
  - Leaf `9` `p0009-b0003` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `9` `p0009-b0008` (`scanner_residue`): *"163422 21/7/21"*
  - Leaf `10` `p0010-b0001` (`scanner_residue`): *"Embossed circular University of Toronto Library stamp (in reverse)"*
  - Leaf `10` `p0010-b0002` (`scanner_residue`): *"PR 9499 .2 D88Z5 1921"*
  - Leaf `23` `p0023-b0005` (`noise`): *"B"*
  - Leaf `25` `p0025-b0005` (`noise`): *"B 2"*
  - Leaf `43` `p0043-b0005` (`noise`): *"c"*
  - Leaf `47` `p0047-b0008` (`noise`): *"c 2"*
  - Leaf `61` `p0061-b0015` (`noise`): *"D"*
  - Leaf `63` `p0063-b0017` (`noise`): *"d 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`81` unique words out of `390` total wraps)**: `Bholanath` (p.31), `transplant` (p.31), `Atonement` (p.33), `assistance` (p.34), `prophetic` (p.36), `commendatory` (p.36), `Jivan-Sandhya` (p.41), `fruittrees` (p.44), `superiority` (p.52), `stagestruck` (p.55), `therefrom` (p.74), `trèsintéressante` (p.77), `connaissent` (p.78), `défenseurs` (p.80), `particulièrement` (p.80), `shareholder` (p.88), `overflow` (p.93), `accompanying` (p.98)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 569,799 chars
- **Distinct Non-ASCII Glyphs (`17` across `164` leaves)**: À Ê à â ç è é ê ë î ï ñ ô ù û ü œ
- **Corrections Replayed**: `11` applied, `0` orphaned/unmatched
