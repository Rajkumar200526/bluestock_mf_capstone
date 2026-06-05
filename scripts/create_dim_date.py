import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

nav = pd.read_csv(
    "data/processed/clean_nav.csv"
)

nav['date'] = pd.to_datetime(
    nav['date']
)

dim_date = pd.DataFrame()

dim_date['date_key'] = nav['date'].drop_duplicates()

dim_date['year'] = dim_date['date_key'].dt.year
dim_date['month'] = dim_date['date_key'].dt.month
dim_date['quarter'] = dim_date['date_key'].dt.quarter

dim_date.to_sql(
    "dim_date",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("dim_date created successfully")