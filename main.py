import sqlite3
try:
    from rich import print
except ImportError:
    print("ERROR: RICH LIBRARY NOT FOUND.\n\nPlease install the dependancies with pip.\n  pip install -r requirements.txt")
    quit()



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


def add_task(cursor, task):
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    cursor.connection.commit()
    list_tasks(cursor)

def list_tasks(cursor):
    tasks = cursor.execute("SELECT id, task, completed FROM tasks").fetchall()
    for task in tasks:
        status = "[green][X][/green]" if task[2] else "[ ]"
        print(f"\n\n{task[0]}. {status} {task[1]}\n")

def complete_task(cursor, task_id_str):
    try:
        task_id = int(task_id_str)
    except ValueError:
        print("\n[red]Invalid number. Please enter a valid integer.[/red]\n")
        return
    task = cursor.execute("SELECT task FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if not task:
        print("\n[yellow]Task not found.[/yellow]\n")
        return
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    cursor.connection.commit()
    list_tasks(cursor)

def delete_task(cursor, task_id_str):
    try:
        task_id = int(task_id_str)
    except ValueError:
        print("\n[red]Invalid number. Please enter a valid integer.[/red]\n")
        return
    task = cursor.execute("SELECT task FROM tasks WHERE id = ?", (task_id,)).fetchone()
    if not task:
        print("\n[yellow]Task not found.[/yellow]\n")
        return
    confirm = input(f"Are you sure you want to delete {task[0]} task? (y/n): ")
    if confirm.lower() == "y":
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        cursor.connection.commit()
        list_tasks(cursor)

def main():
    con = sqlite3.connect("tasks.sqlite")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, task TEXT, completed BOOLEAN DEFAULT 0)")
    print("Welcome to the Dekoder-py-school to do app!")
    choice = input(MENU_PROMPT)
    while choice != "5":
        if choice == "1":
            task = input("Enter the task: ")
            add_task(cursor, task)
        elif choice == "2":
            list_tasks(cursor)
        elif choice == "3":
            list_tasks(cursor)
            task_id = input("Enter the task number to complete: ")
            complete_task(cursor, task_id)
        elif choice == "4":
            list_tasks(cursor)
            task_id = input("Enter the task number to delete: ")
            delete_task(cursor, task_id)
        else:
            print("Invalid option.")
        choice = input(MENU_PROMPT)
    con.close()
    print("Thank you for using my to do app!")

if __name__ == "__main__":
    main()
