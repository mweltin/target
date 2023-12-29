import sqlite3
import os

files  = os.listdir('data')
con = sqlite3.connect("target.sqlite")
cur = con.cursor()
cur.execute("CREATE TABLE target ( file_name VARCHAR(255) NOT NULL UNIQUE);")
cur.execute("CREATE TABLE hit (x INTEGER not null, y integer not null, target_id integer not null, FOREIGN KEY(target_id) REFERENCES target(ROWID))")
cur.execute("CREATE UNIQUE INDEX i1 ON hit(x, y, target_id);")
for file in files:
    cur.execute("INSERT INTO target (file_name) VALUES(?)", (file,) )
con.commit()





