import sqlite3

conn = sqlite3.connect('books_det.db')
print("Opened database successfully")

conn.execute('CREATE TABLE books (name TEXT, author TEXT, id INTEGER)')
print("Table created successfully")
conn.close()