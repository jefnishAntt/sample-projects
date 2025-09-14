todo_tasks = [{"task": 'Brush', "due_time": 'due_time', "done": False}, {"task": 'task', "due_time": 'due_time', "done": False}]

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
