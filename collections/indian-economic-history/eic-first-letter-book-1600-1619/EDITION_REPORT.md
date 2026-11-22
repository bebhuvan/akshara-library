# Edition Verification & Run Audit — *The Register of Letters &c. of the Governour and Company of Merchants of London Trading into the East Indies, 1600–1619*

- **Book ID**: `eic-first-letter-book-1600-1619` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`96.8 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 622 of 622 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `622` extracted, `4` blank/tissue, `0` failed (of `626` PDF leaves)
- **Tracked API Spend**: **`$2.8525`** (`74.8%` cached input tokens: `4,923,752` / `6,583,782` in, `1,067,956` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **21.8 / 25.0** | -3.0: 1 script/codepoint anomaly(ies); -0.2: 1 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Ready to ship as Community Edition! Human page-proof coverage is 0.0% (pages re-read 2.4%) toward Source-Certified.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 617 | `$2.5574` |
| `continuation_arbiter_batch` | 64 | `$0.1336` |
| `page_extract_batch_failed` | 3 | `$0.0675` |
| `primary_quality_retry` | 3 | `$0.0403` |
| `max_tokens_retry` | 2 | `$0.0288` |
| `blind_totals_strip` | 4 | `$0.0168` |
| `page_extract_batch_vetoed` | 2 | `$0.0082` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 622 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `194`
- **450-DPI Blind Totals Strip Disagreements (`1`)**:
  - Leaf `188` `p0188-b0011`: full-page `['', 'Soma totalis', '', '22913li', '16s', '00']` vs blind-strip `['...', '...', '2680', '00', '00']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`154` — catches smudged dates/figures in prose)**:
  - Leaf `21` `p0021-b0004`: VLM read `1614` vs PDF OCR witness `['1604', '1611', '1615']`
  - Leaf `81` `p0081-b0014`: VLM read `105` vs PDF OCR witness `['103']`
  - Leaf `81` `p0081-b0016`: VLM read `111` vs PDF OCR witness `['110', '114']`
  - Leaf `82` `p0082-b0004`: VLM read `138` vs PDF OCR witness `['139', '158']`
  - Leaf `83` `p0083-b0013`: VLM read `211` vs PDF OCR witness `['210', '212', '213']`
  - Leaf `84` `p0084-b0009`: VLM read `218` vs PDF OCR witness `['214', '215', '216']`
  - Leaf `85` `p0085-b0004`: VLM read `231` vs PDF OCR witness `['232', '234', '236']`
  - Leaf `87` `p0087-b0009`: VLM read `315` vs PDF OCR witness `['311', '312', '319']`
  - Leaf `120` `p0120-b0009`: VLM read `1608` vs PDF OCR witness `['1600', '1603']`
  - Leaf `132` `p0132-b0006`: VLM read `1603` vs PDF OCR witness `['1602']`
  - Leaf `151` `p0151-b0003`: VLM read `110` vs PDF OCR witness `['116', '117']`
  - Leaf `190` `p0190-b0006`: VLM read `0042` vs PDF OCR witness `['0052']`
  - Leaf `192` `p0192-b0003`: VLM read `000` vs PDF OCR witness `['002', '060', '100']`
  - Leaf `193` `p0193-b0003`: VLM read `011` vs PDF OCR witness `['012']`
  - Leaf `193` `p0193-b0004`: VLM read `011` vs PDF OCR witness `['012']`
  - Leaf `193` `p0193-b0007`: VLM read `1120` vs PDF OCR witness `['1620']`
  - Leaf `198` `p0198-b0004`: VLM read `1607` vs PDF OCR witness `['1606']`
  - Leaf `258` `p0258-b0003`: VLM read `1601` vs PDF OCR witness `['1600', '1602', '1606']`
  - Leaf `308` `p0308-b0008`: VLM read `123` vs PDF OCR witness `['103']`
  - Leaf `324` `p0324-b0009`: VLM read `1607` vs PDF OCR witness `['1606']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `309` prose joins, `22` split footnotes stitched, `2` multi-page tables unified, `868` total footnotes.
  - Stitched cross-page footnotes: p.36->p.37 (`1`), p.37->p.38 (`2`), p.52->p.53 (`1`), p.70->p.71 (`1`), p.105->p.106 (`1`), p.117->p.118 (`2`), p.138->p.139 (`3`), p.144->p.145 (`2`), p.159->p.160 (`2`), p.188->p.189 (`3`), p.206->p.207 (`4`), p.212->p.213 (`3`), p.235->p.236 (`2`), p.256->p.257 (`8`), p.292->p.293 (`2`)
- **Suppressed Non-Authorial / Scanner Residue Blocks (`168` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"3 1761 04645257 9"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Bookplate of the University of Toronto: King Alfred Library of History, Founded by Goldwin"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"207-"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"154 OI-II."*
  - Leaf `7` `p0007-b0001` (`scanner_residue`): *"HF B16183r"*
  - Leaf `7` `p0007-b0004` (`scanner_residue`): *"UNIVERSITY OF TORONTO blind embossed seal"*
  - Leaf `7` `p0007-b0008` (`scanner_residue`): *"89716 7/8/08."*
  - Leaf `7` `p0007-b0010` (`scanner_residue`): *"SEEN BY PRESERVATION SERVICES DEC 1 6 1991 DATE...................."*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"UNIVERSITY OF TORONTO library embossed stamp"*
  - Leaf `8` `p0008-b0003` (`scanner_residue`): *"DS 465 A3 1893"*
  - Leaf `13` `p0013-b0005` (`noise`): *"b"*
  - Leaf `15` `p0015-b0008` (`noise`): *"b 1"*
- **Unattested Line-Wrap Hyphenation Decisions (`120` unique words out of `780` total wraps)**: `admirable` (p.13), `comportment` (p.26), `manylanguaged` (p.26), `systematically` (p.27), `comprehensiveness` (p.29), `perseverance` (p.29), `Bhau-Dajiana` (p.38), `predominant` (p.44), `Mangalore` (p.45), `irremediable` (p.50), `Gileadense` (p.52), `accommodation` (p.53), `immigrants` (p.54), `cornerstone` (p.57), `determinately` (p.59), `indulgence` (p.60), `excitement` (p.62), `discontinued` (p.63)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 1,081,481 chars, `greek`: 1,271 chars, `other`: 39 chars, `han`: 36 chars, `hangul`: 26 chars, `cyrillic`: 4 chars, `arabic`: 3 chars, `devanagari`: 2 chars
- **Distinct Non-ASCII Glyphs (`187` across `488` leaves)**: · º Æ Ç á â ã æ ç é ï ñ ò ó ô õ ö ā ă ĉ č đ ē ĕ ę ģ ħ Ĩ ĩ Ī ī ł Ń ŉ ō Œ œ ũ ū ſ ƀ ȓ ȕ ȱ ə ɫ ɰ ʂ ʃ ʉ ʰ ʳ ˡ ˢ ̃ ̄ ̧ ̱ ̵ ͠
- **Corrections Replayed**: `161` applied, `0` orphaned/unmatched
