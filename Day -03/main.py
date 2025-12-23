# Day-03/main.py

import random
import string
import pyperclip  # pip install pyperclip

def get_user_choice():
    print("PASSWORD GENERATOR")
    print("-" * 35)
    
    # Length input
    while True:
        try:
            length = int(input("Kitne char ka password chahiye? (8-16): "))
            if 8 <= length <= 16:
                break
            else:
                print("Sirf 8 se 16 tak daal bhai!")
        except:
            print("Number daal na!")
    
    # Options
    upper = input("Uppercase letters? (y/n): ").lower() == 'y'
    nums = input("Numbers chahiye? (y/n): ").lower() == 'y'
    syms = input("Symbols chahiye? (y/n): ").lower() == 'y'
    
    return length, upper, nums, syms

def create_password(length, upper, nums, syms):
    chars = string.ascii_lowercase  # a-z
    
    if upper:
        chars += string.ascii_uppercase  # A-Z
    if nums:
        chars += string.digits           # 0-9
    if syms:
        chars += string.punctuation      # !@#$ etc
    
    if len(chars) == 26 and (upper or nums or syms):
        print("Bhai, kam se kam ek option toh chahiye!")
        return None
    
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    
    return password

def check_strength(pwd):
    score = 0
    if len(pwd) >= 12:
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in string.punctuation for c in pwd):
        score += 1
    
    if score <= 1:
        return "Weak"
    elif score <= 3:
        return "Medium"
    else:
        return "Strong"

def main():
    length, upper, nums, syms = get_user_choice()
    password = create_password(length, upper, nums, syms)
    
    if password:
        strength = check_strength(password)
        print(f"\nTera Password: {password}")
        print(f"Strength: {strength}")
        
        pyperclip.copy(password)
        print("Clipboard pe copy ho gaya!")
        
        input("\nEnter daba ke band kar...")

if __name__ == "__main__ ":
    main()