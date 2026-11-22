# Edition Verification & Run Audit — *Famines and Land Assessments in India*

- **Book ID**: `famines-and-land-assessments` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`85.4 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 347 of 347 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `347` extracted, `5` blank/tissue, `0` failed (of `352` PDF leaves)
- **Tracked API Spend**: **`$1.3052`** (`73.3%` cached input tokens: `2,764,108` / `3,771,184` in, `405,766` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **23.0 / 25.0** | -2.0: 1 multi-column zig-zag reading order warning(s) |
| **2. Scholarly Apparatus & Continuation** | **19.0 / 25.0** | -6.0: 2 unresolved footnote callout/body mismatch(es) |
| **3. Tabular & Numerical Accuracy** | **21.0 / 25.0** | -4.0: 1 collapsed/jammed table row warning(s) |
| **4. Orthographic, Script & Diacritics** | **22.4 / 25.0** | -2.6: 13 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells via akshara review-sheets or Akshara Proofing Studio.
- Resolve 2 unmatched footnote marker(s) via anchor-matched corrections.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 347 | `$1.1064` |
| `continuation_arbiter_batch` | 43 | `$0.0726` |
| `blind_totals_strip` | 17 | `$0.0721` |
| `backup_witness_swap` | 1 | `$0.0385` |
| `page_extract` | 2 | `$0.0155` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 347 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `316, 317`
- **450-DPI Blind Totals Strip Disagreements (`2`)**:
  - Leaf `314` `p0314-b0030`: full-page `['Total .', '2,102', '26,16,336', '586', '14,07,998', '232', '7,35,433', '122', '4,95,531', '68', '3,33,502', '55', '3,39,861']` vs blind-strip `['<sc>Total</sc> .', '2,102', '26,16,336', '586', '14,07,998', '232', '7,35,433', '122', '4,95,531', '68', '3,33,502', '55', '3<unclear></unclear>']`
  - Leaf `317` `p0317-b0016`: full-page `['Total .', '94', '14,724', '51', '16,230', '31', '19,058', '4', '4,510', '180', '54,522']` vs blind-strip `['2,500 and<br>under', 'R. 5,000<br>under']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`51` — catches smudged dates/figures in prose)**:
  - Leaf `9` `p0009-b0015`: VLM read `116` vs PDF OCR witness `['113', '114']`
  - Leaf `29` `p0029-b0004`: VLM read `1813` vs PDF OCR witness `['1812', '1823', '1833']`
  - Leaf `97` `p0097-b0017`: VLM read `1897` vs PDF OCR witness `['1898']`
  - Leaf `109` `p0109-b0008`: VLM read `17,215,502` vs PDF OCR witness `['17216502']`
  - Leaf `128` `p0128-b0010`: VLM read `364` vs PDF OCR witness `['365']`
  - Leaf `131` `p0131-b0003`: VLM read `100` vs PDF OCR witness `['107']`
  - Leaf `131` `p0131-b0003`: VLM read `100` vs PDF OCR witness `['107']`
  - Leaf `204` `p0204-b0008`: VLM read `1856` vs PDF OCR witness `['1857', '1866']`
  - Leaf `269` `p0269-b0013`: VLM read `14,110` vs PDF OCR witness `['14111', '14113']`
  - Leaf `283` `p0283-b0008`: VLM read `14,890` vs PDF OCR witness `['14893']`
  - Leaf `283` `p0283-b0009`: VLM read `14,891` vs PDF OCR witness `['14893']`
  - Leaf `283` `p0283-b0010`: VLM read `14,892` vs PDF OCR witness `['14893']`
  - Leaf `293` `p0293-b0004`: VLM read `2304` vs PDF OCR witness `['2305', '2344', '2804']`
  - Leaf `304` `p0304-b0011`: VLM read `5000` vs PDF OCR witness `['0000']`
  - Leaf `311` `p0311-b0009`: VLM read `50,000` vs PDF OCR witness `['30000', '40000']`
  - Leaf `311` `p0311-b0009`: VLM read `50,000` vs PDF OCR witness `['30000', '40000']`
  - Leaf `311` `p0311-b0009`: VLM read `60,000` vs PDF OCR witness `['30000', '40000']`
  - Leaf `311` `p0311-b0009`: VLM read `60,000` vs PDF OCR witness `['30000', '40000']`
  - Leaf `311` `p0311-b0009`: VLM read `80,000` vs PDF OCR witness `['30000', '40000']`
  - Leaf `311` `p0311-b0009`: VLM read `80,000` vs PDF OCR witness `['30000', '40000']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `229` prose joins, `4` split footnotes stitched, `5` multi-page tables unified, `61` total footnotes.
  - Stitched cross-page footnotes: p.132->p.133 (`1`), p.310->p.311 (`Note`), p.314->p.315 (`Note`), p.314->p.315 (`*`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`44` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"ASIA"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Cornell University Library BOUGHT WITH THE INCOME FROM THE SAGE ENDOWMENT FUND THE GIFT OF"*
  - Leaf `2` `p0002-b0002` (`noise`): *"5474"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"Cornell University Library HC 435.D97F2 Famines and land assessments in India : 3 1924 022"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Cornell University Library"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"The original of this book is in the Cornell University Library. There are no known copyrig"*
  - Leaf `4` `p0004-b0003` (`scanner_residue`): *"http://www.archive.org/details/cu31924022938264"*
  - Leaf `7` `p0007-b0006` (`noise`): *"T"*
  - Leaf `9` `p0009-b0024` (`noise`): *"b"*
  - Leaf `11` `p0011-b0001` (`noise`): *"'"*
  - Leaf `25` `p0025-b0002` (`noise`): *"————♦————"*
  - Leaf `25` `p0025-b0007` (`noise`): *"A"*
- **Unattested Line-Wrap Hyphenation Decisions (`56` unique words out of `875` total wraps)**: `landowners` (p.28), `resistance` (p.39), `sensitiveness` (p.39), `consternation` (p.49), `enforced` (p.49), `undesirable` (p.72), `newlycreated` (p.81), `adhere` (p.90), `receivable` (p.95), `modifications` (p.96), `commencement` (p.114), `approximation` (p.122), `scornfully` (p.143), `belittle` (p.148), `indispensible` (p.149), `mistaken` (p.151), `experiencing` (p.151), `reconsidered` (p.155)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 409,511 chars
- **Distinct Non-ASCII Glyphs (`17` across `31` leaves)**: · Â Ü á â é ê î ô õ ü ā œ Ś ś ˙ „
- **Corrections Replayed**: `67` applied, `0` orphaned/unmatched
