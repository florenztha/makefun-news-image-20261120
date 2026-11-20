# Build notes — news-image-20261120

- **Day summed up:** Friday 20 November 2026 (events that happened, or were
  first reported, that day in at least one time zone).
- **Stories:** 36 total — 3 leads and 10 features drawn as original vector
  scenes, plus 23 one-line briefs. Region counts on the poster are computed
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
