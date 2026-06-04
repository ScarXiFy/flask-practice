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

def add_project(name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO projects (name) VALUES (?)",
        (name,)
    )

    connection.commit()
    connection.close()

def get_projects():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT id, name FROM projects")
    projects = cursor.fetchall()

    connection.close()

    return projects

def delete_project(project_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM projects WHERE id = ?",
        (project_id,)
    )

    connection.commit()
    connection.close()

def update_project(project_id, name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE projects SET name = ? WHERE id = ?",
        (name, project_id)
    )

    connection.commit()
    connection.close()
    