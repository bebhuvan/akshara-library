# Edition Verification & Run Audit — *From Akbar to Aurangzeb*

- **Book ID**: `from-akbar-to-aurangzeb` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`96.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 385 of 386 pages, gemini-3.6-flash on 1 of 386 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `386` extracted, `8` blank/tissue, `0` failed (of `394` PDF leaves)
- **Tracked API Spend**: **`$1.8089`** (`76.0%` cached input tokens: `2,972,200` / `3,908,286` in, `573,339` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **21.0 / 25.0** | -4.0: 1 column total arithmetic mismatch(es) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 385 | `$1.5829` |
| `pro_table_adjudicate` | 2 | `$0.1299` |
| `blind_totals_strip` | 11 | `$0.0429` |
| `continuation_arbiter_batch` | 22 | `$0.0380` |
| `secondary_gemini_rescue` | 1 | `$0.0115` |
| `page_extract_batch_vetoed` | 1 | `$0.0037` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 1 pp., `gemini-3.8-flash`: 385 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `22, 39`
- **Surgical Table Adjudications (`gemini-4-argon` / complex rescue)**:
  - Leaf `151` (`gemini-4-argon`): accepted=`True`, mismatches `1` -> `1`
  - Leaf `285` (`gemini-4-argon`): accepted=`True`, mismatches `4` -> `4`
- **450-DPI Blind Totals Strip Disagreements (`1`)**:
  - Leaf `154` `p0154-b0008`: full-page `['84,000', '„']` vs blind-strip `['84,000', ',,']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`43` — catches smudged dates/figures in prose)**:
  - Leaf `18` `p0018-b0011`: VLM read `182` vs PDF OCR witness `['188']`
  - Leaf `18` `p0018-b0015`: VLM read `197` vs PDF OCR witness `['297']`
  - Leaf `18` `p0018-b0023`: VLM read `233` vs PDF OCR witness `['273', '283']`
  - Leaf `18` `p0018-b0026`: VLM read `260` vs PDF OCR witness `['268']`
  - Leaf `31` `p0031-b0006`: VLM read `1513` vs PDF OCR witness `['1518']`
  - Leaf `73` `p0073-b0005`: VLM read `213` vs PDF OCR witness `['218', '233', '313']`
  - Leaf `123` `p0123-b0006`: VLM read `1639` vs PDF OCR witness `['1637', '1638']`
  - Leaf `126` `p0126-b0007`: VLM read `1628` vs PDF OCR witness `['1620', '1622', '1625']`
  - Leaf `126` `p0126-b0008`: VLM read `1640` vs PDF OCR witness `['1620', '1643', '1649']`
  - Leaf `133` `p0133-b0009`: VLM read `1655` vs PDF OCR witness `['1625']`
  - Leaf `153` `p0153-b0010`: VLM read `5,000` vs PDF OCR witness `['0000', '1000']`
  - Leaf `155` `p0155-b0011`: VLM read `2,000` vs PDF OCR witness `['1000', '3000', '4000']`
  - Leaf `164` `p0164-b0005`: VLM read `138` vs PDF OCR witness `['148', '158', '188']`
  - Leaf `165` `p0165-b0003`: VLM read `111` vs PDF OCR witness `['131']`
  - Leaf `172` `p0172-b0005`: VLM read `153` vs PDF OCR witness `['143', '150', '155']`
  - Leaf `177` `p0177-b0004`: VLM read `1677` vs PDF OCR witness `['1678']`
  - Leaf `183` `p0183-b0009`: VLM read `1612` vs PDF OCR witness `['1622', '1632', '1642']`
  - Leaf `183` `p0183-b0010`: VLM read `1613` vs PDF OCR witness `['1633', '1653', '1663']`
  - Leaf `183` `p0183-b0011`: VLM read `1614` vs PDF OCR witness `['1634', '1644']`
  - Leaf `183` `p0183-b0012`: VLM read `248` vs PDF OCR witness `['238', '348']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `260` prose joins, `11` split footnotes stitched, `0` multi-page tables unified, `195` total footnotes.
  - Stitched cross-page footnotes: p.35->p.36 (`1`), p.48->p.49 (`2`), p.54->p.55 (`1`), p.86->p.87 (`1`), p.92->p.93 (`2`), p.142->p.143 (`1`), p.202->p.203 (`1`), p.256->p.257 (`2`), p.268->p.269 (`1`), p.354->p.355 (`1`), p.362->p.363 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`49` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"BARNETT LIBRARY 45, WELLINGTON SQUARE OXFORD WITHDRAWN CANCELLED"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"BARNETT HOUSE LIBRARY OXFORD 7291 WITHDRAWN HD 2323 10 D 271"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"1 4 -19/2"*
  - Leaf `3` `p0003-b0002` (`scanner_residue`): *"BARNETT LIBRARY 45, WELLINGTON SQUARE OXFORD WITHDRAWN WORC. COLLEGE LIBRARY CANCELLED"*
  - Leaf `3` `p0003-b0003` (`scanner_residue`): *"WORCESTER COLLEGE * THE LIBRARY OXFORD WORC. COLLEGE LIBRARY CANCELLED"*
  - Leaf `3` `p0003-b0004` (`scanner_residue`): *"305121516O"*
  - Leaf `23` `p0023-b0007` (`noise`): *"B"*
  - Leaf `37` `p0037-b0001` (`noise`): *"I"*
  - Leaf `39` `p0039-b0004` (`noise`): *"C"*
  - Leaf `42` `p0042-b0007` (`scanner_residue`): *"Handwritten ink mark or residue at bottom left margin"*
  - Leaf `43` `p0043-b0001` (`noise`): *"I"*
  - Leaf `49` `p0049-b0005` (`noise`): *"—"*
- **Unattested Line-Wrap Hyphenation Decisions (`50` unique words out of `646` total wraps)**: `Pondicherry` (p.11), `exploration` (p.13), `Christendom` (p.30), `concerted` (p.31), `unattractive` (p.35), `surmounted` (p.42), `foreshadowed` (p.47), `assortment` (p.52), `dependence` (p.71), `Mogul-Portuguese` (p.72), `statesmen` (p.82), `Bengalders` (p.99), `reviving` (p.124), `sophisticated` (p.136), `adulterating` (p.136), `requisitioned` (p.141), `reprimanded` (p.150), `performances` (p.157)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 659,881 chars
- **Distinct Non-ASCII Glyphs (`27` across `104` leaves)**: ± · ã ç é ë õ Ā ā ġ ģ ĩ ī œ ū „ ⁄ ₉ ⅓ ⅔ ⅖ ⅗ ⅙ ⎧ ⎩ ⎫ ⎭
- **Corrections Replayed**: `26` applied, `0` orphaned/unmatched
