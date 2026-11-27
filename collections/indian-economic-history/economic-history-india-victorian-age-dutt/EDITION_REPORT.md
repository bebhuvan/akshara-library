# Edition Verification & Run Audit — *The Economic History of India in the Victorian Age*

- **Book ID**: `economic-history-india-victorian-age-dutt` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`98.5 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 651 of 651 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `651` extracted, `9` blank/tissue, `0` failed (of `660` PDF leaves)
- **Tracked API Spend**: **`$2.7009`** (`74.0%` cached input tokens: `5,153,316` / `6,962,174` in, `954,143` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **23.5 / 25.0** | -1.5: 1 ragged table geometry warning(s) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 651 | `$2.4857` |
| `continuation_arbiter_batch` | 79 | `$0.1334` |
| `blind_totals_strip` | 20 | `$0.0818` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 651 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `375, 558, 561`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`189` — catches smudged dates/figures in prose)**:
  - Leaf `14` `p0014-b0006`: VLM read `1894` vs PDF OCR witness `['1896']`
  - Leaf `28` `p0028-b0011`: VLM read `401` vs PDF OCR witness `['441']`
  - Leaf `40` `p0040-b0004`: VLM read `1844` vs PDF OCR witness `['1843']`
  - Leaf `56` `p0056-b0005`: VLM read `1853` vs PDF OCR witness `['1854', '1857']`
  - Leaf `71` `p0071-b0004`: VLM read `1842` vs PDF OCR witness `['1843']`
  - Leaf `72` `p0072-b0003`: VLM read `1849` vs PDF OCR witness `['1844']`
  - Leaf `89` `p0089-b0009`: VLM read `1844` vs PDF OCR witness `['1847']`
  - Leaf `94` `p0094-b0009`: VLM read `90,474` vs PDF OCR witness `['00474']`
  - Leaf `112` `p0112-b0003`: VLM read `1846` vs PDF OCR witness `['1806', '1842', '1847']`
  - Leaf `129` `p0129-b0012`: VLM read `1814` vs PDF OCR witness `['1813']`
  - Leaf `134` `p0134-b0008`: VLM read `100` vs PDF OCR witness `['106']`
  - Leaf `140` `p0140-b0004`: VLM read `100,000` vs PDF OCR witness `['400000']`
  - Leaf `143` `p0143-b0004`: VLM read `1813` vs PDF OCR witness `['1814', '1815', '1816']`
  - Leaf `155` `p0155-b0004`: VLM read `1846` vs PDF OCR witness `['1840', '1841', '1847']`
  - Leaf `155` `p0155-b0005`: VLM read `1836` vs PDF OCR witness `['1831']`
  - Leaf `159` `p0159-b0003`: VLM read `100` vs PDF OCR witness `['150', '400']`
  - Leaf `160` `p0160-b0017`: VLM read `1834` vs PDF OCR witness `['1837', '1838', '1839']`
  - Leaf `178` `p0178-b0005`: VLM read `120` vs PDF OCR witness `['180']`
  - Leaf `185` `p0185-b0026`: VLM read `1844` vs PDF OCR witness `['1840', '1841', '1842']`
  - Leaf `185` `p0185-b0026`: VLM read `1849` vs PDF OCR witness `['1839', '1840', '1841']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `464` prose joins, `4` split footnotes stitched, `0` multi-page tables unified, `513` total footnotes.
  - Stitched cross-page footnotes: p.61->p.62 (`1`), p.119->p.120 (`2`), p.198->p.199 (`4`), p.324->p.325 (`2`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`60` — verify no epigraph/dedication was caught)**:
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2007 with funding from Microsoft Corporation"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"http://www.archive.org/details/indiainvictorian00duttuoft"*
  - Leaf `9` `p0009-b0001` (`scanner_residue`): *"Ec. H D9793 ind"*
  - Leaf `9` `p0009-b0003` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `9` `p0009-b0011` (`scanner_residue`): *"62843 15/9/04"*
  - Leaf `10` `p0010-b0001` (`scanner_residue`): *"E.g. 33934"*
  - Leaf `10` `p0010-b0002` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `10` `p0010-b0004` (`scanner_residue`): *"no 20880 / P / 01"*
  - Leaf `21` `p0021-b0008` (`noise`): *"b"*
  - Leaf `29` `p0029-b0004` (`noise`): *"A"*
  - Leaf `31` `p0031-b0006` (`scanner_residue`): *"7"*
  - Leaf `45` `p0045-b0009` (`noise`): *"B"*
- **Unattested Line-Wrap Hyphenation Decisions (`89` unique words out of `1635` total wraps)**: `State-Loans` (p.23), `retribution` (p.38), `Haidarabad` (p.40), `misconduct` (p.49), `disinterested` (p.55), `Badshah` (p.55), `commanding` (p.56), `circumstanced` (p.68), `complimented` (p.75), `byelaws` (p.78), `compares` (p.79), `accruement` (p.84), `indestructible` (p.90), `supervised` (p.96), `condiment` (p.100), `maltreatment` (p.102), `corporate` (p.110), `conspicuous` (p.115)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 907,776 chars
- **Distinct Non-ASCII Glyphs (`15` across `21` leaves)**: Ü á â æ é ê ô ü ṭ „ ⁄ ⅓ ⅛ ⅜ ⅝
- **Corrections Replayed**: `11` applied, `0` orphaned/unmatched
