# Edition Verification & Run Audit — *The Early History of India*

- **Book ID**: `early-history-of-india-1924` | **Run ID**: `g38-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`community`** | **Rubric Score**: **`88.8 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 559 of 575 pages, gemini-3.6-flash on 16 of 575 pages. Declared reader profile: transliteration (new readings use gemini-3.8-flash).
- **Pages**: `575` extracted, `21` blank/tissue, `0` failed (of `596` PDF leaves)
- **Tracked API Spend**: **`$3.2674`** (`71.3%` cached input tokens: `4,551,700` / `6,381,268` in, `1,190,120` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **19.0 / 25.0** | -6.0: 2 unresolved footnote callout/body mismatch(es) |
| **3. Tabular & Numerical Accuracy** | **20.0 / 25.0** | -5.0: 4 ragged table geometry warning(s) |
| **4. Orthographic, Script & Diacritics** | **24.8 / 25.0** | -0.2: 1 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells in Static Proofing UI ('Needs A Pair of Eyes').
- Resolve 2 unmatched footnote marker(s) via anchor-matched corrections.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 559 | `$2.5953` |
| `continuation_arbiter_batch` | 156 | `$0.4102` |
| `secondary_gemini_rescue` | 16 | `$0.1734` |
| `page_extract_batch_vetoed` | 16 | `$0.0827` |
| `blind_totals_strip` | 1 | `$0.0058` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 16 pp., `gemini-3.8-flash`: 559 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `297, 323, 434, 494, 537, 549`
- **450-DPI Blind Totals Strip Disagreements (`1`)**:
  - Leaf `75` `p0075-b0012`: full-page `['', 'Total . .\nAverage .', '321\n32·1', 'c. 229\n22·9\n(maximum\npossible\n25·0)', 'The Matsya assigns either\n360 or ? 163 (Pargiter, p.\n69) to the dynasty, as a\nwhole.']` vs blind-strip `['<i>Total</i> . .', '<b>321</b>', '<i>c.</i> <b>229</b>', 'ity : 57 years allowed.']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`305` — catches smudged dates/figures in prose)**:
  - Leaf `17` `p0017-b0007`: VLM read `326` vs PDF OCR witness `['322']`
  - Leaf `18` `p0018-b0014`: VLM read `320` vs PDF OCR witness `['820']`
  - Leaf `18` `p0018-b0020`: VLM read `374` vs PDF OCR witness `['373']`
  - Leaf `18` `p0018-b0023`: VLM read `453` vs PDF OCR witness `['455', '456']`
  - Leaf `19` `p0019-b0019`: VLM read `340` vs PDF OCR witness `['300', '640', '840']`
  - Leaf `24` `p0024-b0008`: VLM read `325` vs PDF OCR witness `['825']`
  - Leaf `26` `p0026-b0010`: VLM read `453` vs PDF OCR witness `['458']`
  - Leaf `26` `p0026-b0010`: VLM read `543` vs PDF OCR witness `['548']`
  - Leaf `32` `p0032-b0004`: VLM read `326` vs PDF OCR witness `['826']`
  - Leaf `34` `p0034-b0009`: VLM read `403` vs PDF OCR witness `['401', '408']`
  - Leaf `36` `p0036-b0006`: VLM read `399` vs PDF OCR witness `['899']`
  - Leaf `41` `p0041-b0011`: VLM read `323` vs PDF OCR witness `['328']`
  - Leaf `41` `p0041-b0013`: VLM read `138` vs PDF OCR witness `['188']`
  - Leaf `46` `p0046-b0015`: VLM read `103` vs PDF OCR witness `['108']`
  - Leaf `47` `p0047-b0014`: VLM read `130` vs PDF OCR witness `['180']`
  - Leaf `47` `p0047-b0014`: VLM read `131` vs PDF OCR witness `['181']`
  - Leaf `47` `p0047-b0017`: VLM read `1903` vs PDF OCR witness `['1908', '1913']`
  - Leaf `50` `p0050-b0005`: VLM read `1853` vs PDF OCR witness `['1858']`
  - Leaf `52` `p0052-b0003`: VLM read `326` vs PDF OCR witness `['826']`
  - Leaf `53` `p0053-b0006`: VLM read `330` vs PDF OCR witness `['370', '830']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `342` prose joins, `67` split footnotes stitched, `4` multi-page tables unified, `919` total footnotes.
  - Stitched cross-page footnotes: p.32->p.33 (`2`), p.42->p.43 (`2`), p.57->p.58 (`3`), p.62->p.63 (`1`), p.64->p.65 (`1`), p.67->p.68 (`3`), p.72->p.73 (`2`), p.76->p.77 (`3`), p.80->p.81 (`2`), p.86->p.87 (`1`), p.104->p.105 (`2`), p.108->p.109 (`2`), p.137->p.138 (`2`), p.138->p.139 (`1`), p.157->p.158 (`3`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`117` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00115364 2"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2026 with funding from University of Toronto"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"https://archive.org/details/earlyhistoryofin0000smit_e6k6"*
  - Leaf `11` `p0011-b0001` (`scanner_residue`): *"Hin S 6626 e. 3"*
  - Leaf `11` `p0011-b0005` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY embossed blind stamp"*
  - Leaf `11` `p0011-b0012` (`scanner_residue`): *"195939 11. 5. 25"*
  - Leaf `12` `p0012-b0001` (`scanner_residue`): *"Embossed library stamp: LIBRARY OF THE UNIVERSITY OF TORONTO"*
  - Leaf `12` `p0012-b0003` (`scanner_residue`): *"DS 451 S65 1924 cop. 2"*
  - Leaf `13` `p0013-b0005` (`noise`): *"2656"*
  - Leaf `23` `p0023-b0009` (`noise`): *"2656"*
  - Leaf `23` `p0023-b0010` (`noise`): *"B"*
  - Leaf `25` `p0025-b0010` (`noise`): *"B 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`330` unique words out of `3101` total wraps)**: `bedrock` (p.24), `Marātha` (p.27), `Tungabhadra` (p.29), `disentanglement` (p.30), `revolutionary` (p.30), `répertoire` (p.32), `sinologists` (p.36), `familiarly` (p.37), `stratification` (p.38), `indischer` (p.41), `satisfactorily` (p.42), `synchron` (p.45), `Vishṇupurāṇa` (p.47), `susceptible` (p.52), `impossibility` (p.52), `Nieuw-Indische` (p.53), `companies` (p.57), `Battacharya` (p.58)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 1,011,293 chars, `greek`: 4,023 chars, `hangul`: 2 chars, `other`: 1 chars
- **Distinct Non-ASCII Glyphs (`196` across `533` leaves)**: · Ç É Ü à á â ä ç è é ê ë î ï ñ ó ô ö û ü Ā ā ă č Ē ē ġ ĥ Ī ī Ł Ń Ō ō Ő ő Œ œ ŕ Ś ś š Ū ū ŭ ʻ ̄ ΐ Α Β Γ Δ Ε Ζ Η Ι Κ Λ Μ
- **Corrections Replayed**: `52` applied, `0` orphaned/unmatched
