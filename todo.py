todo_tasks = []

def add_task():
    task = input("Enter a new task:")
    due_time = input("When to be done:")
    task_entry = {"task": task, "due_time": due_time, "done": False}
    todo_tasks.append(task_entry)

def view_task():
    if(todo_tasks):
        for i,task in enumerate(todo_tasks, 1):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {task['task']} in {task['due_time']} {status}")
    else:
        print("No Tasks Planed Yet")

def mark_done():
    task_no = int(input("Enter the Task Number to mark Done"))-1
    if 0 <= task_no < len(todo_tasks):
        todo_tasks[task_no]['done'] = True
        print("Task no marked as done!")
    else:
        print("Invalid Task no")

def remove_task():
    task_no = int(input("Enter the Task no"))-1
    if 0 <= task_no < len(todo_tasks):
        removed_task = todo_tasks.pop(task_no)
        print(f"{removed_task['task']} removed successfully!")
    else:
        print("Invalid Task no")


def menu():
    while True:
        print("\n--- To-Do App ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")
        choice = int(input("Choose an option: "))

        match choice:
            case 1: add_task()
            case 2: view_task()
            case 3: mark_done()
            case 4: remove_task()
            case 5: break
            case _: print("Invalid Nunber")

menu()