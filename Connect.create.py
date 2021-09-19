import sqlite3

#conect to sqlite3
conn=sqlite3.connect("movies.db")

#creating a cursor
cur=conn.cursor()

#creating a table
cur.execute("""create table Movies( 
    name text, 
    actor text, 
   actress text, 
   director text, 
   year_of_release integer
   )""")

#committing the changes and closing
conn.commit()
conn.close()         
