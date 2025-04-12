def mark_complete(tasks, index):
    """Mark a task as complete by index"""
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        print("Task marked complete!")
    else:
        print("Invalid task number.")
