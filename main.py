tasks = []

#reads user input and performs action
while True:
    action = input("Type add, show or exit:")
    
    #removing trailing spaces
    action = action.strip()
    
    match action:
        #to add a task in the list and change it to title case
        case "add":
            task = input("Enter a task: ")
            tasks.append(task.title())
        
        #to display the list    
        case "show":
            for item in tasks:
                print(item)

        #to exit when done
        case "exit":
            print("Bye!")
            break
