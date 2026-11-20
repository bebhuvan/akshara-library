# Edition Verification & Run Audit — *The Periplus of the Erythræan Sea: Travel and Trade in the Indian Ocean by a Merchant of the First Century*

- **Book ID**: `periplus-erythraean-sea` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`98.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 331 of 331 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen). This edition predates that choice and has not been re-read with gemini-4-hydrogen.
- **Pages**: `331` extracted, `11` blank/tissue, `0` failed (of `342` PDF leaves)
- **Tracked API Spend**: **`$1.6086`** (`77.7%` cached input tokens: `2,548,700` / `3,280,144` in, `607,577` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **23.0 / 25.0** | -2.0: 1 intra-book diacritic drift cluster(s) |

### Recommended Operator Next Actions
- Standardize or verify 1 proper-noun diacritic drift cluster(s).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 331 | `$1.6046` |
| `continuation_arbiter` | 1 | `$0.0040` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 331 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `103, 105, 110, 216, 241`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`38` — catches smudged dates/figures in prose)**:
  - Leaf `224` `p0224-b0006`: VLM read `5,000` vs PDF OCR witness `['3000', '4000']`
  - Leaf `278` `p0278-b0002`: VLM read `573` vs PDF OCR witness `['578']`
  - Leaf `305` `p0305-b0007`: VLM read `203` vs PDF OCR witness `['103', '200', '202']`
  - Leaf `308` `p0308-b0070`: VLM read `133` vs PDF OCR witness `['123', '130', '132']`
  - Leaf `308` `p0308-b0079`: VLM read `133` vs PDF OCR witness `['123', '130', '132']`
  - Leaf `310` `p0310-b0092`: VLM read `258` vs PDF OCR witness `['208', '218', '228']`
  - Leaf `311` `p0311-b0041`: VLM read `154` vs PDF OCR witness `['144', '151', '152']`
  - Leaf `312` `p0312-b0075`: VLM read `153` vs PDF OCR witness `['103', '113', '123']`
  - Leaf `312` `p0312-b0098`: VLM read `133` vs PDF OCR witness `['103', '113', '123']`
  - Leaf `313` `p0313-b0068`: VLM read `233` vs PDF OCR witness `['203', '213', '223']`
  - Leaf `313` `p0313-b0076`: VLM read `151` vs PDF OCR witness `['101', '111', '121']`
  - Leaf `315` `p0315-b0006`: VLM read `212` vs PDF OCR witness `['202', '210', '211']`
  - Leaf `315` `p0315-b0072`: VLM read `255` vs PDF OCR witness `['205', '235', '245']`
  - Leaf `316` `p0316-b0002`: VLM read `237` vs PDF OCR witness `['217', '227', '230']`
  - Leaf `316` `p0316-b0034`: VLM read `182` vs PDF OCR witness `['112', '122', '132']`
  - Leaf `318` `p0318-b0049`: VLM read `255` vs PDF OCR witness `['205', '215', '225']`
  - Leaf `318` `p0318-b0107`: VLM read `113` vs PDF OCR witness `['103', '111', '114']`
  - Leaf `319` `p0319-b0005`: VLM read `252` vs PDF OCR witness `['152', '242', '253']`
  - Leaf `319` `p0319-b0027`: VLM read `255` vs PDF OCR witness `['155', '205', '225']`
  - Leaf `319` `p0319-b0053`: VLM read `178` vs PDF OCR witness `['108', '118', '128']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `195` prose joins, `0` split footnotes stitched, `1` multi-page tables unified, `3` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`10` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"22101438235"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2017 with funding from Wellcome Library"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"https://archive.org/details/b29353051"*
  - Leaf `8` `p0008-b0002` (`scanner_residue`): *"WELLCOME LIBRARY INSTITUTE"*
  - Leaf `8` `p0008-b0003` (`scanner_residue`): *"O. Top. 362"*
  - Leaf `32` `p0032-b0003` (`noise`): *"—"*
  - Leaf `60` `p0060-b0003` (`noise`): *"—"*
  - Leaf `64` `p0064-b0003` (`noise`): *"————"*
  - Leaf `228` `p0228-b0004` (`noise`): *"———"*
  - Leaf `280` `p0280-b0008` (`noise`): *"————"*
- **Unattested Line-Wrap Hyphenation Decisions (`164` unique words out of `1108` total wraps)**: `manufacturer` (p.11), `inquirer` (p.11), `shoaling` (p.14), `glittered` (p.15), `navigator` (p.16), `unreliable` (p.19), `copyist` (p.20), `engaged` (p.21), `Eudae-mon` (p.22), `inquiry` (p.22), `conflagration` (p.23), `torment` (p.23), `ingenious` (p.25), `Na-poleon` (p.27), `Four-teenth` (p.27), `Hud-sonus` (p.28), `modification` (p.30), `Unbekann-ten` (p.30)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 548,467 chars
- **Distinct Non-ASCII Glyphs (`43` across `270` leaves)**: · Æ Ç á â ã ä æ ç è é ê ë í î ï ó ô õ ö ú ü ý ā ē ġ ī ō œ ť ū ʻ ʼ ˙ ḍ ṅ ṇ ṣ ṭ ′ ⅓ ⅔ ⅙
- **Corrections Replayed**: `40` applied, `0` orphaned/unmatched
