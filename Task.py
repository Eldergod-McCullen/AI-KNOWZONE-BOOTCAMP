import json
from datetime import datetime

TASKS_FILE = "tasks.json"
tasks = []

def load_tasks():                     # FOR LOADING THE TASKS FROM THE JSON FILE
    global tasks
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []

def save_tasks():                     # FOR SAVING THE TASKS TO THE JSON FILE
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():                                 # FOR ADDING TASKS ONTO THE JSON FILE
    task_name = input("Enter a new task: ")
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    try:
        if due_date:
            datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Task not added.")
        return
    task = {
        "name": task_name,
        "due_date": due_date if due_date else None,
        "completed": False
    }
    tasks.append(task)
    save_tasks()
    print(f"Task '{task_name}' added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "✓" if task["completed"] else "✗"
            due = f" (Due: {task['due_date']})" if task["due_date"] else ""
            print(f"{idx}. [{status}] {task['name']}{due}")

def remove_task():                   # FOR REMOVING THE TASKS FROM THE JSON FILE
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter the task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num - 1)
                save_tasks()
                print(f"Task '{removed['name']}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def edit_task():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter the task number to edit: "))
            if 1 <= num <= len(tasks):
                task = tasks[num - 1]
                new_name = input(f"Enter new name (leave blank to keep '{task['name']}'): ")
                new_due = input(f"Enter new due date (YYYY-MM-DD, leave blank to keep '{task['due_date']}'): ")
                if new_name:
                    task["name"] = new_name
                if new_due:
                    try:
                        datetime.strptime(new_due, "%Y-%m-%d")
                        task["due_date"] = new_due
                    except ValueError:
                        print("Invalid date format. Due date not changed.")
                save_tasks()
                print("Task updated.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def mark_complete():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter the task number to mark as complete: "))
            if 1 <= num <= len(tasks):
                tasks[num - 1]["completed"] = True
                save_tasks()
                print(f"Task '{tasks[num - 1]['name']}' marked as complete.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Edit Task")
        print("5. Mark Task as Complete")
        print("6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            edit_task()
        elif choice == '5':
            mark_complete()
        elif choice == '6':
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()