# Edition Verification & Run Audit — *Speeches and Writings of Sarojini Naidu*

- **Book ID**: `speeches-writings-sarojini-naidu` | **Run ID**: `g38-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 486 of 486 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `486` extracted, `4` blank/tissue, `0` failed (of `490` PDF leaves)
- **Tracked API Spend**: **`$1.4669`** (`77.6%` cached input tokens: `3,887,514` / `5,008,100` in, `480,186` out, `269` thoughts)

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
| `page_extract_batch` | 486 | `$1.4403` |
| `continuation_arbiter_batch` | 23 | `$0.0265` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 486 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`6` — catches smudged dates/figures in prose)**:
  - Leaf `483` `p0483-b0005`: VLM read `312` vs PDF OCR witness `['315', '372', '382']`
  - Leaf `483` `p0483-b0008`: VLM read `409` vs PDF OCR witness `['309', '404', '439']`
  - Leaf `484` `p0484-b0050`: VLM read `120` vs PDF OCR witness `['110', '125', '126']`
  - Leaf `485` `p0485-b0007`: VLM read `377` vs PDF OCR witness `['317', '370', '375']`
  - Leaf `485` `p0485-b0078`: VLM read `208` vs PDF OCR witness `['203', '205']`
  - Leaf `486` `p0486-b0049`: VLM read `111` vs PDF OCR witness `['131', '411']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `262` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `0` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`141` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00582123 6"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2008 with funding from Microsoft Corporation"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"http://www.archive.org/details/speecheswritings00naiduoft"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"DS 481. N25 A 56 19--"*
  - Leaf `8` `p0008-b0002` (`scanner_residue`): *"LIBRARY MAY - 6 1971 UNIVERSITY OF TORONTO"*
  - Leaf `9` `p0009-b0002` (`noise`): *"—"*
  - Leaf `11` `p0011-b0002` (`noise`): *"—"*
  - Leaf `11` `p0011-b0004` (`noise`): *"—"*
  - Leaf `12` `p0012-b0039` (`noise`): *"———"*
  - Leaf `23` `p0023-b0009` (`noise`): *"ii"*
  - Leaf `38` `p0038-b0007` (`noise`): *"————"*
  - Leaf `39` `p0039-b0005` (`noise`): *"* * * * * *"*
- **Unattested Line-Wrap Hyphenation Decisions (`104` unique words out of `874` total wraps)**: `Brahmanagaram` (p.13), `transported` (p.16), `passionateness` (p.16), `rhythmic` (p.17), `humanitarian` (p.17), `womenmartyrs` (p.21), `proscribed` (p.24), `demonstrations` (p.24), `Montagu-Chelmsford` (p.25), `enfranchisement` (p.25), `contended` (p.29), `henceforward` (p.29), `Swarajists` (p.33), `susceptibilities` (p.37), `alternative` (p.38), `onyxcoloured` (p.39), `slumberous` (p.39), `unfathomably` (p.39)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 629,577 chars
- **Distinct Non-ASCII Glyphs (`4` across `8` leaves)**: â æ ə „
- **Corrections Replayed**: `17` applied, `0` orphaned/unmatched
