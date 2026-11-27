# Edition Verification & Run Audit — *A Guide to the India Office Records, 1600–1858*

- **Book ID**: `guide-to-india-office-records-1919` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 151 of 151 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `151` extracted, `5` blank/tissue, `0` failed (of `156` PDF leaves)
- **Tracked API Spend**: **`$0.7633`** (`76.5%` cached input tokens: `1,195,316` / `1,561,785` in, `309,886` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 0.0% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 151 | `$0.7465` |
| `continuation_arbiter_batch` | 8 | `$0.0168` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 151 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`71` — catches smudged dates/figures in prose)**:
  - Leaf `3` `p0003-b0004`: VLM read `1600` vs PDF OCR witness `['1000']`
  - Leaf `8` `p0008-b0029`: VLM read `123` vs PDF OCR witness `['103', '113', '121']`
  - Leaf `12` `p0012-b0004`: VLM read `1793` vs PDF OCR witness `['1791', '1795']`
  - Leaf `14` `p0014-b0002`: VLM read `1814` vs PDF OCR witness `['1811', '1816', '1884']`
  - Leaf `14` `p0014-b0002`: VLM read `1834` vs PDF OCR witness `['1838', '1884']`
  - Leaf `16` `p0016-b0003`: VLM read `1874` vs PDF OCR witness `['1875', '1879', '1884']`
  - Leaf `17` `p0017-b0008`: VLM read `1834` vs PDF OCR witness `['1884']`
  - Leaf `23` `p0023-b0003`: VLM read `1704` vs PDF OCR witness `['1700', '1701', '1702']`
  - Leaf `38` `p0038-b0012`: VLM read `1850` vs PDF OCR witness `['1854', '1855', '1857']`
  - Leaf `40` `p0040-b0015`: VLM read `1784` vs PDF OCR witness `['1781']`
  - Leaf `42` `p0042-b0010`: VLM read `1816` vs PDF OCR witness `['1814', '1836']`
  - Leaf `50` `p0050-b0005`: VLM read `734` vs PDF OCR witness `['732', '733', '735']`
  - Leaf `50` `p0050-b0011`: VLM read `740` vs PDF OCR witness `['760']`
  - Leaf `50` `p0050-b0012`: VLM read `741` vs PDF OCR witness `['711']`
  - Leaf `50` `p0050-b0012`: VLM read `1811` vs PDF OCR witness `['1813', '1814', '1815']`
  - Leaf `50` `p0050-b0013`: VLM read `742` vs PDF OCR witness `['732', '762']`
  - Leaf `50` `p0050-b0016`: VLM read `1849` vs PDF OCR witness `['1819', '1859']`
  - Leaf `51` `p0051-b0003`: VLM read `764` vs PDF OCR witness `['761', '765', '766']`
  - Leaf `51` `p0051-b0003`: VLM read `1884` vs PDF OCR witness `['1814', '1824']`
  - Leaf `52` `p0052-b0016`: VLM read `638` vs PDF OCR witness `['628', '630', '631']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `56` prose joins, `0` split footnotes stitched, `4` multi-page tables unified, `91` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`57` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00581942 0"*
  - Leaf `1` `p0001-b0002` (`scanner_residue`): *"DS Great Britain. India Office 465 A guide to the India A5 office records"*
  - Leaf `1` `p0001-b0003` (`scanner_residue`): *"DS 465 A5"*
  - Leaf `3` `p0003-b0012` (`scanner_residue`): *"6"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2008 with funding from Microsoft Corporation"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"http://www.archive.org/details/guidetoindiaoffi00greauoft"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"Indexing Branch"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"Indexing Br."*
  - Leaf `7` `p0007-b0010` (`scanner_residue`): *"BOOKS AND PERIODICALS AGENCY 3644 Goela House Chowk Mori Gate DELHI-110006 (INDIA)"*
  - Leaf `8` `p0008-b0002` (`noise`): *"—"*
  - Leaf `8` `p0008-b0030` (`noise`): *"—"*
  - Leaf `8` `p0008-b0031` (`scanner_residue`): *"LIBRARY MAR 1 1974 UNIVERSITY OF TORONTO"*
- **Unattested Line-Wrap Hyphenation Decisions (`9` unique words out of `177` total wraps)**: `disappointment` (p.11), `inconvenient` (p.14), `systematic` (p.31), `specifying` (p.31), `Collector-General` (p.64), `commencement` (p.67), `Secretary-General` (p.69), `Durgarayapatnam` (p.90), `occasional` (p.95)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 223,416 chars
- **Distinct Non-ASCII Glyphs (`8` across `8` leaves)**: · Ç Ô ã ç é ô ü
- **Corrections Replayed**: `2` applied, `0` orphaned/unmatched
