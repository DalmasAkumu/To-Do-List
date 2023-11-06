import sqlite3

def create_connection():
    return sqlite3.connect('tasks.db')

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT
        )
    ''')
    conn.commit()