# Day-27/main.py — MUSIC PLAYER (Pygame 2025 WORKING!)
import pygame
import time

print("MUSIC PLAYER — Pygame Edition")
file = input("MP3 file ka full path daal (jaise C:\\Music\\song.mp3): ")

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()

print("Music baj raha hai! Band karne ke liye Enter daba...")
input()  # Enter dabane tak bajega
pygame.mixer.music.stop()
print("Music band ho gaya!")