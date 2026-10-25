
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task added: {task}")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        for number, task in enumerate(tasks, start=1):
            print(f"{number}. {task}")

add_task("Learn Git and GitHub")
add_task("Learn FastAPI")
show_tasks()
