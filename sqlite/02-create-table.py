import sqlite3

conn = sqlite3.connect("sqlite/app.db")

cursor = conn.cursor()
cursor.execute(
    """
    CREATE TABLE if not exists usuarios 
    (id INTEGER primary key, nombre VARCHAR(50))
    """
)
conn.commit()

conn.close()
