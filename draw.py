"""news-23 b50 front-page-dense: draw THE WORLD TODAY, Monday 23 November 2026.
31 stories, 1024x1024, PIL. Written fresh for this entry.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FD = "/usr/share/fonts/truetype/dejavu/"

def F(name, size):
    return ImageFont.truetype(FD + name, size)

SERIFB = "DejaVuSerif-Bold.ttf"
SANSB = "DejaVuSans-Bold.ttf"
SANS = "DejaVuSans.ttf"

BLACK = (10, 10, 10)
WHITE = (255, 255, 255)
GOLD = (212, 175, 55)
RED = (178, 34, 34)
DARKRED = (139, 0, 0)
NAVY = (13, 27, 62)
TEAL = (0, 128, 128)
CREAM = (250, 243, 224)
GRAY = (90, 90, 90)
LGRAY = (230, 230, 230)

img = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(img)


def wrap(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit(text, path, start, min_size, max_w):
    for s in range(start, min_size - 1, -1):
        f = F(path, s)
        if d.textlength(text, font=f) <= max_w:
            return f
    return F(path, min_size)


def chip(x, y, label, color):
    f = F(SANSB, 9)
    tw = d.textlength(label, font=f)
    w = int(tw) + 10
    d.rounded_rectangle([x, y, x + w, y + 14], radius=2, fill=color)
    d.text((x + 5, y + 2), label, font=f, fill=WHITE)
    return w


# ---------- masthead ----------
d.rectangle([0, 0, W, 52], fill=BLACK)
d.text((10, 6), "THE WORLD TODAY", font=F(SERIFB, 38), fill=WHITE)
d.text((W - 10 - d.textlength("MONDAY 23 NOVEMBER 2026", font=F(SANSB, 21)), 14),
       "MONDAY 23 NOVEMBER 2026", font=F(SANSB, 21), fill=GOLD)

# ---------- kicker ----------
d.text((10, 56), "AI rout hits Asia  \u00b7  UN chief urges AI rules  \u00b7  "
       "US lead over China at record low  \u00b7  Anthropic IPO $107.3B",
       font=F(SANSB, 13), fill=RED)

# ---------- number strip (2 rows x 5 cols) ----------
nums = [
    ("-3.3%", "KOSPI", RED), ("5.3", "US-CHINA POWER GAP", (0, 90, 160)),
    ("11,762", "EBOLA CASES, DRC", (0, 120, 60)), ("10T won", "SEOUL STABILISATION FUND", (150, 100, 0)),
    ("2%", "BILLIONAIRE TAX IN PARIS", (110, 40, 140)),
    ("$450M", "SKUBAL DEAL", (130, 0, 130)), ("165", "RUSSIAN MISSILES IN A WEEK", RED),
    ("12,000", "CLEARED IN MANCHESTER", (0, 90, 160)), ("264 kg", "EXPLOSIVES SEIZED IN LEBANON", (150, 100, 0)),
    ("$107.3B", "ANTHROPIC IPO \u2014 LARGEST", (110, 40, 140)),
]
col_w = 202
for i, (num, lab, col) in enumerate(nums):
    r, c = divmod(i, 5)
    x = 8 + c * col_w
    y = 72 + r * 25
    f = fit(num, SANSB, 18, 14, col_w - 6)
    d.text((x, y), num, font=f, fill=col)
    lf = fit(lab, SANSB, 8, 7, col_w - 6)
    d.text((x, y + 18), lab, font=lf, fill=BLACK)

# ---------- region bar ----------
regions = [("ASIA-PACIFIC 7", 7, (0, 128, 128)), ("AMERICAS 8", 8, NAVY),
           ("MIDDLE EAST 6", 6, (180, 130, 30)), ("EUROPE 5", 5, (110, 40, 140)),
           ("AFRICA 3", 3, (139, 0, 0)), ("WORLD 2", 2, (90, 90, 90))]
x = 4
for name, n, col in regions:
    w = int((W - 8) * n / 31)
    d.rectangle([x, 128, x + w, 148], fill=col)
    d.text((x + 4, 133), name, font=F(SANSB, 10), fill=WHITE)
    x += w

# ---------- UTC strip ----------
d.rectangle([0, 150, W, 166], fill=NAVY)
d.text((8, 153), "THE DAY IN UTC   ~00:00 Kospi dives   ~06:30 Guterres opens   "
       "~09:00 Power Index   ~12:00 Paris 2% tax   ~15:00 Kyiv missiles   ~18:00 IPO $97.17",
       font=F(SANS, 10), fill=WHITE)
d.text((W - 8 - d.textlength("~ APPROX", font=F(SANS, 10)), 153), "~ APPROX",
       font=F(SANS, 10), fill=(200, 200, 200))

# ---------- hero scenes ----------
SX = [4, 346, 688]
SW = 332
SY, SH = 168, 158
CAP = 20  # caption strip height at scene bottom

# scene 1: Kospi chart + skyline
x0 = SX[0]
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=NAVY)
d.text((x0 + 8, SY + 4), "-3.3%", font=F(SANSB, 30), fill=(255, 80, 60))
pts = [(x0 + 12 + i * 32, SY + 58 - v) for i, v in enumerate([4, 18, 8, 26, 14, 30, 20, 34, 24, 40])]
d.line(pts, fill=(255, 120, 90), width=2)
for px, py in pts:
    d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 200, 90))
import random
random.seed(23)
for i in range(14):
    bx = x0 + 8 + i * 23
    bh = random.randint(18, 46)
    by = SY + SH - CAP - bh
    d.rectangle([bx, by, bx + 16, SY + SH - CAP], fill=(20, 40, 90))
    for wy in range(by + 4, SY + SH - CAP - 3, 8):
        for wx in range(bx + 3, bx + 14, 6):
            d.rectangle([wx, wy, wx + 3, wy + 4], fill=(255, 220, 100))
d.rectangle([x0, SY + SH - CAP, x0 + SW, SY + SH], fill=BLACK)
d.text((x0 + 8, SY + SH - CAP + 4), "KOSPI 4,708.54   \u00b7   -161 PTS",
       font=F(SANSB, 11), fill=WHITE)

# scene 2: Guterres
x0 = SX[1]
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=TEAL)
d.text((x0 + 10, SY + 8), "150 DELEGATES", font=F(SANSB, 30), fill=GOLD)
d.text((x0 + 10, SY + 44), "BACK A RISK", font=F(SANSB, 30), fill=WHITE)
d.text((x0 + 10, SY + 78), "FRAMEWORK", font=F(SANSB, 30), fill=WHITE)
# globe bottom-right
gx, gy, gr = x0 + SW - 52, SY + SH - CAP - 34, 26
d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=(200, 240, 235), width=2)
d.ellipse([gx - gr // 2, gy - gr, gx + gr // 2, gy + gr], outline=(200, 240, 235), width=1)
d.line([gx - gr, gy, gx + gr, gy], fill=(200, 240, 235), width=1)
d.rectangle([x0, SY + SH - CAP, x0 + SW, SY + SH], fill=BLACK)
d.text((x0 + 8, SY + SH - CAP + 4), "UN  \u00b7  BRIDGETOWN", font=F(SANSB, 11), fill=WHITE)

# scene 3: Asia Power Index bars
x0 = SX[2]
d.rectangle([x0, SY, x0 + SW, SY + SH], fill=CREAM)
d.text((x0 + 8, SY + 4), "NARROWEST SINCE 2018", font=F(SANSB, 11), fill=BLACK)
d.text((x0 + SW - 8 - d.textlength("GAP 5.3", font=F(SANSB, 11)), SY + 4),
       "GAP 5.3", font=F(SANSB, 11), fill=(150, 100, 0))
bars = [("78.9", "US", 78.9, NAVY), ("73.6", "CHINA", 73.6, RED), ("40.5", "INDIA", 40.5, (200, 160, 40))]
bx = x0 + 22
for val, lab, v, col in bars:
    bh = int(v * 0.95)
    by = SY + SH - CAP - 14 - bh
    d.rectangle([bx, by, bx + 78, SY + SH - CAP - 14], fill=col)
    d.text((bx + 39 - d.textlength(val, font=F(SANSB, 13)) // 2, by - 18),
           val, font=F(SANSB, 13), fill=BLACK)
    d.text((bx + 39 - d.textlength(lab, font=F(SANSB, 11)) // 2, SY + SH - CAP - 14 - 15),
           lab, font=F(SANSB, 11), fill=WHITE)
    bx += 96
d.rectangle([x0, SY + SH - CAP, x0 + SW, SY + SH], fill=BLACK)
d.text((x0 + 8, SY + SH - CAP + 4), "ASIA POWER INDEX 2026", font=F(SANSB, 11), fill=WHITE)

# ---------- hero text (starts well below scene caption strips) ----------
heroes = [
    ("1", "AI ROUT HITS ASIA",
     "Kospi closes -3.3% to 4,708.54, sheds 161 pts; intraday -5.8%. Samsung -3.1%, SK Hynix -2.5%.",
     "KOREA EXCHANGE"),
    ("2", "GUTERRES: REGULATE AI BEFORE IT'S TOO LATE",
     "UN chief urges global AI safety rules at the Bridgetown summit; 150 delegates back a risk framework.",
     "UNITED NATIONS"),
    ("3", "US LEAD OVER CHINA AT RECORD LOW",
     "Asia Power Index 2026: US 78.9, China 73.6 \u2014 gap 5.3, narrowest since 2018. India third at 40.5.",
     "LOWY INSTITUTE"),
]
HY = 336
for i, (num, head, body, src) in enumerate(heroes):
    x = SX[i]
    d.ellipse([x, HY, x + 22, HY + 22], fill=RED)
    d.text((x + 8, HY + 3), num, font=F(SANSB, 12), fill=WHITE)
    hf = F(SANSB, 15)
    lines = wrap(head, hf, SW - 30)
    yy = HY
    for ln in lines[:2]:
        d.text((x + 28, yy), ln, font=hf, fill=BLACK)
        yy += 17
    bf = F(SANS, 11)
    blines = wrap(body, bf, SW - 8)
    by = yy + 3
    for ln in blines[:2]:
        d.text((x, by), ln, font=bf, fill=BLACK)
        by += 13
    sy = HY + 66
    d.text((x, sy + 2), src, font=F(SANS, 9), fill=GRAY)
    chip(x + SW - 62, sy, "REPORTED", NAVY)

# ---------- MORE OF THE DAY bar ----------
d.rectangle([0, 418, W, 434], fill=BLACK)
d.text((8, 421), "MORE OF THE DAY  \u2014  10 STORIES", font=F(SANSB, 12), fill=WHITE)

# ---------- 10 cards ----------
cards = [
    ("AMERICAS", (0, 128, 128), "BESSENT: NVIDIA ANSWERS", "Treasury chief wants China answers.", "Reuters", "REPORTED"),
    ("FBI", (139, 0, 0), "FBI PROBES NCIC HACK", "Hackers hit police NCIC database.", "AP", "REPORTED"),
    ("WHITE HOUSE", (150, 100, 0), "IRAN STRIKES MAY RESUME", "Strikes may resume in New Year.", "Reuters", "REPORTED"),
    ("MARKETS", (0, 120, 60), "US FUTURES JUMP 3%", "Holiday rally lifts futures 3%.", "Bloomberg", "REPORTED"),
    ("SPORT", (178, 34, 34), "SKUBAL'S $450M METS DEAL", "Nine-year deal, largest ever.", "AP", "REPORTED"),
    ("SPORT", (178, 34, 34), "TOM JACKSON DIES AT 75", "Broncos LB, ESPN voice, dies.", "ESPN", "REPORTED"),
    ("LEGAL", (110, 40, 140), "STATES SUE SPACEX", "Ten states challenge AI claims.", "AP", "REPORTED"),
    ("TECH", (0, 90, 160), "ANTHROPIC IPO: $107.3B", "Raised at $83; closes $97.17.", "WSJ", "REPORTED"),
    ("EUROPE", (110, 40, 140), "POLAND: 3 MISSILES CROSSED", "Kyiv: three Kh-101s crossed.", "AP", "CLAIM"),
    ("SPACE", (90, 90, 90), "RUSSIAN NUCLEAR SATELLITE", "Intel: satellite may carry a nuke.", "Reuters", "CLAIM"),
]
CW = 200
for i, (cat, col, head, body, src, tag) in enumerate(cards):
    r, c = divmod(i, 5)
    x = 4 + c * 204
    y = 436 + r * 64
    d.rectangle([x, y, x + CW, y + 14], fill=col)
    d.text((x + 4, y + 2), cat, font=F(SANSB, 9), fill=WHITE)
    d.text((x + CW - 12, y + 2), str(i + 1), font=F(SANSB, 9), fill=WHITE)
    hf = fit(head, SANSB, 13, 10, CW - 8)
    d.text((x + 2, y + 17), head, font=hf, fill=BLACK)
    bf = F(SANS, 10)
    blines = wrap(body, bf, CW - 6)
    by = y + 33
    for ln in blines[:2]:
        d.text((x + 2, by), ln, font=bf, fill=BLACK)
        by += 11
    sy = y + 48
    d.text((x + 2, sy + 2), src, font=F(SANS, 9), fill=GRAY)
    chip(x + CW - 62, sy, tag, NAVY if tag == "REPORTED" else RED)

# ---------- map + ALSO ----------
MY = 568
d.rectangle([4, MY, 336, 852], outline=BLACK, width=1)
d.rectangle([4, MY, 336, MY + 16], fill=BLACK)
d.text((8, MY + 2), "WHERE IT HAPPENED", font=F(SANSB, 11), fill=WHITE)
# grid
for gx in range(4, 336, 16):
    d.line([gx, MY + 16, gx, 852], fill=(220, 235, 245), width=1)
for gy in range(MY + 16, 852, 16):
    d.line([4, gy, 336, gy], fill=(220, 235, 245), width=1)
# land blobs
d.ellipse([18, 606, 168, 770], fill=(150, 210, 150))
d.ellipse([180, 596, 322, 740], fill=(150, 210, 150))
d.ellipse([120, 740, 200, 800], fill=(150, 210, 150))
d.ellipse([250, 770, 320, 830], fill=(150, 210, 150))
pins = [(285, 640), (95, 700), (300, 625), (70, 690), (105, 665), (235, 660),
        (85, 640), (60, 720), (95, 735), (110, 745), (215, 620), (230, 635), (255, 615)]
for i, (px, py) in enumerate(pins, 1):
    d.ellipse([px - 8, py - 8, px + 8, py + 8], fill=RED, outline=WHITE, width=1)
    d.text((px - 3, py - 5), str(i), font=F(SANSB, 8), fill=WHITE)
d.text((8, 806), "Pins 1\u201313: 1 Seoul \u00b7 2 Bridgetown \u00b7 3 Beijing", font=F(SANS, 8), fill=BLACK)
d.text((8, 818), "4 Washington \u00b7 5 New York \u00b7 6 Tehran \u00b7 7 Chicago", font=F(SANS, 8), fill=BLACK)
d.text((8, 830), "8 SF \u00b7 9 Denver \u00b7 10 Austin \u00b7 11 Warsaw \u00b7 12 Kyiv \u00b7 13 Moscow",
       font=F(SANS, 8), fill=BLACK)

# ALSO list
d.rectangle([344, MY, 1020, MY + 16], fill=BLACK)
d.text((350, MY + 2), "ALSO ON MONDAY", font=F(SANSB, 11), fill=WHITE)
also_l = [
    "14. Paris: 100+ back 2% billionaire tax", "15. Manchester: 12,000 cleared",
    "16. Zelenskyy: 165 missiles in a week", "17. COP31: the day after pact rejected",
    "18. Benghazi: UN demands port probe", "19. Israel unity talks resume",
    "20. Gaza: two killed in Israeli strike", "21. West Bank settler attacks",
    "22. Iran war: no deal in sight",
]
also_r = [
    "23. Lebanon seizes 264 kg explosives", "24. Bahrain: strike hits plant, 2 hurt",
    "25. Sudan: defences down drones", "26. DRC: fighting traps Ebola teams",
    "27. Bangladesh: Hasina jailed if she returns", "28. Seoul minister quits in exam row",
    "29. SK Telecom -7.3% as hype cools", "30. China eases margin rules",
    "31. Seoul readies 10T-won fund",
]
af = F(SANS, 11)
for i, t in enumerate(also_l):
    d.text((350, MY + 24 + i * 27), t, font=af, fill=BLACK)
for i, t in enumerate(also_r):
    d.text((690, MY + 24 + i * 27), t, font=af, fill=BLACK)

# ---------- DATE CHECK ----------
DY = 858
d.rectangle([4, DY, 1020, 936], outline=RED, width=2)
d.text((10, DY + 4), "DATE CHECK", font=F(SANSB, 13), fill=RED)
d.text((1020 - 10 - d.textlength("READ 23 NOV 2026, 23:59 UTC \u2014 STORIES DATED 23 NOV ONLY",
       font=F(SANSB, 9)), DY + 6),
       "READ 23 NOV 2026, 23:59 UTC \u2014 STORIES DATED 23 NOV ONLY",
       font=F(SANSB, 9), fill=RED)
lo = ("LEFT OUT \u2014 NOT 23 NOV: Democrats reach 258 seats (22 Nov) \u00b7 Sparta II fire "
      "(22 Nov) \u00b7 El Chapo Isidro captured (22 Nov) \u00b7 EU\u2013Indonesia pact (21 Nov) \u00b7 "
      "Nigeria boat (21 Nov) \u00b7 ICJ Myanmar ruling (19 Nov)")
for i, ln in enumerate(wrap(lo, F(SANS, 11), 1000)):
    d.text((10, DY + 24 + i * 14), ln, font=F(SANS, 11), fill=BLACK)
d.text((10, DY + 56), "NOT YET: Dymer search continues (14 missing) \u00b7 4 House races "
       "uncalled \u00b7 COP32 venue not set \u00b7 WHO evacuating trapped Ebola staff",
       font=F(SANS, 11), fill=BLACK)

# ---------- footer ----------
ff = F(SANS, 9)
d.text((8, 942), "Sources: Reuters \u00b7 AP \u00b7 Bloomberg \u00b7 AFP \u00b7 Yonhap \u00b7 BBC \u00b7 WSJ \u00b7 "
       "NYT \u00b7 ESPN \u00b7 Lowy Institute (Asia Power Index 2026).", font=ff, fill=GRAY)
d.text((8, 954), "CHIPS: REPORTED = confirmed by wires \u00b7 CLAIM = one side's claim, "
       "not independently confirmed \u00b7 ONGOING = still developing", font=ff, fill=GRAY)
d.text((8, 966), "All times UTC. Figures as reported 23 Nov 2026. Scenes are drawn "
       "illustrations, not photographs.", font=ff, fill=GRAY)

# ---------- bottom bar ----------
d.rectangle([0, 978, W, H], fill=BLACK)
bt = "THE WORLD TODAY  \u2014  Monday 23 November 2026  \u00b7  31 stories  \u00b7  6 regions"
d.text(((W - d.textlength(bt, font=F(SANSB, 15))) // 2, 992), bt, font=F(SANSB, 15), fill=GOLD)

img.save("entry.png")
print("saved entry.png", img.size)
