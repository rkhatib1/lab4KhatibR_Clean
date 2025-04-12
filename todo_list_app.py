def mark_complete(tasks, index):
    """Mark a task as complete by index"""
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked complete!")
    else:
        print("Invalid task number.")

def add_task(tasks):
    """Add a new task to the to-do list with a priority."""
    task = input("Enter a new task: ")
    priority = input("Enter priority (High/Medium/Low): ")
    priority = priority.capitalize()
    
    # You might store tasks as dictionaries for clarity
    new_task = {"title": task, "priority": priority, "completed": False}
    tasks.append(new_task)
    
    print(f"Task '{task}' added with priority '{priority}'!")
