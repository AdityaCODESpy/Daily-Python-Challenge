# Day-24/main.py (Simple Notes App)
notes = []

while True:
    print("\n1. Add Note  2. View Notes  3. Exit")
    ch = input("Choose: ")
    
    if ch == "1":
        note = input("Note likh: ")
        notes.append(note)
    elif ch == "2":
        for i, n in enumerate(notes, 1):
            print(f"{i}. {n}")
    elif ch == "3":
        break