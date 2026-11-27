# Edition Verification & Run Audit — *The Economic History of India Under Early British Rule*

- **Book ID**: `economic-history-india-early-british-dutt` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`96.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 466 of 466 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `466` extracted, `2` blank/tissue, `0` failed (of `468` PDF leaves)
- **Tracked API Spend**: **`$1.8143`** (`73.7%` cached input tokens: `3,688,856` / `5,003,183` in, `598,302` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **21.0 / 25.0** | -4.0: 1 collapsed/jammed table row warning(s) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 466 | `$1.6157` |
| `blind_totals_strip` | 31 | `$0.1234` |
| `continuation_arbiter_batch` | 44 | `$0.0752` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 466 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `325, 428, 429, 430, 431`
- **450-DPI Blind Totals Strip Disagreements (`10`)**:
  - Leaf `428` `p0428-b0009`: full-page `['Total . . .', '4,197,137', '8,026,193', '6,567,808']` vs blind-strip `['ven', '931\n182\n480', '593', '694\n804\n596', '994', '906\n828\n937', '171', '141']`
  - Leaf `428` `p0428-b0014`: full-page `['Total . . .', '4,123,982', '7,866,094', '6,888,997']` vs blind-strip `['38', '', 'Gr', 'F']`
  - Leaf `428` `p0428-b0019`: full-page `['Total . . .', '4,058,814', '8,016,171', '7,508,038']` vs blind-strip `['<unclear>T</unclear>OTAL ... Rs.', '£', '58,235', '97,891', '30,70', '23,297', '18,303', '39,292', '64,']`
  - Leaf `428` `p0428-b0024`: full-page `['Total . . .', '3,869,298', '8,059,880.', '8,015,327']` vs blind-strip `['<unclear>H</unclear>', '', '. . . . . . . . . .']`
  - Leaf `428` `p0428-b0034`: full-page `['Total . . .', '4,128,133', '9,736,672', '9,955,390']` vs blind-strip `['Total', 'Total as', 'May', 'Total', 'Total as', 'May', 'Total', 'Total as', 'May']`
  - Leaf `428` `p0428-b0039`: full-page `['Total . . .', '4,221,695', '10,485,059', '11,468,185']` vs blind-strip `['40', '', '']`
  - Leaf `429` `p0429-b0009`: full-page `['Total . . .', '4,296,884', '13,464,537', '12,326,880']` vs blind-strip `['<unclear>Beng</unclear>al . . . .', '3,225,436', '9,336,707', '7,464,29<unclear></unclear>']`
  - Leaf `429` `p0429-b0014`: full-page `['Total . . .', '4,480,128', '13,271,385', '14,395,405']` vs blind-strip `['1806-7. · · ·', '4,880,433', '15,403,409', '17,421,41<unclear>1</unclear>']`
  - Leaf `429` `p0429-b0019`: full-page `['Total . . .', '4,604,025', '14,949,395', '16,115,183']` vs blind-strip `['<unclear>...</unclear>al · · · ·', '3,729,098', '9,971,695', '7,760,92<unclear>...</unclear>']`
  - Leaf `429` `p0429-b0024`: full-page `['Total . . .', '4,880,433', '15,403,409', '17,421,418']` vs blind-strip `['1809-10. · · · 5,35,789', '15,525,055', '15,392,88']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`96` — catches smudged dates/figures in prose)**:
  - Leaf `13` `p0013-b0004`: VLM read `1793` vs PDF OCR witness `['1798']`
  - Leaf `27` `p0027-b0009`: VLM read `1763` vs PDF OCR witness `['1765', '1793']`
  - Leaf `27` `p0027-b0011`: VLM read `135` vs PDF OCR witness `['185']`
  - Leaf `27` `p0027-b0015`: VLM read `195` vs PDF OCR witness `['185']`
  - Leaf `28` `p0028-b0011`: VLM read `1837` vs PDF OCR witness `['1817', '1827']`
  - Leaf `28` `p0028-b0012`: VLM read `1837` vs PDF OCR witness `['1817', '1827']`
  - Leaf `30` `p0030-b0004`: VLM read `1817` vs PDF OCR witness `['1837']`
  - Leaf `40` `p0040-b0004`: VLM read `1817` vs PDF OCR witness `['1813']`
  - Leaf `41` `p0041-b0004`: VLM read `1817` vs PDF OCR witness `['1837']`
  - Leaf `41` `p0041-b0006`: VLM read `1817` vs PDF OCR witness `['1837']`
  - Leaf `42` `p0042-b0004`: VLM read `1810` vs PDF OCR witness `['1800', '1820']`
  - Leaf `43` `p0043-b0004`: VLM read `1817` vs PDF OCR witness `['1827']`
  - Leaf `45` `p0045-b0003`: VLM read `1817` vs PDF OCR witness `['1837']`
  - Leaf `74` `p0074-b0011`: VLM read `1771` vs PDF OCR witness `['1773']`
  - Leaf `81` `p0081-b0006`: VLM read `1868` vs PDF OCR witness `['1768']`
  - Leaf `88` `p0088-b0005`: VLM read `1781` vs PDF OCR witness `['1780']`
  - Leaf `93` `p0093-b0004`: VLM read `1773` vs PDF OCR witness `['1772', '1774']`
  - Leaf `94` `p0094-b0005`: VLM read `226,000` vs PDF OCR witness `['223000']`
  - Leaf `94` `p0094-b0006`: VLM read `1774` vs PDF OCR witness `['1773']`
  - Leaf `119` `p0119-b0007`: VLM read `1781` vs PDF OCR witness `['1789']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `330` prose joins, `3` split footnotes stitched, `1` multi-page tables unified, `345` total footnotes.
  - Stitched cross-page footnotes: p.173->p.174 (`2`), p.305->p.306 (`1`), p.454->p.455 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`40` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 07489410 6"*
  - Leaf `6` `p0006-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2010 with funding from University of Toronto"*
  - Leaf `6` `p0006-b0002` (`scanner_residue`): *"http://www.archive.org/details/ed2economichisto00dutt"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"D 9793 e"*
  - Leaf `7` `p0007-b0008` (`scanner_residue`): *"Embossed circular library stamp of the University of Toronto Library."*
  - Leaf `7` `p0007-b0012` (`scanner_residue`): *"93138 26/11/08"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed library stamp: CENTRAL LIBRARY PATIALA"*
  - Leaf `21` `p0021-b0005` (`noise`): *"b"*
  - Leaf `27` `p0027-b0020` (`noise`): *"xxiii"*
  - Leaf `29` `p0029-b0006` (`noise`): *"A"*
  - Leaf `45` `p0045-b0004` (`noise`): *"B"*
  - Leaf `46` `p0046-b0006` (`noise`): *"18"*
- **Unattested Line-Wrap Hyphenation Decisions (`123` unique words out of `1442` total wraps)**: `disables` (p.13), `Governors-General` (p.18), `Salisbury` (p.21), `adjudication` (p.24), `needful` (p.25), `insufficiency` (p.26), `conspiracy` (p.32), `interview` (p.39), `arresting` (p.42), `attitude` (p.48), `inveterate` (p.49), `narrowsighted` (p.58), `proportionable` (p.64), `ordering` (p.68), `donations` (p.69), `complicated` (p.71), `Purneah` (p.79), `letting` (p.88)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 628,614 chars
- **Distinct Non-ASCII Glyphs (`12` across `14` leaves)**: · É Ü ê ı œ ṣ „ ⁄ ⅓ ⅔ ⅛
- **Corrections Replayed**: `24` applied, `0` orphaned/unmatched
