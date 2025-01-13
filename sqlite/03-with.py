import sqlite3

with sqlite3.connect("sqlite/app.db") as conn:

    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists roles 
        (id INTEGER primary key, nombre_role VARCHAR(50))
        """
    )
