# Edition Verification & Run Audit — *A Journey from Madras through the Countries of Mysore, Canara, and Malabar*

- **Book ID**: `journey-from-madras-vol-iii` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`78.0 / 100`** (`community`)
- **Reader**: Read by gemini-4-hydrogen on 568 of 570 pages, gemini-3.6-flash on 2 of 570 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `570` extracted, `26` blank/tissue, `0` failed (of `596` PDF leaves)
- **Tracked API Spend**: **`$16.3003`** (`6.4%` cached input tokens: `476,492` / `7,449,043` in, `1,655,309` out, `842,399` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **8.0 / 25.0** | -12.0: 82 column total arithmetic mismatch(es); -5.0: 8 ragged table geometry warning(s) |
| **4. Orthographic, Script & Diacritics** | **20.0 / 25.0** | -5.0: 83 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 561 | `$11.7811` |
| `max_tokens_retry` | 9 | `$1.7438` |
| `max_tokens_64k_retry` | 2 | `$0.7800` |
| `continuation_arbiter_batch` | 68 | `$0.7526` |
| `page_extract_batch_failed` | 9 | `$0.6231` |
| `blind_totals_strip` | 29 | `$0.3901` |
| `secondary_gemini_rescue` | 2 | `$0.2296` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 2 pp., `gemini-4-hydrogen`: 568 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `53, 220, 221, 222, 224, 261, 273, 274, 275, 351, 373`
- **450-DPI Blind Totals Strip Disagreements (`7`)**:
  - Leaf `13` `p0013-b0094`: full-page `['Total ........', '13641', '6', '21025', '1', '2', '68903', '3', '10347', '7 15', '11372', '9', '1']` vs blind-strip `['Total .........', '13641', '6', '2', '1025', '1', '2', '.....................................', '68903', '—', '3', '10347', '7', '15', '11372', '9', '1']`
  - Leaf `121` `p0121-b0016`: full-page `['General Total', '1043 1½', '26,076', '24 30', '32,311875', '42 0', '1,24', '551 24½', '717,552', '227 21½', '296,334', '71 0', '1¾', '30 11', '5½', '22 8/40', '27,5', '11,36', '1', '8', '7½']` vs blind-strip `['General Total', '1043 1½', '26,076', '24 30', '32,311875', '42 0', '1,24', '551 24½', '717,552', '227 21½', '296,334', '71', '0 1⅗', '30 11 5¼', '22 ½/40', '27,5', '11,36', '1 8 7½']`
  - Leaf `121` `p0121-b0048`: full-page `['General total', '3669 -', '91,728', '58 15', '0,829', '894 0', '12,692', '1', '4', '6¼', '1651 14', '41,22', '25 20', '0,804', '285 30', '9,009', '0', '17', '5', '2068 6', '51,7', '31 2½', '0,782', '146 20', '3,795', '0', '7', '1¾', '7389 6', '184,74', '114 37¼', '0,81', '1326 10', '9,48', '0', '18', '1']` vs blind-strip `['General total', '3669 —', '91,728', '58 15', '0,829', '894 0', '12,692', '1 4 6½', '1651 14', '41,22', '25 20', '0,804', '285 30', '9,009', '0 17 5', '2068 6', '51,7', '31 2½', '0,782', '146 20', '3,795', '0 7 1½', '7389 6', '184,74', '114 37½', '0,81', '1326 10', '9,48', '0 18 1']`
  - Leaf `224` `p0224-b0025`: full-page `['Total value in Rupees', '44585', '', '331532']` vs blind-strip `['Total value in']`
  - Leaf `275` `p0275-b0030`: full-page `['Total value imports Rupees', '—', '108045', 'Total value exports Rupees', '—', '963833']` vs blind-strip `['mports', '—', '—', '—', '—', '—', '—', '—', '—', '—', '—', '49', '—', '—', '—', '—', '1', '—', '8', '1', '—', '—', '—']`
  - Leaf `491` `p0491-b0015`: full-page `['', '14¾;']` vs blind-strip `['14¾ ;']`
  - Leaf `493` `p0493-b0029`: full-page `['leaves a balance of   Fanams,', '1225']` vs blind-strip `['leaves a balance of', '&#45;', '<i>Fanams</i>,', '1225']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`522` — catches smudged dates/figures in prose)**:
  - Leaf `6` `p0006-b0020`: VLM read `1000` vs PDF OCR witness `['1800']`
  - Leaf `7` `p0007-b0007`: VLM read `111,` vs PDF OCR witness `['181']`
  - Leaf `19` `p0019-b0014`: VLM read `161` vs PDF OCR witness `['111', '151', '160']`
  - Leaf `19` `p0019-b0020`: VLM read `2307` vs PDF OCR witness `['2377']`
  - Leaf `19` `p0019-b0023`: VLM read `1718` vs PDF OCR witness `['3718']`
  - Leaf `19` `p0019-b0031`: VLM read `417` vs PDF OCR witness `['410', '414', '517']`
  - Leaf `19` `p0019-b0034`: VLM read `1147` vs PDF OCR witness `['1117']`
  - Leaf `20` `p0020-b0019`: VLM read `261` vs PDF OCR witness `['265']`
  - Leaf `21` `p0021-b0007`: VLM read `160` vs PDF OCR witness `['100', '110', '140']`
  - Leaf `25` `p0025-b0004`: VLM read `961` vs PDF OCR witness `['966']`
  - Leaf `25` `p0025-b0004`: VLM read `179` vs PDF OCR witness `['178']`
  - Leaf `41` `p0041-b0004`: VLM read `1000` vs PDF OCR witness `['1800']`
  - Leaf `41` `p0041-b0006`: VLM read `1000` vs PDF OCR witness `['1800']`
  - Leaf `41` `p0041-b0007`: VLM read `1000` vs PDF OCR witness `['1800']`
  - Leaf `42` `p0042-b0005`: VLM read `1723` vs PDF OCR witness `['1722']`
  - Leaf `42` `p0042-b0005`: VLM read `1723` vs PDF OCR witness `['1722']`
  - Leaf `65` `p0065-b0004`: VLM read `100` vs PDF OCR witness `['106']`
  - Leaf `65` `p0065-b0004`: VLM read `136` vs PDF OCR witness `['106']`
  - Leaf `114` `p0114-b0004`: VLM read `2657` vs PDF OCR witness `['2655']`
  - Leaf `120` `p0120-b0006`: VLM read `100` vs PDF OCR witness `['102']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `345` prose joins, `0` split footnotes stitched, `20` multi-page tables unified, `2` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`136` — verify no epigraph/dedication was caught)**:
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"LIBRARY OF PRINCETON OCT 17 1913 THEOLOGICAL SEMINARY"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2016"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"https://archive.org/details/journeyfrommadra03hami_2"*
  - Leaf `7` `p0007-b0008` (`noise`): *"VOL. III."*
  - Leaf `7` `p0007-b0009` (`noise`): *"B"*
  - Leaf `11` `p0011-b0137` (`noise`): *"VOL. III."*
  - Leaf `13` `p0013-b0095` (`noise`): *"VOL. III."*
  - Leaf `15` `p0015-b0130` (`noise`): *"Vol. III."*
  - Leaf `17` `p0017-b0130` (`noise`): *"VOL. III."*
  - Leaf `23` `p0023-b0008` (`noise`): *"Vol. III. C"*
  - Leaf `31` `p0031-b0007` (`noise`): *"VOL. III."*
  - Leaf `31` `p0031-b0008` (`noise`): *"D"*
- **Unattested Line-Wrap Hyphenation Decisions (`91` unique words out of `1542` total wraps)**: `conformable` (p.19), `inveigled` (p.25), `beforementioned` (p.29), `delinquents` (p.38), `Panch-Drávida` (p.45), `compost` (p.59), `Gungasir` (p.68), `Æschynomene` (p.71), `Sómasékara` (p.79), `contradiction` (p.84), `Umblica` (p.84), `completed` (p.85), `Dharmastulla` (p.86), `ostentation` (p.89), `eternal` (p.94), `Gótram` (p.113), `Hucabuca` (p.115), `Gódávéry` (p.116)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 879,722 chars, `greek`: 7 chars
- **Distinct Non-ASCII Glyphs (`35` across `391` leaves)**: Æ á â ä æ é ë í ó ù ú ā œ ŕ ŭ ſ ε ι ν ο ρ ἱ ⁄ ₀ ₁ ⅓ ⅔ ⅕ ⅖ ⅗ ⅘ ⅙ ⅛ ⅜ ⅞
- **Corrections Replayed**: `151` applied, `0` orphaned/unmatched
