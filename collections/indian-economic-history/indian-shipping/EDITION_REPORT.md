# Edition Verification & Run Audit — *Indian Shipping*

- **Book ID**: `indian-shipping` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 330 of 330 pages. Declared reader profile: indic_script (new readings use gemini-4-hydrogen).
- **Pages**: `330` extracted, `28` blank/tissue, `0` failed (of `358` PDF leaves)
- **Tracked API Spend**: **`$5.2893`** (`3.8%` cached input tokens: `147,456` / `3,845,418` in, `376,912` out, `298,271` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 12.7% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 330 | `$5.2340` |
| `continuation_arbiter_batch` | 21 | `$0.0329` |
| `blind_totals_strip` | 2 | `$0.0224` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 330 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `8, 299, 313, 323`
- **450-DPI Blind Totals Strip Disagreements (`1`)**:
  - Leaf `280` `p0280-b0012`: full-page `['Total', '3231']` vs blind-strip `['Total', '323<sup>1</sup>']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`44` — catches smudged dates/figures in prose)**:
  - Leaf `99` `p0099-b0007`: VLM read `100` vs PDF OCR witness `['600']`
  - Leaf `204` `p0204-b0003`: VLM read `186` vs PDF OCR witness `['187']`
  - Leaf `249` `p0249-b0002`: VLM read `1457` vs PDF OCR witness `['1407']`
  - Leaf `253` `p0253-b0002`: VLM read `1510` vs PDF OCR witness `['1511']`
  - Leaf `253` `p0253-b0002`: VLM read `1521` vs PDF OCR witness `['1511', '1527', '1528']`
  - Leaf `264` `p0264-b0002`: VLM read `100` vs PDF OCR witness `['200']`
  - Leaf `266` `p0266-b0003`: VLM read `1590` vs PDF OCR witness `['1580']`
  - Leaf `269` `p0269-b0002`: VLM read `100` vs PDF OCR witness `['500']`
  - Leaf `279` `p0279-b0002`: VLM read `1661` vs PDF OCR witness `['1662']`
  - Leaf `296` `p0296-b0002`: VLM read `1710` vs PDF OCR witness `['1730', '1740']`
  - Leaf `296` `p0296-b0002`: VLM read `1712` vs PDF OCR witness `['1732']`
  - Leaf `301` `p0301-b0004`: VLM read `1615` vs PDF OCR witness `['1613']`
  - Leaf `305` `p0305-b0003`: VLM read `1800` vs PDF OCR witness `['1801']`
  - Leaf `305` `p0305-b0003`: VLM read `1821` vs PDF OCR witness `['1801']`
  - Leaf `308` `p0308-b0002`: VLM read `1813` vs PDF OCR witness `['1863']`
  - Leaf `308` `p0308-b0005`: VLM read `1811` vs PDF OCR witness `['1801']`
  - Leaf `330` `p0330-b0002`: VLM read `166` vs PDF OCR witness `['163']`
  - Leaf `332` `p0332-b0013`: VLM read `112` vs PDF OCR witness `['111']`
  - Leaf `333` `p0333-b0042`: VLM read `151` vs PDF OCR witness `['131', '181']`
  - Leaf `334` `p0334-b0021`: VLM read `119` vs PDF OCR witness `['112', '114', '116']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `145` prose joins, `7` split footnotes stitched, `2` multi-page tables unified, `407` total footnotes.
  - Stitched cross-page footnotes: p.93->p.94 (`1`), p.107->p.108 (`2`), p.129->p.130 (`4`), p.185->p.186 (`2`), p.211->p.212 (`1`), p.215->p.216 (`2`), p.294->p.295 (`2`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`77` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"SIGILLVM · VNIVERSITATIS · CALIFORNIENSIS · MDCCCLXVIII / FIAT LVX / EX LIBRIS"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2008 with funding from Microsoft Corporation"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"http://www.archive.org/details/indianshippinghi00mookrich"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"UNIV. OF CALIFORNIA"*
  - Leaf `9` `p0009-b0006` (`scanner_residue`): *"Perforated library stamp"*
  - Leaf `10` `p0010-b0001` (`scanner_residue`): *"HE 879 M6"*
  - Leaf `10` `p0010-b0003` (`scanner_residue`): *"UNIV. OF CALIFORNIA"*
  - Leaf `11` `p0011-b0003` (`scanner_residue`): *"255284"*
  - Leaf `17` `p0017-b0005` (`noise`): *"—"*
  - Leaf `22` `p0022-b0004` (`noise`): *"—"*
  - Leaf `23` `p0023-b0018` (`noise`): *"b"*
  - Leaf `27` `p0027-b0030` (`noise`): *"b 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`67` unique words out of `398` total wraps)**: `singlehanded` (p.13), `imperative` (p.21), `overlooked` (p.35), `civilizing` (p.37), `continuance` (p.42), `heaviness` (p.54), `disguise` (p.65), `expeditiously` (p.65), `directness` (p.66), `preservation` (p.66), `Vashishthiputra` (p.71), `contemplation` (p.75), `application` (p.75), `outflying` (p.81), `discharged` (p.86), `demarcate` (p.99), `Suvarṇapushkariṇī` (p.99), `concealment` (p.108)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 298,977 chars, `devanagari`: 5,378 chars, `bengali`: 500 chars
- **Distinct Non-ASCII Glyphs (`136` across `159` leaves)**: · á æ è é ñ ô ü Ā ā ē ī ń Ś ś Ū ū ँ ं ः अ आ इ ई उ ऊ ऋ ए ऐ क ख ग घ ङ च छ ज ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स
- **Corrections Replayed**: `2` applied, `0` orphaned/unmatched
