import sqlite3
import pandas as pd
path           = 'data/'
data           = 'dfcompras.csv'
df             = pd.read_csv(path + data, encoding="utf-8", dtype=str)
df['compra']   = df['compra'].astype(str)
df['processo'] = df['processo'].astype(str)

cod = 1

sql = "insert into posts_compra (codigo, compra, processo , data_publicacao, valor_estimado, "
sql = sql + " valor_min, valor_medio, valor_max)"
sql = sql + " values "

for index, row in df.iterrows():
    l = "(" + (str(cod) + ", '" + row['compra']) + "','" + (row['processo']) + "', '"
    l = l + (row['data_publicacao']) + "', " + (row['valor_estimado']) + ",0,0,0);"
    print(sql + l)
    cod = cod + 1
