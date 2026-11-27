# Edition Verification & Run Audit — *Speeches and Writings of Dadabhai Naoroji*

- **Book ID**: `speeches-and-writings-naoroji-1918` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`92.4 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 920 of 920 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `920` extracted, `6` blank/tissue, `0` failed (of `926` PDF leaves)
- **Tracked API Spend**: **`$3.2127`** (`75.9%` cached input tokens: `7,282,720` / `9,590,831` in, `1,091,669` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **19.0 / 25.0** | -6.0: 2 unresolved footnote callout/body mismatch(es) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **23.4 / 25.0** | -1.6: 8 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Resolve 2 unmatched footnote marker(s) via anchor-matched corrections.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 920 | `$3.0441` |
| `continuation_arbiter_batch` | 80 | `$0.1142` |
| `blind_totals_strip` | 14 | `$0.0543` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 920 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `315, 316`
- **450-DPI Blind Totals Strip Disagreements (`3`)**:
  - Leaf `323` `p0323-b0008`: full-page `['Total ... 1,050,000', '1,150,000']` vs blind-strip `['<b>Total</b> ...', '1,050,000', '1,150,000']`
  - Leaf `846` `p0846-b0018`: full-page `['Total', '£3,842,647']` vs blind-strip `['Total ... £3,842,647']`
  - Leaf `863` `p0863-b0012`: full-page `['Total...', '35–27', 'Total...', '29 77']` vs blind-strip `['Total...', '35-27', 'Total...', '29 77']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`43` — catches smudged dates/figures in prose)**:
  - Leaf `12` `p0012-b0006`: VLM read `375` vs PDF OCR witness `['355']`
  - Leaf `12` `p0012-b0007`: VLM read `396` vs PDF OCR witness `['326']`
  - Leaf `12` `p0012-b0014`: VLM read `647` vs PDF OCR witness `['641']`
  - Leaf `53` `p0053-b0005`: VLM read `377` vs PDF OCR witness `['877']`
  - Leaf `82` `p0082-b0008`: VLM read `1905` vs PDF OCR witness `['1906']`
  - Leaf `83` `p0083-b0006`: VLM read `1903` vs PDF OCR witness `['1901', '1906', '1908']`
  - Leaf `115` `p0115-b0003`: VLM read `1885` vs PDF OCR witness `['1888']`
  - Leaf `142` `p0142-b0003`: VLM read `1893` vs PDF OCR witness `['1833']`
  - Leaf `165` `p0165-b0005`: VLM read `300,000,000` vs PDF OCR witness `['300900000']`
  - Leaf `243` `p0243-b0003`: VLM read `25,500,000` vs PDF OCR witness `['25590000']`
  - Leaf `304` `p0304-b0004`: VLM read `2615` vs PDF OCR witness `['2614', '9615']`
  - Leaf `319` `p0319-b0003`: VLM read `141` vs PDF OCR witness `['142']`
  - Leaf `333` `p0333-b0005`: VLM read `1870` vs PDF OCR witness `['1850']`
  - Leaf `334` `p0334-b0004`: VLM read `25,625,865` vs PDF OCR witness `['25625868']`
  - Leaf `334` `p0334-b0010`: VLM read `230` vs PDF OCR witness `['280']`
  - Leaf `356` `p0356-b0004`: VLM read `922` vs PDF OCR witness `['923', '926']`
  - Leaf `357` `p0357-b0006`: VLM read `932` vs PDF OCR witness `['930', '933', '935']`
  - Leaf `381` `p0381-b0005`: VLM read `24,07,438` vs PDF OCR witness `['2407488']`
  - Leaf `381` `p0381-b0012`: VLM read `27,81,500` vs PDF OCR witness `['2181500']`
  - Leaf `417` `p0417-b0005`: VLM read `1833` vs PDF OCR witness `['1533']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `543` prose joins, `0` split footnotes stitched, `2` multi-page tables unified, `144` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`168` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"LIBRARY OF THE UNIVERSITY OF ILLINOIS 954.03 N15s cop.2 REMOTE STORAGE"*
  - Leaf `7` `p0007-b0003` (`scanner_residue`): *"REMOTE STORAGE"*
  - Leaf `9` `p0009-b0001` (`scanner_residue`): *"954.03 N 15s Cop. 2"*
  - Leaf `9` `p0009-b0003` (`noise`): *"————✦————"*
  - Leaf `9` `p0009-b0005` (`scanner_residue`): *"Asia"*
  - Leaf `15` `p0015-b0002` (`noise`): *"——————"*
  - Leaf `31` `p0031-b0005` (`noise`): *"2"*
  - Leaf `33` `p0033-b0006` (`noise`): *"————"*
  - Leaf `34` `p0034-b0002` (`noise`): *"———❖———"*
  - Leaf `47` `p0047-b0006` (`noise`): *"3"*
  - Leaf `63` `p0063-b0008` (`noise`): *"4"*
  - Leaf `65` `p0065-b0007` (`scanner_residue`): *"UNIVERSITY OF ILLINOIS LIBRARY"*
- **Unattested Line-Wrap Hyphenation Decisions (`152` unique words out of `3064` total wraps)**: `seconder` (p.15), `cosmopolitan` (p.22), `engraven` (p.28), `unpopularity` (p.29), `reformed` (p.30), `emphasizes` (p.31), `leadership` (p.36), `Municipalities` (p.37), `abhorring` (p.39), `advocated` (p.43), `perseverance` (p.45), `calmness` (p.50), `unwarranted` (p.68), `Banquet` (p.91), `systematically` (p.91), `fellowworkers` (p.94), `hopeulness` (p.102), `highminded` (p.116)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 1,382,439 chars
- **Distinct Non-ASCII Glyphs (`12` across `42` leaves)**: · á â æ è é í ü œ ​ „ ☞
- **Corrections Replayed**: `38` applied, `0` orphaned/unmatched
