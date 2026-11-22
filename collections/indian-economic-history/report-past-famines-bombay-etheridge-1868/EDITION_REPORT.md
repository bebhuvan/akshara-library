# Edition Verification & Run Audit — *Report on Past Famines in the Bombay Presidency*

- **Book ID**: `report-past-famines-bombay-etheridge-1868` | **Run ID**: `g38-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`90.0 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 273 of 273 pages. Declared reader profile: english_prose (new readings use gemini-3.8-flash, with the book spelling note on prose pages).
- **Pages**: `273` extracted, `9` blank/tissue, `0` failed (of `282` PDF leaves)
- **Tracked API Spend**: **`$1.6604`** (`66.6%` cached input tokens: `2,168,622` / `3,254,960` in, `569,488` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **20.0 / 25.0** | -5.0: 6 multi-column zig-zag reading order warning(s) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **20.0 / 25.0** | -5.0: 44 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Ready to ship as Community Edition! Human page-proof coverage is 0.0% (pages re-read 13.2%) toward Source-Certified.

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 272 | `$1.3158` |
| `blind_totals_strip` | 40 | `$0.1874` |
| `continuation_arbiter_batch` | 61 | `$0.1356` |
| `primary_quality_retry` | 1 | `$0.0204` |
| `page_extract_batch_failed` | 1 | `$0.0011` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 273 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `58, 59, 60, 61, 69, 176, 199, 200`
- **450-DPI Blind Totals Strip Disagreements (`8`)**:
  - Leaf `176` `p0176-b0029`: full-page `['2,77,472', '78,834', '28', '1,84,586', '52,766', '29', '4,161', '1,344', '32']` vs blind-strip `['32 : : : 32 : : : : : : : : : : : Rs.', 'Percentage.', 'ers. " " " " "', 'to the']`
  - Leaf `181` `p0181-b0016`: full-page `['4,37,041', '1,30,849', '30', '2,01,090', '14,689', '7', '5,57,135', '80,162', '14', '10,36,125', '3,41,520', '33']` vs blind-strip `['4,37,041', '1,30,849', '30', '2,01,090', '14,689', '7', '5,57,135', '80,162', '1', '4', '10,36,125', '3,41,520', '33']`
  - Leaf `182` `p0182-b0021`: full-page `['6,90,036', '1,14,865', '17', '2,04,959', '45,058', '22', '3,51,056', '1,59,157', '45', '1,56,120', '1,32,385', '85']` vs blind-strip `['6,90,036', '1,14,865', '17', '2,04,959', '45,059', '22', '3,51,056', '1,59,157', '45', '1,56,120', '1,32,385', '85']`
  - Leaf `198` `p0198-b0046`: full-page `['11,91,225', '3,32,429', '28', '6,78,857', '1,68,397', '25', '4,82,685', '1,34,661', '16']` vs blind-strip `['11,91,225', '3,32,429', '28', '6,78,857', '1,68,307', '25', '4,82,685', '1,34,661', '16']`
  - Leaf `200` `p0200-b0026`: full-page `['3,07,490', '8,683', '16', '6,06,173', '1,79,521', '30', '2,05,354', '30,143', '15']` vs blind-strip `['3,07,490', '8,683', '16', '6,06,173', '1,79,521', '30', '2,05,3<unclear>8</unclear>']`
  - Leaf `201` `p0201-b0051`: full-page `['4,02,455', '65,846', '16', '2,42,697', '45,669', '19', '6,78,277', '2,56,879', '38', '1,73,190', '50,952', '29', '4,82,609', '1,72,669', '36']` vs blind-strip `['....', '....', '..', '....', '....', '..', '....', '....', '..', '39,161', '21,897', '56', '....', '....', '..']`
  - Leaf `205` `p0205-b0028`: full-page `['80,743', '‥', '37,495', '‥', '46', '‥', '47,284', '9,503', '5,103', '1,037', '11', '11', '‥', '1,902', '‥', '583', '‥', '31']` vs blind-strip `['80,743', '..', '37,495', '..', '46', '..', '47,284', '9,503', '5,103', '1,037', '11', '11', '..', '1,902', '..', '583', '..', '31']`
  - Leaf `260` `p0260-b0005`: full-page `['Gunnies....9,500']` vs blind-strip `['Gunnies ....', '9,500']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`78` — catches smudged dates/figures in prose)**:
  - Leaf `12` `p0012-b0005`: VLM read `1868` vs PDF OCR witness `['1861', '1865', '1867']`
  - Leaf `18` `p0018-b0004`: VLM read `164` vs PDF OCR witness `['163', '165']`
  - Leaf `21` `p0021-b0006`: VLM read `1844` vs PDF OCR witness `['1846']`
  - Leaf `34` `p0034-b0003`: VLM read `1876` vs PDF OCR witness `['1826', '1871']`
  - Leaf `36` `p0036-b0006`: VLM read `1774` vs PDF OCR witness `['1784']`
  - Leaf `36` `p0036-b0006`: VLM read `1782` vs PDF OCR witness `['1784']`
  - Leaf `40` `p0040-b0005`: VLM read `1746` vs PDF OCR witness `['1716', '1741', '1745']`
  - Leaf `40` `p0040-b0005`: VLM read `1756` vs PDF OCR witness `['1716', '1755', '1757']`
  - Leaf `40` `p0040-b0009`: VLM read `3161` vs PDF OCR witness `['3101']`
  - Leaf `40` `p0040-b0010`: VLM read `3161` vs PDF OCR witness `['3101']`
  - Leaf `40` `p0040-b0014`: VLM read `1265` vs PDF OCR witness `['1765']`
  - Leaf `43` `p0043-b0004`: VLM read `1898` vs PDF OCR witness `['1897']`
  - Leaf `43` `p0043-b0004`: VLM read `1902` vs PDF OCR witness `['1802']`
  - Leaf `43` `p0043-b0005`: VLM read `1845` vs PDF OCR witness `['1745']`
  - Leaf `43` `p0043-b0005`: VLM read `1847` vs PDF OCR witness `['1897']`
  - Leaf `43` `p0043-b0005`: VLM read `1852` vs PDF OCR witness `['1802']`
  - Leaf `43` `p0043-b0005`: VLM read `1867` vs PDF OCR witness `['1897']`
  - Leaf `70` `p0070-b0007`: VLM read `1847` vs PDF OCR witness `['1867']`
  - Leaf `72` `p0072-b0004`: VLM read `1847` vs PDF OCR witness `['1747', '1848']`
  - Leaf `74` `p0074-b0003`: VLM read `1825` vs PDF OCR witness `['1821', '1822']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `141` prose joins, `0` split footnotes stitched, `18` multi-page tables unified, `17` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`89` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"CORNELL UNIVERSITY FOUNDED A.D. 1865 Cornell University Library"*
  - Leaf `2` `p0002-b0002` (`scanner_residue`): *"The original of this book is in the Cornell University Library."*
  - Leaf `2` `p0002-b0003` (`scanner_residue`): *"There are no known copyright restrictions in the United States on the use of the text."*
  - Leaf `2` `p0002-b0004` (`scanner_residue`): *"http://www.archive.org/details/cu31924091209449"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"CORNELL UNIVERSITY LIBRARY 3 1924 091 209 449"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"In compliance with current copyright law, Cornell University Library produced this replace"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"CORNELL UNIVERSITY LIBRARY [Seal of Cornell University: Founded by Ezra Cornell]"*
  - Leaf `9` `p0009-b0010` (`noise`): *"——❖——"*
  - Leaf `11` `p0011-b0009` (`noise`): *"1 F"*
  - Leaf `19` `p0019-b0004` (`noise`): *"2 F"*
  - Leaf `27` `p0027-b0016` (`noise`): *"3 F"*
  - Leaf `33` `p0033-b0004` (`scanner_residue`): *"કુટુંબ"*
- **Unattested Line-Wrap Hyphenation Decisions (`78` unique words out of `740` total wraps)**: `characteristics` (p.12), `ntipate` (p.15), `identical` (p.17), `legislative` (p.17), `pecuniarily` (p.17), `Cuddapah` (p.20), `Statesmen` (p.21), `acknowledged` (p.21), `demarcation` (p.26), `conquered` (p.26), `allotted` (p.27), `ascertainable` (p.50), `deduction` (p.50), `Lungurkhanas` (p.51), `constituting` (p.53), `neglected` (p.64), `Oodeypoor` (p.65), `Lallkissondass` (p.71)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 432,158 chars, `gujarati`: 113 chars
- **Distinct Non-ASCII Glyphs (`69` across `60` leaves)**: ´ · à á â è é ó ô ú ü ˙ ં આ ઉ એ ક ખ ગ ચ છ જ ટ ઠ ડ ઢ ણ ત દ ધ ન પ ભ મ ય ર લ વ શ ષ સ હ ા િ ી ુ ૂ ે ો ્ ૦ ૧ ૨ ૩ ૬ ૭ ૮ ૯ ṣ „
- **Corrections Replayed**: `88` applied, `0` orphaned/unmatched
