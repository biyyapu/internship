import sqlite3

#conect to sqlite3
conn=sqlite3.connect("movies.db")

#creating a cursor
cur=conn.cursor()

# inserting multiple movies details
moviesList= [('I','Vikram','Amy Jackson','Shankar',2015),
             ('Master','Vijay','Malavika Mohanan','Lokesh Kanagaraj',2021),
             ('Singam 3','Surya','Anushka Shetty','Hari',2017)]

cur.executemany("insert into Movies values(?,?,?,?,?)",moviesList)

#committing the changes and closing
conn.commit()
conn.close()         
