# Edition Verification & Run Audit — *The Imperial Gazetteer of India: The Indian Empire, Vol. II — Historical*

- **Book ID**: `imperial-gazetteer-of-india-vol-02-historical` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`96.8 / 100`** (`community`)
- **Reader**: Read by gemini-4-hydrogen on 587 of 614 pages, gemini-3.6-flash on 27 of 614 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `614` extracted, `8` blank/tissue, `0` failed (of `622` PDF leaves)
- **Tracked API Spend**: **`$12.9556`** (`3.4%` cached input tokens: `265,436` / `7,728,007` in, `1,047,505` out, `772,114` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **22.0 / 25.0** | -3.0: 1 suspected text omission page(s) vs. OCR witness |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **24.8 / 25.0** | -0.2: 1 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Audit 1 page(s) flagged for low alphabetic coverage vs. OCR witness.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 579 | `$10.8871` |
| `recitation_band_top` | 31 | `$0.5518` |
| `secondary_gemini_rescue` | 27 | `$0.4818` |
| `recitation_retry` | 35 | `$0.4445` |
| `page_extract_batch_failed` | 35 | `$0.3003` |
| `recitation_band_bot` | 14 | `$0.2113` |
| `continuation_arbiter_batch` | 40 | `$0.0788` |

- **Final Page Provenance by Model**: `gemini-3.6-flash`: 27 pp., `gemini-4-hydrogen`: 587 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Retried / Fallback-Rescued Pages (worth a quick scan glance)**:
  - Leaf `576` via `recitation_2band_split` (`gemini-4-hydrogen`)
  - Leaf `582` via `recitation_2band_split` (`gemini-4-hydrogen`)
  - Leaf `590` via `recitation_2band_split` (`gemini-4-hydrogen`)
  - Leaf `600` via `recitation_2band_split` (`gemini-4-hydrogen`)
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`445` — catches smudged dates/figures in prose)**:
  - Leaf `15` `p0015-b0007`: VLM read `135` vs PDF OCR witness `['134']`
  - Leaf `15` `p0015-b0007`: VLM read `154` vs PDF OCR witness `['134']`
  - Leaf `15` `p0015-b0008`: VLM read `205` vs PDF OCR witness `['206']`
  - Leaf `18` `p0018-b0015`: VLM read `125` vs PDF OCR witness `['135']`
  - Leaf `18` `p0018-b0016`: VLM read `125` vs PDF OCR witness `['135']`
  - Leaf `18` `p0018-b0019`: VLM read `127` vs PDF OCR witness `['137']`
  - Leaf `18` `p0018-b0020`: VLM read `127` vs PDF OCR witness `['137']`
  - Leaf `18` `p0018-b0026`: VLM read `130` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0027`: VLM read `130` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0028`: VLM read `130` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0029`: VLM read `131` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0030`: VLM read `131` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0031`: VLM read `132` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0032`: VLM read `132` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0033`: VLM read `132` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0034`: VLM read `133` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0035`: VLM read `133` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0036`: VLM read `133` vs PDF OCR witness `['135', '137']`
  - Leaf `18` `p0018-b0037`: VLM read `134` vs PDF OCR witness `['135', '137']`
  - Leaf `19` `p0019-b0038`: VLM read `168` vs PDF OCR witness `['138', '148', '158']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `434` prose joins, `2` split footnotes stitched, `0` multi-page tables unified, `138` total footnotes.
  - Stitched cross-page footnotes: p.46->p.47 (`2`), p.49->p.50 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`122` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00114402 1"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"MICROFORMED BY PRESERVATION SERVICES FEB 25 1987 DATE...................."*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"In. I 345"*
  - Leaf `7` `p0007-b0003` (`scanner_residue`): *"UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `7` `p0007-b0009` (`scanner_residue`): *"91851 16/9/08."*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Embossed library stamp: UNIVERSITY OF TORONTO LIBRARY"*
  - Leaf `23` `p0023-b0048` (`noise`): *"VOL. II."*
  - Leaf `23` `p0023-b0049` (`noise`): *"b"*
  - Leaf `25` `p0025-b0049` (`noise`): *"b 2"*
  - Leaf `39` `p0039-b0047` (`noise`): *"VOL. II."*
  - Leaf `39` `p0039-b0048` (`noise`): *"c"*
  - Leaf `43` `p0043-b0010` (`noise`): *"VOL. II."*
- **Unattested Line-Wrap Hyphenation Decisions (`184` unique words out of `2321` total wraps)**: `introducing` (p.47), `apocryphal` (p.48), `Vardhamāna-Mahāvīra` (p.50), `Tiruvārūr` (p.54), `Dīgha-Nikāya` (p.59), `Pravachanaparīkshā` (p.64), `Śrīvallabha` (p.64), `deciphering` (p.66), `Rāwalpiṇḍī` (p.67), `Shōlāpūr` (p.69), `Pallavamalla-Nandivarman` (p.71), `Nāgabhaṭṭa` (p.73), `signmanual` (p.75), `spoonshaped` (p.75), `Duṁdubhisara` (p.78), `Sūryamitra` (p.80), `Pālāṭu-Ḍherī` (p.82), `Kotīputa-Kāsapagota` (p.86)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 1,216,040 chars, `greek`: 64 chars
- **Distinct Non-ASCII Glyphs (`88` across `582` leaves)**: · É à á â ã ä æ ç è é ê î ï ñ ô ö û ü Ā ā Ē ē Ī ī Ō ō Ś ś ũ ū ʿ ́ ͟ Η Σ ά έ ή ί α β δ ε η θ ι λ μ ν ο π ς σ τ υ ω Ḍ ḍ Ḥ
- **Corrections Replayed**: `4` applied, `0` orphaned/unmatched
