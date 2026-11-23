# Edition Verification & Run Audit — *A Comprehensive History of India, Vol. I*

- **Book ID**: `comprehensive-history-india-v1` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 733 of 733 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `733` extracted, `13` blank/tissue, `0` failed (of `746` PDF leaves)
- **Tracked API Spend**: **`$14.1172`** (`3.4%` cached input tokens: `296,133` / `8,607,391` in, `1,145,338` out, `986,783` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 0.3% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 733 | `$13.9440` |
| `continuation_arbiter_batch` | 63 | `$0.1396` |
| `blind_totals_strip` | 3 | `$0.0335` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 733 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `8, 22, 23, 29`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`250` — catches smudged dates/figures in prose)**:
  - Leaf `16` `p0016-b0019`: VLM read `281` vs PDF OCR witness `['251']`
  - Leaf `19` `p0019-b0007`: VLM read `1767` vs PDF OCR witness `['1707']`
  - Leaf `19` `p0019-b0049`: VLM read `117` vs PDF OCR witness `['107', '110', '113']`
  - Leaf `19` `p0019-b0075`: VLM read `196` vs PDF OCR witness `['136', '156', '190']`
  - Leaf `20` `p0020-b0005`: VLM read `243` vs PDF OCR witness `['240', '242', '253']`
  - Leaf `20` `p0020-b0006`: VLM read `1600` vs PDF OCR witness `['1000', '1650']`
  - Leaf `20` `p0020-b0006`: VLM read `245` vs PDF OCR witness `['240', '242', '295']`
  - Leaf `20` `p0020-b0009`: VLM read `257` vs PDF OCR witness `['250', '251', '253']`
  - Leaf `20` `p0020-b0010`: VLM read `1600` vs PDF OCR witness `['1000', '1650']`
  - Leaf `20` `p0020-b0010`: VLM read `259` vs PDF OCR witness `['209', '250', '251']`
  - Leaf `20` `p0020-b0011`: VLM read `261` vs PDF OCR witness `['201', '251']`
  - Leaf `20` `p0020-b0013`: VLM read `269` vs PDF OCR witness `['209']`
  - Leaf `20` `p0020-b0016`: VLM read `289` vs PDF OCR witness `['209', '282', '284']`
  - Leaf `20` `p0020-b0037`: VLM read `386` vs PDF OCR witness `['380', '381']`
  - Leaf `20` `p0020-b0056`: VLM read `459` vs PDF OCR witness `['409', '451', '455']`
  - Leaf `20` `p0020-b0057`: VLM read `462` vs PDF OCR witness `['402', '472']`
  - Leaf `20` `p0020-b0059`: VLM read `479` vs PDF OCR witness `['379', '409', '472']`
  - Leaf `20` `p0020-b0066`: VLM read `518` vs PDF OCR witness `['510', '538', '598']`
  - Leaf `20` `p0020-b0073`: VLM read `548` vs PDF OCR witness `['538', '543', '545']`
  - Leaf `20` `p0020-b0084`: VLM read `614` vs PDF OCR witness `['014', '314', '611']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `591` prose joins, `5` split footnotes stitched, `0` multi-page tables unified, `83` total footnotes.
  - Stitched cross-page footnotes: p.58->p.59 (`1`), p.79->p.80 (`1`), p.86->p.87 (`1`), p.107->p.108 (`1`), p.323->p.324 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`196` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 07590477 1"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2011 with funding from University of Toronto"*
  - Leaf `7` `p0007-b0002` (`scanner_residue`): *"http://www.archive.org/details/comprehensivehis01beve"*
  - Leaf `11` `p0011-b0001` (`scanner_residue`): *"HIn. B5714c"*
  - Leaf `11` `p0011-b0010` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `12` `p0012-b0001` (`scanner_residue`): *"Embossed University of Toronto Library stamp"*
  - Leaf `12` `p0012-b0002` (`scanner_residue`): *"Handwritten library accession marks: 10665 / 3/12/90, vols I to III"*
  - Leaf `16` `p0016-b0004` (`noise`): *"Page"*
  - Leaf `16` `p0016-b0010` (`noise`): *"—"*
  - Leaf `17` `p0017-b0015` (`noise`): *"Vol. I."*
  - Leaf `17` `p0017-b0016` (`noise`): *"b"*
  - Leaf `20` `p0020-b0054` (`noise`): *"I."*
- **Unattested Line-Wrap Hyphenation Decisions (`130` unique words out of `3213` total wraps)**: `perspicuous` (p.14), `delineated` (p.36), `monotonous` (p.38), `inundation` (p.39), `reappearing` (p.40), `thunderstorms` (p.43), `stillness` (p.44), `scavenger` (p.45), `peninsular` (p.47), `fulness` (p.48), `indubitable` (p.51), `immoveably` (p.51), `Artaxerxes` (p.54), `transcript` (p.54), `Erythræan` (p.54), `Disquisition` (p.55), `seawalls` (p.58), `Vicramaditya` (p.68)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 1,771,297 chars
- **Distinct Non-ASCII Glyphs (`10` across `67` leaves)**: · Æ æ ç è é ô ü œ „
- **Corrections Replayed**: `30` applied, `0` orphaned/unmatched
