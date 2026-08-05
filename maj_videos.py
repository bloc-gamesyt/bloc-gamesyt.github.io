from yt_dlp import YoutubeDL
import json

CHANNEL_URL = "https://www.youtube.com/@Bloc-gamesYT/videos"

options = {
    "extract_flat": False,
    "quiet": True,
    "playlistend": 50,
    "ignoreerrors": True
}

with YoutubeDL(options) as ydl:
    data = ydl.extract_info(CHANNEL_URL, download=False)

videos = []

for video in data.get("entries", []):

    if not video:
        continue

    videos.append({
        "id": video["id"],
        "titre": video.get("title", "Sans titre"),
        "vues": video.get("view_count", 0),
        "date": video.get("upload_date", "00000000"),
        "miniature": video.get("thumbnail", "")
    })


# Plus récente en premier
videos.sort(
    key=lambda v: v["date"],
    reverse=True
)


with open("videos.json", "w", encoding="utf-8") as f:
    json.dump(
        videos,
        f,
        indent=4,
        ensure_ascii=False
    )


print("Mise à jour terminée :", len(videos), "vidéos")