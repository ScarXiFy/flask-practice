import sqlite3

DATABASE = "projects.db"

def get_connection():
    return sqlite3.connect(DATABASE)

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()