from yt_dlp import YoutubeDL
import json

CHANNEL = "https://www.youtube.com/@Bloc-gamesYT/videos"

opts = {
    "extract_flat": True,
    "quiet": True
}

with YoutubeDL(opts) as ydl:
    data = ydl.extract_info(CHANNEL, download=False)

videos = []

for video in data["entries"]:
    videos.append(video["id"])

with open("videos.json","w",encoding="utf-8") as f:
    json.dump(videos,f,indent=4)

print("videos.json mis à jour")