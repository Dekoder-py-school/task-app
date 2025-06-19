import sqlite3
import time
import argparse

try:
    from rich import print
except ImportError:
    print("ERROR: RICH LIBRARY NOT FOUND.\n\nPlease install the dependencies with pip.\n  pip install -r requirements.txt")
    quit()

parser = argparse.ArgumentParser(description="Simple To Do List CLI App")
parser.add_argument('--list', '-l', default='tasks', help='Name of the task list (default: tasks)')
args = parser.parse_args()
database = args.list + ".sqlite"
database = database.lower().strip()

MENU_PROMPT = f"""Current list: [bold purple]{args.list.title()}[/bold purple]
Choose an option by entering a number:
1. [magenta]Add a new task[/magenta]
2. [blue]List all tasks[/blue]
3. [green]Check a task off[/green]
4. [red]Delete a task[/red]
5. [yellow]Exit[/yellow]
"""

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
    all_complete = all(task[2] for task in tasks)
    if not all_complete:
        for task in tasks:
            status = "[green][X][/green]" if task[2] else "[ ]"
            print(f"\n\n{task[0]}. {status} {task[1]}\n")
    elif len(tasks):
        print("[bold green]All tasks complete.[/bold green]")
        for task in tasks:
            status = "[green][X][/green]" if task[2] else "[ ]"
            print(f"\n\n{task[0]}. {status} {task[1]}\n")
    else:
        print("\n[bold yellow]No tasks found.[/bold yellow]\n")


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
    print("\n[red]WARNING: THIS CANNOT BE UNDONE![/red]")
    confirm = input(f"Are you sure you want to delete {task[0]} task? (y/n): ").lower().strip()
    if confirm in ["y", "n"]:
        if confirm == "y":
            cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            cursor.connection.commit()
            print(f"\n[red]Task '{task[0]}' deleted successfully![/red]\n")
            list_tasks(cursor)
        else:
            print("\n[yellow]Task deletion cancelled.[/yellow]\n")
    else:
        print("\n[red]Invalid input. Please enter 'y' or 'n'.[/red]\n")
        delete_task(cursor, task_id_str)

def main():
    con = sqlite3.connect(database)
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks(id INTEGER PRIMARY KEY, task TEXT, completed BOOLEAN DEFAULT 0)")
    print("Welcome to the Dekoder-py-school to do app!")
    print(MENU_PROMPT)
    choice = input(">>> ").strip()
    while choice != "5":
        if choice == "1":
            task = input("Enter the task: ")
            add_task(cursor, task)
        elif choice == "2":
            list_tasks(cursor)
        elif choice == "3":
            tasks = cursor.execute("SELECT * FROM tasks").fetchall()
            all_complete = all(task[2] for task in tasks)
            if not all_complete:
                list_tasks(cursor)
                task_id = input("Enter the task number to complete: ")
                complete_task(cursor, task_id)
            else:
                print("\n[bold green]All tasks are already completed![/bold green]\n")
        elif choice == "4":
            list_tasks(cursor)
            task_id = input("Enter the task number to delete: ")
            delete_task(cursor, task_id)
        else:
            print("Invalid option.")
        time.sleep(2)
        print(MENU_PROMPT)
        choice = input(">>> ").strip()
    con.close()
    print("Thank you for using my to do app!")

if __name__ == "__main__":
    main()
