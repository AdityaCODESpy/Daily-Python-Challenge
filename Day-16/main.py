# Day-16/main.py
import pyautogui, time
print("5 second mein screenshot le raha hoon...")
time.sleep(5)
ss = pyautogui.screenshot()
ss.save("screenshot.png")
print("screenshot.png save ho gaya!")