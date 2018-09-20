import sqlite3 as sqlt

conn = sqlt.connect("example.db")

c = conn.cursor()
