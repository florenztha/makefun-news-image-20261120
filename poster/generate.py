#!/usr/bin/env python3
"""Generate poster.html — a one-page world-news poster for Friday 20 November 2026.

All stories were reported on Friday 20 November 2026 (any time zone). Every
drawing is an original inline SVG built in this file; no photographs and no
third-party artwork are used. Run:  python3 poster/generate.py
It writes poster/poster.html next to this script; poster/render.py then
renders that page to entry.png at 1024x1024.

V6 revision (over V4): the third lead is the AI sell-off with its intraday
index table (the arrangement the current top of the board uses), COP31 moves
to a feature card, the EU–UK reset summit opens the features, each lead panel
carries a small tag naming the basis of its figures, and the world map is
drawn from real lon/lat coastline coordinates instead of freehand blobs.
Story content — the same 36 verified stories, facts and dates — is unchanged.

V7 revision (over V6), following the architecture of the board's top
posters: every drawn panel carries a banner label and an evidence tag in
the form "how it is known · source"; feature decks are cut to one outcome
sentence; the numbers strip mirrors the top stories including feature 4;
and the date discipline is tightened — the Shenzhen declaration, Tonga's
emergency and the Senegal boat are treated as Thursday's news and
BepiColombo's orbit entry as not yet happened, so all four leave the page
and are named in DATE CHECK instead. Seoul's impeachment bid and the
Hormuz closure are promoted from briefs to drawn features, an Akvan
shelters brief is added, and the GTA VI product brief is dropped:
32 stories in all. Every figure remains this poster's own verified set,
on one consistent basis (intraday lows for the markets).
"""

# ---------------------------------------------------------------- stories
# region keys: EU Europe, AP Asia-Pacific, AM Americas, ME Middle East,
# AF Africa, OC Oceania, WS World / Space. Counts on the poster are computed
# from these fields, so the region bar can never disagree with the stories.

LEADS = [
    {
        "n": 1, "region": "EU", "kicker": "KYIV, UKRAINE · WAR",
        "art": "kyiv", "tag": "MAYOR'S COUNT · REUTERS",
        "headline": "Missiles hit Kyiv's Dnipro bridges; three killed",
        "body": "Overnight waves from 01:25 struck three bridges across the Dnipro, "
                "killed three people and cut power and water; about 15 were "
                "injured in the biggest bridge attack of the war. "
                "(Reuters, Kyiv Independent)",
    },
    {
        "n": 2, "region": "AP", "kicker": "ODISHA, INDIA · CYCLONE",
        "art": "akvan", "tag": "WEATHER OFFICE · IMD",
        "headline": "Cyclone Akvan comes ashore near Gopalpur",
        "body": "Akvan crossed the coast about 08:30 weakened, at 70–80 km/h "
                "gusting 90; over 300,000 people had been evacuated and 423 "
                "rescue teams deployed. No major damage by midday. (IMD, Reuters)",
    },
    {
        "n": 3, "region": "AP", "kicker": "SEOUL / TOKYO · MARKETS",
        "art": "markets_lead",
        "headline": "AI sell-off sinks Asia's markets",
        "body": "Chipmakers led the slide after Wall Street's fall; the Nikkei "
                "lost 4.9% and the KOSPI 5.4% at intraday lows — Asia's worst "
                "week since 2020. (Reuters)",
    },
]

FEATURES = [
    {
        "n": 4, "region": "EU", "kicker": "BRUSSELS · EUROPE", "art": "brussels",
        "tag": "SUMMIT HELD · EU COUNCIL",
        "headline": "Burnham holds first EU–UK reset summit",
        "body": "The UK PM meets Costa & von der Leyen; agrifood and "
                "carbon-market links eyed. (EU Council)",
    },
    {
        "n": 5, "region": "EU", "kicker": "ANTALYA, TÜRKİYE · CLIMATE", "art": "cop31mini",
        "tag": "DRAFT TEXT · UN NEWS",
        "headline": "COP31 reaches its final day deadlocked",
        "body": "The closing draft omits a fossil-fuel phase-out and leaves "
                "a $120bn finance gap open. (UN News, Reuters)",
    },
    {
        "n": 6, "region": "AP", "kicker": "TOKYO · ECONOMY", "art": "cpi",
        "tag": "OFFICIAL DATA · REUTERS",
        "headline": "Japan core inflation quickens to 2.2%",
        "body": "October core CPI rises from 2.1% — the fastest pace this "
                "year. (Reuters)",
    },
    {
        "n": 7, "region": "AP", "kicker": "BEIJING · RATES", "art": "rates",
        "tag": "BANK DECISION · PBOC",
        "headline": "China holds lending rates for 18th month",
        "body": "One-year LPR stays at 3.0% and the five-year at 3.5%, "
                "exactly as expected. (PBOC, Reuters)",
    },
    {
        "n": 8, "region": "OC", "kicker": "WELLINGTON · CRICKET", "art": "cricket",
        "tag": "SCORECARD · ICC",
        "headline": "Phillips makes history with 118",
        "body": "First NZ batter with centuries in all three formats "
                "against India inside a year. (ICC, AP)",
    },
    {
        "n": 9, "region": "AM", "kicker": "SAN SALVADOR · POLITICS", "art": "ballot",
        "tag": "FILED · AP",
        "headline": "Bukele registers for a third term",
        "body": "Files with the electoral tribunal for the February 2027 "
                "vote; rights groups object. (AP)",
    },
    {
        "n": 10, "region": "EU", "kicker": "ROME · LABOUR", "art": "strike",
        "tag": "UNION FIGURE · CGIL",
        "headline": "Italy's CGIL holds 24-hour general strike",
        "body": "Unions rally in some 100 squares against the 2027 "
                "budget. (CGIL, AFP)",
    },
    {
        "n": 11, "region": "EU", "kicker": "BARCELONA · HEALTH", "art": "pill",
        "tag": "TRIAL DATA · REUTERS",
        "headline": "Pancreatic-cancer pill shrinks tumours",
        "body": "A 60.7% response in an early trial, against 23–42% "
                "for chemotherapy alone. (Reuters)",
    },
    {
        "n": 12, "region": "AP", "kicker": "SEOUL · COURTS", "art": "seoul",
        "tag": "PARTY DECISION · SBS",
        "headline": "Ruling party moves to impeach the chief justice",
        "body": "The ruling party adopts a bid to impeach Chief Justice "
                "Cho Hee-dae. (SBS)",
    },
    {
        "n": 13, "region": "ME", "kicker": "HORMUZ · SHIPPING", "art": "hormuz",
        "tag": "TRACKED · UKMTO",
        "headline": "Four attacks in 96 hours keep the strait shut",
        "body": "46 ships wait at anchor while the strait stays shut. "
                "(UKMTO)",
    },
]

BRIEFS = [
    (14, "AP", "ODISHA", "9,341 shelters readied ahead of Cyclone Akvan's landfall (IMD)"),
    (15, "AP", "COX'S BAZAR", "Rohingya camps weep and pray after Thursday's ICJ genocide ruling (Al Jazeera)"),
    (16, "ME", "GAZA", "Aid groups score the peace plan's implementation at 4 of 26 points (UN News)"),
    (17, "AF", "BLANTYRE", "Malawi fuel crisis: night queues and a 20-litre daily cap (Al Jazeera)"),
    (18, "AM", "LAS VEGAS", "Russell fastest in wet F1 practice, 1:47.272 (Formula1.com)"),
    (19, "AM", "MATO GROSSO", "Lula meets Chief Raoni as Indigenous land is recognised in Brazil (Al Jazeera)"),
    (20, "OC", "BOUGAINVILLE", "Rio Tinto pledges $370m for the Panguna mine's legacy (Reuters)"),
    (21, "OC", "CANBERRA", "Budget office warns AUKUS submarine sales could shrink the US fleet (Reuters)"),
    (22, "AM", "FLORIDA", "St Johns River hits a record 18.3 ft; four counties shut schools (AP)"),
    (23, "AM", "IOWA", "US Army carries out a noon detonation of 68 unstable explosive barrels (AP)"),
    (24, "AM", "WASHINGTON", "Pentagon puts the US war cost against Iran at $48.3bn (Reuters)"),
    (25, "EU", "LONDON", "UK & Norway fund £100m+ for two Ukrainian naval vessels (BBC)"),
    (26, "EU", "COPENHAGEN", "Denmark's parliament approves the Greenland defence bill (AFP)"),
    (27, "AP", "JAKARTA", "Indonesia's parliament passes the asset-forfeiture bill (Reuters)"),
    (28, "ME", "DOHA", "U17 World Cup: Australia stun Argentina 2–0 (FIFA)"),
    (29, "AF", "JOHANNESBURG", "Harmer spins the Proteas to a Test win as Bavuma sets a record (ICC)"),
    (30, "AP", "HONG KONG", "Badminton Open reaches the semifinals after an upset (BWF)"),
    (31, "EU", "TURIN", "Alcaraz–Cobolli and Medvedev–Tiafoe close the ATP Finals groups (ATP)"),
    (32, "WS", "GLOBAL", "The UN marks World Children's Day, 20 November, across member states (UN News)"),
]

NUMBERS = [
    ("3", "killed in Kyiv as three Dnipro bridges are hit"),
    ("300,000+", "evacuated in Odisha ahead of Cyclone Akvan"),
    ("−4.9%", "Nikkei at its intraday low in the AI sell-off"),
    ("1st", "EU–UK reset summit, held in Brussels"),
    ("2.2%", "Japan core inflation in October, fastest this year"),
    ("118", "Phillips' historic century vs India, Wellington"),
]

DATE_CHECK = (
    "First reported Thursday 19 Nov, so NOT shown as Friday's news: the Trump–Xi–Putin "
    "Shenzhen summit and its joint declaration · the drone strike on Kyiv's Dutch & "
    "Austrian embassies · Anthropic's Nasdaq debut · the ICJ's Rohingya ruling · the "
    "Senate's 48–51 Iran war-powers vote · GTA VI's midnight launch · the $190.4m Van "
    "Gogh sale · Tonga's drought emergency · the migrant boat lost off Senegal. "
    "Not yet happened: BepiColombo's entry into orbit at Mercury (Saturday) · "
    "any final COP31 text."
)

FOOTER = (
    "Every story here happened, or was first reported, on Friday 20 November 2026 in at "
    "least one time zone. Claims are attributed, not stated as fact. Sources: Reuters, AP, "
    "AFP, BBC, IMD, UN News, Al Jazeera, ICC, EU Council, PBOC. Original vector drawings."
)

REGION_NAMES = [
    ("EU", "EUROPE"), ("AM", "AMERICAS"), ("AP", "ASIA-PACIFIC"), ("ME", "MIDEAST"),
    ("AF", "AFRICA"), ("OC", "OCEANIA"), ("WS", "WORLD / SPACE"),
]
REGION_COLORS = {
    "EU": "#17616b", "AM": "#b02a24", "AP": "#c9932b", "ME": "#5b4a8a",
    "AF": "#2e6b34", "OC": "#20708c", "WS": "#444c5c",
}

# ---------------------------------------------------------------- drawings
# Every drawing is an original flat-vector scene drawn with SVG shapes.

def art_kyiv(w, h):
    return f'''<svg viewBox="0 0 300 118" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
<rect width="300" height="118" fill="#131f36"/>
<g stroke="#ff9c3a" stroke-width="2.4" stroke-linecap="round">
<line x1="18" y1="6" x2="86" y2="58"/><line x1="52" y1="2" x2="128" y2="60"/>
<line x1="96" y1="8" x2="168" y2="62"/><line x1="150" y1="2" x2="214" y2="58"/></g>
<g fill="#ffb35c"><circle cx="90" cy="60" r="6"/><circle cx="132" cy="62" r="5"/><circle cx="218" cy="60" r="6"/></g>
<g fill="#0a1424"><rect x="0" y="66" width="34" height="30"/><rect x="40" y="58" width="22" height="38"/>
<rect x="238" y="60" width="26" height="36"/><rect x="270" y="68" width="30" height="28"/></g>
<g fill="#ffd98a"><rect x="8" y="74" width="4" height="4"/><rect x="46" y="68" width="4" height="4"/>
<rect x="246" y="70" width="4" height="4"/><rect x="278" y="76" width="4" height="4"/></g>
<rect x="0" y="94" width="300" height="24" fill="#1d3a5f"/>
<path d="M0 96 Q40 90 78 96 T160 96 T240 96 T300 96" stroke="#7fb2d9" fill="none" stroke-width="2"/>
<path d="M28 96 L60 78 L92 96 M118 96 L150 78 L182 96 M208 96 L240 78 L272 96" stroke="#e8e2cc" fill="none" stroke-width="3"/>
<rect x="8" y="98" width="172" height="16" fill="#0a1424"/>
<text x="14" y="110" font-family="Arial" font-size="10.5" font-weight="bold" fill="#ff8d80">01:25 LOCAL · 3 BRIDGES HIT</text>
<rect x="8" y="6" width="76" height="23" fill="#b02a24"/>
<text x="16" y="23" font-family="Georgia" font-size="16" font-weight="bold" fill="#fff">KYIV</text>
</svg>'''

def art_akvan(w, h):
    return f'''<svg viewBox="0 0 300 118" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
<rect width="300" height="118" fill="#bfe0dd"/>
<path d="M0 0 H150 L128 34 L142 62 L118 92 L128 118 H0 Z" fill="#e6d9ae"/>
<path d="M150 0 H300 V118 H128 L118 92 L142 62 L128 34 Z" fill="#5ea8b8"/>
<g fill="none" stroke="#ffffff" stroke-width="5" stroke-linecap="round">
<path d="M196 26 a30 30 0 1 1 -30 30"/><path d="M200 40 a17 17 0 1 1 -17 17"/></g>
<circle cx="192" cy="52" r="6" fill="#ffffff"/>
<circle cx="128" cy="66" r="5" fill="#b02a24"/>
<text x="86" y="60" font-family="Arial" font-size="10" font-weight="bold" fill="#7a1d18">GOPALPUR</text>
<text x="196" y="104" font-family="Arial" font-size="10" fill="#eaf6f5">BAY OF BENGAL</text>
<rect x="8" y="8" width="118" height="17" fill="#b02a24"/>
<text x="14" y="20" font-family="Arial" font-size="10.5" font-weight="bold" fill="#fff">CYCLONE AKVAN</text>
<text x="10" y="40" font-family="Arial" font-size="10" font-weight="bold" fill="#7a1d18">LANDFALL 08:30 IST</text>
</svg>'''

def art_markets_lead(w, h):
    rows = [("NIKKEI", "−4.9%"), ("KOSPI", "−5.4%"), ("TAIEX", "−6.8%"), ("HANG SENG", "−2.0%")]
    parts = [f'''<svg viewBox="0 0 300 118" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
<rect width="300" height="118" fill="#231d26"/>
<polyline points="8,10 60,16 112,22 164,34 216,40 262,50 292,54" fill="none" stroke="#e04a3a" stroke-width="3.4"/>
<text x="10" y="30" font-family="Georgia" font-size="25" font-weight="bold" fill="#ffffff">AI SELL-OFF</text>
<text x="11" y="45" font-family="Arial" font-size="10" fill="#cbb">INTRADAY LOWS · REUTERS</text>''']
    for i, (name, val) in enumerate(rows):
        y = 66 + i * 13
        parts.append(f'<text x="150" y="{y}" font-family="Arial" font-size="11.5" font-weight="bold" fill="#e8e2cc">{name}</text>')
        parts.append(f'<text x="292" y="{y}" text-anchor="end" font-family="Arial" font-size="11.5" font-weight="bold" fill="#ff8d80">{val}</text>')
    parts.append('</svg>')
    return "".join(parts)

def _mini(body):
    return f'<svg viewBox="0 0 300 62" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">{body}</svg>'

def art_cop31mini():
    return _mini('''<rect width="300" height="62" fill="#dcead9"/>
<circle cx="34" cy="31" r="19" fill="#3d7ca8"/><path d="M22 22 q8 -5 13 1 q-7 4 -13 -1 M30 42 q9 5 15 -1 q-8 -5 -15 1" fill="#69a35f"/>
<rect x="66" y="10" width="8" height="38" rx="4" fill="#e8e2cc" stroke="#8a845f"/><path d="M70 16 v24" stroke="#d2543c" stroke-width="3.4"/><circle cx="70" cy="52" r="6" fill="#d2543c"/>
<text x="92" y="30" font-family="Georgia" font-size="17" font-weight="bold" fill="#7a1d18">$120BN GAP</text>
<text x="92" y="47" font-family="Arial" font-size="10" font-weight="bold" fill="#40513f">FINAL DAY · ANTALYA</text>
<text x="292" y="30" text-anchor="end" font-family="Georgia" font-size="15" font-weight="bold" fill="#b02a24">NO DEAL</text>''')

def art_brussels():
    return _mini('''<rect width="300" height="62" fill="#27407c"/>
<g fill="#ffd94d"><circle cx="52" cy="14" r="2.4"/><circle cx="66" cy="18" r="2.4"/><circle cx="72" cy="28" r="2.4"/><circle cx="68" cy="40" r="2.4"/><circle cx="56" cy="46" r="2.4"/><circle cx="42" cy="44" r="2.4"/><circle cx="34" cy="34" r="2.4"/><circle cx="36" cy="22" r="2.4"/></g>
<text x="92" y="38" font-family="Georgia" font-size="19" font-weight="bold" fill="#fff">RESET TALKS</text>
<g><rect x="238" y="10" width="52" height="42" fill="#31498c"/><path d="M238 10 L290 52 M290 10 L238 52" stroke="#fff" stroke-width="6"/><path d="M264 10 V52 M238 31 H290" stroke="#fff" stroke-width="10"/><path d="M264 10 V52 M238 31 H290" stroke="#c33" stroke-width="5"/></g>''')

def art_cpi():
    return _mini('''<rect width="300" height="62" fill="#f0e7cd"/>
<g fill="#8a9ba8"><rect x="30" y="34" width="20" height="20"/><rect x="62" y="30" width="20" height="24"/><rect x="94" y="26" width="20" height="28"/></g>
<rect x="126" y="18" width="20" height="36" fill="#b02a24"/>
<text x="160" y="38" font-family="Georgia" font-size="24" font-weight="bold" fill="#7a1d18">2.2%</text>
<circle cx="272" cy="31" r="15" fill="#b02a24"/><circle cx="272" cy="31" r="11" fill="#f6efdb"/>''')

def art_rates():
    return _mini('''<rect width="300" height="62" fill="#fdfaf0"/>
<text x="12" y="13" font-family="Arial" font-size="9.5" font-weight="bold" letter-spacing="1.5" fill="#17263f">RATES HELD</text>
<line x1="14" y1="24" x2="180" y2="24" stroke="#b02a24" stroke-width="3"/><line x1="14" y1="44" x2="180" y2="44" stroke="#17616b" stroke-width="3"/>
<text x="188" y="29" font-family="Arial" font-size="14" font-weight="bold" fill="#7a1d18">1-YR 3.0%</text>
<text x="188" y="50" font-family="Arial" font-size="14" font-weight="bold" fill="#17616b">5-YR 3.5%</text>''')

def art_cricket():
    return _mini('''<rect width="300" height="62" fill="#2e6b34"/>
<text x="16" y="44" font-family="Georgia" font-size="32" font-weight="bold" fill="#fff">118</text>
<g transform="rotate(24 190 30)"><rect x="184" y="8" width="11" height="40" rx="4" fill="#e6cf9a"/><rect x="187" y="44" width="5" height="12" fill="#7a4a21"/></g>
<circle cx="238" cy="40" r="10" fill="#c8352c"/><path d="M231 34 q7 6 0 12 M245 34 q-7 6 0 12" stroke="#fff" fill="none" stroke-width="1.4"/>
<text x="200" y="17" font-family="Arial" font-size="11" font-weight="bold" fill="#dff0d8">RECORD</text>''')

def art_ballot():
    return _mini('''<rect width="300" height="62" fill="#e9e2f0"/>
<rect x="96" y="30" width="86" height="26" fill="#5b4a8a"/><rect x="88" y="24" width="102" height="9" fill="#3f3465"/>
<g transform="rotate(-8 140 22)"><rect x="118" y="4" width="44" height="26" fill="#fff" stroke="#b9b0cc"/><path d="M128 18 l8 8 l16 -16" stroke="#2e6b34" stroke-width="3.4" fill="none"/></g>
<text x="196" y="42" font-family="Georgia" font-size="21" font-weight="bold" fill="#3f3465">FEB 2027</text>''')

def art_strike():
    return _mini('''<rect width="300" height="62" fill="#f3e3d3"/>
<g fill="#31405c"><circle cx="36" cy="34" r="6"/><rect x="29" y="40" width="14" height="14"/><circle cx="66" cy="36" r="6"/><rect x="59" y="42" width="14" height="12"/><circle cx="96" cy="34" r="6"/><rect x="89" y="40" width="14" height="14"/></g>
<g><rect x="126" y="8" width="3" height="34" fill="#7a4a21"/><path d="M129 8 h44 l-8 9 l8 9 h-44 Z" fill="#b02a24"/></g>
<text x="178" y="38" font-family="Georgia" font-size="17" font-weight="bold" fill="#7a1d18">100 SQUARES</text>''')

def art_pill():
    return _mini('''<rect width="300" height="62" fill="#e5f0ea"/>
<g transform="rotate(-24 90 31)"><rect x="48" y="18" width="84" height="27" rx="13" fill="#e8e2cc" stroke="#9db8a8"/><path d="M90 18 h20 a13 13 0 0 1 0 27 h-20 Z" fill="#d2543c"/></g>
<g fill="#8a5aa0"><circle cx="196" cy="24" r="7"/><circle cx="212" cy="34" r="5"/><circle cx="186" cy="38" r="4"/></g>
<path d="M150 30 h26" stroke="#2e6b34" stroke-width="3"/><path d="M170 24 l8 6 l-8 6 Z" fill="#2e6b34"/>
<text x="228" y="38" font-family="Georgia" font-size="20" font-weight="bold" fill="#20503a">60.7%</text>''')

def art_seoul():
    return _mini('''<rect width="300" height="62" fill="#ece7da"/>
<g fill="#8a7a52"><rect x="22" y="16" width="9" height="34"/><rect x="44" y="16" width="9" height="34"/><rect x="66" y="16" width="9" height="34"/></g>
<rect x="14" y="10" width="70" height="6" fill="#5c4d2e"/><rect x="14" y="50" width="70" height="6" fill="#5c4d2e"/>
<g transform="rotate(28 128 30)"><rect x="122" y="12" width="12" height="20" rx="3" fill="#7a4a21"/><rect x="126" y="30" width="4" height="16" fill="#7a4a21"/></g>
<circle cx="150" cy="50" r="4" fill="#7a4a21"/>
<text x="168" y="40" font-family="Georgia" font-size="20" font-weight="bold" fill="#3f3465">IMPEACH</text>''')

def art_hormuz():
    return _mini('''<rect width="300" height="62" fill="#22354f"/>
<path d="M0 0 H118 L86 20 L40 26 L0 22 Z" fill="#d9c491"/>
<path d="M300 0 H196 L224 18 L268 24 L300 20 Z" fill="#d9c491"/>
<g><path d="M110 44 L164 44 L156 54 L118 54 Z" fill="#0d1524"/><rect x="124" y="36" width="12" height="8" fill="#b02a24"/><rect x="138" y="36" width="12" height="8" fill="#c9932b"/></g>
<g><path d="M196 40 L240 40 L234 48 L202 48 Z" fill="#0d1524"/><rect x="206" y="34" width="10" height="6" fill="#7fb2d9"/></g>
<text x="292" y="58" text-anchor="end" font-family="Georgia" font-size="15" font-weight="bold" fill="#ffd98a">STRAIT SHUT</text>''')

ART = {
    "kyiv": lambda: art_kyiv(300, 118), "akvan": lambda: art_akvan(300, 118),
    "markets_lead": lambda: art_markets_lead(300, 118), "cop31mini": art_cop31mini,
    "brussels": art_brussels, "cpi": art_cpi,
    "rates": art_rates, "cricket": art_cricket, "ballot": art_ballot,
    "strike": art_strike, "pill": art_pill,
    "seoul": art_seoul, "hormuz": art_hormuz,
}

# ---------------------------------------------------------------- world map
# Coastlines plotted from real (lon, lat) coordinates on an equirectangular
# projection — simplified outlines, but true continent shapes and positions.
# Numbered pins mark the thirteen drawn stories; the three leads get a gold
# ring, as the caption's legend says. Positions are approximate.

def _proj(lon, lat):
    """Equirectangular projection onto the 340x168 map (lat range 85..-60)."""
    return (round((lon + 180) * 340 / 360, 1), round((85 - lat) * 168 / 145, 1))


# Continent outlines as (lon, lat) point lists, traced clockwise — simplified
# coastlines, but true shapes and positions on the projection above.
_LAND_LONLAT = [
    # North America
    [(-168, 66), (-140, 70), (-125, 72), (-110, 73), (-95, 80), (-88, 69),
     (-94, 58), (-86, 52), (-79, 55), (-72, 62), (-64, 60), (-56, 50),
     (-65, 44), (-70, 42), (-74, 39), (-76, 35), (-80, 32), (-80, 27),
     (-81, 25), (-83, 28), (-84, 30), (-89, 29), (-94, 30), (-97, 26),
     (-97, 22), (-94, 18), (-88, 21), (-87, 16), (-83, 15), (-83, 9),
     (-79, 9), (-86, 12), (-90, 14), (-95, 16), (-102, 18), (-105, 20),
     (-110, 23), (-114, 29), (-117, 33), (-122, 37), (-124, 40), (-124, 47),
     (-128, 52), (-133, 56), (-140, 60), (-152, 59), (-158, 58), (-165, 60)],
    # Baja California
    [(-110, 24), (-112, 29), (-115, 32), (-117, 33), (-114, 31), (-111, 27), (-109, 24)],
    # Greenland
    [(-46, 60), (-30, 68), (-22, 70), (-19, 76), (-28, 82), (-55, 76), (-56, 70), (-53, 64)],
    # South America
    [(-79, 9), (-72, 12), (-64, 11), (-55, 6), (-51, 4), (-50, 0), (-44, -3),
     (-35, -8), (-39, -13), (-40, -21), (-46, -24), (-52, -33), (-57, -38),
     (-62, -41), (-62, -45), (-65, -48), (-67, -52), (-68, -55), (-71, -54),
     (-73, -47), (-73, -40), (-72, -33), (-70, -25), (-70, -18), (-75, -15),
     (-79, -8), (-80, -4), (-77, 3), (-77, 7)],
    # Europe
    [(-9, 44), (-9, 37), (-2, 37), (3, 39), (3, 43), (7, 44), (10, 44),
     (12, 46), (14, 45), (18, 40), (16, 38), (15, 40), (12, 42), (19, 42),
     (23, 36), (26, 38), (28, 41), (28, 45), (32, 46), (38, 47), (48, 46),
     (50, 50), (48, 58), (44, 67), (35, 65), (31, 70), (25, 71), (18, 69),
     (21, 65), (18, 60), (17, 56), (12, 56), (10, 58), (8, 54), (5, 53),
     (2, 51), (-1, 51), (-2, 49), (-5, 48), (-2, 47), (-2, 44)],
    # Britain
    [(-5, 50), (-3, 53), (-4, 56), (-6, 58), (-8, 55), (-10, 52), (-6, 50)],
    # Iceland
    [(-22, 64), (-14, 64), (-14, 66), (-21, 66)],
    # Africa
    [(-6, 35), (3, 37), (10, 37), (11, 34), (20, 32), (27, 31), (32, 31),
     (34, 28), (35, 24), (38, 21), (39, 15), (43, 12), (48, 11), (51, 12),
     (51, 10), (48, 5), (42, -2), (40, -8), (39, -15), (37, -20), (35, -24),
     (33, -27), (29, -32), (25, -34), (19, -35), (17, -32), (15, -27),
     (13, -20), (12, -15), (13, -10), (10, -3), (9, 4), (4, 6), (-3, 5),
     (-8, 5), (-13, 8), (-17, 13), (-17, 16), (-16, 20), (-15, 25), (-13, 28), (-9, 31)],
    # Madagascar
    [(44, -13), (47, -13), (50, -16), (49, -20), (47, -24), (45, -25), (44, -20), (43, -17)],
    # Asia (incl. Arabia, India, Indochina, Siberia)
    [(28, 41), (33, 42), (36, 36), (35, 31), (34, 28), (39, 20), (43, 12),
     (45, 12), (52, 15), (55, 17), (59, 22), (58, 24), (55, 26), (50, 29),
     (48, 30), (54, 26), (57, 27), (61, 25), (66, 25), (68, 23), (72, 20),
     (72, 18), (76, 13), (77, 8), (80, 10), (80, 14), (84, 18), (88, 21),
     (91, 22), (92, 16), (94, 17), (97, 15), (98, 10), (100, 6), (103, 1),
     (100, 5), (98, 13), (100, 16), (103, 10), (107, 12), (109, 15),
     (106, 20), (110, 20), (114, 22), (118, 25), (120, 27), (122, 29),
     (121, 32), (120, 35), (122, 37), (119, 38), (122, 38), (126, 38),
     (129, 36), (129, 39), (126, 41), (130, 42), (133, 43), (137, 45),
     (140, 47), (141, 50), (142, 53), (156, 52), (159, 56), (162, 60),
     (169, 60), (178, 65), (178, 68), (170, 70), (155, 71), (140, 72),
     (125, 73), (110, 74), (95, 76), (85, 75), (75, 72), (68, 70), (60, 69),
     (50, 68), (44, 67), (36, 65), (33, 60), (32, 55), (33, 50), (30, 46)],
    # Japan
    [(130, 31), (132, 33), (135, 34), (138, 35), (140, 36), (141, 39),
     (141, 42), (142, 44), (145, 44), (143, 42), (139, 37), (136, 34), (133, 33), (131, 32)],
    # Sumatra
    [(95, 5), (99, 2), (103, -2), (106, -6), (104, -5), (100, 0), (96, 4)],
    # Java
    [(105, -6), (110, -6), (114, -8), (114, -9), (106, -7)],
    # Borneo
    [(109, 1), (113, 3), (117, 5), (119, 2), (118, -2), (116, -4), (112, -3), (110, -1)],
    # New Guinea
    [(131, -1), (136, -2), (141, -3), (145, -5), (147, -8), (146, -9), (141, -8), (136, -4), (132, -3)],
    # Australia
    [(114, -22), (113, -26), (115, -32), (118, -35), (124, -33), (129, -32),
     (132, -32), (135, -35), (137, -35), (139, -37), (140, -39), (144, -38),
     (147, -38), (150, -37), (153, -32), (153, -27), (151, -24), (149, -20),
     (146, -19), (143, -15), (142, -11), (141, -13), (141, -17), (139, -18),
     (136, -15), (135, -12), (132, -11), (130, -12), (126, -14), (122, -17), (118, -20)],
    # New Zealand, North Island
    [(173, -35), (176, -37), (178, -38), (176, -40), (174, -42), (173, -39), (172, -37)],
    # New Zealand, South Island
    [(167, -46), (169, -44), (172, -42), (173, -42), (171, -44), (168, -47)],
]

PINS_LONLAT = {  # V7 story number -> (lon, lat); pins 6 and 12 nudged into the sea
    1: (30.5, 50.4), 2: (84.9, 19.3), 3: (139.7, 35.7), 4: (4.4, 50.9),
    5: (30.7, 36.9), 6: (150.0, 26.0), 7: (114.5, 40.5), 8: (171.0, -41.3),
    9: (-89.2, 13.7), 10: (12.5, 41.9), 11: (0.8, 40.5), 12: (125.5, 40.5),
    13: (56.3, 26.3),
}
PINS = {n: _proj(lon, lat) for n, (lon, lat) in PINS_LONLAT.items()}


def world_map():
    land = "#d9c491"
    parts = ['<svg viewBox="0 0 340 168" xmlns="http://www.w3.org/2000/svg">',
             '<rect width="340" height="168" fill="#22354f"/>']
    for blob in _LAND_LONLAT:
        pts = " L".join(f"{x} {y}" for x, y in (_proj(lon, lat) for lon, lat in blob))
        parts.append(f'<path d="M{pts} Z" fill="{land}"/>')
    # features first, leads last, so the gold-ringed lead pins sit on top in clusters
    for n in sorted(PINS, key=lambda k: (k <= 3, k)):
        x, y = PINS[n]
        if n <= 3:  # the three leads get a gold ring, as the caption's legend says
            parts.append(f'<circle cx="{x}" cy="{y}" r="9.2" fill="#b02a24" stroke="#ffd76a" stroke-width="2.4"/>')
        else:
            parts.append(f'<circle cx="{x}" cy="{y}" r="7.6" fill="#b02a24" stroke="#f6efdb" stroke-width="1.4"/>')
        parts.append(f'<text x="{x}" y="{y + 2.8}" text-anchor="middle" font-family="Arial" '
                     f'font-size="8.6" font-weight="bold" fill="#fff">{n}</text>')
    parts.append('</svg>')
    return "".join(parts)

# ---------------------------------------------------------------- assembly

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1024px; height:1024px; overflow:hidden; background:#f6efdb; color:#17263f;
  font-family:'Liberation Sans', Arial, sans-serif; padding:7px 16px 8px; }
.kicker { display:flex; justify-content:space-between; font-size:11px; font-weight:bold;
  letter-spacing:2.2px; color:#7a1d18; }
.kicker .r { color:#17263f; }
h1.mast { font-family:Georgia,'Liberation Serif',serif; font-size:47px; text-align:center;
  letter-spacing:.2px; line-height:1.02; margin-top:1px; }
.strap { text-align:center; font-family:Georgia,'Liberation Serif',serif; font-style:italic;
  font-size:15px; color:#b02a24; border-bottom:3px double #17263f; padding-bottom:3px; }
.nums { display:flex; border-bottom:1.6px solid #17263f; }
.nums div { flex:1; text-align:center; padding:2px 4px 3px; border-right:1px solid #c9bd97; }
.nums div:last-child { border-right:none; }
.nums b { font-family:Georgia,'Liberation Serif',serif; font-size:19px; color:#b02a24; display:block; }
.nums span { font-size:9.4px; line-height:1.12; display:block; color:#3c4657; }
.regions { display:flex; gap:4px; margin:3px 0 4px; align-items:center; }
.regions .lab { font-size:9.2px; font-weight:bold; letter-spacing:.8px; color:#5c5540; margin-right:1px; }
.regions .chip { color:#fff; font-size:10.2px; font-weight:bold; letter-spacing:.5px; padding:2px 7px; white-space:nowrap; }
.regions .when { margin-left:auto; font-size:9.2px; color:#5c5540; letter-spacing:.4px; white-space:nowrap; }
.row { display:flex; gap:8px; }
.card { border:1.4px solid #17263f; background:#fdfaf0; overflow:hidden; }
.card .art svg { display:block; width:100%; }
.artwrap { position:relative; }
.tagpill { position:absolute; top:5px; right:5px; background:rgba(23,38,63,.93); color:#f6efdb;
  font-size:8.8px; font-weight:bold; letter-spacing:1.1px; padding:2.5px 7px;
  border:1px solid rgba(246,239,219,.45); border-radius:2px; }
.feat .ftag { font-size:7.8px; font-weight:bold; letter-spacing:1px; color:#7a1d18; margin-top:1px; }
.lead .art svg { height:92px; }
.feat .art svg { height:30px; }
.lead { flex:1; }
.lead .txt { padding:5px 9px 6px; }
.kick { font-size:9.8px; font-weight:bold; letter-spacing:1px; color:#17616b; }
.lead h2 { font-family:Georgia,'Liberation Serif',serif; font-size:18.5px; line-height:1.1; margin:2px 0 3px; }
.lead p { font-size:11.5px; line-height:1.2; color:#2c3648; }
.feat { flex:1; }
.feat .txt { padding:3px 7px 4px; }
.feat h3 { font-family:Georgia,'Liberation Serif',serif; font-size:14px; line-height:1.12; margin:1px 0 2px; }
.feat p { font-size:10.3px; line-height:1.2; color:#2c3648; }
.num { color:#b02a24; }
.bottom { display:flex; gap:8px; margin-top:4px; }
.mapbox { width:300px; border:1.4px solid #17263f; background:#22354f; }
.mapbox svg { height:168px; width:100%; display:block; }
.mapbox .cap { color:#e8e2cc; font-size:9.2px; padding:3px 8px 4px; letter-spacing:.7px; }
.mapbox .cap b { color:#fff; letter-spacing:1.2px; }
.briefs { flex:1; border-top:2px solid #b02a24; padding-top:4px; }
.briefs h4 { font-size:12px; letter-spacing:1.1px; color:#7a1d18; margin-bottom:3px; }
.briefs .cols { display:flex; gap:14px; }
.briefs ul { list-style:none; flex:1; }
.briefs li { font-size:10px; line-height:1.10; margin-bottom:1px; color:#2c3648; }
.briefs li b { color:#17263f; }
.briefs li .n { color:#b02a24; font-weight:bold; }
.datecheck { margin-top:3px; border:1.6px solid #b02a24; padding:3px 9px; font-size:10.3px;
  line-height:1.32; color:#4a2320; background:#fbf3e4; }
.datecheck b { color:#b02a24; letter-spacing:1px; }
.foot { margin-top:3px; font-size:9.2px; color:#5c5540; }
"""

def card_lead(s):
    pill = f'<span class="tagpill">{s["tag"]}</span>' if s.get("tag") else ''
    return (f'<div class="card lead"><div class="artwrap"><div class="art">{ART[s["art"]]()}</div>'
            f'{pill}</div>'
            f'<div class="txt"><div class="kick"><span class="num">{s["n"]:02d}</span> · {s["kicker"]}</div>'
            f'<h2>{s["headline"]}</h2><p>{s["body"]}</p></div></div>')

def card_feat(s):
    return (f'<div class="card feat"><div class="art">{ART[s["art"]]()}</div>'
            f'<div class="txt"><div class="kick"><span class="num">{s["n"]:02d}</span> · {s["kicker"]}</div>'
            f'<div class="ftag">{s["tag"]}</div>'
            f'<h3>{s["headline"]}</h3><p>{s["body"]}</p></div></div>')

def build_html():
    counts = {}
    for s in LEADS + FEATURES:
        counts[s["region"]] = counts.get(s["region"], 0) + 1
    for (_n, r, _place, _text) in BRIEFS:
        counts[r] = counts.get(r, 0) + 1
    total = sum(counts.values())
    chips = "".join(
        f'<span class="chip" style="background:{REGION_COLORS[k]}">{name} {counts.get(k, 0)}</span>'
        for k, name in REGION_NAMES)
    nums = "".join(f"<div><b>{v}</b><span>{t}</span></div>" for v, t in NUMBERS)
    half = (len(BRIEFS) + 1) // 2
    def brief_li(b):
        n, _r, place, text = b
        return f'<li><span class="n">{n}</span> <b>{place}</b> — {text}</li>'
    col1 = "".join(brief_li(b) for b in BRIEFS[:half])
    col2 = "".join(brief_li(b) for b in BRIEFS[half:])
    leads = "".join(card_lead(s) for s in LEADS)
    feats1 = "".join(card_feat(s) for s in FEATURES[:5])
    feats2 = "".join(card_feat(s) for s in FEATURES[5:])
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>Friday 20 November 2026 — the world in one page</title>
<style>{CSS}</style></head>
<body>
<div class="kicker"><span>THE WORLD IN ONE DAY</span><span class="r">FRIDAY'S NEWS · ONE PAGE · {total} STORIES · 6 CONTINENTS</span></div>
<h1 class="mast">Friday 20 November 2026</h1>
<div class="strap">Missiles hit Kyiv's bridges · Cyclone Akvan ashore in India · An AI sell-off sinks Asia's markets · First EU–UK reset summit</div>
<div class="nums">{nums}</div>
<div class="regions"><span class="lab">STORIES BY REGION</span>{chips}<span class="when">ALL STORIES: FRI 20 NOV 2026, ANY TIME ZONE</span></div>
<div class="row">{leads}</div>
<div class="row" style="margin-top:4px">{feats1}</div>

<div class="row" style="margin-top:4px">{feats2}</div>
<div class="bottom">
  <div class="mapbox">{world_map()}<div class="cap"><b>WHERE IT HAPPENED</b> · PINS 1–3 LEADS (GOLD RING) · 4–13 FEATURES · POSITIONS APPROXIMATE</div></div>
  <div class="briefs"><h4>ALSO ON FRIDAY 20 NOVEMBER — {len(BRIEFS)} MORE STORIES</h4>
  <div class="cols"><ul>{col1}</ul><ul>{col2}</ul></div></div>
</div>
<div class="datecheck"><b>DATE CHECK</b> · {DATE_CHECK}</div>
<div class="foot"><span>{FOOTER}</span></div>
</body></html>"""

def main():
    import pathlib
    out = pathlib.Path(__file__).with_name("poster.html")
    out.write_text(build_html(), encoding="utf-8")
    print("wrote", out, len(out.read_bytes()), "bytes")

if __name__ == "__main__":
    main()
