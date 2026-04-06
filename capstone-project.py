# 📝 Capstone Project 1: Advanced Todo App (File I/O)

import sys
import os

TASKS_FILE = "todo_tasks.txt"

def display_menu():
    print("\n--- 📝 PYTHON TODO APP ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Clear All")
    print("5. Exit")

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def main():
    while True:
        display_menu()
        choice = input("Enter choice (1-5): ")
        tasks = load_tasks()

        if choice == "1":
            if not tasks:
                print("\nYour list is empty!")
            else:
                print("\nYOUR TASKS:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "3":
            if not tasks:
                print("Nothing to remove!")
                continue
            try:
                task_num = int(input("Enter task number to remove: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a numeric ID.")

        elif choice == "4":
            confirm = input("Are you sure? (y/n): ")
            if confirm.lower() == 'y':
                save_tasks([])
                print("All tasks cleared!")

        elif choice == "5":
            print("Goodbye!")
            sys.exit()
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    # main() 
    # (Uncomment to play the game!)
    pass
