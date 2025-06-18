MENU_PROMPT = """Choose an option by entering a number:
1. Add a new task
2. List all tasks
3. Check a task off
4. Delete a task
5. Exit
>>> """

"""
Tasks will be stored in a sql database in this format:
id - also used as the number for selecting a task to delete / check off
task - task
completed - boolean (if the task is completed)

displayed when listed like this:
1. [X] Walk the dog
2. [ ] Buy dog food
"""


def add_task(task):
    pass

def list_tasks():
    pass

def complete_task(task_id):
    pass

def delete_task(task_id):
    pass

def main():
    print("Welcome to the Dekoder-py-school to do app!")
    choice = input(MENU_PROMPT)
    while choice != "5":
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            list_tasks()
            task_id = input("Enter the task number to complete: ") # TODO: convert to int with error handling
            complete_task(task_id)
        elif choice == "4":
            list_tasks()
            task_id = input("Enter the task number to complete: ")  # TODO: convert to int with error handling
            delete_task(task_id)
        else:
            print("Invalid option.")
        choice = input(MENU_PROMPT)
    print("Thank you for using my to do app!")

if __name__ == "__main__":
    main()