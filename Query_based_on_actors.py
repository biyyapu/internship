import sqlite3

#conect to sqlite3
conn=sqlite3.connect("movies.db")

#creating a cursor
cur=conn.cursor()

#selecting based on actor 
cur.execute("select * from Movies where actor ='prabhas' ")
print(cur.fetchall())

conn.close()
