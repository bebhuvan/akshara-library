# Edition Verification & Run Audit — *The Truth About Indian Opium*

- **Book ID**: `truth-about-indian-opium` | **Run ID**: `g38-canonical-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 50 of 50 pages. Declared reader profile: tables (new readings use gemini-4-hydrogen). This edition predates that choice and has not been re-read with gemini-4-hydrogen.
- **Pages**: `50` extracted, `0` blank/tissue, `0` failed (of `50` PDF leaves)
- **Tracked API Spend**: **`$0.4822`** (`77.7%` cached input tokens: `382,800` / `492,541` in, `93,132` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 16.0% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract` | 50 | `$0.4603` |
| `continuation_arbiter` | 4 | `$0.0219` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 50 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `31, 48`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`8` — catches smudged dates/figures in prose)**:
  - Leaf `6` `p0006-b0005`: VLM read `1893` vs PDF OCR witness `['1813', '1895']`
  - Leaf `11` `p0011-b0006`: VLM read `488,548` vs PDF OCR witness `['188548']`
  - Leaf `12` `p0012-b0019`: VLM read `1919` vs PDF OCR witness `['1909', '1910', '1911']`
  - Leaf `15` `p0015-b0007`: VLM read `8,496` vs PDF OCR witness `['8490']`
  - Leaf `15` `p0015-b0008`: VLM read `1913` vs PDF OCR witness `['1911', '1912', '1914']`
  - Leaf `15` `p0015-b0008`: VLM read `1,356,066` vs PDF OCR witness `['1356060']`
  - Leaf `30` `p0030-b0002`: VLM read `14,000` vs PDF OCR witness `['11000', '16000']`
  - Leaf `43` `p0043-b0003`: VLM read `1921` vs PDF OCR witness `['1021']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `28` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `10` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`30` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"HV 5816 G7 1922"*
  - Leaf `1` `p0001-b0002` (`scanner_residue`): *"UC-NRLF $B 47 182"*
  - Leaf `1` `p0001-b0003` (`scanner_residue`): *"DOCUMENTS DEPT."*
  - Leaf `1` `p0001-b0004` (`scanner_residue`): *"Yellow circular sticker"*
  - Leaf `1` `p0001-b0005` (`scanner_residue`): *"35790"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"GIFT OF SIGILLVM VNIVERSITATIS CALIFORNIENSIS FIAT LVX MDCCCLXVIII EX LIBRIS DOCUMENTS DEP"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"UNIV. OF CALIFORNIA GIFT MAY 29 1922"*
  - Leaf `3` `p0003-b0006` (`scanner_residue`): *"LIBRARY OF THE UNIVERSITY OF CALIFORNIA"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"TO VIMU AIMROTLIAO"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"HV 5816 G7 1922"*
  - Leaf `4` `p0004-b0004` (`scanner_residue`): *"DOCUMENTS DEPT."*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"CALIFORNIA"*
- **Unattested Line-Wrap Hyphenation Decisions (`9` unique words out of `66` total wraps)**: `connected` (p.6), `quasireligious` (p.7), `transactions` (p.9), `transportation` (p.22), `wellto` (p.25), `progressively` (p.26), `Indo-China` (p.30), `attainment` (p.42), `statements` (p.45)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 86,529 chars
- **Distinct Non-ASCII Glyphs (`6` across `6` leaves)**: · â æ è û ⅗
- **Corrections Replayed**: `6` applied, `0` orphaned/unmatched
