# Day-21/main.py (Expense Tracker)
expenses = []

while True:
    print("\n1. Add Expense  2. View Total  3. Exit")
    ch = input("Choose: ")
    
    if ch == "1":
        amount = float(input("Kitna kharcha: "))
        desc = input("Kis cheez pe: ")
        expenses.append({"amount": amount, "desc": desc})
        print("Add ho gaya!")
    elif ch == "2":
        total = sum(e["amount"] for e in expenses)
        print("Total kharcha:", total)
        for e in expenses:
            print(f"- {e['desc']}: {e['amount']}")
    elif ch == "3":
        break