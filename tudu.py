import json
from datetime import datetime

TODO_FILE = "todo_list.json"

def load_todos():
    try:
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

def display_todo():
    todos = load_todos()

    if not todos:
        print("Your to-do list is empty!")
        return

    print("\nYour To-Do List:")
    for category, tasks in todos.items():
        print(f"\nCategory: {category}")
        for idx, task in enumerate(tasks, start=1):
            status = task.get('status', 'Pending')
            priority = task.get('priority', 'Medium')
            due_date = task.get('due_date', 'No due date')
            print(f"  {idx}. {task['description']} [Status: {status}, Priority: {priority}, Due: {due_date}]")

def add_task():
    todos = load_todos()

    category = input("Enter task category (e.g., Work, Personal): ").capitalize()
    description = input("Enter task description: ")
    priority = input("Enter task priority (High, Medium, Low): ").capitalize()
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ")
    status = "Pending"

    if due_date:
        try:
            due_date = datetime.strptime(due_date, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Setting due date to 'No due date'.")
            due_date = "No due date"
    
    task = {
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'status': status
    }

    if category not in todos:
        todos[category] = []
    todos[category].append(task)
    
    save_todos(todos)
    print(f"Added task: {description}")

def remove_task():
    todos = load_todos()
    display_todo()

    category = input("Enter the category of the task to remove: ").capitalize()
    if category not in todos or not todos[category]:
        print(f"No tasks found in category: {category}")
        return

    task_number = int(input("Enter the task number to remove: "))

    if task_number <= 0 or task_number > len(todos[category]):
        print("Invalid task number!")
    else:
        removed_task = todos[category].pop(task_number - 1)
        if not todos[category]:
            del todos[category]  # Remove the category if it's empty
        save_todos(todos)
        print(f"Removed task: {removed_task['description']}")

def update_task_status():
    todos = load_todos()
    display_todo()

    category = input("Enter the category of the task to update: ").capitalize()
    if category not in todos or not todos[category]:
        print(f"No tasks found in category: {category}")
        return

    task_number = int(input("Enter the task number to update status: "))

    if task_number <= 0 or task_number > len(todos[category]):
        print("Invalid task number!")
    else:
        new_status = input("Enter new status (Pending, In Progress, Completed): ").capitalize()
        todos[category][task_number - 1]['status'] = new_status
        save_todos(todos)
        print(f"Updated task status to: {new_status}")

def display_help():
    print("\nAvailable Commands:")
    print("add/     : Add a new task")
    print("evoke/   : Remove a task")
    print("updt/    : Update a task's status")
    print("show/    : Show the current to-do list")
    print("need/    : Show this help menu")
    print("exit/    : Exit the app")

def main():

    display_todo()

    while True:
        command = input("\nEnter a command (or type 'need/' for help): ").lower().strip()

        if command == 'add/':
            add_task()
        elif command == 'evoke/':
            remove_task()
        elif command == 'updt/':
            update_task_status()
        elif command == 'show/':
            display_todo()
        elif command == 'need/':
            display_help()
        elif command == 'exit/':
            print("Exiting...")
            break
        else:
            print("Invalid command! Type 'need/' for available commands.")

if __name__ == "__main__":
    main()

