from yt_dlp import YoutubeDL
import json

CHANNEL_URL = "https://www.youtube.com/@Bloc-gamesYT/videos"

options = {
    "extract_flat": False,
    "quiet": True,
    "playlistend": 50
}

with YoutubeDL(options) as ydl:
    infos = ydl.extract_info(CHANNEL_URL, download=False)

videos = []

for video in infos["entries"]:

    videos.append({
        "id": video.get("id"),
        "titre": video.get("title"),
        "vues": video.get("view_count", 0),
        "date": video.get("upload_date"),
        "miniature": video.get("thumbnail")
    })


# Tri du plus récent au plus ancien
videos.sort(
    key=lambda x: x["date"] if x["date"] else "",
    reverse=True
)


with open("videos.json", "w", encoding="utf-8") as fichier:
    json.dump(
        videos,
        fichier,
        indent=4,
        ensure_ascii=False
    )


print(f"{len(videos)} vidéos enregistrées !")