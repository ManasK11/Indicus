import sqlite3 as sql

con=sql.connect("books_det.db")
cur = con.cursor()
cur.execute("INSERT INTO books (name,author,id) VALUES (?,?,?)",('David Copperfield','Charles Dickens','1') )
cur.execute("INSERT INTO books (name,author,id) VALUES (?,?,?)",('The Alchemist','Paolo Coelho','2') )
cur.execute("INSERT INTO books (name,author,id) VALUES (?,?,?)",('Oliver Twist','Charles Dickens','3') )

con.commit()