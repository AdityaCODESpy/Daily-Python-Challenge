# Day-04/main.py

import random
import os  # <-- YE ADD KIYA

HIGHSCORE_FILE = "highscore.txt"

def load_highscore():
    if os.path.exists(HIGHSCORE_FILE):  # <-- YE FIX KIYA
        with open(HIGHSCORE_FILE, "r") as file:
            return int(file.read())
    return 999

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as file:
        file.write(str(score))

def play_game():
    print("NUMBER GUESSING GAME")
    print("-" * 30)
    
    secret = random.randint(1, 100)
    attempts = 0
    print("Main 1-100 ke beech ek number soch raha hoon!")
    
    while True:
        guess = int(input("Tera guess daal: "))
        attempts += 1
        
        if guess < secret:
            print("Kam hai! Thoda zyada soch!")
        elif guess > secret:
            print("Zyada hai! Thoda kam soch!")
        else:
            print(f"SAHI JAWAB! {attempts} attempts mein guess kiya!")
            return attempts

def main():
    highscore = load_highscore()
    print(f"Current High Score: {highscore} attempts")
    
    attempts = play_game()
    
    if attempts < highscore:
        print("NEW HIGH SCORE!")
        save_highscore(attempts)
    else:
        print("Achha khel! High score behtar karne ki koshish kar!")
    
    input("\nEnter daba ke band kar...")

if __name__ == "__main__":
    main()