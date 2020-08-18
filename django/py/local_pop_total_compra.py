import sqlite3
try:
    con = sqlite3.connect('db.sqlite3')
    print("Successfully Connected to SQLite")
    cursor = con.cursor()
    cmd  = "INSERT INTO posts_totalcompra (valor_min, valor_medio, valor_max) VALUES (267,2248164.93,30234118.00)"
    cursor.execute(cmd);
    print(cmd)
    con.commit()

finally:
    if (con):
        con.close()
        print("The SQLite connection is closed")
