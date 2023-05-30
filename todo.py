# using ANSI escape codes to colorize the output text on some of the messages
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

# todo_list_app() will run the to-do list application
def todo_list_app():
    # load the list from the file
    todo_list = load_saved_tasks()
    
    # loop until the user chooses to quit
    while True:
        # display the menu from the show_menu() function
        show_menu()
        # prompt the user to enter a choice
        choice = input("Enter your choice: ")
        
        # check the user's choice and call the appropriate function
        if choice == "1":
            add_task(todo_list)
        elif choice == "2":
            view_tasks(todo_list)
        elif choice == "3":
            mark_complete(todo_list)
        elif choice == "4":
            remove_task(todo_list)
        elif choice == "5":
            save_tasks(todo_list)
            break
        else:
            print("Invalid choice. Please try again.")


# load_saved_tasks() will load the list from the file if it exists
def load_saved_tasks():
    # create an empty list to store the tasks
    todo_list = []
    # try to open the file in read mode
    try:
        with open("todo.txt", "r") as file:
            for line in file:
                # strip the newline character from the end of the line
                task = line.strip()
                # add the task to the todo_list
                todo_list.append(task)
        print("To-Do list loaded from 'todo.txt'.")
    # if the file doesn't exist, print a message to the user
    except FileNotFoundError:
        print("No saved to-do list found.")
    # return the todo_list
    return todo_list


# first I need to create a menu that will be displayed to the user to give them options
def show_menu():
    print(" ")
    print("=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Remove Task")
    print("5. Save and Quit")


# add_task() will prompt the user to enter a new task and add it to the list
def add_task(todo_list):
    # prompt the user to enter a new task
    task = input("Enter a new task: ")
    # add the new task to the todo_list
    todo_list.append(task)
    print("Task added!")


# view_tasks() will display all of the tasks in the list
def view_tasks(todo_list):
    print("\nTasks:")
    # loop through the todo_list and print each task with a number in front of it 
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")


# mark_complete() will prompt the user to enter the number of the task they want to mark as complete
def mark_complete(todo_list):
    # display the tasks available to mark as complete
    view_tasks(todo_list)
    # prompt the user to enter the number of the task they want to mark as complete; subtract 1 from the number entered to get the "real" index of the task in the list
    task_index = int(input("Enter the task number to mark as complete: ")) - 1
    # check if the task number entered is valid
    if 0 <= task_index < len(todo_list):
        print(f"Marked task '{todo_list[task_index]}' as {GREEN}complete!{RESET}")
        todo_list.pop(task_index)
    # if the task number entered is not valid, print an error message
    else:
        print("Invalid task number!")


# remove_task() will prompt the user to enter the number of the task they want to remove
def remove_task(todo_list):
    # display the tasks available to remove
    view_tasks(todo_list)
    # prompt the user to enter the number of the task they want to remove; subtract 1 from the number entered to get the "real" index of the task in the list
    task_index = int(input("Enter the task number to remove: ")) - 1
    # check if the task number entered is valid
    if 0 <= task_index < len(todo_list):
        print(f"{RED}Removed task{RESET} '{todo_list[task_index]}'!")
        # remove the task from the list
        todo_list.pop(task_index)
    # if the task number entered is not valid, print an error message
    else:
        print("Invalid task number!")



# prior to being saved the todo_list is stored in the computer's memory, and will be lost when the program ends; 
# save_tasks() will save the list to a file so it can be loaded the next time the program is run
def save_tasks(todo_list):
    # open the file in write mode; if the file doesn't exist, it will be created
    with open("todo.txt", "w") as file:
        # loop through the todo_list and write each task to the file
        for task in todo_list:
            file.write(task + "\n")
    # print a message to the user to let them know the list was saved
    print("To-Do list saved to 'todo.txt'. Goodbye!")

# run the todo_list_app() function
todo_list_app()