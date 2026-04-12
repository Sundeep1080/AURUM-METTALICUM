#!/usr/bin/env python3
"""
AURA Music Index Builder
Fetches free/CC music metadata from Jamendo, Internet Archive, FMA
Run this monthly to keep the library fresh.

Usage:
    pip install requests
    python3 update_index.py

Then commit music_index.json to your GitHub repo.
"""

import json, time, sys
from datetime import datetime

try:
    import requests
except ImportError:
    print("Install requests first: pip install requests")
    sys.exit(1)

INDEX = {
    "version": "1.0",
    "name": "AURA Music Index",
    "description": "Curated free & Creative Commons music — safe to stream and download",
    "updated": datetime.now().strftime("%Y-%m-%d"),
    "total": 0,
    "sources": ["Jamendo", "Internet Archive", "Free Music Archive"],
    "genre_counts": {},
    "tracks": []
}

HEADERS = {"User-Agent": "AURA-Player/1.0"}

def log(msg): print(f"  ✓ {msg}")
def warn(msg): print(f"  ⚠ {msg}")

# ── 1. JAMENDO ─────────────────────────────────────────────
print("\n📀 Fetching Jamendo (Creative Commons)...")
JAMENDO_CLIENT = "b6747d04"
GENRES = ["rock","pop","jazz","classical","electronic","ambient",
          "folk","world","metal","blues","reggae","soul","hiphop","indie","country"]

for genre in GENRES:
    try:
        r = requests.get(
            "https://api.jamendo.com/v3.0/tracks/",
            params={
                "client_id": JAMENDO_CLIENT,
                "format": "json",
                "limit": 100,
                "tags": genre,
                "include": "musicinfo",
                "audioformat": "mp32",
                "order": "popularity_total"
            },
            headers=HEADERS, timeout=12
        )
        tracks = r.json().get("results", [])
        for t in tracks:
            if not t.get("audio") or not t.get("name"):
                continue
            INDEX["tracks"].append({
                "id": f"jmd_{t['id']}",
                "title": t["name"],
                "artist": t.get("artist_name", "Unknown"),
                "album": t.get("album_name", ""),
                "genre": genre.title(),
                "duration": t.get("duration", 0),
                "stream_url": t.get("audio", ""),
                "download_url": t.get("audiodownload", ""),
                "image": t.get("image", ""),
                "license": "Creative Commons",
                "source": "Jamendo",
                "year": (t.get("releasedate","")[:4] or "")
            })
        log(f"Jamendo/{genre}: {len(tracks)} tracks")
        time.sleep(0.4)
    except Exception as e:
        warn(f"Jamendo/{genre}: {e}")

# ── 2. INTERNET ARCHIVE ────────────────────────────────────
print("\n📚 Fetching Internet Archive (public domain)...")
IA_QUERIES = [
    ("classical music", "Classical"),
    ("jazz recordings", "Jazz"),
    ("blues music", "Blues"),
    ("folk music traditional", "Folk"),
    ("piano solo classical", "Classical"),
    ("orchestra symphony", "Classical"),
    ("old time radio music", "Various"),
    ("78rpm records music", "Various"),
    ("world music ethnic", "World"),
    ("ambient electronic", "Electronic"),
]

for query, genre in IA_QUERIES:
    try:
        r = requests.get(
            "https://archive.org/advancedsearch.php",
            params={
                "q": f"({query}) AND mediatype:audio",
                "fl[]": ["identifier","title","creator","year"],
                "rows": 60,
                "output": "json",
                "sort[]": "downloads desc"
            },
            headers=HEADERS, timeout=15
        )
        items = r.json().get("response", {}).get("docs", [])
        for item in items:
            if not item.get("identifier") or not item.get("title"):
                continue
            INDEX["tracks"].append({
                "id": f"ia_{item['identifier']}",
                "title": str(item.get("title",""))[:100],
                "artist": str(item.get("creator","Internet Archive"))[:80],
                "album": "",
                "genre": genre,
                "duration": 0,
                "stream_url": f"https://archive.org/details/{item['identifier']}",
                "download_url": f"https://archive.org/download/{item['identifier']}",
                "image": f"https://archive.org/services/img/{item['identifier']}",
                "license": "Public Domain / CC",
                "source": "Internet Archive",
                "year": str(item.get("year",""))
            })
        log(f"Archive.org '{query}': {len(items)} items")
        time.sleep(0.5)
    except Exception as e:
        warn(f"Archive.org '{query}': {e}")

# ── 3. FREE MUSIC ARCHIVE ──────────────────────────────────
print("\n🎵 Fetching Free Music Archive...")
FMA_GENRES = ["Electronic","Rock","Hip-Hop","Jazz","Classical",
              "Pop","Folk","Ambient","Soul","Metal","Country","Reggae"]

for genre in FMA_GENRES:
    try:
        r = requests.get(
            "https://freemusicarchive.org/api/get/tracks.json",
            params={
                "genre_title": genre,
                "limit": 50,
                "api_key": "60BLHNQCAOUFPIBZ"
            },
            headers=HEADERS, timeout=12
        )
        tracks = r.json().get("dataset", [])
        for t in tracks:
            url = t.get("track_url","") or t.get("track_file","")
            if not url or not t.get("track_title"):
                continue
            INDEX["tracks"].append({
                "id": f"fma_{t.get('track_id','')}",
                "title": t.get("track_title","")[:100],
                "artist": t.get("artist_name","Unknown")[:80],
                "album": t.get("album_title",""),
                "genre": genre,
                "duration": int(t.get("track_duration",0) or 0),
                "stream_url": t.get("track_url",""),
                "download_url": t.get("track_file", t.get("track_url","")),
                "image": t.get("album_image_file",""),
                "license": t.get("license_title","CC"),
                "source": "Free Music Archive",
                "year": str(t.get("track_date_created",""))[:4]
            })
        log(f"FMA/{genre}: {len(tracks)} tracks")
        time.sleep(0.4)
    except Exception as e:
        warn(f"FMA/{genre}: {e}")

# ── DEDUPLICATE ────────────────────────────────────────────
print("\n🔄 Deduplicating...")
seen = set()
unique = []
for t in INDEX["tracks"]:
    key = f"{t['title'].lower().strip()}|{t['artist'].lower().strip()}"
    if key not in seen:
        seen.add(key)
        unique.append(t)
removed = len(INDEX["tracks"]) - len(unique)
INDEX["tracks"] = unique
print(f"  Removed {removed} duplicates")

# ── FINALIZE ──────────────────────────────────────────────
for t in INDEX["tracks"]:
    g = t.get("genre","Other")
    INDEX["genre_counts"][g] = INDEX["genre_counts"].get(g, 0) + 1

INDEX["total"] = len(INDEX["tracks"])

with open("music_index.json", "w", encoding="utf-8") as f:
    json.dump(INDEX, f, ensure_ascii=False, separators=(',',':'))

size_kb = len(json.dumps(INDEX)) / 1024
print(f"\n✅ Index built:")
print(f"   Total tracks : {INDEX['total']:,}")
print(f"   File size    : {size_kb:.1f} KB")
print(f"   Genre counts : {INDEX['genre_counts']}")
print(f"\n📤 Now run:")
print(f"   git add music_index.json")
print(f"   git commit -m 'Update music index - {INDEX['updated']}'")
print(f"   git push")
