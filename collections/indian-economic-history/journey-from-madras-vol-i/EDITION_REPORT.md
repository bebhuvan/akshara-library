# Edition Verification & Run Audit — *A Journey from Madras through the Countries of Mysore, Canara, and Malabar*

- **Book ID**: `journey-from-madras-vol-i` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`81.8 / 100`** (`community`)
- **Reader**: Read by gemini-4-hydrogen on 457 of 457 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `457` extracted, `19` blank/tissue, `0` failed (of `476` PDF leaves)
- **Tracked API Spend**: **`$8.6484`** (`10.3%` cached input tokens: `559,960` / `5,454,014` in, `698,665` out, `581,511` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **8.0 / 25.0** | -5.0: 1 Blind Totals Strip disagreement(s); -12.0: 12 column total arithmetic mismatch(es) |
| **4. Orthographic, Script & Diacritics** | **23.8 / 25.0** | -1.2: 6 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 456 | `$8.0197` |
| `continuation_arbiter_batch` | 29 | `$0.2463` |
| `blind_totals_strip` | 17 | `$0.1940` |
| `max_tokens_retry` | 1 | `$0.1184` |
| `page_extract_batch_failed` | 1 | `$0.0699` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 457 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `103, 162, 196, 269, 328, 414, 450`
- **450-DPI Blind Totals Strip Disagreements (`3`)**:
  - Leaf `182` `p0182-b0013`: full-page `['', 'lb. 58', '11', '5', '2', '11']` vs blind-strip `['lb.', '58', '11', '5', '2', '11']`
  - Leaf `185` `p0185-b0011`: full-page `['', 'lb. 66', '4', '4']` vs blind-strip `['lb.', '66', '4', '4']`
  - Leaf `345` `p0345-b0021`: full-page `['Seers', '51']` vs blind-strip `['<i>Sēers</i>', '51']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`16` — catches smudged dates/figures in prose)**:
  - Leaf `20` `p0020-b0002`: VLM read `160` vs PDF OCR witness `['162']`
  - Leaf `235` `p0235-b0024`: VLM read `160` vs PDF OCR witness `['100', '120']`
  - Leaf `237` `p0237-b0008`: VLM read `130` vs PDF OCR witness `['131']`
  - Leaf `246` `p0246-b0005`: VLM read `100` vs PDF OCR witness `['105']`
  - Leaf `246` `p0246-b0005`: VLM read `100` vs PDF OCR witness `['105']`
  - Leaf `246` `p0246-b0006`: VLM read `100` vs PDF OCR witness `['105']`
  - Leaf `251` `p0251-b0005`: VLM read `213` vs PDF OCR witness `['211']`
  - Leaf `254` `p0254-b0006`: VLM read `157` vs PDF OCR witness `['137']`
  - Leaf `268` `p0268-b0008`: VLM read `213` vs PDF OCR witness `['223']`
  - Leaf `271` `p0271-b0004`: VLM read `100` vs PDF OCR witness `['109']`
  - Leaf `271` `p0271-b0004`: VLM read `100` vs PDF OCR witness `['109']`
  - Leaf `271` `p0271-b0004`: VLM read `100` vs PDF OCR witness `['109']`
  - Leaf `271` `p0271-b0008`: VLM read `100` vs PDF OCR witness `['109']`
  - Leaf `271` `p0271-b0008`: VLM read `100` vs PDF OCR witness `['109']`
  - Leaf `306` `p0306-b0001`: VLM read `263` vs PDF OCR witness `['163']`
  - Leaf `461` `p0461-b0005`: VLM read `100` vs PDF OCR witness `['150']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `325` prose joins, `0` split footnotes stitched, `5` multi-page tables unified, `1` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`98` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"SCD #3125 v.1 10.17.13. Library of the Theological Seminary, PRINCETON, N. J. Purchased by"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"6 E 15"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"Digitized by the Internet Archive in 2016"*
  - Leaf `5` `p0005-b0002` (`scanner_residue`): *"https://archive.org/details/journeyfrommadra01hami_2"*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"LIBRARY OF PRINCETON OCT 17 1913 THEOLOGICAL SEMINARY"*
  - Leaf `7` `p0007-b0003` (`noise`): *"—"*
  - Leaf `7` `p0007-b0005` (`noise`): *"—"*
  - Leaf `7` `p0007-b0007` (`noise`): *"—"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"Library oval ink stamp"*
  - Leaf `13` `p0013-b0009` (`noise`): *"Vol. I."*
  - Leaf `13` `p0013-b0010` (`noise`): *"b"*
  - Leaf `23` `p0023-b0007` (`noise`): *"VOL. I. B"*
- **Unattested Line-Wrap Hyphenation Decisions (`119` unique words out of `1622` total wraps)**: `obstruct` (p.14), `mentioning` (p.17), `Condaturu` (p.24), `Barlerioides` (p.29), `delighted` (p.30), `Dubash` (p.32), `sustenance` (p.40), `garnite` (p.41), `Elamulla` (p.48), `Glanitello` (p.51), `enlarging` (p.57), `hardness` (p.61), `frequenting` (p.66), `Pinakani` (p.67), `whitestone` (p.69), `calculate` (p.75), `luxuriant` (p.76), `perfume` (p.78)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 690,702 chars
- **Distinct Non-ASCII Glyphs (`21` across `295` leaves)**: Æ à á ä æ é í ó ú ü ā ă œ ſ ⁄ ⅐ ⅓ ⅔ ⅕ ⅛ ⅝
- **Corrections Replayed**: `9` applied, `0` orphaned/unmatched
