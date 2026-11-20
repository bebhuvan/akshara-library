# Edition Verification & Run Audit — *The English Factories in India, 1655–1660*

- **Book ID**: `english-factories-india-1655-1660-vol-10` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`100.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 450 of 450 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `450` extracted, `6` blank/tissue, `0` failed (of `456` PDF leaves)
- **Tracked API Spend**: **`$2.0849`** (`75.2%` cached input tokens: `3,606,897` / `4,797,516` in, `747,411` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Community Edition! Human page-proof coverage is 0.0% (pages re-read 2.7%) toward Source-Certified.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 439 | `$1.8081` |
| `primary_quality_retry` | 10 | `$0.1230` |
| `page_extract_batch_vetoed` | 10 | `$0.0382` |
| `recitation_retry` | 1 | `$0.0377` |
| `continuation_arbiter_batch` | 21 | `$0.0340` |
| `recitation_band_bot` | 2 | `$0.0223` |
| `recitation_band_top` | 2 | `$0.0206` |
| `page_extract_batch_failed` | 1 | `$0.0011` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 450 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `262` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `275` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`132` — catches smudged dates/figures in prose)**:
  - Leaf `17` `p0017-b0007`: VLM read `1651` vs PDF OCR witness `['1655', '1656']`
  - Leaf `32` `p0032-b0006`: VLM read `1651` vs PDF OCR witness `['1655', '1659']`
  - Leaf `54` `p0054-b0003`: VLM read `100` vs PDF OCR witness `['130']`
  - Leaf `80` `p0080-b0009`: VLM read `1651` vs PDF OCR witness `['1656']`
  - Leaf `127` `p0127-b0007`: VLM read `1651` vs PDF OCR witness `['1657']`
  - Leaf `151` `p0151-b0004`: VLM read `1651` vs PDF OCR witness `['1652', '1653', '1657']`
  - Leaf `151` `p0151-b0004`: VLM read `1651` vs PDF OCR witness `['1652', '1653', '1657']`
  - Leaf `181` `p0181-b0006`: VLM read `1651` vs PDF OCR witness `['1641', '1655', '1658']`
  - Leaf `184` `p0184-b0004`: VLM read `112,` vs PDF OCR witness `['172']`
  - Leaf `214` `p0214-b0010`: VLM read `1661` vs PDF OCR witness `['1660']`
  - Leaf `275` `p0275-b0005`: VLM read `1657` vs PDF OCR witness `['1658', '1659']`
  - Leaf `351` `p0351-b0010`: VLM read `1651` vs PDF OCR witness `['1661']`
  - Leaf `398` `p0398-b0005`: VLM read `1658` vs PDF OCR witness `['1659']`
  - Leaf `422` `p0422-b0004`: VLM read `1661` vs PDF OCR witness `['1660']`
  - Leaf `430` `p0430-b0004`: VLM read `110` vs PDF OCR witness `['113', '114', '118']`
  - Leaf `432` `p0432-b0007`: VLM read `358` vs PDF OCR witness `['258', '350', '357']`
  - Leaf `432` `p0432-b0009`: VLM read `2759` vs PDF OCR witness `['2729', '2749', '2751']`
  - Leaf `432` `p0432-b0009`: VLM read `363` vs PDF OCR witness `['365', '367', '463']`
  - Leaf `432` `p0432-b0012`: VLM read `398` vs PDF OCR witness `['378']`
  - Leaf `433` `p0433-b0008`: VLM read `110` vs PDF OCR witness `['112', '113', '114']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `311` prose joins, `10` split footnotes stitched, `0` multi-page tables unified, `384` total footnotes.
  - Stitched cross-page footnotes: p.49->p.50 (`1`), p.125->p.126 (`2`), p.133->p.134 (`1`), p.140->p.141 (`1`), p.172->p.173 (`2`), p.266->p.267 (`3`), p.267->p.268 (`1`), p.275->p.276 (`2`), p.280->p.281 (`2`), p.365->p.366 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`92` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 08381415 2"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2010 with funding from University of Toronto"*
  - Leaf `3` `p0003-b0002` (`scanner_residue`): *"http://www.archive.org/details/englishfactories10fost"*
  - Leaf `7` `p0007-b0010` (`scanner_residue`): *"[Vol. 10]"*
  - Leaf `7` `p0007-b0011` (`scanner_residue`): *"Library emboss stamp: University of Toronto Library"*
  - Leaf `7` `p0007-b0012` (`scanner_residue`): *"163184. / 23.6.21."*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed circular library stamp of the University of Toronto."*
  - Leaf `13` `p0013-b0006` (`noise`): *"2258"*
  - Leaf `13` `p0013-b0007` (`noise`): *"B"*
  - Leaf `15` `p0015-b0005` (`noise`): *"B 2"*
  - Leaf `29` `p0029-b0009` (`noise`): *"2258"*
  - Leaf `29` `p0029-b0010` (`noise`): *"C"*
- **Unattested Line-Wrap Hyphenation Decisions (`68` unique words out of `664` total wraps)**: `thoroughness` (p.16), `Adverting` (p.33), `disinterred` (p.36), `unemployed` (p.45), `unchristianlike` (p.47), `Worshipfull` (p.49), `opentraders` (p.69), `Nasserpore` (p.90), `inconvenienced` (p.90), `Mountacute` (p.97), `phisitions` (p.99), `fortefieing` (p.103), `insolencyes` (p.107), `proportionate` (p.126), `ensureance` (p.128), `Ahmadabad` (p.133), `appering` (p.134), `overawing` (p.143)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 872,431 chars, `cyrillic`: 10 chars
- **Distinct Non-ASCII Glyphs (`27` across `347` leaves)**: À à ã ç é Ā ā ē ġ ħ ī œ ū а в е м о с т ч ь ⅓ ⅔ ⅛ ⅝ ⅞
- **Corrections Replayed**: `9` applied, `0` orphaned/unmatched
