# Day-05/main.py
import random

def play():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    comp_score = 0
    
    while True:
        print("\n1. Rock  2. Paper  3. Scissors")
        user = input("Tera move (1/2/3): ")
        if user not in ["1","2","3"]:
            print("Sirf 1, 2, ya 3 daal bhai!")
            continue
            
        user_choice = choices[int(user)-1]
        comp_choice = random.choice(choices)
        
        print(f"Tu: {user_choice} | Computer: {comp_choice}")
        
        if user_choice == comp_choice:
            print("TIE!")
        elif (user_choice == "rock" and comp_choice == "scissors") or \
             (user_choice == "paper" and comp_choice == "rock") or \
             (user_choice == "scissors" and comp_choice == "paper"):
            print("TU JEETA!")
            user_score += 1
        else:
            print("COMPUTER JEETA!")
            comp_score += 1
            
        print(f"Score → Tu: {user_score} | Computer: {comp_score}")
        
        again = input("Phir khelna hai? (y/n): ")
        if again.lower() != "y":
            break

    print(f"\nFINAL: Tu {user_score} - {comp_score} Computer")
    print("Champion!" if user_score > comp_score else "Achha khela!")

play()