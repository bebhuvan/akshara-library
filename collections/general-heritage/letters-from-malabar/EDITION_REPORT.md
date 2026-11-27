# Edition Verification & Run Audit — *Letters from Malabar*

- **Book ID**: `letters-from-malabar` | **Run ID**: `g38-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 204 of 204 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `204` extracted, `0` blank/tissue, `0` failed (of `204` PDF leaves)
- **Tracked API Spend**: **`$0.7883`** (`75.2%` cached input tokens: `1,631,796` / `2,168,611` in, `280,132` out, `299` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 0.5% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 204 | `$0.7458` |
| `continuation_arbiter_batch` | 31 | `$0.0425` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 204 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`19` — catches smudged dates/figures in prose)**:
  - Leaf `15` `p0015-b0013`: VLM read `118` vs PDF OCR witness `['110', '114']`
  - Leaf `35` `p0035-b0004`: VLM read `1716` vs PDF OCR witness `['1715']`
  - Leaf `50` `p0050-b0007`: VLM read `1708` vs PDF OCR witness `['1718']`
  - Leaf `51` `p0051-b0010`: VLM read `1687` vs PDF OCR witness `['1681', '1683']`
  - Leaf `51` `p0051-b0011`: VLM read `1687` vs PDF OCR witness `['1681', '1683']`
  - Leaf `51` `p0051-b0012`: VLM read `1667` vs PDF OCR witness `['1663', '1668', '1669']`
  - Leaf `51` `p0051-b0013`: VLM read `1667` vs PDF OCR witness `['1663', '1668', '1669']`
  - Leaf `51` `p0051-b0017`: VLM read `1665` vs PDF OCR witness `['1663', '1668', '1669']`
  - Leaf `51` `p0051-b0018`: VLM read `1667` vs PDF OCR witness `['1663', '1668', '1669']`
  - Leaf `63` `p0063-b0003`: VLM read `14,000` vs PDF OCR witness `['15000']`
  - Leaf `108` `p0108-b0005`: VLM read `1599` vs PDF OCR witness `['1699']`
  - Leaf `122` `p0122-b0006`: VLM read `300` vs PDF OCR witness `['800']`
  - Leaf `158` `p0158-b0004`: VLM read `872,600` vs PDF OCR witness `['872000']`
  - Leaf `165` `p0165-b0003`: VLM read `100` vs PDF OCR witness `['200', '300']`
  - Leaf `165` `p0165-b0006`: VLM read `210` vs PDF OCR witness `['200']`
  - Leaf `174` `p0174-b0005`: VLM read `6,000` vs PDF OCR witness `['5000']`
  - Leaf `175` `p0175-b0003`: VLM read `3,000` vs PDF OCR witness `['4000', '5000', '6000']`
  - Leaf `181` `p0181-b0003`: VLM read `5,000` vs PDF OCR witness `['6000']`
  - Leaf `184` `p0184-b0003`: VLM read `1780` vs PDF OCR witness `['1760']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `123` prose joins, `4` split footnotes stitched, `1` multi-page tables unified, `42` total footnotes.
  - Stitched cross-page footnotes: p.26->p.27 (`†`), p.109->p.110 (`*`), p.161->p.162 (`*`), p.164->p.165 (`*`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`261` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"Digitized by Google"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"816 / 561"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"Scanner book holder tab"*
  - Leaf `2` `p0002-b0003` (`scanner_residue`): *"15. 3. 305."*
  - Leaf `2` `p0002-b0004` (`scanner_residue`): *"15. 3. 305."*
  - Leaf `2` `p0002-b0005` (`scanner_residue`): *"Scanner book holder tab"*
  - Leaf `2` `p0002-b0006` (`scanner_residue`): *"Digitized by Google"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"12 3 392"*
  - Leaf `3` `p0003-b0002` (`scanner_residue`): *"Digitized by Google"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by Google"*
  - Leaf `5` `p0005-b0013` (`noise`): *"wwwwwwwwwwwwwwwwwwww"*
  - Leaf `5` `p0005-b0015` (`scanner_residue`): *"Digitized by Google"*
- **Unattested Line-Wrap Hyphenation Decisions (`175` unique words out of `1130` total wraps)**: `vandalism` (p.8), `Mountaineers` (p.17), `enlargements` (p.22), `Hydaspes` (p.23), `everincreasing` (p.25), `plastered` (p.28), `Karrekovre` (p.29), `serving` (p.34), `Mangatatya` (p.35), `diversion` (p.36), `obstructing` (p.36), `achieved` (p.37), `Avatorti` (p.37), `advantageous` (p.38), `Tranquebar` (p.39), `inserted` (p.41), `Salsette` (p.42), `dissipation` (p.44)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 354,025 chars
- **Distinct Non-ASCII Glyphs (`16` across `23` leaves)**: à á â æ ç è é ô û ā ę œ „ ′ ⁄ ⅓
- **Corrections Replayed**: `24` applied, `0` orphaned/unmatched
