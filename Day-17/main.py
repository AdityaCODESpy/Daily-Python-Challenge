# Day-17/main.py
import instaloader
L = instaloader.Instaloader()
username = input("Instagram username daal (without @): ")
L.download_profile(username, profile_pic_only=True)
print(f"{username} ki profile pic download ho gayi!")