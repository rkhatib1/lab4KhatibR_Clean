def view_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Current tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    """Delete a task from the to-do list based on its index."""
    if not tasks:
        print("Your to-do list is empty. Nothing to delete.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' has been deleted.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
