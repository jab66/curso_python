import sqlite3

with sqlite3.connect("sqlite/app.db") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO usuarios VALUES (?,?)
        """, (1, "Jorge")
    )
