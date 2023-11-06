
from .database import create_connection

def add_task():
    # This function adds new tasks to the to-do list
    conn = create_connection()
    task = input("Add a new task: ")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    conn.close()
    print("Task is added to the list successfully.")

def display_task():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, task FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    if len(tasks) == 0:
        print("No tasks to display.")
    else:
        print('Tasks:')
        for task in tasks:
            print(f'{task[0]}. {task[1]}')
        choice = int(input('Enter the task number to delete: '))

        if 0 < choice <= len(tasks):
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tasks WHERE id=?", (choice,))
            conn.commit()
            conn.close()
            print('Task deleted successfully.')
        else:
            print('Invalid task number')

def delete_task():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, task FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    if len(tasks) == 0:
        print("No tasks to delete.")
    else:
        print("List of Tasks to Delete:")
        for task in tasks:
            print(f'{task[0]}. {task[1]}')
