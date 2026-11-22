# Edition Verification & Run Audit — *The English Factories in India, 1642–1645*

- **Book ID**: `english-factories-india-1642-1645-vol-07` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 380 of 381 pages, gemini-3.6-flash on 1 of 381 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `381` extracted, `7` blank/tissue, `0` failed (of `388` PDF leaves)
- **Tracked API Spend**: **`$1.8569`** (`71.9%` cached input tokens: `3,063,352` / `4,257,635` in, `588,133` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 2.4% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 366 | `$1.3913` |
| `primary_quality_retry` | 12 | `$0.1507` |
| `recitation_band_top` | 10 | `$0.1016` |
| `recitation_band_bot` | 9 | `$0.0886` |
| `continuation_arbiter_batch` | 31 | `$0.0435` |
| `page_extract_batch_vetoed` | 12 | `$0.0429` |
| `recitation_retry` | 3 | `$0.0282` |
| `secondary_gemini_rescue` | 1 | `$0.0069` |
| `page_extract_batch_failed` | 3 | `$0.0033` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 1 pp., `gemini-3.8-flash`: 380 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `98` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `104` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `153` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `180` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `208` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `253` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `273` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `368` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `369` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`132` — catches smudged dates/figures in prose)**:
  - Leaf `14` `p0014-b0003`: VLM read `1642` vs PDF OCR witness `['1643']`
  - Leaf `14` `p0014-b0006`: VLM read `1642` vs PDF OCR witness `['1643']`
  - Leaf `22` `p0022-b0003`: VLM read `299` vs PDF OCR witness `['249', '399']`
  - Leaf `23` `p0023-b0004`: VLM read `256` vs PDF OCR witness `['252']`
  - Leaf `27` `p0027-b0005`: VLM read `255` vs PDF OCR witness `['254']`
  - Leaf `29` `p0029-b0003`: VLM read `10,000` vs PDF OCR witness `['40000']`
  - Leaf `42` `p0042-b0003`: VLM read `1652` vs PDF OCR witness `['1651', '1653']`
  - Leaf `46` `p0046-b0004`: VLM read `1642` vs PDF OCR witness `['1640', '1641']`
  - Leaf `51` `p0051-b0004`: VLM read `239` vs PDF OCR witness `['235', '339']`
  - Leaf `58` `p0058-b0003`: VLM read `100` vs PDF OCR witness `['200']`
  - Leaf `72` `p0072-b0005`: VLM read `273` vs PDF OCR witness `['275']`
  - Leaf `76` `p0076-b0005`: VLM read `1642` vs PDF OCR witness `['1640', '1641']`
  - Leaf `111` `p0111-b0004`: VLM read `1642` vs PDF OCR witness `['1643']`
  - Leaf `112` `p0112-b0003`: VLM read `1642` vs PDF OCR witness `['1641']`
  - Leaf `113` `p0113-b0003`: VLM read `1801` vs PDF OCR witness `['1803']`
  - Leaf `113` `p0113-b0003`: VLM read `1802` vs PDF OCR witness `['1803']`
  - Leaf `114` `p0114-b0004`: VLM read `1642` vs PDF OCR witness `['1643']`
  - Leaf `140` `p0140-b0005`: VLM read `1813` vs PDF OCR witness `['1810', '1811', '1814']`
  - Leaf `140` `p0140-b0007`: VLM read `1812` vs PDF OCR witness `['1810', '1811', '1814']`
  - Leaf `140` `p0140-b0009`: VLM read `1815` vs PDF OCR witness `['1810', '1811', '1814']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `123` prose joins, `11` split footnotes stitched, `0` multi-page tables unified, `406` total footnotes.
  - Stitched cross-page footnotes: p.38->p.39 (`1`), p.88->p.89 (`2`), p.119->p.120 (`3`), p.137->p.138 (`2`), p.192->p.193 (`2`), p.237->p.238 (`1`), p.242->p.243 (`4`), p.249->p.250 (`1`), p.280->p.281 (`3`), p.289->p.290 (`1`), p.320->p.321 (`3`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`78` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 08381418 6"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"#758en"*
  - Leaf `7` `p0007-b0002` (`scanner_residue`): *"Vol. 7"*
  - Leaf `7` `p0007-b0005` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `7` `p0007-b0012` (`scanner_residue`): *"129236 29/8/13"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `21` `p0021-b0006` (`noise`): *"Foster vii"*
  - Leaf `21` `p0021-b0007` (`noise`): *"b"*
  - Leaf `23` `p0023-b0006` (`noise`): *"b 2"*
  - Leaf `37` `p0037-b0007` (`noise`): *"FOSTER VII"*
  - Leaf `37` `p0037-b0008` (`noise`): *"C"*
  - Leaf `45` `p0045-b0006` (`noise`): *"FOSTER VII"*
- **Unattested Line-Wrap Hyphenation Decisions (`117` unique words out of `831` total wraps)**: `formidable` (p.11), `dislocation` (p.18), `shipwreck` (p.20), `stagnation` (p.22), `contraband` (p.23), `foreshadowing` (p.23), `privileged` (p.26), `skilfully` (p.30), `negotiated` (p.30), `explaining` (p.32), `discharging` (p.33), `adjoining` (p.40), `surprising` (p.40), `designation` (p.40), `inaccuracies` (p.42), `respectably` (p.43), `unwillingnes` (p.47), `elcewhere` (p.54)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 708,754 chars, `han`: 2 chars
- **Distinct Non-ASCII Glyphs (`40` across `238` leaves)**: Ã à ã ä ç è é ó Ā ā ē ġ ĩ Ī ī ō Ś ū ſ ʀ ʙ ᴀ ᴄ ᴇ ᴍ ᴏ ᴛ Ṣ ṭ „ ′ ⅓ ⅔ ⅕ ⅘ ⅛ ⅝ ⅞ 料 無
- **Corrections Replayed**: `10` applied, `0` orphaned/unmatched
