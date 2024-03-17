tasks = []

# reads user input and performs action
while True:
    action = input("Type add, edit, show, complete or exit: ")

    # removing trailing spaces
    action = action.strip()

    match action:
        # to add a task in the list and change it to title case
        case "add":
            task = input("Enter a task: ")
            tasks.append(task.title())

        # to edit the tasks
        case "edit":
            number = input("Enter a task number to edit: ")
            current_task = tasks[int(number) - 1]
            print(current_task)
            new_task = input("Enter the new task: ")
            tasks[int(number) - 1] = new_task.title()

        # to display the list
        case "show" | "display":
            for index, item in enumerate(tasks):
                print(f"{index + 1}-{item}")

        # to complete a task
        case "complete":
            number = input("Enter a task number to mark complete: ")
            tasks.pop(int(number) - 1)            

        # to exit when done
        case "exit":
            print("Bye!")
            break

        case _:
            print("Choose a correct option!")
