# Day 01: Motivation Booster
# Author: Aditya
# Date: 9 November 2025

import datetime
import random

START_DATE = datetime.date(2025, 11, 9)

quotes = [
    "Bhai, aaj se shuruat! 53 din baad tu pro banega!",
    "Har din 1 program = 1 skill up!",
    "Code likh, error aayega, fix kar, jeet jaayega!",
    "Python seekh raha hai? Toh future bright hai!",
    "Aaj ka mehnat, kal ka confidence!",
    "Error aaya? Welcome to programming!",
    "Tu ruk mat, code chalte reh!"
]

def main():
    today = datetime.date.today()
    day_number = (today - START_DATE).days + 1
    
    if day_number < 1:
        print("Bhai, challenge 9 Nov se start hai! Abhi wait kar")
        return
    
    quote = random.choice(quotes)
    
    print("="*50)
    print(f"     DAY {day_number} OF PYTHON CHALLENGE")
    print("="*50)
    print(f"Aaj ki taarikh: {today.strftime('%d %B %Y')}")
    print(f"Time: {datetime.datetime.now().strftime('%I:%M %p')}")
    print()
    print("MOTIVATION FOR TODAY:")
    print(f"   \"{quote}\"")
    print()
    print("Ab code likhna shuru kar!")
    print("="*50)

if _name_ == "_main_":
    main()
