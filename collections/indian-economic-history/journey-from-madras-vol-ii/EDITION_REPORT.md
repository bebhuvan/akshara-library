# Edition Verification & Run Audit — *A Journey from Madras through the Countries of Mysore, Canara, and Malabar*

- **Book ID**: `journey-from-madras-vol-ii` | **Run ID**: `g4-hydrogen-batch-v1` | **Collection**: `indian-economic-history`
- **Edition Tier**: **`community`** | **Rubric Score**: **`75.0 / 100`** (`community`)
- **Reader**: Read by gemini-4-hydrogen on 584 of 584 pages. Declared reader profile: transliteration (new readings use gemini-4-hydrogen).
- **Pages**: `584` extracted, `14` blank/tissue, `0` failed (of `598` PDF leaves)
- **Tracked API Spend**: **`$11.0055`** (`13.4%` cached input tokens: `943,064` / `7,019,687` in, `894,112` out, `756,391` thoughts)

---

## 1. Quantitative Rubric Breakdown & Highest-Leverage Actions

| Pillar | Score | Deductions |
| :--- | ---: | :--- |
| **1. Structural & Page Completeness** | **25.0 / 25.0** | Clean (0 deductions) |
| **2. Scholarly Apparatus & Continuation** | **25.0 / 25.0** | Clean (0 deductions) |
| **3. Tabular & Numerical Accuracy** | **8.0 / 25.0** | -5.0: 1 Blind Totals Strip disagreement(s); -12.0: 26 column total arithmetic mismatch(es) |
| **4. Orthographic, Script & Diacritics** | **17.0 / 25.0** | -6.0: 2 script/codepoint anomaly(ies); -2.0: 10 `<unclear>` ink span(s) awaiting scan check |

### Recommended Operator Next Actions
- Inspect flagged statistical table cells in Static Proofing UI ('Needs A Pair of Eyes').

---

## 2. Spend, Stage & Model Telemetry

| Pipeline Stage | API Calls | Spend (USD) |
| :--- | ---: | ---: |
| `page_extract_batch` | 584 | `$10.3323` |
| `blind_totals_strip` | 39 | `$0.4465` |
| `continuation_arbiter_batch` | 24 | `$0.2267` |

- **Final Page Provenance by Model**: `gemini-4-hydrogen`: 584 pp.

---

## 3. High-Attention Verification Signals

- **Sideways Broadside Leaves Auto-Rotated**: `343, 395`
- **450-DPI Blind Totals Strip Disagreements (`11`)**:
  - Leaf `32` `p0032-b0013`: full-page `['Fanams', '276']` vs blind-strip `['<i>Fanams 276</i>']`
  - Leaf `38` `p0038-b0012`: full-page `['', 'Fanams 247']` vs blind-strip `['<i>Fanams</i>', '<i>247</i>']`
  - Leaf `53` `p0053-b0007`: full-page `['Large pieces', '5']` vs blind-strip `['Large pieces', '-', '5']`
  - Leaf `238` `p0238-b0009`: full-page `['Gópály Fanams', '114⅗']` vs blind-strip `['<i>Gópály Fanams</i>', '114<sup>3</sup>/<sub>5</sub>']`
  - Leaf `428` `p0428-b0009`: full-page `['Clear profit', '25', '36 2/3']` vs blind-strip `['Clear profit', '‐', '‐', '‐', '25 36⅔']`
  - Leaf `454` `p0454-b0011`: full-page `['Porays', '15 8/10']` vs blind-strip `['<i>Porays</i>', '15 <sup><unclear>1</unclear></sup>/<sub>10</sub>']`
  - Leaf `466` `p0466-b0012`: full-page `['', '27,1⁄2', '0', '0']` vs blind-strip `['27,½', '0', '0']`
  - Leaf `468` `p0468-b0011`: full-page `["Total population by Mr. Barber's ditto", '120,101']` vs blind-strip `['Total population by Mr. Barber’s ditto', '120,101']`
  - Leaf `506` `p0506-b0013`: full-page `['Total of two crops', 'Bushels 22½', '£. 2', '3', '5½']` vs blind-strip `['Total of two crops - Bushels', '22½', '£. 2', '3', '5½']`
  - Leaf `506` `p0506-b0024`: full-page `['Total', '83', '39,6448', '3', '10', '8¾']` vs blind-strip `['Total - -', '83', '39,6448', '3 10 8¾']`
  - Leaf `537` `p0537-b0019`: full-page `['Total buffaloes', '1410', '']` vs blind-strip `['Total buffaloes', '-', '1410']`
- **Secondary OCR Witness 1-Digit Numeric Near-Misses (`45` — catches smudged dates/figures in prose)**:
  - Leaf `35` `p0035-b0004`: VLM read `106` vs PDF OCR witness `['100']`
  - Leaf `38` `p0038-b0006`: VLM read `110` vs PDF OCR witness `['150']`
  - Leaf `115` `p0115-b0011`: VLM read `25,073888` vs PDF OCR witness `['25073883']`
  - Leaf `115` `p0115-b0014`: VLM read `25,073888` vs PDF OCR witness `['25073883']`
  - Leaf `118` `p0118-b0006`: VLM read `1000` vs PDF OCR witness `['7000']`
  - Leaf `120` `p0120-b0004`: VLM read `100` vs PDF OCR witness `['104']`
  - Leaf `121` `p0121-b0004`: VLM read `100` vs PDF OCR witness `['105']`
  - Leaf `122` `p0122-b0006`: VLM read `100` vs PDF OCR witness `['106']`
  - Leaf `123` `p0123-b0009`: VLM read `100` vs PDF OCR witness `['107']`
  - Leaf `132` `p0132-b0006`: VLM read `100` vs PDF OCR witness `['140']`
  - Leaf `140` `p0140-b0008`: VLM read `174` vs PDF OCR witness `['124']`
  - Leaf `167` `p0167-b0006`: VLM read `141` vs PDF OCR witness `['151']`
  - Leaf `173` `p0173-b0004`: VLM read `1000` vs PDF OCR witness `['1800']`
  - Leaf `173` `p0173-b0004`: VLM read `1000` vs PDF OCR witness `['1800']`
  - Leaf `173` `p0173-b0007`: VLM read `1000` vs PDF OCR witness `['1800']`
  - Leaf `176` `p0176-b0006`: VLM read `1000` vs PDF OCR witness `['1080']`
  - Leaf `246` `p0246-b0004`: VLM read `200` vs PDF OCR witness `['100', '230']`
  - Leaf `248` `p0248-b0015`: VLM read `140` vs PDF OCR witness `['440']`
  - Leaf `268` `p0268-b0015`: VLM read `173` vs PDF OCR witness `['177']`
  - Leaf `301` `p0301-b0004`: VLM read `100` vs PDF OCR witness `['180']`

---

## 4. Structural Stitches, Flyleaf Filtering & Line-Wrap Audit

- **Cross-Page Assembly**: `407` prose joins, `0` split footnotes stitched, `4` multi-page tables unified, `0` total footnotes.
- **Suppressed Non-Authorial / Scanner Residue Blocks (`137` — verify no epigraph/dedication was caught)**:
  - Leaf `2` `p0002-b0001` (`scanner_residue`): *"Library of the Theological Seminary, PRINCETON, N. J. Purchased by the Mary Cheves Dulles "*
  - Leaf `5` `p0005-b0005` (`noise`): *"—"*
  - Leaf `5` `p0005-b0007` (`noise`): *"—"*
  - Leaf `5` `p0005-b0009` (`noise`): *"—"*
  - Leaf `5` `p0005-b0012` (`scanner_residue`): *"LIBRARY OF PRINCETON OCT 17 1913 THEOLOGICAL SEMINARY"*
  - Leaf `6` `p0006-b0001` (`scanner_residue`): *"Faint blue library stamp"*
  - Leaf `9` `p0009-b0007` (`noise`): *"VOL. II."*
  - Leaf `9` `p0009-b0008` (`noise`): *"B"*
  - Leaf `23` `p0023-b0006` (`noise`): *"Vol. II."*
  - Leaf `23` `p0023-b0007` (`noise`): *"C"*
  - Leaf `31` `p0031-b0015` (`noise`): *"Vol. II. D"*
  - Leaf `41` `p0041-b0005` (`noise`): *"Vol. II. E"*
- **Unattested Line-Wrap Hyphenation Decisions (`128` unique words out of `2316` total wraps)**: `coagulation` (p.28), `Kindalay` (p.30), `crystallization` (p.37), `woshipper` (p.42), `communion` (p.42), `Chapagodu` (p.42), `precedence` (p.45), `Miasamudra` (p.51), `efflorescence` (p.55), `superstratum` (p.55), `convulsed` (p.57), `miniature` (p.59), `Philosophical` (p.59), `pattana` (p.62), `Togotaru` (p.64), `speedily` (p.66), `bullockload` (p.69), `Cummavar` (p.80)

---

## 5. Scripts, Diacritics & Human Corrections

- **Detected Scripts**: `latin`: 900,193 chars, `greek`: 31 chars
- **Distinct Non-ASCII Glyphs (`47` across `418` leaves)**: Æ à á â æ ç é ë ì í ï ó ú ü ń œ ŕ Α Λ α γ δ ε η ι κ λ ν ο ρ ς σ τ υ φ ⁄ ₀ ₁ ⅓ ⅔ ⅕ ⅗ ⅙ ⅛ ⅜ ⅝ ⅞
- **Corrections Replayed**: `3` applied, `0` orphaned/unmatched
