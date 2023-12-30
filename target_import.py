import sqlite3
import os

files  = os.listdir('data')
con = sqlite3.connect("target.sqlite")
cur = con.cursor()
for file in files:
    cur.execute("INSERT INTO target (file_name) VALUES(?)", (file,) )
con.commit()





