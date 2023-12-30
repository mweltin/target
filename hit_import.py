import csv
import sqlite3

with open('hit.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    hits = [row for row in csv_reader]

con = sqlite3.connect("target.sqlite")
cur = con.cursor()

for hit in hits:
    rowid = cur.execute("select rowid from target where file_name = ?", (hit['img'],) )
    rowid = rowid.fetchone()[0]
    cur.execute("insert into hit (x, y, target_id) values (?,?,?)", (hit['x'], hit['y'], rowid,))

con.commit()