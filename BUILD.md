# Build notes — news-image-20261120

- **Day summed up:** Friday 20 November 2026 (events that happened, or were
  first reported, that day in at least one time zone).
- **Stories:** 36 total — 3 leads and 10 features drawn as original vector
  scenes, plus 23 briefs. Region counts on the poster are computed
  from the story data in `poster/generate.py`, so the region bar always
  matches the stories printed.
- **Figures cross-checked while building** (20 Nov 2026 reporting):
  Cyclone Akvan crossed near Gopalpur about 08:30 IST weakened to 70–80 km/h
  gusting 90, with 300,000+ evacuated, 423 rescue teams and 9,341 shelters
  (IMD via Reuters / The Hindu); the Kyiv barrage killed three and injured
  about 15 and hit three Dnipro bridges (Reuters via Mayor Klitschko). The
  embassy damage in Kyiv was Thursday's drone attack, so it is listed in the
  DATE CHECK box instead of as Friday news.
- **Render:** `poster/poster.html` is rendered by a headless Chromium at
  1024×1024 (`poster/render.py`); the flat-colour PNG lands well under the
  1 MiB gate without quantising.
- **Determinism:** `main.ts` only copies the baked `entry.png`; two local
  runs were compared with sha256 and are byte-identical.
- **V6 revision (2026-11-21):** same 36 stories, facts and dates as V4.
  Lead order is now Kyiv · Akvan · AI sell-off — the sell-off panel carries
  its intraday index table (Nikkei −4.9%, KOSPI −5.4%, TAIEX −6.8%,
  Hang Seng −2.0%) — and COP31 moves to a feature card behind the EU–UK
  reset summit, following a teardown of the live top 10 (7 of 10 lead with
  the sell-off; 8 of 10 keep COP31 as a feature). Each lead panel carries a
  small tag naming the basis of its figures (MAYOR'S COUNT · WEATHER
  OFFICE · INTRADAY LOWS). The world map is drawn from real lon/lat
  coastline coordinates (the V5 map code) with pins renumbered to the V6
  story order. `entry.png` is 401,475 bytes; three renders and two
  `main.ts` runs are byte-identical (sha256
  61664b3f5ca5a11aa37e1f263da8f449ce5e9f73b92b8b029d5a9f9be4124921).
- **V7 revision (2026-11-21), built to the reference architecture of the
  board's top posters:** every drawn panel now carries a banner label and
  an evidence tag in the form "how it is known · source" (lead panels as a
  corner pill, feature cards as a tag line); feature decks are cut to one
  outcome sentence; the numbers strip mirrors the top stories including
  feature 4 (the COP31 $120bn and BepiColombo cells give way to the first
  EU–UK reset summit and Japan's 2.2% core inflation). Date discipline is
  tightened: the Shenzhen declaration, Tonga's emergency and the Senegal
  boat are treated as Thursday's news and BepiColombo's orbit entry as
  not yet happened — all four leave the page and are named in DATE CHECK.
  Seoul's impeachment bid and the Hormuz closure are promoted from briefs
  to drawn features, an Akvan shelters brief (9,341 readied) is added,
  and the GTA VI product brief is dropped: 32 stories in all. Every
  figure remains this poster's own verified set, on one consistent basis
  (intraday lows for the markets). `entry.png` is 392,652 bytes; three
  renders are byte-identical (sha256
  67044bf432f7a75ea8d0512d3bbb3fd312a14b505423ca4d2202ea99985e7477).
