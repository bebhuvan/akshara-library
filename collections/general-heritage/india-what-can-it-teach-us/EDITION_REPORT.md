# Edition Verification & Run Audit — *India: What Can It Teach Us?*

- **Book ID**: `india-what-can-it-teach-us` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`machine_checked`** | **Rubric Score**: **`100.0 / 100`** (`machine_checked`)
- **Reader**: Read by gemini-4-hydrogen on 344 of 344 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `344` extracted, `6` blank/tissue, `0` failed (of `350` PDF leaves)
- **Tracked API Spend**: **`$6.8034`** (`5.4%` cached input tokens: `229,376` / `4,261,099` in, `508,158` out, `379,243` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **25.0 / 25.0** | Clean (0 deductions) |

### Recommended Operator Next Actions
- Ready to ship as Machine-Checked Edition (no open validator hotspots; 6.7% of pages re-read; 0.0% verified by a person toward Source-Certified).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 341 | `$5.7659` |
| `secondary_gemini_rescue` | 3 | `$0.3500` |
| `page_extract` | 3 | `$0.1576` |
| `primary_quality_retry` | 3 | `$0.1530` |
| `recitation_band_top` | 3 | `$0.1020` |
| `page_extract_batch_vetoed` | 3 | `$0.0720` |
| `recitation_band_bot` | 2 | `$0.0680` |
| `continuation_arbiter_batch` | 37 | `$0.0648` |
| `tertiary_gemini_rescue` | 3 | `$0.0557` |
| `blind_totals_strip` | 1 | `$0.0105` |
| `continuation_arbiter` | 1 | `$0.0039` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 344 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `none`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`22` — catches smudged dates/figures in prose)**:
  - Leaf `319` `p0319-b0011`: VLM read `138` vs PDF OCR witness `['139', '148', '198']`
  - Leaf `319` `p0319-b0011`: VLM read `195` vs PDF OCR witness `['145', '155', '165']`
  - Leaf `321` `p0321-b0044`: VLM read `212` vs PDF OCR witness `['214', '215', '216']`
  - Leaf `321` `p0321-b0074`: VLM read `166` vs PDF OCR witness `['176', '266']`
  - Leaf `323` `p0323-b0009`: VLM read `117` vs PDF OCR witness `['119', '147', '157']`
  - Leaf `325` `p0325-b0011`: VLM read `108` vs PDF OCR witness `['102', '107', '158']`
  - Leaf `325` `p0325-b0035`: VLM read `108` vs PDF OCR witness `['102', '107', '158']`
  - Leaf `326` `p0326-b0049`: VLM read `166` vs PDF OCR witness `['116', '136', '161']`
  - Leaf `328` `p0328-b0014`: VLM read `186` vs PDF OCR witness `['126', '166', '176']`
  - Leaf `328` `p0328-b0028`: VLM read `110` vs PDF OCR witness `['120', '130', '150']`
  - Leaf `330` `p0330-b0025`: VLM read `211` vs PDF OCR witness `['251', '261']`
  - Leaf `330` `p0330-b0041`: VLM read `188` vs PDF OCR witness `['118', '181', '183']`
  - Leaf `331` `p0331-b0036`: VLM read `108` vs PDF OCR witness `['109', '158', '188']`
  - Leaf `332` `p0332-b0007`: VLM read `108` vs PDF OCR witness `['102', '106', '128']`
  - Leaf `333` `p0333-b0035`: VLM read `110` vs PDF OCR witness `['115', '130', '150']`
  - Leaf `333` `p0333-b0036`: VLM read `110` vs PDF OCR witness `['115', '130', '150']`
  - Leaf `333` `p0333-b0037`: VLM read `110` vs PDF OCR witness `['115', '130', '150']`
  - Leaf `334` `p0334-b0041`: VLM read `181` vs PDF OCR witness `['131', '151', '171']`
  - Leaf `336` `p0336-b0007`: VLM read `111` vs PDF OCR witness `['112', '113', '116']`
  - Leaf `336` `p0336-b0025`: VLM read `111` vs PDF OCR witness `['112', '113', '116']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `230` prose joins, `20` split footnotes stitched, `0` multi-page tables unified, `378` total footnotes.
  - Stitched cross-page footnotes: p.31->p.32 (`3`), p.33->p.34 (`2`), p.78->p.79 (`5`), p.87->p.88 (`4`), p.114->p.115 (`1`), p.117->p.118 (`1`), p.147->p.148 (`4`), p.149->p.150 (`2`), p.153->p.154 (`1`), p.186->p.187 (`3`), p.187->p.188 (`4`), p.188->p.189 (`4`), p.195->p.196 (`1`), p.245->p.246 (`2`), p.272->p.273 (`1`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`60` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO 3 1761 00879644 3"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2007 with funding from Microsoft Corporation"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"http://www.archive.org/details/indiawhatcanitte00mluoft"*
  - Leaf `6` `p0006-b0002` (`scanner_residue`): *"DS 425 M95 1892"*
  - Leaf `12` `p0012-b0007` (`noise`): *"—"*
  - Leaf `13` `p0013-b0002` (`noise`): *"—♦—"*
  - Leaf `13` `p0013-b0025` (`scanner_residue`): *"Faint circular library stamp."*
  - Leaf `15` `p0015-b0002` (`noise`): *"—♦—"*
  - Leaf `19` `p0019-b0004` (`noise`): *"b"*
  - Leaf `23` `p0023-b0002` (`noise`): *"—◆—"*
  - Leaf `23` `p0023-b0006` (`noise`): *"B"*
  - Leaf `25` `p0025-b0006` (`noise`): *"B 2"*
- **Unattested Line-Wrap Hyphenation Decisions (`157` unique words out of `769` total wraps)**: `encouragement` (p.7), `disappointing` (p.8), `kindhearted` (p.11), `suspect` (p.17), `Nachrichten` (p.19), `Vikramakâla` (p.20), `Wassiljew` (p.22), `outlandish` (p.25), `astounding` (p.25), `Âryâvarta` (p.29), `Mediterranean` (p.32), `demonstrative` (p.36), `construction` (p.37), `perspective` (p.38), `profiting` (p.38), `overburdened` (p.43), `preservation` (p.44), `converging` (p.47)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 434,928 chars, `greek`: 1,419 chars, `devanagari`: 76 chars, `hebrew`: 3 chars, `han`: 2 chars
- **Distinct Non-ASCII Glyphs (`180` across `244` leaves)**: · Á Â Æ É Ê Î Ô Û Ü à á â ä æ ç è é ê ì í î ð ñ ò ó ô ö ú û ü ā ă đ ī œ š ŭ ŷ ́ ̆ ̐ Α Γ Δ Ζ Η Θ Κ Μ Ο Π Σ Τ Χ ά έ ή ί α
- **Corrections Replayed**: `17` applied, `0` orphaned/unmatched
