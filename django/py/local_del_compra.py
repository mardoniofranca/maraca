import sqlite3
import pandas as pd
path           = 'data/'
data           = 'dfcompras.csv'
df             = pd.read_csv(path + data, encoding="utf-8", dtype=str)
df['compra']   = df['compra'].astype(str)
df['processo'] = df['processo'].astype(str)

cod = 1

sql = "delete from posts_compra"

try:
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()
    cursor.execute(sql);
    con.commit()
    cod = cod + 1
finally:
    if (con):
        con.close()
        print("The SQLite connection is closed")
