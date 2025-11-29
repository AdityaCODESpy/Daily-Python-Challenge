import pywhatkit
import time

print("=== WhatsApp Message Scheduler - FINAL FIX ===\n")

# Sab kuch string mein lete hain pehle
msg = input("Message likh: ")

# Number - sirf string, kabhi int nahi
phone = input("Number daal (+91 ke saath): ").strip()

# Auto +91 add kar deta hai
if not phone.startswith("+"):
    phone = phone.replace(" ", "").replace("-", "")
    if phone.startswith("0"):
        phone = "+91" + phone[1:]
    elif phone.startswith("91"):
        phone = "+" + phone
    else:
        phone = "+91" + phone

print(f"Final number: {phone}")

# Time - ab yahan int bana denge
h = int(input("Hour (0-23): "))
m = int(input("Minute (0-59): "))

print(f"\nMessage: {msg}")
print(f"Number : {phone}")
print(f"Time   : {h:02d}:{m:02d}\n")

print("10 second mein WhatsApp Web khulega...")
print("→ Pehli baar QR scan kar lena bhai!")
time.sleep(10)

try:
    pywhatkit.sendwhatmsg(h, m, msg, phone)   # h aur m int, phone string
    print("\nMessage bheja gaya ya schedule ho gaya! SUCCESS")
except Exception as e:
    print(f"\nError aaya: {e}")

print("\nHo gaya bhai! Ab jaa ke soja 😎")
input("\nEnter daba ke band kar...")