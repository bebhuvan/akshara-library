# Edition Verification & Run Audit — *The English Factories in India, 1622–1623*

- **Book ID**: `english-factories-india-1622-1623-vol-02` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`86.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 429 of 430 pages, gemini-3.6-flash on 1 of 430 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `430` extracted, `0` blank/tissue, `0` failed (of `430` PDF leaves)
- **Tracked API Spend**: **`$2.4750`** (`68.6%` cached input tokens: `3,455,203` / `5,037,948` in, `735,613` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **11.0 / 25.0** | -3.0: 1 script/codepoint anomaly(ies); -6.0: 3 intra-book diacritic drift cluster(s); -5.0: 362 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Standardize or verify 3 proper-noun diacritic drift cluster(s).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 398 | `$1.5952` |
| `primary_quality_retry` | 33 | `$0.4269` |
| `recitation_band_top` | 14 | `$0.1434` |
| `page_extract_batch_vetoed` | 32 | `$0.1306` |
| `recitation_band_bot` | 12 | `$0.1188` |
| `continuation_arbiter_batch` | 17 | `$0.0237` |
| `secondary_gemini_rescue` | 2 | `$0.0196` |
| `page_extract_failed` | 1 | `$0.0130` |
| `blind_totals_strip` | 1 | `$0.0038` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 1 pp., `gemini-3.8-flash`: 429 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `395`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `22` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `78` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `127` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `131` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `135` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `176` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `234` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `244` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `255` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `270` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `318` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `342` via `recitation_2band_split` (`gemini-3.8-flash`)

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `225` prose joins, `5` split footnotes stitched, `0` multi-page tables unified, `296` total footnotes.
  - Stitched cross-page footnotes: p.28->p.29 (`1`), p.55->p.56 (`1`), p.136->p.137 (`1`), p.283->p.284 (`2`), p.290->p.291 (`3`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`129` — verify no epigraph/dedication was caught)**:
  - Leaf `3` `p0003-b0002` (`scanner_residue`): *"Perforated library stamp pattern"*
  - Leaf `3` `p0003-b0003` (`scanner_residue`): *"Digitization target / barcode residue"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Lit Com. Sotheran 12-8-27 15843"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"D 12-14-27 apg"*
  - Leaf `9` `p0009-b0005` (`scanner_residue`): *"Digitization residue / finger-cot mark"*
  - Leaf `16` `p0016-b0005` (`noise`): *"FOSTER II."*
  - Leaf `16` `p0016-b0006` (`noise`): *"b"*
  - Leaf `18` `p0018-b0007` (`noise`): *"b 2"*
  - Leaf `25` `p0025-b0007` (`scanner_residue`): *"Black corner artifact/calibration triangle from scanner edge."*
  - Leaf `29` `p0029-b0006` (`scanner_residue`): *"black mark/thumb cutout residue"*
  - Leaf `32` `p0032-b0007` (`noise`): *"Foster. II."*
  - Leaf `32` `p0032-b0008` (`noise`): *"c"*
- **Unattested Line-Wrap Hyphenation Decisions (`86` unique words out of `568` total wraps)**: `strenuously` (p.8), `relegated` (p.12), `withdrawing` (p.18), `battleground` (p.22), `affectionate` (p.23), `strengthening` (p.25), `consternation` (p.29), `cashbox` (p.38), `Vangerlee` (p.46), `complymentall` (p.49), `contrye` (p.55), `Cottonwool` (p.62), `Costake` (p.70), `com-m` (p.72), `unhumanly` (p.77), `moneychanger` (p.85), `remembrence` (p.88), `restoreinge` (p.97)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 748,150 chars, `cyrillic`: 4 chars
- **Distinct Non-ASCII Glyphs (`28` across `341` leaves)**: · á ã ç é ñ ô Ā ā ē Ġ ġ Ī ī Ō ō ũ ū ſ г е н о ′ ⁄ ⅓ ⅛ ⅝
- **Corrections Replayed**: `77` applied, `0` orphaned/unmatched
