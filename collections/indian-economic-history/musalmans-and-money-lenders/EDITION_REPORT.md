# Edition Verification & Run Audit — *Musalmans and Money-Lenders in the Punjab*

- **Book ID**: `musalmans-and-money-lenders` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`96.4 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 207 of 207 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `207` extracted, `9` blank/tissue, `0` failed (of `216` PDF leaves)
- **Tracked API Spend**: **`$0.7968`** (`75.5%` cached input tokens: `1,638,612` / `2,171,388` in, `274,588` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **22.0 / 25.0** | -3.0: 1 unresolved footnote callout/body mismatch(es) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **24.4 / 25.0** | -0.6: 3 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Resolve 1 unmatched footnote marker(s) via anchor-matched corrections.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 207 | `$0.7401` |
| `blind_totals_strip` | 10 | `$0.0414` |
| `continuation_arbiter_batch` | 8 | `$0.0153` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 207 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `191`
- **450-DPI Blind Totals Strip Disagreements (`2`)**:
  - Leaf `125` `p0125-b0012`: full-page `['Total ...', '...', '1,081', '6,31,069', 'These figures are taken from the Revenue Administra-\ntion Report for 1884-85, Statement XB.']` vs blind-strip `['Total ...', '...', '1,081', '6,31,069', 'These figure<unclear>s</unclear><br>tion']`
  - Leaf `191` `p0191-b0025`: full-page `['', 'TOTAL ...', '68,55,161', '5,064', '1,131', '3,254', '47,799', '57,248', '2,825', '1,719', '4,544', '61,792', '']` vs blind-strip `['...', 'Bannu', '4', '4,22,659', '548', '92', '14']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`43` — catches smudged dates/figures in prose)**:
  - Leaf `8` `p0008-b0022`: VLM read `176` vs PDF OCR witness `['126', '136', '146']`
  - Leaf `8` `p0008-b0032`: VLM read `196` vs PDF OCR witness `['126', '136', '146']`
  - Leaf `8` `p0008-b0032`: VLM read `197` vs PDF OCR witness `['177', '194', '198']`
  - Leaf `9` `p0009-b0010`: VLM read `120` vs PDF OCR witness `['130', '190']`
  - Leaf `9` `p0009-b0021`: VLM read `160` vs PDF OCR witness `['130', '190']`
  - Leaf `9` `p0009-b0025`: VLM read `129` vs PDF OCR witness `['119', '179']`
  - Leaf `9` `p0009-b0025`: VLM read `135` vs PDF OCR witness `['130', '131', '132']`
  - Leaf `9` `p0009-b0036`: VLM read `169` vs PDF OCR witness `['119', '179']`
  - Leaf `10` `p0010-b0014`: VLM read `115` vs PDF OCR witness `['105', '135']`
  - Leaf `30` `p0030-b0011`: VLM read `19,000` vs PDF OCR witness `['10000']`
  - Leaf `30` `p0030-b0012`: VLM read `272,000` vs PDF OCR witness `['279000']`
  - Leaf `30` `p0030-b0015`: VLM read `26,000` vs PDF OCR witness `['36000']`
  - Leaf `30` `p0030-b0019`: VLM read `100` vs PDF OCR witness `['000']`
  - Leaf `57` `p0057-b0008`: VLM read `1844` vs PDF OCR witness `['1849']`
  - Leaf `58` `p0058-b0006`: VLM read `1,000` vs PDF OCR witness `['3000']`
  - Leaf `64` `p0064-b0006`: VLM read `1870` vs PDF OCR witness `['1860']`
  - Leaf `64` `p0064-b0006`: VLM read `1870` vs PDF OCR witness `['1860']`
  - Leaf `88` `p0088-b0007`: VLM read `1872` vs PDF OCR witness `['1871']`
  - Leaf `88` `p0088-b0009`: VLM read `1886` vs PDF OCR witness `['1866']`
  - Leaf `88` `p0088-b0013`: VLM read `1867` vs PDF OCR witness `['1866']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `132` prose joins, `1` split footnotes stitched, `0` multi-page tables unified, `74` total footnotes.
  - Stitched cross-page footnotes: p.105->p.106 (`†`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`85` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Cornell University Library BOUGHT WITH THE INCOME FROM THE SAGE ENDOWMENT FUND THE GIFT OF"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"7673-2"*
  - Leaf `2` `p0002-b0003` (`scanner_residue`): *"RETURN TO ALBERT R. MANN LIBRARY ITHACA, N. Y."*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"Cornell University Library HD 1167.T48"*
  - Leaf `3` `p0003-b0002` (`scanner_residue`): *"Musalmans and money-lenders in the Punja"*
  - Leaf `3` `p0003-b0004` (`scanner_residue`): *"3 1924 013 743 848"*
  - Leaf `3` `p0003-b0005` (`scanner_residue`): *"mann"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Cornell University Library"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"The original of this book is in the Cornell University Library. There are no known copyrig"*
  - Leaf `4` `p0004-b0003` (`scanner_residue`): *"http://www.archive.org/details/cu31924013743848"*
  - Leaf `5` `p0005-b0008` (`noise`): *"~~~~~"*
  - Leaf `5` `p0005-b0010` (`noise`): *"—"*
- **Unattested Line-Wrap Hyphenation Decisions (`120` unique words out of `1002` total wraps)**: `expansive` (p.16), `prairielike` (p.17), `bordering` (p.18), `pressing` (p.18), `everpressing` (p.19), `multiplied` (p.19), `illumed` (p.20), `moulded` (p.20), `concentration` (p.21), `compounded` (p.22), `nominal` (p.23), `separatist` (p.25), `animosities` (p.26), `consciousness` (p.26), `carries` (p.28), `openair` (p.28), `displaying` (p.28), `municipal` (p.29)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 311,394 chars
- **Distinct Non-ASCII Glyphs (`12` across `38` leaves)**: · À à á â æ é í ô ú ý „
- **Corrections Replayed**: `24` applied, `0` orphaned/unmatched
