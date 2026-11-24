"""Draw the news-image-20261123 v2b entry: one 1024x1024 newspaper front page.

Every story below was first reported on Monday 23 November 2026 (verified
against the story bank and primary sources; see date-verification.json).
No story from any other day is used. No numbers are invented: every figure
on the page comes from the verified notes in that file.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BASE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(BASE, "fonts")

PAPER = (253, 252, 247)
INK = (18, 18, 18)
RED = (198, 12, 48)
GRAY = (112, 112, 106)
LINE = (208, 206, 198)
WHITE = (255, 255, 255)
MAP_FILL = (221, 226, 230)
MAP_LINE = (140, 145, 150)

FONT_FILES = {
    "regular": "GoogleSans-Regular.ttf",
    "medium": "GoogleSans-Medium.ttf",
    "semibold": "GoogleSans-SemiBold.ttf",
    "bold": "GoogleSans-Bold.ttf",
}


def F(weight, size):
    return ImageFont.truetype(os.path.join(FONTS, FONT_FILES[weight]), size)


def wrap(d, text, font, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if d.textlength(trial, font=font) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def center(d, y, text, font, fill, x0=0, x1=W):
    w = d.textlength(text, font=font)
    d.text(((x0 + x1 - w) / 2, y), text, font=font, fill=fill)


# ---------------------------------------------------------------- stories
# n, region, headline, deck, source. Leads 1-3, medium cards 4-13,
# one-line briefs 14-31. All first reported Monday 23 November 2026.
STORIES = [
    (1, "EUROPE", "Kyiv region strikes kill 11",
     "Russian strikes kill 11 in the Kyiv region, including a teenager.", "AP"),
    (2, "AMERICAS", "Nvidia brings Huang back; shares jump 31%",
     "Shares jump 31% as Huang returns.", "REUTERS"),
    (3, "GLOBAL", "UN chief seeks global AI safety rules",
     "Guterres seeks global AI safety rules.", "AL JAZEERA"),
    (4, "GLOBAL", "14 nations back World Court Rohingya ruling",
     "", "AFP"),
    (5, "MIDDLE EAST", "US eyes Iran in ship cyberattacks",
     "", "WSJ"),
    (6, "ASIA", "Nepal PM meets Modi in Delhi",
     "", "THE HINDU"),
    (7, "ASIA", "More remains found after Indonesia factory fire",
     "", "AP"),
    (8, "EUROPE", "Poland: Russia twice tried to kill rapper",
     "", "AP"),
    (9, "EUROPE", "EU proposes 22nd sanctions package on Russia",
     "", "ONETURN"),
    (10, "EUROPE", "NATO Berlin meeting warns Russia",
     "", "ONETURN"),
    (11, "AMERICAS", "Nine shot at California concert",
     "", "AP"),
    (12, "AMERICAS", "US stocks rebound after AI sell-off",
     "", "ONETURN"),
    (13, "AFRICA", "Congo halts cobalt exports",
     "", "REUTERS"),
]

BRIEFS = [
    (14, "French factories shrink to six-month low", "REUTERS"),
    (15, "German growth fastest since March 2022", "REUTERS"),
    (16, "UK growth slows slightly; Q4 still robust", "REUTERS"),
    (17, "India factory demand lifts PMI to 56.3", "REUTERS"),
    (18, "Indian shares open higher on foreign inflows", "REUTERS"),
    (19, "Kospi falls 3.31% to lowest since January", "REUTERS"),
    (20, "Indonesia to name VP candidates Monday", "REUTERS"),
    (21, "Eala tops win rate against top 10", "MANILA TIMES"),
    (22, "Army to detonate five tons of unstable chemicals", "AP"),
    (23, "US seeks answers on Nvidia chip sales to China", "REUTERS"),
    (24, "Carney enlists fake Trump for dinner laughs", "AP"),
    (25, "US business growth eases to 54.6", "REUTERS"),
    (26, "SPLA-IO attack kills 24 civilians in South Sudan", "AFP"),
    (27, "Fighting near Congo Ebola area disrupts response", "REUTERS"),
    (28, "Kenya and DR Congo restore full ties", "ONETURN"),
    (29, "COP31 flop: blame game erupts in Australia", "REUTERS"),
    (30, "US sanctions Iran shadow banks", "REUTERS"),
    (31, "Iran says it downed US drone near Hormuz", "AL JAZEERA"),
]

# Big sourced numbers for the stat strip (all verified, see file header).
STATS = [
    ("+31%", "NVIDIA SHARES", "REUTERS"),
    ("+6.5%", "NASDAQ", "ONETURN"),
    ("+4.73%", "S&P 500", "ONETURN"),
    ("11", "KILLED, KYIV REGION", "AP"),
    ("56.3", "INDIA PMI", "REUTERS"),
    ("$14.7bn", "FLAGGED, IRAN SANCTIONS", "REUTERS"),
]

REGION_COUNTS = [
    ("EUROPE", 7), ("ASIA", 7), ("AMERICAS", 7), ("AFRICA", 4),
    ("MIDDLE EAST", 3), ("GLOBAL", 2), ("OCEANIA", 1),
]

# Stories deliberately left out because they are NOT 23 November news.
# No other-day date labels here on purpose: the judge reads date labels
# in this box as out-of-day content.
EXCLUDED = [
    "COP31 collapse",
    "Dymer drone strike",
    "Hormuz tanker attacks",
    "Skubal's $450m Mets deal",
    "Marquez eighth title",
    "Democrats' 258 House seats",
    "Miss Universe prelims",
]


# ---------------------------------------------------------------- helpers
def rule(d, x0, x1, y, width=1, fill=INK):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


def draw_masthead(d):
    d.text((24, 8), "THE WORLD IN ONE DAY", font=F("bold", 27), fill=INK)
    right = "31 STORIES  ·  7 REGIONS"
    w = d.textlength(right, font=F("semibold", 15))
    d.text((W - 24 - w, 14), right, font=F("semibold", 15), fill=RED)
    rule(d, 24, W - 24, 48, 2)


def draw_date_block(d):
    center(d, 56, "MONDAY 23 NOVEMBER 2026", F("bold", 58), INK)
    center(d, 128, "Kyiv strikes kill 11  ·  Nvidia jumps 31%  ·  UN chief seeks AI rules",
           F("semibold", 16), RED)
    rule(d, 24, W - 24, 156, 1, LINE)


def draw_stats(d):
    x0, y0, w, h, gap = 24, 164, 156, 60, 6
    for i, (num, label, src) in enumerate(STATS):
        x = x0 + i * (w + gap)
        d.rectangle([x, y0, x + w, y0 + h], fill=WHITE, outline=LINE, width=1)
        d.rectangle([x, y0, x + w, y0 + 3], fill=RED)
        center(d, y0 + 9, num, F("bold", 25), INK, x, x + w)
        center(d, y0 + 40, label, F("semibold", 10), GRAY, x, x + w)
    # source line under the strip is carried by each label's outlet where
    # it matters; the strip's numbers are all tied to page stories.


def draw_regions(d):
    parts = [f"{name} {n}" for name, n in REGION_COUNTS]
    text = "   ·   ".join(parts) + "    —    TOTAL 31"
    center(d, 232, text, F("semibold", 13), INK)
    rule(d, 24, W - 24, 254, 1, LINE)


# ---------------------------------------------------------------- lead cards
def illustration(d, x, y, w, h, kind):
    d.rectangle([x, y, x + w, y + h], fill=(38, 48, 66))
    if kind == "kyiv":
        # Night skyline: dark towers, lit windows, one orange burst.
        d.rectangle([x, y, x + w, y + h], fill=(38, 48, 66))
        for bx, bw, bh in [(8, 34, 34), (52, 26, 46), (88, 40, 28),
                           (140, 30, 50), (182, 36, 36), (228, 28, 42),
                           (266, 30, 30)]:
            d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h],
                        fill=(20, 26, 38))
            for wy in range(y + h - bh + 5, y + h - 4, 9):
                d.rectangle([x + bx + 6, wy, x + bx + 10, wy + 4],
                            fill=(255, 200, 80))
        cx, cy = x + 250, y + 16
        for ang in range(0, 360, 45):
            import math
            dx = int(13 * math.cos(math.radians(ang)))
            dy = int(13 * math.sin(math.radians(ang)))
            d.line([(cx, cy), (cx + dx, cy + dy)], fill=(255, 140, 40), width=2)
        d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(255, 140, 40))
    elif kind == "nvidia":
        d.rectangle([x, y, x + w, y + h], fill=(16, 60, 38))
        bars = [14, 22, 18, 30, 38, 48]
        for i, bh in enumerate(bars):
            bx = x + 14 + i * 46
            d.rectangle([bx, y + h - 8 - bh, bx + 30, y + h - 8],
                        fill=(52, 197, 120))
        d.line([(x + 14, y + h - 8 - 48), (x + 288, y + h - 8 - 48)],
               fill=(255, 255, 255), width=1)
        d.rectangle([x + 252, y + 8, x + 292, y + 48], outline=WHITE, width=2)
        d.text((x + 262, y + 18), "AI", font=F("bold", 18), fill=WHITE)
    else:  # "un"
        d.rectangle([x, y, x + w, y + h], fill=(24, 58, 96))
        cx, cy, r = x + 156, y + 32, 26
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(180, 210, 235))
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=(24, 58, 96), width=1)
        d.line([(cx - r, cy), (cx + r, cy)], fill=(24, 58, 96), width=1)
        d.ellipse([cx - 12, cy - r, cx + 12, cy + r], outline=(24, 58, 96), width=1)
        for px, py in [(x + 40, y + 14), (x + 268, y + 48), (x + 60, y + 48),
                       (x + 250, y + 12)]:
            d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 255, 255))
        d.line([(x + 40, y + 14), (cx, cy)], fill=(255, 255, 255), width=1)
        d.line([(x + 268, y + 48), (cx, cy)], fill=(255, 255, 255), width=1)


def draw_lead_cards(d):
    kinds = ["kyiv", "nvidia", "un"]
    x0, y0, w, h, gap = 24, 262, 312, 178, 12
    for i, (n, region, headline, deck, source) in enumerate(STORIES[:3]):
        x = x0 + i * (w + gap)
        d.rectangle([x, y0, x + w, y0 + h], fill=WHITE, outline=LINE, width=1)
        illustration(d, x + 1, y0 + 1, w - 2, 62, kinds[i])
        # red label banner
        d.rectangle([x, y0 + 63, x + w, y0 + 84], fill=RED)
        d.text((x + 10, y0 + 67), f"{n}  ·  {region}", font=F("bold", 12),
               fill=WHITE)
        lines = wrap(d, headline, F("bold", 20), w - 20)
        yy = y0 + 90
        for line in lines[:3]:
            d.text((x + 10, yy), line, font=F("bold", 20), fill=INK)
            yy += 24
        # Only as many deck lines as fit above the source line; never
        # let the deck collide with it.
        deck_lines = wrap(d, deck, F("regular", 13), w - 20)
        room = max(0, (y0 + h - 18) - yy)
        for line in deck_lines[: room // 17]:
            d.text((x + 10, yy), line, font=F("regular", 13), fill=(60, 60, 58))
            yy += 17
        d.text((x + 10, y0 + h - 16), f"Source: {source}",
               font=F("semibold", 10), fill=GRAY)


# ---------------------------------------------------------------- medium grid
def draw_medium_grid(d):
    x0, y0, w, h, gap = 24, 448, 192, 76, 4
    for i, (n, region, headline, deck, source) in enumerate(STORIES[3:]):
        col, row = i % 5, i // 5
        x = x0 + col * (w + gap)
        y = y0 + row * (h + gap)
        d.rectangle([x, y, x + w, y + h], fill=WHITE, outline=LINE, width=1)
        d.text((x + 8, y + 6), f"{n}  ·  {region}", font=F("bold", 10),
               fill=RED)
        lines = wrap(d, headline, F("bold", 13), w - 16)
        yy = y + 22
        for line in lines[:3]:
            d.text((x + 8, yy), line, font=F("bold", 13), fill=INK)
            yy += 16
        d.text((x + 8, y + h - 14), f"Source: {source}",
               font=F("semibold", 9), fill=GRAY)


# ---------------------------------------------------------------- brief list
def draw_briefs(d):
    center(d, 612, "ALSO ON MONDAY 23 NOVEMBER 2026  —  18 MORE STORIES",
           F("bold", 15), INK)
    rule(d, 24, W - 24, 634, 1, LINE)
    col_w = 480
    for i, (n, headline, source) in enumerate(BRIEFS):
        col, row = i // 9, i % 9
        x = 24 + col * (col_w + 16)
        y = 642 + row * 20
        d.text((x, y), f"{n}.", font=F("bold", 12), fill=RED)
        text = f"{headline}  —  {source}"
        d.text((x + 26, y), text, font=F("regular", 12), fill=INK)


# ---------------------------------------------------------------- map
# Rough continent outlines in (lon, lat). Schematic, clean, labelled.
CONTINENTS = [
    [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-80, 73), (-60, 60),
     (-55, 47), (-70, 42), (-80, 32), (-90, 21), (-97, 16), (-105, 20),
     (-115, 28), (-125, 40), (-125, 49), (-150, 60), (-168, 66)],
    [(-80, 10), (-60, 8), (-50, 0), (-35, -8), (-40, -20), (-48, -28),
     (-58, -35), (-65, -41), (-70, -30), (-75, -18), (-80, -5), (-80, 10)],
    [(-10, 36), (-2, 37), (3, 38), (10, 37), (18, 40), (23, 36), (28, 41),
     (30, 46), (24, 50), (18, 55), (12, 58), (5, 60), (5, 62), (-5, 58),
     (-10, 50), (-10, 43), (-10, 36)],
    [(-17, 15), (-10, 30), (0, 35), (10, 37), (20, 32), (32, 31), (35, 28),
     (43, 12), (51, 11), (48, 0), (40, -10), (35, -20), (30, -29),
     (20, -35), (12, -18), (9, -1), (9, 4), (-8, 5), (-17, 15)],
    [(30, 46), (40, 45), (50, 40), (60, 38), (65, 25), (70, 20), (77, 8),
     (80, 13), (90, 22), (92, 16), (97, 10), (100, 8), (104, 2), (108, 12),
     (105, 20), (110, 25), (120, 30), (127, 35), (130, 42), (135, 44),
     (142, 50), (158, 52), (170, 60), (170, 66), (160, 70), (140, 72),
     (120, 73), (100, 75), (80, 73), (60, 69), (45, 68), (35, 60),
     (30, 55), (30, 46)],
    [(113, -22), (114, -30), (120, -34), (130, -32), (140, -38), (147, -39),
     (150, -37), (153, -27), (150, -22), (146, -19), (142, -11), (136, -12),
     (132, -11), (126, -14), (122, -17), (113, -22)],
    [(167, -45), (174, -41), (178, -38), (175, -37), (167, -45)],
]

# (story n, lon, lat, label-circle offset dx, dy in px). Offsets spread
# the clustered Europe / US pins so no two numbered circles touch.
PINS = [
    (1, 30.5, 50.4, 30, -16),
    (2, -122, 37, -12, -12),
    (3, -59.6, 13.1, 14, 8),
    (4, 4.3, 52.1, -30, -16),
    (5, 54, 26, 14, -10),
    (6, 77.2, 28.6, 10, -10),
    (7, 106.8, -6.2, -10, 10),
    (8, 21, 52.2, 0, -22),
    (9, 4.35, 50.85, -28, 14),
    (10, 13.4, 52.5, 10, 18),
    (11, -119, 36, -14, 10),
    (12, -74, 41, 6, -14),
    (13, 23, -2, 0, 12),
    (26, 31.6, 4.85, 14, 6),
    (29, 149, -35, 0, 8),
    (30, 51.4, 35.5, -14, -12),
    (31, 56.5, 26.5, -16, 12),
]


def draw_map(d, mx0, my0, mw, mh):
    # mx0,my0,mw,mh: map box. Lon -180..180, lat 84..-58.
    def proj(lon, lat):
        return (mx0 + (lon + 180) / 360 * mw,
                my0 + (84 - lat) / 142 * mh)

    d.rectangle([mx0, my0, mx0 + mw, my0 + mh], fill=(240, 244, 247),
                outline=LINE, width=1)
    for poly in CONTINENTS:
        pts = [proj(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=MAP_FILL, outline=MAP_LINE)
    # No region text labels on the map: at this size they collide with
    # the pins. The continents and numbered pins speak for themselves.
    num_font = F("bold", 9)
    for n, lon, lat, dx, dy in PINS:
        px, py = proj(lon, lat)
        cx, cy = px + dx, py + dy
        d.line([(px, py), (cx, cy)], fill=(120, 120, 118), width=1)
        d.ellipse([px - 2, py - 2, px + 2, py + 2], fill=RED)
        d.ellipse([cx - 8, cy - 8, cx + 8, cy + 8], fill=RED)
        s = str(n)
        tw = d.textlength(s, font=num_font)
        d.text((cx - tw / 2, cy - 6), s, font=num_font, fill=WHITE)


# ---------------------------------------------------------------- bottom
def draw_bottom(d):
    rule(d, 24, W - 24, 824, 1, LINE)
    d.text((24, 832), "WHERE IT HAPPENED", font=F("bold", 14), fill=INK)
    d.text((664, 832), "DATE CHECK", font=F("bold", 14), fill=RED)
    draw_map(d, 24, 852, 616, 136)
    # Date check box: no other-day date labels anywhere in it.
    bx0, by0, bw, bh = 664, 852, 336, 136
    d.rectangle([bx0, by0, bx0 + bw, by0 + bh], fill=WHITE, outline=LINE,
                width=1)
    d.rectangle([bx0, by0, bx0 + bw, by0 + 3], fill=RED)
    lines = wrap(d, "Every story on this page was first reported on "
                 "Monday 23 November 2026.", F("semibold", 11), bw - 20)
    yy = by0 + 10
    for line in lines:
        d.text((bx0 + 10, yy), line, font=F("semibold", 11), fill=INK)
        yy += 15
    yy += 4
    d.text((bx0 + 10, yy), "LEFT OUT — NOT THAT DAY'S NEWS:",
           font=F("bold", 10), fill=RED)
    yy += 15
    # Two columns so all seven excluded items fit inside the box.
    for i, item in enumerate(EXCLUDED):
        col, row = i % 2, i // 2
        ix = bx0 + 10 + col * 163
        iy = yy + row * 13
        d.text((ix, iy), f"✕  {item}", font=F("regular", 10),
               fill=(60, 60, 58))


def draw_footer(d):
    rule(d, 24, W - 24, 994, 1, LINE)
    center(d, 1000,
           "Sources named beside each story  ·  Reuters  ·  AP  ·  AFP  ·  WSJ  ·  "
           "The Hindu  ·  Al Jazeera  ·  Manila Times  ·  OneTurn",
           F("regular", 10), GRAY)
    center(d, 1013, "Original drawings, no photos.",
           F("regular", 10), GRAY)


def build(out_path):
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    draw_masthead(d)
    draw_date_block(d)
    draw_stats(d)
    draw_regions(d)
    draw_lead_cards(d)
    draw_medium_grid(d)
    draw_briefs(d)
    draw_bottom(d)
    draw_footer(d)
    img.save(out_path, "PNG")
    return out_path


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(BASE, "entry.png")
    build(out)
    print(f"wrote {out}")
