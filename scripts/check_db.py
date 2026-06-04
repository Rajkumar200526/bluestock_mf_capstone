import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
)

tables = cursor.fetchall()

print("Tables Found:")

for table in tables:
    print(table[0])

conn.close()