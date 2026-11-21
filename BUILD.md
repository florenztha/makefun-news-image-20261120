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
