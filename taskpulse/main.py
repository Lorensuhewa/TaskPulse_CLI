import datetime
import sys

from taskpulse.manager import TaskManager
from taskpulse.utils import prompt_non_empty


def render_task_table(tasks):
    if not tasks:
        print("\n No tasks available.")
        return

    headers = ["ID", "Title", "Description", "Category", "Priority", "Due Date", "Status"]
    row_format = "{:<5} {:<20} {:<30} {:<15} {:<10} {:<12} {:<10}"
    print(row_format.format(*headers))
    print("-" * 110)

    for task in tasks:
        print(row_format.format(
            task.id,
            task.title,
            task.description,
            task.category,
            task.priority,
            task.due_date.strftime("%Y-%m-%d"),
            task.status
        ))

def handle_add(manager: TaskManager):
    print("\n ----- Add New Task -----")
    title = prompt_non_empty("Enter title: ")
    desc = prompt_non_empty("Enter description: ")
    category = prompt_non_empty("Enter category: ")
    priority = prompt_non_empty("Enter priority (High, Medium, Low): ")
    due_date = prompt_non_empty("Enter due date (YYYY-MM-DD): ")

    task = manager.add_task(title, desc, category, priority, due_date)
    print(f"\n Task '{task.title}' added successfully with ID {task.id}.")

def handle_view(manager: TaskManager):
    print("\n ----- View Tasks -----")
    render_task_table(manager.tasks)

def handle_search(manager: TaskManager):
    print("\n ----- Search Tasks -----")
    keyword = prompt_non_empty("Enter keyword to search in title or description: ")
    filtered_tasks = [task for task in manager.tasks if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
    render_task_table(filtered_tasks)

def handle_update(manager: TaskManager):
    print("\n ----- Update Task -----")
    task_id = prompt_non_empty("Enter task ID to update: ")
    task = manager.find_by_id(int(task_id))
    if not task:
        print(f"\n Task with ID {task_id} not found.")
        return

    print(f"\n Updating Task '{task.title}' (ID: {task.id})")
    new_title = input(f"Enter new title [{task.title}]: ").strip() or task.title
    new_desc = input(f"Enter new description [{task.description}]: ").strip() or task.description
    new_category = input(f"Enter new category [{task.category}]: ").strip() or task.category
    new_priority = input(f"Enter new priority (High, Medium, Low) [{task.priority}]: ").strip() or task.priority
    new_due_date = input(f"Enter new due date (YYYY-MM-DD) [{task.due_date.strftime('%Y-%m-%d')}]: ").strip() or task.due_date.strftime('%Y-%m-%d')
    new_status = input(f"Enter new status (Pending, Completed) [{task.status}]: ").strip() or task.status

    # Update the task attributes
    task.title = new_title
    task.description = new_desc
    task.category = new_category
    task.priority = new_priority
    task.due_date = datetime.strptime(new_due_date, "%Y-%m-%d")
    task.status = new_status

    manager.save()
    print(f"\n Task '{task.title}' updated successfully.")

def handle_complete(manager: TaskManager):
    print("\n ----- Mark Task as Completed -----")
    task_id = prompt_non_empty("Enter task ID to mark as completed: ")
    if task_id is None:
        print("\n Invalid task ID.")
        return

    task = manager.find_by_id(int(task_id))
    if not task:
        print(f"\n Task with ID {task_id} not found.")
        return

    confirm = input(f"Are you sure you want to mark task '{task.title}' as completed? (y/n): ").strip().lower()
    if confirm == 'y':
        task.mark_completed()
        manager.save()
        print(f"\n Task '{task.title}' marked as completed.")
    else:
        print("\n Operation cancelled.")

def handle_statistics(manager: TaskManager):
    print("\n ----- Task Statistics -----")
    stats = manager.get_statistics()
    print(f"Total tasks: {stats['total_tasks']}")
    print(f"Completed tasks: {stats['completed_tasks']}")
    print(f"Pending tasks: {stats['pending_tasks']}")
    print("")
    print (f"High priority tasks: {stats['priorities']['High']}")
    print (f"Medium priority tasks: {stats['priorities']['Medium']}")
    print (f"Low priority tasks: {stats['priorities']['Low']}")
    print(" ")
    print(f"Percentage of completed tasks: {stats['completed_percentage']:.2f}%")
    print(" ------------------------------------")

def handle_sort(manager: TaskManager):
    print("\n ----- Sort Tasks -----")
    print("Sort by: 1. Priority 2. Due Date 3. Status")
    choice = input("Enter your choice (1-3): ").strip()
    criterion_map = {"1": "priority", "2": "due_date", "3": "status"}
    criterion = criterion_map.get(choice)
    if not criterion:
        print("\n Invalid choice.")
        return
    sorted_tasks = manager.sort_tasks(criterion)
    render_task_table(sorted_tasks)

def main():
    manager = TaskManager()

    while True:
        print("\n ----- Task Manager -----")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Search Tasks")
        print("4. Update Task")
        print("5. Mark Task as Completed")
        print("6. View Statistics")
        print("7. Sort Tasks")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            handle_add(manager)
        elif choice == "2":
            handle_view(manager)
        elif choice == "3":
            handle_search(manager)
        elif choice == "4":
            handle_update(manager)
        elif choice == "5":
            handle_complete(manager)
        elif choice == "6":
            handle_statistics(manager)
        elif choice == "7":
            handle_sort(manager)
        elif choice == "8":
            print("\n Exiting Task Manager. Goodbye!")
            sys.exit(0)
        else:
            print("\n Invalid choice. Please try again.")

if __name__ == "__main__":
    main()