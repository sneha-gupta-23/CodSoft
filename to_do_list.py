import json
import os

TODO_FILE = 'todo_list.json'


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    tasks.append({"title": title, "description": description, "completed": False})
    print(f"Task '{title}' added!")


def view_tasks(tasks):
    for index, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['title']} - {task['description']} [{status}]")


def update_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to update: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["title"] = input("Enter the new title: ")
        tasks[task_index]["description"] = input("Enter the new description: ")
        print("Task updated!")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to delete: ")) - 1
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['title']}' deleted!")
    else:
        print("Invalid task number.")


def mark_task_completed(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['title']}' marked as completed!")
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List")
        print("1. Add task")
        print("2. View tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task as completed")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_task_completed(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()