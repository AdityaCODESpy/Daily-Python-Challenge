# Day-15/main.py
from gtts import gTTS
text = input("Kya bolna hai? ")
tts = gTTS(text, lang='hi')
tts.save("speech.mp3")
print("speech.mp3 ban gaya! Play kar!")