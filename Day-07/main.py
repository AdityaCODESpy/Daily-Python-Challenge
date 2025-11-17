# Day-07/main.py
def calculator():
    print("SIMPLE CALCULATOR")
    print("1. +  2. -  3. *  4. /")
    
    while True:
        choice = input("\nOperation chuno (1-4): ")
        if choice in ["1","2","3","4"]:
            a = float(input("Pehla number: "))
            b = float(input("Dusra number: "))
            
            if choice == "1": print("Result:", a + b)
            elif choice == "2": print("Result:", a - b)
            elif choice == "3": print("Result:", a * b)
            elif choice == "4":
                if b != 0:
                    print("Result:", a / b)
                else:
                    print("Zero se divide nahi kar sakte!")
        else:
            print("Sirf 1-4 daal!")
            
        again = input("Phir calculate karega? (y/n): ")
        if again.lower() != "y":
            print("Bye!")
            break

calculator()