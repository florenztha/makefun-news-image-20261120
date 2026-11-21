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
- **V7 revision (over round 2 / V4):** same 36 stories, same lead trio,
  features, strap and numbers — three execution upgrades from a teardown of
  the then-current top ten: the world map is plotted from real
  longitude/latitude coastline outlines (pins renumbered to this poster's
  story order), each lead panel carries a small basis tag (MAYOR'S COUNT ·
  WEATHER OFFICE · CLOSING DRAFT), and the markets feature panel shows the
  intraday index moves (Nikkei −4.9%, KOSPI −5.4%, TAIEX −6.8%, Hang Seng
  −2.0%) as a data grid. entry.png: 400,708 bytes,
  sha256 329f3d52074fa53d542806cf886dda3e0b32571455c15f1286466fd0ad695e08,
  three consecutive renders byte-identical.
