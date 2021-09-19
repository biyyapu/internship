import sqlite3

#conect to sqlite3
conn=sqlite3.connect("movies.db")

#creating a cursor
cur=conn.cursor()

# inserting multiple movies details
moviesList= [('AA','Nithin','samantha','Trivikram',2018),
             ('Murari','Mahesh Babu','sonali bindre','krishna Vamsi',2001),
             ('Mirchi','prabhas','Anushka Shetty','Koratala Siva',2015)]

cur.executemany("insert into Movies values(?,?,?,?,?)",moviesList)

#committing the changes and closing
conn.commit()
conn.close()         
