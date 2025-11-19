# Day-10/main.py
import json
import os
import random
import string

FILE = "passwords.json"
MASTER = "1234"   # ← Pehli baar yahi daal, baad mein change kar dena

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(16))

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def main():
    print("PASSWORD MANAGER")
    print("-" * 30)
    
    pwd = input("Master Password daal: ")
    if pwd != MASTER:
        print("GALAT PASSWORD! Band ho raha hai...")
        return
    
    data = load_data()
    
    while True:
        print("\n1. Add Password   2. View All   3. Generate   4. Exit")
        ch = input("Kya karega? ")
        
        if ch == "1":
            site = input("Website/App ka naam: ")
            username = input("Username/Email: ")
            password = input("Password (khali chhod to generate): ")
            if not password:
                password = generate_password()
            data[site] = {"user": username, "pass": password}
            save_data(data)
            print("Password save ho gaya!")
            
        elif ch == "2":
            if not data:
                print("Koi password nahi hai abhi tak!")
            for site, info in data.items():
                print(f"\n{site} → {info['user']} : {info['pass']}")
                
        elif ch == "3":
            print("Naya strong password:", generate_password())
            
        elif ch == "4":
            print("Bye! Sab safe hai!")
            break

if __name__ == "__main__":
    main()