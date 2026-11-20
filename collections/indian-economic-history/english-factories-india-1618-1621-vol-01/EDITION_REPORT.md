# Edition Verification & Run Audit — *The English Factories in India, 1618–1621*

- **Book ID**: `english-factories-india-1618-1621-vol-01` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 435 of 435 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `435` extracted, `3` blank/tissue, `0` failed (of `438` PDF leaves)
- **Tracked API Spend**: **`$2.4051`** (`70.2%` cached input tokens: `3,445,133` / `4,904,645` in, `738,427` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 1.8% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 404 | `$1.5695` |
| `primary_quality_retry` | 21 | `$0.3159` |
| `recitation_retry` | 11 | `$0.2111` |
| `page_extract_batch_vetoed` | 20 | `$0.0928` |
| `recitation_band_bot` | 7 | `$0.0720` |
| `recitation_band_top` | 7 | `$0.0701` |
| `continuation_arbiter_batch` | 21 | `$0.0423` |
| `blind_totals_strip` | 5 | `$0.0189` |
| `page_extract_batch_failed` | 11 | `$0.0124` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 435 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `150` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `156` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `162` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `203` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `233` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `395` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `410` via `recitation_2band_split` (`gemini-3.8-flash`)
- **450-DPI Blind Totals Strip Disagreements (`1`)**:
  - Leaf `318` `p0318-b0011`: full-page `['', '1705.', '12.', '0<fraction>11/16</fraction>']` vs blind-strip `['', '1705.', '12.', '0<sup>11</sup>/<sub>16</sub>']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`157` — catches smudged dates/figures in prose)**:
  - Leaf `11` `p0011-b0002`: VLM read `1618` vs PDF OCR witness `['1616']`
  - Leaf `11` `p0011-b0004`: VLM read `1617` vs PDF OCR witness `['1616']`
  - Leaf `12` `p0012-b0004`: VLM read `1618` vs PDF OCR witness `['1612']`
  - Leaf `14` `p0014-b0004`: VLM read `1619` vs PDF OCR witness `['1618']`
  - Leaf `16` `p0016-b0003`: VLM read `1618` vs PDF OCR witness `['1616', '1617', '1619']`
  - Leaf `16` `p0016-b0004`: VLM read `1618` vs PDF OCR witness `['1616', '1617', '1619']`
  - Leaf `17` `p0017-b0004`: VLM read `1616` vs PDF OCR witness `['1610', '1615', '1618']`
  - Leaf `19` `p0019-b0006`: VLM read `622` vs PDF OCR witness `['632']`
  - Leaf `23` `p0023-b0004`: VLM read `1617` vs PDF OCR witness `['1619']`
  - Leaf `27` `p0027-b0003`: VLM read `1619` vs PDF OCR witness `['1614']`
  - Leaf `42` `p0042-b0003`: VLM read `1621` vs PDF OCR witness `['1631']`
  - Leaf `43` `p0043-b0003`: VLM read `1619` vs PDF OCR witness `['1618']`
  - Leaf `44` `p0044-b0005`: VLM read `1617` vs PDF OCR witness `['1618']`
  - Leaf `45` `p0045-b0003`: VLM read `1617` vs PDF OCR witness `['1618']`
  - Leaf `51` `p0051-b0003`: VLM read `1618` vs PDF OCR witness `['1616', '1619']`
  - Leaf `51` `p0051-b0003`: VLM read `1618` vs PDF OCR witness `['1616', '1619']`
  - Leaf `53` `p0053-b0003`: VLM read `1616` vs PDF OCR witness `['1614']`
  - Leaf `53` `p0053-b0003`: VLM read `1617` vs PDF OCR witness `['1614']`
  - Leaf `75` `p0075-b0003`: VLM read `1618` vs PDF OCR witness `['1615']`
  - Leaf `75` `p0075-b0004`: VLM read `1618` vs PDF OCR witness `['1615']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `206` prose joins, `11` split footnotes stitched, `2` multi-page tables unified, `658` total footnotes.
  - Stitched cross-page footnotes: p.26->p.27 (`1`), p.30->p.31 (`1`), p.65->p.66 (`1`), p.107->p.108 (`4`), p.113->p.114 (`1`), p.118->p.119 (`5`), p.253->p.254 (`3`), p.282->p.283 (`1`), p.309->p.310 (`2`), p.339->p.340 (`6`), p.352->p.353 (`2`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`85` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 08381422 8"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2010 with funding from University of Toronto"*
  - Leaf `3` `p0003-b0002` (`scanner_residue`): *"http://www.archive.org/details/englishfactories01fost"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"Embossed circular library stamp of the University of Toronto Library."*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed circular library stamp of the University of Toronto"*
  - Leaf `22` `p0022-b0005` (`scanner_residue`): *"J"*
  - Leaf `23` `p0023-b0005` (`noise`): *"FOSTER"*
  - Leaf `23` `p0023-b0006` (`noise`): *"b"*
  - Leaf `25` `p0025-b0005` (`noise`): *"b 2"*
  - Leaf `39` `p0039-b0006` (`noise`): *"foster"*
  - Leaf `39` `p0039-b0007` (`noise`): *"c"*
  - Leaf `41` `p0041-b0004` (`noise`): *"c 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`80` unique words out of `607` total wraps)**: `superintendence` (p.10), `empowering` (p.12), `compliance` (p.13), `lastnamed` (p.17), `whichever` (p.28), `consolation` (p.37), `persistent` (p.39), `helplessly` (p.47), `Dansborg` (p.51), `weakness` (p.52), `Warehousekeeper` (p.52), `fabulousreal` (p.54), `Gehangier` (p.58), `Gulkhandah` (p.74), `embrodred` (p.75), `acknowledgeth` (p.76), `enviously` (p.76), `gloriously` (p.80)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 755,839 chars, `katakana`: 3 chars, `han`: 3 chars, `hiragana`: 2 chars
- **Distinct Non-ASCII Glyphs (`44` across `333` leaves)**: à â ã ä æ ç è é ï ô Ā ā ē ġ ģ ĩ Ī ī ō š ţ ť ū ſ ̃ ḍ ṇ ṛ ṭ ′ ⁄ ⁱ ⅓ ⅔ ⅛ ⅜ ⅝ ⅞ を イ ス ン 数 旪
- **Corrections Replayed**: `18` applied, `0` orphaned/unmatched
