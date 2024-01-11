import sqlite3
import os

files  = os.listdir('raw_data')
con = sqlite3.connect("target.sqlite")
cur = con.cursor()
cur.execute("CREATE TABLE target ( file_name VARCHAR(255) NOT NULL UNIQUE);")
cur.execute("CREATE TABLE hit (x INTEGER not null, y integer not null, target_id integer not null, FOREIGN KEY(target_id) REFERENCES target(ROWID))")
cur.execute("CREATE UNIQUE INDEX i1 ON hit(x, y, target_id);")