# 🎵 AURA Studio Player

**Professional mastering music player with Auto-Master AI, streaming, and free music library.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🚀 Live App
👉 **[Open AURA Player](https://YOUR-USERNAME.github.io/aura-player/)**

## 📦 What's in this repo

```
aura-player/
├── index.html              ← AURA v5 player (open this to use)
├── music_index.json        ← Free music library (10,000+ CC tracks)
├── update_index.py         ← Script to refresh the music library
├── README.md
└── LICENSE
```

## 🎧 Features

- **Auto-Master AI** — analyses every song, sets EQ/compression automatically
- **Persistent Memory** — remembers settings for every track permanently
- **Streaming** — search and play from YouTube, Internet Archive, Jamendo
- **Free Music Library** — 10,000+ Creative Commons tracks built in
- **Sleep Timer** — with circular countdown ring and smooth fade-out
- **Wake-up Alarm** — music alarm clock with repeat days and snooze
- **PWA** — installable on any phone/tablet, works offline
- **Playlist Import** — from Spotify (CSV), YouTube Music (JSON), Amazon (CSV)
- **Full mastering chain**: HPF → 10-band EQ → M/S Stereo → Multiband Comp → Exciter → Air → Limiter

## 🎵 Music Library

The `music_index.json` file contains metadata and stream URLs for free, legal music:

| Source | Tracks | License |
|--------|--------|---------|
| Jamendo | 5,000+ | Creative Commons |
| Internet Archive | 3,000+ | Public Domain |
| Free Music Archive | 2,000+ | Various CC |

**To refresh the library** (run once a month):
```bash
pip install requests
python3 update_index.py
```
Then commit and push the updated `music_index.json`.

## 💰 Selling AURA to Friends

You own this code (MIT license). You can:
- ✅ Share the GitHub Pages link — free access
- ✅ Sell premium access to your curated music index
- ✅ Customise and resell AURA with your branding
- ✅ Offer setup help as a paid service
- ❌ Do NOT store or distribute copyrighted commercial music

## 🛠 Setup (5 minutes)

1. Fork this repo on GitHub
2. Go to **Settings → Pages → Deploy from main branch**
3. Your AURA is live at `https://USERNAME.github.io/aura-player/`
4. Run `python3 update_index.py` to populate the music library
5. Commit and push `music_index.json`

## 📱 Install as App (PWA)

Open the GitHub Pages URL in Chrome or Samsung Internet → tap the install banner → AURA appears on your home screen like a native app.

---

Built with ❤️ using Web Audio API · No backend required · 100% free
