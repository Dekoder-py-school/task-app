MENU_PROMPT = """Choose an option by entering a number:
1. Add a new task
2. List all tasks
3. Check a task off
4. Delete a task
5. Exit
>>> """

def add_task():
    pass

def list_tasks():
    pass

def complete_task():
    pass

def delete_task():
    pass

def main():
    print("Welcome to the Dekoder-py-school to do app!")
    choice = input(MENU_PROMPT)
    while choice != "5":
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        else:
            print("Invalid option.")
        choice = input(MENU_PROMPT)
    print("Thank you for using my to do app!")

if __name__ == "__main__":
    main()