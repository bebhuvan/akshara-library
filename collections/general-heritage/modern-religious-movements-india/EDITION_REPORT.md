# Edition Verification & Run Audit — *Modern Religious Movements in India*

- **Book ID**: `modern-religious-movements-india` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 499 of 499 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `499` extracted, `19` blank/tissue, `0` failed (of `518` PDF leaves)
- **Tracked API Spend**: **`$8.4163`** (`4.5%` cached input tokens: `262,144` / `5,836,270` in, `616,986` out, `526,161` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 7.0% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 498 | `$8.3175` |
| `continuation_arbiter_batch` | 45 | `$0.0707` |
| `recitation_retry` | 1 | `$0.0195` |
| `page_extract_batch_failed` | 1 | `$0.0086` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 499 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `138, 235, 417`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`43` — catches smudged dates/figures in prose)**:
  - Leaf `19` `p0019-b0013`: VLM read `138` vs PDF OCR witness `['198']`
  - Leaf `133` `p0133-b0003`: VLM read `1846` vs PDF OCR witness `['1848']`
  - Leaf `160` `p0160-b0005`: VLM read `1885` vs PDF OCR witness `['1884', '1888']`
  - Leaf `184` `p0184-b0009`: VLM read `1887` vs PDF OCR witness `['1888']`
  - Leaf `208` `p0208-b0003`: VLM read `1880` vs PDF OCR witness `['1882']`
  - Leaf `230` `p0230-b0005`: VLM read `1873` vs PDF OCR witness `['1872', '1875', '1879']`
  - Leaf `243` `p0243-b0003`: VLM read `1900` vs PDF OCR witness `['1902']`
  - Leaf `255` `p0255-b0008`: VLM read `225` vs PDF OCR witness `['215', '226']`
  - Leaf `255` `p0255-b0010`: VLM read `211` vs PDF OCR witness `['215']`
  - Leaf `289` `p0289-b0005`: VLM read `1885` vs PDF OCR witness `['1884']`
  - Leaf `398` `p0398-b0003`: VLM read `1882` vs PDF OCR witness `['1888']`
  - Leaf `433` `p0433-b0005`: VLM read `1888` vs PDF OCR witness `['1882', '1887', '1898']`
  - Leaf `438` `p0438-b0006`: VLM read `1887` vs PDF OCR witness `['1884']`
  - Leaf `498` `p0498-b0010`: VLM read `452` vs PDF OCR witness `['456']`
  - Leaf `503` `p0503-b0010`: VLM read `390` vs PDF OCR witness `['300', '320', '360']`
  - Leaf `503` `p0503-b0018`: VLM read `355` vs PDF OCR witness `['305', '351', '353']`
  - Leaf `503` `p0503-b0026`: VLM read `111` vs PDF OCR witness `['101', '113', '115']`
  - Leaf `503` `p0503-b0029`: VLM read `419` vs PDF OCR witness `['410', '412', '439']`
  - Leaf `503` `p0503-b0030`: VLM read `435` vs PDF OCR witness `['433', '434', '438']`
  - Leaf `503` `p0503-b0030`: VLM read `390` vs PDF OCR witness `['300', '320', '360']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `342` prose joins, `1` split footnotes stitched, `0` multi-page tables unified, `618` total footnotes.
  - Stitched cross-page footnotes: p.291->p.292 (`5`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`39` — verify no epigraph/dedication was caught)**:
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2007 with funding from Microsoft Corporation"*
  - Leaf `5` `p0005-b0002` (`scanner_residue`): *"http://www.archive.org/details/modernreligiousm00farqiala"*
  - Leaf `9` `p0009-b0001` (`scanner_residue`): *"LIBRARY UNIVERSITY OF CALIFORNIA SANTA BARBARA"*
  - Leaf `21` `p0021-b0007` (`noise`): *"B"*
  - Leaf `37` `p0037-b0007` (`noise`): *"c"*
  - Leaf `53` `p0053-b0008` (`noise`): *"D"*
  - Leaf `73` `p0073-b0008` (`noise`): *"E"*
  - Leaf `91` `p0091-b0007` (`noise`): *"F"*
  - Leaf `109` `p0109-b0010` (`noise`): *"G"*
  - Leaf `125` `p0125-b0008` (`noise`): *"H"*
  - Leaf `143` `p0143-b0008` (`noise`): *"I"*
  - Leaf `159` `p0159-b0008` (`noise`): *"K"*
- **Unattested Line-Wrap Hyphenation Decisions (`163` unique words out of `1697` total wraps)**: `varying` (p.11), `forthcoming` (p.12), `compress` (p.14), `Friedrich` (p.28), `Lansdowne` (p.47), `journalistic` (p.56), `unchanging` (p.56), `transgressions` (p.58), `abstain` (p.62), `crowning` (p.73), `intercaste` (p.73), `disunion` (p.75), `inculcated` (p.75), `substituting` (p.75), `forgiving` (p.85), `Comorin` (p.87), `vouchsafed` (p.89), `unutterable` (p.92)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 711,854 chars
- **Distinct Non-ASCII Glyphs (`37` across `365` leaves)**: à æ ç è é ê í ñ ô ö ú ü Ā ā Ī ī Ś ś ū ḍ Ḥ ḥ ḵ ḷ Ṁ ṁ ṅ Ṇ ṇ Ṛ ṛ Ṣ ṣ Ṭ ṭ ẖ ⅖
- **Corrections Replayed**: `4` applied, `0` orphaned/unmatched
