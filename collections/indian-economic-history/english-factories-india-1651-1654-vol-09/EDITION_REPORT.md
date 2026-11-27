# Edition Verification & Run Audit — *The English Factories in India, 1651–1654*

- **Book ID**: `english-factories-india-1651-1654-vol-09` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 367 of 368 pages, gemini-3.6-flash on 1 of 368 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `368` extracted, `6` blank/tissue, `0` failed (of `374` PDF leaves)
- **Tracked API Spend**: **`$1.8734`** (`70.5%` cached input tokens: `2,942,896` / `4,176,294` in, `567,982` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 1.4% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 347 | `$1.3039` |
| `primary_quality_retry` | 21 | `$0.2782` |
| `recitation_band_bot` | 8 | `$0.0879` |
| `page_extract_batch_vetoed` | 21 | `$0.0846` |
| `recitation_band_top` | 8 | `$0.0810` |
| `continuation_arbiter_batch` | 18 | `$0.0258` |
| `secondary_gemini_rescue` | 1 | `$0.0119` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 1 pp., `gemini-3.8-flash`: 367 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `56` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `77` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `87` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `111` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `192` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `232` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `291` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`143` — catches smudged dates/figures in prose)**:
  - Leaf `15` `p0015-b0007`: VLM read `1660` vs PDF OCR witness `['1665']`
  - Leaf `16` `p0016-b0003`: VLM read `116` vs PDF OCR witness `['118']`
  - Leaf `23` `p0023-b0003`: VLM read `212` vs PDF OCR witness `['211', '218', '312']`
  - Leaf `27` `p0027-b0004`: VLM read `281` vs PDF OCR witness `['381']`
  - Leaf `28` `p0028-b0005`: VLM read `1651` vs PDF OCR witness `['1654']`
  - Leaf `31` `p0031-b0003`: VLM read `532` vs PDF OCR witness `['539']`
  - Leaf `31` `p0031-b0004`: VLM read `1652` vs PDF OCR witness `['1650', '1651']`
  - Leaf `32` `p0032-b0003`: VLM read `1652` vs PDF OCR witness `['1642', '1650', '1651']`
  - Leaf `39` `p0039-b0005`: VLM read `551` vs PDF OCR witness `['550']`
  - Leaf `40` `p0040-b0003`: VLM read `556` vs PDF OCR witness `['550', '551']`
  - Leaf `47` `p0047-b0003`: VLM read `2132` vs PDF OCR witness `['3132']`
  - Leaf `71` `p0071-b0005`: VLM read `2203` vs PDF OCR witness `['2303']`
  - Leaf `77` `p0077-b0003`: VLM read `216` vs PDF OCR witness `['212']`
  - Leaf `111` `p0111-b0005`: VLM read `1652` vs PDF OCR witness `['1650', '1651', '1653']`
  - Leaf `125` `p0125-b0003`: VLM read `1652` vs PDF OCR witness `['1651', '1653']`
  - Leaf `125` `p0125-b0004`: VLM read `2238` vs PDF OCR witness `['3238']`
  - Leaf `136` `p0136-b0004`: VLM read `1651` vs PDF OCR witness `['1650']`
  - Leaf `167` `p0167-b0003`: VLM read `6,000` vs PDF OCR witness `['1000', '4000']`
  - Leaf `167` `p0167-b0005`: VLM read `120,` vs PDF OCR witness `['121']`
  - Leaf `175` `p0175-b0004`: VLM read `2274` vs PDF OCR witness `['2374']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `176` prose joins, `6` split footnotes stitched, `0` multi-page tables unified, `368` total footnotes.
  - Stitched cross-page footnotes: p.68->p.69 (`3`), p.113->p.114 (`3`), p.135->p.136 (`1`), p.149->p.150 (`1`), p.227->p.228 (`4`), p.250->p.251 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`79` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 08381416 0"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2010 with funding from University of Toronto"*
  - Leaf `5` `p0005-b0002` (`scanner_residue`): *"http://www.archive.org/details/englishfactories09fost"*
  - Leaf `6` `p0006-b0003` (`noise`): *"Front. E.F. IX."*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"[Call number label at top left]"*
  - Leaf `7` `p0007-b0002` (`scanner_residue`): *"[Vol. 9]"*
  - Leaf `7` `p0007-b0005` (`scanner_residue`): *"[Embossed circular library stamp of the University of Toronto Library]"*
  - Leaf `7` `p0007-b0008` (`scanner_residue`): *"137125- 15/11/15-"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed library stamp of University of Toronto"*
  - Leaf `9` `p0009-b0005` (`noise`): *"a 2"*
  - Leaf `23` `p0023-b0006` (`noise`): *"FOSTER IX"*
  - Leaf `23` `p0023-b0007` (`noise`): *"b"*
- **Unattested Line-Wrap Hyphenation Decisions (`73` unique words out of `678` total wraps)**: `utilization` (p.10), `foreboded` (p.11), `supporting` (p.16), `considerably` (p.25), `aggrandisement` (p.42), `overboard` (p.47), `withholding` (p.47), `extreamity` (p.48), `demeanour` (p.49), `reconsiled` (p.49), `summoning` (p.50), `overlayd` (p.60), `injustice` (p.68), `inconveniencies` (p.69), `appropriating` (p.70), `preperations` (p.73), `interpreted` (p.79), `Lieutenant` (p.89)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 671,625 chars, `arabic`: 7 chars, `cyrillic`: 3 chars
- **Distinct Non-ASCII Glyphs (`32` across `306` leaves)**: É Ø á â ã ç è é ö Ā ā ġ ħ Ī ī ō ū б о ъ ج ر ل م ي ہ Ḥ ṛ ⁄ ⁱ ⅛ ⅝
- **Corrections Replayed**: `9` applied, `0` orphaned/unmatched
