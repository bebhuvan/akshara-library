# Edition Verification & Run Audit — *The English Factories in India, 1637–1641*

- **Book ID**: `english-factories-india-1637-1641-vol-06` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`100.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 392 of 393 pages, gemini-3.6-flash on 1 of 393 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `393` extracted, `5` blank/tissue, `0` failed (of `398` PDF leaves)
- **Tracked API Spend**: **`$1.9145`** (`71.8%` cached input tokens: `3,159,315` / `4,398,155` in, `601,003` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Community Edition! Human page-proof coverage is 0.0% (pages re-read 2.5%) toward Source-Certified.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 372 | `$1.4057` |
| `primary_quality_retry` | 21 | `$0.2583` |
| `page_extract_batch_vetoed` | 21 | `$0.0814` |
| `recitation_band_top` | 7 | `$0.0708` |
| `recitation_band_bot` | 6 | `$0.0628` |
| `continuation_arbiter_batch` | 19 | `$0.0269` |
| `secondary_gemini_rescue` | 1 | `$0.0087` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 1 pp., `gemini-3.8-flash`: 392 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `6`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `95` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `158` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `285` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `333` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `342` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `360` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`182` — catches smudged dates/figures in prose)**:
  - Leaf `22` `p0022-b0005`: VLM read `1629` vs PDF OCR witness `['1639']`
  - Leaf `23` `p0023-b0004`: VLM read `1639` vs PDF OCR witness `['1539', '1633', '1638']`
  - Leaf `51` `p0051-b0003`: VLM read `263` vs PDF OCR witness `['283']`
  - Leaf `52` `p0052-b0003`: VLM read `312` vs PDF OCR witness `['310', '311', '372']`
  - Leaf `52` `p0052-b0003`: VLM read `272` vs PDF OCR witness `['262', '270', '274']`
  - Leaf `60` `p0060-b0004`: VLM read `1897` vs PDF OCR witness `['1894']`
  - Leaf `78` `p0078-b0004`: VLM read `321` vs PDF OCR witness `['331']`
  - Leaf `88` `p0088-b0004`: VLM read `67,865` vs PDF OCR witness `['57865']`
  - Leaf `104` `p0104-b0004`: VLM read `600` vs PDF OCR witness `['200']`
  - Leaf `127` `p0127-b0004`: VLM read `358` vs PDF OCR witness `['350']`
  - Leaf `177` `p0177-b0003`: VLM read `110` vs PDF OCR witness `['120']`
  - Leaf `180` `p0180-b0005`: VLM read `122` vs PDF OCR witness `['126']`
  - Leaf `186` `p0186-b0004`: VLM read `1665` vs PDF OCR witness `['1667']`
  - Leaf `189` `p0189-b0006`: VLM read `325` vs PDF OCR witness `['335']`
  - Leaf `198` `p0198-b0003`: VLM read `1,000` vs PDF OCR witness `['2000', '3000', '7000']`
  - Leaf `203` `p0203-b0007`: VLM read `101` vs PDF OCR witness `['103']`
  - Leaf `205` `p0205-b0006`: VLM read `1622` vs PDF OCR witness `['1623', '1632']`
  - Leaf `214` `p0214-b0006`: VLM read `1690` vs PDF OCR witness `['1694']`
  - Leaf `232` `p0232-b0008`: VLM read `1718` vs PDF OCR witness `['1716']`
  - Leaf `240` `p0240-b0003`: VLM read `28,000` vs PDF OCR witness `['38000']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `163` prose joins, `4` split footnotes stitched, `0` multi-page tables unified, `402` total footnotes.
  - Stitched cross-page footnotes: p.102->p.103 (`2`), p.169->p.170 (`5`), p.176->p.177 (`3`), p.265->p.266 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`79` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 08381419 4"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2010 with funding from University of Toronto"*
  - Leaf `5` `p0005-b0002` (`scanner_residue`): *"http://www.archive.org/details/englishfactories06fost"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed circular library stamp of Toronto University Library with crown emblem."*
  - Leaf `23` `p0023-b0006` (`noise`): *"FOSTER VI"*
  - Leaf `23` `p0023-b0007` (`noise`): *"b"*
  - Leaf `25` `p0025-b0006` (`noise`): *"b 2"*
  - Leaf `39` `p0039-b0005` (`noise`): *"FOSTER VI"*
  - Leaf `39` `p0039-b0006` (`noise`): *"C"*
  - Leaf `41` `p0041-b0006` (`noise`): *"c 2"*
  - Leaf `55` `p0055-b0007` (`scanner_residue`): *"64"*
  - Leaf `55` `p0055-b0008` (`noise`): *"FOSTER VI"*
- **Unattested Line-Wrap Hyphenation Decisions (`78` unique words out of `648` total wraps)**: `publication` (p.9), `embarrassment` (p.11), `hardships` (p.20), `extortionate` (p.22), `passports` (p.24), `commencement` (p.35), `reimburse` (p.41), `predominant` (p.51), `depression` (p.52), `adulteration` (p.52), `passagemoney` (p.56), `interpreting` (p.61), `questionlesse` (p.66), `sickenesse` (p.70), `Verasheroone` (p.83), `disturbing` (p.86), `temporarily` (p.86), `thanckfullnesse` (p.88)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 716,732 chars
- **Distinct Non-ASCII Glyphs (`26` across `270` leaves)**: · Ã á ã ç é ó ô Ā ā ē Ī ī Ō ō ū ′ ⁄ ₂ ₉ ⅓ ⅔ ⅕ ⅛ ⅜ ⌈
- **Corrections Replayed**: `3` applied, `0` orphaned/unmatched
