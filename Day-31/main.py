# Day-31/main.py
# pip install tkinter (already hai)

from tkinter import *

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.set(result)
        except:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = Tk()
root.title("GUI CALCULATOR")
root.geometry("400x600")

screen = StringVar()
screen.set("")
entry = Entry(root, textvar=screen, font="lucida 30 bold")
entry.pack(fill=X, ipadx=8, pady=10, padx=10)

buttons = [
    "C", "/", "*", "=",
    "7", "8", "9", "-",
    "4", "5", "6", "+",
    "1", "2", "3", "",
    "0", ".", ""
]

f = Frame(root, bg="grey")
f.pack()

i = 0
for btn in buttons:
    b = Button(f, text=btn, font="lucida 25 bold", padx=20, pady=20)
    b.grid(row=i//4, column=i%4)
    b.bind("<Button-1>", click)
    i += 1

root.mainloop()