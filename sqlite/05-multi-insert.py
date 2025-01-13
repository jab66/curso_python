import sqlite3

with sqlite3.connect("sqlite/app.db") as conn:
    cursor = conn.cursor()
    usuarios = [
        (2, "Daniel"), (3, "Roberto"), (4, "Alejandro")
    ]
    cursor.executemany(
        """
        INSERT INTO usuarios VALUES (?,?)
        """, usuarios
    )
