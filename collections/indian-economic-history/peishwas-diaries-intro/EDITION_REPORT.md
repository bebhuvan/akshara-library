# Edition Verification & Run Audit — *Introduction to the Peishwa's Diaries*

- **Book ID**: `peishwas-diaries-intro` | **Run ID**: `g38-canonical-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 48 of 48 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `48` extracted, `0` blank/tissue, `0` failed (of `48` PDF leaves)
- **Tracked API Spend**: **`$0.3367`** (`77.6%` cached input tokens: `367,488` / `473,437` in, `39,309` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 18.8% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract` | 48 | `$0.2544` |
| `continuation_arbiter` | 21 | `$0.0822` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 48 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`1` — catches smudged dates/figures in prose)**:
  - Leaf `25` `p0025-b0006`: VLM read `55,000` vs PDF OCR witness `['35000', '55030']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `28` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `0` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`9` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"DS 432 M2R3"*
  - Leaf `1` `p0001-b0002` (`scanner_residue`): *"UC-NRLF $B 573 952"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"LIBRARY"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"DS 432 M2 R3"*
  - Leaf `5` `p0005-b0004` (`noise`): *"—————————✤—————————"*
  - Leaf `42` `p0042-b0003` (`noise`): *"————0————"*
  - Leaf `46` `p0046-b0001` (`scanner_residue`): *"14 DAY USE RETURN TO DESK FROM WHICH BORROWED LOAN DEPT. This book is due on the last date"*
  - Leaf `46` `p0046-b0002` (`scanner_residue`): *"6"*
  - Leaf `47` `p0047-b0001` (`scanner_residue`): *"Gaylord GAYLAMOUNT® PAMPHLET BINDER Syracuse, N.Y. Stockton, Calif."*
- **Unattested Line-Wrap Hyphenation Decisions (`26` unique words out of `80` total wraps)**: `prevail` (p.6), `circumstances` (p.6), `transferring` (p.9), `dimunition` (p.10), `exerted` (p.12), `exclusively` (p.13), `Ibrahim-khan` (p.16), `underwent` (p.17), `headquarters` (p.18), `contingencies` (p.21), `Ganga-thadi` (p.22), `improvement` (p.24), `shoptax` (p.24), `banishment` (p.27), `householders` (p.31), `dispatched` (p.32), `maintenanceallowances` (p.32), `entirely` (p.34)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 64,536 chars
- **Distinct Non-ASCII Glyphs (`5` across `4` leaves)**: á â ⅓ ⅖ ⅗
- **Corrections Replayed**: `10` applied, `0` orphaned/unmatched
