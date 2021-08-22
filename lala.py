import sqlite3
conector=sqlite3.connect("test.db")
cursor=conector.cursor()

def eliminartodo(cursor,con):
    cursor.execute("DELETE FROM Item")
    con.commit()

eliminartodo(cursor,conector)

for row in cursor.execute("SELECT * FROM Item"):
   print(row)