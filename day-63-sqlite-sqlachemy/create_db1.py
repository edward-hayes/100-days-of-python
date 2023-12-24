import sqlite3

db = sqlite3.connect("test-db1.db")
cursor = db.cursor()
sql = f"CREATE TABLE movies (id INTEGER PRIMARY KEY, title NOT NULL, director)"
cursor.execute(sql)