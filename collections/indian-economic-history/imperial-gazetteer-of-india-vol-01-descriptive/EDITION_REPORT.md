# Edition Verification & Run Audit — *The Imperial Gazetteer of India: The Indian Empire, Vol. I — Descriptive*

- **Book ID**: `imperial-gazetteer-of-india-vol-01-descriptive` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`89.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 607 of 607 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `607` extracted, `5` blank/tissue, `0` failed (of `612` PDF leaves)
- **Tracked API Spend**: **`$3.2901`** (`73.8%` cached input tokens: `5,018,263` / `6,801,080` in, `1,213,915` out, `1,100` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **14.0 / 25.0** | -8.0: 2 collapsed/jammed table row warning(s); -3.0: 2 ragged table geometry warning(s) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 579 | `$2.6874` |
| `primary_quality_retry` | 20 | `$0.1713` |
| `continuation_arbiter_batch` | 64 | `$0.1537` |
| `recitation_retry` | 8 | `$0.1216` |
| `page_extract_batch_vetoed` | 20 | `$0.0976` |
| `blind_totals_strip_batch` | 17 | `$0.0319` |
| `recitation_band_top` | 1 | `$0.0093` |
| `page_extract_batch_failed` | 8 | `$0.0090` |
| `recitation_band_bot` | 1 | `$0.0083` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 607 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `93, 192, 193, 528, 533, 536`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `582` via `recitation_2band_split` (`gemini-3.8-flash`)
- **450-DPI Blind Totals Strip Disagreements (`3`)**:
  - Leaf `553` `p0553-b0018`: full-page `['All ages . .', '40.6\n39.6', '38.6', '20.2\n19.1', '18.0', '']` vs blind-strip `['All ages . .', '40·6\n39·6', '38·6', '20·2\n19·1', '18·0', '', '', '', '', '.']`
  - Leaf `568` `p0568-b0015`: full-page `['India . .', '', '1,230', '10.8', '20.7', '9.3', '1.3', '70.7']` vs blind-strip `['India . .', '1,230', '10·8', '20·7', '9·3', '1·3', '70·7']`
  - Leaf `569` `p0569-b0028`: full-page `['1895–00', '39', '996', '2·1', '1·5', '9·1', '3·2', '5·0', '29·6']` vs blind-strip `['All India . }', '1881-94', '38', '1,099', '2.4', '2.8', '10.7', '2.1', '6.1', '33.8 }']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`193` — catches smudged dates/figures in prose)**:
  - Leaf `11` `p0011-b0003`: VLM read `1901` vs PDF OCR witness `['1900']`
  - Leaf `24` `p0024-b0011`: VLM read `101` vs PDF OCR witness `['100', '102', '104']`
  - Leaf `24` `p0024-b0012`: VLM read `101` vs PDF OCR witness `['100', '102', '104']`
  - Leaf `24` `p0024-b0013`: VLM read `101` vs PDF OCR witness `['100', '102', '104']`
  - Leaf `24` `p0024-b0032`: VLM read `111` vs PDF OCR witness `['110', '112', '113']`
  - Leaf `24` `p0024-b0036`: VLM read `115` vs PDF OCR witness `['105', '110', '112']`
  - Leaf `26` `p0026-b0008`: VLM read `137` vs PDF OCR witness `['136']`
  - Leaf `26` `p0026-b0009`: VLM read `138` vs PDF OCR witness `['136']`
  - Leaf `26` `p0026-b0010`: VLM read `138` vs PDF OCR witness `['136']`
  - Leaf `26` `p0026-b0011`: VLM read `138` vs PDF OCR witness `['136']`
  - Leaf `26` `p0026-b0012`: VLM read `139` vs PDF OCR witness `['136']`
  - Leaf `26` `p0026-b0013`: VLM read `139` vs PDF OCR witness `['136']`
  - Leaf `26` `p0026-b0014`: VLM read `139` vs PDF OCR witness `['136']`
  - Leaf `26` `p0026-b0026`: VLM read `146` vs PDF OCR witness `['136']`
  - Leaf `27` `p0027-b0037`: VLM read `199` vs PDF OCR witness `['169', '179', '189']`
  - Leaf `30` `p0030-b0014`: VLM read `304` vs PDF OCR witness `['300', '301', '303']`
  - Leaf `30` `p0030-b0015`: VLM read `304` vs PDF OCR witness `['300', '301', '303']`
  - Leaf `30` `p0030-b0016`: VLM read `305` vs PDF OCR witness `['300', '301', '303']`
  - Leaf `30` `p0030-b0027`: VLM read `314` vs PDF OCR witness `['310', '311', '313']`
  - Leaf `30` `p0030-b0028`: VLM read `314` vs PDF OCR witness `['310', '311', '313']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `413` prose joins, `3` split footnotes stitched, `1` multi-page tables unified, `155` total footnotes.
  - Stitched cross-page footnotes: p.153->p.154 (`1`), p.234->p.235 (`2`), p.567->p.568 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`182` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00114401 3"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"MICROFORMED BY PRESERVATION SERVICES DATE FEB 2 5 1987"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2013"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"http://archive.org/details/imperialgazette01hunt"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"MICROFILMED BY PRESERVATION SERVICES DATE... MAR 0 2 1987"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"In. I345"*
  - Leaf `7` `p0007-b0005` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `7` `p0007-b0011` (`scanner_residue`): *"91302 219108."*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed circular library stamp of the University of Toronto Library."*
  - Leaf `23` `p0023-b0047` (`noise`): *"vol. i."*
  - Leaf `23` `p0023-b0048` (`noise`): *"b"*
  - Leaf `25` `p0025-b0031` (`noise`): *"b 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`189` unique words out of `2211` total wraps)**: `nomination` (p.12), `undesirable` (p.15), `onwards` (p.17), `rockyserrated` (p.46), `countermarch` (p.47), `unconnected` (p.48), `deepcleft` (p.53), `cropproducing` (p.60), `siltcharged` (p.62), `flatroofed` (p.62), `benevolent` (p.62), `dustpowdered` (p.62), `thenceforward` (p.65), `abutting` (p.75), `roundness` (p.78), `decorative` (p.79), `interlace` (p.81), `pepperfestooned` (p.86)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 1,177,180 chars, `greek`: 72 chars
- **Distinct Non-ASCII Glyphs (`86` across `532` leaves)**: ¯ ± ´ · É à á â ä å æ ç è é ê ë í î ï ñ ö ü Ā ā ē ġ ħ ī ō œ Ś ś ū ʻ Μ Π ά έ ή ί α γ δ ε θ ι κ λ μ ν ο π ρ ς τ υ φ ό Ḍ ḍ
- **Corrections Replayed**: `86` applied, `0` orphaned/unmatched
