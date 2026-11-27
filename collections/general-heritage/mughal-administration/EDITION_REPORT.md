# Edition Verification & Run Audit — *The Mughal Administration: Six Lectures*

- **Book ID**: `mughal-administration` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 88 of 88 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `88` extracted, `4` blank/tissue, `0` failed (of `92` PDF leaves)
- **Tracked API Spend**: **`$1.4759`** (`8.8%` cached input tokens: `89,345` / `1,010,713` in, `109,551` out, `98,861` thoughts)

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
| `page_extract_batch` | 88 | `$1.4481` |
| `continuation_arbiter_batch` | 4 | `$0.0278` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 88 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `4`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`4` — catches smudged dates/figures in prose)**:
  - Leaf `31` `p0031-b0008`: VLM read `6599` vs PDF OCR witness `['6598']`
  - Leaf `64` `p0064-b0007`: VLM read `169` vs PDF OCR witness `['167']`
  - Leaf `66` `p0066-b0003`: VLM read `1662` vs PDF OCR witness `['1062']`
  - Leaf `71` `p0071-b0025`: VLM read `163` vs PDF OCR witness `['162']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `42` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `23` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`11` — verify no epigraph/dedication was caught)**:
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"With the compliments of the Registrar,Patna University."*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"... Patna Un..."*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"S2457m"*
  - Leaf `7` `p0007-b0005` (`scanner_residue`): *"UNIVERSITY OF TORONTO"*
  - Leaf `7` `p0007-b0008` (`scanner_residue`): *"169860. 16. 3. 2"*
  - Leaf `9` `p0009-b0002` (`noise`): *"—"*
  - Leaf `9` `p0009-b0007` (`noise`): *"—"*
  - Leaf `9` `p0009-b0011` (`noise`): *"—"*
  - Leaf `9` `p0009-b0015` (`noise`): *"—"*
  - Leaf `10` `p0010-b0006` (`noise`): *"—"*
  - Leaf `91` `p0091-b0001` (`scanner_residue`): *"University of Toronto Library. DO NOT REMOVE THE CARD FROM THIS POCKET. Acme Library Card "*
- **Unattested Line-Wrap Hyphenation Decisions (`43` unique words out of `205` total wraps)**: `Hastings` (p.13), `individualistic` (p.13), `discharging` (p.13), `spectacular` (p.14), `capitalists` (p.17), `calculations` (p.17), `maintaining` (p.17), `gamblingdens` (p.29), `dancing` (p.30), `powdersupply` (p.32), `elephants` (p.38), `Karkaráqi` (p.38), `approval` (p.40), `tasdiqát` (p.40), `netweavers` (p.46), `kárkhánahs` (p.47), `safeguard` (p.48), `villagelife` (p.50)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 137,189 chars
- **Distinct Non-ASCII Glyphs (`6` across `44` leaves)**: á â æ ā œ ṛ
- **Corrections Replayed**: `3` applied, `0` orphaned/unmatched
