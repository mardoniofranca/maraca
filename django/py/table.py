table = "posts_compra"

import sqlite3
try:
    con = sqlite3.connect('db.sqlite3')
    print("Successfully Connected to SQLite")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM " + table )
    rows = cursor.fetchall()
    for row in rows:
            print(row)
finally:
    if (con):
        con.close()
        print("The SQLite connection is closed")
