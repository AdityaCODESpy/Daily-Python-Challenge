# Day-12/main.py — YT-DLP VERSION (2025 WORKING!)
import yt_dlp

print("YOUTUBE DOWNLOADER 2025 — YT-DLP POWER!")
link = input("YouTube link daal: ")

ydl_opts = {
    'format': 'best[height<=720]',  # HD quality
    'outtmpl': 'video.%(ext)s',  # File name
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print("DOWNLOAD HO GAYA → video.mp4 check kar!")
except:
    print("Link galat hai ya internet off hai!")