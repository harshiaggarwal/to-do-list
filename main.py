tasks = []
while True:
    action = input("Type add, show or exit:")
    match action:
        case "add":
            task = input("Enter a task: ")
            tasks.append(task.title())
        case "show":
            print(tasks)
        case "exit":
            print("Bye!")
            break
