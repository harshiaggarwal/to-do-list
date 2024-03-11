tasks = []
while True:
    action = input("Type add, show or exit:")
    action = action.strip()
    match action:
        case "add":
            task = input("Enter a task: ")
            tasks.append(task.title())
        case "show":
            for item in tasks:
                print(item)
        case "exit":
            print("Bye!")
            break
