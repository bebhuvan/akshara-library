# Edition Verification & Run Audit — *The English Factories in India, 1624–1629*

- **Book ID**: `english-factories-india-1624-1629-vol-03` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`100.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 439 of 442 pages, gemini-3.6-flash on 3 of 442 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `442` extracted, `4` blank/tissue, `0` failed (of `446` PDF leaves)
- **Tracked API Spend**: **`$2.2456`** (`72.3%` cached input tokens: `3,536,130` / `4,890,530` in, `705,334` out, `110` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Community Edition! Human page-proof coverage is 0.0% (pages re-read 2.7%) toward Source-Certified.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 418 | `$1.5765` |
| `primary_quality_retry` | 16 | `$0.1986` |
| `recitation_retry` | 7 | `$0.1788` |
| `recitation_band_top` | 5 | `$0.0595` |
| `page_extract_batch_vetoed` | 16 | `$0.0584` |
| `continuation_arbiter_batch` | 34 | `$0.0520` |
| `secondary_gemini_rescue` | 3 | `$0.0457` |
| `page_extract_batch_failed` | 8 | `$0.0397` |
| `recitation_band_bot` | 3 | `$0.0289` |
| `max_tokens_retry` | 1 | `$0.0077` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 3 pp., `gemini-3.8-flash`: 439 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `244` via `recitation_2band_split` (`gemini-3.8-flash`)
  - Leaf `288` via `recitation_2band_split` (`gemini-3.8-flash`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`182` — catches smudged dates/figures in prose)**:
  - Leaf `26` `p0026-b0005`: VLM read `1891` vs PDF OCR witness `['1890']`
  - Leaf `30` `p0030-b0003`: VLM read `170` vs PDF OCR witness `['171']`
  - Leaf `31` `p0031-b0003`: VLM read `207` vs PDF OCR witness `['203', '307']`
  - Leaf `31` `p0031-b0004`: VLM read `202` vs PDF OCR witness `['203', '302']`
  - Leaf `34` `p0034-b0005`: VLM read `1648` vs PDF OCR witness `['1628']`
  - Leaf `39` `p0039-b0003`: VLM read `1627` vs PDF OCR witness `['1617', '1623', '1628']`
  - Leaf `41` `p0041-b0007`: VLM read `300` vs PDF OCR witness `['100', '350', '500']`
  - Leaf `41` `p0041-b0007`: VLM read `150` vs PDF OCR witness `['100', '350']`
  - Leaf `62` `p0062-b0006`: VLM read `265` vs PDF OCR witness `['260']`
  - Leaf `71` `p0071-b0003`: VLM read `100` vs PDF OCR witness `['103']`
  - Leaf `87` `p0087-b0003`: VLM read `12,000` vs PDF OCR witness `['14000']`
  - Leaf `99` `p0099-b0003`: VLM read `200` vs PDF OCR witness `['100', '500', '600']`
  - Leaf `109` `p0109-b0009`: VLM read `1181` vs PDF OCR witness `['1180']`
  - Leaf `123` `p0123-b0004`: VLM read `1625` vs PDF OCR witness `['1635']`
  - Leaf `123` `p0123-b0007`: VLM read `1625` vs PDF OCR witness `['1635']`
  - Leaf `128` `p0128-b0003`: VLM read `1184` vs PDF OCR witness `['1185']`
  - Leaf `146` `p0146-b0007`: VLM read `200` vs PDF OCR witness `['100', '250', '400']`
  - Leaf `146` `p0146-b0007`: VLM read `200` vs PDF OCR witness `['100', '250', '400']`
  - Leaf `147` `p0147-b0003`: VLM read `1,000` vs PDF OCR witness `['4000']`
  - Leaf `174` `p0174-b0004`: VLM read `153` vs PDF OCR witness `['133']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `195` prose joins, `16` split footnotes stitched, `1` multi-page tables unified, `432` total footnotes.
  - Stitched cross-page footnotes: p.16->p.17 (`1`), p.17->p.18 (`2`), p.26->p.27 (`2`), p.29->p.30 (`2`), p.34->p.35 (`1`), p.42->p.43 (`2`), p.48->p.49 (`1`), p.50->p.51 (`2`), p.67->p.68 (`4`), p.119->p.120 (`1`), p.174->p.175 (`5`), p.209->p.210 (`2`), p.213->p.214 (`1`), p.233->p.234 (`1`), p.246->p.247 (`2`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`89` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 08381421 0"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2010 with funding from University of Toronto"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"http://www.archive.org/details/englishfactories03fost"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"[Vol. 3]"*
  - Leaf `7` `p0007-b0008` (`scanner_residue`): *"104110 11/7/10"*
  - Leaf `9` `p0009-b0004` (`noise`): *"a 2"*
  - Leaf `23` `p0023-b0006` (`noise`): *"FOSTER III"*
  - Leaf `23` `p0023-b0007` (`noise`): *"b"*
  - Leaf `25` `p0025-b0007` (`noise`): *"b 2"*
  - Leaf `39` `p0039-b0005` (`noise`): *"foster iii"*
  - Leaf `39` `p0039-b0006` (`noise`): *"c"*
  - Leaf `41` `p0041-b0012` (`noise`): *"C 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`81` unique words out of `700` total wraps)**: `indignity` (p.12), `dismayed` (p.16), `commissioners` (p.27), `deputation` (p.31), `facilities` (p.34), `abstention` (p.43), `constructed` (p.53), `Masulapatan` (p.57), `communication` (p.58), `bricklayers` (p.64), `cacaroches` (p.67), `whomsoever` (p.84), `unaccessable` (p.90), `independently` (p.100), `severally` (p.100), `courragiusly` (p.105), `incurrage` (p.105), `wrongfullie` (p.114)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 789,174 chars
- **Distinct Non-ASCII Glyphs (`27` across `326` leaves)**: · º à ã ç é ï Ā ā ġ ī Ń Ō ō œ ũ ū ſ Ṇ ṭ ′ ₨ ⅓ ⅔ ⅛ ⅜ ⅞
- **Corrections Replayed**: `16` applied, `0` orphaned/unmatched
