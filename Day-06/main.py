# Day-06/main.py
import random

words = ["python", "coding", "challenge", "github", "hangman", "aditya"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("HANGMAN GAME — 6 galat guesses allowed!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    print(f"Attempts bache: {attempts}")
    guess = input("Ek letter daal: ").lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Sahi guess!")
    else:
        attempts -= 1
        print("Galat!")

if "_" not in guessed:
    print("\nTU JEET GAYA! Word tha:", word)
else:
    print("\nHAAR GAYA! Word tha:", word)