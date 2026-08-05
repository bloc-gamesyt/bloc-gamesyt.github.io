from yt_dlp import YoutubeDL
import json

# Mets ton vrai ID de chaîne ici
CHANNEL_ID = "UCJlbzgymdG0bEYWQrulOI2w"

URL = f"https://www.youtube.com/channel/{CHANNEL_ID}/videos"

options = {
    "extract_flat": True,
    "quiet": False,
    "playlistend": 50
}

with YoutubeDL(options) as ydl:
    data = ydl.extract_info(URL, download=False)


videos = []

for video in data.get("entries", []):
    if video:
        videos.append({
            "id": video["id"],
            "titre": video.get("title", "Sans titre")
        })


with open("videos.json", "w", encoding="utf-8") as f:
    json.dump(videos, f, indent=4, ensure_ascii=False)


print("Nombre de vidéos trouvées :", len(videos))