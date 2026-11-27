# Edition Verification & Run Audit — *The Religion of the Veda*

- **Book ID**: `religion-of-the-veda` | **Run ID**: `g38-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-3.8-flash on 321 of 322 pages, gemini-4-neon on 1 of 322 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `322` extracted, `12` blank/tissue, `0` failed (of `334` PDF leaves)
- **Tracked API Spend**: **`$1.1603`** (`76.1%` cached input tokens: `2,679,665` / `3,519,515` in, `348,969` out, `1,228` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 3.1% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 315 | `$0.9708` |
| `secondary_gemini_rescue` | 1 | `$0.0660` |
| `continuation_arbiter_batch` | 32 | `$0.0430` |
| `primary_quality_retry` | 7 | `$0.0377` |
| `page_extract_batch_vetoed` | 7 | `$0.0195` |
| `recitation_band_bot` | 3 | `$0.0122` |
| `recitation_band_top` | 3 | `$0.0112` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 321 pp., `gemini-4-neon`: 1 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `2` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `120` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`40` — catches smudged dates/figures in prose)**:
  - Leaf `37` `p0037-b0003`: VLM read `1824` vs PDF OCR witness `['1829']`
  - Leaf `48` `p0048-b0003`: VLM read `1200` vs PDF OCR witness `['1000', '1500', '1600']`
  - Leaf `207` `p0207-b0006`: VLM read `157` vs PDF OCR witness `['187']`
  - Leaf `319` `p0319-b0007`: VLM read `110` vs PDF OCR witness `['112', '120', '130']`
  - Leaf `319` `p0319-b0011`: VLM read `110` vs PDF OCR witness `['112', '120', '130']`
  - Leaf `319` `p0319-b0025`: VLM read `144` vs PDF OCR witness `['134', '141', '164']`
  - Leaf `319` `p0319-b0027`: VLM read `116` vs PDF OCR witness `['112', '126', '156']`
  - Leaf `320` `p0320-b0040`: VLM read `110` vs PDF OCR witness `['113', '115', '118']`
  - Leaf `320` `p0320-b0045`: VLM read `173` vs PDF OCR witness `['113', '133', '273']`
  - Leaf `321` `p0321-b0003`: VLM read `112` vs PDF OCR witness `['110', '152']`
  - Leaf `321` `p0321-b0046`: VLM read `186` vs PDF OCR witness `['106', '126', '185']`
  - Leaf `321` `p0321-b0046`: VLM read `188` vs PDF OCR witness `['108', '138', '148']`
  - Leaf `322` `p0322-b0007`: VLM read `111` vs PDF OCR witness `['118', '161']`
  - Leaf `322` `p0322-b0008`: VLM read `143` vs PDF OCR witness `['149']`
  - Leaf `322` `p0322-b0021`: VLM read `108` vs PDF OCR witness `['109', '118', '158']`
  - Leaf `322` `p0322-b0030`: VLM read `113` vs PDF OCR witness `['118', '213']`
  - Leaf `322` `p0322-b0037`: VLM read `179` vs PDF OCR witness `['109', '139', '149']`
  - Leaf `323` `p0323-b0010`: VLM read `131` vs PDF OCR witness `['130', '138']`
  - Leaf `323` `p0323-b0010`: VLM read `147` vs PDF OCR witness `['140', '143', '149']`
  - Leaf `323` `p0323-b0010`: VLM read `157` vs PDF OCR witness `['156', '177', '187']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `203` prose joins, `2` split footnotes stitched, `0` multi-page tables unified, `242` total footnotes.
  - Stitched cross-page footnotes: p.243->p.244 (`1`), p.282->p.283 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`61` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"TRINITY COLLEGE LIBRARY 3 1761 02718026 4"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"FROM K. KAWASE, KOBE [bookseller label]"*
  - Leaf `2` `p0002-b0003` (`scanner_residue`): *"Ex Libris THE CANADIAN SCHOOL OF MISSIONS"*
  - Leaf `2` `p0002-b0004` (`noise`): *"1930"*
  - Leaf `2` `p0002-b0005` (`scanner_residue`): *"Courtesy of The Estate of C.J.L. Bates"*
  - Leaf `3` `p0003-b0001` (`noise`): *"C. J. L. Bates Kwansei Gakuin Kobe, Nov. 21. 191"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"COLLEGIUM SACROSANCTÆ TRINITATIS APUD TORONTONENSES FROM THE LIBRARY OF TRINITY COLLEGE TO"*
  - Leaf `10` `p0010-b0002` (`noise`): *"——"*
  - Leaf `10` `p0010-b0012` (`noise`): *"——"*
  - Leaf `11` `p0011-b0003` (`noise`): *"—————"*
  - Leaf `11` `p0011-b0010` (`noise`): *"—"*
  - Leaf `12` `p0012-b0001` (`scanner_residue`): *"226"*
- **Unattested Line-Wrap Hyphenation Decisions (`154` unique words out of `978` total wraps)**: `amplification` (p.13), `Columbia` (p.19), `chromophotographic` (p.21), `ascetiism` (p.27), `supply` (p.31), `corrosive` (p.33), `cultivators` (p.35), `emancipated` (p.36), `latitudinarian` (p.36), `burning` (p.37), `frenzying` (p.37), `Artaphernes` (p.40), `artaof` (p.40), `Palestine` (p.42), `Drangiana` (p.42), `Graeco-Parthian` (p.42), `nevertheless` (p.44), `Venkan` (p.49)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 327,126 chars, `greek`: 311 chars, `hangul`: 1 chars
- **Distinct Non-ASCII Glyphs (`94` across `232` leaves)**: À Æ Ç à á ä æ ç é ë ï ñ ô ö ü Ā ā ē ę ī ĭ ō œ ũ ū ŭ ̯ Γ Δ Ζ Κ Ο ά έ ή ί α β γ δ ε ζ η θ ι κ λ μ ν ο π ρ ς σ τ υ φ χ ω ό
- **Corrections Replayed**: `30` applied, `0` orphaned/unmatched
