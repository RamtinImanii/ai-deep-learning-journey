# In-memory data
tasks = []
next_task_id = 1


# Functions
# -----------------------------------


def show_menu():
    """Display the main menu."""

    menu = """================================
       DAILY TASK TRACKER
================================

1. Dashboard
2. Show Today's Tasks
3. Add Task
4. Complete Task
5. Exit

"""
    print(menu)


# -----------------------------------


def dashboard():
    """Display task statistics."""

    print("-" * 20, "\nDashboard\n", "-" * 20, sep="")

    if not tasks:
        print("No tasks yet.")
        return

    completed_tasks = [task for task in tasks if task["status"] == "Done"]
    pending_tasks = [task for task in tasks if task["status"] == "Pending"]

    total_count = len(tasks)
    completed_count = len(completed_tasks)
    pending_count = len(pending_tasks)

    percentage = completed_count / total_count * 100

    print(f"Total tasks: {total_count}")
    print(f"Completed tasks: {completed_count}")
    print(f"Pending tasks: {pending_count}")
    print(f"Completion rate: {percentage:.1f}%")


# -----------------------------------


def show_tasks():
    """Display all tasks for today."""

    print("-" * 20, "\nToday's Tasks\n", "-" * 20, sep="")

    if not tasks:
        print("No tasks yet.")
        return

    for task in tasks:
        print(f'[{task["id"]}] {task["title"]} - {task["status"]}')


# -----------------------------------


def add_task():
    """Add a new task to the task list."""

    global next_task_id

    print("-" * 20, "\nAdd a Task\n", "-" * 20, sep="")

    title = input("Enter task title: ").strip()

    while not title:
        print("Task title cannot be empty.")
        title = input("Enter task title: ").strip()

    task = {"id": next_task_id, "title": title, "status": "Pending"}

    tasks.append(task)
    next_task_id += 1

    print(f'Task "{title}" added successfully.')


# -----------------------------------


def complete_task():
    """Mark a task as completed using its ID."""

    print("-" * 20, "\nComplete a Task\n", "-" * 20, sep="")

    while True:
        task_id_input = input("Enter task ID: ").strip()

        if task_id_input.isdigit() and int(task_id_input) > 0:
            task_id = int(task_id_input)
            break

        print("Invalid ID. Please enter a positive integer.")

    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "Done":
                print("This task is already marked as done.")
            else:
                task["status"] = "Done"
                print(f"Task {task_id} marked as done.")
            return

    print(f"No task found with ID {task_id}.")


# -----------------------------------
# Main program


while True:
    show_menu()
    option = input("Choose an option: ").strip()

    if option == "1":
        dashboard()

    elif option == "2":
        show_tasks()

    elif option == "3":
        add_task()

    elif option == "4":
        complete_task()

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
