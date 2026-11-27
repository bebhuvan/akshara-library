# Edition Verification & Run Audit — *The English Factories in India, 1634–1636*

- **Book ID**: `english-factories-india-1634-1636-vol-05` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 395 of 402 pages, gemini-3.6-flash on 7 of 402 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `402` extracted, `4` blank/tissue, `0` failed (of `406` PDF leaves)
- **Tracked API Spend**: **`$2.1948`** (`69.6%` cached input tokens: `3,223,044` / `4,628,875` in, `636,621` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 2.5% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 371 | `$1.3992` |
| `primary_quality_retry` | 25 | `$0.3401` |
| `recitation_band_top` | 11 | `$0.1154` |
| `page_extract_batch_vetoed` | 25 | `$0.1088` |
| `recitation_band_bot` | 6 | `$0.0641` |
| `secondary_gemini_rescue` | 7 | `$0.0624` |
| `recitation_retry` | 6 | `$0.0617` |
| `continuation_arbiter_batch` | 25 | `$0.0362` |
| `page_extract_batch_failed` | 6 | `$0.0068` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 7 pp., `gemini-3.8-flash`: 395 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `6, 405`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `79` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `122` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `205` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `317` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`183` — catches smudged dates/figures in prose)**:
  - Leaf `25` `p0025-b0003`: VLM read `228` vs PDF OCR witness `['238']`
  - Leaf `36` `p0036-b0004`: VLM read `1635` vs PDF OCR witness `['1535', '1637']`
  - Leaf `37` `p0037-b0003`: VLM read `1636` vs PDF OCR witness `['1635']`
  - Leaf `42` `p0042-b0004`: VLM read `415` vs PDF OCR witness `['445']`
  - Leaf `43` `p0043-b0003`: VLM read `124` vs PDF OCR witness `['134']`
  - Leaf `45` `p0045-b0004`: VLM read `217` vs PDF OCR witness `['216', '218', '317']`
  - Leaf `49` `p0049-b0003`: VLM read `262` vs PDF OCR witness `['263', '264', '265']`
  - Leaf `52` `p0052-b0003`: VLM read `1634` vs PDF OCR witness `['1633']`
  - Leaf `71` `p0071-b0005`: VLM read `292` vs PDF OCR witness `['392']`
  - Leaf `82` `p0082-b0006`: VLM read `5,000` vs PDF OCR witness `['3000']`
  - Leaf `94` `p0094-b0003`: VLM read `1,000` vs PDF OCR witness `['8000']`
  - Leaf `102` `p0102-b0007`: VLM read `1631` vs PDF OCR witness `['1634']`
  - Leaf `104` `p0104-b0005`: VLM read `333` vs PDF OCR witness `['334']`
  - Leaf `114` `p0114-b0003`: VLM read `6,000` vs PDF OCR witness `['3000', '9000']`
  - Leaf `114` `p0114-b0003`: VLM read `5,000` vs PDF OCR witness `['3000', '9000']`
  - Leaf `124` `p0124-b0004`: VLM read `1630` vs PDF OCR witness `['1634']`
  - Leaf `147` `p0147-b0003`: VLM read `20,000` vs PDF OCR witness `['30000']`
  - Leaf `151` `p0151-b0004`: VLM read `363` vs PDF OCR witness `['263']`
  - Leaf `182` `p0182-b0004`: VLM read `1552` vs PDF OCR witness `['1553']`
  - Leaf `194` `p0194-b0004`: VLM read `1636` vs PDF OCR witness `['1635']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `167` prose joins, `5` split footnotes stitched, `0` multi-page tables unified, `338` total footnotes.
  - Stitched cross-page footnotes: p.40->p.41 (`3`), p.136->p.137 (`1`), p.201->p.202 (`2`), p.253->p.254 (`2`), p.272->p.273 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`84` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 04303 4800"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2008 with funding from Microsoft Corporation"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"http://www.archive.org/details/englishfactories05fostuoft"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"Call number label snippet."*
  - Leaf `7` `p0007-b0002` (`scanner_residue`): *"[Vol. 5]"*
  - Leaf `7` `p0007-b0005` (`scanner_residue`): *"Embossed circular library stamp of the University of Toronto Library."*
  - Leaf `7` `p0007-b0012` (`scanner_residue`): *"Handwritten numbers: 117500 / 18/7/11"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed library stamp of University of Toronto"*
  - Leaf `23` `p0023-b0007` (`noise`): *"Foster v"*
  - Leaf `23` `p0023-b0008` (`noise`): *"b"*
  - Leaf `25` `p0025-b0006` (`noise`): *"b 2"*
  - Leaf `39` `p0039-b0006` (`noise`): *"FOSTER V"*
- **Unattested Line-Wrap Hyphenation Decisions (`82` unique words out of `845` total wraps)**: `cottonwool` (p.10), `consolidate` (p.16), `unfriendly` (p.18), `distasteful` (p.18), `guaranteeing` (p.20), `forbidding` (p.22), `announcement` (p.22), `opportune` (p.22), `disavowing` (p.36), `postponed` (p.39), `assassination` (p.46), `precedence` (p.51), `consequentlie` (p.60), `wheresoever` (p.72), `suggesting` (p.74), `Mascareena` (p.75), `disembark` (p.79), `deductions` (p.81)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 726,470 chars
- **Distinct Non-ASCII Glyphs (`22` across `301` leaves)**: ã æ ç é í ó Ā ā ġ Ī ī ō œ Ū ū ˙ ṭ ⁄ ₈ ⅛ ⅜ ⅞
- **Corrections Replayed**: `7` applied, `0` orphaned/unmatched
