# Edition Verification & Run Audit — *A Brief History of the Indian Peoples*

- **Book ID**: `brief-history-indian-peoples` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 263 of 264 pages, gemini-3.8-flash on 1 of 264 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `264` extracted, `2` blank/tissue, `0` failed (of `266` PDF leaves)
- **Tracked API Spend**: **`$4.5458`** (`10.3%` cached input tokens: `319,488` / `3,113,938` in, `343,312` out, `285,200` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 4.9% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 262 | `$4.3306` |
| `recitation_band_top` | 2 | `$0.0562` |
| `recitation_retry` | 2 | `$0.0372` |
| `blind_totals_strip` | 3 | `$0.0359` |
| `recitation_band_bot` | 2 | `$0.0260` |
| `continuation_arbiter_batch` | 11 | `$0.0233` |
| `secondary_gemini_rescue` | 1 | `$0.0173` |
| `page_extract_batch_failed` | 2 | `$0.0113` |
| `tertiary_gemini_rescue` | 1 | `$0.0080` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 1 pp., `gemini-4-hydrogen`: 263 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **450-DPI Blind Totals Strip Disagreements (`1`)**:
  - Leaf `37` `p0037-b0027`: full-page `['Total for all India, including Burma', '1,768,061', '294,962,764', '166']` vs blind-strip `['Total for all India, including Burma . . . }', '1,768,061', '294,962,764', '166']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`107` — catches smudged dates/figures in prose)**:
  - Leaf `13` `p0013-b0009`: VLM read `101` vs PDF OCR witness `['100', '102', '103']`
  - Leaf `13` `p0013-b0009`: VLM read `101` vs PDF OCR witness `['100', '102', '103']`
  - Leaf `13` `p0013-b0012`: VLM read `110` vs PDF OCR witness `['100', '112', '113']`
  - Leaf `13` `p0013-b0012`: VLM read `110` vs PDF OCR witness `['100', '112', '113']`
  - Leaf `13` `p0013-b0012`: VLM read `111` vs PDF OCR witness `['112', '113', '116']`
  - Leaf `13` `p0013-b0012`: VLM read `111` vs PDF OCR witness `['112', '113', '116']`
  - Leaf `15` `p0015-b0009`: VLM read `173` vs PDF OCR witness `['163', '170', '171']`
  - Leaf `15` `p0015-b0009`: VLM read `174` vs PDF OCR witness `['164', '170', '171']`
  - Leaf `16` `p0016-b0007`: VLM read `1813` vs PDF OCR witness `['1814', '1815', '1817']`
  - Leaf `16` `p0016-b0007`: VLM read `213` vs PDF OCR witness `['203', '210', '211']`
  - Leaf `16` `p0016-b0007`: VLM read `1845` vs PDF OCR witness `['1805', '1815', '1835']`
  - Leaf `36` `p0036-b0009`: VLM read `494` vs PDF OCR witness `['294']`
  - Leaf `40` `p0040-b0006`: VLM read `1891` vs PDF OCR witness `['1881']`
  - Leaf `41` `p0041-b0006`: VLM read `1891` vs PDF OCR witness `['1893']`
  - Leaf `111` `p0111-b0004`: VLM read `1000` vs PDF OCR witness `['1001']`
  - Leaf `112` `p0112-b0012`: VLM read `1627` vs PDF OCR witness `['1628']`
  - Leaf `112` `p0112-b0015`: VLM read `1712` vs PDF OCR witness `['1713', '1718']`
  - Leaf `112` `p0112-b0016`: VLM read `1712` vs PDF OCR witness `['1713', '1718']`
  - Leaf `112` `p0112-b0018`: VLM read `1719` vs PDF OCR witness `['1713', '1718', '1759']`
  - Leaf `112` `p0112-b0018`: VLM read `1738` vs PDF OCR witness `['1718', '1748']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `184` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `7` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`40` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"DS 436 H80 1907 UNIVERSITY OF CALIFORNIA, SAN DIEGO 3 1822 01153 9566"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Edward McNeill."*
  - Leaf `7` `p0007-b0002` (`noise`): *"—♦—"*
  - Leaf `9` `p0009-b0002` (`noise`): *"—♦—"*
  - Leaf `11` `p0011-b0002` (`noise`): *"—✦—"*
  - Leaf `19` `p0019-b0003` (`noise`): *"—"*
  - Leaf `19` `p0019-b0008` (`noise`): *"B"*
  - Leaf `21` `p0021-b0006` (`noise`): *"B 2"*
  - Leaf `35` `p0035-b0008` (`noise`): *"C"*
  - Leaf `51` `p0051-b0006` (`noise`): *"D"*
  - Leaf `53` `p0053-b0006` (`noise`): *"D 2"*
  - Leaf `67` `p0067-b0006` (`noise`): *"E"*
- **Unattested Line-Wrap Hyphenation Decisions (`76` unique words out of `664` total wraps)**: `educational` (p.9), `proofsheets` (p.9), `embody` (p.9), `pearshaped` (p.19), `feverbreeding` (p.22), `hillsides` (p.23), `everincreasing` (p.26), `riverchannels` (p.27), `darkbrown` (p.27), `plantains` (p.29), `highlying` (p.30), `landingstairs` (p.30), `vegetation` (p.31), `birthplace` (p.41), `Early-Metal` (p.42), `longhaired` (p.44), `smallbodied` (p.44), `childweddings` (p.47)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 437,015 chars
- **Distinct Non-ASCII Glyphs (`14` across `231` leaves)**: Á Í Ú á â æ ç é í ö ú ü œ ⅓
- **Corrections Replayed**: `16` applied, `0` orphaned/unmatched
