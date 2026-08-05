from yt_dlp import YoutubeDL
import json

# Remplace par l'URL de l'onglet Shorts de ta chaîne
CHANNEL_URL = "https://www.youtube.com/@Bloc-gamesYT/shorts"


options = {
    "extract_flat": True,
    "quiet": False,
    "playlistend": 50,
    "ignoreerrors": True
}


with YoutubeDL(options) as ydl:
    data = ydl.extract_info(CHANNEL_URL, download=False)


shorts = []


for video in data.get("entries", []):

    if video:

        shorts.append({
            "id": video["id"],
            "titre": video.get("title", "Sans titre")
        })


with open("shorts.json", "w", encoding="utf-8") as f:
    json.dump(
        shorts,
        f,
        indent=4,
        ensure_ascii=False
    )


print("Shorts trouvés :", len(shorts))