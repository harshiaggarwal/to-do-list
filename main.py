# reads user input and performs action
while True:
    action = input("Type add, edit, show, complete or exit: ")

    # removing trailing spaces
    action = action.strip()

    match action:
    
        # to read tasks from the file and add tasks
        case "add":
            task = input("Enter a task: ") + "\n"

            file = open("tasks.txt", "r")
            tasks = file.readlines()
            file.close()
            
            tasks.append(task.title())
            
            file = open("tasks.txt", "r")
            file.writelines(tasks)
            file.close()
    
        # to edit the tasks
        case "edit":
            number = input("Enter a task number to edit: ")
            current_task = tasks[int(number) - 1]
            print(current_task)
            new_task = input("Enter the new task: ")
            tasks[int(number) - 1] = new_task.title()

        # to display the list
        case "show" | "display":
            file = open("tasks.txt", "r")
            tasks = file.readlines()
            file.close()
            
            for index, item in enumerate(tasks):
                print(f"{index + 1}-{item}")

        # to complete a task
        case "complete":
            file = open("tasks.txt", "r")
            tasks = file.readlines()
            file.close()

            number = input("Enter a task number to mark complete: ")
            tasks.pop(int(number) - 1)

            file = open("tasks.txt", "w")
            file.writelines(tasks)
            file.close()           

        # to exit when done
        case "exit":
            print("Bye!")
            break

        case _:
            print("Choose a correct option!")
