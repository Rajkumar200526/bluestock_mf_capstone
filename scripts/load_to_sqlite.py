import sqlite3
import pandas as pd

print("Connecting Database...")

conn = sqlite3.connect(
    "data/db/bluestock_mf.db"
)

print("Loading Files...")

fund = pd.read_csv(
    "data/raw/01_fund_master.csv",
    encoding="latin1"
)

nav = pd.read_csv(
    "data/processed/clean_nav.csv"
)

transactions = pd.read_csv(
    "data/processed/clean_transactions.csv"
)

performance = pd.read_csv(
    "data/processed/clean_performance.csv"
)

print("Saving Tables...")

fund.to_sql(
    "dim_fund",
    conn,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    conn,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    conn,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database Created Successfully!")