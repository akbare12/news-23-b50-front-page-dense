# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b50-front-page-dense/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b50-front-page-dense/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A one-page front page summing up 23 November 2026's world news in a single image:
the AI rout that hit Asian markets, the UN chief's call to regulate AI before it is
too late, and the US lead over China at its narrowest since 2018 — plus 28 more
stories, a world map, and a DATE CHECK box separating 23 Nov news from stories
dated other days.

## Stories (31)

**Heroes:** Kospi −3.3% to 4,708.54 (AI rout hits Asia) · Guterres at the Bridgetown
summit — 150 delegates back an AI risk framework · Asia Power Index 2026: US 78.9,
China 73.6, gap 5.3.

**10 cards:** Bessent demands Nvidia answers · FBI probes NCIC hack · Trump: Iran
strikes may resume in the New Year · Nasdaq futures +3% · Skubal's $450M Mets deal ·
Tom Jackson dies at 75 · States sue SpaceX · Anthropic IPO $107.3B (raised at
$83/share) · Poland: 3 Russian Kh-101 missiles crossed airspace (CLAIM) · Intel
warns of a Russian nuclear satellite (CLAIM).

**Also on Monday (18):** Paris 2% billionaire tax · Manchester 12,000 cleared ·
Zelenskyy: 165 Russian missiles in a week · COP31, the day after · Israel unity
talks resume · Gaza: two killed in Israeli strike · West Bank settler attacks ·
Iran war: no deal in sight · Lebanon seizes 264 kg explosives · Bahrain: strike
hits plant, 2 hurt · Benghazi: UN demands port probe · Sudan: air defences down
drones · DRC: fighting traps Ebola teams · Bangladesh: Hasina jailed if she
returns · Seoul minister quits over AI exam chaos · SK Telecom −7.3% · China
eases margin rules · Seoul readies 10T-won fund.

## How it is built

`draw.py` (Pillow) renders `entry.png` (1024×1024). `main.py` (stdlib only)
copies it to `$MAKEFUN_OUTPUT_DIR/entry.png` and verifies the PNG header,
dimensions, size and byte-identity of the copy.

## Sources

Reuters · AP · Bloomberg · AFP · Yonhap · BBC · WSJ · NYT · ESPN · Lowy
Institute (Asia Power Index 2026). All times UTC. Figures as reported
23 Nov 2026. Scenes are drawn illustrations, not photographs.
