# Day 02: To-Do List App
# Author: AdityaCODESpy
# Date: 10 November 2025

import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                tasks.append(line.strip())
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks):
    task = input("Naya task daal bhai: ")
    tasks.append(task)
    print("Task add ho gaya!")

def view_tasks(tasks):
    if not tasks:
        print("Koi task nahi hai abhi!")
    else:
        print("\nTERE TASKS:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("Kaunsa task delete karega (number daal): "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                print(f"Task delete ho gaya: {removed}")
            else:
                print("Galat number daala bhai!")
        except:
            print("Sirf number daal!")

def main():
    print("="*50)
    print("     DAY 2 OF PYTHON CHALLENGE")
    print("         TO-DO LIST APP")
    print("="*50)
    
    tasks = load_tasks()
    
    while True:
        print("\nMENU:")
        print("1. Naya Task Add Kar")
        print("2. Saare Tasks Dekh")
        print("3. Task Delete Kar")
        print("4. Save & Exit")
        print("5. Exit Bina Save")
        
        choice = input("\nKya karega? (1/2/3/4/5): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks save ho gaye! Bye!")
            break
        elif choice == "5":
            print("Bye! Tasks save nahi hue!")
            break
        else:
            print("Galat option! 1-5 mein se daal!")

if __name__ == "__main__":
    main()