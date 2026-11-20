# Edition Verification & Run Audit — *The Pālas of Bengal*

- **Book ID**: `palas-of-bengal` | **Run ID**: `g38-canonical-v1` | **Collection**: `general-heritage`
- **Edition Tier**: **`community`** | **Rubric Score**: **`80.2 / 100`** (`community`)
- **Reader**: Read by gemini-3.8-flash on 105 of 105 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen). This edition predates that choice and has not been re-read with gemini-4-hydrogen.
- **Pages**: `105` extracted, `21` blank/tissue, `0` failed (of `126` PDF leaves)
- **Tracked API Spend**: **`$1.2042`** (`87.4%` cached input tokens: `826,848` / `946,085` in, `204,704` out, `0` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **19.0 / 25.0** | -6.0: 2 unresolved footnote callout/body mismatch(es) |
| **3. Tabular & Numerical Accuracy** | **25.0 / 25.0** | Clean (0 deductions) |
| **4. Orthographic, Script & Diacritics** | **11.2 / 25.0** | -3.0: 1 script/codepoint anomaly(ies); -10.0: 31 intra-book diacritic drift cluster(s); -0.8: 4 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Resolve 2 unmatched footnote marker(s) via anchor-matched corrections.
- Standardize or verify 31 proper-noun diacritic drift cluster(s).

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract` | 108 | `$0.9191` |
| `continuation_arbiter` | 47 | `$0.2851` |

- **Final Page Provenance by Model**: `gemini-3.8-flash`: 105 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `58, 89, 91, 93, 95, 99, 101, 103, 107, 109, 111, 113`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`31` — catches smudged dates/figures in prose)**:
  - Leaf `11` `p0011-b0002`: VLM read `1911` vs PDF OCR witness `['1914']`
  - Leaf `18` `p0018-b0006`: VLM read `1891` vs PDF OCR witness `['1896']`
  - Leaf `19` `p0019-b0008`: VLM read `22,4` vs PDF OCR witness `['284']`
  - Leaf `33` `p0033-b0004`: VLM read `1178` vs PDF OCR witness `['1175']`
  - Leaf `35` `p0035-b0006`: VLM read `877` vs PDF OCR witness `['817', '867']`
  - Leaf `35` `p0035-b0016`: VLM read `110` vs PDF OCR witness `['150']`
  - Leaf `42` `p0042-b0016`: VLM read `250` vs PDF OCR witness `['150']`
  - Leaf `50` `p0050-b0014`: VLM read `168` vs PDF OCR witness `['166']`
  - Leaf `64` `p0064-b0011`: VLM read `346` vs PDF OCR witness `['341']`
  - Leaf `64` `p0064-b0013`: VLM read `348` vs PDF OCR witness `['341']`
  - Leaf `75` `p0075-b0007`: VLM read `1890` vs PDF OCR witness `['1090', '1896']`
  - Leaf `80` `p0080-b0021`: VLM read `100` vs PDF OCR witness `['110']`
  - Leaf `115` `p0115-b0013`: VLM read `101` vs PDF OCR witness `['103', '105', '106']`
  - Leaf `116` `p0116-b0042`: VLM read `111` vs PDF OCR witness `['112']`
  - Leaf `116` `p0116-b0058`: VLM read `103` vs PDF OCR witness `['102', '106', '107']`
  - Leaf `116` `p0116-b0058`: VLM read `104` vs PDF OCR witness `['102', '106', '107']`
  - Leaf `116` `p0116-b0067`: VLM read `110` vs PDF OCR witness `['112']`
  - Leaf `118` `p0118-b0009`: VLM read `101` vs PDF OCR witness `['102', '103', '104']`
  - Leaf `118` `p0118-b0034`: VLM read `101` vs PDF OCR witness `['102', '103', '104']`
  - Leaf `118` `p0118-b0039`: VLM read `110` vs PDF OCR witness `['112']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `34` prose joins, `0` split footnotes stitched, `0` multi-page tables unified, `277` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`32` — verify no epigraph/dedication was caught)**:
  - Leaf `1` `p0001-b0001` (`scanner_residue`): *"ASIA DS 485 .B41 B21 1915a ++"*
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Asia DS 425 B41 B21 1915a ++"*
  - Leaf `3` `p0003-b0001` (`scanner_residue`): *"CORNELL UNIVERSITY LIBRARY 3 1924 096 224 476"*
  - Leaf `4` `p0004-b0001` (`scanner_residue`): *"Cornell University Library"*
  - Leaf `4` `p0004-b0002` (`scanner_residue`): *"The original of this book is in the Cornell University Library."*
  - Leaf `4` `p0004-b0003` (`scanner_residue`): *"There are no known copyright restrictions in the United States on the use of the text."*
  - Leaf `4` `p0004-b0004` (`scanner_residue`): *"http://www.archive.org/details/cu31924096224476"*
  - Leaf `5` `p0005-b0001` (`scanner_residue`): *"In compliance with current copyright law, Cornell University Library produced this replace"*
  - Leaf `8` `p0008-b0001` (`scanner_residue`): *"OLIN DS 485 B41 B21++"*
  - Leaf `8` `p0008-b0002` (`scanner_residue`): *"CORNELL UNIVERSITY LIBRARY [Cornell University Library Bookplate Seal: Founded by Ezra Cor"*
  - Leaf `9` `p0009-b0012` (`noise`): *"20-8-15."*
  - Leaf `17` `p0017-b0008` (`noise`): *"—————"*
- **Unattested Line-Wrap Hyphenation Decisions (`31` unique words out of `205` total wraps)**: `surprised` (p.13), `liegelord` (p.14), `Mahā-mahopadhyaya` (p.16), `children` (p.16), `Indrā-yudhā` (p.21), `Prati-hāra` (p.28), `reoccupied` (p.30), `Brāhmaṇi-cal` (p.31), `greatgrandfather` (p.32), `Gopālade-vapravarddhamāna` (p.35), `extremity` (p.36), `Indo-Scythian` (p.42), `Kuch-Bihar` (p.43), `Gau-ḍadhvaja` (p.44), `imperfect` (p.45), `antagonist` (p.49), `mahattavanaṁ` (p.54), `chiefship` (p.55)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 176,695 chars
- **Distinct Non-ASCII Glyphs (`51` across `98` leaves)**: · Ñ Ü á â æ è é î ñ ö û ü Ā ā ē Ī ī ı ō ő œ Ś ś ū ̐ ̣ । ॥ Ḍ ḍ Ḥ ḥ ḷ ḻ ḿ ṁ ṃ ṅ Ṇ ṇ Ṛ ṛ ṝ Ṣ ṣ Ṭ ṭ ạ ∥ ❲
- **Corrections Replayed**: `29` applied, `0` orphaned/unmatched
