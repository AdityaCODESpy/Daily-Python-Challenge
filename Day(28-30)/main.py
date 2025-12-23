# Day-30/main.py (Simple Chatbot)
print("SIMPLE CHATBOT — Hello bol!")

while True:
    msg = input("Tu: ").lower()
    if "hello" in msg or "hi" in msg:
        print("Bot: Hello bhai! Kaise ho?")
    elif "bye" in msg:
        print("Bot: Bye! Milte hain!")
        break
    else:
        print("Bot: Samajh nahi aaya — hello bol na!")