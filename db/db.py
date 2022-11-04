import sqlite3

connection = sqlite3.connect('img.db', check_same_thread=False)

cursor = connection.cursor()

with sqlite3.connect("img.db") as con:
    cur = con.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS Img (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_file TEXT)""")
