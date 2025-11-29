# Day-13/main.py
import pyshorteners
print("URL SHORTENER")
long = input("Lamba URL daal: ")
s = pyshorteners.Shortener()
short = s.tinyurl.short(long)
print("Short URL →", short) 