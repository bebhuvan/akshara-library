# Edition Verification & Run Audit — *A Comprehensive History of India, Vol. II*

- **Book ID**: `comprehensive-history-india-v2` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 876 of 876 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `876` extracted, `16` blank/tissue, `0` failed (of `892` PDF leaves)
- **Tracked API Spend**: **`$16.6956`** (`2.3%` cached input tokens: `241,230` / `10,275,254` in, `1,340,587` out, `1,147,847` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 0.2% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 876 | `$16.5250` |
| `continuation_arbiter_batch` | 80 | `$0.1706` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 876 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `8, 20, 21, 23, 25, 27`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`156` — catches smudged dates/figures in prose)**:
  - Leaf `17` `p0017-b0061`: VLM read `172` vs PDF OCR witness `['171', '173', '175']`
  - Leaf `17` `p0017-b0066`: VLM read `197` vs PDF OCR witness `['147', '191']`
  - Leaf `38` `p0038-b0007`: VLM read `4,320,000` vs PDF OCR witness `['4820000']`
  - Leaf `45` `p0045-b0008`: VLM read `156` vs PDF OCR witness `['150']`
  - Leaf `52` `p0052-b0013`: VLM read `129` vs PDF OCR witness `['120']`
  - Leaf `58` `p0058-b0006`: VLM read `330,000,000` vs PDF OCR witness `['830000000']`
  - Leaf `91` `p0091-b0008`: VLM read `3000` vs PDF OCR witness `['8000']`
  - Leaf `158` `p0158-b0009`: VLM read `290` vs PDF OCR witness `['291']`
  - Leaf `183` `p0183-b0007`: VLM read `333` vs PDF OCR witness `['833']`
  - Leaf `184` `p0184-b0006`: VLM read `100` vs PDF OCR witness `['000']`
  - Leaf `196` `p0196-b0006`: VLM read `3,655,534` vs PDF OCR witness `['3055534']`
  - Leaf `196` `p0196-b0006`: VLM read `79,600` vs PDF OCR witness `['79000']`
  - Leaf `198` `p0198-b0006`: VLM read `9,633,371` vs PDF OCR witness `['9033371']`
  - Leaf `198` `p0198-b0006`: VLM read `1,821,653` vs PDF OCR witness `['1821053']`
  - Leaf `200` `p0200-b0010`: VLM read `1,070,068` vs PDF OCR witness `['1070008']`
  - Leaf `209` `p0209-b0012`: VLM read `335` vs PDF OCR witness `['325']`
  - Leaf `265` `p0265-b0004`: VLM read `1760` vs PDF OCR witness `['1700']`
  - Leaf `265` `p0265-b0010`: VLM read `1760` vs PDF OCR witness `['1700']`
  - Leaf `270` `p0270-b0004`: VLM read `1762` vs PDF OCR witness `['1702']`
  - Leaf `270` `p0270-b0009`: VLM read `1762` vs PDF OCR witness `['1702']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `745` prose joins, `2` split footnotes stitched, `0` multi-page tables unified, `89` total footnotes.
  - Stitched cross-page footnotes: p.739->p.740 (`1`), p.741->p.742 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`234` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Miss. Hist"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"Toronto University Library Presented by Messrs Blackie & Sons through the Committee formed"*
  - Leaf `11` `p0011-b0001` (`scanner_residue`): *"HIn. B5714C"*
  - Leaf `11` `p0011-b0003` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `12` `p0012-b0001` (`scanner_residue`): *"Embossed library stamp: UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `12` `p0012-b0002` (`scanner_residue`): *"Handwritten accession mark: 10665 / 3/12/90 e"*
  - Leaf `13` `p0013-b0018` (`noise`): *"—"*
  - Leaf `17` `p0017-b0099` (`noise`): *"Vol. II."*
  - Leaf `17` `p0017-b0100` (`noise`): *"b"*
  - Leaf `37` `p0037-b0010` (`noise`): *"VOL. II."*
  - Leaf `45` `p0045-b0011` (`noise`): *"Vol. II."*
  - Leaf `45` `p0045-b0012` (`noise`): *"91"*
- **Unattested Line-Wrap Hyphenation Decisions (`126` unique words out of `3878` total wraps)**: `Brahmachari` (p.41), `dogliving` (p.42), `depositaries` (p.48), `numberless` (p.56), `monotheists` (p.57), `Swayambhu` (p.60), `Glorified` (p.61), `unhabitable` (p.63), `fascinated` (p.63), `prophecy` (p.66), `Hastinapur` (p.67), `dishevelled` (p.68), `Bindabashni` (p.69), `sugarcandy` (p.74), `contraction` (p.79), `cynosuroides` (p.79), `theologians` (p.81), `distortion` (p.82)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 2,137,707 chars
- **Distinct Non-ASCII Glyphs (`10` across `57` leaves)**: · Æ æ ç è é ô ù œ ″
- **Corrections Replayed**: `33` applied, `0` orphaned/unmatched
