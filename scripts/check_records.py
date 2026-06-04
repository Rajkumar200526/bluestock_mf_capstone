import sqlite3

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

cursor = conn.cursor()

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance"
]

for table in tables:

    query = f"SELECT COUNT(*) FROM {table}"

    cursor.execute(query)

    count = cursor.fetchone()[0]

    print(table, ":", count)

conn.close()