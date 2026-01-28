# Day 13 - To-Do List (Console App)
# 100 Days of Python Challenge

tasks = []

def show_menu():
    print("\nTo-Do List Menu")
    print("--------------------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1/2/3/4): ").strip()

    # Add task
    if choice == "1":
        task = input("Enter a new task: ").strip()
        if task == "":
            print("Task cannot be empty.")
        else:
            tasks.append({"task": task, "done": False})
            print("Task added successfully.")

    # View tasks
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            print("--------------------")
            for i, t in enumerate(tasks, start=1):
                status = "Done" if t["done"] else "Pending"
                print(f"{i}. {t['task']} - {status}")

    # Mark task as completed
    elif choice == "3":
        if not tasks:
            print("No tasks to mark.")
        else:
            task_no = int(input("Enter task number to mark as completed: "))
            if 1 <= task_no <= len(tasks):
                tasks[task_no - 1]["done"] = True
                print("Task marked as completed.")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "4":
        print("Program End. Stay productive!")
        break

    else:
        print("Invalid choice. Please try again.")
