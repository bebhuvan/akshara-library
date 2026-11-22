# Akshara Public-Domain Digital Library (`akshara-library`)

**58 full scholarly editions · 1308 structured CSV/JSON statistical tables · CC0 Public Domain**

Every edition in this repository is compiled from camera-original Archive.org JP2 scans with 100% diplomatic orthographic fidelity.

## Per-Book Folder Structure

```text
collections/<collection>/<book_id>/
  README.md              # Overview & direct release links
  EDITORIAL_NOTE.md      # Source scan SHA-256 & normalization policy
  EDITION_REPORT.md      # 100-point rubric breakdown & validator telemetry
  PROOFING_BRIEFING.md   # Open items for community proofreaders
  edition_manifest.json  # Machine metadata & provenance tags
  cover.svg / cover.webp # Contextual series cover
  epub/<book_id>.epub    # Typeset EPUB 3
  html/<book_id>.html    # Single-page Gutenberg-style HTML
  markdown/<book_id>.md  # Scholarly Markdown
  tei/<book_id>.tei.xml  # TEI P5 XML archival master
  figures/*.webp         # Cropped plates & maps
  datasets/              # Diplomatic 2D + Tidy CSV/JSON tables
```

Heavy Print PDFs and de-blotted `.originals.pdf` camera scan backups live under GitHub Releases (`edition-<book_id>`).

## Complete Catalog

| Title | Author(s) | Year | Tier | Rubric | Tables |
| :--- | :--- | :---: | :--- | ---: | ---: |
| [A Guide to the India Office Records, 1600–1858](collections/indian-economic-history/guide-to-india-office-records-1919/README.md) | William Foster | 1919 | `machine_checked` | 100.0 | 14 |
| [A Journey from Madras through the Countries of Mysore, Canara, and Malabar](collections/indian-economic-history/journey-from-madras-vol-i/README.md) | Francis Buchanan | 1807 | `community` | 81.8 | 43 |
| [A Journey from Madras through the Countries of Mysore, Canara, and Malabar](collections/indian-economic-history/journey-from-madras-vol-ii/README.md) | Francis Buchanan | 1807 | `community` | 75.6 | 64 |
| [A Journey from Madras through the Countries of Mysore, Canara, and Malabar](collections/indian-economic-history/journey-from-madras-vol-iii/README.md) | Francis Buchanan | 1807 | `community` | 78.0 | 70 |
| [An Essay on the Economic Causes of Famines in India](collections/indian-economic-history/economic-causes-of-famines-in-india-ray-1909/README.md) | Satis Chandra Ray | 1909 | `community` | 99.8 | 4 |
| [Early Travels in India, 1583–1619](collections/indian-economic-history/early-travels-in-india-1583-1619/README.md) | William Foster | 1921 | `community` | 100.0 | 0 |
| [East India (Exchange and Currency): Announcements Concerning the Recommendations of the Committee on Indian Exchange and Currency (Cmd. 626)](collections/indian-economic-history/east-india-exchange-currency-1920/README.md) | Great Britain. India Office | 1920 | `machine_checked` | 100.0 | 0 |
| [Economics in India](collections/indian-economic-history/economics-in-india-inaugural-lecture-jevons-1915/README.md) | H. Stanley Jevons | 1915 | `machine_checked` | 100.0 | 0 |
| [England's Debt to India](collections/indian-economic-history/englands-debt-to-india-lajpat-rai-1917/README.md) | Lala Lajpat Rai | 1917 | `community` | 99.0 | 73 |
| [Essays, Speeches, Addresses and Writings (on Indian Politics) of the Hon'ble Dadabhai Naoroji](collections/indian-economic-history/essays-speeches-addresses-writings-naoroji-1887/README.md) | Dadabhai Naoroji, Chunilal Lallubhai Parekh | 1887 | `community` | 83.9 | 149 |
| [Exposition of the Practical Operation of the Judicial and Revenue Systems of India](collections/indian-economic-history/judicial-revenue-systems-india-rammohun-1832/README.md) | Rammohun Roy | 1832 | `machine_checked` | 100.0 | 3 |
| [Famines and Land Assessments in India](collections/indian-economic-history/famines-and-land-assessments/README.md) | Romesh Chunder Dutt | 1900 | `community` | 85.4 | 29 |
| [From Akbar to Aurangzeb](collections/indian-economic-history/from-akbar-to-aurangzeb/README.md) | W. H. Moreland | 1923 | `community` | 96.0 | 27 |
| [India at the Death of Akbar](collections/indian-economic-history/india-at-the-death-of-akbar/README.md) | W. H. Moreland | 1920 | `machine_checked` | 100.0 | 5 |
| [India: What Can It Teach Us?](collections/general-heritage/india-what-can-it-teach-us/README.md) | F. Max Müller | 1892 | `machine_checked` | 100.0 | 2 |
| [Indian Famines, Their Causes and Prevention](collections/indian-economic-history/indian-famines-causes-prevention-dutt-1901/README.md) | Romesh Chunder Dutt | 1901 | `community` | 95.0 | 3 |
| [Indian Finance](collections/indian-economic-history/indian-finance-moxon-1881/README.md) | Thomas Bouchier Moxon | 1881 | `machine_checked` | 100.0 | 9 |
| [Indian Shipping](collections/indian-economic-history/indian-shipping/README.md) | Radhakumud Mookerji | 1912 | `machine_checked` | 100.0 | 7 |
| [Introduction to the Peishwa's Diaries](collections/indian-economic-history/peishwas-diaries-intro/README.md) | Mahadev Govind Ranade | 1900 | `machine_checked` | 100.0 | 0 |
| [Life in an Indian Village](collections/general-heritage/life-in-an-indian-village/README.md) | T. Ramakrishna | 1891 | `machine_checked` | 100.0 | 0 |
| [Modern Religious Movements in India](collections/general-heritage/modern-religious-movements-india/README.md) | John Nicol Farquhar | 1915 | `machine_checked` | 100.0 | 5 |
| [Musalmans and Money-Lenders in the Punjab](collections/indian-economic-history/musalmans-and-money-lenders/README.md) | Septimus Smet Thorburn | 1886 | `community` | 99.4 | 13 |
| [Poverty and Un-British Rule in India](collections/indian-economic-history/poverty-and-un-british-rule/README.md) | Dadabhai Naoroji | 1901 | `community` | 71.6 | 169 |
| [Recent Economic Developments in the Punjab](collections/indian-economic-history/recent-economic-developments-punjab-wilson-1910/README.md) | James Wilson | 1910 | `community` | 88.0 | 15 |
| [Report on Past Famines in the Bombay Presidency](collections/indian-economic-history/report-past-famines-bombay-etheridge-1868/README.md) | A. T. Etheridge | 1868 | `community` | 90.0 | 63 |
| [Some Aspects of Indian Commerce and Industry](collections/indian-economic-history/some-aspects-indian-commerce-industry-shirras-1911/README.md) | G. Findlay Shirras | 1911 | `machine_checked` | 100.0 | 2 |
| [Speeches and Writings of Dadabhai Naoroji](collections/indian-economic-history/speeches-and-writings-naoroji-1918/README.md) | Dadabhai Naoroji | 1918 | `community` | 92.4 | 39 |
| [The Early History of India](collections/general-heritage/early-history-of-india-1924/README.md) | Vincent A. Smith | 1924 | `community` | 86.3 | 15 |
| [The Early History of the Tea Industry in North-East India](collections/indian-economic-history/early-history-tea-industry/README.md) | Harold H. Mann | 1918 | `community` | 97.0 | 3 |
| [The East India Trade in the XVIIth Century, in Its Political and Economic Aspects](collections/indian-economic-history/east-india-trade-17th-century-khan/README.md) | Shafaat Ahmad Khan | 1923 | `community` | 92.0 | 13 |
| [The Economic History of India in the Victorian Age](collections/indian-economic-history/economic-history-india-victorian-age-dutt/README.md) | Romesh Chunder Dutt | 1904 | `community` | 98.5 | 74 |
| [The Economic History of India Under Early British Rule](collections/indian-economic-history/economic-history-india-early-british-dutt/README.md) | Romesh Chunder Dutt | 1906 | `community` | 92.0 | 27 |
| [The Economic Life of a Bengal District](collections/indian-economic-history/economic-life-bengal-district-faridpur-1916/README.md) | J. C. Jack | 1916 | `machine_checked` | 100.0 | 20 |
| [The English Factories in India, 1618–1621](collections/indian-economic-history/english-factories-india-1618-1621-vol-01/README.md) | William Foster | 1906 | `machine_checked` | 100.0 | 5 |
| [The English Factories in India, 1622–1623](collections/indian-economic-history/english-factories-india-1622-1623-vol-02/README.md) | William Foster | 1908 | `community` | 85.0 | 2 |
| [The English Factories in India, 1624–1629](collections/indian-economic-history/english-factories-india-1624-1629-vol-03/README.md) | William Foster | 1909 | `community` | 100.0 | 1 |
| [The English Factories in India, 1630–1633](collections/indian-economic-history/english-factories-india-1630-1633-vol-04/README.md) | William Foster | 1910 | `machine_checked` | 100.0 | 1 |
| [The English Factories in India, 1634–1636](collections/indian-economic-history/english-factories-india-1634-1636-vol-05/README.md) | William Foster | 1911 | `machine_checked` | 100.0 | 0 |
| [The English Factories in India, 1637–1641](collections/indian-economic-history/english-factories-india-1637-1641-vol-06/README.md) | William Foster | 1912 | `community` | 100.0 | 0 |
| [The English Factories in India, 1642–1645](collections/indian-economic-history/english-factories-india-1642-1645-vol-07/README.md) | William Foster | 1913 | `machine_checked` | 100.0 | 1 |
| [The English Factories in India, 1646–1650](collections/indian-economic-history/english-factories-india-1646-1650-vol-08/README.md) | William Foster | 1914 | `machine_checked` | 100.0 | 0 |
| [The English Factories in India, 1651–1654](collections/indian-economic-history/english-factories-india-1651-1654-vol-09/README.md) | William Foster | 1915 | `machine_checked` | 100.0 | 0 |
| [The English Factories in India, 1655–1660](collections/indian-economic-history/english-factories-india-1655-1660-vol-10/README.md) | William Foster | 1921 | `community` | 100.0 | 0 |
| [The English Factories in India, 1661–1664](collections/indian-economic-history/english-factories-india-1661-1664-vol-11/README.md) | William Foster | 1923 | `community` | 94.0 | 0 |
| [The English Factories in India, 1665–1667](collections/indian-economic-history/english-factories-india-1665-1667-vol-12/README.md) | Sir William Foster | 1925 | `community` | 100.0 | 2 |
| [The History & Economics of Indian Famines](collections/indian-economic-history/history-and-economics-indian-famines-loveday-1914/README.md) | Alexander Loveday | 1914 | `community` | 85.0 | 9 |
| [The Imperial Gazetteer of India: The Indian Empire, Vol. I — Descriptive](collections/indian-economic-history/imperial-gazetteer-of-india-vol-01-descriptive/README.md) | Great Britain. India Office | 1907 | `community` | 80.0 | 81 |
| [The Imperial Gazetteer of India: The Indian Empire, Vol. II — Historical](collections/indian-economic-history/imperial-gazetteer-of-india-vol-02-historical/README.md) | Great Britain. India Office | 1908 | `community` | 96.8 | 0 |
| [The Imperial Gazetteer of India: The Indian Empire, Vol. III — Economic](collections/indian-economic-history/imperial-gazetteer-of-india-vol-03-economic/README.md) | Great Britain. India Office | 1907 | `community` | 84.0 | 96 |
| [The Imperial Gazetteer of India: The Indian Empire, Vol. IV — Administrative](collections/indian-economic-history/imperial-gazetteer-of-india-vol-04-administrative/README.md) | Great Britain. India Office | 1907 | `community` | 88.0 | 60 |
| [The Mughal Administration: Six Lectures](collections/general-heritage/mughal-administration/README.md) | Jadunath Sarkar | 1920 | `machine_checked` | 100.0 | 0 |
| [The People of India](collections/general-heritage/people-of-india/README.md) | Sir Herbert Hope Risley | 1915 | `machine_checked` | 100.0 | 51 |
| [The Periplus of the Erythræan Sea: Travel and Trade in the Indian Ocean by a Merchant of the First Century](collections/indian-economic-history/periplus-erythraean-sea/README.md) | Wilfred H. Schoff | 1912 | `machine_checked` | 100.0 | 4 |
| [The Pālas of Bengal](collections/general-heritage/palas-of-bengal/README.md) | R. D. Banerji | 1915 | `community` | 86.4 | 0 |
| [The Register of Letters &c. of the Governour and Company of Merchants of London Trading into the East Indies, 1600–1619](collections/indian-economic-history/eic-first-letter-book-1600-1619/README.md) | George Birdwood, William Foster | 1893 | `community` | 96.8 | 21 |
| [The Religion of the Veda](collections/general-heritage/religion-of-the-veda/README.md) | Maurice Bloomfield | 1908 | `machine_checked` | 100.0 | 0 |
| [The Truth About Indian Opium](collections/indian-economic-history/truth-about-indian-opium/README.md) | G. Graham Dixon, Great Britain. India Office | 1922 | `machine_checked` | 100.0 | 13 |
| [While Sewing Sandals](collections/general-heritage/while-sewing-sandals/README.md) | Emma Rauschenbusch-Clough | 1899 | `machine_checked` | 100.0 | 1 |
