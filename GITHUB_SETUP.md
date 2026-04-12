# 🚀 AURA — GitHub Setup Guide

## Step 1: Create GitHub Repository

1. Go to **github.com** → Sign in
2. Click **"New repository"** (green button)
3. Name it: `aura-player`
4. Set to **Public** (so GitHub Pages works free)
5. Click **"Create repository"**

---

## Step 2: Upload Files

Upload these files to your repo:
- `index.html` ← Main AURA player
- `music_index.json` ← Free music library
- `update_index.py` ← Script to refresh library
- `README.md` ← Documentation

**How to upload:**
1. In your repo, click **"Add file" → "Upload files"**
2. Drag all 4 files
3. Click **"Commit changes"**

---

## Step 3: Enable GitHub Pages

1. Go to your repo **Settings**
2. Click **"Pages"** in left sidebar
3. Under "Source" → select **"Deploy from a branch"**
4. Branch: **main** · Folder: **/ (root)**
5. Click **Save**

⏳ Wait 2–3 minutes…

Your AURA is now live at:
```
https://YOUR-USERNAME.github.io/aura-player/
```

---

## Step 4: Grow the Music Library

Run this once a month to add more tracks:

```bash
# Install Python dependency
pip install requests

# Run updater
python3 update_index.py

# Push updated index
git add music_index.json
git commit -m "Update music library"
git push
```

---

## 💰 Sharing / Selling AURA

**Option 1 — Free sharing:**
Share the GitHub Pages link. Anyone can open it in their browser instantly.

**Option 2 — Premium access:**
- Keep your repo Private (₹0 on GitHub)
- Share only with paying friends
- Charge ₹199–499 for lifetime access

**Option 3 — Custom domain:**
- Buy a domain (e.g., auramusic.in — ~₹800/year)
- Point it to GitHub Pages
- Looks professional: `https://auramusic.in`

**Option 4 — PWA distribution:**
- Friends open the URL in Chrome/Samsung Internet
- Tap "Add to Home Screen"
- Looks exactly like a Play Store app

---

## 📞 What friends get

✅ AURA Studio Player (professional mastering)
✅ Auto-Master AI (analyses every song automatically)
✅ Free music library (50+ tracks, growing monthly)
✅ Search & stream from YouTube, Archive.org, Jamendo
✅ Sleep timer + Wake-up alarm
✅ Works on any phone/tablet/laptop
✅ No ads, no subscription, forever

---

## ⚠️ Legal note

- AURA itself: 100% yours to sell ✅
- music_index.json: CC/Public Domain only ✅  
- Streaming: Piped API / Archive.org / Jamendo ✅
- DO NOT add copyrighted MP3s to the repo ❌
