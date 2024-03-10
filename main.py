prompt = "Enter a task to do:"
tasks = []
while True:
    task = input(prompt)
    tasks.append(task.title())
    print(tasks, "Next...")